# import os
# os.remove("demo.txt")


# # val1 = int(input("enter num1:"))
# # val2 = int(input("enter num2:"))
# # sum = val1+ val2
# # print(sum)


# # side = float(input("enter side of square: "))
# # print("area = " , side *side)

# # value1 = float(input("enter first float value:"))
# # value2 = float(input("enter second float value:"))
# # avg = (value1 + value2)/2
# # print("avg = ", avg)


# # val1 = int(input("enter first value"))
# # val2 = int(input("enter second value"))
# # print(val1>=val2)


# # str1 = "UJJWAL"
# # print(str1[2:len(str1)])


# # str1 = "uJJWAL sharma"
# # str1 = str1.capitalize()  
# # print(str1.capitalize())
# # print(str1.replace("sharma","kumar"))
# # print(str1.find("m"))
# # print(str1.count("a"))

# # name = input("enter your name: ")
# # print(len(name))

# # age = 16
# # f(age>=18):
# #    print("can vote and apply for license")
# # else:
# #    print("not eligible")


# # light = input("enter traffic light signal:")
# # if(light== "red"):
# #   print("stop")
# # elif(light=="green"):
# #   print("you can go")
# # lse:
# #   print("ready to drive")

# # marks = int(input("enter student marks: "))
# # if (marks >=90):
# #     grade = "A"
# # elif(marks < 90 and marks>= 80 ):
# #     grade = "B"
# # elif(marks<80 and marks >= 70):
# #     grade = "C"
# # else:
# #     grade = "D"

# # print ("grade of student", grade)

# # num = int(input("enter your number:"))
# # if(num%2 == 0):
# #     num = "even"
# # else:
# #     num = "odd"

# # print("your number is :", num)

# # num1 = int(input("enter first number:"))
# # num2 = int(input("enter second number:"))
# # num3 = int(input("enter third number:"))

# # if(num1>num2):
# #    if(num1>num3):
# #         print("first number is greater:", num1)
# # elif(num3>num2):
# #     print("third number is greater: ", num3)
# # else:
# #     print("second number is greater", num2)

# # num = int(input("enter your number:"))
# # if(num%7 == 0):
# #     num = "divide by 7"
# # else:
# #     num = "not divided by 7"
# # print(num)

# # num1 = int(input("enter first number:"))
# # num2 = int(input("enter second number:"))
# # num3 = int(input("enter third number:"))
# # if(num1>num2 and num1>num3):
# #     print("first number is greater:", num1 )
# # elif(num2>num3):
# #     print("second number is greater:", num2)
# # else:
# #     print("third number is greater:",  num3)

# # list = [2,1,3]
# # list.append(6)
# # # list.sort(reverse = True)
# # # list.reverse()
# # list.insert(2,9)
# # list.pop(2)
# # print(list)

# # first_movie = input("enter first fav movie:")
# # second_movie = input("enter second fav movie:")
# # third_movie = input("enter third fav movie:")

# # list = [first_movie,second_movie,third_movie]
# # print(list)

# # num = [4,2,3,2,4]
# # num_copy = num.copy()
# # num_copy.reverse()

# # if(num_copy == num):
# #     print("list is palindrome")
# # else:
# #     print("list is not palindrome")

# # grade = ["C" ,"D" ,"A" , "A","B", "B" ,"A" ]
# # grade.sort()
# # print(grade)

# # info = {
# #     "name" : "Ujjwal",
# #     "subjects" : ["hindi", "python", "english"],
# #     "topics" : ("dict", "set"),
# #     "age" : 24,
# #     "is_adult" : True,
# #     "marks" : 96
# # }


# # info["name"] = "new"
# # info["surname"] = "kumar"
# # print(info["name"])
# # print(info["marks"])
# # print(info["surname"])

# # collection = set()
# # collection.add(1)
# # collection.add(4)
# # collection.add((3,6,89,4,4,4))
# # collection.add(8)
# # collection.add("java")
# # collection.remove(8)
# # collection.remove(4)
# # print(collection)
# # print(collection.pop())


# # num = int(input("enter your number:"))
# # if(num%2== 0 ):
# #     num = num*num
# # else:
# #     num = num * num * num
# # print(num)

# # str = "abcabc"
# # dict = {ch: str.count(ch) for ch in set(str)}
# # print(dict)

# # set1 = {1,2,3}
# # set2 = {3,4,5}
# # print(set1.union(set2))
# # print(set1.intersection(set2))


# # item = {
# #     "table" : {
# #         "a piece of furniture",
# #         "lists of facts and figures"
# #         },
# #     "cat":     "a small animal"
    
# # }

# # print(item)


# # list = ["python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"]
# # list1 = set(list.copy())
# # print(list)
# # print(len(list1))


# # subjects = {}
# # english_marks = int(input("enter english marks:"))
# # physics_marks = int(input("enter physics marks:"))
# # chem_marks = int(input("enter chem marks:"))
# # subjects.update({"english_marks" : english_marks })
# # subjects.update({"physics_marks" : physics_marks})
# # subjects.update({"chem_marks" : chem_marks})
# # print(subjects)


# # subjects = {}
# # english_marks = int(input("enter english marks:"))
# # subjects.update({"english" : english_marks})
# # physics_marks = int(input("enter physics marks:"))
# # subjects.update({"physics" : physics_marks})
# # chem_marks = int(input("enter chem marks:"))
# # subjects.update({"chemistry" : chem_marks})
# # print(subjects)


# # values = {
# #     ("float", 9.0),
# #     ("int", 9)
# # }
# # print(values)



# # i = 1 
# # while i<= 999:
# #     print("UJJWAL", i)
# #     i += 1

# # i=100
# # while i>=1:
# #     print(i)
# #     i-=1

# # i=1
# # while i<=100:
# #     print(i)
# #     i +=1

# # num = int(input("enter your number:"))
# # i=1
# # while i<=10:
# #     print(num*i)
# #     i+=1

# # i=1
# # list= []
# # while i<=10:
# #     list.append(i * i)
# #     i+=1
# # print(list)
# # i= 0
# # while i <len(list):
# #     print(list[i])
# #     i+=1

# # i=1
# # list= []
# # while i<=10:
# #     list.append(i * i)
# #     i+=1
# # num = int(input("enter number for search:"))
# # i=0
# # while i<len(list):
# #     if(list[i]== num ):
# #         print("Found at index: ", i)
# #         break
# #     else:
# #         print("Finding...")
# #     i+=1


# # i=0
# # while i<=50:
# #     if(i%2!=0):
# #         i+=1
# #         continue
# #     print(i)
# #     i+=1

# # i=1
# # list= []
# # while i<=10:
# #     list.append(i * i)
# #     i+=1
# # for item in list: print(item)           #one line code to get data of list
# # i=0                                     #loop traversing to get data of list
# # while i< len(list):
# #     print(list[i])
# #     i+=1

# # num = int(input("enter your number:"))
# # for i in range(1, 11):
# #     print(num*i)


# # num = int(input("enter number:"))
# # sum = 0
# # # for i in range(1 , num+1):
# # #     sum += i
# # # print(sum)

# # i= 0 
# # while i<= num:
# #     sum += i
# #     i+=1 
# # print(sum)

# # num = int(input("enter your number:"))
# # fac = 1
# # # for i in range(1,num+1):
# # #     fac = fac*i
# # # print(fac)
# # i = 1
# # while i<= num:
# #     fac = fac * i
# #     i+=1
# # print(fac)



# # def cal_sum(a,b):
# #     return a+b
   

# # print(cal_sum(3,6))
# # print(cal_sum(24,94))
# # print(cal_sum(23,94))

# # def avg(a,b,c):
# #     return (a+b+c)/3



# # a=int(input("enter first number:"))
# # b=int(input("enter second number:"))
# # c=int(input("enter third number"))
# # print(avg(a,b,c))


# def calc_mul(a,b):
#     return a*b

# try:
#     a=input("enter first number:")
#     b=input("enter second number:")

#     a = int(a) if a.strip() != "" else 1
#     b = int(b) if b.strip() != ""else 1
#     print("Multiplication ->" , calc_mul(a,b))

# except ValueError:
#     print("⚠️ Please enter valid numbers only!")

# def print_len(list):
#    return print(len(list))
# def items(list):
#    for item in list:
#       print(item, end=" ")

# a = ("sda", "wqd" ,  "qwr")
# items(a)
# print()


# n= 4
# fac= 1
# for i in range(1, n+1):
#     fac = fac*i 
# print(fac)

# def cal_fac(n):
#     fac = 1
#     for i in range(1,n+1):
#         fac *= i
#     return fac

# n=int(input("enter your number:"))
# print(cal_fac(n))

# def convert(usd):
#     inr = 88.375*usd
#     print(usd , "USD = ", inr, "INR")

# n = int(input("enter usd:"))
# convert(n)

# def check(num):
#     if(num%2==0):
#         print("Number is Even")
#     else:
#         print("Numberis Odd")

# n = int(input("enter number to check if it is odd or even:"))
# check(n)


# def show(n):
#     if n==0:
#         return
#     print(n)
#     show(n-1)

# n = int(input("enter number :"))
# show(n)

# def fact(n):
#     if(n==0 or n==1):
#         return 1 
#     else:
#         return n*  fact(n-1)    
# print((fact(6)))

# def sum_of_natural_num(n):
#     if(n==0):
#         return 0
#     else:
#         return sum_of_natural_num(n-1) + n
    
# n= int(input("enter your no.: "))
# print(sum_of_natural_num(n))


# def elements(list, i=0):
#     if(i == len(list)):
#         return 
#     print(list[i], end=" ")
#     (elements(list ,i+1))

# student = ("ujjwal", "harshit", "arya", "aryan", "anurag")
# elements(student)
# print()


# file = open("practice.txt", "rt")
# line1 = file.readline()
# print(line1,end ="")
# line2 = file.readline()
# print(line2)
# file.close()

# file = open("demo.txt", "a")
# data = file.write("\nthis new line")
# file.close()

# with open("demo.txt", "r")as new_file:
#     data = new_file.read()
#     print(data)

# with open("demo.txt", "w") as new_file:
#     data = new_file.write("new")


# with open("practice.txt", "w") as file:
#     file.write("Hy everyone\nWe are learning File I/O\nusing Java\nI like progrmming in Java.")

# with open("practice.txt", "r+") as file:
#     data = file.read()
# new_data = data.replace("Java", "Python")
# print(new_data)
# import os
# os.remove("practice.txt")


# def check_for_word(word):
#     with open("practice.txt", "r") as f:
#         data = f.readline()  
#         if(word in data):
#             print("found")
#         else:
#             print("Not Found")

# word = input("enter word:")
# check_for_word(word)




# def check_for_line(word):
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#         if(word in data):
#             print(line_no)
#             return
#         line_no += 1        
#     return -1

# word = input("enter word:")
# check_for_line(word)

# def check_for_line(word):
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(f"Found at line {line_no}")
#                 return
#             line_no += 1
#     return -1

# word = input("Enter word: ")
# check_for_line(word)

count = 0
with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

    num = data.split(",")
    print(num)
    for value in num:
        if(int(value) % 2 == 0):
            count += 1 
print(count)