import json
import requests
import bs4
import re
def conta_vezes(link,palavraa):
    vezes=0
    lista=[]

    req=requests.get(link)#recebe url.
    soup = bs4.BeautifulSoup(req.text.upper(),'lxml')#transforma o objeto do request em um soup.
    teste=" ".join(soup.find_all(string=re.compile(palavraa.upper())))#apartir do soup, procura a palavra ignorando diferença de maiusculo e transforma em uma string. 
    teste=teste.split(" ")#divide a string em uma lista
    for i in teste: 
        palavra=limpa(i)#chama função que limpa caracters especiais.
        if palavra==palavraa.upper():#conta quantidade de vezes em que a palavra aparece na lista    
            vezes+=1
    return vezes

def json_repeticoes(site_url,palavra,vezes,lista,nome):#cria um json com nome do site, palavra e qtd de vezes que a palavra aparece.
    no_site={'url':site_url,'palavra':palavra,'vezes':vezes}
    json_l=open(nome+'.json','w')
    json.dumps(no_site)
    json_l.close
    return no_site

def gera(lista,palavraa):#a partir de uma lista de urls e uma palavra chama os metodos para busca e criação de json com os resultados.
    lista_j={}
    links_list=lista
    palavra=palavraa
    numero=0
    for link in links_list:
        if link not in lista_j:
            nome=""+str(numero)
            numero+=1
            lista_j[link]=json_repeticoes(link,palavra,conta_vezes(link,palavra),lista_j,nome)
    for x in lista_j:
        print(lista_j[x])
def limpa(palavra):
    simbolos="'\"|!@#$%&*()_+[]{}?^,.<>;:=-/"
    for i in range (0,len(simbolos)):
        palavra=palavra.replace(simbolos[i],"")
    if len(palavra)>0:
        return palavra
    
