import os
import random

def create_random_files(n, num_nodes):
    for i in range(n):
        with open(os.path.join('data', f'random_file{i+1}.txt'), 'w') as f:
            nodes = [random.randint(1, 100) for _ in range(num_nodes)]
            f.write(str(num_nodes) + '\n')
            f.write(' '.join(map(str, nodes)) + '\n')

def generate_degraded_bst_data(n):
    data = random.sample(range(1, n+1), n)
    data.sort(reverse=True)
    return data

def create_degraded_files(n, num_nodes):
    for i in range(n):
        with open(os.path.join('data', f'degraded_file{i+1}.txt'), 'w') as f:
            nodes = generate_degraded_bst_data(num_nodes)
            f.write(str(num_nodes) + '\n')
            f.write(' '.join(map(str, nodes)) + '\n')

os.makedirs('data', exist_ok=True)

create_degraded_files(5, 10)
create_random_files(5, 10)
