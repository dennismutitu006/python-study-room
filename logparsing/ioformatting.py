#otput of a program can either be printed in human readable form or
#written in a file for future use (using the write())
#the standard output file can be referenced as sys.stdout

#Ways to format output.
#using formatted string literals
#example code

year = 2016
event = 'Referendum'
f'Results of the {year} {event}'

#using str.format()

yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes / total_votes
'{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)


#you can also do the string handling urself by using string slicing and concatenation 
#operations to create any layout you can imagine.

#when u dont need any fancy output but just want a quick display of some variables for 
#debugging purposes you can convert any value to a string with the repr() or str()
