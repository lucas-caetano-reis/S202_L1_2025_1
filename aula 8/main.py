from database import Database
from game_database import GameDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.197.118.97:7687", "neo4j", "center-maneuver-songs")
db.drop_all() # Deletando todos os dados do banco de dados para começar do zero

# Criando uma instância da classe GameDatabase para interagir com o banco de dados
game_db = GameDatabase(db)

# Criando alguns jogadores
game_db.create_player("Lucas")
game_db.create_player("Vinícius")
game_db.create_player("Jean")
game_db.create_player("Lucca")

# Criando algumas partidas e suas relações com os jogadores
match1 = game_db.create_match()
match2 = game_db.create_match()

# Atualizando o nome de um jogador
game_db.update_player("Jean", "Ricardo") # Atualizando o nome de Jean para Ricardo

game_db.insert_player_match("Lucas", match1, 300)
game_db.insert_player_match("Vinícius", match1, 200)
game_db.insert_player_match("Lucca", match1, 150)
game_db.insert_player_match("Ricardo", match1, 100)

game_db.insert_player_match("Lucas", "123456789", 1000)

game_db.insert_player_match("Lucas", match2, 500)
game_db.insert_player_match("Vinícius", match2, 400)
game_db.insert_player_match("Lucca", match2, 300)
game_db.insert_player_match("Ricardo", match2, 0)

# Deletando um jogador e uma partida
game_db.delete_player("Ricardo")
game_db.delete_match("987654321")

# Imprimindo todas as informações do banco de dados
print("Jogadores:")
print(game_db.get_players())
print("-" * 20)
print("Partidas:")
print(game_db.get_match(match1))
print("-" * 20)
print(game_db.get_match("123456789"))
print("-" * 20)
print(game_db.get_player_history("Lucas"))
print("-" * 20)
print(game_db.get_player_history("Vinícius"))
print("-" * 20)
print(game_db.get_player_history("Lucca"))
print("-" * 20)

# Fechando a conexão com o banco de dados
db.close()