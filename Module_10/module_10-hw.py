from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, name, contact=[]):
        self.data[name] = Record(name, Phone(contact))

    def change_record(self, name, contact):
        self.data[name] = Record(name, Phone(contact))

    def show_phone(self, name):
        return self.data[name]

    def delete_record(self, name):
        self.data.pop(name)

    def __str__(self):
        result = "All contacts in Address book:\n"
        for val in self.data.values():
            result += f'{str(val)}\n'
        return result


class Field:
    pass


class Name:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name.title()

    def func(self):
        return self.name


def input_error(func):
    def inner(user_input):
        try:
            result = func(user_input)
            return result
        except TypeError:
            return "Wrong Input! Check the name and contact information, please."
        except KeyError:
            return "Wrong input! No entered name in Address book."
        except ValueError:
            return "Wrong input! Give me name and contact information, please."
        except IndexError:
            return "Wrong input! Enter name, please."
    return inner


class Phone:
    def __init__(self, phone=[]):
        self.phone = phone

    def add(self, contact):
        self.phone.append(contact)

    def change(self, old_contact, new_contact):
        if old_contact in self.phone:
            self.delete(old_contact)
            self.add(new_contact)

    def delete(self, contact):
        self.phone.remove(contact)

    def __str__(self):
        return str(self.phone)


class Record:
    def __init__(self, name, phone=Phone()):
        self.name = Name(name)
        self.phone = phone

    def add(self, name, contact):
        self.phone.add(contact)

    def delete(self, name, contact):
        self.phone.delete(contact)

    def __str__(self):
        return f'{self.name}: {self.phone}'


@input_error
def parser_users_input(user_input):
    name, phone = user_input.split(" ")
    if not user_input.startswith(" ") and phone[1:].isdigit():
        address_book.add_record(name.title(), phone)
        address_book.change_record(name.title(), phone)
    elif not user_input.startswith(" ") and not phone.isdigit() and phone.count("@", 0, -1) != 0:
        address_book.add_record(name.title(), phone)
        address_book.change_record(name.title(), phone)
    else:
        print("Wrong input name or contact information! Check, please.")


address_book = AddressBook()


def main():
    while True:
        user_ans = input("Phone book bot\n>>").lower()
        user_ans_a = user_ans.split(" ")
        for i in user_ans_a:
            if i == "hello":
                print("How can I help you?")
            if i == "add":
                add_command()
            if i == "change":
                change_command()
            if i == "phone" and i == user_ans_a[0]:
                phone_command()
            if i == "delete":
                delete_command()
        if user_ans == "show all":
            print(address_book)
        if len(user_ans) == 0:
            print("Empty input!")
        if user_ans == "good bye" or user_ans == "close" or user_ans == "exit":
            print("Good bye!\nHope see you soon!")
            break


def add_command():
    user_input = input("Give me name and contact information to add, please\n"
                       "(between name and contact information must be space)\n>>").lower()
    parser_users_input(user_input)
    print(f"{user_input.title().split(' ')[0]}`s contact information {user_input.split(' ')[1]} added to Address book.")


def change_command():
    user_input = input("Give me name and new contact information to change, please\n"
                       "(between name and contact information must de space)\n>>").lower()
    parser_users_input(user_input)
    print(f"{user_input.split(' ')[0]}`s contact information changed on {user_input.split(' ')[1]}.")


def phone_command():
    user_info = input("Enter only name, please\n>>").lower()
    print(f"{address_book.show_phone(user_info.title())}")


def delete_command():
    user_input = input("Are you sure?\nIf <<YES>>\nGive me name to delete all contact details, please\n"
                       "If <<NO>>\nEnter <<No>>\n>>").lower()
    for i in user_input.split():
        if i == "no":
            continue
        else:
            address_book.delete_record(user_input.title())
        print(f"{user_input.title()} was successfully deleted form Address Book.")


if __name__ == "__main__":
    main()
