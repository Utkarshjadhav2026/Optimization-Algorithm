import numpy as np

# States
states = ["Idle", "Active", "Breakdown"]

# Actions
actions = ["Assign", "Maintain", "Rest"]

# Rewards
rewards = {
    ("Idle", "Assign"): 0,
    ("Active", "Assign"): 10,
    ("Active", "Maintain"): -5,
    ("Breakdown", "Maintain"): -5,
    ("Breakdown", "Rest"): -20
}

# Transition probabilities
P = {
    ("Idle", "Assign"): [("Active", 1.0)],
    ("Active", "Assign"): [("Active", 0.7), ("Breakdown", 0.3)],
    ("Active", "Maintain"): [("Idle", 1.0)],
    ("Breakdown", "Maintain"): [("Idle", 1.0)],
}

gamma = 0.9
V = {s: 0 for s in states}

# Value Iteration
for _ in range(10):
    new_V = {}
    for s in states:
        action_values = []
        for a in actions:
            if (s, a) in P:
                value = rewards.get((s, a), 0)
                for s_next, prob in P[(s, a)]:
                    value += gamma * prob * V[s_next]
                action_values.append(value)
        new_V[s] = max(action_values) if action_values else 0
    V = new_V

print("State Values:", V)
