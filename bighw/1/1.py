# def find_contact():
#     dictionary = []
#     pb = open('phonebook.txt', 'r+', encoding ='utf-8')
#     for line in pb:
#         s = line.split(" ")
#         dict = {
#             "second_name": s[0],
#             "first_name": s[1],
#             "middle_name": s[2],
#             "phone": s[3],
#         }
#         dictionary.append(dict)
#     find_second_name = input("Введите фамилию (обязательно с большой буквы!)")
#     for etem in dictionary:
#         if etem['second_name'] == find_second_name:
#             print("Такой человек есть в списке!")
#         else:
#             print("Такого человека в списке нет!") 