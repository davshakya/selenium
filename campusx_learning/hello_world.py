# -*- coding: utf-8 -*-
"""session-1-tasks.ipynb
Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j7D_owmjwodnY8zedxdpIOQIyB-GufeU

# Task : Session 1
Solve these questions own your own and try to test yourself what you have learned in the session.

Happy Learning!

### Q1 :- Print the given strings as per stated format.

**Given strings**:
```
"Data" "Science" "Mentorship" "Program"
"By" "CampusX"
```
**Output**:
```
Data-Science-Mentorship-Program-started-By-CampusX
```
Concept- [Seperator and End]
"""

# Write your code here
# print("Data", "Science", "Mentorship", "Program", "By", "CampusX", sep="-")

"""### Q2:- Write a program that will convert celsius value to fahrenheit."""

# Write your code here
calsius_value=int(input("Enter temp value on celsius:"))
fahrenheit=calsius_value*9/5_32
print(fahrenheit)

"""### Q3:- Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax."""

# Write your code here
n1=int(input("enter first number"))
n2=int(input("enter second number"))
print(n1,n2)
n1,n2=n2,n1
print(n1,n2)

"""### Q4:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input."""

# Write your code here
import math
i1=int(input("enter first coordinates"))
i2=int(input("enter second coordinates"))
j1=int(input("enter first coordinates"))
j2=int(input("enter second coordinates"))
distance=math.sqrt((i2-i1)**2+(j2-j1)**2)
print(distance)

"""### Q5:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.

"""

# Write your code here
p=int(input("enter principle"))
r=int(input("enter rate"))
t=int(input("enter time"))
interest=p*r*t/100
print(interest)

"""### Q6:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.

For example:
Input:
heads -> 4
legs -> 12
<br>
Output:
dogs -> 2
chicken -> 2
"""

# Write your code here
heads=int(input("enter head count:"))
legs=int(input("enter leg count:"))
total_legs=6
rem=legs%total_legs
if rem==0:
    count=(legs//total_legs)
    print("dogs=",count, "and chicken=",count)
elif rem==4:
    count=(legs//total_legs)
    print("dogs=",count+1,"and chicken=",count)
elif rem==2:
    count=(legs//total_legs)
    print("dogs=",count,"and chicken=",count+1)
else:
    print("Wrong input")

"""### Q7:- Write a program to find the sum of squares of first n natural numbers where n will be provided by the user."""

# Write your code here
n=int(input("Enter range of natural number:"))
sum=n*(n+1)/2
print(f"sum of {n} natural numbe=",sum)

"""### Q8:- Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user."""

# Write your code here
a1=int(input("enter first number:"))
a2=int(input("enter second number:"))
n=int(input("enter term number:"))
d=a2-a1
an=a1+(n-1)*d
print(f"{n}th number is", an)


"""### Q9:- Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user."""

# Write your code here
num1=int(input("enter numerator1"))
den1=int(input("enter denominator1"))
num2=int(input("enter numerator2"))
den2=int(input("enter denominator2"))
frec_result=(num1*den2+num2*den1)/(den1*den2)
print(frec_result)

"""### Q10:- Given the height, width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained? Assume all the inputs are provided by the user.
Input:<br>
Dimensions of the milk tank<br>
H = 20cm, L = 20cm, B = 20cm
<br><br>
Dimensions of the glass<br>
h = 3cm, r = 1cm
"""

# Write your code here
tank_H=int(input("enter tank height:"))
tank_W=int(input("enter tank width:"))
tank_B=int(input("enter tank breadth:"))
glass_H=int(input("enter glass height:"))
glass_R=int(input("enter radius of glass:"))
tank_volume=tank_H*tank_W*tank_B
glass_volume=3.14*glass_R**2*glass_H
print("Total=",tank_volume/glass_volume)
