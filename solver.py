import sympy as sp

def solve_equation(equation_str):
    """ Solve a simple linear equation using sympy. """
    try:
        lhs, rhs = equation_str.split('=')
        x = sp.symbols('x')
        expr = sp.Eq(sp.sympify(lhs), sp.sympify(rhs))
        solution = sp.solve(expr, x)
        return solution
    except Exception as e:
        return f"Error solving equation: {e}"
