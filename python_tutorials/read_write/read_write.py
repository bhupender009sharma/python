fw = open('sample.txt', 'w')  # fw is our object , open is function to open or create a file, sample.txt is the file
                              # name that we created , and 'w' is the keyword to write into the file
fw.write('I have written this line\n')   # write is the function to write
fw.write('sabka maalik ek \n')           # \n moves the cursor to the next line
fw.close()                               # this will close the file, so it does not use extra memory

fr = open('sample.txt','r')          # here we created fr object for file reading, and r is the keyword to reading
text = fr.read()                     # we stored all the strings of the sample file into the text variable
fr.close()
print(text)
