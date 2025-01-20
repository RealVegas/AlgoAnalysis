# Ханойские башни, количество дисков n, количество стержней 3,
# Диски обозначены цифрами от 1 до n. Стержни обозначены буквами a, b, c.

# noinspection PyDefaultArgument
def hanoi_towers(n: int, a: str, b: str, c: str, move_number: list[int] = [1]) -> None:
    if n == 1:
        print(f'{move_number} Диск 1: {a} -> {b}')
        move_number[0] += 1
        return

    hanoi_towers(n - 1, a, c, b)
    print(f'{move_number} Диск {n}: {a} -> {b}')
    move_number[0] += 1
    hanoi_towers(n - 1, c, b, a)


# Запрос количества дисков
while True:
    disk_amount: str = input('Введите количество дисков: ')

    if disk_amount.isnumeric():
        disk_amount: int = int(disk_amount)
        break
    else:
        print('Количество дисков должно быть целым числом\n')

# Запуск решения
print('-' * 100)
print(f'Минимальное количество перекладываний для решения задачи: {2 ** disk_amount - 1}')
print('-' * 100)
print('Решение задачи:')
hanoi_towers(n=disk_amount, a='a', b='b', c='c')