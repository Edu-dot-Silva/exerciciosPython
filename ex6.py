print('Central de Filmes')
print('*****************')

filmes = {
    'Batman':{
        'Vilão:Charada'' e '
        'Classificação: 16 anos'
    },
    'Vingadores':{
        'Vilão:Thanos'' e '
        'Classificação: 14 anos'
    },
    'Homem aranha':{
        'Vilão:Sexteto Sinistro'' e '
        'Classificação: 14 anos'
    },
    'Barbie':{
        'Vilão:Ken'' e '
        'Classificação: 12 anos'
    },
    'Flash':{
        'Vilão:Os efeitos especiais'' e '
        'Classificação: 14 anos'
    }
}

print(f'Nossos filmes são: {filmes.keys()}')

filme_escolhido = input('Qual filme você deseja ver mais detalhes? ').capitalize()

if filme_escolhido in filmes.keys():
    print(f'{filme_escolhido}\n{filmes[filme_escolhido]}')
