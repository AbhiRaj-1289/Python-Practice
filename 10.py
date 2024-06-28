with open("sample.txt","r") as reader, open("Sample_copy.txt","w") as writer:
        for lines in reader:
            lines = lines[::-1]
            writer.write(lines)
            print(lines,end=" ")  