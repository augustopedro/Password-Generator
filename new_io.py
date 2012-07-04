'''Modulo para manipulação de conteudo de arquivos .txt divididos pelo
separador \\n(Quebra de linha).'''


def extrai_conteudo(nome_arq):
    '''Abre um arquivo de nome nome_arq e retorna uma lista com as linhas do
    arquivo sem a quebra de linha(\\n) .'''
    lista = []
    with open(nome_arq, 'r')as arq:
        for linha in arq:
            lista.append(linha.strip())
    return lista


def grava_conteudo(lista, nome_arq):
    '''Grava conteúdo de uma lista em um arquivo de nome nome_arq.'''
    with open(nome_arq, 'a') as arq:
        for elem in lista:
            arq.write(elem)
            arq.write('\n')