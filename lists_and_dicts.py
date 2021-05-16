# Lists

example_list = [3, 5, 7, 9, 10.5]
print(example_list)
example_list.append('Python')
print(example_list)  # Проверяем, добавился ли новый элемент в список
print(f'Длина списка: {len(example_list)}')
print(f'Первый элемент: {example_list[0]}')
print(f'Последний элемент: {example_list[-1]}')
print(f'Элементы со 2 по 4 :{example_list[1:4]}')
example_list.remove('Python')
print(example_list)  # Проверяем, удалился ли элемент в списке

# Dicts
example_dict = {"city": "Москва", "temperature": "20"}
print(f"Значение ключа city: {example_dict['city']}")
example_dict['temperature'] = int(example_dict['temperature']) - 5
print(example_dict)
print(f"Проверка наличия ключа country - "
      f"{example_dict.get('country')}")
example_dict.get("country", "Россия")
example_dict['date'] = '27.05.2019'
print(example_dict)  # Проверяем, добавился ли новый элемент в словарь
print(f'Длина словаря: {len(example_dict)}')
