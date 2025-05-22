#Questão 3
class TeacherCRUD:
    def __init__(self, database): #recebe a instância do banco de dados
        self.db = database #armazenando a instância do banco de dados na variável self.db

    def create_teacher(self, name, data_nasc, cpf): #cria um professor com um nome, data de nascimento e cpf
        query = "CREATE (:Teacher {name: $name, data_nasc: $data_nasc, cpf: $cpf})" #query para criar um professor
        parameters = {"name": name, "data_nasc": data_nasc, "cpf": cpf} #parâmetros da query
        self.db.execute_query(query, parameters) #executa a query no banco de dados

    def read_teacher(self, name): #lê os dados de um professor
        query = """
        MATCH (t:Teacher {name: $name})
        RETURN t.name AS name, t.data_nasc AS data_nasc, t.cpf AS cpf
        """
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters) #executa a query no banco de dados
        return [(result["name"], result["data_nasc"], result["cpf"]) for result in results] #retorna os dados de um professor

    def update_teacher(self, name, newCpf):
        query = "MATCH (t:Teacher {name: $name}) SET t.cpf = $newCpf"
        parameters = {"name": name, "newCpf": newCpf}
        self.db.execute_query(query, parameters)

    def delete_teacher(self, name):
        query = "MATCH (t:Teacher {name: $name}) DETACH DELETE t"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)