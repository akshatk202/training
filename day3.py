##\dictionary\##

# dt={
#     "name":"akshat",
#     "branch":"cse",
#     "year":2,
#     "year":3
# }
# print(dt)
# print(type(dt))
# print(len(dt))                      #normal dictionary

# dt={
#     "name":"akshat",
#     "branch":"cse",
#     "year":2,
#     "year":3,
#     "class":["aksaht","alpika","amit"],
#     "year":("1","2","3"),
#     "set":{True,"hello",1}
# }
# print(dt)
# print(type(dt))                     #taking set in that

# thisdt=dict(name="akshat", section="4",year="2")    
# print(thisdt)
# print(type(thisdt))                  #dictionary constructor

# dt={
#     "name":"akshat",
#     "age":"19",
#     "DOB":"2004"
# }
# print(dt["age"])                    #print an specific key values
# print(type(dt))                     
# print(dt.get("DOB"))                #also for print an specific key values
# print(dt.keys())                    #only for print an key name
# print(dt.values())                  #print only values of the keys

# dt={
#     "name":"akshat",
#     "age":"19",
#     "DOB":"2004"
# }
# print(dt.items())                   #print all the items of the dictionary
# x=dt.update({"age":20})
# print(dt)                           #update the value in dictionary

# print(dt.pop("age"))
# print(dt)                           #remove key and value of the key

# dt={'dt1':{"name":"ram"},
#     'dt2':{"name":"akshat"}}
# print(dt)                           #print whole dictionary
# print(dt['dt1'])                    #print dictionary under dictionary
# print(dt['dt1']["name"])            #print value of a dictionary



##\IF ELSE STATEMENT\##

# a=200
# b=30
# if a>b:
#     print("a is greater than b")
# elif a==b:
#     print("a is equal to b")
# else:
#     print("b is greater than a")

# a=10
# b=30
# if a<b: print("a is smaller than b")            #short hand if

# a=2
# b=320
# print("a") if a>b else print("b")                 #short end if else

# a=300
# b=300
# # print("a") if a>b else print("equal") if a==b else print("b")               #multiple condition in same line

# # OR #

# if a>b:
#     print("a")
# else:
#     if a==b:
#         print("equal")
#     else:
#         print("b")



##\CONDITIONAL STATEMENT\##

# a=200
# b=33
# c=500
# # if a>b and c>a:
# #     print("both condition are true")

# # if a>b or c>a:
# #     print("both condition are true")

# if not b<a:
#     print("condition is true")
# else:
#     print("false")

# x=41
# if x>10:
#     print("above ten"),
#     if x>20:
#         print("above 20"),
#     else:
#         print("but not above 20")                 #nested if condition

# x=41
# if x>10:
#     print("above ten"),
#     if x>20:
#         pass                                #pass statement in nested if condition
#     else:
#         print("but not above 20")

# x=input("enter alphabet:")
# y=input("enter alphabet:")
# if x!=y:
#     print("cond is true")
# else:
#     print("cond is not true")               #not equal to condition

# x=int(input("enter number:"))
# y=int(input("enter number:"))
# if x==y:
#     print("cond is true")
# else:
#     print("cond is not true")               #equal equal to condition


## Identify and print vovel and consonent in alphabets
## Answer
# x=input("enter vovel:")
# if x==('a'or 'e'or 'i'or 'o'or 'u'or 'A' or 'E' or 'I' or 'O' or 'U'):
#     print("vovels")
# else:
#     print("other")


##\LOOP STATEMENT\##

# for x in 'mango':
#     print(x)

# fruits=["apple", "mango", "orange"]
# for x in fruits:
#     print(x)

# fruits=["apple", "mango", "orange"]
# for x in fruits:
#     print(x)                          #break statement in loops
#     if x=="mango":
#         break

# fruits=["apple", "mango", "orange", "watermelon"]
# for x in fruits:                    #continue statement in loops
#     print(x)
#     if x=="mango": 
#         continue

# for x in range(6):
#     print (x)                           #loop in range which don't have any starting point

# for x in range (2,10):
#     print(x)                              #loop in range which have starting point

# for x in range (6):
#     print(x)
# else:
#     print("finished")                       #working of loop

# for x in range(6):
#     if x==3: break
#     print(x)
# else:
#     print("finished")

# for x in range(6):
#     if x==3: continue
#     print(x)
# else:
#     print("finished")

# dt={
#     "name":"akshat",
#     "age":"19",
#     "DOB":"2004"
# }
# for x in dt:
#     print(dt[x])                                  #loop in dictionary
    
# for x in dt.keys():
#     print(x)                                      #for printing keys

# for x in dt.values():
#     print(x)                                      #for printing values

# for x,y in dt.items():
#     print(x,y)                                    #forn printing both key and value


##\TABLE PROGRAM\##

# y=int(input("enter a value:"))
# for i in range(1,11):                             #for printing a table
#     print(f"{y} * {i} * {y*i}")           

# fruits=["apple", "mango", "orange"]
# for index, fruits in enumerate(fruits):
#     print(index,fruits)                             #for printing an index and values    

    

