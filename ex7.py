# um programa de auxilio de notas para monta a media final
# 2 semestres com duas notas


print('Vamos calcular a media final dos alunos')
divisor = 2

# notas do primeiro semestre

primeiraNota = float(input('Qual a nota da primeira prova do primeiro semestre?'))
segundaNota = float(input('Qual a nota da segunda prova do primeiro semestre?'))

# notas do segundo semestres

terceiraNota = float(input('Qual a nota da primeira prova do segundo semestre?'))
quartaNota = float(input('Qual a nota da segunda prova do segundo semestre?'))

mediaPrimeiroSemestre = (primeiraNota+segundaNota)/divisor

mediaSegundoSemestre = (terceiraNota+quartaNota)/divisor

mediaDoAno = (mediaPrimeiroSemestre+mediaSegundoSemestre)/divisor

print('A media final do primeiro semestre sera',round(mediaPrimeiroSemestre,1))
print('A media final do segundo semestre sera',round(mediaSegundoSemestre,1))
print('A media final do ano sera',round(mediaDoAno,1))

if mediaPrimeiroSemestre>=7:
    print('No primeiro semestre o aluno ficou com media de',round(mediaPrimeiroSemestre,1),',logo foi Aprovado no primeiro semestre')
else:
    print('No primeiro semestre o aluno ficou com media de',round(mediaPrimeiroSemestre,1),',logo foi Reprovado no primeiro semestre')

if mediaSegundoSemestre>=7:
    print('No segundo semestre o aluno ficou com media de',round(mediaSegundoSemestre,1),',logo foi Aprovado no segundo semestre')
else:
    print('No segundo semestre o aluno ficou com media de',round(mediaSegundoSemestre,1),',logo foi Reprovado no segundo semestre')

if mediaDoAno>=7:
    print('No total o aluno ficou com media de',round(mediaDoAno,1),',logo foi Aprovado no ano letivo')
else:
    print('No total o aluno ficou com media de',round(mediaDoAno,1),',logo foi Reprovado no ano letivo')

