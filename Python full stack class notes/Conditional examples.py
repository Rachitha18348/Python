name = input()
marks = int(input())
age = int(input())

if 0 < marks < 100:
    if marks >= 90:
        if age >= 18:
            print("%s scored %d marks and got Scholarship" % (name, marks))
        else:
            print("%s scored %d marks and is Outstanding" % (name, marks))
    elif marks >= 80:
        print("%s scored %d marks and is Excellent" % (name, marks))
    elif marks >= 60:
        print("%s scored %d marks and is Very Good" % (name, marks))
    elif marks >= 50:
        print("%s scored %d marks and is Good" % (name, marks))
    else:
        print("%s scored %d marks and Failed" % (name, marks))
else:
    print("%d is an Invalid Marks value" % marks)



college = input("Is he in the college? (yes/no): ")

if college == "yes":
    block = input("Is he in the block? (yes/no): ")

    if block == "yes":
        floor = input("Is he on the floor? (yes/no): ")

        if floor == "yes":
            classroom = input("Is he in the classroom? (yes/no): ")

            if classroom == "yes":
             
                    print("Found him!")
                
            else:
                    print("Not in the classroom")
        else:
            print("Not on the floor")
    else:
        print("Not in the block")
else:
    print("Not in the college")
