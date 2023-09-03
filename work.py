
"""
def upload_txt(txt_direction):
    txt = open(txt_direction)
    for i in txt:
        lst = i.replace("\n","").split(" ")
        print(lst)
        if not(revisar_lst(lst)):
            break
def revisar_lst(lst):
    #TODO hacer los if
    estado = ""
    for i in lst:
        if i == "":
            estado = True
        elif i == "defVar":
            estado = True                
        elif "walk" in i:
            #falta revisar walk function
            lst_i = i.split("(").split(")")
            values = lst_i[1]
        elif estado:
            pass
        else:
            estado = False
        if not(estado):
            break
    return estado

"""
defined_names = []
procedures = []
lista_corchetes = []
lista_direcciones = ["north", "south", "west", "east","front", "right", "left","back"]

def upload_txt(txt_direction):
    estado = True
    with open(txt_direction) as txt:
        for line in txt:
            line = line.strip()

            if not line:
                continue
            if ";" in line:
                line = line[0:len(line)-1]
            tokens = line.split()
            print(tokens)
            print(estado)
            estado = process_tokens(tokens,estado)
            if estado == False:
                break
    if sum(lista_corchetes) != 0:
        estado = False
    return estado

def process_tokens(tokens,estado):
    if tokens[0] == "defVar":
        estado = define_variable(tokens,estado)
    elif tokens[0] == "defProc":
        #corregir define_procedure, esta no define variable como defVar
        estado = define_procedure(tokens,estado)
    elif tokens[0] == "{":
        lista_corchetes.append(1)
    elif tokens[0] == "}":
        lista_corchetes.append(-1)
    elif "walk" in tokens[0]:
        estado = walk_function(tokens,estado)
    elif "drop"in tokens[0]:
        print(defined_names)
        estado = one_pos_func(tokens,estado,"drop",defined_names)
    elif "get" in tokens[0]:
        estado = one_pos_func(tokens,estado,"get",defined_names)
    elif "grab" in tokens[0]:
        estado = one_pos_func(tokens,estado,"grab",defined_names)
    elif "letGo" in tokens[0]:
        estado = one_pos_func(tokens,estado,"letGo",defined_names)
    elif tokens[0] == "nop()" or tokens[0] == "nop ()":
        estado = True
    elif tokens[0] in procedures:
        #falta
        pass
    elif "if" == tokens[0]:
        estado = funct_if(tokens,estado)
    elif "while" == tokens[0]:
        estado = funct_while(tokens,estado)
    elif "repeat" == tokens[0]:
        estado = funct_repeat(tokens,estado)
    else:
        estado = validate_command(tokens,estado)
    return estado

def define_variable(tokens, estado):
    if len(tokens) >= 3:
        variable_name = tokens[1]
        defined_names.append(variable_name)
    else:
        estado = False
    return estado

def define_procedure(tokens,estado):
    if len(tokens) >= 3:
        procedure_name = tokens[1]
        procedures.append(procedure_name)
    else:
        estado = False
    return estado
def validate_command(tokens,estado):
    for token in tokens:
        if token in defined_names:
            continue
        elif token.startswith('(') and token.endswith(')'):
            function_name = token[1:-1]
            if function_name not in defined_names:
                estado = False
        else:
            estado = False  
    return estado
def walk_function(tokens,estado):
    #aun no esta acabada la funcion
    val = ""
    for i in tokens:
        if i == "walk":
            continue
        elif "walk" in i:
            i = i.split("(")
            val += i[1]
        else:
            val += i
    correct_str =""
    for i in val:
        if i != "(" and i != ")":

            correct_str+=i

    lst_walk_fn = correct_str.split(",")
    result_Try = 0
    for i in lst_walk_fn:
        try:
            float(i)
            result_Try = True 
        except:
            result_Try = False

        if i in defined_names:
            estado = True
        elif i in lista_direcciones:
            estado = True
        elif result_Try:
            estado = True
        
        else:
            estado = False
            
    return estado
def one_pos_func(tokens,estado,fn,type):
    if tokens[0] != fn:
        tokens[0].split("(")
    val = ""
    for i in tokens:
        if i == fn:
            print("entra")
            continue
        elif i == "(" or i == ")":
            continue
        elif fn in i:
            i = i.split("(")
            if len(i[1])>1:
                val = i[1][0]
            else:
                val = i[1]
            if val in type:
                estado = True
        elif i in type:
            estado = True
        elif len(i)>1:
            val_2 = ""
            for j in i:
                if j != "(" and j != ")":
                    val_2 +=j

            if val_2 in type:
                estado = True
            else:
                estado = False               
            
        else:
            estado = False
    return estado     
def funct_if(tokens,estado):
    #TODO hacerla toda
    for i in tokens:
        if i == "if":
            continue
        else:
            estado = False
    return estado
def funct_while(tokens,estado):
    #TODO hacerla toda
    return estado
def funct_repeat(tokens,estado):
    #TODO hacerla toda
    return estado
def cond_detection(tokens,estado):
    #completar function
    i = 0
    el = tokens[i]
    while el != "{":
        if "can" in el:
            estado = True
        else:
            estado = False
        i +=1
        el = tokens[i]
    return estado
print(upload_txt("a.txt"))