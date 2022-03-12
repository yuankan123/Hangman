"""
a = input("please enter your height:")
b = input("please enter your singer:")
c = input("please enter your colour:")

my_dict = {"height": a, "singer": b, "colour": c }
print(my_dict)


my_dict = {"singer" : "songs"}
print(my_dict)


for i in "Camus":
    print(i)


string1 = input("word1:")
string2 = input("word2:")
A = "Yeseterday I wrote a " + string1 +". "
B = "I sent it to " + string2 + "."
C = A + B
print(C)


a = "aldous Huxley was born in 1894."
a = a.capitalize()
print(a)



a = "Where now? Who now? when now?"
reslut = a.split("? ")
print(reslut)


string = ["The", "fox", "jumped", "over", "the", "fence", "."]
string[-2] = string[-2] + string[-1]
string = string[0:-1]
one = " ".join(string)
print(one)

string = "A screaming comes across the sky."
string = string.replace("s", "$")
print(string)


print("Hemingway".index("m"))


string1 = "three" + " "
string1 = string1 *3
string1 = string1[:-1]
print(string1)


string = "It was bright cold day in April,and the clocks were striking thirteen."
string = string.split(",")
string = string[0]
print(string)


string = ["the walking dead", "entourage", "the sopranos", "the vampire diaries"]
for a in string:
    print(a)

for i in range(26, 50):
    print(i)



string = ["the walking dead", "entourage", "the sopranos", "the vampire diaries"]

for i, a in enumerate(string):
    print(i)
    print(a)


string = [1, 2, 3, 4, 5, 6]
while True:
    number = input("please enter an number, q to quit:")
    
    if number == "q":
        break
    number = int(number)
    if number in string:
        print("You are right.")
    else:
        print("You are wrong.")


number1 = [8, 19, 148, 4]
number2 = [9, 1, 33, 83]
number3 = []

for i1 in number1:
    for i2 in number2:
        number3.append(i1 * i2)
for i in number3:
    print(i)



import statistics
nums = [1, 4, 8, 54, 23, 65, 65, 78]
a = statistics.median_high(nums)
print(a)


import cubed
n = cubed.calcu(7)
print(n)


import os
st= open("testbooks.txt", "w")
st.write("hello")
st.close()

import os
with open("testbooks.txt", "r") as f:
    print(f.read())


import os
answer1 = input("please enter your name:")
answer2 = input("please enter your age:")
with open("testbooks.txt", "w") as f:
    f.write(answer1)
    f.write(answer2)



import csv
with open("st.csv", "w") as f:
    r = csv.writer(f, delimiter = ",")
    r.writerow(["one", "two", "three"])
    r.writerow(["four", "five", "six"])


import csv

list1 =[
       ["top gun", "risky business", "minority report"],
       ["titanic", "the revenant", "inception"],
       ["traning day", "man on fire", "flight"]
       ]
print(type(list1))
with open("st.csv", "w") as f:
    r = csv.writer(f, delimiter = ",")
    for text in list1:
        r.writerow(text)
        """
words = ["cat", "dog", "river", "class", "grass", "wake"]
a = len(words)
print(a)
        





    

