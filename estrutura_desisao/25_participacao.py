participacao = 0

telefone = input("Telefonou para vítima? (Responda com sim ou não.) ")
if telefone == 'sim':
    participacao +=1
local = input("Esteve no local do crime? (Responda com sim ou não.) ")
if local == 'sim':
    participacao +=1
mora = input("Mora perto da vítima? (Responda com sim ou não.) ")
if mora == 'sim':
    participacao +=1
devia = input("Devia para a vítima? (Responda com sim ou não.) ")
if devia == 'sim':
    participacao +=1
trabalhou = input("Já trabalhou com a  vítima? (Responda com sim ou não.) ")
if trabalhou == 'sim':
    participacao +=1

if participacao == 2:
    print("Suspeita!")
elif participacao > 2 and participacao <= 4:
    print("Cúmplice!")
elif participacao == 5:
    print("Assassino!")
else:
    print("Inocente!")