import timeit
import numpy as np
from spiceypy import spiceypy as spice
from spiceypy.tests.gettestkernels import downloadKernels, CoreKernels, MarsKernels, CassiniKernels, ExtraKernels, cleanup_Cassini_Kernels, cleanup_Core_Kernels, cleanup_Extra_Kernels, cleanup_Mars_Kernels

# downloadKernels()

spice.kclear()
spice.furnsh(CoreKernels.testMetaKernel)

# list of et times
etOne = spice.str2et('Dec 25, 2007')
etTwo = spice.str2et('Dec 25, 2017')
num_steps = 100000
num_trials = 1
et = np.linspace(etOne, etTwo, num_steps)
# no vectorization
def spk_novectorization():
    state = np.zeros((num_steps, 6))
    lt = np.zeros(num_steps)
    for ii, t in enumerate(et):
        state[ii, :], lt[ii] = spice.spkezr('Moon',t, 'J2000', 'NONE', 'EARTH')
    return state, lt

def spk_oneline():
    state, lt = spice.spkezr_oneline('Moon', et, 'J2000', 'NONE', 'EARTH')
    return state, lt

def spk_loop():
    state, lt = spice.spkezr_loop('Moon', et, 'J2000', 'NONE', 'EARTH')
    return state, lt

def spk_loop_andrew():
    output = spice.spkezr_loop_andrew('Moon', et, 'J2000', 'NONE', 'EARTH')
    return output

def spk_loop_shankar():
    state, lt = spice.spkezr_loop_shankar('Moon', et, 'J2000', 'NONE', 'EARTH')
    return state, lt

print("No Vectorization: ", timeit.timeit(spk_novectorization, number=num_trials)/num_trials)
# list comprehension and mapping tuples to arrays
print("OneLine: ", timeit.timeit(spk_oneline, number=num_trials)/num_trials)
print("Loop: ", timeit.timeit(spk_loop, number=num_trials)/num_trials)
print("Andrew: " , timeit.timeit(spk_loop_andrew, number=num_trials)/num_trials)
print("Shankar: " , timeit.timeit(spk_loop_shankar, number=num_trials)/num_trials)
spice.kclear()
# cleanup_Cassini_Kernels()
# cleanup_Core_Kernels()
# cleanup_Extra_Kernels()
# cleanup_Mars_Kernels()

