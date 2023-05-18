
# ===============================================
# ==== Einstein =================================
# ===============================================

# What should I have done?

# You've probably heard of E = mc2 where E
# denotes energy (in joules), m denotes mass (in kilograms) and
# c denotes the speed of light (approximately equal to 30,000,000 m/s).
# In fact, this formula means that energy
# and mass are equivalent.
# In a file named einstein.py, write a program that receives mass (in kilograms)
# from the user in int form, puts it in the formula,
# and outputs its energy (in joules) in int form.

# ===============================================

def calculate_energy(m):
    c = 300000000
    return int(m * c ** 2)


mass = input("[?] Enter the mass in kg: ")
energy = calculate_energy(int(mass))
print(energy)


# ===============================================

# OUtPut's :

# [?] Enter the mass in kg: 1
# 90000000000000000

# [?] Enter the mass in kg: 14
# 1260000000000000000

# [?] Enter the mass in kg: 50
# 4500000000000000000

# ===============================================
