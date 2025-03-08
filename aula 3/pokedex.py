from database import Database
from helper.writeAJson import writeAJson

class Pokedex:
    def __init__(self, bancoDeDados: Database):
        self.database = bancoDeDados # Armazena a instância do banco de dados

    #Pokemons por nome
    def getPokemonByName(self, nome: str):
        resultado = self.database.collection.find_one({"name": nome})
        writeAJson(resultado, "Pokemon_por_nome") # Gera o log
        return resultado

    #Pokemons por tipo
    def getPokemonsByType(self, tipos: list):
        resultado = list(self.database.collection.find({"type": {"$in": tipos}}))
        writeAJson(resultado, "Pokemon_por_tipo") # Gera o log
        return resultado
    
    #Pokemons por fraqueza
    def getPokemonsbyWeaknesses(self, fraquezas: list):
        resultado = list(self.database.collection.find({"weaknesses": {"$all": fraquezas}}))
        writeAJson(resultado, "Pokemon_por_fraquezas") # Gera o log
        return resultado
    
    #Pokemons por número
    def getPokemonByNumber(self,numero: str):
        resultado = self.database.collection.find({"num": numero})
        writeAJson(resultado, "Pokemon_por_numero")
        return resultado
    
    #Pokemons por chance de aparição
    def getPokemonBySpawnChance(self, menor_chance_de_aparicao: float, maior_chance_de_aparicao: float):
        resultado = list(self.database.collection.find({"spawn_chance": {"$gt": menor_chance_de_aparicao, "$lt": maior_chance_de_aparicao}}))
        writeAJson(resultado, "Pokemon_por_chance_de_aparicao")
        return resultado

# Criando a instância do banco de dados
db = Database(database="pokedex", collection="pokemons")

# Criando a instância da Pokedex
pokedex = Pokedex(db)

#Todos os pokemons
pokemons = db.collection.find()
# db.resetDatabase()

#Pokemon por nome
pikachu = pokedex.getPokemonByName("Pikachu")

#Pokemons por tipo
tipos = ["Fighting"]
pokemons = pokedex.getPokemonsByType(tipos)

#Pokemons por fraquezas
fraquezas = ["Psychic" , "Ice"]
pokemons = pokedex.getPokemonsbyWeaknesses(fraquezas)

#Pokemons por número
numero = pokedex.getPokemonByNumber("151")

#Pokemons por chance de aparição
pokemons = pokedex.getPokemonBySpawnChance(0.3, 0.6)