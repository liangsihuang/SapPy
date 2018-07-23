from domain.component.DomainComponent import DomainComponent
from tagged.MapOfTaggedObjects import MapOfTaggedObjects

class LoadPattern(DomainComponent):
    PATTERN_TAG_LoadPattern = 1

    def __init__(self, tag, fact=1.0):
        DomainComponent.__init__(self, tag, self.PATTERN_TAG_LoadPattern)
        self._scaleFactor = fact
        self._theNodalLoads = MapOfTaggedObjects()
        self._currentGeoTag = 0

    def setTimeSeries(self, theTimeSeries):
        self._theSeries = theTimeSeries

    def addNodalLoad(self, load):
        theDomain = self.getDomain()
        self._theNodalLoads.addComponent(load)
        load.setDomain(theDomain)
        load.setPatternTag(self.getTag())
        self._currentGeoTag = self._currentGeoTag + 1



    


