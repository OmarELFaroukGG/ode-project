import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#this is what we want to solve:
#(3𝑦𝑥^2−𝑦/𝑥^2 )𝑑𝑥+(𝑥^3+cos⁡𝑦+1/𝑥)𝑑𝑦=0  #type : exact 
#y is dependent on x and x is independent variable

# Define the ODE as a function
def model(y, x):
    dydx = -(3 * y * x**2 - y / x**2) / (x**3 + np.cos(y) + 1 / x) #we rearanged the eqn so it satisfy dy/dx
    return dydx #reutrn the 

# Initial condition
y0 = 1.0  # You can adjust the initial condition as needed

## This means that the solution of the ODE will be computed with the assumption that 
## at the starting point (x = 0.1 in the code), the value of y is 1.0.

# x values (array)
x_values = np.linspace(0.1, 2, 101)  # Starting from a small value to avoid division by zero at x=0

# generates an array of 101 equally spaced values between 0.1 and 2.
# This array represents the values of the independent variable x at which
# we want to compute the corresponding values of the dependent variable y.


# Solve the ODE using odeint function from scipy.integrate libirary
# IT is a numerical integration method that calculates an approximate solution to the ODE
# given the initial condition and a set of values for the independent variable.

solution = odeint(model, y0, x_values)
# takes three main arguments:
# model: The function defining the ODE.
# y0: The initial condition for the dependent variable y at the initial point of the independent variable x.
# x_values: An array of x values at which the solution should be computed.
# solution, is an array where each element corresponds to the value of y at the corresponding x value.



print("the number of solution array elements count:",len(solution))
print("solution is ", solution) # it will be only 1 column because y is the only depnent variable in the eqn.
#so as we print the length it will be the same lenght of x_values array which is 101 elements
    


# Extract y values from the solution and store in a list
y_values = solution[:, 0].tolist() 
#[:, 0] Selecting all rows from the first column, which contains the values of the dependent variable y. 
# and these values are associated with the corresponding x values used in the computation.
# The x values are defined separately in the x_values array when specifying the range for solving the ODE.

# Print the list of y values
print("List of y values:", y_values)

# Plot the solution
plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Solution of the First-Order ODE')
plt.show()

