# Step 1

# Step 2
# Fahrenhit to Celsius conversion function
def f_to_c(f_temp):
    return (f_temp - 32) * (5 / 9)

# Testing f_to_c function
f100_in_celcius = f_to_c(100)
print(f100_in_celcius)

# Step 3
def c_to_f(c_temp):
    f_temp = c_temp * (9 / 5) + 32
    return f_temp

# Testing c_to_f function
c100_in_fahrenheit = c_to_f(100)
print(c100_in_fahrenheit)