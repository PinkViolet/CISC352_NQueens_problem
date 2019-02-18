import random
import os
import os.path
import operator

inputFile = "nqueens.txt"

outputFile = "nqueens_out.txt"

def get_input_file():
    global inputFile
    with open(inputFile, "r") as f:
        return [int(x) for x in f]

#For each table size N, run ouputPendingFile() and write_output_file() when solution found
def outputPendingFile(table):
    global table_size
    pendingStr = ""
    for i in range(0, len(table)):
        if i == 0:
            pendingStr = pendingStr + "[" + str(table[i]) + ", "
        elif i == (len(table) - 1):
            pendingStr = pendingStr + str(table[i]) + "]"
        else:
            pendingStr = pendingStr + str(table[i]) + ", "
    return pendingStr

def write_output_file(pendingStr):
    global outputFile
    with open(outputFile, "a") as f:
        f.write(pendingStr + "\n")


'''
Takes in the y coordinates and returns the number of conflicts based on the x coordinate
forward diagnol conflicts are respective piece (the first value is piece with x value of 1, etc etc
backward diagnol is same as forward
'''
def check_conflict(table):
    conflict_y = []
    position = 0
    conflict_forward = []
    conflict_backward = []
    forwardDiagnol = []
    backwardDiagnol = []
    totalConflicts = []
    for i in table:
        conflict_y.append(table.count(i)-1)
        forwardDiagnol.append((position+1)-i)
        backwardDiagnol.append((position+1)+i)
        position = position + 1
    for x in forwardDiagnol:
        conflict_forward.append(forwardDiagnol.count(x)-1)
    for y in backwardDiagnol:
        conflict_backward.append(backwardDiagnol.count(y)-1)
    totalConflicts = list(map(operator.add, conflict_y, conflict_forward))
    totalConflicts = list(map(operator.add, totalConflicts, conflict_backward))
    return (totalConflicts)      

'''
Initialize the table and no points in same col and row
'''
def place_queen(table_size): # can be used for restart
    yCoord = list(range(1,table_size + 1))
    random.shuffle(yCoord)
    return yCoord



'''
find how many conflict the point (col, row) has with all Queens
'''
def check_conflict_in_spot(table, row, col):
    count = 0
    queen_x = 1
    for queen in table:
        if col != queen_x:
            print("(col, row) = (" + str(col) + ", " + str(row) + ")")
            print("(queen_x, queen) = (" + str(queen_x) + ", " + str(queen) + ")")
            if row == queen:
                count = count + 1
            if row - col == queen - queen_x:
                count = count + 1
            if row + col == queen + queen_x:
                count = count + 1
        queen_x = queen_x + 1
    return count

'''
for each column calculate the conflict the point
(C, Ri) has for every i in range(1, table size + 1)
and form a list contain the spot with minimun conflict
and randomly choose a spot to place queen
'''
def move_queen(table, target_col):
    possible_place = []
    min_conflict = len(table)
    for row in range(1, len(table) + 1):
        c = check_conflict_in_spot(table, row, target_col)
        if c == min_conflict:
            possible_place.append(row)
        elif c < min_conflict:
            possible_place = [row]
            min_conflict = c
    table[target_col - 1] = random.choice(possible_place)
    return table

'''
This Fumction is to find a new col which has the same row
with the previous modified col
'''
def find_queen_to_swap(table, col):
    target_row = table[col - 1]
    x = 1
    for y in table:
        if target_row == y and x != col:
            return x
        else:
            x = x + 1
    #don't find second col, random a new col
    return random.randint(1, len(table))
    

def main():
    list_of_TS = get_input_file()
    for table_size in list_of_TS:5
        col_to_swap = random.randint(1, table_size)
        final_check = False
        table = place_queen(table_size)
        while final_check == False:
            total_conflict = 0
            c_list = check_conflict(table)
            for c in c_list:
                total_conflict = total_conflict + c
            if total_conflict == 0:
                final_check = True
                write_output_file(outputPendingFile(table))
            else:
                table = move_queen(table, col_to_swap)
                col_to_swap = find_queen_to_swap(table, col_to_swap)

    return



main()
