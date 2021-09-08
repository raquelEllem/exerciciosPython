import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except:
    print('Não foi possível acessar o Pudim :(')
else:
    print('Pudim acessado com sucesso!')