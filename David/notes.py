/*
How to download the cs50 library?

1a. Download the CS50 Library from https://github.com/cs50/libcs50/releases
1b. Extract/unzip the downloaded zipped folder
2a. Open Terminal and change directory to the unzipped CS50 library folder. For example if folder is on desktop and the folder is named libcs50-10.1.0 , then terminal command should be:
cd desktop/libcs50-10.1.0
2b. Still in terminal after changing directory, then run the command:
sudo make install
3a. After installation, close terminal, go to visual studio and write your C program
#include <cs50.h>
3b. Link cs50 when compiling your code with clang. Example if your file name is hello.c
clang hello.c -o hello -lcs50
If you run clang hello.c -o hello -lcs50, no make hello is needed

Binary codes = machine codes 
source codes = human codes 

source codes => compiler => machine codes 

How to compile using CLI?
1) ./make yourFilename (your file name must not have the c extension which is .c)
OR
1) clang fileName.c -o fileName -lcs50 for using CS50 library

2) ./fileName (your file name must not have the c extension which is .c)

BackSlash (\n):
-> To create a new line

Adding variable into strings
-> printf("Hello, %s\n", variable)
-> This is for strings only (%s)

How to deal with having strings with percent symbol?
-> Use double percent

C programming variable's types?
-> bool
-> char
-> double
-> float
-> int
-> long 
-> strings

What is char? 
-> Char stands for character

For example 'y'
-> Use signle quotes only!


And Or operators?
-> And => &
-> or => ||













*/