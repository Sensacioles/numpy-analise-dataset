import numpy as np 
#Construção do dataset
pais = np.zeros(6)
pais = ['Itália','Japão','Alemanha','Brasil','Austrália','Canadá']
codigoPais = np.zeros(6)
codigoPais = [1,2,3,4,5,6]
idh = np.zeros(6)
idh = [0.854,0.884,0.885,0.699,0.939,0.926]
pop = np.zeros(6)
pop = [60.36,126.5,83.02,209.5,24.99,37.59]
print(f'País: {np.array(pais)}\n'
f'Código do país: {np.array(codigoPais)}\n'
f'IDH: {np.array(idh)}\n'
f'População(milhões): {np.array(pop)}\n')

#Processo de Fatiamento
idhOrdenado = np.sort(idh)
popOrdenado = np.sort(pop)
print(f'Top 3 menores IDHs:{idhOrdenado[:3:]}\n' #Fatiamento dos 3 primeiros elementos do vetor de IDH ordenado
f'Top 3 maiores IDHs: {idhOrdenado[3::]}\n' #Fatiamento dos 3 últimos elementos do vetor de IDH ordenado
f'Maior população: {popOrdenado[len(popOrdenado)-1::]}\n') #Fatiamento do último elemento do vetor de população ordenado

#Processo de Vetorização
print(f'Relação País x Código:\n {np.array([pais,codigoPais])}\n' #Vetorização correlacionando País com Código respectivo
f'Relação IDH x População:\n {np.array([idh,pop])}\n' #Vetorização correlacionando IDH com População
f'Dataset:\n {np.array([pais,codigoPais,idh,pop])}\n') #Vetorização do dataset

#Processo de Vetorização com Indexação Booleana
somaIdh = 0
somaPop = 0
for j in range(len(pais)):
    somaIdh += idhOrdenado[j]
    somaPop += popOrdenado[j]
mediaIdh = somaIdh/len(pais)
mediaPop = somaPop/len(pais)
contIdh = 0
contpop = 0
for i in idhOrdenado:
    if i > mediaIdh:
        contIdh += 1
vetIdhAcima = np.zeros(contIdh)
vetIdhAbaixo = np.zeros(len(idhOrdenado)-contIdh)
for p in popOrdenado:
    if p > mediaPop:
        contpop += 1
vetPopAcima = np.zeros(contpop)
contvet = 0
for ac in idhOrdenado:
    if ac > mediaIdh:
        vetIdhAcima[contvet] = ac
        contvet += 1
contvet = 0
for ab in idhOrdenado:
    if ab < mediaIdh:
        vetIdhAbaixo[contvet] = ab
        contvet += 1
contvet = 0
for pp in popOrdenado:
    if pp > mediaPop:
        vetPopAcima[contvet] = pp
        contvet += 1
print(f'IDHs acima da média: {vetIdhAcima}\n' #Vetorização com indexação booleana de IDHs acima da média
f'IDHs abaixo da média: {vetIdhAbaixo}\n' #Vetorização com indexação de IDHs abaixo da média
f'Populações acima da média: {vetPopAcima}') #Vetorização com indexação de populações acima da média