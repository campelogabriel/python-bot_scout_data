def get_text(texto):
    new_arr_text = []
    texto = texto.split(" ")
    texto_sem_metion = []
    for n in texto:
        if n.startswith("@"):
            continue
        else:
            texto_sem_metion.append(n)

    texto_tratado = " ".join(texto_sem_metion)


    if ' no ' in texto_tratado:
        new_arr_text = texto_tratado.strip().split("no")
        return {"nome": new_arr_text[0],"camp": new_arr_text[1]}            
    elif ' na ' in texto_tratado:
        new_arr_text = texto_tratado.strip().split("na")
        return {"nome": new_arr_text[0],"camp": new_arr_text[1]}    
    if ' pelo ' in texto_tratado:
        new_arr_text = texto_tratado.strip().split("pelo")
        return {"nome": new_arr_text[0],"camp": new_arr_text[1]}
    elif ' pela ' in texto_tratado:
        new_arr_text = texto_tratado.strip().split("pela")
        return {"nome": new_arr_text[0],"camp": new_arr_text[1]}
    elif ' em ' in texto_tratado:
        new_arr_text = texto_tratado.strip().split("em")
        return {"nome": new_arr_text[0],"camp": new_arr_text[1]}
    else:
        return {"nome": texto_tratado.strip(),"camp": ""}



