# Open a file

with open('README.md') as file:
    print(file.readline())


# open (file_top_open, mode)
# r = reading
# w = writting
# a = appending


# read() – read all text from a file into a string. This method is useful if you have a small file and you want to manipulate the whole text of that file.
# readline() – read the text file line by line and return all the lines as strings.
# readlines() – read all the lines of the text file and return them as a list of strings.


with open('hello.txt', 'w') as f:
    f.write('This is test file.')
