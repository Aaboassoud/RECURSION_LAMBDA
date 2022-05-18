## 1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:
vowels = ("aeiou")
def count_vowels(words:str):
    #### Note: the function should be able to count how many vowels no matter if it is lowercase or uppercase . 
    words = words.lower()
    if not words:
        return 0
    elif words[0] in vowels:
        return 1 + count_vowels(words[1:])
    else:
        return 0 + count_vowels(words[1:])
print("number of vowels in phrase or word = ", count_vowels("I LOVE PYTHON"))

# 2) Given a list of numbers : [40,35, 10, 15, 20]
list_of_numbers = [40,35, 10, 15, 20]

#### create a new list containing each number from the previous list mutliplied by itself.
new_list=list(map(lambda number:number*number,list_of_numbers))

#### print the new list.
print(new_list)