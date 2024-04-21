'''

Database for fluid properties relevant to thermo-physical fenomena.

Curve fit equations from tables in:

T. L. Bergman, A. S. Lavine, F. P. Incropera and D. P. Dewitt, 
Fundamentals of Heat and Mass Transfer, 7th ed. Hoboken, NJ, USA: Wiley, 2011

'''
def density(T):
    return 357.35*T**-1.004

def specific_heat(T):
    return 1E-13*T**4 - \
        6E-10*T**3 + \
        1E-06*T**2 - \
        0.0004*T + \
        1.0613

def dynamic_viscosity(T):
    return -2E-23*T**6 + \
        2E-19*T**5 - \
        8E-16*T**4 + \
        2E-12*T**3 - \
        2E-09*T**2 + \
        1E-06*T - \
        8E-05

def kinematic_viscosity(T):
    return 5E-24*T**6 - \
        4E-20*T**5 + \
        1E-16*T**4 - \
        2E-13*T**3 + \
        2E-10*T**2 - \
        4E-09*T + \
        1E-07

def thermal_conductivity(T):
    return 3E-21*T**6 - \
        1E-17*T**5 - \
        5E-15*T**4 + \
        8E-11*T**3 - \
        1E-07*T**2 + \
        0.0001*T - \
        0.004

def thermal_diffusivity(T):
    return 2E-24*T**6 - \
        1E-20*T**5 + \
        1E-17*T**4 + \
        2E-14*T**3 + \
        5E-11*T**2 + \
        1E-07*T - \
        1E-05

def prandtl_number(T):
    return 3E-20*T**6 - \
        4E-16*T**5 + \
        1E-12*T**4 - \
        3E-09*T**3 + \
        3E-06*T**2 - \
        0.0013*T + \
        0.8975
