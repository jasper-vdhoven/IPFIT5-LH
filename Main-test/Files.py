import os


Folder_path = os.getcwd()
print(Folder_path)

def listDir(dir):
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        print ('File Name: '+ fileName)
        print ('Folder Path: '+ os.path.abspath(os.path.join(dir, fileName)))


if __name__ == '__main__':
    listDir(Folder_path)
