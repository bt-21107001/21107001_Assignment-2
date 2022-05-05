number_1 = int(input("Enter 1st number (a) "))


number_2 = int(input("Enter 2nd number (b) "))


"""Using 'exor' function because it gives output "0" for same input values (0 0 and 1 1) and output 1 for different input values (0 1 and 1 0)
Therefore, in two numbers, when we'll have different values at a bit, we will get 1 and we will need to replace that bit in the original number to make the numbers same
We will count the number of 1s that come in binary after 'exor' operation to check how many bits we need to flip to convert 'a' to 'b' as asked in question
"""

ex_or = number_1 ^ number_2


bin_exor = bin(ex_or)
check_string = str(bin_exor)


bits_need_flip = check_string.count("1")

print("Number of bits needed to be flipped to convert ‘a’ to ‘b’ are:", bits_need_flip)
