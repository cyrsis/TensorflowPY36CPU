# env.py

class ArmEnv(object):
    def __init__(self):
        self.action_bound = None
        self.action_dim = None
        self.state_dim = None
    def step(self, action):
        pass
    def reset(self):
        pass
    def render(self):
        pass