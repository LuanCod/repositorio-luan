bicicletas = ['trek' , 'cannondale' , 'redline' , 'specialized']

message = "Minha primeira bicicleta foi uma " + bicicletas[2].title() + "."
print(message)


times = ['real madrid' , 'barcelona' , 'arsenal' , 'liverpool' , 'chelsea' , 'manchester city']
print(times[3].title())

times.append(['manchester united' , 'milan' , 'inter' , 'roma'])

print(times)

mensagem_time = "Raimundinho torce para o " + times[6][2].title() + "!"
print(mensagem_time)

# times[6] = 'corínthians'
# del times[1]

pop_times = times.pop(6)

print (pop_times)