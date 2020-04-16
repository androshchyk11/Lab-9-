import timeit

print("1 - Сocktail sort(from small to big);\n"
      "2 - Shell sort(from small to big);\n"
      "3 - Heapsort(from small to big);\n"
      "4 - Сocktail sort((from big to small);\n"
      "5 - Shell sort(from big to small);\n"
      "6 - Heapsort(from big to small);\n")

flag = int(input("Choose what do you want to use: "))

mysetup = '''
import numpy as np
import random
            '''

if flag == 1:
    mycode = '''
def coctailSort(a):
      n = len(a)
      swapped = True #флажок
      start = 0 # початок
      end = n - 1 # конець
      while (swapped == True):
      # скидуємо розміщений прапор при вході в цикл,
      # оскільки він може бути True після минулої ітерації
            swapped = False

    # Проходимо циклом зправа наліво як у бульбашковому сортуванні
            for i in range(start, end):
                  if (a[i] > a[i + 1]):
                        a[i], a[i + 1] = a[i + 1], a[i]
            swapped = True

    # якщо нічого не мінялось, то массив відосртований
            if (swapped == False):
                  break

    # інакше ставимо флажок = False
            swapped = False

    # зміщуємо кінець на 1 оскільки останній елемент і так уже на своєму місці
            end = end - 1

    # аналогічно до минулих операцій проходимо зправа наліво
            for i in range(end - 1, start - 1, -1):
                  if (a[i] > a[i + 1]):
                        a[i], a[i + 1] = a[i + 1], a[i]
                  swapped = True

    # збільшуємо початок оскільки тепер перше значення стоїть на своєму місці
            start = start + 1
      return a

q = int(input("press 1 if you want to fill array by yourself, press 2 if you want to fill array by random:"))
if (q == 2):
    array = np.zeros(100, dtype=int)
    for i in range(100):
        array[i] = random.randint(0, 100)
    print("your array: " , array)
    array = coctailSort(array)#Викликаємо функцію coctailSort()
    print("Sorted array: ", array)
elif q == 1:
    array = np.zeros(30, dtype=int)
    for i in range(30):
        z = int(input())
        array[i] = z
    print("your array: " , array)
    array = coctailSort(array)#Викликаємо функцію coctailSort()
    print("Sorted array: ", array)
      '''

elif flag == 2:
    mycode = '''

def shellSort(arr):
    n = len(arr)
    gap = n // 2

# Зробіть розрізний тип вставки для цього розміру масиву.
# Перший елемент gap елементів a[0..gap-1] уже в відрізку
# додаємо по одному елементу до відрізку поки увесь відрізок буде відсортований

    while gap > 0:

        for i in range(gap, n):

        # додажмо arr[i] у елементи відрізку які уже відсортовані
            temp = arr[i]

        # зсуємо попередні елементи, відсортовані до розриву, до правильної позиції arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            # ставимо temp (arr[i]) у правильну позицію
            arr[j] = temp
        gap //= 2
    return(arr)
    
    
q = int(input("press 1 if you want to fill array by yourself, press 2 if you want to fill array by random:"))
if (q == 2):
    array = np.zeros(100, dtype=int)
    for i in range(100):
        array[i] = random.randint(0, 100)
    print("your array: " , array)
    array = shellSort(array)#Викликаємо функцію shellSort()
    print("Sorted array: ", array)
elif q == 1:
    array = np.zeros(30, dtype=int)
    for i in range(30):
        z = int(input())
        array[i] = z
    print("your array: " , array)
    array = shellSort(array)#Викликаємо функцію shellSort()
    print("Sorted array: ", array)
'''
elif flag == 3:
    mycode = '''
def heapSort(arr):
    n = len(arr)

    # Створюмо набір елементів.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

        # Один за одним витягуємо елементи
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
    return arr


def heapify(arr, n, i):
    largest = i  # Ініціалізуємо найбільший як основу
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # Якщо left є в основі і більший ніє основа, то
    if l < n and arr[i] < arr[l]:
        largest = l

    # Якщо right є в основі і більший ніє основа, то
    if r < n and arr[largest] < arr[r]:
        largest = r

        # міняємо основу, якщо потрібно
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # посилаємо основу в фукнцію heapify.
        heapify(arr, n, largest)

q = int(input("press 1 if you want to fill array by yourself, press 2 if you want to fill array by random:"))
if (q == 2):
    array = np.zeros(100, dtype=int)
    for i in range(100):
        array[i] = random.randint(0, 100)
    print("your array: " , array)
    array = heapSort(array)#Викликаємо функцію shellSort()
    print("Sorted array: ", array)
elif q == 1:
    array = np.zeros(30, dtype=int)
    for i in range(30):
        z = int(input())
        array[i] = z
    print("your array: " , array)
    array = heapSort(array)#Викликаємо функцію shellSort()
    print("Sorted array: ", array)
    '''

print("time of a program: ", timeit.timeit(setup=mysetup,
                                           stmt=mycode,
                                           number=1))
