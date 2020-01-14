import json


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


class UnitParam:

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

    def getdefault(self, filepath='config/params/unitparams_default.json'):
        """
        Get default unit parameter configurations.
        Args:
            filepath: Unit parameter configuration file path.

        Returns:
            self: A modified self, with every member variable initialized.

        """
        with open(filepath) as f_unitparam:
            unitparamjson = json.load(f_unitparam)
            # PID parameters
            self.PID.taux = unitparamjson['PID']['taux']
            self.PID.tauy = unitparamjson['PID']['tauy']
            self.PID.tauz = unitparamjson['PID']['tauz']
            # Max acceleration
            self.amax = unitparamjson['amax']
            # Communication parameters
            self.communication.rc = unitparamjson['communication']['rc']
            self.communication.tdelay = unitparamjson['communication']['tdelay']
            # GPS parameters
            self.GPS.tGPS = unitparamjson['GPS']['tGPS']
            self.GPS.sigmax = unitparamjson['GPS']['sigmax']
            self.GPS.sigmay = unitparamjson['GPS']['sigmay']
            self.GPS.sigmaz = unitparamjson['GPS']['sigmaz']
            # External noise parameters
            self.extnoise.sigmax = unitparamjson['externalnoise']['sigmax']
            self.extnoise.sigmay = unitparamjson['externalnoise']['sigmay']
            self.extnoise.sigmaz = unitparamjson['externalnoise']['sigmaz']
            # Wind velocity and etc. parameters
            self.wind.avg = unitparamjson['wind']['avg']
            self.wind.stdev = unitparamjson['wind']['stdev']
            self.wind.angle = unitparamjson['wind']['angle']
            # Package loss parameters
            self.pkgloss.distance = unitparamjson['packageloss']['distance']
            self.pkgloss.ratio = unitparamjson['packageloss']['ratio']

        return self


