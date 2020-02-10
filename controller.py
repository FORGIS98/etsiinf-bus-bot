import EMT

def etsiinf():
    diccio = EMT.getEtsiinf()
    text = ""

    if(diccio == None):
        return "NO MORE BUSES"

    for i in diccio:
        text += i
        text += " -> "
        text += diccio[i]
        text += "\n"

    return text

def colonia():
    diccio = EMT.getColonia()
    text = ""

    if(diccio == None):
        return "NO MORE BUSES"

    for i in diccio:
        text += i
        text += " -> "
        text += diccio[i]
        text += "\n"

    return text

