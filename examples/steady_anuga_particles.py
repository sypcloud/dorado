"""Make an example of the workflow with gridded anuga output data."""

import numpy as np
from particlerouting.routines import steady_plots
import particlerouting.particle_track as pt

# load some variables from a anuga output so stage is varied
data = np.load('ex_anuga_data.npz')

# pull depth and stage from that data
depth = data['depth']
qx = data['qx']
qy = data['qy']

# create the parameters object and then assign the values
params = pt.params()

# define the params variables
params.stage = depth  # for this example we don't have stage data
params.depth = depth
params.qx = qx
params.qy = qy

params.seed_xloc = list(range(20, 30))
params.seed_yloc = list(range(48, 53))
params.Np_tracer = 50
params.dx = 50.
params.model = 'Anuga'

# Apply the parameters to run the particle routing model
np.random.seed(0)  # fix the random seed for example

# using steady (time-invariant) plotting routine
walk_data = steady_plots(params, 50, 'steady_anuga_example')
