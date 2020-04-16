import timeit

print("1 - Bubble sort(from small to big);\n"
      "2 - Selection sort(from small to big);\n"
      "3 - Insertion sort(from small to big);\n"
      "4 - Bubble sort(from big to small);\n"
      "5 - Selection sort(from big to small);\n"
      "6 - Insertion sort(from big to small);\n")

flag = int(input("Choose what do you want to use: "))

mysetup = '''
import numpy as np
import random
            '''

if flag == 1:
    mycode = '''
def bubbleSort(arr):
    n = len(arr)
    audits = 0 #лічильник перестановок

    # Проходимо по всіх елементах масиву
    for i in range(n):
        swapped = False
        # Останній i-тий елемент на місці
        for j in range(0, n - i - 1):

            # Проходимо по массиву від 0 елемента до n-i-1
            # Міняємо місцями якшо елемент більший ніж наступний
            if arr[j] > arr[j + 1]: 
                audits+=1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Якщо у внутрішньому циклі не мінялися елементи тоді зупиняємо сортування

        if swapped == False:
            break
    print("Audits in this program: ", audits)
    return arr    
    
#Флажок, по якому обираємо вводити елементи масива від руки або за допомогою рандому
q = int(input("press 1 if you want to fill array by yourself, press 2 if you want to fill array by random:"))

if (q == 2):
    array = np.zeros(100, dtype=int) #я викоистовую 100 елементів для того, щоб програма працювала швидше та, щоб було видно увесь масив
    for i in range(100):
        array[i] = random.randint(0, 100)
    print("your array: " , array)
    array = bubbleSort(array)
    print("Sorted array: ", array)
elif q == 1:
    array = np.zeros(30, dtype=int) #створюємо масив із 30 елементів для ручного вводу
    #заповнюємо масив
    for i in range(30): 
        z = int(input())
        array[i] = z
    print("your array: " , array)
    array = bubbleSort(array) #Викликаємо функцію сортування бульбашкою
    print("Sorted array: ", array) 
'''
elif flag == 2:
    mycode = '''

def selectionSort(arr):
    audits = 0 #лічильник перестановок
    for i in range(len(arr)):
        # Знаходимо мінімальний елемент у масиві
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
            # Міняємо місцями знайдений мінімальний елемент з першим елементом   
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 
        audits+=1
        print("Audits in this program: ", audits)
    return arr
    
#Флажок, по якому обираємо вводити елементи масива від руки або за допомогою рандому
q = int(input("press 1 if you want to fill array by yourself, press 2 if you want to fill array by random:"))
if (q == 2):
    array = np.zeros(100, dtype=int)
    for i in range(100):
        array[i] = random.randint(0, 100)
    print("your array: " , array)
    array = selectionSort(array)#Викликаємо функцію selectionSort()
    print("Sorted array: ", array)
elif q == 1:
    array = np.zeros(30, dtype=int)
    for i in range(30):
        z = int(input())
        array[i] = z
    print("your array: " , array)
    array = selectionSort(array)#Викликаємо функцію selectionSort()
    print("Sorted array: ", array) 
'''
elif flag == 3:
    mycode = '''
def insertionSort(arr):
    audits = 0 #лічильник перестановок
    for i in range(1, len(arr)):
        key = arr[i]
    # Перемістимо елементи arr[0..i-1], які
    # більше ніж key, на одне положення вперед
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        audits+=1
        arr[j + 1] = key
    print("Audits in this program: ", audits)
    return arr

#Флажок, по якому обираємо вводити елементи масива від руки або за допомогою рандому
q = int(input("press 1 if you want to fill array by yourself, press 2 if you want to fill array by random:"))
if (q == 2):
    array = np.zeros(100, dtype=int)
    for i in range(100):
        array[i] = random.randint(0, 100)
    print("your array: " , array)
    array = insertionSort(array)#Викликаємо функцію insertionSort()
    print("Sorted array: ", array)
elif q == 1:
    array = np.zeros(30, dtype=int)
    for i in range(30):
        z = int(input())
        array[i] = z
    print("your array: " , array)
    array = insertionSortt(array)#Викликаємо функцію insertionSort()
    print("Sorted array: ", array) 
'''
elif flag == 4:
    mycode = '''
# увесь цей фрагмент коду аналігчний до першого, окрім переміщення в циклі, ми все порівняюємо та переміщуємо в іншу сторону
def bubbleSort(arr):
    audits = 0 #лічильник перестановок
    n = len(arr)
    audits = 0

    # Проходимо по всіх елементах масиву
    for i in range(n):
        swapped = False
        # Останній i-тий елемент на місці
        for j in range(0, n - i - 1):

            # Проходимо по массиву від 0 елемента до n-i-1
            # Міняємо місцями якшо елемент менший ніж наступний
            if arr[j] < arr[j + 1]: 
                audits+=1
                arr[j+1], arr[j] = arr[j], arr[j+1]
                swapped = True

        # Якщо у внутрішньому циклі не мінялися елементи тоді зупиняємо сортування

        if swapped == False:
            break
    print("Audits in this program: ", audits)
    return arr    
    
#Флажок, по якому обираємо вводити елементи масива від руки або за допомогою рандому
q = int(input("press 1 if you want to fill array by yourself, press 2 if you want to fill array by random:"))

if (q == 2):
    array = np.zeros(100, dtype=int) #я викоистовую 100 елементів для того, щоб програма працювала швидше та, щоб було видно увесь масив
    for i in range(100):
        array[i] = random.randint(0, 100)
    print("your array: " , array)
    array = bubbleSort(array)
    print("Sorted array: ", array)
elif q == 1:
    array = np.zeros(30, dtype=int) #створюємо масив із 30 елементів для ручного вводу
    #заповнюємо масив
    for i in range(30): 
        z = int(input())
        array[i] = z
    print("your array: " , array)
    array = bubbleSort(array) #Викликаємо функцію сортування бульбашкою
    print("Sorted array: ", array) 
    '''
elif flag == 5:
    mycode = '''
# увесь цей фрагмент коду аналігчний до другого, окрім переміщення в циклі, ми все порівняюємо та переміщуємо в іншу сторону

def selectionSort(arr):
    audits = 0 #лічильник перестановок
    for i in range(len(arr)):
        # Знаходимо мінімальний елемент у масиві
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] < arr[j]:
                min_idx = j
            audits += 1
            # Міняємо місцями знайдений мінімальний елемент з першим елементом   
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    print("Audits in this program: ", audits) 
    return arr
    
#Флажок, по якому обираємо вводити елементи масива від руки або за допомогою рандому
q = int(input("press 1 if you want to fill array by yourself, press 2 if you want to fill array by random:"))
if (q == 2):
    array = np.zeros(100, dtype=int)
    for i in range(100):
        array[i] = random.randint(0, 100)
    print("your array: " , array)
    array = selectionSort(array)#Викликаємо функцію selectionSort()
    print("Sorted array: ", array)
elif q == 1:
    array = np.zeros(30, dtype=int)
    for i in range(30):
        z = int(input())
        array[i] = z
    print("your array: " , array)
    array = selectionSort(array)#Викликаємо функцію selectionSort()
    print("Sorted array: ", array) 
'''

elif flag == 6:
    mycode = '''

# увесь цей фрагмент коду аналігчний до третього, окрім переміщення в циклі, ми все порівняюємо та переміщуємо в іншу сторону

def insertionSort(arr):
    audits = 0 #лічильник перестановок
    for i in range(1, len(arr)):
        key = arr[i]
    # Перемістимо елементи arr[0..i-1], які
    # більше ніж key, на одне положення вперед
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            audits+=1
        arr[j+1] = key
    print("Audits in this program: ", audits)
    return arr

#Флажок, по якому обираємо вводити елементи масива від руки або за допомогою рандому
q = int(input("press 1 if you want to fill array by yourself, press 2 if you want to fill array by random:"))
if (q == 2):
    array = np.zeros(100, dtype=int)
    for i in range(100):
        array[i] = random.randint(0, 100)
    print("your array: " , array)
    array = insertionSort(array)#Викликаємо функцію insertionSort()
    print("Sorted array: ", array)
elif q == 1:
    array = np.zeros(30, dtype=int)
    for i in range(30):
        z = int(input())
        array[i] = z
    print("your array: " , array)
    array = insertionSortt(array)#Викликаємо функцію insertionSort()
    print("Sorted array: ", array)
'''
print("time of a program: ", timeit.timeit(setup=mysetup,
                                           stmt=mycode,
                                           number=1))
