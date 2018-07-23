from analysis.integrator.Integrator import Integrator

class IncrementalIntegrator(Integrator):
    def __init__(self, clasTag):
        Integrator.__init__(self, clasTag)
        

    def setTimeSeries(self, theSeries):
        pass