def removeEmptyLines():
    with open("file1.txt", 'r') as inp, open('file2.txt', 'w') as out:
        for line in inp:
            if line.strip():
                out.write(line)

removeEmptyLines()
