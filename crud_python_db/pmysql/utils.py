
import MySQLdb


def conectar():
    """
    Função para conectar ao servidor
    """
    try:
        conn = MySQLdb.connect(
            db='pmysql',
            host='localhost',
            user='projeto',
            passwd='projeto'
        )
        return conn
    except MySQLdb.Error as e:
        print(f'Erro na conexão ao MySQL Server: {e}')


def desconectar(conn):
    """ 
    Função para desconectar do servidor.
    """
    if conn:
         conn.close()


def listar():
    """
    Função para listar os produtos
    """
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()

    if len(produtos) > 0:
        print('Listando produtos...')
        print('--------------------')
        for produto in produtos:
            print(f'ID: {produto[0]}')
            print(f'Produto: {produto[1]}')
            print(f'Preço: {produto[2]}')
            print(f'Estoque: {produto[3]}')
            print('--------------------')
    else:
        print(f'Não existem produtos cadastrados.')
    desconectar(conn)
     

def inserir():
    """
    Função para inserir um produto
    """  
    conn = conectar()
    cursor = conn.cursor()

    nome = input(f'Informe o nome do produto: ')
    preco = float(input(f'Informe o preço do produto:'))
    estoque = int(input('Informe a quantidade em estoque: '))
    cursor.execute(f"INSERT INTO produtos (nome, preco, estoque) VALUES ('{nome}', {preco}, {estoque}) ")
    conn.commit()
    
    if cursor.rowcount == 1:
        print(f'O produto {nome} foi inserido com sucesso.')
    else:
        print('Não foi possível inserir o produto.')
    desconectar


def atualizar():
    """
    Função para atualizar um produto
    """
    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input('Informe o nome do produto: '))
    nome = input('Informe o novo nome do produto: ')
    preco = float(input('Informe o novo preço do produto: '))
    estoque = int(input('Informe a nova quantidade em estoque: '))

    cursor.execute(f"UPDATE produtos SET nome='{nome}', preco={preco}, estoque={estoque} WHERE id={codigo}")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'O produto {nome} foi atualizado com sucesso.')
    else:
        print('Erro ao atualizar o produto.')
    desconectar(conn)
    

def deletar():
    """
    Função para deletar um produto
    """  
    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input('Informe o código do produto: '))

    cursor.execute(f'DELETE FROM produtos WHERE id={codigo}')
    conn.commit()

    if cursor.rowcount == 1:
        print('Produto excluído com sucesso.')
    else:
        print(f'Erro ao excluir o produto com id = {codigo}')
    desconectar(conn)


def menu():
    """
    Função para gerar o menu inicial
    """
    print('========= Gerenciamento de Produtos ==============')
    print('Selecione uma opção: ')
    print('1 - Listar produtos.')
    print('2 - Inserir produtos.')
    print('3 - Atualizar produto.')
    print('4 - Deletar produto.')
    opcao = int(input())
    if opcao in [1, 2, 3, 4]:
        if opcao == 1:
            listar()
        elif opcao == 2:
            inserir()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
        else:
            print('Opção inválida')
    else:
        print('Opção inválida')
