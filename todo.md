#Bugs and Issues

## SQL Parser
1. Error handling in parse_sql_file(self): does not seem to get called from within the `__main__()`. It prints the error but doesn't stop the method from being called.

2. Something about the following line of SQL `TO_CHAR(SYSDATE, 'yyyy-MM-dd') AS REPORT_RUN_DATE,` broke the sql_parser. I'm guessing it has to do with the comma in the TO_CHAR function call, but that's only a guess at this point.


#Features and ideas 

## SQL Generator
1. Look at another general refactor
2. It's getting more and more tightly couple to the main class. specifically how group has to be the last argument passed. The class and the main file just know too much about each other. 
3. The test suite needs some major love and attention.

## XML Generator
1. Add RecordType and RecordSpec to the xml file
2. More meaningful name for metadata name

## EQL Generator
1. add where clause to end of file

## SQL Parser
Failure modes

1. Multiple columns per line

## Reader Writer

make the file extension optional

make the filenames reflect the group name

Fix some of those ugly methods.

improve the implementation of the Excel Writer.

Need to build some resiliancy there. If there's a single empty cell, it can bork the whole thing. Basically, I need to scan all the cells and remove any empty ones.

## Readme
Readme is pretty out of date.
