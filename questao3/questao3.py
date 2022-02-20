def grupoDeAnagramas(palavra):
    grupo_anagramas = dict()
    anagramas = list()

    for n in range(1, len(palavra)+1):
        for i in range(0, len(palavra)):
            palavra_ordenada = "".join(sorted(palavra[i: i+n]))

            if len(palavra_ordenada) < n:
                break
            if palavra_ordenada not in grupo_anagramas:
                grupo_anagramas[palavra_ordenada] = [palavra[i: i + n]]
            else:
                grupo_anagramas[palavra_ordenada].append(palavra[i: i + n])

            if len(grupo_anagramas[palavra_ordenada]) >= 2:
                anagramas.append(grupo_anagramas[palavra_ordenada])

    return len(anagramas), anagramas

palavra = 'ifailuhkqq'
print(grupoDeAnagramas(palavra))
