print('This program checks if string input by user has the word "name" in it.')
print('You get "Yes" and "No" accordingly.')


#User inputs a string
inp_user = input("Please input the string ")



#Using 'in' operator to find "name" in user input string
true_or_false = "name" in inp_user



#Using 'if else' to produce "Yes" and "No"
if true_or_false == True:
    print("Yes")

else:
    print("No")    