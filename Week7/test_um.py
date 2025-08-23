from um import count

def main():
    test_um()
    test_multiple_ums()
    test_no_um()
    
def test_um():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album") == 1
    
def test_multiple_ums():
    assert count("Um, thanks, um...") == 2
    
def test_no_um():
    assert count("Hello world") == 0
    
    
if __name__ == "__main__":
    main()