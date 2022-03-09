import pandas as pd
to=int(input("Enter the total number of elements you want in the series:"))
lst,le = [],0
for i in range(0, to):
	ele = str(input("Enter a word:"))
	lst.append(ele)
le=len(lst)
series=pd.Series(lst)
print("After converting it to uppercase:",end=" ")
for i in series:
    i=i.capitalize()
    print(i ,end=" ")