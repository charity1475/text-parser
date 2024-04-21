import re

"""
We will need an input and output file to read and write the data. 
"""
input_file = "input.txt"
output_file = "output_python.txt"

# Initialized text block flag
in_block = False

"""
In this sample we will read the start delimeter xxx$ and end delimeter #end# to identify the block of text we need to process.
then in the block  we check for each word if it starts with acc and then we extract the number part and add it to the word.
In the use case a number will be used to fecth a value in excel and apppend next.
"""
start_pattern = re.compile(r"\d+\$")
acc_pattern = re.compile(r"acc:(\d+)")


count = 0
with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
    for line in f_in:
        start_match = start_pattern.search(line)
        if start_match:
            in_block = True
        elif "#end#" in line:
            in_block = False

        if in_block:
            words = line.split()
            for word in words:
                acc_match = acc_pattern.search(word)
                if word.startswith("acc"):
                    acc_number = word.split(":")[1]
                    f_out.write(word + "   NEW[ " + acc_number + " ]")
                    count += 1
                else:
                    f_out.write(word)
                f_out.write(" ")
            f_out.write("\n")
        else:
            f_out.write(line)
print(f"{count} Total Accounts  were Found.\n")
