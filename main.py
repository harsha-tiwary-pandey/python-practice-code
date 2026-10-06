# This is a sample Python script.
from SalaryCalculator import calculate_salary, total_salary
from code_practice import (reverse_string, palindrome, count_characters, first_non_repeat_char,
                           remove_duplicate, frequency_count, anagram, count_vowels, vowels_consonants, remove_spaces)

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    salary = calculate_salary(10000)
    print(salary)

    total_salary = total_salary(salary, 14000, 20000)
    print(total_salary)

    reverse_string("input data")
    palindrome("madam")
    palindrome("hello")
    count_characters("input data")
    first_non_repeat_char("holoh ele i")
    remove_duplicate("hello data")
    frequency_count("input data")
    anagram("rasp", "srp")
    count_vowels("input data")
    vowels_consonants("input data")
    remove_spaces("input : data is entered")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
    '''  a = [10, 20] # list

    b = [10, 20] # list

    print(id(a))
    print(id(b))

    print(a == b)
    print(a is b)

    a = 10
    b = 20

    print(a is b) '''





