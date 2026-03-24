# Variáveis da pizzaria 
nome = input("Por favor, informe seu nome: ")
pizza_sabor = input("Informe o sabor da pizza - [Frango com Requeijão], [Calabresa], [Mussarela], [Banana com Chocolate]: ")
pizza_tamanho = input("Informe o tamanho da pizza - [Pequena], [Média], [Grande]: ")
dia_semana = input("Informe o dia da semana - [Quarta], [Quinta], [Sexta], [Sábado]: ")

print(f"O sabor escolhida da pizza é {pizza_sabor}, o tamanho é {pizza_tamanho} e hoje é {dia_semana}.")

# Promoções -> Estruturas condicionais.
# Comprando qualquer pizza de qualuqer tamanho, sábado, o refri é gratuito.
# Comprando uma pizza de calabresa de tamanho médio, em qualquer dia, o frete e o refri são gratuitos.
# Comprando qualquer pizza de qualquer tamanho no domingo, o frete e o refri são gratuitos.