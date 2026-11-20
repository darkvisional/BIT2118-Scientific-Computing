"""Task 10: Estimate break-even volume with two root-finding methods."""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import root_scalar


def main():
    fixed_cost = 2000
    margin = 20
    cost_growth = 0.01
    tolerance = 1e-10


    def profit(units):
        return margin * units - fixed_cost - cost_growth * units**2


    solution = root_scalar(profit, bracket=[0, 500], method="bisect", xtol=tolerance)

    # Rearrange profit = 0 to get the next estimate for units sold.
    units = 0.0
    for iteration in range(1, 101):
        next_units = (fixed_cost + cost_growth * units**2) / margin
        if abs(next_units - units) < tolerance:
            units = next_units
            break
        units = next_units
    else:
        raise RuntimeError("Fixed-point iteration did not converge.")

    print(f"Bisection break-even  : {solution.root:.2f} units")
    print(f"Fixed-point break-even: {units:.2f} units ({iteration} iterations)")
    print(f"Profit at break-even  : KES {profit(solution.root):.6f}")

    q_vals = np.linspace(0, 500, 300)
    plt.plot(q_vals, profit(q_vals))
    plt.axhline(0, linewidth=0.8)
    plt.axvline(solution.root, linestyle="--", label=f"Break-even = {solution.root:.1f}")
    plt.xlabel("Units sold")
    plt.ylabel("Profit (KES)")
    plt.title("Break-even analysis")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
