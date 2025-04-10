from Modelos import Motorista, Corrida, Passageiro
from bson import ObjectId

class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def criar_motorista(self, motorista:Motorista):
        try:
            documento = {
                "nota": motorista.nota,
                "corridas": [
                    {
                        "nota": corrida.nota,
                        "distancia": corrida.distancia,
                        "valor": corrida.valor,
                        "passageiro": {
                            "nome": corrida.passageiro.nome,
                            "documento": corrida.passageiro.documento
                        }
                    }
                    for corrida in motorista.corridas
                ]
            }
            resposta = self.db.collection.insert_one(documento)
            print(f"Motorista criado com o ID: {resposta.inserted_id}\n") #cria um id para o objeto
            return resposta.inserted_id
        except Exception as e:
            print(f"Um erro ocorreu ao criar este motorista: {e}\n")
            return None

    def ler_motorista_pelo_id(self, id: str):
        try:
            dados = self.db.collection.find_one({"_id": ObjectId(id)})
            if not dados:
                print(f"Motorista não encontrado. Por favor, confira o id: {dados}.\n")
                return None
            
            corridas = []
            for corridas_dados in dados["corridas"]:
                passageiro = Passageiro(
                    nome=corridas_dados["passageiro"]["nome"],
                    documento=corridas_dados["passageiro"]["documento"]
                )
                corrida = Corrida(
                    nota=corridas_dados["nota"],
                    distancia=corridas_dados["distancia"],
                    valor=corridas_dados["valor"],
                    passageiro=passageiro
                )
                corridas.append(corrida)

            motorista = Motorista(nota=dados["nota"], corridas=corridas)
            return motorista
        except Exception as e:
            print(f"Um erro ocorreu ao ler este motorista: {e}\n")
            return None

    def atualizar_motorista(self, id: str, nota:int):
        try:
            resposta = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"nota": nota}})
            print(f"Motorista atualizado: {resposta.modified_count} documento(s) modificado(s)\n")
            return resposta.modified_count
        except Exception as e:
            print(f"Um erro ocorreu ao atualizar este motorista: {e}\n")
            return None

    def apagar_motorista(self, id: str):
        try:
            resposta = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Motorista apagado: {resposta.deleted_count} documento(s) apagado(s)\n")
            return resposta.deleted_count
        except Exception as e:
            print(f"Um erro ocorreu ao apagar este motorista: {e}\n")
            return None