# In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below, wherein is_valid still expects a str as input and returns True if that str meets all requirements and False if it does not, but main is only called if the value of __name__ is "__main__":

# def main():
#     ...


# def is_valid(s):
#     ...


# if __name__ == "__main__":
#     main()
# Then, in a file called test_plates.py, implement four or more functions that collectively test your implementation of is_valid thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

# pytest test_plates.py


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False
    if not s[:2].isalpha():
        return False
    if not s.isalnum():
        return False  
    for i, char in enumerate(s):
        if char.isdigit():
            if char == '0':
                return False  
            if not s[i:].isdigit():
                return False  
            break
    return True

if __name__ == "__main__":
    main()
    
    
