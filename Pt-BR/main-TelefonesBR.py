from TelefonesBR import telefonesbr
import re

telefone = "552126481234"
telefone_objeto = telefonesbr(telefone)

#padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
#resposta = re.search(padrao,telefone)
#print(resposta.group())

print(telefone_objeto)