preco = float(input('Digite o preço do produto:'))
p = float(input('Digite o percentual de desconto do produto:'))

desconto = preco * (p/100)

final = preco - desconto

print("O preço do produto é {}, o desconto será de {}%.".format(preco, p))
print('O valor calculado de desconto é: {}. O valor final do produto será: {}'. format(desconto, final))