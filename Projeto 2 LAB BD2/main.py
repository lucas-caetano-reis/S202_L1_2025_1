from database import Database
from teacher_crud import TeacherCRUD
from CLI import TeacherCLI

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.200.34.106:7687", "neo4j", "abrasive-decision-coating")
# db.drop_all() # Deletando todos os dados do banco de dados para começar do zero

# Criando uma instância da classe TeacherDatabase para interagir com o banco de dados
teacherDB = TeacherCRUD(db)

teacherDB.create_teacher("Chris Lima", 1956, "189.052.396-66")
teacherDB.read_teacher("Chris Lima")
teacherDB.update_teacher("Chris Lima", "162.052.777-77")

print(f"Por favor, consulte o banco de dados para verificar se as alterações foram feitas.\n")

teacherCLI = TeacherCLI(teacherDB)
teacherCLI.run()

# Fechando a conexão com o banco de dados
db.close()