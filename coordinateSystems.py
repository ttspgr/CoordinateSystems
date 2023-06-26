#Parte A
#Criação da variável contadora "i" que controlará o número de iterações por pontos
i = 0
#Criação das variáveis de armazenamento das coordenadas para distância
coordxmaior = 0
coordymaior = 0
coordxmenor = 0
coordymenor = 0
#Criação de variáveis de armazenamento das distâncias
acumula_distmaior = 0
acumula_distmenor = 0
#Criação de variáveis de armazenamento da posição dos pontos em relação aos quadrantes
acumula_q1 = 0
acumula_q2 = 0
acumula_q3 = 0
acumula_q4 = 0
#Criação de variáveis abx e ory a partir do input do usuário no formato "x,y"
#A manipulação de string "split" é usada para automaticamente assignar os valores às variáveis
abx, ory = input('Olá! Por favor digite as coordenadas desejadas na forma "x,y":\n').split(',')
#Conversão de abx e ory em variáveis do tipo "integer" para possibilitar a computação
X = int(abx)
Y = int(ory)
#Definição de pontos a serem informados pelo usuário atribuídos à variável nup.
nup = int(input('Por favor, informe o número de pontos que serão comparados à origem transladada: '))
#Laço while criado para iteração de cada ponto, até o número desejado pelo usuário
#A execução é condicionada pelo contador exibir um valor menor que aquele estabelecido pelo
#usário na variável nup
while i < nup:
#Criação de variáveis xn e yn para assumir os valores de pontos informados pelo usuário
    xn, yn = input('Por favor informe as coordenadas do ponto desejado na forma "(X,Y)": ').split(',')
#transformação das variáveis xn e yn em variáveis do tipo "integer"
    xn = int(xn)
    yn = int(yn)
#Cálculo da distância euclidiana entre o ponto informado e a origem transladada
    dist = ((xn - X)**2 + (yn - Y)**2)**(1/2)
#Código empregado para comparar e armazenar os valores de distância de interesse
    if acumula_distmaior == 0:
#Os valores da 1ª distância são inicialmente atribuídos automaticamente às variáveis, bem como as coordenadas para cada ponto da distância inicial são armazenados
        acumula_distmaior = dist
        acumula_distmenor = dist
        coordxmaior = xn
        coordymaior = yn
        coordxmenor = xn
        coordymenor = yn
#Comparação empregada para armazenar a distância computada e as coordenadas do ponto     #mais distante, caso maior que o valor prévio
    if acumula_distmaior < dist:
        acumula_distmaior = dist
        coordxmaior = xn
        coordymaior = yn
#Comparação similar a anterior, mas para a menor distância e o ponto mais próximo
    if acumula_distmenor > dist:
        acumula_distmenor = dist
        coordxmenor = xn
        coordymenor = yn
#Linhas de comparação para situar o ponto em um dos 4 quadrantes. Ao final da comparação 
#o acumulador correspondente ao quadrante recebe uma unidade
    if xn == X or yn == Y:
        print(f'O ponto ({xn}, {yn}) está sobre o eixo de coordenadas')
    if xn > X:
        if yn > Y:
            print(f'O ponto ({xn},{yn}) está no 1º quadrante.')
            acumula_q1 += 1
        elif yn < Y:
            print(f'O ponto ({xn},{yn}) está no 4º quadrante.')
            acumula_q4 += 1
    elif xn < X:
        if yn > Y:
            print(f'O ponto ({xn},{yn}) está no 2º quadrante.')
            acumula_q2 += 1
        elif yn < Y:
            print(f'O ponto ({xn},{yn}) está no 3º quadrante.')
            acumula_q3 += 1
#Antes do final de execução do código do laço. O contador recebe então uma unidade que #registra a #execução e segue na execução do código
    i += 1
#Comandos de saída fora do laço designados a informar as coordenadas ponto mais distante e mais #próximo e as respectivas distâncias deles até a origem transladada
print(f'Ponto ({coordxmenor},{coordymenor}) é o mais próximo, distância = {acumula_distmenor:.2f}.')
print(f'Ponto ({coordxmaior},{coordymaior}) é o mais distante, distância = {acumula_distmaior:.2f}.')
#Comando de saída final que revela o valor final de pontos armazenado em cada um dos #acumuladores criados para cada quadrante
print(f'Existe(m) {acumula_q1} pontos no 1º quadrante; {acumula_q2} no 2º quadrante; {acumula_q3} no 3º quadrante e {acumula_q4} no 4º quadrante. ')
#Fim da parte A do Projeto

#Parte B
#Criação das variáveis que, a partir de valores de entrada do usuário informam as #coordenadas X e Y da origem em que o robô está posicionado. Note que o modelo de entrada #foi feito por meio de entradas separas
robox = int(input('Digite a coordenada X do ponto de origem A do robô: '))
roboy = int(input('Digite a coordenada Y do ponto de origem A do robô: '))
#Criação e atribuição da variável "tempo", que descreve o tempo de caminhada do robô, e é #necessária para definição do range para o for loop
tempo = int(input('Digite por quanto tempo o robô irá caminhar: '))
#Criação de um "for loop" que inicia no valor 1, para que a lógica no padrão de movimento do #robô siga o padrão desejado. O loop itera sobre os número no intervalo de 1 à variável de #tempo definida +1, visto que o for loop executa iterações até o penúltimo valor, e no caso, #o penúltimo valor equivale ao último instante da caminhada.
for i in range(1,tempo+1,1):
#O padrão encontrado para o movimento do robô diz respeito ao módulo 3 da unidade no #intervalo de 1 ao tempo+1, de modo que o resto igual à 1 sinaliza um movimento vertical
#(soma de uma unidade na coordenada Y original do robô) e os restos 2 e 0 indicam um #movimento horizontal (soma de uma unidade na coordenada X original do robô).
  if i % 3 == 1:
    roboy += 1
  if i % 3 == 2 or i % 3 == 0:
    robox += 1
#Fim do foor loop com a saída das coordenadas da posição final do robô 
print(f'Ao final da caminhada, o robô estará no ponto ({robox},{roboy}) do plano cartesiano')
#Fim da parte B