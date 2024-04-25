#przystosowanie main.py pod testy


import os
import random

NAZWA_TESTOWANEJ_FUNKCJI = 'FindMinMax' # -> TUTAJ PODAJ FUNKCJE KTORA CHCESZ TESTOWAC

def create_random_files(start, end, step):
    for num_nodes in range(start, end+1, step):
        with open(os.path.join('data', f'random_file{num_nodes}.txt'), 'w') as f:
            nodes = [random.randint(1, 100) for _ in range(num_nodes)]
            f.write(str(num_nodes) + '\n')
            f.write(' '.join(map(str, nodes)) + '\n')
            # f.write(NAZWA_TESTOWANEJ_FUNKCJI + '\n') 
            f.write('PrintTotalTime\n')
            

def generate_degraded_bst_data(n):
    data = random.sample(range(1, n+1), n)
    data.sort(reverse=True)
    return data

def create_degraded_files(start, end, step):
    for num_nodes in range(start, end+1, step):
        with open(os.path.join('data', f'degraded_file{num_nodes}.txt'), 'w') as f:
            nodes = generate_degraded_bst_data(num_nodes)
            f.write(str(num_nodes) + '\n')
            f.write(' '.join(map(str, nodes)) + '\n')
            # f.write(NAZWA_TESTOWANEJ_FUNKCJI + '\n') 
            f.write('PrintTotalTime\n')

os.makedirs('data', exist_ok=True)

create_degraded_files(10, 100, 10)
create_random_files(10, 100, 10)