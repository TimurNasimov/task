def get_pass(num):
    pass_new = ''
    for i in range(1, num):
        for j in range(2, num):
            if j <= i:
                continue
            elif num % (i + j) == 0:
                pass_new += str(i) + str(j)
    return pass_new


n = int(input('Введите любое целое число от 3 до 20 включительно: '))

result = get_pass(n)
print('Ваш пароль:', result)
