def print_my_name():
  print("Hello, my name is Topias")

def return_my_name():
  return "Topias"

def repeat_a_word(word, repetition):
    if type(word) is not str or type(repetition) is not int:
        raise Exception("please give string and int")

    return word * repetition

def largest_of_three(a, b, c):
    if type(a) and type(b) and type(c) is not int:
        raise Exception("please give int")
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest

print_my_name()
print(return_my_name())
print(repeat_a_word("hello", 2))
print(largest_of_three(1,2,3))
#print(largest_of_three(1,2,"apina"))