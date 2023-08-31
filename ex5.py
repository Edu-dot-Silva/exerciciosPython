#um dicionario vario semana
#colocar um chave para cada dia da semana
#o valor de cada dia é um lista de aulas que existem no dia
#sabado e domingo opcional ser vazio ou nao

print('************************')
print('Consulta Aulas da Semana')
print('************************')

dias_da_semana = {
    'Segunda' : 'Python e JavaScript',
    'Terça' : 'Java e Ruby',
    'Quarta' : 'C e C++',
    'Quinta' : 'Android e Kotlin',
    'Sexta' : 'C# e PHP'

}

while True:
    print('Qual dia da semana você gostaria de consultar o horario de aula?')
    dia_solicitado = input('Digite o dia: ').capitalize()

    if dia_solicitado in dias_da_semana:
        print(f'Na {dia_solicitado} você tera aulas de {dias_da_semana[dia_solicitado]}')

    if dia_solicitado == 'Sabado' or dia_solicitado == 'Domingo':
        print(f'Vai descansar loko,aula de {dia_solicitado}? Ta maluco?')
        break