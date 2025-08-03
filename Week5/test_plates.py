from plates import is_valid

def main():
    test_plates()
    
    
def test_plates():
    assert is_valid("CS50") == True # true is valid
    assert is_valid("CS05") == False # false is invalid
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False
    