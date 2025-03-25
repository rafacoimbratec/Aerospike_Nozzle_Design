# Second Project Group 3
Compressible Inviscid (and Viscous) High Speed Nozzle Flows 

Inspired by "Linear Aerospike Contour Design using
 Angelino’s Method and CFD Validation" - João Pedro Cristóvão Silva

 # Steps:
    1-Angelino python method - design the countor of the Aerospike for control variables
        - Altitude
        - PR
        - Outlet Mach
        - Gamma
        - Expansion Lines
    2-Solidworks - create the geometry of the spike and control domain
    3-Theoretical analysis of CFD methods being implemented
    4-Analyse four RPS
        - sea level
        - above operational altitude
        - +above operational altitude
        - operational altitude
    5-Diamond Mach analysis (shock expansion theory)
    6-Thrust vector analysis (capacity of aerospike to have high effiency for under-expansion conditions)
    7-Validation
    S. Khan, A.Khan, andA.Munir,“Designandanalysis approach for linear aerospike nozzle,” Science Vision, vol. 20, pp. 25– 37, 07 2014.
 [Online]. Available:https://www.researchgate.net/publication/280342589_Design_and_Analysis_Approach_for_Linear_Aerospike_Nozzle

# Report Structure
    1-Introduction
    2-Conventional Rocket Nozzles
        a-Bell Nozzle
        b-Altitude Limitations of Real Bell Nozzles
    3-Advanced Rocket Nozzles Design
        a-Aerospike Nozzle
        b-Overall balance (advantage and disadvantages)
    4-Methodology
        a-Countour Design
        b-Numerical study
        c-Parameters of Study
    5-Results and Dicussion

# Theoretical Notes
    Aerospike Nozzle
        -Low altitudes the high ambient pressure causes the exhaust flow to remain close to the nozzles wall and be directed to the axial position through a series of expansion-compression fans.
        -Higher altitudes, the free boundary promotes the appearence of compression shocks that enable the exhaust flow to remain primarily axial, even in a wider plume.
        -Design alatitude, the wake is already closed, but the plume is less wider than a underexpanded scenario, with more axial flow

        Analyse truncation?
    
# Method of characteristics 
    MOC - utilizes characteristic lines, which are part of the mathematical definition of PDE. These lines have a constant relation between some of the flow's velocity angles along them
    To apply the MOC the flow is assumed - supersonic, steady, inviscid, irrotational and two dimensional.

# Aerospike countour design
Literature:
    1-H.Greer,“Rapid method for plug nozzle design,”ARS Journal,vol.31,pp.560–561,Apr. 1961. 
    2-G. Angelino, “Approximate method for plug nozzle design,” AIAA Journal, vol. 2, pp. 1834–1835, Oct. 1964. DOI: 10.2514/3.2682

    Assumption nº1: At the throat the flow is sonic in a straight line and not a curved line
    Assumption nº2: The flow expands solely due to the centered expansion fan on lip A.
    Assumption nº3:The flow is desired to be parallel to the centerline at the exit, the flow at the throat must be incident with an angle equal to the Prandtl-Meyer angle of the chosen exit MN.

    "Therefore, for the scope of the present dissertation, this simplified method seems appro
    priate. Moreover, considering a large number of characteristic lines will lead to a more
    accurate contour, even without considering complex methods of interpolating the result
    ing points." - Angelino Method justification

    https://github.com/mvernacc/aerospike-nozzle-design-gui/blob/master/Spike%20Contour%20Algorithm.pdf

    For validation purposes:
        Gamma = 1.4
        Me = 4.16
        N_lines = 100

    Inviscid model:
        PR:
            20 - 0m
            188 - 15545m
            20480 - 47750m
                static pressure,mach,temperature,stag pressure, velocity
    Turbulent model, Rans:
            20480 - 47750 - Thrust vectoring, wall y+, static pressure, mach