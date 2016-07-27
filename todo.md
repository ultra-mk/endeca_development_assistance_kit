#Bugs and Issues

## SQL Parser
1. Error handling in parse_sql_file(self): does not seem to get called from within the `__main__()`. It prints the error but doesn't stop the method from being called.

2. Something about the following line of SQL `TO_CHAR(SYSDATE, 'yyyy-MM-dd') AS REPORT_RUN_DATE,` broke the sql_parser. I'm guessing it has to do with the comma in the TO_CHAR function call, but that's only a guess at this point.


#Features and ideas 

## SQL Generator
1. Simple thing. Set schema with a script. Get rid of that stupid schema + table concat
2. Add SQL for `FND_EID_GROUPS_TL` table.
3. Add group name for `FND_EID_ATTR_GROUPS` as a parameter. Currently exists as a class variable.


## XML Generator



## EQL Generator


## SQL Parser
Really need some resiliancy there. Commented lines, multiple columns on a line can bork the whole thing.

## Reader Writer
Fix some of those ugly methods.

improve the implementation of the Excel Writer.

Need to build some resiliancy there. If there's a single empty cell, it can bork the whole thing. Basically, I need to scan all the cells and remove any empty ones.

## Readme
Readme is pretty out of date.