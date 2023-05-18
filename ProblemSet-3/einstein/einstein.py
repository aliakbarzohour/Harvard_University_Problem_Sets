

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
