"""Task 08: Iterative Methods - linked investment accounts"""
import numpy as np
import matplotlib.pyplot as plt

A = np.array([
    [ 3., -1.,  0.,  0.,  0.],
    [-1.,  3., -1.,  0.,  0.],
    [ 0., -1.,  3., -1.,  0.],
    [ 0.,  0., -1.,  3., -1.],
    [ 0.,  0.,  0., -1.,  3.]
])
b = np.array([12., 8., 9., 7., 10.])

def jacobi(A, b, tol=1e-8, max_iter=500):
    D = np.diag(A)
    # Jacobi uses the previous iteration for every account.
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        x_new = (b - R @ x) / D
        error = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x_new, errors
        x = x_new
    return x, errors

def gauss_seidel(A, b, tol=1e-8, max_iter=500):
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        previous = x.copy()
        # Use the updated values for accounts already visited in this pass.
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i + 1:] @ previous[i + 1:]) / A[i, i]

        error = np.linalg.norm(x - previous, ord=np.inf)
        errors.append(error)
        if error < tol:
            break
    return x, errors


jacobi_returns, jacobi_errors = jacobi(A, b)
seidel_returns, seidel_errors = gauss_seidel(A, b)
exact = np.linalg.solve(A, b)

print(f"Jacobi returns (%), {len(jacobi_errors)} iterations:", jacobi_returns)
print(f"Gauss-Seidel returns (%), {len(seidel_errors)} iterations:", seidel_returns)
print("Direct solution (%):", exact)

plt.semilogy(range(1, len(jacobi_errors) + 1), jacobi_errors, label="Jacobi")
plt.semilogy(range(1, len(seidel_errors) + 1), seidel_errors, label="Gauss-Seidel")
plt.xlabel("Iteration")
plt.ylabel("Maximum change (percentage points)")
plt.title("Convergence for linked investment returns")
plt.legend()
plt.grid(True)
plt.show()
