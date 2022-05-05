given_input = "Python is a case sensitive language"
print(given_input)


#PART a
#Use len() function to find length of string
str_length = len(given_input)

print("Length of the string is:", str_length)


#PART b
str_reverse = given_input[::-1]
print("The reversed string is:",str_reverse)


#PART c
#Using slice to store a part of string in a variable
str_slice = given_input[10:26]


#PART d
#repalcing the stored sliced string 
replaced_str = given_input.replace(str_slice, "object oriented")

print(replaced_str)


#PART e (Index of "a")
index_a = given_input.find("a")
print('Index of "a" substring in input string is:',index_a)


#PART f
#To remove white spaces, replacing spaces with empty quotes
g = given_input.replace(" ", "")

print(g)
