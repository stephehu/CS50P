from bank import value

def main():
    test_hello()
    test_h()
    test_other()
    
def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0
    
def test_h():
    assert value("hi") == 20
    assert value("Hey") == 20

def test_other():
    assert value("what's up") == 100
    assert value("YO") == 100
    
if __name__ == "__main__":
    main()