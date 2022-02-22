sturec=[[1,"Arya",96],[2,"Arun",28],[3,"Iniyan",84],[4,"Tamil",61]]
print("|Roll.No|Name      |Marks |")
size=len(sturec)
for i in range(0,size):
    p=5-len(str(sturec[i][0]))
    n=9-len(sturec[i][1])
    print("|",sturec[i][0]," "*p,end="|")
    print(sturec[i][1]," "*n,end="|")
    print(sturec[i][2]," "*3,end="| \n")
