from analysis.integrator.StaticIntegrator import StaticIntegrator

class LoadControl(StaticIntegrator):
    INTEGRATOR_TAGS_LoadControl = 6
    def __init__(self, dLambda, numIncr, minLambda, maxLambda):
        StaticIntegrator.__init__(self, self.INTEGRATOR_TAGS_LoadControl)
        self._deltaLambda = dLambda
        self._specNumIncrStep = numIncr
        self._dLambdaMin = minLambda
        self._dLambdaMax = maxLambda


    def setTimeSeries(self, theSeries):
        pass