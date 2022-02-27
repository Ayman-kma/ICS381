def add(a, b):
    return a + b


def second_min(number_list):
    mylist = list(dict.fromkeys(number_list))
    return insertion_sort(mylist)[1]


def insertion_sort(number_list):
    i = 1
    while i < len(number_list):
        j = i
        while j > 0 and number_list[j-1] > number_list[j]:
            number_list[j], number_list[j-1] = number_list[j-1], number_list[j]
            j = j-1
        i = i + 1
    return number_list
