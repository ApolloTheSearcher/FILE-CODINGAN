# Expection built-in function
'''
Jadi pada error juga ada kaya urutannya, urutannya sebagai berikut:
BaseException
    +-- Exception
        +-- StopIteration
        +-- StopAsyncIteration
        +-- ArithmeticError
        |    +-- FloatingPointError
        |    +-- OverflowError
        |    +-- ZeroDivisionError
        +-- AssertionError
        +-- AttributeError
        +-- BufferError
        +-- EOFError
        +-- ImportError
        |    +-- ModuleNotFoundError
        +-- LookupError
        |    +-- IndexError
        |    +-- KeyError
        +-- MemoryError
        +-- NameError
        |    +-- UnboundLocalError
        +-- OSError
        |    +-- BlockingIOError
        |    +-- ChildProcessError
        |    +-- ConnectionError
        |    |    +-- BrokenPipeError
        |    |    +-- ConnectionAbortedError
        |    |    +-- ConnectionRefusedError
        |    |    +-- ConnectionResetError
        |    +-- FileExistsError
        |    +-- FileNotFoundError
        |    +-- InterruptedError
        |    +-- IsADirectoryError
        |    +-- NotADirectoryError
        |    +-- PermissionError
        |    +-- ProcessLookupError
        |    +-- TimeoutError
        +-- ReferenceError
        +-- RuntimeError
        |    +-- NotImplementedError
        |    +-- RecursionError
        +-- SyntaxError
        |    +-- IndentationError
        |         +-- TabError
        +-- SystemError
        +-- TypeError
        +-- ValueError
        |    +-- UnicodeError
        |         +-- UnicodeDecodeError
        |         +-- UnicodeEncodeError
        |         +-- UnicodeTranslateError
        
# Raising Exceptions
Jadi kita bisa mengganti pesan jika kita terdapat error loh. menggunakannya dengan if else statement kita taro
raisenya di condisi si else statement kemudian setelah raise kita pesan errornya seperti apa jika pesan itu 
salah, atau raise juga bisa berdiri sendiri tanpa if else statement.
Contoh:
''' 
instrument_catalog = {
    'Marimba': 1999,
    'Kora': 499,
    'Flute': 899
}

def print_instrument_price(instrument):
    # Write your code below:
    if instrument in instrument_catalog:
        print('The price of a ' + instrument + ' is ' + str(instrument_catalog[instrument]))
    else:
        raise KeyError(instrument + " is not found in instrument catalog!") # raising exception

print_instrument_price('Marimba')
print_instrument_price('Flute')
print_instrument_price('Piano') # This should raise a KeyError dan print the message below