def converter_k(valor):
    if isinstance(valor, str):
        if valor == "-" or valor == "":
            return 0
        valor = valor.strip().lower()
        if valor.endswith("k"):
            return int(float(valor.replace("k", "")) * 1000)
        elif valor.endswith("m"):
            return int(float(valor.replace("m", "")) * 1000000)
    return int(valor)

