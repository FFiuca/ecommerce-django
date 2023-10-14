from master import models as mMaster
from user import models as mUser
from store import models as mStore

class CheckOutFunctions:
    def __init__(self, customer: mUser.Customer):
        self.customer = customer

    def add(self, data: list):
        pass
