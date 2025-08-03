from twttr import shorten

def main():
    test_uppercase()
    test_lowercase()
    
    
def test_uppercase():
    assert shorten("HELLO WORLD") == "HLL WRLD"
    assert shorten("Today is a GOOD day") == "Tdy s  GD dy"
    
def test_lowercase():
    assert shorten("this is cs50") == "ths s cs50"
    
if __name__ == "__main__":
    main()