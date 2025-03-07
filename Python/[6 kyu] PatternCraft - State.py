# https://www.codewars.com/kata/5682e72eb7354b2f39000021/train/python

class SiegeState:
    def __init__(self, m=False, d=20):
        self.m = m
        self.d = d


class TankState:
    def __init__(self, m=True, d=5):
        self.m = m
        self.d = d

class Tank:
    def __init__(self, state = None):
        self.state = TankState()

    def can_move(self):
        return self.state.m

    def damage(self):
        return self.state.d