"""Task 09: Eigenvalues - bank systemic risk"""
import numpy as np

banks = np.array([
    [0., 1., 1., 0.],
    [1., 0., 1., 1.],
    [1., 1., 0., 1.],
    [0., 1., 1., 0.]
])

# The lending matrix is symmetric, so the eigenpairs are real and ordered.
eigenvalues, eigenvectors = np.linalg.eigh(banks)

dom_value = eigenvalues[-1]
dom_vec = np.abs(eigenvectors[:, -1])
scores = dom_vec / dom_vec.sum()

names = ["Bank A", "Bank B", "Bank C", "Bank D"]

print(f"Dominant eigenvalue: {dom_value:.4f}")
print("\nSystemic importance scores:")
for n, s in zip(names, scores):
    print(f"  {n}: {s:.4f}")
leaders = [name for name, score in zip(names, scores) if np.isclose(score, scores.max())]
print("\nMost systemic:", ", ".join(leaders))
