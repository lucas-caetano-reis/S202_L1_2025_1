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


class TeacherCLI(SimpleCLI):
    def __init__(self, teacher_CRUD):
        super().__init__()
        self.teacher_CRUD = teacher_CRUD
        self.add_command("create", self.create_teacher)
        self.add_command("read", self.read_teacher)
        self.add_command("update", self.update_teacher)
        self.add_command("delete", self.delete_teacher)

    def create_teacher(self):
        name = input("Entre com o nome do professor: ")
        data_nasc = input("Entre com a data de nascimento do professor: ")
        cpf = (input("Entre com o CPF do professor: "))
        self.teacher_CRUD.create_teacher(name, data_nasc, cpf)
        print("Professor criado com sucesso.")

    def read_teacher(self):
        name = input("Entre com o nome do professor: ")
        professores = self.teacher_CRUD.read_teacher(name)
        if professores:
            for prof in professores:
                print(f"Nome: {prof[0]}")
                print(f"Data de Nascimento: {prof[1]}")
                print(f"CPF: {prof[2]}")
                print("-" * 20)
        else: 
            print("Professor não encontrado")

    def update_teacher(self):
        name = input("Entre com o nome do professor: ")
        newCpf = input("Entre com o novo cpf do professor: ")
        self.teacher_CRUD.update_teacher(name, newCpf)
        print("CPF atualizado com sucesso.")

    def delete_teacher(self):
        name = input("Entre com o nome do professor a ser deletado: ")
        self.teacher_CRUD.delete_teacher(name)
        print("Professor deletado com sucesso.")
        
    def run(self):
        print("Bem vindo ao CLI dos professores!")
        print("Comandos disponíveis: create, read, update, delete, sair")
        super().run()