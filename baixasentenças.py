# -*- encoding: utf-8 -*-
import bs4, re, shelve
from selenium import webdriver


def entranapagina():#loga no site do tcu e baixa arquivos

    browser = webdriver.Firefox(executable_path='C:\\Users\\cubas\\OneDrive\\python\\scripts\\geckodriver.exe')
    browser.get('https://pje.tjdft.jus.br/consultapublica/ConsultaPublica/listView.seam')

    classe_judicial = 'PROCEDIMENTO DO JUIZADO ESPECIAL CÍVEL'
    data_autuaçãoi = '19/01/2018'
    data_autuaçãof = '06/04/2018'
    tipo_processo = 'Inclusão Indevida em Cadastro de Inadimplentes'

    browser.find_element_by_id('fPP:j_id175:classeJudicial').send_keys(classe_judicial)
    browser.find_element_by_id('fPP:dataAutuacaoDecoration:dataAutuacaoInicioInputDate').send_keys(data_autuaçãoi)
    browser.find_element_by_id('fPP:dataAutuacaoDecoration:dataAutuacaoFimInputDate').send_keys(data_autuaçãof)
    browser.find_element_by_id('fPP:searchProcessos').click()

    x = input('Se solicitado, complete o captcha. Pressione qualquer tecla.')

# acha os processos a terem a decisão baixada:

    site = browser.page_source
    sitesoup = bs4.BeautifulSoup(site)
    elementos = sitesoup.find_all("a", string=re.compile(tipo_processo))
    print('elementos:')
    print(elementos)

    enderecos = []
    for ele in elementos:
        print('ele:')
        print(ele)
        click = ele.get("onclick")
        print('click:')
        print(click)
        enderecos.append(click)
    print('endereços:')
    print(enderecos)

    #salva lista no hd
    shelfarq = shelve.open('C:\\extratordesentenças\\extratordesentencas')
    shelfarq['enderecos_processos'] = enderecos
    shelfarq.close()
    print('endereços salvos no hd')


entranapagina()
print('extração finalizada')
