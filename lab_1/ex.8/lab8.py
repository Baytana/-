#8. Имена и адреса электронной почты. Напишите программу, которая сохраняет имена и адреса электронной почты в словаре в виде пар 
# "ключ: значение". Программа должна вывести меню, которое позволяет пользователю отыскать адрес электронной почты человека, 
# добавить новое имя и адрес электронной почты, изменить существующий адрес электронной почты и удалить существующие имя и 
# адрес электронной почты. Программа должна законсервировать словарь и сохранить его в файле при выходе пользователя из программы. 
# При каждом запуске программы она должна извлекать словарь из файла и расконсервировать его.

import pickle
import os

def save_contacts(contacts):
    with open('contacts.pkl', 'wb') as f:
        pickle.dump(contacts, f)

def load_contacts():
    if os.path.exists('contacts.pkl'):
        with open('contacts.pkl', 'rb') as f:
            return pickle.load(f)
    else:
        return {}

def find_contact(contacts, name):
    if name in contacts:
        print('---------------------------------')        
        print(f"Адрес электронной почты для {name}: {contacts[name]}")
    else:
        print(f"{name} не найден в списке контактов.")

def add_contact(contacts, name, email):
    contacts[name] = email
    save_contacts(contacts)
    print('---------------------------------')
    print(f"{name} добавлен в список контактов с адресом электронной почты: {email}")

def update_contact(contacts, name, email):
    if name in contacts:
        contacts[name] = email
        save_contacts(contacts)
        print('---------------------------------')
        print(f"Адрес электронной почты для {name} обновлен: {email}")
    else:
        print(f"{name} не найден в списке контактов.")

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print('---------------------------------')
        print(f"{name} удален из списка контактов.")
    else:
        print(f"{name} не найден в списке контактов.")

def main():
    contacts = load_contacts()

    while True:
        print("\nМеню:")
        print("1. Найти адрес электронной почты")
        print("2. Добавить новый контакт")
        print("3. Обновить адрес электронной почты")
        print("4. Удалить контакт")
        print("5. Выйти из программы")

        choice = input("Выберите действие: ")

        if choice == '1':
            name = input("Введите имя для поиска адреса электронной почты: ")
            find_contact(contacts, name)
        elif choice == '2':
            name = input("Введите имя нового контакта: ")
            email = input("Введите адрес электронной почты нового контакта: ")
            add_contact(contacts, name, email)
        elif choice == '3':
            name = input("Введите имя контакта для обновления адреса электронной почты: ")
            if name in contacts:
                email = input("Введите новый адрес электронной почты: ")
                update_contact(contacts, name, email)
            else:
                print(f"{name} не найден в списке контактов.")
        elif choice == '4':
            name = input("Введите имя контакта для удаления: ")
            delete_contact(contacts, name)
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие из меню.")

if __name__ == "__main__":
    main()
