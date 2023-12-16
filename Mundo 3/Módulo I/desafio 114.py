import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except:
    print('ERRO! Não foi possível acessar esse site')
else:
    print('Site acessado com sucesso!')