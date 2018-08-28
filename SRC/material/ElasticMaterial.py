from material.UniaxialMaterial import UniaxialMaterial

class ElasticMaterial(UniaxialMaterial):
    MAT_TAG_ElasticMaterial = 1

    def __init__(self, tag, e, et = 0.0):
        super().__init__(tag, self.MAT_TAG_ElasticMaterial)
        self._Epos = e
        self._Eneg = e
        self._eta = et
        self._trialStrain = 0.0
        self._trialStrainRate = 0.0
        self._committedStrain = 0.0
        self._committedStrainRate = 0.0

    def revertToLastCommit(self):
        self._trialStrain = self._committedStrain
        self._trialStrainRate = self._committedStrainRate
        return 0
        