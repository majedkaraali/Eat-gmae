fl=open("scoredata.txt","r")
sc_list=[]
for i in fl:
   # print(type(i))
   # print(i)
    sc_list.append(i)
max_sc=max(sc_list)
#print(max_sc)