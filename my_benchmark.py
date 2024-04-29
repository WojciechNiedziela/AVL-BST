# Testy wszystkich funkcji

import os
import random, math

NAZWA_TESTOWANEJ_FUNKCJI = 'Rebalance' # -> TUTAJ PODAJ FUNKCJE KTORA CHCESZ TESTOWAC

def generate_unique_nodes(num_nodes):
    # if num_nodes > start:
    #     raise ValueError("num_nodes cannot be greater than start")

    nodes = list(range(1, num_nodes + 1))
    random.shuffle(nodes)
    return nodes[:num_nodes]

# def create_random_files(start, end, step):
#     for num_nodes in range(start, end+1, step):
#         with open(os.path.join('AVL-BST/data', f'random_file{num_nodes}.txt'), 'w') as f:
#             nodes = generate_unique_nodes(num_nodes)
#             f.write(str(num_nodes) + '\n')
#             f.write(' '.join(map(str, nodes)) + '\n')
#             f.write(NAZWA_TESTOWANEJ_FUNKCJI + '\n') 
#             f.write('PrintTotalTime\n')
#             f.write('Exit')
            

def create_random_files(start, end, step):
    num_nodes = start
    while num_nodes <= end:
        with open(os.path.join('AVL-BST/data', f'random_file{num_nodes}.txt'), 'w') as f:
            nodes = generate_unique_nodes(num_nodes)
            f.write(str(num_nodes) + '\n')
            f.write(' '.join(map(str, nodes)) + '\n')
            f.write(NAZWA_TESTOWANEJ_FUNKCJI + '\n') 
            f.write('PrintTotalTime\n')
            f.write('Exit')
        num_nodes *= step  # Multiply num_nodes with step in each iteration


def generate_degraded_bst_data(n):
    data = random.sample(range(1, n+1), n)
    data.sort(reverse=True)
    return data

def create_degraded_files(start, end, step):
    for num_nodes in range(start, end+1, step):
        with open(os.path.join('AVL-BST/data', f'degraded_file{num_nodes}.txt'), 'w') as f:
            nodes = generate_degraded_bst_data(num_nodes)
            f.write(str(num_nodes) + '\n')
            f.write(' '.join(map(str, nodes)) + '\n')
            f.write(NAZWA_TESTOWANEJ_FUNKCJI + '\n') 
            f.write('PrintTotalTime\n')
            f.write('Exit')


os.makedirs('AVL-BST/data', exist_ok=True)

# create_degraded_files(250, 2625, 125)
# create_degraded_files(250*3, 2625*3, 125*3)

create_random_files(pow(2, 6), pow(2, 13), 2)