class Passageiro:
    def __init__(self, nome: str, documento: str):
        self.nome = nome
        self.documento = documento

    def __str__(self):
        return (
                f"Nome: {self.nome};\n"    
                f"Número de documento: {self.documento}.\n"
            )

class Corrida:
    def __init__(self, nota: int, distancia: float , valor: float, passageiro: Passageiro):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro

    def __str__(self):
        return (
                f"Nota da corrida: {self.nota};\n"
                f"Distância percorrida: {self.distancia} km;\n"
                f"Valor cobrado: R$ {self.valor:.2f};\n"
                f"Passageiro: {self.passageiro}\n"
            )

class Motorista:
    def __init__(self, nota: int, corridas: list[Corrida]):
        self.corridas = corridas
        self.nota = nota
    
    def __str__(self):
        corridas_resumo = "\n".join(str(corrida) for corrida in self.corridas)
        return (
            f"Nota do motorista: {self.nota}\n"
            f"Total de corridas: {len(self.corridas)}\n"
            f"Corridas do motorista:\n\n{corridas_resumo}"
        )