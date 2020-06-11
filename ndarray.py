import numpy as np
#1.B) Distribuição Uniforme PARES
quant1 = 10
senha = np.zeros(quant1,dtype=int)
senha = np.random.randint(100,1000,quant1)
par = senha % 2 == 0
print(f'Senhas: {senha}\n'
f'Senhas pares: {par}\n'
f'Quantidade absoluta: {(senha%2==0).sum()}\n'
f'Quantidade relativa: {(senha%2==0).sum()/quant1*100:.1f}\n')

#2.E) Média da soma dos termos múltiplos de 2 e 5
quant2 = 100
termos = np.zeros(quant2,dtype=int)
termos = np.random.randint(100,1000,quant2)
somaMult = 0
quantMult = 0
for m in range(len(termos)):
    if termos[m] % 2 == 0 and termos[m] % 5 == 0:
        quantMult += 1
        somaMult += m
print(f'Média da soma dos múltiplos: {somaMult/quantMult:.1f}\n')

#3.E) Exibir termos e seus índices > nUser:
termoIndice = np.zeros(100,dtype=int)
termoIndice = np.random.normal(100,10,100)
nUser = int(input('Insira um número: '))
for ind in range(len(termoIndice)):
    if termoIndice[ind] > nUser:
        print(f'Termos maiores que {nUser} e seus índices: {termoIndice[ind]:.2f} [{ind}]')

#4.B) Lista Atletas(Matrícula e Tempo) < tMédio,
#matrícula do vencedor e do perdedor,
#diferença entre os dois:

matriculaGaroto = np.zeros(5000,dtype=int)
matriculaGaroto = np.random.randint(0,5001,5000)
tempo = np.zeros(5000,dtype=float)
tempo = np.random.normal(250,10,5000)
vencedorTemp = tempo.min()
perdedorTemp = tempo.max()
somaTempo = 0
for te in tempo:
    somaTempo += te
for k in range(len(tempo)):
    if tempo[k] < somaTempo/len(tempo):
        if tempo[k] > 0:
            print(f'Matrícula e tempo: {matriculaGaroto[k]} {tempo[k]:.2f} min')
print(f'\nTempo médio: {somaTempo/(len(tempo)):.2f} min')
for p in range(len(tempo)):
    if tempo[p] == perdedorTemp:
        print(f'Perdedor: {matriculaGaroto[p]} {perdedorTemp:.2f} min')
for v in range(len(tempo)):
    if tempo[v] == vencedorTemp:
        print(f'Vencedor: {matriculaGaroto[v]} {vencedorTemp:.2f} min')
print(f'Diferença de tempo entre o perdedor e o vencedor: {perdedorTemp-vencedorTemp:.2f} min\n')

#5.E) Lista de matrículas com média semestral >= média da turma:

matriculaAluno = np.zeros(50,dtype=int)
matriculaAluno = np.random.randint(0,51,50)
notaPrimeiro = np.zeros(50,dtype=float) 
notaPrimeiro = np.random.normal(44,2,50) 
notaSegundo = np.zeros(50,dtype=float) 
notaSegundo = np.random.normal(44,2,50) 
somaNotaPrimeiro = 0
somaNotaSegundo = 0
somaNotaFinal = 0
for nn1 in range(len(notaPrimeiro)):
    somaNotaPrimeiro += notaPrimeiro[nn1]
for nn2 in range(len(notaSegundo)):
    somaNotaSegundo += notaSegundo[nn2]
somaNotaFinal = somaNotaPrimeiro + somaNotaSegundo
médiaTurma = somaNotaFinal/(len(matriculaAluno))
notaFinal = np.zeros(50,dtype=float)
for nf1 in range(len(notaPrimeiro)):
    notaFinal[nf1] += notaPrimeiro[nf1]
for nf2 in range(len(notaSegundo)):
    notaFinal[nf2] += notaSegundo[nf2]
contAcima = 0
for ms in range(len(notaFinal)):
    if notaFinal[ms] >= médiaTurma:
    #if (notaFinal[ms]/2) >= médiaTurma:
        contAcima += 1
        print(f'Matrículas com média semestral >= média da turma: {matriculaAluno[ms]} Nota: {notaFinal[ms]}')
print(f'Alunos acima da média: {contAcima}')
print(f'Média da turma: {médiaTurma:.2f}\n')
#Nesse caso, a média semestral individual foi considerada a nota final(nota do semestre1 + nota do semestre2). Se
#fosse usada a fórmula de média aritmética (assim como no código comentado), nenhuma matrícula seria printada pois 
#a média da turma seria muito alta pra qualquer média individual ser validada.

#6.A) Total do carrinho:
quantMercadoria = np.zeros(100,dtype=int)
quantMercadoria = np.random.randint(1,5,100)
preçoMercadoria = np.zeros(100,dtype=float)
preçoMercadoria = np.random.normal(40,0.4,100)
for pt in range(len(quantMercadoria)):
    totalCarrinho = quantMercadoria[pt] * preçoMercadoria[pt]
print(f'Total a ser pago: R$ {totalCarrinho:.2f}\n')

#7.B) Valor médio em cada grupo:
bronze = np.zeros(100,dtype=float)
bronze = np.random.normal(44,2,100)
prata = np.zeros(100,dtype=float)
prata = np.random.normal(249,3,100)
ouro = np.zeros(50,dtype=float)
ouro = np.random.normal(499,4,50)
diamante = np.zeros(25,dtype=float)
diamante = np.random.normal(999,5,25)
somaBr = 0
somaPr = 0
somaOu = 0
somaDi = 0
for br in range(len(bronze)):
    somaBr += bronze[br]
for pr in range(len(prata)):
    somaPr += prata[pr]
for ou in range(len(ouro)):
    somaOu += ouro[ou]
for di in range(len(diamante)):
    somaDi += diamante[di]
print(f'Média Bronze: R$ {somaBr/(len(bronze)):.2f}\n'
f'Média Prata: R$ {somaPr/(len(prata)):.2f}\n'
f'Média Ouro: R$ {somaOu/(len(ouro)):.2f}\n'
f'Média Diamante: R$ {somaDi/(len(diamante)):.2f}')