import pandas as pd

    
# # data=pd.read_csv("D:/Dev_Progs/selenium/book1.csv")
# # print(data)

data1=pd.read_excel("D:\Dev_Progs\selenium\sample.xlsx")
# print(data1)
x=data1.to_dict(orient="records")
# x=data1.iloc[3,2]
print(x)
# for i in range(5)




#Reading two Excel Sheets
# sheet1 = pd.read_excel(r'Book1.xlsx')
# sheet2 = pd.read_excel(r'Book2.xlsx')
# Iterating the Columns Names of both Sheets
# for i,j in zip(sheet1,sheet2):
# 	# Creating empty lists to append the columns values	
# 	a,b =[],[]

# 	# Iterating the columns values
# 	for m, n in zip(sheet1[i],sheet2[j]):
# 		a.append(m)
# 		b.append(n)

# 	# Sorting the lists
# 	a.sort()
# 	b.sort()
# 	# Iterating the list's values and comparing them
# 	for m, n in zip(range(len(a)), range(len(b))):
#      		print(m)
	 		# if a[m] != b[n]:
			# print('Column name : \'{}\' and Row Number : {}'.format(i,m))
# print(a)
# print(b)




# sheet1 = pd.read_excel('Book1.xlsx')
# sheet2 = pd.read_excel('Book2.xlsx')
# print(sheet1)
# for i,j in zip(sheet1,sheet2):
#  a,b=[],[]
 
#  for x,y in zip(sheet1[i],sheet2[j]):
#   a.append(x)
#   b.append(y)
#   a.sort()
#   b.sort()
#   for m,n in zip(range(len(a)),range(len(b))):
#    if a[m]==b[n]:
#     #   print(f"equal {a[m]},{b[n]}")
#     pass
#    else:
#       print(f"not equal {a[m]},{b[n]}")

# print(a)
# print(len(b))	
	