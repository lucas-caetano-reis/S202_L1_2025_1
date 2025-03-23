from database import Database
from writeAJson import writeAJson
from livroModel import LivroModel
from cli import PersonCLI

db = Database(database="Livros_BD", collection="Livros")
livroModel = LivroModel(database=db)
db.resetDatabase


personCLI = PersonCLI(livroModel)
personCLI.run()
