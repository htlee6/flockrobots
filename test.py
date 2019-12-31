import utils.PhaseUtils.phasedata as pd
import utils.PhaseUtils.phaselist as pl

l = pl.PhaseList(timestep=10, innerstatenumber=3, agentnumber=5)
d = pd.PhaseData()
d = l.data[0]
d.randomphase(initsize=pd.Position3D(1, 2, 3), initcenter=pd.Position3D(1, 3, 5), fromagentno=3, toagentno=4, radius=1)
pass
