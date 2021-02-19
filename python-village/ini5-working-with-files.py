file=open("rosalind_ini5.txt","r")
lines=file.readlines()
output=open("ini5_out.txt","w+")
for i,line in enumerate(lines):
    if i%2==0:
        continue
    else:
        output.write(line)
