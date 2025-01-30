def outros(df, cutoff):

    count = 0
    for i, v in df.items():
        if v < cutoff:
            count += v
            df.pop(i)

    if count > 0: df["Outros"] = count
    return df

def analisa(df, dado, pct, mostra_nome=True, nome=None):
    
    analise = df[dado].value_counts()

    if mostra_nome:
        if nome: analise.name = nome
        else: analise.name = dado
    else:
        analise.name = ''

    print(analise)

    analise = outros(analise, len(df) * pct)

    return analise