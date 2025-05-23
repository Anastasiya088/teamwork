import math

def calculate_xk(x, k):
    if k < 0:
        return "k має бути невід'ємним"
    if k == 0:
        return 1.0
    xk = 1.0
    for i in range(1, k + 1):
        xk *= (x * x) / ((2 * i) * (2 * i - 1))
    return xk

def calculate_Pn(n):
    if n < 0:
        return "n має бути невід'ємним"
    if n == 0:
        return 1.0
    Pn = 1.0
    for i in range(1, n + 1):
        Pn *= (1 + 1 / (i * i))
    return Pn

def calculate_Dn(n, a, b):
    if n < 1:
        return "n має бути натуральним числом"
    if n == 1:
        return a + b
    if n == 2:
        return (a + b)**2 - a * b
    d_prev = (a + b)**2 - a * b
    d_prev_prev = a + b
    for i in range(3, n + 1):
        d_current = (a + b) * d_prev - a * b * d_prev_prev
        d_prev_prev = d_prev
        d_prev = d_current
    return d_prev

def calculate_Sn(n):
    if n < 1:
        return "n має бути натуральним числом"
    a = [0] * (n + 3)
    a[1] = 1
    a[2] = 1
    a[3] = 1
    for i in range(4, n + 1):
        a[i] = a[i - 1] + a[i - 3]
    Sn = 0
    for k in range(1, n + 1):
        Sn += a[k] / (2**k)
    return Sn

def calculate_ln_taylor(x, epsilon):
    if abs(x) >= 1:
        return "x має бути в межах (-1, 1)"
    term = x
    result = term
    n = 1
    while abs(term) > epsilon:
        n += 2
        term = (x ** n) / n
        result += term
    return 2 * result

if __name__ == "__main__":
    print("a) Обчислення x_k:")
    x_val_a = 2.0
    k_val_a = 3
    result_a = calculate_xk(x_val_a, k_val_a)
    print(f"x_{k_val_a} для x = {x_val_a} дорівнює: {result_a}\n")

    print("b) Обчислення P_n:")
    n_val_b = 5
    result_b = calculate_Pn(n_val_b)
    print(f"P_{n_val_b} дорівнює: {result_b}\n")

    print("c) Обчислення визначника D_n:")
    n_val_c = 4
    a_val_c = 2
    b_val_c = 3
    result_c = calculate_Dn(n_val_c, a_val_c, b_val_c)
    print(f"Визначник D_{n_val_c} для a = {a_val_c}, b = {b_val_c} дорівнює: {result_c}\n")

    print("d) Обчислення суми S_n:")
    n_val_d = 7
    result_d = calculate_Sn(n_val_d)
    print(f"Сума S_{n_val_d} дорівнює: {result_d}\n")

    print("e) Обчислення ln((1+x)/(1-x)) за допомогою ряду Тейлора:")
    x_val_e = 0.5
    epsilon_val_e = 1e-6
    result_e_taylor = calculate_ln_taylor(x_val_e, epsilon_val_e)
    result_e_math = math.log((1 + x_val_e) / (1 - x_val_e))
    print(f"ln((1+{x_val_e})/(1-{x_val_e})) за рядом Тейлора (точність {epsilon_val_e}): {result_e_taylor}")
    print(f"ln((1+{x_val_e})/(1-{x_val_e})) з бібліотеки math: {result_e_math}")
    print(f"Різниця: {abs(result_e_taylor - result_e_math)}\n")