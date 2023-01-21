contents = ["I want to learn python","Do you think programming is so easy?","I hope i can work as SOC from Juni"]
filenames=["doc.txt","report.txt","present.txt"]

# for index,content in enumerate(contents):
#     file=open(filenames[index],'w')
#     file.writelines(content)
#     file.close()
    
for filename,content in zip(filenames,contents):
    file = open(filename,"w")
    file.write(content)
    