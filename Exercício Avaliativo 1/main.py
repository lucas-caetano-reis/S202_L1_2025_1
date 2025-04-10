from database import Database
from dao import MotoristaDAO
from cli import MotoristaCLI #interface para o usuário editar a coleção

db = Database(database="MotoristasBD", collection="Motoristas") # banco de dados e collection que serão utilizados neste exercício avaliativo
motoristaDAO = MotoristaDAO(database=db)
db.resetDatabase


motoristaCLI = MotoristaCLI(motoristaDAO)
motoristaCLI.run()