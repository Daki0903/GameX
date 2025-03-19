class Physics:
    def __init__(self, velocity_x=0, velocity_y=0, gravity=0):
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.gravity = gravity

    def apply_gravity(self):
        self.velocity_y += self.gravity
