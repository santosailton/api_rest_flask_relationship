import mysql.connector


def testar_conexao():
    try:
        # Configurar os parâmetros de conexão
        host = 'database-3.c7kdr3enlzpi.us-west-2.rds.amazonaws.com'  # substitua pelo endereço do seu servidor MySQL
        database = 'BooksData'  # substitua pelo nome do seu banco de dados
        user = 'admin'  # substitua pelo nome de usuário do seu banco de dados
        password = '123456789'  # substitua pela senha do seu banco de dados

        # Estabelecer a conexão com o banco de dados
        conexao = mysql.connector.connect(
            host=host,
            # database=database,
            user=user,
            password=password
        )

        # Verificar se a conexão foi estabelecida com sucesso
        if conexao.is_connected():
            print('Conexão estabelecida com sucesso!')

            # Fechar a conexão
            conexao.close()
            print('Conexão fechada.')

    except mysql.connector.Error as erro:
        print(f'Erro ao conectar ao banco de dados: {erro}')


# Chamando a função para testar a conexão
testar_conexao()
