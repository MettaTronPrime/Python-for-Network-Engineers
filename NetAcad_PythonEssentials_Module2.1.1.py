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
#duplicate the arrow, placing both arrows side by side; note: a string may be multiplied by using the following trick: "string" * 2 will produce "stringstring" 
# (we'll tell you more about it soon)
#remove any of the quotes, and look carefully at Python's response; pay attention to where Python sees an error - is this the place where the error really exists?
#do the same with some of the parentheses;
#change any of the print words into something else, differing only in case (e.g., Print) - what happens now?
#replace some of the quotes with apostrophes; watch what happens carefully.
#print("    *\n","  * *\n"," *   *\n","*     *")
#print("***   ***")
#print("  *   *\n"," *   *\n"," *****") 
print('       *\n',"     *  *\n","   *      *\n"," *          *\n","*             *")
print("*               *")
print("******      ******")
print("      *     *\n","     *     *\n","     *     *\n","     *     *\n","     *******") 


#Apostrophes are good if you want to:

#Print('Something simple') 
#But what if you're trying to print something like:

#Print('This Isn't as simple') 
#You would get an error. Python thinks your string starts with the first apostrophe and ends with the second.

#In this case you would use quotation marks.

#Print("This isn't as simple")
#Now python realizes your string starts at the first quotation mark and ends at the last quotation mark. It interprets the apostrophe simply as a string.

#What if the string you're printing has quotation marks though?

#Print("He said "this has quotation marks".") 
#You'd get an error again, to fix this you'd have to use triple apostrophes.

#Print('''He said "This has quotation marks".''') 

#Singles would work fine also

#'He said "This has quotation marks".'
#Triples would be required for something like

#'''He said "John's dog is dead".'''

#They make no technical difference, as long as you use the same character at the beginning and end of your strings.
#  In other words, this works:

#"Hello, world!"
#'Something.'

#But this does NOT:

#"Hello, world!'
#'Something."

#As for convention, apostrophes (') are usually used for individual characters or strings not shown to the end-user, and double-quotes (") are used for any text seen by the user.

#You can use, within a string, a different type of quote to the outer pair literally:

#"He said, 'this is interesting', to the crowd"
#You can also escape a quote to use it literally using the backslash character:

#'That\'s interesting'


#In Python, single-quoted strings and double-quoted strings are the same. This PEP does not make a recommendation for this.
#Pick a rule and stick to it. When a string contains single or double quote characters, however, use the other one to avoid backslashes in the string. It improves readability.

#https://www.python.org/dev/peps/pep-0008/#string-quotes

#Key Differences Between Single and Double Quotes in Python

#Single Quotation Mark	                                                Double Quotation Mark
#Represented as ‘ ‘	                                                    Represented as ” “
#Single quotes for anything that behaves like an Identifier.	        Double quotes generally we used for text.
#Single quotes are used for regular expressions, dict keys or SQL.	    Double quotes are used for string representation.
#Eg. ‘We “welcome” you.’	                                            Eg. “Hello it’s me.”

#What if you have to use strings that may include both single and double quotes? 
# For this, Python allows you to use triple quotes. A simple example for the same is shown below.
#  Triple quotes also allow you to add multi-line strings to Python variables instead of being limited to single lines.

#Example of triple quotes
#sentence1 = '''He asked, "did you speak with him?"'''
#print(sentence1)
#sentence2 = '''"That's great", she said.'''
#print(sentence2)
#Output:

#He asked, "did you speak with him?"
##"That's great", she said.