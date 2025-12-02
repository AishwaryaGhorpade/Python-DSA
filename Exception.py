def func():
    try:
        l=[1,2,3,4]
        idex=int(input("Enter index: "))
        print(l[idex])
        return 1
    except:
        print("Index error")
        return 0
    finally:
        print("execute always")
    #print("execute always")   #doesn't work when except block execute so finally keyword should use
    # even try block return the value also finally block execute

res=func()
print(res)
print("END!!!")