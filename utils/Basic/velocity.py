class Velocity2D:

    vx: float
    vy: float

    def __init__(self, vx=0.0, vy=0.0):
        self.vx = vx
        self.vy = vy

    def __str__(self):
        return '{%f, %f}' % self.vx, self.vy

    def velocitydiff(self, vel: 'Velocity2D'):
        return Velocity2D(self.vx-vel.vx, self.vy-vel.vy)


class Velocity3D(Velocity2D):

    vz: float

    def __init__(self, vx=0.0, vy=0.0, vz=0.0):
        self.vx = vx
        self.vy = vy
        self.vz = vz

        '''self.vx = velcotiy3dlist['vx1']
        self.vy = velcotiy3dlist['vy1']
        self.vz = velcotiy3dlist['vz1']'''

    def __str__(self):
        return '{%f, %f, %f}' % self.vx, self.vy, self.vz

    def velocitydiff(self, vel: 'Velocity3D'):
        return Velocity3D(self.vx-vel.vx, self.vy-vel.vy, self.vz-vel.vz)


