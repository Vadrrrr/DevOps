import json
import math


def quad(a, b, c):
    if (a or b or c) != 0 or isinstance((a, b, c), int):
        disc = b**2-4*a*c
        ans1 = (-b-math.sqrt(disc))/(2*a)
        ans2 = (-b+math.sqrt(disc))/(2*a)

        if ans1 == ans2:
            full_ans = ans1
        else:
            full_ans = [ans1, ans2]

        if a > 1:
            pattern = f'{a}x^2+{b}x+{c}=0'
            result = {'equation': pattern, 'solution': {'discriminant': float(disc), 'x': full_ans}}

            with open('file.json', 'w') as f:
                json.dump(result, f, indent=3)
        elif a == 1:
            pattern = f'x^2+{b}x+{c}=0'
            result = {'equation': pattern, 'solution': {'discriminant': float(disc), 'x': full_ans}}

            with open('file.json', 'w') as f:
                json.dump(result, f, indent=3)
    else:
        return 'Cannot generate a quadratic equation.'
