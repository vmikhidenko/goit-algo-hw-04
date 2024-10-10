import timeit
import random
import matplotlib.pyplot as plt
import pandas as pd

# Визначаємо функції сортування
def merge_sort(arr):
    # Якщо масив має лише один елемент або пустий, повертаймо його як є
    if len(arr) <= 1:
        return arr

    # Розділяємо масив на дві половини
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Рекурсивно сортуємо та об'єднуємо частини
    return merge(merge_sort(left_half), merge_sort(right_half))

# Функція для об'єднання двох відсортованих частин
def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Порівнюємо елементи з лівої та правої частин та додаємо менший
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Додаємо залишки елементів з лівої частини
    merged.extend(left[left_index:])
    # Додаємо залишки елементів з правої частини
    merged.extend(right[right_index:])
    return merged

# Функція сортування вставками
def insertion_sort(lst):
    # Проходимо по всіх елементах списку, починаючи з другого
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        # Переміщуємо елементи, які більші за ключ, вправо
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

# Підготовка даних для тестування
small_data = [random.randint(0, 1000) for _ in range(100)]
medium_data = [random.randint(0, 1000) for _ in range(1000)]
large_data = [random.randint(0, 1000) for _ in range(10000)]

# Функція для тестування алгоритмів сортування
def test_sorting_algorithms():
    # Створюємо копії даних для кожного алгоритму сортування
    small_copy = small_data[:]
    medium_copy = medium_data[:]
    large_copy = large_data[:]

    results = []

    # Тестуємо Timsort (вбудована функція sorted)
    results.append(("Timsort (small)", timeit.timeit(lambda: sorted(small_copy), number=10)))
    results.append(("Timsort (medium)", timeit.timeit(lambda: sorted(medium_copy), number=10)))
    results.append(("Timsort (large)", timeit.timeit(lambda: sorted(large_copy), number=10)))

    # Тестуємо сортування злиттям
    results.append(("Merge Sort (small)", timeit.timeit(lambda: merge_sort(small_copy), number=10)))
    results.append(("Merge Sort (medium)", timeit.timeit(lambda: merge_sort(medium_copy), number=10)))
    results.append(("Merge Sort (large)", timeit.timeit(lambda: merge_sort(large_copy), number=10)))

    # Тестуємо сортування вставками (лише для маленьких даних через його неефективність на більших)
    results.append(("Insertion Sort (small)", timeit.timeit(lambda: insertion_sort(small_copy), number=10)))

    # Повертаємо результати у вигляді DataFrame
    df = pd.DataFrame(results, columns=["Algorithm", "Time (seconds)"])
    return df

# Запускаємо тестування та отримуємо результати
result_df = test_sorting_algorithms()

# Функція для побудови графіку порівняння часу сортування
def plot_sorting_comparison(df):
    # Отримуємо дані для побудови графіку
    algorithms = df["Algorithm"]
    times = df["Time (seconds)"]

    # Створюємо стовпчиковий графік для часу виконання кожного алгоритму сортування
    plt.figure(figsize=(10, 6))
    plt.barh(algorithms, times, color='lightblue', edgecolor='black')
    plt.xlabel('Час (секунди)')
    plt.title('Порівняння продуктивності алгоритмів сортування')
    plt.gca().invert_yaxis()  # Інвертуємо вісь Y для кращої читабельності
    plt.grid(True, axis='x', linestyle='--', linewidth=0.5)
    plt.tight_layout()

    # Відображаємо графік
    plt.show()

# Побудова графіку з використанням даних продуктивності
plot_sorting_comparison(result_df)
