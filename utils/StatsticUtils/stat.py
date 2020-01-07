from enum import Enum
import csv

timeelapsedneararena = 5.0


class SaveMode(Enum):
    FALSE = 0
    TIMELINE = 1
    STAT = 2
    STEADYSTAT = 3


class Item:
    # 4 digits
    acceleration: list
    # 4 digits
    correlation: list
    # 4 digits
    distancebetweenunits: list
    # 3 digits
    distancebetweenneighbors: list
    # 1 digits
    collisionratio: float
    # 8 digits
    velocity: list
    # 3 digits
    CoM: list

    def __init__(self, acceleration=[0.0 for i in range(4)],
                 correlation=[0.0 for i in range(4)],
                 distancebetweenunits=[0.0 for i in range(4)],
                 distancebetweenneighbors=[0.0 for i in range(3)],
                 collisionratio=0.0,
                 velocity=[0.0 for i in range(8)],
                 CoM=[0.0 for i in range(3)]):

        self.acceleration = acceleration
        self.correlation = correlation
        self.distancebetweenunits = distancebetweenunits
        self.distancebetweenneighbors = distancebetweenneighbors
        self.collisionratio = collisionratio
        self.velocity = velocity
        self.CoM = CoM
        pass

    def reset(self):
        self.acceleration = [0.0 for i in range(4)]
        self.correlation = [0.0 for i in range(4)]
        self.distancebetweenunits = [0.0 for i in range(4)]
        self.distancebetweenneighbors = [0.0 for i in range(3)]
        self.collisionratio = 0.0
        self.velocity = [0.0 for i in range(8)]
        self.CoM = [0.0 for i in range(3)]


class StatUtil:
    elapsedtime: float
    startofsteadystate: float
    savemode: SaveMode
    sum: Item
    stdev: Item

    def __init__(self, elpasedtime=0.0, startofsteadystate=0.0,
                 savemode=SaveMode.FALSE, sum=Item(), stdev=Item()):
        self.elapsedtime = elpasedtime
        self.startofsteadystate = startofsteadystate
        self.savemode = savemode
        self.sum = sum
        self.stdev = stdev
        pass

    def reset(self):
        self.sum.reset()
        self.stdev.reset()
        pass

    def initmodelspecificstatus(self, currentdirectory: str):

        f_distancefromarena = open(currentdirectory+'/distance_from_arena.csv', 'w+')
        f_clusterdependentcorrelation = open(currentdirectory+'/cluster_dependent_correlation.csv', 'w+')
        f_clusterparameters = open(currentdirectory+'/cluster_parameters.csv', 'w+')

        # preparations
        title_distancefromarena = [
            'time(s)',
            'distance_from_arena_avg(cm)',
            'distance_from_arena_stdev(cm)',
            'distance_from_arena_min(cm)',
            'distance_from_arena_max(cm)',
            'number_of_agents_outside']
        title_clusterdependentcorrelation = [
            'time(s)',
            'cluster_dependent_correlation_avg',
            'cluster_dependent_correlation_stdev',
            'cluster_dependent_correlation_min',
            'cluster_dependent_correlation_max']
        title_clusterparameters = [
            'time_(s)',
            'min_cluster_size',
            'max_cluster_size',
            'agents_not_in_cluster']

        if self.savemode is SaveMode.STAT or self.savemode is not SaveMode.STEADYSTAT:
            csvwriter_distancefromarena = csv.writer(
                f_distancefromarena)
            csvwriter_distancefromarena.writerow(
                title_distancefromarena)

        csvwriter_clusterdependentcorrelation = csv.writer(
            f_clusterdependentcorrelation)
        csvwriter_clusterdependentcorrelation.writerow(
            title_clusterdependentcorrelation)
        csvwriter_clusterparameters = csv.writer(
            f_clusterparameters)
        csvwriter_clusterparameters.writerow(
            title_clusterparameters)

        if self.savemode is SaveMode.STAT or self.savemode is SaveMode.STEADYSTAT:
            f_distancefromarena_stdev = open(currentdirectory+'/distance_from_arena_stdev.csv', 'w+')
            f_clusterdependentcorrelation_stdev = open(currentdirectory+'/cluster_dependent_correlation_stdev.csv', 'w+')
            f_clusterparameters_stdev = open(currentdirectory+'/cluster_parameters_stdev.csv', 'w+')

            # preparations
            title_distancefromarena_stdev = [
                'time_elapsed_near_arena_(s)',
                'distance_from_arena_avg_(cm)',
                'distance_from_arena_stdev_(cm)',
                'distance_from_arena_min_(cm)',
                'distance_from_arena_max_(cm)',
                'number_of_agents_outside']
            title_clusterdependentcorrelation_stdev = [
                'time_(s)',
                'cluster_dependent_correlation_avg',
                'cluster_dependent_correlation_stdev',
                'cluster_dependent_correlation_min',
                'cluster_dependent_correlation_max']
            title_clusterparameters_stdev = [
                'time_(s)', 'min_cluster_size',
                'max_cluster_size',
                'agents_not_in_cluster']

            csvwriter_distancefromarena_stdev = csv.writer(
                f_distancefromarena_stdev)
            csvwriter_distancefromarena_stdev.writerow(
                title_distancefromarena_stdev)

            csvwriter_clusterdependentcorrelation_stdev = csv.writer(
                f_clusterdependentcorrelation_stdev)
            csvwriter_clusterdependentcorrelation_stdev.writerow(
                title_clusterdependentcorrelation_stdev)

            csvwriter_clusterparameters_stdev = csv.writer(
                f_clusterparameters_stdev)
            csvwriter_clusterparameters_stdev.writerow(
                title_clusterparameters_stdev)

        # TODO: how to deal with the global variable 'TimeElapsedNearArena'? This is a question

        global timeelapsedneararena
        timeelapsedneararena = 0.0

