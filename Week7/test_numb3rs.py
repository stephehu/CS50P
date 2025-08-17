from numb3rs import validate

def main():
    test_valid_address()
    test_invalid_address
    
def test__address():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    
def test_invalid_address():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("192.168.001.1") == False
    assert validate("cat") == False
    
if __name__ == "__main__":
    main()