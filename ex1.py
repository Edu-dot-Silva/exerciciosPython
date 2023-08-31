valorDaConta = float(input('Informe o Valor da conta(Ultilize ponto e nao virgula):'))
valorDaTaxa = float(input('Informe o valor da taxa em % a ser cobrada(Ultilize ponto e nao virgula):'))
valorDaTaxa = valorDaConta/10
tempoEmMeses = int(input('Informe quantos meses ate o pagamento:'))

print('Pelos dados informados,sua conta com valor inicial de',valorDaConta,'após',tempoEmMeses,
      'meses com taxa de',valorDaTaxa,'% ficara com um valor final de',valorDaTaxa*tempoEmMeses+valorDaConta)