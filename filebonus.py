contents = ['Monday', 'Tuesday', 'Wednesday']

filenames = ['file1.txt', 'file2.txt', 'file3.txt']

for content, file in zip(contents, filenames):
    file = open(f"{file}", 'w')
    file.write(content)