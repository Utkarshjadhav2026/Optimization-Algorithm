import numpy as np

class CandidateMDP:
    """
    Represents a candidate in the MDP framework.
    Each candidate has a probability of success and a reward for successful hire.
    """
    def __init__(self, name, success_prob, reward_success=10, reward_fail=0):
        self.name = name
        self.success_prob = success_prob  # Probability of a successful hire
        self.reward_success = reward_success
        self.reward_fail = reward_fail

    def expected_reward(self):
        """
        Expected reward from hiring this candidate once
        """
        return self.success_prob * self.reward_success + (1 - self.success_prob) * self.reward_fail

def value_iteration(candidates, discount_factor=0.9, iterations=100):
    """
    Compute long-term expected reward for each candidate using Value Iteration
    """
    # Initialize value for each candidate (state)
    values = np.zeros(len(candidates))
    
    for i in range(iterations):
        new_values = np.zeros(len(candidates))
        for idx, candidate in enumerate(candidates):
            # Immediate reward for hiring this candidate
            immediate_reward = candidate.expected_reward()
            
            # Long-term value: discounted value of best next action
            future_reward = discount_factor * max(values)
            
            # Update value
            new_values[idx] = immediate_reward + future_reward
        
        values = new_values

    # Determine optimal strategy
    optimal_idx = np.argmax(values)
    return values, optimal_idx

def interactive_mdp():
    """
    Interactive MDP simulator for hiring decisions
    """
    print("=== Interactive Long-Term Hiring Simulator (MDP) ===\n")
    
    num_candidates = int(input("Enter number of candidates: "))
    candidates = []

    for i in range(num_candidates):
        name = input(f"Enter name of candidate {i+1}: ")
        success_prob = float(input(f"Enter hidden success probability for {name} (0 to 1): "))
        reward_success = float(input(f"Enter reward for successful hire for {name}: "))
        reward_fail = float(input(f"Enter reward for failed hire for {name}: "))
        candidates.append(CandidateMDP(name, success_prob, reward_success, reward_fail))

    discount_factor = float(input("\nEnter discount factor for long-term strategy (0 < gamma < 1, e.g., 0.9): "))
    iterations = int(input("Enter number of iterations for value iteration (e.g., 100): "))

    # Compute optimal strategy
    values, optimal_idx = value_iteration(candidates, discount_factor, iterations)

    print("\n=== Long-Term Expected Rewards ===")
    for idx, candidate in enumerate(candidates):
        print(f"{candidate.name}: Expected Long-Term Reward = {values[idx]:.2f}")
    
    print(f"\nOptimal candidate to hire (long-term strategy): {candidates[optimal_idx].name}")

# Run the interactive simulator
if __name__ == "__main__":
    interactive_mdp()
