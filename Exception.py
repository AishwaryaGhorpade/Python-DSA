def func():
    try:
        l=[1,2,3,4]
        idex=int(input("Enter index: "))
        print(l[idex])
        return 1
    except:
        print("Index error")
        return 0
    finally:  #finally always execute even function return the value in try or ecept
        print("Final block execute always")
    # print("execute always")   #doesn't execute this line when try or except block return the value so finally keyword should use

res=func()
print(res)
print("END!!!")

# output
# using print statement output
# 1)Enter index: 2
# 3
# 1
# END!!!

# 2)Enter index: 5
# Index error
# 0
# END!!!

#using finally output
# 1)Enter index: 2
# 3
# Final block execute always
# 1
# END!!!

# 2)Enter index: 5
# Index error
# Final block execute always
# 0
# END!!!