def s_calc():
    try:
        r_val = float(input("Укажите радиус: "))
        h_val = float(input("Укажите высоту: "))

    except NameError:
        return
    s_side = 2 * 3.14 * r_val * h_val
    s_circle = 3.14 * r_val ** 2
    s_full = s_side + 2 * s_circle
    return s_side, s_full


s_side_val, s_full_val = s_calc()
print(f"Площадь боковой пов-ти - {s_side_val}; Полная площадь -{s_full_val}")
