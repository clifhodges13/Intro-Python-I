"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
with open('./foo.txt') as foo:
  print(foo.read())

print(foo.closed) # Prints True if the file successefully closed after reading

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open('./bar.txt', 'w+') as bar:
  lines = ('Your mother was a hampster,\n', 'and your father smelled of elderberries.\n', 'Now go away, or I shall taunt you a second timuh.')
  for l in lines:
    bar.write(l)