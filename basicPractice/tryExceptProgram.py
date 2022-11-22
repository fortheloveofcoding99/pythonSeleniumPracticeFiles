
def multiples7():
    l1 = [22,12,13,14,15,16]
    l2 =[]
    try:
        for x in l1:
            l2.append(x/7)
        print(l2)
    except:
        print('Is not divided by 7',x)
    finally:
        print("program quits")


multiples7()

