import os

read_file = "E:/Python New/vignaR.csv"

fd = os.open(read_file , os.O_RDONLY)

read = (fd,100)

os.close(fd)