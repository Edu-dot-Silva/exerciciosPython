# crie um programa que calcula o aumento de salario

salarioInicial = float(input('Informe o salario:'))
porcentagemDeAumento = float(input('informe quantos porcento de aumento quer aplicar:'))
porcentagemAplicada = float(salarioInicial*porcentagemDeAumento/100)

print('O salario informado de R$',int(salarioInicial),'com aumento de',round(porcentagemDeAumento),'% ficara com um valor final de R$',salarioInicial+porcentagemAplicada)
