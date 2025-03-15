from database import Database
from helper.writeAJson import writeAJson

class ProductAnalyzer:
    def __init__(self, banco_de_dados: Database):
        self.database = banco_de_dados

    # 1- Total de vendas por dia
    def total_vendas_por_dia(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$data_compra", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"_id": 1}}
        ]
        result = list(self.database.collection.aggregate(pipeline))
        writeAJson(result, "Total_de_vendas_por_dia")
        return result

    # 2- Produto mais vendido em todas as compras
    def produto_mais_vendido(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"Produtos": "$produtos.descricao", "Compra": "$data_compra"}, "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"_id.Compra": 1, "total": -1}},
            {"$group": {"_id": "$_id.Compra", "Produtos": {"$first": "$_id.Produtos"}, "quantidade": {"$first": "$total"}}}
        ]
        result = list(self.database.collection.aggregate(pipeline))
        writeAJson(result, "Produto_mais_vendido_em_cada_compra")
        return result

    # 3- Cliente que mais gastou em uma única compra
    def cliente_que_mais_gastou(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ]
        result = list(self.database.collection.aggregate(pipeline))
        writeAJson(result, "Cliente_que_mais_gastou_em_uma_única_compra")
        return result

    # 4- Lista de produtos que venderam mais do que uma quantidade
    def produtos_acima_de_quantidade(self, quantidade_minima):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
            {"$match": {"total": {"$gt": quantidade_minima}}}
        ]
        result = list(self.database.collection.aggregate(pipeline))
        writeAJson(result, "Lista_de_produtos_que_venderam_mais_do_que_uma_quantidade")
        return result

# Criando a instância do banco de dados
db = Database(database="mercado", collection="compras")
db.resetDatabase()

# Criando a instância de ProductAnalyzer
analyzer = ProductAnalyzer(db)

# Executando as análises
analyzer.total_vendas_por_dia()
analyzer.produto_mais_vendido()
analyzer.cliente_que_mais_gastou()
analyzer.produtos_acima_de_quantidade(1)