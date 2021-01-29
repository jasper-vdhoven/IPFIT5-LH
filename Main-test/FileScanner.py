import os
import logging
# def __init__(self, path, name, size):
# self.Path = path
# self.Name = name
# self.Size = size

# Set logging settings and create newline, upon starting this function


logging.basicConfig(filename="file_logging.log", level=logging.INFO, format='%(asctime)s, %(levelname)s, %(funcName)s, '
                                                                            '%(message)s')
logging.info('Start of run')


P1 = "/Users/maadalhajsaleh/Desktop"
P2 = ".pdf"
# list = {(path,name),(path,size),(name,path)}
# for(i = 0, i++, i > list.length){
#   list[i] => inputcheck(list[i].p1,list[i].p2)
# }
filesList = []


def InputCheck(P1, P2):
    if isinstance(P1, str) and isinstance(P2, str):
        if P1.__contains__("/"):
            for root, subdirs, files in os.walk(P1):
                for file in files:
                    if file.__contains__(P2):
                        logging.info('Path: ' + root + '\n' + 'File Name: ' + str(file))

        elif P2.__contains__("/"):
            for root, subdirs, files in os.walk(P2):
                for file in files:
                    if file.__contains__(P1):
                        logging.info('Path: ', root + '\n', 'File Name: ', str(file))

    elif isinstance(P2, int):  # TO DO write the logic when P2 is int
        for path, subdirs, files in os.walk(P1):
            for name in files:
                filesList.append(os.path.join(path, name))
            for i in filesList:
                fileSize = os.path.getsize(str(i))
                if fileSize >= P2 * 1024:
                    logging.info("The File: " + str(i) + " File Size is: " + str(fileSize / 1024) + " kiloBytes")

    elif isinstance(P1, int):
        for path, subdirs, files in os.walk(P2):
            for name in files:
                filesList.append(os.path.join(path, name))
            for i in filesList:
                fileSize = os.path.getsize(str(i))
                if fileSize >= P1 * 1024:
                    logging.info("The File: " + str(i) + " is: " + str(fileSize / 1024) + " kiloBytes")
    else:
        logging.info("input error")


if __name__ == "__main__":
    InputCheck(P1, P2)
