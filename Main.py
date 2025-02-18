# Step 1

# Fahrenhit to Celsius conversion function
def f_to_c(f_temp):
    return (f_temp - 32) * (5 / 9)

# Testing f_to_c function
f100_in_celcius = f_to_c(100)
print(f100_in_celcius)