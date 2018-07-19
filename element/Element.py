from domain.component.DomainComponent import DomainComponent

class Element(DomainComponent):

    def __init__(self, tag, classTag):
        super().__init__(tag, classTag)
        # 构造函数不写也行，因为没新东西
        # 后面扩展会加新东西

    def getExternalNodes(self):
        pass
        # 在子类实现