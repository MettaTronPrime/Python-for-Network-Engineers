#!/usr/bin/env python

#print ("The itsy bitsy spider\nclimbed up the waterspout")
#print ()
#print ("Down came the rain\nand washed the spider out")

#Code for ABC in hexadecimal
#print ("\x41\x42\x43")

#code for ABC in octal
#print ("\101\102\103")

#observe the output from the following
#print ("\1\2\3")
#print ("10\20\30")
#print("\10\20\30\40\50")
#print("The itsy bitsy spider" , "climbed up" , "the waterspout.")
#print ("\n\1\2\3\4\5","\101\102\103\104\105")
print()
#print("My name is","Python.")
#print("Monty Python.")
print()
print("My name is","Python.", end=" ")
print("Monty Python.")
print ("\n\1\2\3\4\5","\101\102\103\104\105")
#The end statement for printing in Python allows the programmer to define a custom ending character for each print call other than the default \n

#For instance, if you have a function that is to print all values within a list on the same line, you do:

#def value(l):
#   for items in l:
#       print(l, end=' ')
#So if the list argued to this function contains the values [1, 2, 3, 4], it will print them in this manner: 1 2 3 4. 
# If this new ending character parameter was not defined they would be printed:
#1
#2
#3
#4
#The same principle applies for ANY value you provide for the end option

#The separator between the arguments to print() function in Python is space by default (softspace feature) , which can be modified and can be made to any character, integer or string as per our choice.
#  The ‘sep’ parameter is used to achieve the same, it is found only in python 3.x or later. It is also used for formatting the output strings.

#code for disabling the softspace feature
#print('A','L','D', sep='')
print('D','E','V', sep='', end='')
print('N','E','T', '\n\2\2\2', sep='')

#for formatting a date
print('05','21','2022', sep='/')

#another example
print('ryannewton301','gmail.com', sep='@')

#observe the output from the following
#print('\a\b\A\B')

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

print("Programming","Essentials","in", sep='***', end='...')
print("Python")
print()
print()
print()
print()
#print("    *")
#print("   * *")
#print("  *   *")
#print(" *     *")
#print("***   ***")
#print("  *   *")
#print("  *   *")
#print("  *****")
#minimize the number of print() function invocations by inserting the \n sequence into the strings
#make the arrow twice as large (but keep the proportions)
#duplicate the arrow, placing both arrows side by side; note: a string may be multiplied by using the following trick: "string" * 2 will produce "stringstring" (we'll tell you more about it soon)
#remove any of the quotes, and look carefully at Python's response; pay attention to where Python sees an error - is this the place where the error really exists?
#do the same with some of the parentheses;
#change any of the print words into something else, differing only in case (e.g., Print) - what happens now?
#replace some of the quotes with apostrophes; watch what happens carefully.
print("    *\n","  * *\n"," *   *\n","*     *")
print("***   ***")
print("  *   *\n"," *   *\n"," *****") 
print("       *\n","     *  *\n","   *      *\n"," *          *\n","*            *")
print("*               *")
print("******      ******")
print("      *     *\n","     *     *\n","     *******") 