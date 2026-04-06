def disp() :
    print("Inside Display()",id(disp))
def fun() :
    print("Inside fun()",id(fun))
def msg() :
    print("Inside msg()",id(msg))

l = [disp,fun,msg]
for x in l:
    x()
    print(id(x))
