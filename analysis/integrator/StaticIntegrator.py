from analysis.integrator.IncrementalIntegrator import IncrementalIntegrator

class StaticIntegrator(IncrementalIntegrator):
    def __init__(self, clasTag):
        IncrementalIntegrator.__init__(self, clasTag)
        

    def setTimeSeries(self, theSeries):
        pass