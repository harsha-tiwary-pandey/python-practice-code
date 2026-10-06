from os.path import split


def reverse_string(string):
    size = len(string)
    print(string[-1:-(size+1):-1])

def palindrome(string):
    size = len(string) + 1
    if string[0:size:1] == string[-1:-size:-1]:
        print(string, " is a palindrome")
    else:
        print(string, " is not a palindrome")

def count_characters(string):
    size = 0
    for ch in string:
        size += 1
    print("No. of characters in string ",string," is: ",size)

def first_non_repeat_char(string):
    for ch in string:
        if string.index(ch) == string.rindex(ch):
            print(ch, " is the first non-repeating character in string: ", string)
            break

def remove_duplicate(string):
    reslt =[]
    for ch in string:
        if string.index(ch) == string.rindex(ch):
            reslt.append(ch)
        continue
    print("".join(reslt))

def frequency_count(string):
    dict_obj = {}
    for ch in string:
        dict_obj[ch] = dict_obj.get(ch, 0) + 1
    print(dict_obj)

def anagram(string1, string2):
    set1 = set()
    set2 = set()

    for ch in string1:
        set1.add(ch)
    for ch in string2:
        set2.add(ch)
    if set1 == set2:
        print(string1, " and ", string2,  "are anagram")
    else:
        print(string1, " and " ,string2, " are not anagram")

def count_vowels(string):
    count = 0
    for ch in string:
        if ch == 'a' or ch == 'e' or ch=='i' or ch=='o' or ch== 'u':
            count +=1
    print("vowels in string: ", string , " = ", count)

def vowels_consonants(string):
    vowels_list = []
    consonants_list = []
    for ch in string:
        if ch=='a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            vowels_list.append(ch)
        else:
            consonants_list.append(ch)
    print("vowels list: ", vowels_list)
    print("consonants list: ", consonants_list)

def remove_spaces(string):
    list_ele = string.split(" ")
    print(list_ele)

    # reverse each word logic
    list_final_ele = []
    for word in list_ele:
        list_final_ele.append(word[-1:-(len(word)+1):-1])
    print(list_final_ele)

    #longest word logic
    longest_word = ""
    for word in list_ele:
        if len(word) >= len(longest_word):
            longest_word = word
    print("longest word in string : ", string, " is: ", longest_word)

    #count word logic
    count = 0
    for word in list_ele:
        if word.isalpha():
            count += 1
    print("No. of words in string: ", string, " is = ",count)

    #only digits
    string1 = "name1 : is 123 and roll1 is * 21333432 6"
    list_eles = string1.split(" ")
    final_list_eles = []
    for word in list_eles:
        if word.isdigit():
            final_list_eles.append(word)
    print("digits in string : ", string1, " is: ", " ".join(final_list_eles))