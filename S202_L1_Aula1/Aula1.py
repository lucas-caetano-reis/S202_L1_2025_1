class Professor:
    # inicializa a classe professor, que recebe o atributo nome
    def __init__(self, nome):
        # estabele um relacionamento de referência entre a classe e o atributo nome
        self.nome = nome

    # método recebe o argumento assunto
    def ministrar_aula(self , assunto):
        # mostra o nome do professor, assunto da aula e sai do método
        return f"O professor {self.nome} está ministrando uma aula sobre {assunto}."


class Aluno:
    # inicializa a classe aluno, que recebe o atributo nome
    def __init__(self, nome):
        # estabele um relacionamento de referência entre a classe e o atributo nome
        self.nome = nome

    def presenca(self):
        # mostra o nome do aluno e sai do método
        return f"O aluno {self.nome} está presente."

class Aula:
    # inicializa a classe Aula, que recebe os atributos professor e assunto
    def __init__(self, professor, assunto):
        self.professor = professor
        self.assunto = assunto
        #cria uma lista de alunos, relacionada à classe
        self.alunos = []

    def adicionar_aluno(self, aluno): #método recebe o atributo aluno
        # adciona todos os alunos à lista alunos
        # append -> adiciona aluno à lista
        self.alunos.append(aluno)

    def listar_presenca(self):
        # saída de texto e chamada do nome do professor
        print(f"Presença na aula sobre {self.assunto} ministrada pelo professor {self.professor.nome}:\n")
        #roda a lista de alunos, chama o método presenca e formata a string para que cada presença esteja em uma linha separada
        return "\n".join(aluno.presenca() for aluno in self.alunos)

#cria uma instância de Professor, com o nome "Lucas"
professor = Professor("Lucas")
#cria duas instâncias de aluno, chamadas "Maria" e "Pedro"
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
#cria uma instância de aula, com uma instància de professor e um assunto
aula = Aula(professor, "Programação Orientada a Objetos")
#chama os métodos adicionar_aluno, lista_presenca e ministrar_aula
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
print(aula.listar_presenca(), "\n")
print(professor.ministrar_aula("Programação Orientada a Objetos"))