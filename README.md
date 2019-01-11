# sap2D
用Python改写OpenSees，目的：
1. 熟悉有限元分析的整个流程，OpenSees源程序采用`C++`语言，语法过于复杂，不易于理解有限元本身
2. 重点在于单元和材料的编程（理解非线性和动力学），其他类越简单越好，不用顾忌效率，能用就行
3. 熟悉整个有限元程序的基本框架

## 第一个例子：弹性桁架单元
[TrussExample](http://opensees.berkeley.edu/wiki/index.php/Basic_Truss_Example)

流程：
1. 生成 Node, Element, SP_Constraint 对象，并添加到 Domain
2. 生成 LoadPattern 和 NodalLoad 对象，并添加到 Domain
3. 生成 AnalysisModel 对象: 为了对节点进行重新排号，不能直接使用Element类和Node类，而应先转化为FE_Element和DOF_Group
4. 生成 Algorithm 对象
5. 生成 Integrator 对象：决定是荷载增量法或是弧长法，包含有集合所有节点不平衡力的方法，所以叫integrator
6. 生成 Handler 对象
7. 生成 Numberer 对象
8. 生成 SOESolver 和 SOE 对象
9. 生成 Analysis 对象，组成部分为`3-8`, 并调用方法 analyze()，即不断调用`3-8`中的方法



