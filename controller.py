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

def colonia(update, context):
    diccio = EMT.getColonia()
    text = ""

    if(diccio == None):
        context.bot.send_message(chat_id=update.effective_chat.id, text="NO MORE BUSES")

    for i in diccio:
        text += i
        text += " -> "
        text += diccio[i]
        text += "\n"

    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

