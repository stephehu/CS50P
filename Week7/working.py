# Whereas most countries use a 24-hour clock, the United States tends to use a 12-hour clock. Accordingly, instead of “09:00 to 17:00”, many Americans would say they work “9:00 AM to 5:00 PM” (or “9 AM to 5 PM”), wherein “AM” is an abbreviation for “ante meridiem” and “PM” is an abbreviation for “post meridiem”, wherein “meridiem” means midday (i.e., noon).

# Conversion Table
# In a file called working.py, implement a function called convert that expects a str in any of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
# 9:00 AM to 5 PM
# 9 AM to 5:00 PM
# Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

# Structure working.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

# import re
# import sys


# def main():
#     print(convert(input("Hours: ")))


# def convert(s):
#     ...


# ...


# if __name__ == "__main__":
#     main()
# Either before or after you implement convert in working.py, additionally implement, in a file called test_working.py, three or more functions that collectively test your implementation of convert thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

# pytest test_working.py


import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$", s)
    if not matches:
        raise ValueError("Invalid format")
    h1 = matches.group(1)
    m1 = matches.group(2)
    t1 = matches.group(3)
    h2 = matches.group(4)
    m2 = matches.group(5)
    t2 = matches.group(6)
    
    if m1 is None:
        m1 = "00"
    if m2 is None:
        m2 = "00"
    h1 = int(h1)
    m1 = int(m1)
    h2 = int(h2)
    m2 = int(m2)
    if not (1 <= h1 <= 12 and 0 <= m1 < 60 and 1 <= h2 <= 12 and 0 <= m2 < 60):
        raise ValueError("Invalid time value")
    
    if t1 == "AM":
        if h1 == 12:
            h1 = 0
    else:  
        if h1 != 12:
            h1 += 12
    t1_24 = f"{h1:02}:{m1:02}"

    if t2 == "AM":
        if h2 == 12:
            h2 = 0
    else: 
        if h2 != 12:
            h2 += 12
    t2_24 = f"{h2:02}:{m2:02}"

    return f"{t1_24} to {t2_24}"
            
    
if __name__ == "__main__":
    main()