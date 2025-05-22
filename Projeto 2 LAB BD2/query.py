class TeacherDatabase:
    def __init__(self, database): #recebe a instância do banco de dados
        self.db = database #armazenando a instância do banco de dados na variável self.db

    def encontrar_renzo(self): #função usada para buscar um professor cujo nome seja Renzo
        query = """
        MATCH (t:Teacher)
        WHERE t.name = 'Renzo'
        RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf
        """
        results = self.db.execute_query(query) #executa a query no banco de dados
        return [(result["ano_nasc"], result["cpf"]) for result in results]
    
    def encontrar_comeca_com_m(self): #função usada para buscar um professor cujo nome comece com a letra M
        query = """
        MATCH (t:Teacher)
        WHERE t.name STARTS WITH 'M'
        RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf
        ORDER BY t.name
        """
        results = self.db.execute_query(query) #executa a query no banco de dados
        return [(result["ano_nasc"],result["cpf"]) for result in results]
    
    def encontrar_cidades(self): #função usada para buscar todas as cidades
        query = """
        MATCH (c:City)
        RETURN c.name AS name
        """
        results = self.db.execute_query(query) #executa a query no banco de dados
        return [result["name"] for result in results]
    
    def encontrar_escolas(self): #função usada para buscar todas as escolas com número entre 150 e 550
        query = """
        MATCH (s:School)
        WHERE 150 <= s.number <= 550
        RETURN s.name AS name, s.address AS address, s.number AS number
        """
        results = self.db.execute_query(query) #executa a query no banco de dados
        return [(result["name"],result["address"],result["number"]) for result in results]
    
    def encontrar_professor_mais_novo_e_professor_mais_velho(self): #função usada para buscar os professores com a maior e menor idade
        query = """
        MATCH (t:Teacher)
        RETURN MAX(t.ano_nasc) as mais_novo, MIN(t.ano_nasc) as mais_velho
        """
        results = self.db.execute_query(query)
        result = results[0]
        return result["mais_novo"], result["mais_velho"]

    def media_aritmetica_populacao_cidades(self):
        query = """
        MATCH (c:City)
        RETURN AVG(c.population) as media_populacoes
        """
        results = self.db.execute_query(query)
        return results[0]["media_populacoes"]
    
    def buscar_cep_e_mudar_nome(self):
        query = """
        MATCH (c:City)
        WHERE c.cep = "37540-000"
        RETURN REPLACE(c.name, "a", "A") AS nome
        """
        results = self.db.execute_query(query)
        return [(result["nome"]) for result in results]
    
    def letra_nome_professor(self):
        query = """
        MATCH (t:Teacher)
        RETURN substring(t.name, 2, 1) as caractere
        """
        results = self.db.execute_query(query)
        return [(result["caractere"]) for result in results]