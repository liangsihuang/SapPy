from SRC.material.UniaxialMaterial import UniaxialMaterial

class ElasticMaterial(UniaxialMaterial):
    MAT_TAG_ElasticMaterial = 1

    def __init__(self, tag, e, et = 0.0):
        super().__init__(tag, ElasticMaterial.MAT_TAG_ElasticMaterial)
        self.Epos = e
        self.Eneg = e
        self.eta = et
        self.trialStrain = 0.0
        self.trialStrainRate = 0.0
        self.committedStrain = 0.0
        self.committedStrainRate = 0.0

    def revertToLastCommit(self):
        self.trialStrain = self.committedStrain
        self.trialStrainRate = self.committedStrainRate
        return 0
        