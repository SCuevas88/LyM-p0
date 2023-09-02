
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

def upload_txt(txt_direction):
    estado = True
    with open(txt_direction) as txt:
        for line in txt:
            line = line.strip()

            if not line:
                continue
            tokens = line.split()
            print(tokens)
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
        if i != "(" or i != ")":
            correct_str+=i
            
    lst_walk_fn = correct_str.split(",")
    for i in lst_walk_fn:
        if i in defined_names:
            pass
        else:
            estado = False
    return estado
print(upload_txt("a.txt"))