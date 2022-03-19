import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def fitness(state):
    attacks = 0
    N = len(state)
    for index in range(N):
        for index2 in range(index+1,N):
            if  state[index2] == state[index]:
                attacks += 1
            if abs(state[index2]-state[index]) == abs(index2-index):
                attacks += 1
    total_attacks = (N*(N-1))/2
    return (total_attacks - attacks)        

def is_goal(state):
    N = len(state)
    total_attacks = (N*(N-1))/2
    if(fitness(state) == total_attacks):
        return True
    else:
        return False

def fitness_probs(population):
    fitness_list = []
    prob_list = []
    fitness_sum = 0
    
    for state in population:
        fit = fitness(state)
        fitness_sum = fitness_sum + fit
        fitness_list.append(fit)
    
    for f in fitness_list:
        prob_list.append(f/fitness_sum)
    
    return prob_list


def select_parents(population,probs):
    indices = np.random.choice(len(population),2,p=probs)    
    # states = np.random.choice(population,2,probs)
    return population[indices[0]],population[indices[1]]

def reproduce(parent1,parent2):
    N = len(parent1)
    c = np.random.randint(0,N)
    state = (parent1[0:c]+parent2[c:N])
    return state


def mutate(state,m_rate=0.1):
    float = np.random.uniform(0,1)
    if float > m_rate:
        return state
    else:
        N = len(state)
        first_sample = np.random.randint(0,N)
        second_sample = np.random.randint(0,N)
        asdf = list(state)
        asdf[first_sample] = second_sample
        tt = tuple(asdf)
        # print(tt)
        return tt


def genetic_algorithm(population, m_rate=0.1, max_iters=5000):
    iters = 0
    goal = False
    while iters < max_iters and not goal:
        new_population = []
        probs = fitness_probs(population)
        for i in range(len(population)):
            parents = select_parents(population,probs)
            state = reproduce(parents[0],parents[1])
            state = mutate(state,m_rate)
            # if is_goal(state):
            #     goal = True
            new_population.append(state)
        
        for s in new_population:
            if is_goal(s):
                goal = True
        iters = iters + 1
        population = new_population

    # highest_fitness = fitness(population[0])
    # for i in len(population)-1:
    #     if (fitness(population[i])<fitness(population[i+1])):
    #         highest_fitness = fitness(population[i+1])
    highest = population[0]
    for state in population:
        if fitness(state) > fitness(highest):
            highest = state
        
    return highest, iters


def visualize_nqueens_solution(n_queens, file_name):
    N = len(n_queens)
    array = []
    # print(array)
    for i in range(N):
        col = []
        for j in range(N):
            if n_queens[i] == j:
                # array[j][i] = 1
                col.append(1)
            else:
                col.append(0)
                # array[j][i] = 0
        array.append(col)
    # print(array)
    array2 = np.array(array).T.tolist()
    print(array2)

    plt.figure(figsize=(N, N))
    ax = sns.heatmap(array2,cmap='Purples', linewidths=1.5, linecolor='k', cbar=False)
    plt.savefig(file_name)
    plt.show()