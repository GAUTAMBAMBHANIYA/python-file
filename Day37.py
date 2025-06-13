# finally
# if there are Exception or not but finally block always run

def fun1():
    try:
        a=5
        b=0
        print(a/b)
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("i am always run ")
fun1()