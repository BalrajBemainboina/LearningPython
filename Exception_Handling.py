a = 5
b = 2
try:
    print(a/b)
    k = int(input("Enter a Integer"))
    print(k)
    s = 'nm' + 10
except ZeroDivisionError as e:
    print("You cannot divide with zero", e)
except ValueError as e:
    print("Wrong Input", e)
except Exception as e:
    print("Something Went wrong...", e)
finally:
    print("Your Execution finished")
