# Variáveis da pizzaria 

nome = input("Por favor, informe seu nome: ")
FRETE = 2 # contanten fake
pizza_sabor = input("Informe o sabor da pizza - [Frango com Requeijão], [Calabresa], [Mussarela], [Banana com Chocolate]: ")
pizza_tamanho = input("Informe o tamanho da pizza - [Pequena], [Média], [Grande]: ")
dia_semana = input("Informe o dia da semana - [Quarta], [Quinta], [Sexta], [Sábado], [Domingo]: ")

print(f"O sabor escolhida da pizza é {pizza_sabor}, o tamanho é {pizza_tamanho} e hoje é {dia_semana}.")

# Promoções -> Estruturas condicionais.
# Comprando qualquer pizza de qualuqer tamanho, sábado, o refri é gratuito.
if dia_semana == "Sábado":
    print("Pedido aceito com sucesso!")
    print("O Refri hoje é por conta da casa, aproveite!")
elif dia_semana == "Domingo":
    print("Pedido aceito com sucesso!")
    print("O frete e o Refri hoje é por conta da casa, aproveite!")
elif pizza_sabor == "Calabresa" and pizza_tamanho == "Média":
    print("Pedido aceito com sucesso!")
    print("O frete é são por conta da casa, aproveite!")

# Comprando uma pizza de calabresa de tamanho médio, em qualquer dia, o frete é gratuito.
# Comprando qualquer pizza de qualquer tamanho no domingo, o frete e o refri são gratuitos.