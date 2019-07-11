import random  # импорт модуля random для генерации списка из случайных элементов, который мы будем сортировать
import datetime  # испорт модуля datetime для записи времени до и после старта оборачиваемой функции


def decorator_speed_test(inside):  # функция-декоратор, принимающая функцию inside
    def decor(*args, **kwargs):  # переменное количество неименованных и именованных аргументов
        start = datetime.datetime.now()  # запись времени до старта функции
        inside(*args, **kwargs)  # оборачиваемая функция
        end = datetime.datetime.now()  # запись времени после исполнения функции
        print(f'Функция {inside.__name__} выполнена за {end - start} секунд.')  # f-строка с разницей таймеров
    return decor  # возврат результата функции-декоратора


@decorator_speed_test  # оборачивание функции декоратором decorator_speed_test
def bubble_sort(sort):  # функция пузырьковой сортировки
    quantity = len(sort)
    for i in range(1, quantity):
        for k in range(0, quantity - i):
            if sort[k] > sort[k + 1]:
                sort[k], sort[k + 1] = sort[k + 1], sort[k]


@decorator_speed_test  # оборачивание функции декоратором decorator_speed_test
def fast_sort(nums):  # функция быстрой сортировки
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return fast_sort(s_nums) + e_nums + fast_sort(m_nums)


to_sort = random.sample(range(100), 100)  # создаем список из 100 случайных элементов со случайным порядком
to_sort_copy = list.copy(to_sort)  # создаем копию списка, т.к. сортировка пузырьком у меня сортирует сам список

bubble_sort(to_sort_copy)  # запуск пузырьковой сортировки в декораторе
fast_sort(to_sort)  # запуск быстрой сортировки в декораторе
