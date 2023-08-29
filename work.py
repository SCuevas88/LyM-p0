
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
    estado = True
    for i in lst:
        if i == "":
            estado = True
        elif estado:
            pass
        else:
            estado = False
        if estado == False:
            break
    return estado
upload_txt("a.txt")