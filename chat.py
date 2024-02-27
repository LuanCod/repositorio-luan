minha_lista = [10, 20, 30, 40, 50]

sublista_inicio_omitido = minha_lista[1:3]  # Equivalente a minha_lista[0:3]
sublista_fim_omitido = minha_lista[2:4]    # Equivalente a minha_lista[0:5]

print(sublista_inicio_omitido)
print(sublista_fim_omitido)

print(len(sublista_inicio_omitido))

meu_dict = {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'}

print(meu_dict)

produto = {'nome': 'Laptop', 'preco': 1200, 'estoque': 50}
del produto['estoque']

print(produto)