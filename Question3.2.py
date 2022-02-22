sturec=[[1,"Arya",96],[2,"Arun",28],[3,"Iniyan",84],[4,"Tamil",61]]
print("Roll.No|Name      |Marks |")
size=len(sturec)
p=5-len(str(sturec[1][0]))
n=8-len(sturec[1][1])
print("|",sturec[1][0]," "*p,end="|")
print(sturec[1][1]," "*n,end="|")
print(sturec[1][2]," "*3,end="| \n")
