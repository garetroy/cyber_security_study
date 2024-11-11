
from BanditLevel import BanditLevel

class BanditLevel17(BanditLevel):
    def __init__(self):
        super().__init__("", __file__, password="None")

    def get_next_password(self):
        return super().get_next_password()
