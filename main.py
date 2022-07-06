# This is a sample Python script.
test_file = open("test.txt", "w")
test_file.write("This is a long list of numbers\n")

for i in range(1000):
    test_file.write(str(i) + "\n")

test_file.close()
