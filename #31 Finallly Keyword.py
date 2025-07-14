try:
    print(x)
except ValueError:
    print("value error")
except:
    print("Error for another reason")
finally:
    print("i will handle error with try and excepr") # this finally is always print if error is there or not this line is always print.




try:
    print("Debargha nandi")
except ValueError:
    print("value error")
except:
    print("Error for another reason")
finally:
    print("i will handle error with try and excepr")