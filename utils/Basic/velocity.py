class Velocity2D:

    vx: float
    vy: float

    def __init__(self, vx=0.0, vy=0.0):
        self.vx = vx
        self.vy = vy

    def __str__(self):
        print('The 2D velocity vector is [%f, %f]. '% self.vx, self.vy)

    def velocitydiff(self, vel: 'Velocity2D'):
        return Velocity2D(self.vx-vel.vx, self.vy-vel.vy)


class Velocity3D(Velocity2D):

    vz: float

    def __init__(self, vx=0.0, vy=0.0, vz=0.0):
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def __str__(self):
        print('The 3D velocity vector is [%f, %f, %f]. ' % self.vx, self.vy, self.vz)

    def velocitydiff(self, vel: 'Velocity3D'):
        return Velocity3D(self.vx-vel.vx, self.vy-vel.vy, self.vz-vel.vz)


