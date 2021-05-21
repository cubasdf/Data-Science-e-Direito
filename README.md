# Data-Science-e-Direito

I.	Objetivo do Programa.
O programa, escrito em Python, tem o objetivo de construir um banco de dados com o endereço das informações públicas de processos judiciais, junto ao TJDFT, escolhidos de acordo com os critérios definidos pelo usuário e disponibilizados no site de consulta pública de processos do TJDFT.
Desse modo, o programa visa proporcionar uma base de dados que permita o estudo qualitativo e quantitativo dos processos judiciais junto ao TJDFT de acordo com as técnicas aprendidas no curso Data Science e Direito, como análises gráficas e estatísticas.

II.	Resultado do Programa.
Uma lista, criada pelo módulo Shelve do Pyhton, que armazena em disco rígido o endereço das informações públicas de processos judiciais, junto ao TJDFT, escolhidos de acordo com os critérios definidos pelo usuário.

III.	Desafios para a implementação e aperfeiçoamento do Programa.
a.	Desafios Técnicos:
i.	A consulta pública dos processos judiciais no Pje (Processo Judicial Eletrônico) do TJDFT é protegida por reCAPTCHA, o que dificulta o desenvolvimento de aplicativos de automação para extração de dados.
ii.	O número de processos retornados na consulta pública do Pje do TJDFT é muito reduzido, limitado a 31, o que tornam necessárias muitas iterações para a construção de um banco de dados robusto.

b.	Desafios para a criação do módulo que analisa o banco de dados (em construção):
i.	A análise quantitativa e qualitativa dos processos judiciais requer a avaliação de vários tipos de decisões judiciais, não apenas das Sentenças, como as decisões interlocutórias. Por exemplo, há categorias de processos judiciais que tiveram suas apreciações suspensas, por Despacho Interlocutório, para aguardar o julgamento de Incidente de Resolução de Demandas Repetitivas (art. 976 do CPC), como ocorreu para a classe “Inclusão Indevida em Cadastro de Inadimplentes”, em que há vários processos suspensos no aguardo do julgamento do REsp. 1.525.174/RS.

IV.	Observações Finais.

a.	O programa está disponibilizado no GitHub.com
b.	A utilização do programa pressupõe, além da instalação do Python e dos módulos utilizados: 
i.	Para a utilização automatizada do Firefox, é necessário o download do arquivo geckodriver.exe e sua cópia na correspondente pasta. O arquivo está disponível em https://github.com/mozilla/geckodriver/releases.
ii.	Criação da pasta C:\extratordesentenças
c.	A simplicidade do programa permite a fácil alteração das variáveis que contém as características dos processos judiciais, bem como a iteração da pesquisa para a criação de um grande banco de dados de modo a trabalhar com o limitador de 31 processos retornados na pesquisa pública do Pje do TJDFT.
