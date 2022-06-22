#User inputs three sides

side1 = float(input("Enter length 1\n"))
side2 = float(input("Enter length 2\n"))
side3 = float(input("Enter length 3\n"))

print("Can the given input lengths form a triangle?")
#Since sides of triangle cannot be negative or zero, use if else to eliminate those values
if side1 > 0 and side2 > 0 and side3 > 0:
    #As the question demands converting values into integer, use 'round' function
    side_1 = int(round(side1))
    side_2 = int(round(side2))
    side_3 = int(round(side3))



    a = side_1 + side_2
    b = side_2 + side_3
    c = side_1 + side_3



    #If any of the three lengths is greater than the sum of the other two, then you cannot form a triangle.
    #Checking for this condition
    check_1 = a > side_3
    check_2 = b > side_1
    check_3 = c > side_2


    #Checking if the three conditions are true or false, and converts it into "Yes and "No"
    #Using 'and' function on all three because all need to be true for a triangle to be formed
    #Using 'str' so that we can convert string to print "Yes" and "No"

    answer = str(check_1 & check_2 & check_3)
    answer = answer.replace("True", "Yes")
    answer = answer.replace("False", "No")

    print(answer)

else:
    print("No\nA triangle cannot have zero or negative length sides.")
