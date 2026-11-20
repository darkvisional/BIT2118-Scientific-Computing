"""Task 04: Floating-point errors in monthly payments."""
from decimal import Decimal

import numpy as np


def main():
    payment_text = "4999.99"
    monthly_payment = float(payment_text)
    months = 360

    naive_total = 0.0
    for _ in range(months):
        naive_total += monthly_payment

    payments = np.full(months, monthly_payment)
    numpy_total = np.sum(payments)
    exact_total = Decimal(payment_text) * months

    # Compare the stored floats with the exact decimal amount.
    naive_error = abs(Decimal.from_float(naive_total) - exact_total)
    numpy_error = abs(Decimal.from_float(float(numpy_total)) - exact_total)

    print(f"Exact total      : KES {exact_total:.2f}")
    print(f"Naive loop total : KES {naive_total:.2f}")
    print(f"NumPy sum total  : KES {numpy_total:.2f}")
    print(f"Naive error      : KES {naive_error:.3e}")
    print(f"NumPy error      : KES {numpy_error:.3e}")
    print(f"Loop within half a cent: {naive_error < Decimal('0.005')}")


if __name__ == "__main__":
    main()
