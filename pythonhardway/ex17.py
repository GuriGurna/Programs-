from sys import argv 
from os.path import exists 
 
script, from_file, to_file = argv
 
print(f"copying from {from_file} to {to_file}")
# we could do these two on one line ,how?
in_file = open(from_file)
indata = in_file.read()

print(f"the input file is {len(indata)} bytes long ")

print(f"does the output file exists? {exists(to_file)}")
print("ready, hit RETURN to continue , CTRL-C to abort.")
input()

out_file = open(to_file)
out_file.write(indata) 

print("alright, all done.")

out_file.close()
in_file.close()
