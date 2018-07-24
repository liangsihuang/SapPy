from domain.component.DomainComponent import DomainComponent
from tagged.MapOfTaggedObjects import MapOfTaggedObjects

class LoadPattern(DomainComponent):
    PATTERN_TAG_LoadPattern = 1

    def __init__(self, tag, fact=1.0):
        DomainComponent.__init__(self, tag, self.PATTERN_TAG_LoadPattern)
        self._scaleFactor = fact
        self._theNodalLoads = MapOfTaggedObjects()
        self._currentGeoTag = 0

    # methods to set the associated TimeSeries and Domain
    def setTimeSeries(self, theTimeSeries):
        self._theSeries = theTimeSeries

    # methods to add loads
    def addNodalLoad(self, load):
        theDomain = self.getDomain()
        self._theNodalLoads.addComponent(load)
        load.setDomain(theDomain)
        load.setPatternTag(self.getTag())
        self._currentGeoTag = self._currentGeoTag + 1

    # methods to remove loads

    # methods to apply loads

    # methods for o/p

    # methods to obtain a blank copy of the LoadPattern
    


    


