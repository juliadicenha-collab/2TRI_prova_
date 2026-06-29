class carro:
    def __init__(self, marca, modelo, placa, valor_diaria):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.valor_diaria = valor_diaria
        self.quilometragem = 0
        self.disponivel = True

    def exibir(self):
        status = "Disponível" if self.disponivel else "Alugado"
        print(f"\n--- Dados do Veículo ---")
        print(f"Carro: {self.marca} {self.modelo} | Placa: {self.placa}")
        print(f"Diária: R$ {self.valor_diaria:.2f} | KM: {self.quilometragem} km")
        print(f"Status: {status}")
        print("-" * 24)

    def alugar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"Sucesso: {self.modelo} alugado!")
        else:
            print(f"Erro: {self.modelo} já está alugado.")

    def devolver(self, nova_quilometragem):
        if self.disponivel:
            print(f"Erro: {self.modelo} não está alugado.")
            return

        if nova_quilometragem <= self.quilometragem:
            print(f"Erro: KM {nova_quilometragem} inválida. Deve ser maior que {self.quilometragem} km.")
            return

        self.quilometragem = nova_quilometragem
        self.disponivel = True
        print(f"Sucesso: {self.modelo} devolvido com {self.quilometragem} km.")
