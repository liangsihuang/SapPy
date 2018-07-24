from domain.component.DomainComponent import DomainComponent

class Element(DomainComponent):

    def __init__(self, tag, classTag):
        super().__init__(tag, classTag)
        # 构造函数不写也行，因为没新东西
        # 后面扩展会加新东西
    
    # methods dealing with nodes and number of external dof
    def getExternalNodes(self):
        pass # 纯虚，在子类实现
        
    # methods dealing with commited state and update
    def revertToLastCommit(self):
        pass # 纯虚，在子类实现
    
    def isSubdomain(self):
        return False # 有鬼用？（注意：虚函数）

    # methods to return the current linearized stiffness, damping and mass matrices
    # methods for applying loads
    def zeroLoad(self):
        pass # 空函数？有鬼用？（注意：虚函数）

    # methods for obtaining resisting force (force includes elemental loads)
    # methods for obtaining information specific to an element
