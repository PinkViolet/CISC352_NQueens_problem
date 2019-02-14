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
        f.write(pendingStr)

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

#def move_queen()

table_size = 10

#table = [] # x is index [y]

not_improved = 0

inputFile = "nqueens.txt"

outputFile = "nqueens_out.txt"



def main():
#    list_of_TS = get_input_file()
    table = place_queen(10)
    print(table)
    write_output_file(outputPendingFile(table))
    Conflicts = check_conflict(table)
    print(Conflicts)
    return



main()
