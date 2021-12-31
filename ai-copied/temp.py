import os
a = open("files","a")
def absoluteFilePaths(directory):
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:
            text = str(os.path.abspath(os.path.join(dirpath, f))) + "\n"
            a.write(text)
absoluteFilePaths(".")
a.close()