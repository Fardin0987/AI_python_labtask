import random
import math


def fitness(x):
    return (x**2) / 2.0 - 3 * x

def ga_solver():
    pop = [format(random.randint(0, 31), '05b') for _ in range(6)]
    print("GA Initial Population:", pop)
    
    for gen in range(15):
        decoded = [int(ch, 2) for ch in pop]
        fits = [max(0.1, fitness(x)) for x in decoded]
        
     
        total_fit = sum(fits)
        probs = [f / total_fit for f in fits]
        mating_pool = random.choices(pop, weights=probs, k=len(pop))
        
      
        next_pop = []
        for i in range(0, len(mating_pool), 2):
            p1, p2 = mating_pool[i], mating_pool[i+1]
            pt = random.randint(1, 4)
            c1, c2 = p1[:pt] + p2[pt:], p2[:pt] + p1[pt:]
          
            c1 = ''.join('1' if b == '0' and random.random() < 0.1 else '0' if random.random() < 0.1 else b for b in c1)
            c2 = ''.join('1' if b == '0' and random.random() < 0.1 else '0' if random.random() < 0.1 else b for b in c2)
            next_pop.extend([c1, c2])
        pop = next_pop

    best_ch = max(pop, key=lambda ch: fitness(int(ch, 2)))
    best_x = int(best_ch, 2)
    print(f"GA Best Result: x = {best_x}, f(x) = {fitness(best_x)}\n")


def simulated_annealing():
    curr_x = random.randint(0, 31)
    curr_fit = fitness(curr_x)
    T, T_min, alpha = 100.0, 0.01, 0.95
    
    while T > T_min:
        neighbor = max(0, min(31, curr_x + random.choice([-1, 1])))
        neighbor_fit = fitness(neighbor)
        delta = neighbor_fit - curr_fit
        
        if delta > 0 or random.random() < math.exp(delta / T):
            curr_x, curr_fit = neighbor, neighbor_fit
        T *= alpha

    print(f"Simulated Annealing Best Result: x = {curr_x}, f(x) = {curr_fit}")

if __name__ == "__main__":
    ga_solver()
    simulated_annealing()