test = [[0,1,0,0,0,0,0,1], [0,1,1,0,1,0,0,0], [0,1,1,0,1,1,1,1], [0,1,1,0,1,0,1,0], [0,0,0,0,0,0,0,0]]
new_test  = [[]]

""" {0,1,0,0,0,0,0,1},
    {0,1,1,0,1,0,0,0},
    {0,1,1,0,1,1,1,1},
    {0,1,1,0,1,0,1,0},
    {0,0,0,0,0,0,0,0} """

columns = 3
start = 0
end = columns
count = 0
max_list = 0
max_list_count = 0

if len(test) % 3 == 0:
    max_list = len(test) // columns
else:
    max_list = (len(test) // columns) + 1

while max_list_count < max_list:
    for i in range(len(test[0])):
        for j in range(start, end):
            if j > len(test) - 1:
                new_test[count].append(0)
                continue
            new_test[count].append(test[j][i])
        count += 1
        if len(test[0]) * max_list > count:
            new_test.append([])
    max_list_count += 1
    end += columns
    start += columns

for i in range(len(new_test)):
    for j in range(len(new_test[0])):
        print(new_test[i][j], end = " ")
    if i % 7 == 0 and i != 0:
        print("\n")
    else:
        print()

print()



""" for i in range(8):
    for j in range(3):
        print(test[j][i], end = " ")
    print()
print()
for i in range(8):
    for j in range(3,5):
        print(test[j][i], end = " ")
    print("0") """




