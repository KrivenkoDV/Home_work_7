## Задание № 1,2

from pprint import pprint

def dict_collector(file_path):
    with open(file_path, 'rt',encoding ='utf 8' ) as file:
        menu = {}
        for line in file:
            dish_name = line[:-1]
            counter = file.readline().strip()
            list_of_ingridient = []
            for i in range(int(counter)):
                dish_items = dict.fromkeys(['ingredient_name', 'quantity', 'measure'])
                ingridient = file.readline().strip().split(' | ') # читаем строку и определяем разделитель (strip - убирает знаки переноса)
                for item in ingridient:
                    dish_items['ingredient_name'] = ingridient[0]
                    dish_items['quantity'] = ingridient[1]
                    dish_items['measure'] = ingridient[2]
                list_of_ingridient.append(dish_items)
                cook_book = {dish_name: list_of_ingridient}
                menu.update(cook_book)
            file.readline()

    return(menu)

dict_collector('cook_book.txt')

def get_shop_list_by_dishes(dishes, persons=int):

    menu = dict_collector('cook_book.txt')
    print('Задание №1')
    print('Меню :')
    pprint(menu)
    print()
    list = {}

    try:
        for dish in dishes:
            for item in (menu[dish]):
                items_list = dict([(item['ingredient_name'], {'measure': item['measure'], 'quantity': int(item['quantity'])*persons})])
                if list.get(item['ingredient_name']):
                    extra_item = (int(list[item['ingredient_name']]['quantity']) +
                                  int(items_list[item['ingredient_name']]['quantity']))
                    list[item['ingredient_name']]['quantity'] = extra_item

                else:
                    list.update(items_list)

        print('Задание №2')
        print(f"Для приготовления выбранных блюд на {persons} человек нам необходимо купить:")
        pprint(list)
    except KeyError:
        print("Не верно написано наименование блюда!")


get_shop_list_by_dishes(['Утка по-пекински', 'Фахитос'], 3)

## Задание № 3
import os

current = os.getcwd()
folder_name = "files"

file_path = os.path.join(current, folder_name)
files = os.listdir(file_path)

file_dict = {}
for f in files:
    name = os.path.join(file_path,f)
    with open(name, encoding='utf-8') as file:
        lines = file.readlines()
        text = []
        len_text = len(lines)
        for line in lines:
            text.append(line.strip())
        file_dict[f] = (len_text, text)

sorted_values = sorted(file_dict.values())
sorted_dict = {}

for i in sorted_values:
    for k in file_dict.keys():
        if file_dict[k] == i:
            sorted_dict[k] = file_dict[k]
            break

with open('merged_file.txt', "w", encoding='utf-8') as file:
    for key, value in sorted_dict.items():
        file.write(f"{key}\n")
        file.write(f"{value[0]}\n")
        for val in value[1]:
            file.write(f"{val}\n")

print()
print(f'Задание №3 - Файл {file} успешно записан!')