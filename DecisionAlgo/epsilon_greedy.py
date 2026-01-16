import random

drivers = ["A", "B", "C"]
true_rates = {"A": 0.7, "B": 0.5, "C": 0.3}

successes = {d: 0 for d in drivers}
trials = {d: 0 for d in drivers}

epsilon = 0.1
rounds = 1000

def pull(driver):
    return 1 if random.random() < true_rates[driver] else 0

for _ in range(rounds):
    if random.random() < epsilon:
        driver = random.choice(drivers)  # explore
    else:
        driver = max(drivers, key=lambda d: successes[d] / (trials[d] + 1e-5))  # exploit

    reward = pull(driver)
    successes[driver] += reward
    trials[driver] += 1

print("Trials:", trials)
print("Successes:", successes)
