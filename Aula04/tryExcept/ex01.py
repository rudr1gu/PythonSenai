try:
    print(10/2)
    print(2>3)
    print(int('a'))
except ZeroDivisionError:
    print("ZeroDivisionError:")
except TypeError:
    print("TypeError")
except ValueError:
    print('ValueError')
except:
    print('outro erro')
