while True:
    try:
        array = [int(x) for x in input("Введите целые числа в любом порядке, через пробел: ").split()]
        break
    except ValueError:
        print("Нужно ввести целые числа!")


def merge_sort(array):
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


array = merge_sort(array)
print(array)

while True:
    try:
        element = int(input("Введите любое целое число не выходящее за границы списка: "))
        if element < min(array) or element > max(array):
            print("Указанное число не входит в диапазон списка!")
        else:
            break
    except ValueError:
        print("Нужно ввести целое число!")


def binary_search(array, element, left, right):
    middle = (left + right) // 2
    if array[middle] == element:
        return print(f'Позиция указанного числа {middle}')
    elif element < array[middle] and element > array[middle - 1]:
        return print(f'Указанное число занимает позицию между {middle - 1} и {middle}')
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


binary_search(array, element, 0, len(array) - 1)
