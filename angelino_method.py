"""
Author: Rafael Coimbra Azeiteiro, Insituto Superior Técnico, Universidade de Lisboa, 2025
This code is based on work by João Pedro Cristóvão Silva - "Angelino’s Method and CFD Validation" - João Pedro Cristóvão Silva
However, all possible changes and features are going to be implemented by me, and the code is going to be adapted to the project needs.
More in depth about the project is referenced in the README.md file.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

"""
User inputs: 
    1- Flow adiabatic constant
    2- Aerospike Exit Mach number
    3-Number of characteristic lines
Each line will corresponde to a close interval division between M=1 and M=Me
For each M number, a length and inclination angle will be calculated
The aerospike countour export - Excel + image
Initially, all dimensionless by throat diameter - Implementation?
"""

def main():
    #Defined area of the throat
    A_t = 4.005e-3
    # User inputs 
    print("Enter inputs for aerospike countour design:")
    try:
        gamma = float(input("Flow adiabatic constant: "))
        Me = float(input("Aerospike Exit Mach number: "))
        n = int(input("Number of characteristic lines: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    lip_coords = [0,3] #Coordinates for the lip of the aerospike
    interval = (Me-1)/(n-1) #Interval between each characteristic line
    M = 1
    # Lists to store data
    flow_data = np.zeros(shape=(n, 3)) #[M, L/D, theta]
    pm_angle_exit = pm_angle(gamma, Me) #This function was created for a previous project
    for i in range(n):
        flow_data[i,0] = M
        flow_data[i,1] = M*epsilon(M,gamma)
        flow_data[i,2] = pm_angle_exit + mach_angle(M) - pm_angle(gamma, M)
        M += interval
    PR=(1+((gamma-1)/2)*Me**2)**(gamma/(gamma-1))
    # Draw figure
    points, lip_coords = set_points(flow_data, lip_coords)
    points_dimensionalized = points*A_t
    lip_coords_dimensionalized = [lip_coords[0]*A_t, lip_coords[1]*A_t]
    draw_figure(points, lip_coords)
    print("Aerospike contour design completed.")
    print("Exit pressure ratio: ", PR)
    print("Throat Angle: ",pm_angle_exit)
    print("Length: ",points[len(flow_data)-1,0])
    print("Height: ",points[0,1])
    print("Aerospike contour data exported to aerospike_data.xlsx")
    print("Aerospike contour image exported to aerospike_contour.png")
    
    
    
def pm_angle(gamma, Me):
    #Prandtl-Meyer function
    #This function was created for a previous project
    #It calculates the Prandtl-Meyer angle for a given Mach number
    A=math.sqrt((gamma+1)/(gamma-1))
    B=math.atan(math.sqrt(((gamma-1)/(gamma+1))*(Me**2-1)))-math.atan(math.sqrt(Me**2-1))
    return A*B

def epsilon(M,gamma):
    #It calculates the expansion ratio for a given Mach number
    return (1/M)*((1+((gamma-1)/2)*M**2)**((gamma+1)/(2*(gamma-1))))

def mach_angle(M):
    #It calculates the Mach angle for a given Mach number
    return math.asin(1/M)


def set_points(flow,P):
#creating the points
    size = len(flow)
    points = np.zeros(shape=(size,2))
    for i in range(size):
        points[i,0] = P[0] + flow[i,1]*math.cos(flow[i,2]) #x
        points[i,1] = P[1] - flow[i,1]*math.sin(flow[i,2]) #y
    #moving the geometry to a ref where x_first_point = 0 and y_last_point=0
    new_x = points[0,0]
    new_y = points[size-1,1]
    for i in range(size):
        points[i,0] = points[i,0] - new_x
        points[i,1] = points[i,1] - new_y
    new_lip_coord = [0,0]
    new_lip_coord[0] = P[0] - new_x
    new_lip_coord[1] = P[1] - new_y
    return points, new_lip_coord


def draw_figure(flow_data, P):
    # Draw figure
    #the lip
    P_1 = [P[0]+0.02,P[1]+0.02]
    P_2 = [P[0]-0.3,P[1]+0.02]
    plt.plot([P[0],P_2[0]],[P[1],P_2[1]],color='blue')
    plt.plot([P_1[0],P_2[0]],[P_1[1],P_2[1]],color='blue')
    #plot the countour
    plt.plot(flow_data[:,0], flow_data[:,1], color='black')
    #plot the characteristic lines
    for i in range(len(flow_data)):
        plt.plot([P[0],flow_data[i,0]],[P[1],flow_data[i,1]],color='red')
    plt.show()
    # Export data to Excel
    #df = pd.DataFrame(flow_data, columns=["M", "L/D", "Theta"])
    #df.to_excel("aerospike_data.xlsx", index=False)
    # Export figure
    #fig.savefig("aerospike_contour.png")
    
if __name__ == "__main__":
    main()
