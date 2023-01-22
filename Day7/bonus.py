filenames = ["1.doc","2.report","3.presentation"]

filenames = [filename.replace('.','-')+'.txt' for filename in filenames]

for names in filenames:
    print(names)