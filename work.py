
lista_corchetes = []
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
upload_txt("a.txt")



# Intento Sergio
defined_names = set()

def upload_txt(txt_direction):
    with open(txt_direction) as txt:
        for line in txt:
            line = line.strip()
            if not line:
                continue
            tokens = line.split()
            process_tokens(tokens)

def process_tokens(tokens):
    if tokens[0] == "defVar":
        define_variable(tokens)
    elif tokens[0] == "defProc":
        define_procedure(tokens)
    elif tokens[0] == "{":
        pass
    else:
        validate_command(tokens)

def define_variable(tokens):
    if len(tokens) >= 3:
        variable_name = tokens[1]
        defined_names.add(variable_name)
    else:
        print("Error: Invalid variable definition")

def define_procedure(tokens):
    if len(tokens) >= 3:
        procedure_name = tokens[1]
        defined_names.add(procedure_name)
    else:
        print("Error: Invalid procedure definition")

def validate_command(tokens):
    for token in tokens:
        if token in defined_names:
            continue
        elif token.startswith('(') and token.endswith(')'):
            function_name = token[1:-1]
            if function_name not in defined_names:
                print(f"Error: Undefined function '{function_name}'")
        else:
            print(f"Error: Undefined variable or command '{token}'")

upload_txt("a.txt")