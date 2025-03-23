from pymongo import MongoClient
from bson.objectid import ObjectId

class LivroModel:
    def __init__(self, database):
        self.db = database

    def criar_livro(self, titulo:str, autor:str, ano:int, preco:float):
        try:
            resposta = self.db.collection.insert_one({"titulo": titulo, "autor": autor, "ano": ano, "preco": preco})
            print(f"Livro criado com o ID: {resposta.inserted_id}")
            return resposta.inserted_id
        except Exception as e:
            print(f"Um erro ocorreu ao criar este livro: {e}")
            return None

    def ler_livro_pelo_id(self, id: str):
        try:
            resposta = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Livro encontrado: {resposta}")
            return resposta
        except Exception as e:
            print(f"Um erro ocorreu ao ler este livro: {e}")
            return None

    def atualizar_livro(self, id: str, titulo:str, autor:str, ano:int, preco:float):
        try:
            resposta = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"titulo": titulo, "autor": autor, "ano": ano, "preco": preco}})
            print(f"Livro atualizado: {resposta.modified_count} documento(s) modificado(s)")
            return resposta.modified_count
        except Exception as e:
            print(f"Um erro ocorreu ao atualizar este livro: {e}")
            return None

    def apagar_livro(self, id: str):
        try:
            resposta = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Livro apagado: {resposta.deleted_count} documento(s) apagado(s)")
            return resposta.deleted_count
        except Exception as e:
            print(f"Um erro ocorreu ao apagar este livro: {e}")
            return None