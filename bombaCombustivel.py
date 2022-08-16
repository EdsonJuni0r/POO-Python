# Classe Bomba de Combustivel:  Utilizar classes e metodos
# Classe chamada bombaCombustivel
# tipoCombustivel
# valorListro
# quantidadeCombustivel


class bombaCombustivel: #clase Bomba de combustivel
    def __init__(self, tipoCombustivel, valorLitro, quantCombustivel):
        self.tipo = tipoCombustivel
        self.valor = valorLitro
        self.quant = quantCombustivel

    def info(self):
        return print("Tipo de combustivel:",self.tipo, "| Valor por litro:",self.valor, "reais | Quantidade restante de combustivel:",self.quant, "litros") 

    def abastecerPorValor(self,  valor): #função abastecer por valor
        self.litros = valor / self.valor  #divide o valor pago pelo valor do litro do combustivel
        self.quant = self.quant - self.litros #subtrai na quantidade total de combustivel
        return print("A quantidade a ser abatecida com",valor, "reais, é:" ,self.litros, "litros.") #retorna a quantidade de litros a ser abastecida

    def abastecerPorLitro(self,  litros): #função abastecer por litro
        self.valorPago = litros * self.valor #multiplica a quantidade de litros pelo valor do litro do combustivel
        self.quant = self.quant - litros #subtrai na quantidade total de combustivel
        return print("O valor a ser pago para",litros, "litros, é:" ,self.valorPago, "reais.") #retorna o valor a ser pago

    def alterarValor(self, a): #função para alterar o valor do litro
        self.valor = a  #valor recebe um novo valor
        return self.valor  #retorna o novo valor

    def alterarCombustivel(self, b): #função para alterar o tipo do Combustivel
        self.tipo = b #tipo do combustivel recebe um no tipo
        return self.tipo #retorna o novo tipo

    def alterarQuantCombustivel(self, c): #função para alterar a quantidade de combustivel
        self.quant = c  #quantidade recebe uma nova quantidade
        return self.quant #retorna a nova quantidade


b = bombaCombustivel('gasolina', 5, 1000)

print("------------------------------------------------------------------------------------------------")
b.info()#mostra as informações
print("------------------------------------------------------------------------------------------------")
b.abastecerPorValor(20) #chamada da função abastecer por Valor, retorna a quantidade de Litros de acordo com o valor informado

b.abastecerPorLitro(5) #chamada da função abastecer por Litro, retorna o valor a ser pago de  acordo com a quantidade de litros informado
b.info()
print("------------------------------------------------------------------------------------------------")
print("O valor do combustivel foi alterado para:", b.alterarValor(5.95)) #chamada da função Altera Valor, onde é fornecido um novo valor para o litro

print("O novo tipo de combustivel é:" ,b.alterarCombustivel('diesel')) #chamada da função Altera o tipo de combustivel, onde é fornecido um novo tipo de combustivel
 
print("------------------------------------------------------------------------------------------------")
b.info() #mostra as informações atualizadas
print("------------------------------------------------------------------------------------------------")

print("A nova quantidade é:" ,b.alterarQuantCombustivel(2000), "litros.") #chamada da função altera a quantidade de combustivel, onde é fornecido uma nova quantidade de combustivel

print("------------------------------------------------------------------------------------------------")
b.info()#mostra as informações atualizadas
print("------------------------------------------------------------------------------------------------")



