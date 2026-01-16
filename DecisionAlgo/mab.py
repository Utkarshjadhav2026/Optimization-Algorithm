import random

class Candidate:
    """
    Represents a job candidate (an arm in the bandit problem)
    Each candidate has a true probability of being a 'successful hire'
    """
    def __init__(self, name, success_prob):
        self.name = name
        self.success_prob = success_prob  # unknown to the hiring manager
        self.trials = 0   # times this candidate was selected
        self.successes = 0  # number of successful outcomes

    def hire(self):
        """
        Simulate hiring this candidate.
        Returns 1 if successful, 0 if not.
        """
        result = 1 if random.random() < self.success_prob else 0
        self.trials += 1
        self.successes += result
        return result

def epsilon_greedy(candidates, epsilon=0.1):
    """
    Epsilon-Greedy strategy:
    - With probability epsilon: explore (choose a random candidate)
    - With probability 1-epsilon: exploit (choose candidate with highest success rate so far)
    """
    if random.random() < epsilon:
        # Explore: choose a random candidate
        chosen = random.choice(candidates)
    else:
        # Exploit: choose candidate with highest estimated success rate
        chosen = max(candidates, key=lambda c: c.successes / c.trials if c.trials > 0 else 0)
    return chosen

def simulate_hiring(candidates, rounds=50, epsilon=0.1):
    """
    Simulate multiple hiring rounds to find the best candidate
    """
    for i in range(rounds):
        candidate = epsilon_greedy(candidates, epsilon)
        result = candidate.hire()
        print(f"Round {i+1}: Hired {candidate.name} -> {'Success' if result else 'Fail'}")
    
    # Show final statistics
    print("\n=== Hiring Results ===")
    for c in candidates:
        success_rate = c.successes / c.trials if c.trials > 0 else 0
        print(f"{c.name}: Hired {c.trials} times, Success rate: {success_rate:.2f}")

    # Best candidate based on observed data
    best_candidate = max(candidates, key=lambda c: c.successes / c.trials if c.trials > 0 else 0)
    print(f"\nBest candidate to hire: {best_candidate.name} with observed success rate {best_candidate.successes / best_candidate.trials:.2f}")

# -------------------------------
# Interactive part: define candidates
# -------------------------------

print("Welcome to the Interactive Hiring Simulator!\n")
num_candidates = int(input("Enter number of candidates: "))
candidates = []

for i in range(num_candidates):
    name = input(f"Enter name of candidate {i+1}: ")
    success_prob = float(input(f"Enter hidden success probability for {name} (0 to 1): "))
    candidates.append(Candidate(name, success_prob))

rounds = int(input("\nEnter number of hiring rounds to simulate: "))
epsilon = float(input("Enter epsilon (exploration rate, e.g., 0.1): "))

# Run simulation
simulate_hiring(candidates, rounds, epsilon)