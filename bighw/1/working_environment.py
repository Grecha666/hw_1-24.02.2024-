def show_contacts():
    pb = open('phonebook.txt', 'r', encoding ='utf-8')
    for line in pb:
        print(line)
    pb.close()


def add_contact():
    dictionary = []
    pb = open('phonebook.txt', 'r+', encoding ='utf-8')
    for line in pb:
        s = line.split(" ")
        dict = {
            "second_name": s[0],
            "first_name": s[1],
            "middle_name": s[2],
            "phone": s[3],
        }
        dictionary.append(dict)
    new_contact = input("Напиши новый контакт. Обязательно вводи данные через пробел!")
    contact = new_contact.split()
    print(f"Добавили новый контакт({contact}) в телефонный справочник ")
    pb.writelines(f"{contact[0]} {contact[1]} {contact[2]} {contact[3]}\n")
    pb.close()
    return dictionary


def function_for_replacing_value():

    ID = 'id'
    SECONDE_NAME = 'фамилия'
    FIRST_NAME = 'имя'
    MIDDLE_NAME = 'отчество'
    PHONE = 'телефон'
    HEAD = [ID, SECONDE_NAME, FIRST_NAME, MIDDLE_NAME, PHONE]

    dir = []
    a = open('phonebook.txt', 'r', encoding ='utf-8')
    for i, line in enumerate(a, 1):
    # print(i, '', line)
        row = [i] + line.split()
        b = zip(HEAD, row)
        dir.append(dict(b))
    # dir.append(dict(zip(HEAD, row))) - более компактная запись двух верхних строк
    a = dir
    return a 

def new():

    contact = int(input('Напиши номер контакта, который хочешь скопировать: '))
    k = (function_for_replacing_value())
    # dir = [{'id': 1, 'фамилия': 'Куваев', 'имя': 'Дмитрий', 'отчество': 'Кириллович', 'телефон': '8-916-445-76-98'}, {'id': 2, 'фамилия': 'Кутяпа', 'имя': 'Ольга', 'отчество': 'Станиславовна', 'телефон': '8-987-567-76-77'}, {'id': 3, 'фамилия': 'Батон', 'имя': 'Антон', 'отчество': 'Антонович', 'телефон': '8-654-678-77-78'}, {'id': 4, 'фамилия': '6', 'имя': '6', 'отчество': '6', 'телефон': '6'}]
    p = next((i for i, x in enumerate(k) if x['id'] == contact))
    k = k[p]
    res = list(k.values())
    res =[str(item) for item in res]
    m = ' '.join(res)
    with open('new_book.txt', 'a', encoding ='utf-8') as data:
        data.writelines(m)
    print(f"Контакт {m} записан в новый справочник!")


def main(): #Ф-ия main реализовывает цикл событий. Внутри ф-ии нужно создать бесконечный цикл, который будет общаться через терминал с пользователем
    
    while True:
        print("Что Вы хотите сделать?")
        print("1 - Вывести данные")
        print("2 - Записать новый контакт")
        # print("3 - Найти есть ли контакт в справочнике (поиск выполнить по фамилии)")
        print("4 - Записать контакт в новый телефонный справочник (new_book)")
        print("0 - Выход")

        n = int(input())
        if n == 1:
            show_contacts()
        elif n == 2:
            add_contact()
        # elif n == 3:
        #     find_contact()
        elif n == 4:
            new() 
        elif n == 0:
            break
        else:
            print('Такой команды нет!')

    
if __name__ == "__main__":
    main()




