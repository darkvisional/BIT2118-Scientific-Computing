"""BIT 2118 integrated project: Financial Calculator.

Author: Keith Kyule | Reg: BSCCS/2025/49920
Run with python3 code/Project_Financial_Calculator.py.
"""
import matplotlib.pyplot as plt

import Task_02_numpy_arrays as task02
import Task_03_vectorization as task03
import Task_04_numerical_errors as task04
import Task_05_matrix_algebra as task05
import Task_06_linear_systems as task06
import Task_07_gaussian_lu as task07
import Task_08_iterative_linear as task08
import Task_09_eigenvalues as task09
import Task_10_bisection_fixed_point as task10
import Task_11_newton_secant as task11
import Task_12_nonlinear_equations as task12
import Task_13_interpolation as task13
import Task_14_curve_fitting as task14
import Task_15_numerical_differentiation as task15
import Task_16_numerical_integration as task16
import Task_17_euler_ode as task17
import Task_18_scipy_ode as task18
import Task_19_optimization as task19
import Task_20_monte_carlo as task20


# Keep the original menu numbers and append the three missing tasks.
MENU = {
    "1": ("Portfolio Summary", task02.main),
    "2": ("Vectorized Returns", task03.main),
    "3": ("Precision Check", task04.main),
    "4": ("Portfolio Rebalancing", task05.main),
    "5": ("Budget Allocation", task06.main),
    "6": ("Bank Contagion", task09.main),
    "7": ("Break-Even", task10.main),
    "8": ("Loan IRR", task11.main),
    "9": ("Price Interpolation", task13.main),
    "10": ("Revenue Forecasting", task14.main),
    "11": ("Price Momentum", task15.main),
    "12": ("Total Interest", task16.main),
    "13": ("Loan Amortization", task17.main),
    "14": ("Compound Growth", task18.main),
    "15": ("Portfolio Optimization", task19.main),
    "16": ("Investment Risk", task20.main),
    "17": ("Monthly Loan Balances", task07.main),
    "18": ("Linked Investment Returns", task08.main),
    "19": ("Market Equilibrium", task12.main),
}


def main():
    print("\nBIT 2118 - FINANCIAL CALCULATOR")
    while True:
        print("\nAvailable analyses:")
        for choice, (title, _) in MENU.items():
            print(f"  {choice:>3}. {title}")
        print("    0. Exit")

        try:
            choice = input("\nSelect: ").strip()
        except EOFError:
            choice = "0"
        if choice == "0":
            print("Goodbye.")
            break
        if choice not in MENU:
            print("Invalid choice.")
            continue

        title, run_task = MENU[choice]
        print(f"\n{title}")
        try:
            run_task()
        except Exception as error:
            print(f"Error: {error}")
        finally:
            plt.close("all")


if __name__ == "__main__":
    main()
