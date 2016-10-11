from default import open_and_returns_bs4_object, create_json_file


urls = 'http://pesquisapramim.com.br/categoria/biscoitos-13'


def produtos(obj):
    produtos = obj.find(
        'div', {'class': 'article'}
    ).find(
        'div', {'class': 'lista'}
    )

    list_produtos = list()
    for produto in produtos.findAll('div', {'class': 'item'}):
        nome = produto.find('a').findAll('span')[1].get_text().strip()
        preco = produto.find('strong').get_text().strip()

        print('{};{}'.format(nome.strip(), preco.strip()))

        list_produtos.append((nome, preco))

    return list_produtos


for page in range(1, 7):
    try:
        url = '{}/?Pag={}'.format(urls, page)
        obj = open_and_returns_bs4_object(url)
        produtos(obj)
    except:
        break
