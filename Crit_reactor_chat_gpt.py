import numpy as np

def sample_neutron_life_time():
    # assume una distribuzione esponenziale per la vita del neutron
    life_time = np.random.exponential(1.0)
    return life_time

def simulate_neutron(beta, life_time):
    # calcola se il neutron si assorbe o viene riflesso
    probability = np.exp(-beta * life_time)
    if np.random.uniform(0, 1) < probability:
        return False # assorbi
    else:
        return True # riflesso

def calculate_k_eff(beta, num_neutrons):
    # esegui la simulazione Monte Carlo
    absorbed_neutrons = 0
    for i in range(num_neutrons):
        life_time = sample_neutron_life_time()
        if not simulate_neutron(beta, life_time):
            absorbed_neutrons += 1
    k_eff = float(absorbed_neutrons) / float(num_neutrons)
    return k_eff

# valori di input
beta = 0.1
num_neutrons = 100000

# calcola la criticità tramite simulazione Monte Carlo
k_eff = calculate_k_eff(beta, num_neutrons)

# stampa il risultato
print("La criticità del reattore è: ", k_eff)