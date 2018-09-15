from SRC.domain.component.DomainComponent import DomainComponent
from SRC.tagged.storage.MapOfTaggedObjects import MapOfTaggedObjects

class LoadPattern(DomainComponent):
    PATTERN_TAG_LoadPattern = 1

    def __init__(self, tag, fact=1.0):
        DomainComponent.__init__(self, tag, LoadPattern.PATTERN_TAG_LoadPattern)
        self.isConstant = 1        # to indicate whether setConstant has been called

        self.loadFactor = 0        # current load factor
        self.scaleFactor = fact    # factor to scale load factor from time series

        self.theSeries = None      # pointer to associated TimeSeries

        self.currentGeoTag = 0
        self.lastGeoSendTag = -1
        # storage objects for the loads and constraints
        self.theNodalLoads = MapOfTaggedObjects()          
        self.theElementalLoads = MapOfTaggedObjects()
        self.theSPs = MapOfTaggedObjects()

    # methods to set the associated TimeSeries and Domain
    def setTimeSeries(self, theTimeSeries):
        self.theSeries = theTimeSeries

    def setDomain(self, theDomain):
        for tag in self.theNodalLoads:
            nodLoad = self.theNodalLoads.getComponent(tag)
            nodLoad.setDomain(theDomain)
        for tag in self.theElementalLoads:
            eleLoad = self.theElementalLoads.getComponent(tag)
            eleLoad.setDomain(theDomain)
        for tag in self.theSPs:
            theSP = self.theSPs.getComponent(tag)
            theSP.setDomain(theDomain)
        
        super().setDomain(theDomain)

    # methods to add loads
    def addNodalLoad(self, load):
        theDomain = self.getDomain()
        self.theNodalLoads.addComponent(load)
        load.setDomain(theDomain)
        load.setPatternTag(self.getTag())
        self.currentGeoTag += 1
        
    def addElementalLoad(self, load):
        pass
    def addSP_Constraint(self, theSP):
        pass
    
    def getNodalLoads(self):
        return self.theNodalLoads
    def getElementalLoads(self):
        return self.theElementalLoads
    def getSPs(self):
        return self.theSPs

    # methods to remove loads
    def clearAll(self):
        pass
    def removeNodalLoad(self, tag):
        pass
    def removeElementalLoad(self, tag):
        pass
    def removeSP_Constraint(self, tag):
        pass

    # methods to apply loads
    def applyLoad(self, pseudoTime=0.0):
        pass
    def setLoadConstant(self):
        pass
    def unsetLoadConstant(self):
        pass
    def getLoadFactor(self):
        pass

    # methods for o/p

    # methods to obtain a blank copy of the LoadPattern
    


    


