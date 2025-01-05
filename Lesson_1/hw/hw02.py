

string = " "
for i in range(1,10):
    for j in range(9-i, 9):
        string = "*" + string + "*"
    for k in range(i,9):
        string = " " + string
    print(string)
    string = " "







