def nome_valido(nome):
    return bool(nome) and all(c.isaplha() or c.isspace() for c in nome)

#Essa função percorre cada caractere da string nome e verifica se é uma letra ou espaço,
#bloqueando qualquer outro tipo de dado