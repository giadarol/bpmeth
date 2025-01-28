import bpmeth
import numpy as np
import matplotlib.pyplot as plt

"""
Compare the analytical and numerical solution for the exact dipole
"""

# Parameters
length = 1
angle = 1
h = angle/length

BB = 1 # Only q By / P0 plays a role so lets call this quantity BB
x0 = 0.1
y0 = 0
tau0 = 0
px0 = 0.3
py0 = 0.2
ptau0 = 0
beta0 = 1
qp0 = [x0, y0, tau0, px0, py0, ptau0]


# EXACT SOLUTION
# Plot a trajectory with dipole in y direction
delta = np.sqrt(1 + 2*ptau0/beta0 + ptau0**2) - 1
theta0 = np.arcsin(px0 / np.sqrt((1+delta)**2 - py0**2))

s = np.linspace(0,1,100)
px = px0*np.cos(s*h) + ( np.sqrt((1+delta)**2-px0**2-py0**2) - (1/h + x0)*BB )*np.sin(s*h)
pxder = -px0*h*np.sin(s*h) + ( np.sqrt((1+delta)**2-px0**2-py0**2) - (1/h + x0)*BB )*h*np.cos(s*h)
x = 1/h * 1/BB * ( h*np.sqrt((1+delta)**2-px**2-py0**2) - pxder - BB)
y = h*py0/BB*s - py0/BB * ( np.arcsin(px/np.sqrt((1+delta)**2)) - np.arcsin(px0/np.sqrt((1+delta)**2)) ) + y0


# NUMERICAL SOLUTION
p_sp = bpmeth.SympyParticle()

dipole = bpmeth.DipoleVectorPotential(h, BB)
H_dipole = bpmeth.Hamiltonian(length, h, dipole)
sol_dipole = H_dipole.solve(qp0, ivp_opt={'t_eval':s})


# CANVAS TO PLOT
canvas_zx = bpmeth.CanvasZX()
#canvas_zxy = bpmeth.CanvasZXY()

# Frame in the origin
fr = bpmeth.Frame()
# Curvilinear coordinates in global frame
fb = bpmeth.BendFrame(fr,length,angle)

fb.plot_trajectory_zx(s,x,y, canvas=canvas_zx, color="blue")
H_dipole.plotsol(qp0, canvas_zx=canvas_zx)

plt.show()


# PLOT THE DIFFERENCE
fig, ax = plt.subplots()
ax.plot(s, x-sol_dipole.y[0])
ax.set_xlabel('s')
ax.set_ylabel('absolute error x')
plt.show()