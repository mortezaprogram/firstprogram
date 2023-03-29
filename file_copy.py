import os
import shutil

fileFormat = r".pdf"
dirpath = r"D:\trainingfoad\python\Udemy_Python_Programming_Bootcamp_2021-12.part1_Downloadly.ir"
desPath = r"D:\file_copy"


def main():
    for (path, dir, file) in os.walk(dirpath):
        for fls in file:
            sourcePath = (str(path) + str('\\') + str(fls))
            if sourcePath.endswith(fileFormat):
                print(sourcePath)
                shutil.copy(sourcePath, desPath)


if __name__ == '__main__':
    main()
