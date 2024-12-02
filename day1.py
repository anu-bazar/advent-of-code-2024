#Part one
file_name = "C:\\Users\\anuba\\Downloads\\advent-of-code\\day1\\input.txt"
with open(file_name, "r") as file:
    lines = file.readlines()
    column_1=[]
    column_2=[]
    result = []
    for line in lines:
        column_1.append(line.split("   ")[0])
        column_2.append(line.split("   ")[1].replace("\n",""))
    #sort columns
    column_1.sort()
    column_2.sort()
    
    for i in range(len(column_1)):
        if column_1[i] > column_2[i]:
            result.append(int(column_1[i])-int(column_2[i]))
        elif column_1[i] < column_2[i]:
            result.append(int(column_2[i])-int(column_1[i]))
        else:
            result.append(0)
    print(sum(result))


#Part two 
