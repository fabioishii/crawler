import json
import requests
import bs4
import re
def conta_vezes(link,palavraa):
    vezes=0
    lista=[]
    req=requests.get(link)
    soup = bs4.BeautifulSoup(req.text.upper(),'lxml')
    teste=" ".join(soup.find_all(string=re.compile(palavraa.upper())))
    teste=teste.split(" ")
    for i in teste:
        palavra=limpa(i)
        if palavra==palavraa.upper():    
            vezes+=1
    return vezes

def json_repeticoes(site_url,palavra,vezes,lista,nome):
    no_site={'url':site_url,'palavra':palavra,'vezes':vezes}
    json_l=open(nome+'.json','w')
    json.dumps(no_site)
    json_l.close
    return no_site

def gera(lista,palavra):
    lista_j={}
    links_list=lista
    palavra=palavra
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
    
