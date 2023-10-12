import os
import shutil
if(os.path.isdir("C:\Binaryfilesdemo1")):
    print("the directory or folder already exists with name binary files demo")
else:
    print("the directory or folder does not exist.. so need folder created")
    os.mkdir("c:\Binaryfilesdemo1")
    os.chdir("c:\Binaryfilesdemo")
    sourcepath = "c:\Binaryfilesdemo\Binaryfile.tbf"
    destinationpath = "c:\Binaryfilesdemo1\Binaryfilecopy.txt"
    shutil.copy(sourcepath,destinationpath)
    print("the file is copied to new location with name binaryfilecopy.pdf")
    os.remove("c:\Binaryfilesdemo1\Binaryfilecopy.pdf")
    os.chdir("c;\Binaryfilesdemo")
    print(os.listdir())