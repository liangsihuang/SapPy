# sap2D

[TrussExample](http://opensees.berkeley.edu/wiki/index.php/Basic_Truss_Example)

框架：
1. 生成 Node, Element, SP_Constraint 对象，并添加到 Domain
2. 生成 LoadPattern 和 NodalLoad 对象，并添加到 Domain
3. 生成 AnalysisModel 对象
4. 生成 Algorithm 对象
5. 生成 Integrator 对象
6. 生成 Handler 对象
7. 生成 Numberer 对象
8. 生成 SOESolver 和 SOE 对象
9. 生成 Analysis 对象，组成部分为`3-8`, 并调用方法 analyze()，即不断调用`3-8`中的方法



