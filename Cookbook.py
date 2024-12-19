def read_recipes(file_name):
    cook_book = {}

    with open(file_name, 'r', encoding='utf-8') as file:
        for _ in range(3):  # Читаем только первые 3 блюда
            dish_name = file.readline().strip()
            if not dish_name:
                break

            ingredient_count = int(file.readline().strip())
            ingredients = []

            for _ in range(ingredient_count):
                ingredient_line = file.readline().strip()
                ingredient_name, quantity, measure = ingredient_line.split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })

            cook_book[dish_name] = ingredients

            # Пустая строка между блюдами
            file.readline()

    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = read_recipes('recipes.txt')

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                if name not in shop_list:
                    shop_list[name] = {
                        'measure': ingredient['measure'],
                        'quantity': ingredient['quantity'] * person_count
                    }
                else:
                    shop_list[name]['quantity'] += ingredient['quantity'] * person_count

    return shop_list


shop_list=get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(shop_list)
