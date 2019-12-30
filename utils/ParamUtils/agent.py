class UnitParamBasic:

    def __init__(self, name, unit, value):
        if isinstance(name, str):
            self.name = name
        if isinstance(unit, str):
            self.unit = unit
        if isinstance(value, {float, int}):
            self.value = value


class PIDctrl:

    taux: float
    tauy: float
    tauz: float

    def __init__(self, taux=0.0, tauy=0.0, tauz=0.0):
        self.taux = taux
        self.tauy = tauy
        self.tauz = tauz


class Communication:

    rc: float
    tdelay: float

    def __init__(self, rc=0.0, tdelay=0.0):
        self.rc = rc
        self.tdelay = tdelay


class GPSctrl:

    tGPS: float
    sigmax: float
    sigmay: float
    sigmaz: float

    def __init__(self, tGPS=0.0, sigmax=0.0, sigmay=0.0, sigmaz=0.0):
        self.tGPS = tGPS
        self.sigmax = sigmax
        self.sigmay = sigmay
        self.sigmaz = sigmaz


class ExternalNoise:

    sigmax: float
    sigmay: float
    sigmaz: float

    def __init__(self, sigmax=0.0, sigmay=0.0, sigmaz=0.0):
        self.sigmax = sigmax
        self.sigmay = sigmay
        self.sigmaz = sigmaz


class Wind:

    avg: float
    stdev: float
    angle: float

    def __init__(self, avg_magnititude=0.0, stdev=0.0, angle=0.0):
        self.avg = avg_magnititude
        self.stdev = stdev
        self.angle = angle


class PackageLoss:

    distance: float
    ratio: float

    def __init__(self, distance=0.0, ratio=0.0):
        self.distance = distance
        self.ratio = ratio


class AgentParam:

    PID: PIDctrl
    amax: float
    communication: Communication
    GPS: GPSctrl
    extnoise: ExternalNoise
    wind: Wind
    pkgloss: PackageLoss

    def __init__(self, PID=PIDctrl(), amax=0.0, communication=Communication(),
                 GPS=GPSctrl(), extnoise=ExternalNoise(), wind=Wind(), pkgloss=PackageLoss()):

        # TODO: to be finished
        self.PID = PID
        self.amax = amax
        self.communication = communication
        self.GPS = GPS
        self.extnoise = extnoise
        self.wind = wind
        self.pkgloss = pkgloss
        pass




