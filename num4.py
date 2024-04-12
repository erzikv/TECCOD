def sort_strings_by_length(strings_list):
    """Сортировка списка строк по длине."""
    strings_sorted_ascending = sorted(strings_list, key=len)
    strings_sorted_descending = sorted(strings_list, key=len, reverse=True)
    return strings_sorted_ascending, strings_sorted_descending

# Пример использования:
strings = ["яблоко", "груша", "слива", "абрикос", "вишня", "персик"]
ascending, descending = sort_strings_by_length(strings)
print(f"Список строк по возрастанию длины: {ascending}")
print(f"Список строк по убыванию длины: {descending}")


#Эта программа использует встроенную функцию sorted() для сортировки списка строк.
#Аргумент key=len указывает, что сортировка должна производиться по длине строк. 
#А reverse=True указывает на сортировку в обратном порядке.