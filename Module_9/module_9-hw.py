phone_dict = {}


def input_error(func):
    def inner(user_info):
        try:
            result = func(user_info)
            return result
        except KeyError:
            return "Wrong input! << " + user_info + " >> No entered name in phone book."
        except ValueError:
            return "Wrong input! << " + user_info + " >> Give me name and phone number, please."
        except IndexError:
            return "Wrong input! << " + user_info + " >> Enter user`s name, please."
    return inner


@input_error
def handler_add(user_info):
    global phone_dict
    user_info_a = user_info.split(" ")
    name, phone = user_info_a
    phone_dict[name] = phone
    return f"{name} added to phone book."


@input_error
def handler_change(user_info):
    user_info_a = user_info.split(" ")
    for key, value in phone_dict.items():
        if key == user_info_a[0]:
            phone_dict[key] = user_info_a[1]
    return f"{user_info_a[0]} changed phone number on {user_info_a[1]}"


@input_error
def handler_phone(user_info):
    user_info_a = user_info.split()
    return f"{user_info_a[0]} has phone number - {phone_dict[user_info]}"


def handler_show_all():
    result = "All contacts in phone book:\n".format()
    for key, val in phone_dict.items():
        result += ('{} - {}\n'.format(key, val))
    return result


@input_error
def parser_users_input(user_info):
    user_info_1 = user_info.split(" ")
    if len(user_info_1[0]) > 0 and 10 == len(user_info_1[1]) or\
            len(user_info_1[1]) == 12 and user_info_1[1].isdigit():
        handler_add(user_info)
        handler_change(user_info)
    if len(user_info_1[0]) == 0 or 10 > len(user_info_1[1]) or\
            len(user_info_1[1]) > 12 or not user_info_1[1].isdigit():
        print("Wrong input name or phone number! Check, please.")
    return user_info


def main():
    while True:
        user_ans = input("Phone book bot\n>>").lower()
        user_ans_a = user_ans.split(" ")
        for i in user_ans_a:
            if i == "hello":
                print("How can I help you?")
            if i == "add":
                user_info = input("Give me name and phone number, please\n"
                                  "(between name and phone number must be space)\n>>").lower()
                parser_users_input(user_info)
                print(handler_add(user_info))
            if i == "change":
                user_info = input("Give me name and new phone number, please\n"
                                  "(between name and phone number must de space)\n>>").lower()
                parser_users_input(user_info)
                print(handler_change(user_info))
            if i == "phone" and i == user_ans_a[0]:
                user_info = input("Enter only name, please\n>>").lower()
                print(handler_phone(user_info))
        if user_ans == "show all":
            print(handler_show_all())
        if user_ans == "good bye" or user_ans == "close" or user_ans == "exit":
            print("Good bye!")
            break


if __name__ == "__main__":
    main()
