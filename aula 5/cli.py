class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Entre com um comando: ")
            if command == "sair":
                print("Tchau!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido. Tente novamente.")


class PersonCLI(SimpleCLI):
    def __init__(self, livro_model):
        super().__init__()
        self.livro_model = livro_model
        self.add_command("criar", self.criar_livro)
        self.add_command("ler", self.ler_livro)
        self.add_command("atualizar", self.atualizar_livro)
        self.add_command("apagar", self.apagar_livro)

    def criar_livro(self):
        titulo = input("Entre com o título do livro: ")
        autor = input("Entre com o autor do livro: ")
        ano = int(input("Entre com o ano de publicação do livro: "))
        preco = float(input("Entre com o preço de venda do livro: "))
        self.livro_model.criar_livro(titulo, autor, ano, preco)

    def ler_livro(self):
        id = input("Entre com id do livro: ")
        livro = self.livro_model.ler_livro_pelo_id(id)
        if livro:
            print(f"Título: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Ano: {livro['ano']}")
            print(f"Preço: {livro['preco']}")

    def atualizar_livro(self):
        id = input("Entre com o id do livro: ")
        titulo = input("Entre com o título do livro: ")
        autor = input("Entre com o autor do livro: ")
        ano = int(input("Entre com o ano de publicação do livro: "))
        preco = float(input("Entre com o preço de venda do livro: "))
        self.livro_model.atualizar_livro(id, titulo, autor, ano, preco)

    def apagar_livro(self):
        id = input("Entre com o id do livro: ")
        self.livro_model.apagar_livro(id)
        
    def run(self):
        print("Bem vindo ao CLI dos livros!")
        print("Comandos disponíveis: criar, ler, atualizar, apagar, sair")
        super().run()