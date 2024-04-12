def unique_elements(numbers):
    """Возвращает список уникальных элементов."""
    return list(set(numbers))

# Пример использования:
numbers_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = unique_elements(numbers_list)
print(f"Уникальные элементы: {unique_list}")

#Эта функция использует встроенный тип данных set в Python,
#который автоматически удаляет все дубликаты,
#и затем преобразует set обратно в list, чтобы сохранить тип данных списка. 
