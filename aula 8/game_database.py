import uuid #para criar IDs únicos

class GameDatabase:
    def __init__(self, database): #recebe a instância do banco de dados
        self.db = database #armazenando a instância do banco de dados na variável self.db

    def create_player(self, name): #cria um jogador com um nome e um ID único
        query = "CREATE (:Player {id: $id, name: $name})" #query para criar um jogador
        parameters = {"id": str(uuid.uuid4()), "name": name} #parâmetros da query, incluindo um ID único gerado com uuid4
        self.db.execute_query(query, parameters) #executa a query no banco de dados

    def create_match(self): #cria uma partida com um ID único
        id = str(uuid.uuid4())
        query = "CREATE (:Match {id: $id})"
        parameters = {"id": id}
        self.db.execute_query(query, parameters)
        return id

    def insert_player_match(self, player_name, id, player_score):
        query = """
        // Cria a partida se o id não corresponder a uma partida já existente
        MERGE (m:Match {id: $id})


        // Se o jogador não existir, cria um novo jogador
        MERGE (p:Player {name: $player_name})

        // Cria a relação entre o jogador e a partida
        // Se a relação já existir, atualiza a pontuação
        MERGE (p)-[r:PLAYED]->(m)
        ON CREATE SET r.score = $player_score
        ON MATCH SET r.score = $player_score
        """
        parameters = {"player_name": player_name, "id": id, "player_score": player_score}
        self.db.execute_query(query, parameters)

    def get_players(self): #retorna todos os jogadores do banco de dados
        query = "MATCH (p:Player) RETURN p.name AS name" #query para retornar todos os jogadores
        results = self.db.execute_query(query) #executa a query no banco de dados
        return [result["name"] for result in results] #retorna uma lista com os nomes dos jogadores

    def get_match(self, id): #retorna os detalhes de uma partida específica
        query = "MATCH (m:Match {id: $id})<-[r:PLAYED]-(p:Player) RETURN p.name AS player_name, r.score AS player_score, m.id AS id"
        parameters = {"id": id}
        results = self.db.execute_query(query, parameters)
        return [(result["player_name"], result["player_score"]) for result in results]

    def update_player(self, old_name, new_name):
        query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def delete_player(self, name):
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
    
    def delete_match(self, id):
        query = "MATCH (m:Match {id: $id}) DETACH DELETE m"
        parameters = {"id": id}
        self.db.execute_query(query, parameters)

    def get_player_history(self, player_name):
        print(f"Histórico de Jogador: {player_name}")
        query = """
        MATCH (p:Player {name: $name})- [r:PLAYED]->(m:Match)
        RETURN m.id AS id, r.score AS score
        """
        parameters = {"name": player_name}
        results = self.db.execute_query(query, parameters)
        return [(r["id"], r["score"]) for r in results]