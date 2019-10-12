
list1 = [False,True,True,None,True,None,None,False,False,None,True,False]
list2 = ["or","or","or","==","!=","==","and","==","!=","and","==","or"]
list3 = [False,False,None,None,True,True,False,True,None,False,True,None]


for a in range(12):
    b = (str(list1[a]) + " " + list2[a] + " " + str(list3[a]))
    x = eval(b)
    print(b + " => " +  str(x))
