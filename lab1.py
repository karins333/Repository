import itertools


def signed_permutations(n):
    numbers = list(range(1, n + 1))
    perms = itertools.permutations(numbers)
    signed_perms = []

    for perm in perms:

        for signs in itertools.product([-1, 1], repeat=n):
            signed_perm = [str(sign * num) for sign, num in zip(signs, perm)]
            signed_perms.append(" ".join(signed_perm))

    return signed_perms


try:
    n = int(input("Введите n (≤ 6): ").strip())
    if n > 6:
        print("Ошибка: n должно быть ≤ 6")
    else:
        signed_perms = signed_permutations(n)
        print(len(signed_perms))
        for perm in signed_perms:
            print(perm)
except ValueError:
    print("Ошибка: введите целое число")