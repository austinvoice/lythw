# take input and tests

def super_int_input(prompt):
    try:
        i = int(input(prompt))
        return i
    except ValueError:
        print("Bad input.")
    except KeyboardInterrupt:
        print("Aborted.")
    except:
        print("Unknown error.")
        
    return None
