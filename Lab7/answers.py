#checking code is working:
print("hello world")
#exercize 1 solution 1
people= [("Jon",15), ("Ned",45), ("Arya",9), ("Catelyn",44),("Bran",10)]
for i in people:
  if i[1] > 18:
    print(i[0])
#exercize 1 shorter solution
for name,age in people:
  if age > 18:
    print(name)

#exersize 2
books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
dic={}
for keys in books:
  value_1 = len(keys)
  value_2 = len(set(keys))
  dic[keys]= (value_1 , value_2)
print(dic)

#exersize 3:
summation = 0
for key in dic.keys():
  value1,value2 = dic[key]
  summation += value1 + value2
  value3= summation/2
  dic[key]= (value1,value2,value3) 
  print(key, "->", dic[key])


#exersize 4
employee_dic = {}
for i in range(5):
  employee_name = input("Insert the employee name:\t")
  employee_salary= int(input("Insert the employee salary:\t"))
  employee_dic[employee_name] = employee_salary

print(employee_dic.values())
  

    
    
    
  

  