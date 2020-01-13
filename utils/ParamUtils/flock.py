import json


class FlockParam:
    """

    """

    v_flock: float
    v_rep: float
    v_frict: float
    v_max: int
    r0: float
    r0_offset_frict: float
    r0_shill: float
    slope_rep: float
    slope_frict: float
    slope_shill: float
    v_shill: float
    acc_shill: float
    a_frict: float
    c_frict: float
    arena_radius: float
    arena_centerx: float
    arena_centery: float
    arena_shape: int
    dimofsimulation: int

    def __init__(self, v_flock=0.0, v_rep=0.0, v_frict=0.0, v_max=0, r0=0.0, r0_offset_frict=0.0, slope_shill=0.0, v_shill=0.0, acc_shill=0.0,
                 r0_shill=0.0, slope_rep=0.0, slope_frict=0.0, a_frict=0.0, c_frict=0.0, arena_radius=0.0, arena_centerx=0.0, arena_centery=0.0, arena_shape=1, dimofsimulation=2):
        self.v_flock = v_flock
        self.v_rep = v_rep
        self.v_frict = v_frict
        self.v_max = v_max
        self.r0 = r0
        self.r0_offset_frict = r0_offset_frict
        self.r0_shill = r0_shill
        self.slope_rep = slope_rep
        self.slope_frict = slope_frict
        self.slope_shill = slope_shill
        self.v_shill = v_shill
        self.acc_shill = acc_shill
        self.a_frict = a_frict
        self.c_frict = c_frict
        self.arena_radius = arena_radius
        self.arena_centerx = arena_centerx
        self.arena_centery = arena_centery
        self.arena_shape = arena_shape
        # IGNORE THIS PART
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # if list(arena.keys()) == ['centerx', 'centery', 'shape']:
        #    self.arena = arena
        # else:
        #    raise KeyError(
        #        'The keys of \'arena\' should me \'centerx\', \'centery\'&\'shape\', check again.')
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        self.dimofsimulation = dimofsimulation

    def getdefault(self, filepath='default'):
        if filepath == 'default':
            filepath = 'config/params/flockparams_default.json'

        filecontent = open(filepath)
        thejson = json.load(filecontent)
        newflockparam = FlockParam(
            v_flock=thejson['v_flock'],
            v_rep=thejson['v_rep'],
            v_frict=['v_frict'],
            v_max=thejson['v_max'],
            r0=thejson['r0'],
            r0_offset_frict=thejson['r0_offset_frict'],
            r0_shill=thejson['r0_shill'],
            slope_rep=thejson['slope_rep'],
            slope_frict=thejson['slope_frict'],
            a_frict=thejson['a_frict'],
            c_frict=thejson['c_frict'],
            arena_radius=thejson['arena']['radius'],
            arena_centerx=thejson['arena']['centerx'],
            arena_centery=thejson['arena']['centery'],
            arena_shape=thejson['arena']['shape'],
            dimofsimulation=thejson['dimofsimulation'],
            slope_shill=thejson['slope_shill'],
            v_shill=thejson['v_shill'],
            acc_shill=thejson['acc_shill'])

        return newflockparam

    def applyrange(self):
        """
        Each member variable(aka parameter) of a 'FlockParam' instance has a range.
        This function is used to check whether the actual value is within the range.
        If more than Max -> Max; else if less than Min -> Min.
        :return: a 'FlockParam' instance in the given range.
        """
        return self
        pass

    def refresh(self):
        """I don't know why the original use this function"""
        pass
