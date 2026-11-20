"""Task 17: Euler ODE - loan amortization"""
import numpy as np
import matplotlib.pyplot as plt


def main():
    initial_balance = 500000.0
    monthly_rate = 0.01
    monthly_payment = 11122.22
    step, end_month = 1.0, 60

    # End at month 60 even if the last time step has to be shorter.
    months = np.append(np.arange(0, end_month, step), end_month)
    balance = np.zeros_like(months)
    balance[0] = initial_balance

    for i, duration in enumerate(np.diff(months)):
        balance_rate = monthly_rate * balance[i] - monthly_payment
        balance[i + 1] = max(0.0, balance[i] + duration * balance_rate)

    print(f"Balance after {end_month} months (Euler): KES {balance[-1]:.2f}")

    plt.plot(months, balance, marker="o", markersize=3)
    plt.xlabel("Month")
    plt.ylabel("Loan balance (KES)")
    plt.title("Loan amortization via Euler method")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
