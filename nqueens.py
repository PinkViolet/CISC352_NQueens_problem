import random
import os
import os.path
import operator


def get_input_file():
    global inputFile
    with open(inputFile, "r") as f:
        return [int(x) for x in f]

#For each table size N, run ouputPendingFile() and write_output_file() when solution found
def outputPendingFile(table):
    global table_size
    pendingStr = ""
    for i in range(0, table_size):
        if i == 0:
            pendingStr = pendingStr + "[" + str(table[i]) + ", "
        elif i == (table_size - 1):
            pendingStr = pendingStr + str(table[i]) + "]"
        else:
            pendingStr = pendingStr + str(table[i]) + ", "
    return pendingStr

def write_output_file(pendingStr):
    global outputFile
    with open(outputFile, "a") as f:
        f.write(pendingStr + "\n")

#def initialization() #start the program
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
        

def place_queen(table_size): # can be used for restart
    yCoord = list(range(1,table_size + 1))
    random.shuffle(yCoord)
    return yCoord



'''
find how many conflict the point (col, row) has with Queens
'''
def check_conflict_in_spot(table, row, col):
    count = 0
    queen_x = 1
    #print("table in check spot: ")
    #print(table)
    for queen in table:
        #print("queen: (" + str(queen_x) + ", " + str(queen) + ")\n")
        #print("spot: (" + str(col) + ", " + str(row) + ")\n")
        #print("before count conflict: " + str(count) + "\n")
        if col != queen_x:
            #print("(col, row) = (" + str(col) + ", " + str(row) + ")")
            #print("(queen_x, queen) = (" + str(queen_x) + ", " + str(queen) + ")")
            if row == queen:
                count = count + 1
            if row - col == queen - queen_x:
                count = count + 1
            if row + col == queen + queen_x:
                count = count + 1
        queen_x = queen_x + 1
        #print("after count conflict: " + str(count) + "\n")
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
        #print("col: " + str(target_col))
        c = check_conflict_in_spot(table, row, target_col)
        if c == min_conflict:
            possible_place.append(row)
        elif c < min_conflict:
            possible_place = [row]
            min_conflict = c
#    print("possible_place: ")
#    print(possible_place)
#    print("\n")
#    print("target_col in move queen: " + str(target_col))
#    print("\ntable in move queen: ")
#    print(table)
#    print("target col - 1: " + str(target_col - 1))
    table[target_col - 1] = random.choice(possible_place)
    return table

#table_size = len(table)

#table = [] # x is index [y]

not_improved = 0

inputFile = "nqueens.txt"

outputFile = "nqueens_out.txt"

def find_queen_to_swap(table, col):
    target_row = table[col - 1]
    x = 1
    for y in table:
#        print("index x: " + str(x))
        if target_row == y and x != col:
            return x
        else:
            x = x + 1
    #return col
    

def main():
    '''
    # best table = [5,2,4,1,3]
    table = [2, 5, 4, 3, 1]
    swap_queen_col = 1
    print("table before: ")
    print(table)
    print("\n")
    table = move_queen(table, swap_queen_col)
    print("table after move: ")
    print(table)
    print("\n")
    print("the next col to swap: " + str(find_queen_to_swap(table, swap_queen_col)))
    '''

    
    list_of_TS = get_input_file()
    #print(list_of_TS)
    for i in list_of_TS:
        table = place_queen(i)

        #table = [2, 5, 4, 3, 1]
        check_status = False
        num_conflict = 0
        swap_queen_col = random.randint(1, len(table) + 1)
        #print(swap_queen_col)
        list_conflict = check_conflict(table)
        #print("list_conflict: ")
        #print(list_conflict)
        #print("\n")
        
        while (check_status == False):
            for c in list_conflict:
                num_conflict = num_conflict + c
            if num_conflict != 0:
                table = move_queen(table, swap_queen_col)
                list_conflict = check_conflict(table)
                if list_conflict[swap_queen_col - 1] == 0:
                    swap_queen_col = random.randint(1, len(table))
                else:
                    swap_queen_col = find_queen_to_swap(table, swap_queen_col)
            else:
                check_status == True
        #print("result table: ")
        print(table)
        #print("\n")
    
    return

#        write_output_file(outputPendingFile(table))






main()
