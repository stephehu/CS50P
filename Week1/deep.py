# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, 
# the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) 
# forty-two or forty two. Otherwise output No.

prompt = input("What is the answer to the Great Question of life, the Universe and Everything? ")
if prompt == "42" or prompt.lower() == "forty_two" or prompt.lower() == "forty two":
    print("Yes")
else:
    print("No")
    
    
