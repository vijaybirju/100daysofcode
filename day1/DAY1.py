#100daysofcode
#day1
#split funtion in python

#Example 1
#Now split funtion can convert  string(myname) into a list of strings.
myname="I am Vijay kumar gangwal or Vijay gangwal or you can call me Vijay uff birju or simply Birju"
list1=myname.split()
print("myname into list1:",list1)
#output : 
'''['I', 'am', 'Vijay', 'kumar', 'gangwal', 'or', 'Vijay', 'gangwal', 'or', 'you', 'can', 'call', 'me', 'Vijay', 'uff', 'birju', 'or', 'simply', 'Birju']'''


#Example 2
#we can pass any symbol(eg. #) or number in split with which we want separate our list 
string2="#100#days#of#code"
list2=string2.split('#')
print("string2 into list2:",list2)
#output : ['', '100', 'days', 'of', 'code']

#Example 3
#split and convert string into integers sepratred by space

str_of_numbers="1 23 4 5 6 6 78 9 0"
list_of_str=str_of_numbers.split()
print(list_of_str)#still it is not string
#output : ['1', '23', '4', '5', '6', '6', '78', '9', '0']

#map every element of str with int which convert them in integer
map_into_int=map(int,list_of_str)
print("map_into_int:",map_into_int)
list_of_int=list(map_into_int)
print(list_of_int) 
#output : [1, 23, 4, 5, 6, 6, 78, 9, 0]
#which is list of integer
