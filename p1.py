#Fall 2019 CO term-project
#Zhaoxi Sun & Hongbao Zhao & Qiran Sun & Yang Yi

import sys



arguments = sys.argv[1:]
branches = {}
def getInstructions(arguments):#Hongbo Zhao
    global branches
    mode = arguments[0]
    file = arguments[1]
    instruction = ""
    line_num = 0
    f= open(file)
    for line in f.readlines():
        line = line.strip()
        instruction += line
        line_num += 1
        lenOfInst = len(line)
        if line[lenOfInst-1] == ":":
            branch_name = line[0: lenOfInst-1]
            branches[branch_name] = line_num
    f.close()


def set_cycleStages(cycle_stages, i, j, current_stage):#Hongbo Zhao
    if current_stage == 1:
        k = 0
        while k < j:
            cycle_stages[j].append(".")
            k += 1
        cycle_stages[j].append("IF");
        k = j + 1
        while k < 16:
            k += 1
            cycle_stages[j].append(".")
    elif cycle_stages[j][i] == "*":
        pass
    elif current_stage == 2:
        cycle_stages[j][i] = "ID"
    elif current_stage == 3:
        if cycle_stages[j][i-1] == "*":
            cycle_stages[j][i] = "*"
        else:
            cycle_stages[j][i] = "EX"
    elif current_stage == 4:
        if cycle_stages[j][i-1] == "*":
            cycle_stages[j][i] = "*"
        else:
            cycle_stages[j][i] = "MEM"
    elif current_stage == 5:
        if cycle_stages[j][i-1] == "*":
            cycle_stages[j][i] = "*"
        else:
            cycle_stages[j][i] = "WB"
            
def getOperation(instruction, operation):#Hongbo Zhao
    lenInst = len(instruction)
    if instruction[len-1] == ':':
        return "branch"
    if instruction == "nop":
        return "nop"
    index = 0
    while instruction[index] != ' ':
        index += 1
    operation = instruction[0:index]
    if operation == "bne" or operation == "beq":
        return "J"
    else:
        return "I"

    
def read_instruction(instruction, tt)：#Zhaoxi Sun
    #gloabl variables to allow us to change the data in the function
    global destination
    global operand1
    global operand2
    #N type
    if tt=="N":
        operand_count = 0
        for i in range(len(instruction)):
            if instruction[i] == "$":
                if operand_count == 0: #count is 0, just destination
                    operand_count += 1
                    destination = instruction[i+1:i+3]
                elif operand_count == 1:
                    if instruction[i+1] == "z":
                        operand1 = instruction[i+1:i+5]
                    else:
                        operand1 = instruction[i+1,i+3]
                    operand_count += 1
            elif instruction[i] == "," and operand_count == 2:
                if instruction[i+1] == "$":
                    operand2 = instruction[i+1:i+3]
                else:
                    operand2 = instruction[i+1,len(instruction)]
    #J type
    elif tt== "J":
        operand_count = 0
        for i in range(len(instruction)):
            if instruction[i] == "$":
                if operand_count == 0:
                    operand_count+=1;
                    operand1 = instruction[i+1:i+3]
                elif operand_count == 1:
                    operand2 = instruction[i+1:i+3]
             elif instruction[i-1] == "," and operand_count == 1:
                destination = instruction[i:len(instruction)]
destinations = {}                
def set_destinationStage(destination, current_stage):#Hongbo Zhao
    global destinations
    destinations[destination] = current_stage

    
    
    
    
def update_registerFile(operation, destination, operand1, operand2, register_file):#Mike Yang
    global destination 
    global operation1
    global operation2
    v0 = 0
    if operation1 == "zero":
        v1 = 0
    else:
        v1 = register_file[operand1][1] #    assuming maps are implemented as lists of lists
    if operation == "add" or operation == "and" or operation == "or" or operation == "slt":
        v2 = register_file[operand2][1]
        if operation == "add":
            v0 = v1 + v2
        elif operation == "and":
            v0 = v1 & v2
        elif operation == "or":
            v0 = v1^v2
        elif operation == "slt":
            if v1 < v2:
                v0 = 1
            else:
                v0 = 0
    else:
        v2 = int(operand2)
        
            
