from domain.component.DomainComponent import DomainComponent
from tagged.MapOfTaggedObjects import MapOfTaggedObjects

class LoadPattern(DomainComponent):
    PATTERN_TAG_LoadPattern = 1

    def __init__(self, tag, fact=1.0):
        DomainComponent.__init__(self, tag, self.PATTERN_TAG_LoadPattern)
        self._isConstant = 1        # to indicate whether setConstant has been called

        self._loadFactor = 0        # current load factor
        self._scaleFactor = fact    # factor to scale load factor from time series

        self._theSeries = None      # pointer to associated TimeSeries

        self._currentGeoTag = 0
        self._lastGeoSendTag = -1
        # storage objects for the loads and constraints
        self._theNodalLoads = MapOfTaggedObjects()          
        self._theElementalLoads = MapOfTaggedObjects()
        self._theSPs = MapOfTaggedObjects()

    # methods to set the associated TimeSeries and Domain
    def setTimeSeries(self, theTimeSeries):
        self._theSeries = theTimeSeries

    def setDomain(self, theDomain):
        pass
    # methods to add loads
    def addNodalLoad(self, load):
        theDomain = self.getDomain()
        self._theNodalLoads.addComponent(load)
        load.setDomain(theDomain)
        load.setPatternTag(self.getTag())
        self._currentGeoTag = self._currentGeoTag + 1
    def addElementalLoad(self, load):
        pass
    def addSP_Constraint(self, theSP):
        pass
    
    def getNodalLoads(self):
        pass
    def getElementalLoads(self):
        pass
    def getSPs(self):
        pass

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
    


    


