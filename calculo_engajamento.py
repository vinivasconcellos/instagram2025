def formatar_mes(df_postagens2025):
    """
    Remove espaços extras da coluna 'Mês'
    """
    df_postagens2025 = df_postagens2025.copy()  # boa prática para evitar efeitos colaterais
    #df_postagens2025["Mês"] = df_postagens2025["Mês"].astype(str).str.strip()
    df_postagens2025["Mês"] = df_postagens2025["Mês"].str.strip()
    df_postagens2025["Título / Tema do Post"] = df_postagens2025["Título / Tema do Post"].str.strip()
    df_postagens2025["Formato"] = df_postagens2025["Formato"].str.strip()
    df_postagens2025["Mês"] = df_postagens2025["Mês"].str.capitalize()
    df_postagens2025["Título / Tema do Post"] = df_postagens2025["Título / Tema do Post"].str.lower()
    df_postagens2025["Formato"] = df_postagens2025["Formato"].str.capitalize()
    return df_postagens2025





