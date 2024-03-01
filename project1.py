#open input file in read mode
ifile = open("/Users/ajarajachitrala/Documents/content/input.pdf")
#read and store the file content in variable named fcontent
fcontent = ifile.read()
#close input file
ifile.close()
#open output file in write mode
ofile = open("/Users/ajarajachitrala/Documents/content/output.txt", "w")
#write input file content to output file 
ofile.write(fcontent)
#close output file
ofile.close()





