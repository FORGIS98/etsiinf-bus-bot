import model


def etsiinf():
    return model.getEtsiinf()

def colonia():
    return model.getColonia()

def aluche():
    return model.getAluche()

def moncloa():
    return model.getMoncloa()


options = {
        "etsiinf": etsiinf,
        "colonia": colonia,
        "aluche": aluche,
        "moncloa": moncloa
        }

def busInfo(name):
    dic = options[name]()
    text = ""

    for i in dic:
        if(dic[i] == []):
            dic[i].append("Parece que no hay buses :/")
        text += i
        text += " -> "
        text += " | ".join(dic[i])
        text += "\n"

    return text
