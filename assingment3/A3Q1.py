#System of Ordinary Differential Equations: Lorenz Euations

import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt

"""
The system of ODEs that we will solve is W ≡XYZ(Lornez Equations)
    X(t) = -σ (X - Y)
    Y(t) = rX - Y - XZ
    Z(t) = -bZ + XY
    Constants:σ,r,b
σ = Prandtl number(ratio of kinematic viscosity to thermal diffusivity)
r = Rayleigh number(dependent on vertical temperature difference between top and bottom of atmosphere)
b = Dimensionless length scale

Initial Conditions:
W0 = [0.,1.,0.]
t = 60
σ = 10.
r = 28
b = 8./3
"""
def XYZ(y,t,σ,r,b):
    X, Y, Z = y

    dydt = [-σ*(X-Y),
            r*X - Y - X*Z,
            -b*Z + X*Y]
    return dydt

def XYZT(y,t,σ,r,b,dt):
    X, Y, Z, T = y
    dydt = [-1*σ(X-Y),
            r*X - Y - X*Z-dt*Y,
            -b*Z + X*Y,
            dt*Y]
    return dydt

def solve_XYZmodel(σ,r,b,ti,tf,y0_XYZ,solve_XYZ=True,dt=0.01,y0_XYZT=[]):
    """
    INPUT:
    σ, r, b, ti, tf, y0_XYZT        #see XYZ function
    OPTIONAL INPUT:
    ::boolean:: solve_XYZ           #whether or not to solve XYZ, default True; if False, solve for XYZT system
    dt, y0_XYZT                      #see XYZT function
    """
    t = np.linspace(ti, tf, 3000)
    if solve_XYZ == True:
        sol_XYZ = scipy.integrate.odeint(XYZ, y0_XYZ, t, args=(σ, r, b))
        plt.title('Lorenz Model')
        plt.plot(t, sol_XYZ[:,0], 'y', label='X(t)')
        plt.plot(t, sol_XYZ[:,1], 'r', label='Y(t)')
        plt.plot(t, sol_XYZ[:,2], 'b', label='Z(t)')
        plt.legend(loc='best')
        plt.xlabel('t')
        plt.grid()
        plt.show()
    else:
        #XYZT model (includes time):
        sol_XYZT = sol_XYZ = scipy.integrate.odeint(XYZT, y0_XYZT, t, args=(σ, r, b, dt))
        plt.title('XYZT Model')
        plt.plot(t, sol_XYZT[:,0], 'y', label='X(t)')
        plt.plot(t, sol_XYZT[:,1], 'r', label='Y(t)')
        plt.plot(t, sol_XYZT[:,2], 'b', label='Z(t)')
        plt.plot(t, sol_XYZT[:,3], 'black', label='D(t)')
        plt.legend(loc='best')
        plt.xlabel('t')
        plt.grid()
        plt.show()

def main():
    σ = 10
    r = 28
    b = 8./3 
    


    y0_XYZ = [0.,1.,0.] #Initial Conditions for XYZ model

    w0_XYZ = [0.,1.00000001,0.] #W0` conditions
    
    dt = 0.01
    y0_XYZT = [0.,1.,0.,60] #Initial Conditions for XYZT model
    
    #set of b and g values to plot
    b_set = [0.2,0.5,0.12,0.4]
    g_set = [0.1,0.1,0.07,0.3]
    try:
        assert(len(b_set) == len(g_set)) #check if both lists are same length
    except AssertionError:
        print("ERROR: Lists not the same length")
        return False
    
    #Interval
    ti = 0
    tf = 200
    
    for i in range(0,len(b_set),1):
        solve_XYZmodel(b_set[i],r,g_set[i],ti,tf,y0_XYZ)

    solve_XYZmodel(σ,r,b,ti,tf,y0_XYZ,False,dt,y0_XYZT)
    solve_XYZmodel(σ,r,b,ti,tf,w0_XYZ,False,dt,y0_XYZT)    

if __name__ == "__main__":
    main()