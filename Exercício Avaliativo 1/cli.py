#É a interface de modificação da coleção

from dao import MotoristaDAO
from Modelos import Passageiro, Corrida, Motorista

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input(f"\nEntre com um comando:")
            if command == "sair":
                print("Tchau!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print(f"Comando inválido. Tente novamente.\n")

class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_dao: MotoristaDAO):
        super().__init__()
        self.motorista_dao = motorista_dao
        self.add_command("criar", self.criar_motorista)
        self.add_command("ler", self.ler_motorista)
        self.add_command("atualizar", self.atualizar_motorista)
        self.add_command("apagar", self.apagar_motorista)

    def criar_motorista(self):
        qtd_corridas = int(input(f"Quantas corridas deseja cadastrar?"))
        corridas = []

        for i in range(qtd_corridas):
            print(f"\nCorrida {i+1}:")
            nota_corrida = int(input("Nota da corrida: "))
            distancia = float(input("Distância (km): "))
            valor = float(input("Valor (R$): "))

            nome_passageiro = input("Nome do passageiro: ")
            documento_passageiro = input("Documento do passageiro: ")

            passageiro = Passageiro(nome_passageiro, documento_passageiro)
            corrida = Corrida(nota_corrida, distancia, valor, passageiro)
            corridas.append(corrida)


        nota_motorista = int(input("Nota do motorista: "))
        
        motorista = Motorista(nota_motorista, corridas)
        self.motorista_dao.criar_motorista(motorista)

    def ler_motorista(self):
        id = input(f"Entre com o id do motorista:")
        motorista = self.motorista_dao.ler_motorista_pelo_id(id)
        if motorista:
            print(f"Motorista encontrado: {id}\n")
            print(f"{motorista}\n")

    def atualizar_motorista(self):
        id = input(f"Entre com o id do motorista:")
        nota = int(input(f"Entre com a nota do motorista:"))
        self.motorista_dao.atualizar_motorista(id, nota)

    def apagar_motorista(self):
        id = input(f"Entre com o id do motorista: ")
        self.motorista_dao.apagar_motorista(id)
        
    def run(self):
        print(f"Bem vindo ao CLI dos motoristas!")
        print(f"Comandos disponíveis: criar, ler, atualizar, apagar, sair\n")
        super().run()