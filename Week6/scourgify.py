# Data, too, often needs to be “cleaned,” as by reformatting it, so that values are in a consistent, if not more convenient, format. Consider, for instance, this CSV file of students, before.csv, below:

# name,house
# "Abbott, Hannah",Hufflepuff
# "Bell, Katie",Gryffindor
# "Bones, Susan",Hufflepuff
# "Boot, Terry",Ravenclaw
# "Brown, Lavender",Gryffindor
# "Bulstrode, Millicent",Slytherin
# "Chang, Cho",Ravenclaw
# "Clearwater, Penelope",Ravenclaw
# "Crabbe, Vincent",Slytherin
# "Creevey, Colin",Gryffindor
# "Creevey, Dennis",Gryffindor
# "Diggory, Cedric",Hufflepuff
# "Edgecombe, Marietta",Ravenclaw
# "Finch-Fletchley, Justin",Hufflepuff
# "Finnigan, Seamus",Gryffindor
# "Goldstein, Anthony",Ravenclaw
# "Goyle, Gregory",Slytherin
# "Granger, Hermione",Gryffindor
# "Johnson, Angelina",Gryffindor
# "Jordan, Lee",Gryffindor
# "Longbottom, Neville",Gryffindor
# "Lovegood, Luna",Ravenclaw
# "Lupin, Remus",Gryffindor
# "Malfoy, Draco",Slytherin
# "Malfoy, Scorpius",Slytherin
# "Macmillan, Ernie",Hufflepuff
# "McGonagall, Minerva",Gryffindor
# "Midgen, Eloise",Gryffindor
# "McLaggen, Cormac",Gryffindor
# "Montague, Graham",Slytherin
# "Nott, Theodore",Slytherin
# "Parkinson, Pansy",Slytherin
# "Patil, Padma",Gryffindor
# "Patil, Parvati",Gryffindor
# "Potter, Harry",Gryffindor
# "Riddle, Tom",Slytherin
# "Robins, Demelza",Gryffindor
# "Scamander, Newt",Hufflepuff
# "Slughorn, Horace",Slytherin
# "Smith, Zacharias",Hufflepuff
# "Snape, Severus",Slytherin
# "Spinnet, Alicia",Gryffindor
# "Sprout, Pomona",Hufflepuff
# "Thomas, Dean",Gryffindor
# "Vane, Romilda",Gryffindor
# "Warren, Myrtle",Ravenclaw
# "Weasley, Fred",Gryffindor
# "Weasley, George",Gryffindor
# "Weasley, Ginny",Gryffindor
# "Weasley, Percy",Gryffindor
# "Weasley, Ron",Gryffindor
# "Wood, Oliver",Gryffindor
# "Zabini, Blaise",Slytherin
# Source: en.wikipedia.org/wiki/List_of_Harry_Potter_characters

# Even though each “row” in the file has three values (last name, first name, and house), the first two are combined into one “column” (name), escaped with double quotes, with last name and first name separated by a comma and space. Not ideal if Hogwarts wants to send a form letter to each student, as via mail merge, since it’d be strange to start a letter with:

# Dear Potter, Harry,

# Rather than with, for instance:

# Dear Harry,

# In a file called scourgify.py, implement a program that:

# Expects the user to provide two command-line arguments:
# the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
# the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
# Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.
# If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.

import sys
import os
import csv

def main():
    if len(sys.argv) != 3:
        sys.exit("Expected two command-line arguments")
    if not os.path.isfile(sys.argv[1]):
        sys.exit("File does not exist")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a csv file")
    students = []
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            first, last = row["name"].split(",")
            students.append({"first name": first.strip(), "last name": last.strip(), "house": row["house"].strip()})
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames = ["first name", "last name", "house"])
        writer.writeheader()
        writer.writerows(students)

if __name__ == "__main__":
    main()