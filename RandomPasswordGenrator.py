import random
import string
import os
from colorama import Fore


class colors:
    starter = Fore.LIGHTBLUE_EX
    success = Fore.LIGHTGREEN_EX
    error = Fore.RED
    information = Fore.LIGHTYELLOW_EX
    setting = Fore.MAGENTA


setting = {
    'length': 6,
    'upper': True,
    'lower': True,
    'symbol': True,
    'number': True,
    'space': False,
}
setting_items = {
    '1': f'length of password : {setting["length"]}',
    '2': f'have Upper Case : {setting["upper"]}',
    '3': f'have Lower Case : {setting["lower"]}',
    '4': f'have symbol : {setting["symbol"]}',
    '5': f'have number : {setting["number"]}',
}

PASSWORD_MIN_LENGTH = 4
PASSWORD_MAX_LENGTH = 30


def clear_screen():
    os.system("clear")


def welcome(setting):
    print(colors.information+'*'*5, 'Welcome', '*'*5, sep='')
    # print('-'*20)
    print(show_setting_items(setting))


def get_user_password_length(value, pwd_min_length=PASSWORD_MIN_LENGTH, pwd_max_length=PASSWORD_MAX_LENGTH):
    while True:
        user_input = input(colors.starter+"Enter your password length "
                           f"(defult is {value}) (Enter : defult) : ")
        if user_input == '':
            return value
        if user_input.isdigit():
            if int(user_input) > pwd_min_length and int(user_input) < pwd_max_length:
                return int(user_input)
            else:
                print(colors.error+"you should enter number between"
                      f" {pwd_min_length} and {pwd_max_length}")
                clear_screen()
        else:
            clear_screen()
            print(colors.error+"You should enter numbes.")
        print(colors.error+"Please try again.")


def ask_for_set_or_change_setting(setting):
    while True:
        continue_or_break = input(
            colors.starter+"Do you want to change defult setting (y : yes , n : no  , enter : yes) : ")
        if continue_or_break in ['y', 'n', '']:
            if continue_or_break in ['y', '']:
                get_setting(setting)
            break
        else:
            print(colors.error+"Please Enter correct option.")
            print(colors.error+"Try again")
            clear_screen()
            print(show_setting_items(setting))


def get_yes_or_no_from_user(option, value):
    while True:
        user_input = input(colors.starter+f"Include {option} ? Defult is {value}"
                           " (y : yes , n : no , Enter : defult) ")
        if user_input == '':
            return value
        if user_input in ['y', 'n']:
            return user_input == 'y'

        print(colors.error+"Invalid input , Please try again")
        clear_screen()


def show_setting_items(setting):
    string_for_show = f"""
    [1] length of password : {setting["length"]}
    [2] have Upper Case : {setting["upper"]}
    [3] have Lower Case : {setting["lower"]}
    [4] have symbol : {setting["symbol"]}
    [5] have number : {setting["number"]}
    """
    return colors.setting+string_for_show


def which_option_want_to_change():
    while True:
        user_input = input(
            colors.starter+"Which item do you want to change it (q : back) (Enter number) : ")
        for item, value in setting_items.items():
            if user_input == item:
                choose = item
                clear_screen()
                return choose
        if user_input == 'q':
            return 'q'
        clear_screen()
        print(show_setting_items(setting))
        print(colors.error+"Enter wrong number")
        print(colors.error+"Try again")


def get_setting(setting):
    while True:
        clear_screen()
        print(show_setting_items(setting))
        choose = which_option_want_to_change()
        if choose == 'q':
            return True
        i = 1
        choose = int(choose)
        for option, value in setting.items():
            if i == choose:
                if option == 'length':
                    length = get_user_password_length(value)
                    set_setting(setting, option, length)
                else:
                    set_setting(setting, option,
                                get_yes_or_no_from_user(option, value))
                    show_setting_items(setting)
                break
            i += 1


def set_setting(setting, option, answer):
    setting[option] = answer


def generate_upper():
    return(random.choice(string.ascii_uppercase))


def generate_lower():
    return(random.choice(string.ascii_lowercase))


def generate_number():
    return(random.choice('0123456789'))


def generate_symbol():
    return(random.choice('!@#$%^&*()_-+=[]{}|\/><:'))


def generate_password_char(choices):
    choice = random.choice(choices)

    if choice == 'upper':
        return generate_upper()
    if choice == 'lower':
        return generate_lower()
    if choice == 'number':
        return generate_number()
    if choice == 'symbol':
        return generate_symbol()
    if choice == 'space':
        return ' '


def generate_password(setting):
    choices = list(filter(lambda x: setting[x], [
                   'upper', 'lower', 'symbol', 'number', 'space']))
    password_length = setting['length']
    finall_password = ''
    for i in range(password_length):
        finall_password += generate_password_char(choices)
    return finall_password


def continue_or_break_password_loop():
    while True:
        continue_or_break = input(
            colors.starter+"Do you want another password (y : yes , n : no  , enter : yes) : ")
        if continue_or_break in ['y', 'n', '']:
            if continue_or_break == 'n':
                return True
            return False
        else:
            print(colors.error+"Please Enter correct option.")
            print(colors.error+"Try again")


def generate_password_loop(setting):
    while True:
        clear_screen()
        print("-"*20)
        print(colors.information +
              f"Generated password: {generate_password(setting)}")
        if continue_or_break_password_loop() == True:
            break


def ask_for_change_setting():
    while True:
        change = input("Do you want to change setting (y : yes , n : no ) ? ")
        if change in ['y', 'n']:
            if change == 'y':
                get_setting(setting)
                print(show_setting_items(setting))
                return True
            return False
        clear_screen()
        print(show_setting_items(setting))
        print(colors.error+'Enter wrong answer')
        print(colors.error+'Try again')


def run():
    clear_screen()
    welcome(setting)
    ask_for_change_setting()
    generate_password_loop(setting)


run()
print(colors.information+"I wish you enjoed this app :)")
print(colors.information+"Bye")