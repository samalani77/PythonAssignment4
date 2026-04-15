
fh = open("sample.txt","wt")
fh.write("This is a sample text file. \n")
fh.write("It contains multiple lines.")
fh.close()

fh = open("sample.txt","rt")
Line1 = fh.readline()
Line2 = fh.readline()
print(f"Reading file content:")
print(f"Line 1: {Line1}")
print(f"Line 2: {Line2}")
fh.close()
