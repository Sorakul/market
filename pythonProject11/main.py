class Product:
    def __init__(self, article, name, cost, number):
        self.article = article
        self.name = name
        self.cost = cost
        self.number = number

    def get_info(self):
        print("------------------------------")
        print("Артикул:", self.article, '\nНазвание:', self.name, '\nСтоимость', self.cost, '\nКоличество', self.number)
        print("------------------------------")


all_products = []


def add_product():
    print("Введите характеристики нового товара")
    flag = True
    while flag:
        flag = False
        article = int(input("Артикул:"))
        for i in all_products:
            if article == i.article:
                print("Товар с таким артикулом уже существует!")
                flag = True
    name = input("Название:")
    cost = int(input("Стоимость:"))
    number = int(input("Количество:"))
    new_product = Product(article, name, cost, number)
    all_products.append(new_product)
    main_menu()


def change_product():
    change_pr_article = int(input("Введите артикул товара, характеристики которого хотите изменить:"))
    print(
        "Выберите какую характеристику товара вы хотите изменить:\n1 - Изменить артикул\n2 - Изменить название\n3 - Изменить количество\n4 - Изменить все характеристики")
    var = int(input())
    for i in all_products:
        if change_pr_article == i.article:
            if var == 1:
                flag = True
                while flag:
                    flag = False
                    change_art = int(input("Введите новый артикул товара:"))
                    for i in all_products:
                        if change_art == i.article:
                            print("Товар с таким артикулом уже существует!")
                            flag = True
                    if not flag:
                        print("Артикул товара успешно изменен с", i.article, "на", change_art)
                        i.article = change_art

            elif var == 2:
                change_name = input()
                print("Имя товара изменено с", i.name, "на", change_name)
                i.name = change_name

            elif var == 3:
                change_number = int(input())
                print("Количество товара изменено с", i.number, "на", change_number)
                i.number = change_number

            elif var == 4:
                flag = True
                while flag:
                    flag = False
                    change_art = int(input("Введите новый артикул товара:"))
                    for i in all_products:
                        if change_art == i.article:
                            print("Товар с таким артикулом уже существует!")
                            flag = True
                    if not flag:
                        print("Артикул товара успешно изменен с", i.article, "на", change_art)
                        i.article = change_art

                change_name = input()
                print("Имя товара изменено с", i.name, "на", change_name)
                i.name = change_name

                change_number = int(input())
                print("Количество товара изменено с", i.number, "на", change_number)
                i.number = change_number

            else:
                print("Такой вариант отсутвует в списке!")
                change_product()

            break

    main_menu()


def delete_product():
    flag = True
    while flag:
        del_prod_art = int(input("Введите артикул товара, который вы хотите удалить из каталога:"))
        for i in all_products:
            if del_prod_art == i.article:
                flag = False
                print("Товар с артикулом", del_prod_art, "удален.")
                all_products.remove(i)
                break
        if flag:
            print("Товара с таким артикулом не найдено!")
    main_menu()


def main_menu():
    for i in all_products:
        i.get_info()
    print("МЕНЮ\n1 - Добавить товар\n2 - Изменить характеристики товара\n3 - Удалить товар\n")
    var = int(input())
    if var == 1:
        add_product()
    if var == 2:
        if len(all_products) != 0:
            change_product()
        else:
            print("В каталоге отсутствуют товары!")
            main_menu()
    if var == 3:
        delete_product()


main_menu()
