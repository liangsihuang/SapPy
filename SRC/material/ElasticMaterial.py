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

    
    
    def setTrialStrain(self, strain, strainRate):
        self.trialStrain = strain
        self.trialStrainRate = strainRate
        return 0
    
    def setTrial(self, strain, stress, tangent, strainRate=0.0):
        self.trialStrain = strain
        self.trialStrainRate = strainRate
        if self.trialStrain >= 0.0:
            stress = self.Epos * self.trialStrain + self.eta * self.trialStrainRate
            tangent = self.Epos
        else:
            stress = self.Eneg * self.trialStrain + self.eta * self.trialStrainRate
            tangent = self.Eneg
        return 0
        
    def getStrain(self):
        return self.trialStrain

    def getStrainRate(self):
        return self.trialStrainRate

    def getStress(self):
        if self.trialStrain >= 0.0:
            return self.Epos*self.trialStrain + self.eta*self.trialStrainRate
        else:
            return self.Eneg*self.trialStrain + self.eta*self.trialStrainRate

    def getTangent(self):
        if self.trialStrain > 0.0:
            return self.Epos
        elif self.trialStrain < 0.0:
            return self.Eneg
        else:
            if self.Epos > self.Eneg:
                return self.Epos
            else:
                return self.Eneg

    def getDampTangent(self):
        return self.eta

    def getInitialTangent(self):
        if self.Epos > self.Eneg:
            return self.Epos
        else:
            return self.Eneg
    
    def commitState(self):
        self.committedStrain = self.trialStrain
        self.committedStrainRate = self.trialStrainRate
        return 0

    def revertToLastCommit(self):
        self.trialStrain = self.committedStrain
        self.trialStrainRate = self.committedStrainRate
        return 0

    def revertToStart(self):
        self.trialStrain = 0.0
        self.trialStrainRate = 0.0
        return 0

    def getCopy(self):
        pass
    

    