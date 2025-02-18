# Inputs for functions
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Step 1 & 2
# Fahrenhit to Celsius conversion function
def f_to_c(f_temp):
    return (f_temp - 32) * (5 / 9)

# Testing f_to_c function
f100_in_celcius = f_to_c(100)
print(f100_in_celcius)

# Step 3 & 4 
def c_to_f(c_temp):
    f_temp = c_temp * (9 / 5) + 32
    return f_temp

# Testing c_to_f function
c100_in_fahrenheit = c_to_f(100)
print(c100_in_fahrenheit)

# Step 5 - 7
def get_force(mass, acceleration):
    return mass * acceleration

# Save force value to variable
train_force = get_force(train_mass, train_acceleration)
print(train_force)

print(f'The GE train supplies {train_force} Newtons of force.')

# Step 8 -10

# Set Constant value
c= 3*10**8

# Function for energy calculation
def get_energy(mass, c):
    return mass * c**2

# Test energy function
bomb_energy = get_energy(bomb_mass, c)
print(f'A 1kg bomb supplies {bomb_energy} Joules of energy.')