from scipy.sparse import lil_matrix, csr_matrix
from scipy.sparse.linalg import spsolve
import xlrd as xlrd
import xlwt as xlwt
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt


# 一个结构为一个类
# 结构类的属性有：
# 字典属性：             对应的方法：
# 节点，                   载入节点
# 材料，                   载入材料
# 截面，                   载入截面
# 单元，                   载入单元
# 节点力，                  载入节点力
# 分布力，                  载入分布力
# 边界条件（第一类）         载入边界条件

# 矩阵属性：             对应有方法
# 整体刚度矩阵，           得到整体刚度矩阵（直接刚度法，对号入座组装）
# 节点力向量                 得到节点力向量（等效节点力处理）

# 结果属性：节点位移向量
# 计算的主方法：加边界条件（0-1化处理），求解线性方程组（solve）,结果输出到excel（output）

class Structure(object):
    def __init__(self):
        self.node = {}
        self.material = {}
        self.cross_section = {}
        self.element = {}
        self.concentrated_force = {}
        self.distributed_load = {}
        self.boundary_conditions = {}
        self.global_k = []
        self.global_force = []
        self.node_displacement = []
        self.load_in_node()
        self.load_in_material()
        self.load_in_cross_section()
        self.load_in_element()
        self.load_in_concentrated_force()
        self.load_in_distributed_load()
        self.load_in_boundary_conditions()
        self.get_global_k()
        self.get_global_force()
        self.add_boundary_conditions()

    def load_in_node(self):
        data = xlrd.open_workbook('structure_model.xlsx')
        table = data.sheet_by_name('node')
        for i in range(table.nrows):
            data_list = []
            data_list.extend(table.row_values(i))
            nodenum = int(data_list[0])
            n = Node(nodenum, data_list[1], data_list[2])
            self.node[nodenum] = n

    def load_in_material(self):
        data = xlrd.open_workbook('structure_model.xlsx')
        table = data.sheet_by_name('material')
        for i in range(table.nrows):
            data_list = []
            data_list.extend(table.row_values(i))
            materialnum = int(data_list[0])
            m = Material(data_list[1])
            self.material[materialnum] = m

    def load_in_cross_section(self):
        data = xlrd.open_workbook('structure_model.xlsx')
        table = data.sheet_by_name('cross_section')
        for i in range(table.nrows):
            data_list = []
            data_list.extend(table.row_values(i))
            csnum = int(data_list[0])
            i = data_list[1]
            a = data_list[2]
            cs = CrossSection(i, a)
            self.cross_section[csnum] = cs

    def load_in_element(self):
        data = xlrd.open_workbook('structure_model.xlsx')
        table = data.sheet_by_name('element')
        for i in range(table.nrows):
            data_list = []
            data_list.extend(table.row_values(i))
            elemun = int(data_list[0])
            n1num = int(data_list[1])
            n2num = int(data_list[2])
            materialnum = int(data_list[3])
            csnum = int(data_list[4])
            ele = Element(self.node[n1num], self.node[n2num], self.material[materialnum], self.cross_section[csnum])
            self.element[elemun] = ele

    def load_in_concentrated_force(self):
        data = xlrd.open_workbook('structure_model.xlsx')
        table = data.sheet_by_name('concentrated_force')
        for i in range(table.nrows):
            data_list = []
            data_list.extend(table.row_values(i))
            num = int(data_list[0])
            n = int(data_list[1])
            d = int(data_list[2])
            v = data_list[3]
            cf = ConcentratedForce(n, d, v)
            self.concentrated_force[num] = cf

    def load_in_distributed_load(self):
        data = xlrd.open_workbook('structure_model.xlsx')
        table = data.sheet_by_name('distributed_load')
        for i in range(table.nrows):
            data_list = []
            data_list.extend(table.row_values(i))
            elenum = int(data_list[0])
            p1 = data_list[1]
            p2 = data_list[2]
            t = int(data_list[3])
            # 均布力既储存在了总的结构属性中，又储存在每个单元的属性中，不太好，浪费，容易混淆
            self.distributed_load[elenum] = DistributedLoad(p1, p2, t)
            self.element[elenum].distributed_load = DistributedLoad(p1, p2, t)

    def load_in_boundary_conditions(self):
        data = xlrd.open_workbook('structure_model.xlsx')
        table = data.sheet_by_name('boundary_conditions')
        for i in range(table.nrows):
            data_list = []
            data_list.extend(table.row_values(i))
            num = int(data_list[0])
            n = int(data_list[1])
            d = int(data_list[2])
            v = data_list[3]
            self.boundary_conditions[num] = BoundaryConditions(n, d, v)

    def get_global_k(self):
        self.global_k = lil_matrix((3 * len(self.node), 3 * len(self.node)))
        for key in self.element:
            for i in [1, 2]:
                for j in [1, 2]:
                    for p in [1, 2, 3]:
                        for q in [1, 2, 3]:
                            em = (i - 1) * 3 + p
                            en = (j - 1) * 3 + q
                            if i == 1:
                                gm = (self.element[key].n1.num - 1) * 3 + p
                            else:
                                gm = (self.element[key].n2.num - 1) * 3 + p
                            if j == 1:
                                gn = (self.element[key].n1.num - 1) * 3 + q
                            else:
                                gn = (self.element[key].n2.num - 1) * 3 + q
                            new = self.element[key].gk[em - 1, en - 1]
                            self.global_k[gm - 1, gn - 1] += new

    # 均布力的处理在形成总刚度矩阵时处理，而不是在单元里面处理
    # 用到了总结构里的均布力存储，没用到各个单元里的存储
    def get_global_force(self):
        self.global_force = lil_matrix((3 * len(self.node), 1))
        for key in self.concentrated_force:
            n = 3 * (self.concentrated_force[key].node_num - 1) + self.concentrated_force[key].degree_of_freedom
            self.global_force[n - 1, 0] = self.concentrated_force[key].value
        for key in self.distributed_load:
            l = self.element[key].l
            n1num = self.element[key].n1.num
            n2num = self.element[key].n2.num
            t = self.distributed_load[key].loadtype
            p1 = self.distributed_load[key].p1
            p2 = self.distributed_load[key].p2
            f1 = 0
            f2 = 0
            m1 = 0
            m2 = 0
            # 线性横向均布力的等效节点力公式：可用力法推导出来，但计算量特别大
            # 弯矩逆时针为正
            if t == 1:
                f1 = (7 * p1 + 3 * p2) * l / 20
                m1 = (3 * p1 + 2 * p2) * pow(l, 2) / 60
                f2 = (3 * p1 + 7 * p2) * l / 20
                m2 = -(2 * p1 + 3 * p2) * pow(l, 2) / 60
            elif t == 2:
                pass
            n = 3 * (n1num - 1) + 2
            self.global_force[n - 1, 0] += f1
            n = 3 * (n1num - 1) + 3
            self.global_force[n - 1, 0] += m1
            n = 3 * (n2num - 1) + 2
            self.global_force[n - 1, 0] += f2
            n = 3 * (n2num - 1) + 3
            self.global_force[n - 1, 0] += m2

    def add_boundary_conditions(self):
        # 若要考虑支座位移，要对力向量做出改动
        # self.global_force[:] -= v*self.global_k[:, m]
        # 上式可通用于第一类约束和支座位移
        for key in self.boundary_conditions:
            n = self.boundary_conditions[key].node_num
            d = self.boundary_conditions[key].degree_of_freedom
            v = self.boundary_conditions[key].value
            m = 3 * (n - 1) + d - 1
            self.global_force[m] = v
            self.global_k[:, m] = 0
            self.global_k[m, :] = 0
            self.global_k[m, m] = 1

    def solve(self):
        gk = csr_matrix(self.global_k)
        gf = csr_matrix(self.global_force)
        self.node_displacement = spsolve(gk, gf)

    def output_load(self):
        data = xlwt.Workbook()
        table = data.add_sheet('element_node_force')
        for key in self.element:
            self.element[key].cal_node_dis(self)
            self.element[key].cal_node_force(self)
            table.write(key - 1, 0, key)
            for i in range(6):
                value = self.element[key].ele_node_force[i, 0]
                table.write(key - 1, i + 1, value)
        data.save('result_load.xls')

    def output_node_dis(self):
        data = xlwt.Workbook()
        table = data.add_sheet('element_node_dis')
        n=len(self.node)
        for key in self.node:
            table.write(key - 1, 0, key)
            for i in range(n):
                value = self.node_displacement[i,0]
                table.write(key - 1, i + 1, value)
        data.save('result_node_dis.xls')

    def post_processor(self):
        for key in self.element:
            x1 = self.element[key].n1.x
            y1 = self.element[key].n1.y
            plt.plot(x1, y1, 'ro')
            x2 = self.element[key].n2.x
            y2 = self.element[key].n2.y
            plt.plot(x2, y2, 'ro')
            x = [x1, x2]
            y = [y1, y2]
            plt.plot(x, y)
        plt.show()


# 节点类
# 属性：单元号int，x坐标float，y坐标float
class Node(object):
    def __init__(self, num, x, y):
        self.num = num
        self.x = x
        self.y = y


# 材料类
# 属性：弹性模量float
class Material(object):
    def __init__(self, elastic_modulus):
        self.elastic_modulus = elastic_modulus


# 截面类
# 属性：惯性矩float
class CrossSection(object):
    def __init__(self, inertia, area):
        self.inertia = inertia
        self.area = area


# 集中力
# 属性：节点号int，自由度号int，值float
class ConcentratedForce(object):
    def __init__(self, node_num, degree_of_freedom, value):
        self.node_num = node_num
        self.degree_of_freedom = degree_of_freedom
        self.value = value


# 线性分布力
# 属性：左端荷载值float，右端荷载值float，荷载类型int
class DistributedLoad(object):
    def __init__(self, p1, p2, loadtype):
        self.p1 = p1
        self.p2 = p2
        self.loadtype = loadtype


# 边界条件
# 属性：节点号int，自由度号int，值float
class BoundaryConditions(object):
    def __init__(self, node_num, degree_of_freedom, value):
        self.node_num = node_num
        self.degree_of_freedom = degree_of_freedom
        self.value = value





# 不同单元的主要区别：单个节点的自由度不同，带来：
# 1.单元刚度矩阵不同，从而总刚度矩阵不同
# 2.位移向量不同
# 3.力向量不同

# 单元类
# 属性：
# i节点Node类，j节点Node类，材料Material类，截面CrossSection类
# 单元长度float
# 局部坐标下的单元刚度矩阵narray，整体坐标下的单元刚度矩阵narray，转换矩阵narray
# 节点位移narray，节点力narray，分布力None
# 方法：
# 得到长度，得到局部坐标单刚，得到转换矩阵，得到整体坐标单刚



# 默认的单元暂时为有轴力的平面梁单元
class Element(object):
    def __init__(self, n1, n2, material, cross_section):
        # 每个节点的自由度默认为3
        self.ndof = 3
        self.n1 = n1
        self.n2 = n2
        self.material = material
        self.cross_section = cross_section
        self.l = 0
        self.ek = np.zeros([self.ndof * 2, self.ndof * 2])
        self.gk = np.zeros([self.ndof * 2, self.ndof * 2])
        self.transform_matrix = np.zeros([self.ndof * 2, self.ndof * 2])
        self.get_l()
        self.get_ek()
        self.get_transform_matrix()
        self.get_gk()
        self.ele_node_dis = np.zeros([self.ndof * 2, 1])
        self.ele_node_force = np.zeros([self.ndof * 2, 1])
        self.distributed_load = None

    def get_l(self):
        xx = pow(self.n1.x - self.n2.x, 2)
        yy = pow(self.n1.y - self.n2.y, 2)
        self.l = sqrt(xx + yy)

    def get_ek(self):
        l = self.l
        e = self.material.elastic_modulus
        a = self.cross_section.area
        i = self.cross_section.inertia
        self.ek[0] = [e * a / l, 0, 0, -e * a / l, 0, 0]
        self.ek[1] = [0, 12 * e * i / pow(l, 3), 6 * e * i / pow(l, 2), 0, -12 * e * i / pow(l, 3),
                      6 * e * i / pow(l, 2)]
        self.ek[2] = [0, 6 * e * i / pow(l, 2), 4 * e * i / l, 0, -6 * e * i / pow(l, 2), 2 * e * i / l]
        self.ek[3] = [-e * a / l, 0, 0, e * a / l, 0, 0]
        self.ek[4] = [0, -12 * e * i / pow(l, 3), -6 * e * i / pow(l, 2), 0, 12 * e * i / pow(l, 3),
                      -6 * e * i / pow(l, 2)]
        self.ek[5] = [0, 6 * e * i / pow(l, 2), 2 * e * i / l, 0, -6 * e * i / pow(l, 2), 4 * e * i / l]

    def get_transform_matrix(self):
        c = (self.n2.x - self.n1.x) / self.l
        s = (self.n2.y - self.n1.y) / self.l
        self.transform_matrix[0] = [c, -s, 0, 0, 0, 0]
        self.transform_matrix[1] = [s, c, 0, 0, 0, 0]
        self.transform_matrix[2] = [0, 0, 1, 0, 0, 0]
        self.transform_matrix[3] = [0, 0, 0, c, -s, 0]
        self.transform_matrix[4] = [0, 0, 0, s, c, 0]
        self.transform_matrix[5] = [0, 0, 0, 0, 0, 1]

    def get_gk(self):
        t = np.dot(self.transform_matrix, self.ek)
        self.gk = np.dot(t, np.transpose(self.transform_matrix))

    # 计算局部坐标下单元的节点位移，为计算单元节点力做准备
    def cal_node_dis(self, s):
        if not isinstance(s, Structure):
            raise TypeError('bad operand type')
        m = self.n1.num
        n = self.n2.num
        gm = self.ndof * (m - 1) + 1
        gn = self.ndof * (n - 1) + 1
        # 从结构类Structured的属性node_displacement中取出单元位移
        self.ele_node_dis[0:self.ndof, 0] = s.node_displacement[gm - 1:gm + 2]
        self.ele_node_dis[self.ndof:2 * self.ndof, 0] = s.node_displacement[gn - 1:gn + 2]
        # 从整体坐标转换到局部坐标
        self.ele_node_dis = np.dot(np.transpose(self.transform_matrix), self.ele_node_dis)

    def cal_node_force(self, s):
        if not isinstance(s, Structure):
            raise TypeError('bad operand type')
        self.ele_node_force = np.dot(self.ek, self.ele_node_dis)  # 局部坐标下的节点力
        if self.distributed_load is not None:
            l = self.l
            n1num = self.n1.num
            n2num = self.n2.num
            t = self.distributed_load.loadtype
            p1 = self.distributed_load.p1
            p2 = self.distributed_load.p2
            f1 = 0
            f2 = 0
            m1 = 0
            m2 = 0
            if t == 1:
                f1 = (7 * p1 + 3 * p2) * l / 20
                m1 = (3 * p1 + 2 * p2) * pow(l, 2) / 60
                f2 = (3 * p1 + 7 * p2) * l / 20
                m2 = -(2 * p1 + 3 * p2) * pow(l, 2) / 60
            elif t == 2:
                pass
            self.ele_node_force[1, 0] += f1
            self.ele_node_force[2, 0] += m1
            self.ele_node_force[4, 0] += f2
            self.ele_node_force[5, 0] += m2


# 子类：平面无轴力梁单元，每个节点2个自由度
class Beam(Element):
    def __init__(self):
        self.ndof = 2

    def get_ek(self):
        l = self.l
        e = self.material.elastic_modulus
        a = self.cross_section.area
        i = self.cross_section.inertia
        self.ek[0] = [12 * e * i / pow(l, 3), 6 * e * i / pow(l, 2), -12 * e * i / pow(l, 3),
                      6 * e * i / pow(l, 2)]
        self.ek[1] = [6 * e * i / pow(l, 2), 4 * e * i / l, -6 * e * i / pow(l, 2), 2 * e * i / l]
        self.ek[2] = [-12 * e * i / pow(l, 3), -6 * e * i / pow(l, 2), 12 * e * i / pow(l, 3),
                      -6 * e * i / pow(l, 2)]
        self.ek[3] = [6 * e * i / pow(l, 2), 2 * e * i / l, -6 * e * i / pow(l, 2), 4 * e * i / l]

    def get_transform_matrix(self):
        c = (self.n2.x - self.n1.x) / self.l
        s = (self.n2.y - self.n1.y) / self.l
        self.transform_matrix[0] = [c, -s, 0, 0]
        self.transform_matrix[1] = [s, c, 0, 0]
        self.transform_matrix[2] = [0, 0, c, -s]
        self.transform_matrix[3] = [0, 0, s, c]

    # 计算局部坐标下单元的节点位移，为计算单元节点力做准备
    def cal_node_dis(self, s):
        if not isinstance(s, Structure):
            raise TypeError('bad operand type')
        m = self.n1.num
        n = self.n2.num
        gm = 2 * (m - 1) + 1
        gn = 2 * (n - 1) + 1
        # 从结构类Structured的属性node_displacement中取出单元位移
        # 不用ndof，思路有点和前面不同了
        self.ele_node_dis[0:2, 0] = s.node_displacement[gm - 1:gm + 1]
        self.ele_node_dis[2:4, 0] = s.node_displacement[gn - 1:gn + 1]
        # 从整体坐标转换到局部坐标
        self.ele_node_dis = np.dot(np.transpose(self.transform_matrix), self.ele_node_dis)

    def cal_node_force(self, s):
        if not isinstance(s, Structure):
            raise TypeError('bad operand type')
        self.ele_node_force = np.dot(self.ek, self.ele_node_dis)  # 局部坐标下的节点力
        if self.distributed_load is not None:
            l = self.l
            n1num = self.n1.num
            n2num = self.n2.num
            t = self.distributed_load.loadtype
            p1 = self.distributed_load.p1
            p2 = self.distributed_load.p2
            f1 = 0
            f2 = 0
            m1 = 0
            m2 = 0
            if t == 1:
                f1 = (7 * p1 + 3 * p2) * l / 20
                m1 = (3 * p1 + 2 * p2) * pow(l, 2) / 60
                f2 = (3 * p1 + 7 * p2) * l / 20
                m2 = -(2 * p1 + 3 * p2) * pow(l, 2) / 60
            elif t == 2:
                pass
            # 不同ndof，思路不同
            self.ele_node_force[1, 0] += f1
            self.ele_node_force[2, 0] += m1
            self.ele_node_force[3, 0] += f2
            self.ele_node_force[4, 0] += m2


# 子类：平面有轴力梁单元，每个节点3个自由度
class Beam2(Element):
    pass
