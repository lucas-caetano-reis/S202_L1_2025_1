from database import Database
from query import TeacherDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.200.34.106:7687", "neo4j", "abrasive-decision-coating")
# db.drop_all() # Deletando todos os dados do banco de dados para começar do zero

# Criando uma instância da classe GameDatabase para interagir com o banco de dados
teacher_db = TeacherDatabase(db)

print("=" * 50)
print("1. Data de nascimento e CPF do professor Renzo:")
for ano_nasc, cpf in teacher_db.encontrar_renzo():
    print(f"  - Ano de nascimento: {ano_nasc}, CPF: {cpf}")

print("=" * 50)
print("2. Professores com nomes que começam com a letra 'M':")
for ano_nasc, cpf in teacher_db.encontrar_comeca_com_m():
    print(f"  - Ano de nascimento: {ano_nasc}, CPF: {cpf}")

print("=" * 50)
print("3. Cidades presentes no banco de dados:")
for cidade in teacher_db.encontrar_cidades():
    print(f"  - {cidade}")

print("=" * 50)
print("4. Escolas com números entre 150 e 550:")
for nome, endereco, numero in teacher_db.encontrar_escolas():
    print(f"  - {nome}, {endereco}, nº {numero}")

print("=" * 50)
print("5. Professor mais novo e mais velho:")
mais_novo, mais_velho = teacher_db.encontrar_professor_mais_novo_e_professor_mais_velho()
print(f"  - Mais novo (ano de nascimento): {mais_novo}")
print(f"  - Mais velho (ano de nascimento): {mais_velho}")

print("=" * 50)
print("6. Média aritmética das populações das cidades:")
print(f"  - Média: {teacher_db.media_aritmetica_populacao_cidades():.2f}")

print("=" * 50)
print("7. Substituição de 'a' por 'A' no nome da cidade com CEP 37540-000:")
for nome in teacher_db.buscar_cep_e_mudar_nome():
    print(f"  - {nome}")

print("=" * 50)
print("8. Terceira letra dos nomes dos professores:")
for letra in teacher_db.letra_nome_professor():
    print(f"  - {letra}")
print("-" * 20)