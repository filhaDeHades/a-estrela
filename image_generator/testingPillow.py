from PIL import Image, ImageColor, ImageFont, ImageDraw

#Constants:
TIPOS = ['modo', 'tam','color', 'title','save']

#Configurations inputs:
numarq_inp = 0
files_inp = []
folders_inp = []
grafics_inp = []

def takeInput1(name):
    dicti = {}
    arq = open(name)
    linhas = arq.readlines()
    param = []
    base = ''
    for i in range(len(linhas)):
        linha = linhas[i].strip('\n')
        
        if i <= len(TIPOS) - 1:
            if TIPOS[i] == 'modo':
                dicti['modo'] = linha.upper()

            elif TIPOS[i] == 'tam':
                linha = linha.split()
                dicti['tam'] = (int(linha[0]), int(linha[1]))

            elif TIPOS[i] == 'color':
                cor = ImageColor.getrgb(f'#{linha}')
                dicti['color'] = cor
            elif TIPOS[i] == 'title':
                dicti['title'] = linha
        if i == 4:
            base = linha
        if i > 4:
            param.append(linha)
            if i == len(linhas)-1:
                dicti['save'] = (base, param)
    arq.close()
    return dicti


def takeInput2(name):
    global folders_inp
    global numarq_inp
    global files_inp
    global grafics_inp
    arq = open(name)
    linhas = arq.readlines()
    for i in range(len(linhas)):
        if i == 0:
            folders_inp = linhas[i].split()
            numarq_inp = len(folders_inp)+1
        if i == 1:
            files_inp = linhas[i].split()
        if i == 2:
            grafics_inp = linhas[i].split()


def recuperandoArquetipos(inicio, arquivo):
    imagens = []

    for i in range(numarq_inp):
        if i != numarq_inp-1:
            arquivo = f'{i+1}.png'
            if i == 2:
                arquivo = f'{i+1}-1.png'
            image2 = Image.open(inicio+f'{files_inp[0]}'+arquivo)
            arquivo = '.png'
        else:
            image2 = Image.open(inicio+f'{files_inp[1]}'+arquivo)
        imagens.append(image2)
    return imagens


def recuperandoGraficos(inicio, arquivo):
    # recebera pasta 'modeloX' do pai

    graficos = []

    for nomeGraf in grafics_inp:
        graficoString = inicio + nomeGraf + arquivo
        grafico = Image.open(graficoString)
        graficos.append(grafico)
    
    return graficos


def posicionandoArquetipos(imagem, arquetipos, arq=''):
    larg = 50
    alt = 300
    for i in range(len(arquetipos)):
        
        arq = arquetipos[i]
        imagem.paste(arq, (larg, alt))
        alt += 480 + 50


def posicionandoGraficos(imagem, graficos,pasta=0, arq=''):
    larg = 580
    alt = 300 + (480+50)*pasta

    for i in range(len(graficos)):
        grafic = graficos[i]
        imagem.paste(grafic,(larg,alt))
        larg += 640 + 50
    imagem.save(arq)


def resgatandoParametros(string):
    valor1 = 0
    valor2 = 0
    params = string.split('(')
    del(params[0])
    for i in range(len(params)):
        params[i] = params[i].split(')')[0]
        valor1 = int(params[i][0]) * 1.0
        valor2 = int(params[i][2]) * 0.1
        params[i] = valor1 + valor2
        
    return (params[0], params[1])


def escrevendo(imagem, param, arq):
    fonte =ImageFont.truetype('arial.ttf', 200)
    texto = 'Resultados 2000 timesteps - ' + param
    imagemComTexto = ImageDraw.Draw(imagem)
    imagemComTexto.text((1060, 50), texto, ('black'), font=fonte)
    imagem.save(arq)
        

def setsFundo(modo, tam=(10, 10),cor=ImageColor.getrgb("#555"),pastaBase=('(0-5)(0-5)(0-5)(0-5)','(0-1)(0-1)')):
    image1 = Image.new(modo,tam,cor)
    inicio1 = 'imagens\\'

    parametros = resgatandoParametros(pastaBase[1])
    #print(parametros)
    
    inicio2 = f'{inicio1}{pastaBase[0]}\\{pastaBase[1]}\\'
    arquivo = '.png'
    
    nomeArq = f'imagens/slides/Resultados-({int(parametros[0]//10)}-{int(parametros[0]*10)})({int(parametros[1]//10)}-{int(parametros[1]*10)}).png'

    imagens = recuperandoArquetipos(inicio1, arquivo)
    escrevendo(image1, f'Alfa: {parametros[0]:.1f} Beta: {parametros[1]:.1f}', nomeArq)
    posicionandoArquetipos(image1, imagens, nomeArq)
    cont=0
    for i in range(6):
        nomepasta = inicio2 + f'modelo{cont+1}\\'
        graficos = recuperandoGraficos(nomepasta,arquivo)
        posicionandoGraficos(image1, graficos, cont, nomeArq)
        cont += 1


inputs = takeInput1('input.txt')
takeInput2('inputConfig.txt')


for param in inputs['save'][1]:
    pastaBase = (inputs['save'][0], param)
    setsFundo(inputs['modo'], inputs['tam'],inputs['color'],pastaBase)
