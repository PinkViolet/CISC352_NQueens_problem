import random
import os
import os.path


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
def check_conflict(table):
    global table_size
    conflict_num = 0
    x = 1
    conflict_in_col = []
    for i in table:
        y = i
        n = 1
        for j in table:
            if x == 
                conflict = conflict + 1
            if y = j:
                conflict = conflict + 1
                
        x = x + 1
'''       
        

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

    return



main()
