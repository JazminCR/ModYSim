from sympy import symbols, solve, Eq, exp

x, u = symbols('x u')
F = (-x**2 / 2) + 2*x - 1

# resolvés F(x) = u para despejar x
Fx_inv = solve(Eq(F, u), x)
print(Fx_inv)
