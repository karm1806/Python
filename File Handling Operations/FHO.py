with open("class-notes.txt", "w") as f:
    f.write("Hello World!!!")
    print(f.write)
f.close()
with open("class-notes.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
file.close()        
file = open("new.txt", "x")
import os
if os.path.exists("demofile.txt"):
    print('File exists!!!')
else:
    print("The file does not exist.")
file2 = open("sample_doc", "w")
import os
os.remove("sample_doc.txt")
import os
os.rmdir("Sample Folder")