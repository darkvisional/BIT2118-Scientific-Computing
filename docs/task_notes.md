# BIT 2118 task notes

These are the financial adaptations for Tasks 2–20. Each entry identifies the inputs and operation (B), gives a change to try (C), and explains the output (D). The financial scenarios and their assumptions cover section E. All inputs are sample data. To repeat a comparison, edit the indicated input in the matching script, run it again, and restore the original value afterward.

## Task 2 — NumPy arrays

- **Inputs and method.** Twelve monthly account balances are recorded in thousands of Kenyan shillings (KES). Scale the readings to KES, compute their mean and extremes, then multiply by a fixed exchange rate of 0.0077 USD per KES.
- **Change to try.** Change the first reading from 45.2 to 55.2. The mean rises from KES 54,408.33 to KES 55,241.67, while the minimum and maximum stay the same.
- **Interpretation.** The mean gives a typical account level. The low point of KES 38,700 shows the month with the least cash available.

## Task 3 — Vectorization

- **Inputs and method.** Generate one million seeded price changes between −500 and 500 cents for a base price of 1,000 currency units. Convert cents to currency units and calculate percentage changes using a loop and a NumPy array expression.
- **Change to try.** Set the base price to 2,000. All percentage changes halve. The first drops from about 0.274% to 0.137%.
- **Interpretation.** Both methods calculate the same returns. The elapsed times show the benefit of doing the array arithmetic in NumPy on the machine running the script.

## Task 4 — Floating-point errors

- **Inputs and method.** Add 360 payments of KES 4,999.99 using a loop and NumPy. Compare both binary floating-point totals with an exact decimal total.
- **Change to try.** Set the payment text to `"5000.00"`. The loop and NumPy errors become zero because the whole-shilling payments and their sum can be represented exactly.
- **Interpretation.** The original exact total is KES 1,799,996.40. Both floating-point results round to that amount at cent precision, while the scientific notation shows the smaller errors.

## Task 5 — Matrix algebra

- **Inputs and method.** Each of three portfolios holds three assets, valued in millions of KES. Right-multiply the holdings matrix by a matrix of allocation fractions. Each row of allocation fractions sums to one.
- **Change to try.** Replace the first allocation row with `[0.80, 0.20, 0.00]`. The first portfolio changes from `[4.65, 3.35, 2.00]` to `[4.15, 3.85, 2.00]` after rebalancing, and its total stays at KES 10 million.
- **Interpretation.** The row sums show whether each portfolio kept its value. The original allocation determinant of 0.85 describes how the transformation scales volume in the space of holdings.

## Task 6 — Linear systems

- **Inputs and method.** Use the 2×2 coefficient matrix and totals `[23, 14]` as two model constraints on online and in-store sales. Solve `A @ x = b` for the two amounts in thousands of KES.
- **Change to try.** Raise the first total from 23 to 24. Online sales move from 3.47 to 3.37 and in-store sales from 3.58 to 3.89, in thousands of KES.
- **Interpretation.** Each amount is the share implied by both constraints. Multiplying the solution by the coefficient matrix reproduces the input totals.

## Task 7 — Gaussian elimination and LU decomposition

- **Inputs and method.** Use a fixed 3×3 matrix describing three linked loan balances and three monthly payment vectors. Factor the matrix once with LU and reuse the factors for each vector.
- **Change to try.** Raise the first payment in month 1 from KES 5,000 to KES 5,100. The first balance for that month rises from KES 7,357.84 to KES 7,463.69. The other months use their own payment vectors.
- **Interpretation.** Each vector gives the loan balances for that month. Small residuals and agreement with the direct solve for month 1 check that the balances satisfy the equations.

## Task 8 — Iterative methods

- **Inputs and method.** Use a 5×5 system of linked accounts with diagonal coefficients of 3 and adjacent coefficients of −1. Start with zero returns, update them with Jacobi and Gauss–Seidel, and compare both with a direct solve.
- **Change to try.** Raise the first target in `b` from 12 to 13. The first equilibrium return rises from about 6.47% to 6.85%, and the neighboring accounts also move.
- **Interpretation.** Both methods reach the same equilibrium. The graph tracks the largest change between successive estimates, so a line reaching the tolerance earlier takes fewer iterations.

## Task 9 — Eigenvalues and eigenvectors

- **Inputs and method.** Use a symmetric 4×4 matrix with a 1 for each link between banks. Normalize the dominant eigenvector so the centrality scores sum to one.
- **Change to try.** Add a link between Banks A and D by setting both corresponding entries to 1. The dominant eigenvalue rises from about 2.56 to 3, and all four scores become 0.25.
- **Interpretation.** In the original network, B and C tie at about 0.281 because they have the same pattern of connections. The scores describe relative network centrality in this model.

## Task 10 — Bisection and fixed-point iteration

- **Inputs and method.** Profit is modeled as KES `20q − 2000 − 0.01q²` for `q` units. Find its zero on [0, 500] using bisection and the rearranged equation using fixed-point iteration.
- **Change to try.** Raise `fixed_cost` from KES 2,000 to KES 2,500. Both methods move the break-even point from about 105.57 to 133.97 units.
- **Interpretation.** On the graph, the profit curve crosses zero at break-even. With the original costs, 106 is the first whole-unit volume in the plotted range with positive profit.

## Task 11 — Newton–Raphson and secant

- **Inputs and method.** A KES 50,000 loan is repaid in five year-end payments of KES 12,000. Find the discount rate at which the present value of the payments equals the loan amount. Newton uses the derivative, and secant uses two starting rates.
- **Change to try.** Raise all five payments to KES 12,500. The rate rises from about 6.40% to 7.93% with the same loan and term.
- **Interpretation.** The rate is the annual borrowing cost implied by the cash flows. The near-zero net present value checks the result.

## Task 12 — Nonlinear equations

- **Inputs and method.** Market demand gives price `100 − 2Q`, and supply gives `10 + Q^1.5`. Assume nonnegative quantities and solve the two price equations together, starting at quantity 20 and price KES 60.
- **Change to try.** Raise the demand intercept from 100 to 110. The equilibrium moves from about 15.24 units at KES 69.51 to 16.50 units at KES 77.01.
- **Interpretation.** At equilibrium the two curves imply the same price. Residuals close to zero verify that the result satisfies both equations.

## Task 13 — Interpolation

- **Inputs and method.** Estimate a stock price between seven hourly observations from 09:00 to 15:00 using linear and cubic interpolation.
- **Change to try.** Change the time passed to both interpolators from 11.5 to 12, and update the output labels. The linear estimate goes from KES 105.25 to KES 107.50, and the cubic estimate also equals KES 107.50 at that measured hour.
- **Interpretation.** Both curves pass through the observations. The linear curve joins them with straight segments, and the cubic curve changes slope smoothly between them.

## Task 14 — Curve fitting

- **Inputs and method.** Fit `a * exp(b * t)` to eight monthly revenues in thousands of KES. Measure the fit with root mean squared error (RMSE).
- **Change to try.** Predict month 10 instead of month 12 by changing the month in the forecast call. The forecast falls from about KES 720,045 to KES 517,260.
- **Interpretation.** The model fits the observations with an RMSE of about KES 1,536. The plotted line past month 8 is a forecast under the same growth model, so its accuracy depends on that growth continuing.

## Task 15 — Numerical differentiation

- **Inputs and method.** Use seven daily closing prices. Estimate price momentum with central differences on inside days and one-sided differences at the ends.
- **Change to try.** Raise the fifth closing price from KES 108.70 to KES 110.70. The estimate on day 4 rises from 3.45 to 4.45 KES per day.
- **Interpretation.** Values above zero on the graph indicate rising prices over the neighboring interval. Values below zero indicate falling prices.

## Task 16 — Numerical integration

- **Inputs and method.** Use 13 monthly rate samples between months 0 and 12. Integrate the rate curve by the trapezoidal and Simpson rules, then apply it to a fixed KES 100,000 balance without compounding.
- **Change to try.** Raise the first rate from 0.50% to 0.60%. The trapezoidal estimate increases from KES 6,940 to KES 6,990, and Simpson's estimate rises from about KES 6,926.67 to KES 6,960.
- **Interpretation.** The estimated interest is the principal times the accumulated rate. The two methods approximate the curve differently between measurements.

## Task 17 — Euler method for ODEs

- **Inputs and method.** Start with a KES 500,000 balance, 1% monthly interest, and a KES 11,122.22 monthly payment. Euler's method updates the balance over 60 months using interest minus the payment as the rate of change.
- **Change to try.** Lower `monthly_payment` to KES 10,500. The balance at month 60 rises from about KES 0.31 to KES 50,816.82.
- **Interpretation.** The graph shows the amount still owed. As the balance shrinks, less of a fixed payment goes to interest, so the balance falls more quickly.

## Task 18 — ODEs with SciPy

- **Inputs and method.** Start with KES 10,000 earning continuously compounded interest at 8% per year. Use `solve_ivp` to integrate `dA/dt = r * A` for ten years and compare it with the exponential formula.
- **Change to try.** Increase `r` from 0.08 to 0.10. The final balance rises from about KES 22,255.41 to KES 27,182.82.
- **Interpretation.** Growth speeds up as the balance increases. The solver and formula curves should overlap at the scale of the graph, with the printed error showing their small difference.

## Task 19 — Numerical optimization

- **Inputs and method.** Allocate a KES 100,000 budget between assets returning 8% and 14%, with risk weights of 0.04 and 0.12. Minimize the weighted risk score while requiring at least KES 10,000 in expected return.
- **Change to try.** Raise `min_ret` to 11% of the budget. The allocation to Asset B rises from roughly KES 33,333 to KES 50,000.
- **Interpretation.** Asset A has the lower risk weight. The minimum-risk allocation holds just enough of the higher-return Asset B to meet the target.

## Task 20 — Monte Carlo simulation

- **Inputs and method.** Simulate 100,000 one-period returns from a normal distribution with mean 8% and standard deviation 15%, using seed 42. Start with KES 100,000 and count final values below KES 80,000.
- **Change to try.** Increase the standard deviation to 20% and leave the seed unchanged. The estimated chance of losing more than 20% rises from 3.129% to 8.210%.
- **Interpretation.** The original fifth-percentile final value is about KES 83,125, meaning roughly 5% of the simulations finish at or below it. The graph shows how the estimated loss probability settles as more draws are included.
