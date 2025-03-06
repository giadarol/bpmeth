import bpmeth
import xtrack as xt
import sympy

import numpy as np

b1 = "0.003*cos(2*s)"

s = sympy.symbols('s')
b1_f = sympy.lambdify(s, b1, modules='numpy')

# Vector potential (bs, b1, a1, b2, a2, b3, a3, ,... as function of s)
A_wiggler = bpmeth.GeneralVectorPotential(hs='0', b=(b1,))

# Make Hamiltonian for a defined length
H_wiggler = bpmeth.Hamiltonian(length=10, curv=0, vectp=A_wiggler)

# This guy is able to track an Xsuite particle!
p = xt.Particles(x=np.linspace(-1e-3, 1e-3, 10), energy0=10e9, mass0=xt.ELECTRON_MASS_EV)
sol = H_wiggler.track(p, return_sol=True)

# I want to see the trajectory along the object
import matplotlib.pyplot as plt
plt.close('all')
plt.figure()
for ss in sol:
    plt.plot(ss.t, ss.y[0])
plt.xlabel('s [m]')
plt.ylabel('x [m]')

plt.show()



