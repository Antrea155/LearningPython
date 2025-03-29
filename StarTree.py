
treeHight = 9;
sym = '*';
sym_space = ' ';
rowStr = '';
x = 1;

while x <= treeHight:
    w = (x*2) - 1
    rowStr = '';
    xspaces = treeHight - x;
    i = 1;
    while i <= xspaces:
        rowStr += sym_space;
        i+= 1;
    i=1;
    while i <= w:
        rowStr += sym;
        i +=1;
    print(rowStr);
    x+= 1;


"""
for x in range(1, treeHight + 1):  
    w = (x * 2) - 1 
    rowStr = sym * w 
    print(rowStr.center(treeHight * 2 - 1))  #
"""