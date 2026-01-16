import numpy as np
import pandas as pd

# ------------------------------
# MONTE CARLO SIMULATION FUNCTION
# ------------------------------

def monte_carlo_car_purchase(n_simulations=10000, seed=42):
    """
    Monte Carlo simulation to estimate probability of a car owner buying a car.
    
    Args:
        n_simulations (int): Number of people to simulate
        seed (int): Random seed for reproducibility
    
    Returns:
        pandas DataFrame with simulated data and purchase decision
    """

    np.random.seed(seed)

    # ------------------------------
    # 1. Generate random features
    # ------------------------------
    
    # Income in $ (10k to 100k)
    income = np.random.randint(10000, 100001, n_simulations)

    # Age in years (18-70)
    age = np.random.randint(18, 71, n_simulations)

    # Current car? 0 = No, 1 = Yes
    current_car = np.random.choice([0, 1], n_simulations, p=[0.6, 0.4])

    # Car need factor (0–1), higher = more urgent/likely to buy
    car_need = np.random.rand(n_simulations)

    # ------------------------------
    # 2. Compute probability to buy
    # ------------------------------

    # Base probability influenced by income (normalize to 0-1)
    prob_income = income / 100000

    # Age factor: people 25-50 more likely
    prob_age = np.where((age >= 25) & (age <= 50), 0.8, 0.4)

    # Current car reduces probability
    prob_car = np.where(current_car == 1, 0.3, 1.0)

    # Combine all factors into a probability (0-1)
    prob_buy = prob_income * 0.4 + prob_age * 0.3 + car_need * 0.2 + prob_car * 0.1

    # Clip probability to 0-1
    prob_buy = np.clip(prob_buy, 0, 1)

    # ------------------------------
    # 3. Decide purchase (Monte Carlo)
    # ------------------------------

    purchase = np.random.rand(n_simulations) < prob_buy

    # ------------------------------
    # 4. Create DataFrame
    # ------------------------------
    
    df = pd.DataFrame({
        "income": income,
        "age": age,
        "current_car": current_car,
        "car_need": car_need.round(2),
        "prob_buy": prob_buy.round(2),
        "purchase": purchase
    })

    return df

# ------------------------------
# 5. RUN SIMULATION
# ------------------------------

if __name__ == "__main__":
    df_simulation = monte_carlo_car_purchase(n_simulations=10000)

    # Print first 10 simulated users
    print(df_simulation.head(10))

    # Estimate probability of purchase
    purchase_rate = df_simulation['purchase'].mean()
    print(f"\nEstimated probability of buying a car: {purchase_rate*100:.2f}%")

