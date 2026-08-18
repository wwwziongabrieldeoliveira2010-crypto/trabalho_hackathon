def vali_txt(text):
    if text.strip == "":
        print ("Erro: o campo tem que ser letra")
        return False

    elif any(text.isdigit() for char in text):
        print ("Erro: campo tem que letra")
        return False


    return True 