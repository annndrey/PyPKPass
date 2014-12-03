from PyPKPass.PKPass import PKPass
from PyPKPass.PKPassField import PKPassField

class PKStoreCard(PKPass):
    def __init__(self, passTypeIdentifier, serialNumber):
        super(PKStoreCard, self).__init__(passTypeIdentifier, serialNumber)
        
        # Style-Specific Information
        self.passType = "storeCard"
