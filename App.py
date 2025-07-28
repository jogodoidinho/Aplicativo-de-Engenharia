import tkinter as tk
from tkinter import ttk
dados = {}

root = tk.Tk()
def on_button_click():
        label.config(text="Botão clicado!")

        
root.title('Lucas Conserva Alves')
root.configure(background ='#ffffff')
root.geometry('700x500')
root.resizable(True,True)
label = tk.Label(root,text='Escolha Uma Opção',font=('Arial Bold',20))
label.grid(column=0,row=0)

def taxadeacidente():

    taxadeacidente = tk.Toplevel()
    taxadeacidente.title('Taxa de Motorização')
    taxadeacidente.configure(background ='#dee0e3')
    taxadeacidente.geometry('700x500')
    taxadeacidente.resizable(True,True)

    def resposta():
        w = float(ibge_veiculos.get())
        x = float(ibge_pessoas.get())
        y = float(Estatistica_veiculos.get())
        z = float(Estatistica_pessoas.get())
        resultadoIBGE.configure(text=f'{w/x}')
        resultatoestatistica.configure(text=f'{y/z}')
        erroresposta.configure(text=f'{(y/z) - (w/x)}')
        dados['monitoracao'] = y/z

    #informaçoes do ibge
    texto = tk.Label(taxadeacidente,text='Numero de Veiculos /IBGE')
    texto.grid(row=1, column=0, padx=10, pady=5,sticky= 'nsew')
    
    ibge_veiculos = tk.Entry(taxadeacidente,width=20)
    ibge_veiculos.grid(row=2, column=0, padx=10, pady=5,sticky= 'nsew')

    texto2 = tk.Label(taxadeacidente,text='População /IBGE')
    texto2.grid(row=1, column=1, padx=10, pady=5,sticky= 'nsew')
    
    ibge_pessoas = tk.Entry(taxadeacidente,width=20)
    ibge_pessoas.grid(row=2, column=1, padx=10, pady=5,sticky= 'nsew')

    #agr o da cidade

    texto3 = tk.Label(taxadeacidente,text='Numero de Veiculos /Estatistica')
    texto3.grid(row=3, column=0, padx=10, pady=5,sticky= 'nsew')
    
    Estatistica_veiculos = tk.Entry(taxadeacidente,width=20)
    Estatistica_veiculos.grid(row=4, column=0, padx=10, pady=5,sticky= 'nsew')

    texto4 = tk.Label(taxadeacidente,text='População /Estatistica')
    texto4.grid(row=3, column=1, padx=10, pady=5,sticky= 'nsew')
    
    Estatistica_pessoas = tk.Entry(taxadeacidente,width=20)
    Estatistica_pessoas.grid(row=4, column=1, padx=10, pady=5,sticky= 'nsew')

    #taxadeacidente pra enviar

    b = tk.Button(taxadeacidente,text='Enviar',command=resposta)
    b.grid(row=5, column=0, padx=10, pady=5,sticky= 'nsew')
    
    #acidentes
    acidentesIBGE = tk.Label(taxadeacidente,text=f'Taxa de Acidente/IBGE')
    acidentesIBGE.grid(row=1, column=3, padx=10, pady=5,sticky= 'nsew')
    resultadoIBGE = tk.Label(taxadeacidente,text=f'',background='#8c8c8c')
    resultadoIBGE.grid(row=2, column=3, padx=10, pady=5,sticky= 'nsew')

    acidenteestatistica = tk.Label(taxadeacidente,text=f'Taxa de Acidente/Estatisticas')
    acidenteestatistica.grid(row=3, column=3, padx=10, pady=5,sticky= 'nsew')
    resultatoestatistica = tk.Label(taxadeacidente,text=f'',background='#8c8c8c')
    resultatoestatistica.grid(row=4, column=3, padx=10, pady=5,sticky= 'nsew')

    #Erro
    erro = tk.Label(taxadeacidente,text=f'Taxa de Erro')
    erro.grid(row=1, column=4, padx=10, pady=5,sticky= 'nsew')
    erroresposta = tk.Label(taxadeacidente,text=f'',background='#8c8c8c')
    erroresposta.grid(row=2, column=4, padx=10, pady=5,sticky= 'nsew')
    
    

    taxadeacidente.mainloop()

def uso_de_energia():

    def calculo():
        fossil = float(resposta_texto.get())
        limpa = float(resposta_texto2.get())
        calc = limpa/(fossil + limpa)
        resposta.configure(text=f'{calc}')
        dados['uso de energia'] = calc
        
    #janela
    uso_de_energia = tk.Toplevel()
    uso_de_energia.title('Taxa de Motorização')
    uso_de_energia.configure(background ='#dee0e3')
    uso_de_energia.geometry('700x500')
    uso_de_energia.resizable(True,True)

    #textos
    texto = tk.Label(uso_de_energia,text='Frota Fossil')
    texto.grid(row=1, column=0, padx=10, pady=5,sticky= 'nsew')
    resposta_texto = tk.Entry(uso_de_energia,width=20)
    resposta_texto.grid(row=2, column=0, padx=10, pady=5,sticky= 'nsew')
    
    texto2 = tk.Label(uso_de_energia,text='Frota Limpa')
    texto2.grid(row=1, column=1, padx=10, pady=5,sticky= 'nsew')
    resposta_texto2 = tk.Entry(uso_de_energia,width=20)
    resposta_texto2.grid(row=2, column=1, padx=10, pady=5,sticky= 'nsew')

    texto3 = tk.Label(uso_de_energia,text='Frota Limpa')
    texto3.grid(row=1, column=2, padx=10, pady=5,sticky= 'nsew')

    resposta = tk.Label(uso_de_energia,text='')
    resposta.grid(row=2, column=2, padx=10, pady=5,sticky= 'nsew')
    #botao
    botao = tk.Button(uso_de_energia,text='Enviar',command= calculo)
    botao.grid(row=3, column=0, padx=10, pady=5,sticky= 'nsew')

def transporte_compartil():
   
    #janela
    uso_de_energia = tk.Toplevel()
    uso_de_energia.title('transporte_compartilhado')
    uso_de_energia.configure(background ='#dee0e3')
    uso_de_energia.geometry('700x500')
    uso_de_energia.resizable(True,True)

    #textos
    texto = tk.Label(uso_de_energia,text='Na cidade existe alguma das modalidades ?',font=("Arial Bold", 10) )
    texto.grid(row=0, column=1, padx=10, pady=5,sticky= 'nsew') 

    texto2 = tk.Label(uso_de_energia,text='Total',font=("Arial Bold", 10) )
    texto2.grid(row=1, column=1, padx=10, pady=5,sticky= 'nsew')

    total = tk.Label(uso_de_energia,text='',font=("Arial Bold", 10))
    total.grid(row=4, column=1, padx=10, pady=5,sticky= 'nsew')
    #caixas
    respostacarona = tk.IntVar()
    respostacarro = tk.IntVar()
    respostabicicleta = tk.IntVar()
    
    #caixas
    perguntacarona = tk.Checkbutton(uso_de_energia, text="Carona Solidaria", variable=respostacarona)
    perguntacarro = tk.Checkbutton(uso_de_energia, text="Aluguel de carro", variable=respostacarro)
    perguntabicicleta = tk.Checkbutton(uso_de_energia, text="Aluguel de bicicleta", variable=respostabicicleta)
    perguntacarona.grid(row=1, column=0, padx=10, pady=5,sticky= 'nsew')
    perguntacarro.grid(row=1, column=1, padx=10, pady=5,sticky= 'nsew')
    perguntabicicleta.grid(row=1, column=2, padx=10, pady=5,sticky= 'nsew')
    
    
    def enviar():
        try:
            x = 0
            y = 0
            z = 0
            if respostacarona.get() == 1:
                x = 0.3
            if respostacarro.get() == 1:
                y = 0.3
            if respostabicicleta.get() == 1:
                z = 0.3
        except:
            pass
        total.configure(text=f'{(x+y+z)}')
        dados['transporte'] = (x + y + z)
    #botao
    botao = tk.Button(uso_de_energia,text='Enviar',command=enviar)
    botao.grid(row=2, column=1, padx=10, pady=5,sticky= 'nsew')

def ciclovias():
    #janela
    ciclovias = tk.Toplevel()
    ciclovias.title('ciclovias')
    ciclovias.configure(background ='#dee0e3')
    ciclovias.geometry('700x500')
    ciclovias.resizable(True,True)

    #textos
    Extensão_Total = tk.Label(ciclovias,text='Extensão Total',font=("Arial Bold", 10) )
    Ciclovia_Exclusiva = tk.Label(ciclovias,text='Ciclovia Exclusiva',font=("Arial Bold", 10) )
    Ciclovia = tk.Label(ciclovias,text='Ciclovia ',font=("Arial Bold", 10) )
    Ciclovia_Compartilhada = tk.Label(ciclovias,text='Ciclovia Compartilhada',font=("Arial Bold", 10) )
    Extensão_Ciclovia = tk.Label(ciclovias,text='Extensao Da Ciclovia',font=("Arial Bold", 10) )
    taxa = tk.Label(ciclovias,text='Taxa da Ciclovia',font=("Arial Bold", 10) )
    r1 = tk.Label(ciclovias,text='',font=("Arial Bold", 10) )
    r2 = tk.Label(ciclovias,text='',font=("Arial Bold", 10) )

    Extensão_Total.grid(row=0, column=1, padx=10, pady=5,sticky= 'nsew')
    Ciclovia_Exclusiva.grid(row=1, column=1, padx=10, pady=5,sticky= 'nsew')
    Ciclovia.grid(row=2, column=1, padx=10, pady=5,sticky= 'nsew')
    Ciclovia_Compartilhada.grid(row=3, column=1, padx=10, pady=5,sticky= 'nsew')
    Extensão_Ciclovia.grid(row=0, column=3, padx=10, pady=5,sticky= 'nsew')
    taxa.grid(row=0, column=4, padx=10, pady=5,sticky= 'nsew')
    r1.grid(row=1, column=3, padx=10, pady=5,sticky= 'nsew')
    r2.grid(row=1, column=4, padx=10, pady=5,sticky= 'nsew')

    #inputs

    total = tk.Entry(ciclovias,width=20)
    exclusiva = tk.Entry(ciclovias,width=20)
    nsei = tk.Entry(ciclovias,width=20)
    compartilhada = tk.Entry(ciclovias,width=20)

    total.grid(row=0, column=2, padx=10, pady=5,sticky= 'nsew')
    exclusiva.grid(row=1, column=2, padx=10, pady=5,sticky= 'nsew')
    nsei.grid(row=2, column=2, padx=10, pady=5,sticky= 'nsew')
    compartilhada.grid(row=3, column=2, padx=10, pady=5,sticky= 'nsew')

    #calculo
    def calculo():
        x = float(exclusiva.get())
        y = float(nsei.get())
        z = float(compartilhada.get())
        extensaosla = float(total.get())
        r1.configure(text=f'{(z+y+x)}')
        r2.configure(text=f'{(z+y+x)/extensaosla}')
        dados['ciclovias'] = (z+y+x)/extensaosla 
    #botao
    enviar = tk.Button(ciclovias,text='Enviar',command= calculo)
    enviar.grid(row=4, column=1, padx=10, pady=5,sticky= 'nsew')

def terminais():
    #janela
    terminais = tk.Toplevel()
    terminais.title('Termianais Intermodais')
    terminais.configure(background ='#dee0e3')
    terminais.geometry('700x500')
    terminais.resizable(True,True)
    #texto
    texto = tk.Label(terminais,text='Nº de Terminais')
    texto.grid(row=0, column=0, padx=10, pady=5,sticky= 'nsew')

    texto2 = tk.Label(terminais,text='Nº de Terminais')
    texto2.grid(row=0, column=1, padx=10, pady=5,sticky= 'nsew')

    texto3 = tk.Label(terminais,text='Taxa')
    texto3.grid(row=0, column=2, padx=10, pady=5,sticky= 'nsew')

    texto4 = tk.Label(terminais,text='')
    texto4.grid(row=1, column=2, padx=10, pady=5,sticky= 'nsew')

    #Inputs

    resposta_texto = tk.Entry(terminais,width=20)
    resposta_texto.grid(row=1, column=0, padx=10, pady=5,sticky= 'nsew')
    
    resposta_texto2 = tk.Entry(terminais,width=20)
    resposta_texto2.grid(row=1, column=1, padx=10, pady=5,sticky= 'nsew')

    #calculo
    def calculo():
        terminal1 = float(resposta_texto.get())
        terminal2 = float(resposta_texto2.get())
        calc = terminal2/terminal1
        texto4.configure(text=f'{calc}')
        dados['terminais'] = calc

    #botao
    botao = tk.Button(terminais,text='Enviar',command= calculo)
    botao.grid(row=2, column=0, padx=10, pady=5,sticky= 'nsew')
def bilheteria():
    #janela
    bilheteria = tk.Toplevel()
    bilheteria.title('Sistema Integrado de Bilheteria')
    bilheteria.configure(background ='#dee0e3')
    bilheteria.geometry('700x500')
    bilheteria.resizable(True,True)

    #textos
    texto = tk.Label(bilheteria,text='Na cidade existe alguma das modalidades ?',font=("Arial Bold", 10) )
    texto.grid(row=0, column=0, padx=10, pady=5,sticky= 'nsew') 

    texto2 = tk.Label(bilheteria,text='Total',font=("Arial Bold", 10) )
    texto2.grid(row=3, column=0, padx=10, pady=5,sticky= 'nsew')

    total = tk.Label(bilheteria,text='',font=("Arial Bold", 10))
    total.grid(row=4, column=0, padx=10, pady=5,sticky= 'nsew')

    
    #caixas
    fisico = tk.IntVar()
    temporal = tk.IntVar()
    

    #caixas
    perguntafisico = tk.Checkbutton(bilheteria, text="Sistema de integração fisico", variable=fisico)
    perguntatemporal = tk.Checkbutton(bilheteria, text="Sistema de integração temporal", variable=temporal)
    
    perguntafisico.grid(row=1, column=0, padx=10, pady=5,sticky= 'nsew')
    perguntatemporal.grid(row=1, column=1, padx=10, pady=5,sticky= 'nsew')

    #funcao
    def enviar():
        try:
            x = 0
            y = 0
            if fisico.get() == 1:
                x = 0.5
            if temporal.get() == 1:
                y = 0.5
        except:
            pass
        total.configure(text=f'{x+y}')
        dados['bilheteria'] = (x + y)

    #botao
    botao = tk.Button(bilheteria,text='Enviar',command=enviar)
    botao.grid(row=2, column=0, padx=10, pady=5,sticky= 'nsew')

def informação():
    #janela
    informação = tk.Toplevel()
    informação.title('Sistema de Informação')
    informação.configure(background ='#dee0e3')
    informação.geometry('700x500')
    informação.resizable(True,True)

    #texto
    texto = tk.Label(informação,text='Nº de canais ')
    texto.grid(row=0, column=0, padx=10, pady=5,sticky= 'nsew')

    texto2 = tk.Label(informação,text='Nº de canais utilizados')
    texto2.grid(row=0, column=1, padx=10, pady=5,sticky= 'nsew')

    texto3 = tk.Label(informação,text='Total')
    texto3.grid(row=0, column=2, padx=10, pady=5,sticky= 'nsew')

    texto4 = tk.Label(informação,text='')
    texto4.grid(row=1, column=2, padx=10, pady=5,sticky= 'nsew')

    #Inputs

    resposta_texto = tk.Entry(informação,width=20)
    resposta_texto.grid(row=1, column=0, padx=10, pady=5,sticky= 'nsew')
    
    resposta_texto2 = tk.Entry(informação,width=20)
    resposta_texto2.grid(row=1, column=1, padx=10, pady=5,sticky= 'nsew')

    #calculo
    def calculo():
        terminal1 = float(resposta_texto.get())
        terminal2 = float(resposta_texto2.get())
        calc = terminal1/terminal2
        texto4.configure(text=f'{calc}')
        dados['informação'] = calc


    #botao
    botao = tk.Button(informação,text='Enviar',command= calculo)
    botao.grid(row=2, column=0, padx=10, pady=5,sticky= 'nsew')
    
def viagem():
    #janela
    viagem = tk.Toplevel()
    viagem.title('Tempo de Viagem do Transporte P')
    viagem.configure(background ='#dee0e3')
    viagem.geometry('700x500')
    viagem.resizable(True,True)
    
    #textos
    texto = tk.Label(viagem,text='Dia:')
    texto.grid(row=0, column=0, padx=10, pady=5,sticky= 'nsew')

    texto2 = tk.Label(viagem,text='Somatoria')
    texto2.grid(row=0, column=3, padx=10, pady=5,sticky= 'nsew')

    texto3 = tk.Label(viagem,text='Média')
    texto3.grid(row=0, column=4, padx=10, pady=5,sticky= 'nsew')

    resposta_somatoria = tk.Label(viagem,text='')
    resposta_somatoria.grid(row=1, column=3, padx=10, pady=5,sticky= 'nsew')

    resposta_media = tk.Label(viagem,text='')
    resposta_media.grid(row=1, column=4, padx=10, pady=5,sticky= 'nsew')

    #dias
    dia = tk.Label(viagem,text=f'Dia 1')
    dia.grid(row=1, column=0, padx=10, pady=5,sticky= 'nsew')

    dia2 = tk.Label(viagem,text=f'Dia 2')
    dia2.grid(row=2, column=0, padx=10, pady=5,sticky= 'nsew')

    dia3 = tk.Label(viagem,text=f'Dia 3')
    dia3.grid(row=3, column=0, padx=10, pady=5,sticky= 'nsew')

    dia4 = tk.Label(viagem,text=f'Dia 4')
    dia4.grid(row=4, column=0, padx=10, pady=5,sticky= 'nsew')

    dia5 = tk.Label(viagem,text=f'Dia 5')
    dia5.grid(row=5, column=0, padx=10, pady=5,sticky= 'nsew')

    dia6 = tk.Label(viagem,text=f'Dia 6')
    dia6.grid(row=6, column=0, padx=10, pady=5,sticky= 'nsew')

    dia7 = tk.Label(viagem,text=f'Dia 7')
    dia7.grid(row=7, column=0, padx=10, pady=5,sticky= 'nsew')

    dia8 = tk.Label(viagem,text=f'Dia 8')
    dia8.grid(row=8, column=0, padx=10, pady=5,sticky= 'nsew')

    dia9 = tk.Label(viagem,text=f'Dia 9')
    dia9.grid(row=9, column=0, padx=10, pady=5,sticky= 'nsew')

    dia10 = tk.Label(viagem,text=f'Dia 10')
    dia10.grid(row=10, column=0, padx=10, pady=5,sticky= 'nsew')

    dia11 = tk.Label(viagem,text=f'Dia 11')
    dia11.grid(row=11, column=0, padx=10, pady=5,sticky= 'nsew')

    dia12 = tk.Label(viagem,text=f'Dia 12')
    dia12.grid(row=12, column=0, padx=10, pady=5,sticky= 'nsew')

    dia13 = tk.Label(viagem,text=f'Dia 13')
    dia13.grid(row=13, column=0, padx=10, pady=5,sticky= 'nsew')

    dia14 = tk.Label(viagem,text=f'Dia 14')
    dia14.grid(row=14, column=0, padx=10, pady=5,sticky= 'nsew')
    
    dia15 = tk.Label(viagem,text=f'Dia 15')
    dia15.grid(row=15, column=0, padx=10, pady=5,sticky= 'nsew')

    #inputs
    dia = tk.Entry(viagem,text=f'Dia 1')
    dia.grid(row=1, column=1, padx=10, pady=5,sticky= 'nsew')

    dia2 = tk.Entry(viagem,text=f'Dia 2')
    dia2.grid(row=2, column=1, padx=10, pady=5,sticky= 'nsew')

    dia3 = tk.Entry(viagem,text=f'Dia 3')
    dia3.grid(row=3, column=1, padx=10, pady=5,sticky= 'nsew')

    dia4 = tk.Entry(viagem,text=f'Dia 4')
    dia4.grid(row=4, column=1, padx=10, pady=5,sticky= 'nsew')

    dia5 = tk.Entry(viagem,text=f'Dia 5')
    dia5.grid(row=5, column=1, padx=10, pady=5,sticky= 'nsew')

    dia6 = tk.Entry(viagem,text=f'Dia 6')
    dia6.grid(row=6, column=1, padx=10, pady=5,sticky= 'nsew')

    dia7 = tk.Entry(viagem,text=f'Dia 7')
    dia7.grid(row=7, column=1, padx=10, pady=5,sticky= 'nsew')

    dia8 = tk.Entry(viagem,text=f'Dia 8')
    dia8.grid(row=8, column=1, padx=10, pady=5,sticky= 'nsew')

    dia9 = tk.Entry(viagem,text=f'Dia 9')
    dia9.grid(row=9, column=1, padx=10, pady=5,sticky= 'nsew')

    dia10 = tk.Entry(viagem,text=f'Dia 10')
    dia10.grid(row=10, column=1, padx=10, pady=5,sticky= 'nsew')

    dia11 = tk.Entry(viagem,text=f'Dia 11')
    dia11.grid(row=11, column=1, padx=10, pady=5,sticky= 'nsew')

    dia12 = tk.Entry(viagem,text=f'Dia 12')
    dia12.grid(row=12, column=1, padx=10, pady=5,sticky= 'nsew')

    dia13 = tk.Entry(viagem,text=f'Dia 13')
    dia13.grid(row=13, column=1, padx=10, pady=5,sticky= 'nsew')

    dia14 = tk.Entry(viagem,text=f'Dia 14')
    dia14.grid(row=14, column=1, padx=10, pady=5,sticky= 'nsew')
    
    dia15 = tk.Entry(viagem,text=f'Dia 15')
    dia15.grid(row=15, column=1, padx=10, pady=5,sticky= 'nsew')

    #def
    def calculo():
        lista = [float(dia.get()),
                 float(dia2.get()),
                 float(dia3.get()),
                 float(dia4.get()),
                 float(dia5.get()),
                 float(dia6.get()),
                 float(dia7.get()),
                 float(dia8.get()),
                 float(dia9.get()),
                 float(dia10.get()),
                 float(dia11.get()),
                 float(dia12.get()),
                 float(dia13.get()),
                 float(dia14.get()),
                 float(dia15.get())
                 ]
        resposta_somatoria.configure(text=f'{sum(lista)}')
        resposta_media.configure(text=f'{sum(lista)/15}')
        dados['viagem'] = sum(lista)/15
    #botao
    botao = tk.Button(viagem,text='Enviar',command= calculo)
    botao.grid(row=1, column=2, padx=10, pady=5,sticky= 'nsew')

def mobilidade():
    #janela
    mobilidade = tk.Toplevel()
    mobilidade.title('Politica de Mobilidade Urbana')
    mobilidade.configure(background ='#dee0e3')
    mobilidade.geometry('700x500')
    mobilidade.resizable(True,True)

    #texto
    texto = tk.Label(mobilidade,text='Calculo',font=("Arial Bold", 10) )
    texto.grid(row=0, column=0, padx=10, pady=5,sticky= 'nsew') 

    texto2 = tk.Label(mobilidade,text='Total',font=("Arial Bold", 10) )
    texto2.grid(row=3, column=0, padx=10, pady=5,sticky= 'nsew')

    total = tk.Label(mobilidade,text='',font=("Arial Bold", 10))
    total.grid(row=4, column=0, padx=10, pady=5,sticky= 'nsew')

    #caixas
    fisico = tk.IntVar()
    temporal = tk.IntVar()
    

    #caixas
    perguntafisico = tk.Checkbutton(mobilidade, text="A cidade possui um plano de mobilidade urbana?", variable=fisico)
    perguntatemporal = tk.Checkbutton(mobilidade, text="Esse plano está atualizado para o atual cenario do centro urbano?", variable=temporal)
    
    perguntafisico.grid(row=1, column=0, padx=10, pady=5,sticky= 'nsew')
    perguntatemporal.grid(row=1, column=1, padx=10, pady=5,sticky= 'nsew')

    #funcao
    def enviar():
        try:
            x = 0
            y = 0
            if fisico.get() == 1:
                x = 0.5
            if temporal.get() == 1:
                y = 0.5
        except:
            pass
        total.configure(text=f'{x+y}')
        dados['mobilidade'] = x + y
    #botao
    botao = tk.Button(mobilidade,text='Enviar',command=enviar)
    botao.grid(row=2, column=0, padx=10, pady=5,sticky= 'nsew')

def distribuicao():
    #janela
    distribuicao = tk.Toplevel()
    distribuicao.title('Acidentes de Transito')
    distribuicao.configure(background ='#dee0e3')
    distribuicao.geometry('700x500')
    distribuicao.resizable(True,True)

    #textos
    texto = tk.Label(distribuicao,text='Nº de Centros')
    texto.grid(row=1, column=0, padx=10, pady=5,sticky= 'nsew')
    resposta_texto = tk.Entry(distribuicao,width=20)
    resposta_texto.grid(row=2, column=0, padx=10, pady=5,sticky= 'nsew')
    
    texto2 = tk.Label(distribuicao,text='População')
    texto2.grid(row=1, column=1, padx=10, pady=5,sticky= 'nsew')
    resposta_texto2 = tk.Entry(distribuicao,width=20)
    resposta_texto2.grid(row=2, column=1, padx=10, pady=5,sticky= 'nsew')

    texto3 = tk.Label(distribuicao,text='Taxa')
    texto3.grid(row=1, column=2, padx=10, pady=5,sticky= 'nsew')

    resposta = tk.Label(distribuicao,text='')
    resposta.grid(row=2, column=2, padx=10, pady=5,sticky= 'nsew')

    #def
    def calculo():
        x = float(resposta_texto.get())
        y = float(resposta_texto2.get())
        resposta.configure(text=f'{x/y}')
        dados['distribuicao'] = x/y
    #botao
    botao = tk.Button(distribuicao,text='Enviar',command= calculo)
    botao.grid(row=3, column=0, padx=10, pady=5,sticky= 'nsew')

def acidente():
    #janela
    acidente = tk.Toplevel()
    acidente.title('Centros Logisticos de Distribução')
    acidente.configure(background ='#dee0e3')
    acidente.geometry('700x500')
    acidente.resizable(True,True)

    #textos
    texto = tk.Label(acidente,text='Nº de Acidentes Fatais')
    texto.grid(row=1, column=0, padx=10, pady=5,sticky= 'nsew')
    resposta_texto = tk.Entry(acidente,width=20)
    resposta_texto.grid(row=2, column=0, padx=10, pady=5,sticky= 'nsew')
    
    texto2 = tk.Label(acidente,text='População')
    texto2.grid(row=1, column=1, padx=10, pady=5,sticky= 'nsew')
    resposta_texto2 = tk.Entry(acidente,width=20)
    resposta_texto2.grid(row=2, column=1, padx=10, pady=5,sticky= 'nsew')

    texto3 = tk.Label(acidente,text='Taxa')
    texto3.grid(row=1, column=2, padx=10, pady=5,sticky= 'nsew')

    resposta = tk.Label(acidente,text='')
    resposta.grid(row=2, column=2, padx=10, pady=5,sticky= 'nsew')

    #def
    def calculo():
        x = float(resposta_texto.get())
        y = float(resposta_texto2.get())
        resposta.configure(text=f'{x/y}')
        dados['acidentes'] = x/y
    #botao
    botao = tk.Button(acidente,text='Enviar',command= calculo)
    botao.grid(row=3, column=0, padx=10, pady=5,sticky= 'nsew')

def educacao():
    #janela
    educacao = tk.Toplevel()
    educacao.title('Centros Logisticos de Distribução')
    educacao.configure(background ='#dee0e3')
    educacao.geometry('700x500')
    educacao.resizable(True,True)

    #texto
    texto = tk.Label(educacao,text='Calculo',font=("Arial Bold", 10) )
    texto.grid(row=0, column=0, padx=10, pady=5,sticky= 'nsew') 

    texto2 = tk.Label(educacao,text='Como são as ações educativas pelo principal orgão educador de trânsito ?',font=("Arial Bold", 10),background='#ffffff')
    texto2.grid(row=3, column=0, padx=10, pady=5,sticky= 'nsew')

    total = tk.Label(educacao,text='Total',font=("Arial Bold", 10) )
    total.grid(row=6, column=0, padx=10, pady=5,sticky= 'nsew')

    vazio = tk.Label(educacao,text='',font=("Arial Bold", 10) )
    vazio.grid(row=7, column=0, padx=10, pady=5,sticky= 'nsew')
    #caixas
    fisico = tk.IntVar()
    escola = tk.IntVar()
    material = tk.IntVar()
    acoes = tk.IntVar()

    #caixas
    perguntafisico = tk.Checkbutton(educacao, text="Local fisico para educação de trânsito?", variable=fisico)
    perguntaescola = tk.Checkbutton(educacao, text="Presença em escolas?", variable=escola)
    perguntamaterial = tk.Checkbutton(educacao, text="Material para educação no transito?", variable=material)
    perguntaacoes = tk.Checkbutton(educacao, text="Ações com condutores para educação", variable=acoes)


    perguntafisico.grid(row=1, column=0, padx=10, pady=5,sticky= 'nsew')
    perguntaescola.grid(row=1, column=1, padx=10, pady=5,sticky= 'nsew')
    perguntamaterial.grid(row=2, column=0, padx=10, pady=5,sticky= 'nsew')
    perguntaacoes.grid(row=2, column=1, padx=10, pady=5,sticky= 'nsew')

    #caixinha
    opcoes = ['Pontuais','Constantes']

    caixa = ttk.Combobox(educacao,values=opcoes)
    caixa.current(0)
    caixa.grid(row=4, column=0, padx=10, pady=5,sticky= 'nsew')

    #def
    def calculo():
        pergunta_caixa = str(caixa.get())
        fisico_r = int(fisico.get())
        escola_r = int(escola.get())
        materia_r = int(material.get())
        acoes_r = int(acoes.get())

        if pergunta_caixa.upper() == 'CONSTANTES':
            pergunta_caixa = 0.2
        else:
            pergunta_caixa = 0
        if fisico_r == 1:
            fisico_r = 0.2
        if escola_r == 1:
            escola_r = 0.2
        if materia_r == 1:
            materia_r = 0.2
        if acoes_r == 1:
            acoes_r = 0.2
        vazio.configure(text=f'{pergunta_caixa+fisico_r+escola_r+materia_r+acoes_r}')
        dados['calculo'] = pergunta_caixa+fisico_r+escola_r+materia_r+acoes_r
        print(dados)
    #botao
    botao = tk.Button(educacao,text='Enviar',command= calculo)
    botao.grid(row=5, column=0, padx=10, pady=5,sticky= 'nsew')

def inteligencia():
    def calculo():
        gps = float(resposta_texto.get())
        onibus = float(resposta_texto2.get())
        calc = gps/onibus
        resposta.configure(text=f'{calc}')
        dados['inteligencia'] = calc
        
    #janela
    inteligencia = tk.Toplevel()
    inteligencia.title('Sistemas Inteligentes')
    inteligencia.configure(background ='#dee0e3')
    inteligencia.geometry('700x500')
    inteligencia.resizable(True,True)

    #textos
    texto = tk.Label(inteligencia,text='Frota com GPS')
    texto.grid(row=1, column=0, padx=10, pady=5,sticky= 'nsew')
    resposta_texto = tk.Entry(inteligencia,width=20)
    resposta_texto.grid(row=2, column=0, padx=10, pady=5,sticky= 'nsew')
    
    texto2 = tk.Label(inteligencia,text='Frota total de ônibus')
    texto2.grid(row=1, column=1, padx=10, pady=5,sticky= 'nsew')
    resposta_texto2 = tk.Entry(inteligencia,width=20)
    resposta_texto2.grid(row=2, column=1, padx=10, pady=5,sticky= 'nsew')

    texto3 = tk.Label(inteligencia,text='Total')
    texto3.grid(row=1, column=2, padx=10, pady=5,sticky= 'nsew')

    resposta = tk.Label(inteligencia,text='')
    resposta.grid(row=2, column=2, padx=10, pady=5,sticky= 'nsew')
    #botao
    botao = tk.Button(inteligencia,text='Enviar',command= calculo)
    botao.grid(row=3, column=0, padx=10, pady=5,sticky= 'nsew')

def digital():
    #janela
    digital = tk.Toplevel()
    digital.title('Integração Digital')
    digital.configure(background ='#dee0e3')
    digital.geometry('700x500')
    digital.resizable(True,True)

    #textos
    P_modais = tk.Label(digital,text=' P_modais',font=("Arial Bold", 10) )
    P_área = tk.Label(digital,text='P_área',font=("Arial Bold", 10) )
    N_inow = tk.Label(digital,text=' N_inow ',font=("Arial Bold", 10) )
    Tmax = tk.Label(digital,text=' Tmax',font=("Arial Bold", 10) )
    Tespera = tk.Label(digital,text=' Tespera',font=("Arial Bold", 10) )

    Ui = tk.Label(digital,text='U ',font=("Arial Bold", 10) )
    Total = tk.Label(digital,text='Total',font=("Arial Bold", 10) )
    r1 = tk.Label(digital,text='',font=("Arial Bold", 10) )
    r2 = tk.Label(digital,text='',font=("Arial Bold", 10) )

    P_modais.grid(row=0, column=1, padx=10, pady=5,sticky= 'nsew')
    P_área.grid(row=1, column=1, padx=10, pady=5,sticky= 'nsew')
    N_inow.grid(row=2, column=1, padx=10, pady=5,sticky= 'nsew')
    Tmax.grid(row=3, column=1, padx=10, pady=5,sticky= 'nsew')
    Tespera.grid(row=4, column=1, padx=10, pady=5,sticky= 'nsew')

    Ui.grid(row=0, column=3, padx=10, pady=5,sticky= 'nsew')
    Total.grid(row=0, column=4, padx=10, pady=5,sticky= 'nsew')
    r1.grid(row=1, column=3, padx=10, pady=5,sticky= 'nsew')
    r2.grid(row=1, column=4, padx=10, pady=5,sticky= 'nsew')

    #inputs

    P_modais_1 = tk.Entry(digital,width=20)
    P_área_1 = tk.Entry(digital,width=20)
    N_inow_1 = tk.Entry(digital,width=20)
    Tmax_1 = tk.Entry(digital,width=20)
    Tespera_1 = tk.Entry(digital,width=20)

    P_modais_1.grid(row=0, column=2, padx=10, pady=5,sticky= 'nsew')
    P_área_1.grid(row=1, column=2, padx=10, pady=5,sticky= 'nsew')
    N_inow_1.grid(row=2, column=2, padx=10, pady=5,sticky= 'nsew')
    Tmax_1.grid(row=3, column=2, padx=10, pady=5,sticky= 'nsew')
    Tespera_1.grid(row=4, column=2, padx=10, pady=5,sticky= 'nsew')


    #calculo
    def calculo():
        modais = float(P_modais_1.get())
        area = float(P_área_1.get())
        inow = float(N_inow_1.get())
        tmax = float(Tmax_1.get())
        tesperasla = float(Tespera_1.get())
        calc = (tesperasla/tmax)
        calc2 = (modais*0.4) + (area *0.3) + (inow * 0.2) + (calc * 0.2)           
        r1.configure(text=f'{calc}')
        r2.configure(text=f'{calc2}')
        dados['digital'] = calc2 
    #botao
    enviar = tk.Button(digital,text='Enviar',command= calculo)
    enviar.grid(row=5, column=1, padx=10, pady=5,sticky= 'nsew')

def infraestrutura():
    def calculo():
        semaforos = float(resposta_texto.get())
        km = float(resposta_texto2.get())
        calc = semaforos/km
        resposta.configure(text=f'{calc}')
        dados['infraestrutura'] = calc
        
    #janela
    infraestrutura = tk.Toplevel()
    infraestrutura.title('Infraestrutura Conectada')
    infraestrutura.configure(background ='#dee0e3')
    infraestrutura.geometry('700x500')
    infraestrutura.resizable(True,True)

    #textos
    texto = tk.Label(infraestrutura,text='Quantidade Semaforos')
    texto.grid(row=1, column=0, padx=10, pady=5,sticky= 'nsew')
    resposta_texto = tk.Entry(infraestrutura,width=20)
    resposta_texto.grid(row=2, column=0, padx=10, pady=5,sticky= 'nsew')
    
    texto2 = tk.Label(infraestrutura,text='KM²')
    texto2.grid(row=1, column=1, padx=10, pady=5,sticky= 'nsew')
    resposta_texto2 = tk.Entry(infraestrutura,width=20)
    resposta_texto2.grid(row=2, column=1, padx=10, pady=5,sticky= 'nsew')

    texto3 = tk.Label(infraestrutura,text='Total')
    texto3.grid(row=1, column=2, padx=10, pady=5,sticky= 'nsew')

    resposta = tk.Label(infraestrutura,text='')
    resposta.grid(row=2, column=2, padx=10, pady=5,sticky= 'nsew')
    #botao
    botao = tk.Button(infraestrutura,text='Enviar',command= calculo)
    botao.grid(row=3, column=0, padx=10, pady=5,sticky= 'nsew')

def abertos():
     #janela
    abertos = tk.Toplevel()
    abertos.title('Dados abertos de mobilidade')
    abertos.configure(background ='#dee0e3')
    abertos.geometry('700x500')
    abertos.resizable(True,True)

    #textos
    portais = tk.Label(abertos,text=' QTD PORTAIS (TQ)',font=("Arial Bold", 10) )
    tipo_dados = tk.Label(abertos,text='TIPO DADOS (TD)',font=("Arial Bold", 10) )
    atualizacao = tk.Label(abertos,text=' ATUALIZACAO (TA) ',font=("Arial Bold", 10) )
    formato = tk.Label(abertos,text=' FORMATO ABERTO (TS)',font=("Arial Bold", 10) )
    acesso = tk.Label(abertos,text=' FACIL ACESSO (TS)',font=("Arial Bold", 10) )

    raw4 = tk.Label(abertos,text='TEC_04_RAW ',font=("Arial Bold", 10) )
    tec4 = tk.Label(abertos,text='TEC_04',font=("Arial Bold", 10) )
    r1 = tk.Label(abertos,text='',font=("Arial Bold", 10) )
    r2 = tk.Label(abertos,text='',font=("Arial Bold", 10) )

    portais.grid(row=0, column=1, padx=10, pady=5,sticky= 'nsew')
    tipo_dados.grid(row=1, column=1, padx=10, pady=5,sticky= 'nsew')
    atualizacao.grid(row=2, column=1, padx=10, pady=5,sticky= 'nsew')
    formato.grid(row=3, column=1, padx=10, pady=5,sticky= 'nsew')
    acesso.grid(row=4, column=1, padx=10, pady=5,sticky= 'nsew')

    raw4.grid(row=0, column=3, padx=10, pady=5,sticky= 'nsew')
    tec4.grid(row=0, column=4, padx=10, pady=5,sticky= 'nsew')
    r1.grid(row=1, column=3, padx=10, pady=5,sticky= 'nsew')
    r2.grid(row=1, column=4, padx=10, pady=5,sticky= 'nsew')

    #inputs

    portais_1 = tk.Entry(abertos,width=20)
    tipo_dados_1 = tk.Entry(abertos,width=20)
    atualizacao_1 = tk.Entry(abertos,width=20)
    formato_1 = tk.Entry(abertos,width=20)
    acesso_1 = tk.Entry(abertos,width=20)

    portais_1.grid(row=0, column=2, padx=10, pady=5,sticky= 'nsew')
    tipo_dados_1.grid(row=1, column=2, padx=10, pady=5,sticky= 'nsew')
    atualizacao_1.grid(row=2, column=2, padx=10, pady=5,sticky= 'nsew')
    formato_1.grid(row=3, column=2, padx=10, pady=5,sticky= 'nsew')
    acesso_1.grid(row=4, column=2, padx=10, pady=5,sticky= 'nsew')


    #calculo
    def calculo():
        portaiss = float(portais_1.get())
        tipo_dadoss = float(tipo_dados_1.get())
        atualizacaos = float(atualizacao_1.get())
        formatos = float(formato_1.get())
        acessos = float(acesso_1.get())
        calc = (portaiss * 2) + (tipo_dadoss * 1.5) + (atualizacaos * 3) + (formatos * 5 ) + (acessos * 2)
        calc2 = (calc / 36) * 5           
        r1.configure(text=f'{calc}')
        r2.configure(text=f'{calc2}')
        dados['abertos'] = calc2 
    #botao
    enviar = tk.Button(abertos,text='Enviar',command= calculo)
    enviar.grid(row=5, column=1, padx=10, pady=5,sticky= 'nsew')

#questionario principal

b1 = tk.Button(root,text='Taxa de Motorização',command=taxadeacidente)
b1.grid(row=1, column=0, padx=10, pady=5,sticky= 'nsew')

b2 =tk.Button(root,text='Uso de Energia Limpa e Combusti',command= uso_de_energia)
b2.grid(row=1, column=1, padx=10, pady=5,sticky= 'nsew')

b3 =tk.Button(root,text='Sistema de Transporte Compartil',command= transporte_compartil )
b3.grid(row=2, column=0, padx=10, pady=5,sticky= 'nsew')

b4 =tk.Button(root,text='Ciclovias',command= ciclovias)
b4.grid(row=2, column=1, padx=10, pady=5,sticky= 'nsew',)

b5 =tk.Button(root,text='Termianais Intermodais',command=terminais)
b5.grid(row=3, column=0, padx=10, pady=5,sticky= 'nsew')

b6 =tk.Button(root,text='Sistema Integrado de Bilheteria',command=bilheteria)
b6.grid(row=3, column=1, padx=10, pady=5,sticky= 'nsew')

b7 =tk.Button(root,text='Sistema de Informação',command=informação)
b7.grid(row=4, column=0, padx=10, pady=5,sticky= 'nsew')

b8 =tk.Button(root,text='Tempo de Viagem do Transporte P',command=viagem)
b8.grid(row=4, column=1, padx=10, pady=5,sticky= 'nsew')

b9 =tk.Button(root,text='Politica de Mobilidade Urbana',command=mobilidade)
b9.grid(row=5, column=0, padx=10, pady=5,sticky= 'nsew')

b10 =tk.Button(root,text='Centros Logisticos de Distribução',command=distribuicao)
b10.grid(row=5, column=1, padx=10, pady=5,sticky= 'nsew')

b11=tk.Button(root,text='Acidentes de Transito',command=acidente)
b11.grid(row=6, column=0,padx=10, pady=5,sticky= 'nsew')

b12=tk.Button(root,text='Educação para o Transito',command=educacao)
b12.grid(row=6, column=1,padx=10, pady=5,sticky= 'nsew')

b13=tk.Button(root,text='Sistemas Inteligentes',command=inteligencia)  #########
b13.grid(row=7, column=0,padx=10, pady=5,sticky= 'nsew')

b14=tk.Button(root,text='Integração Digital',command=digital)
b14.grid(row=7, column=1,padx=10, pady=5,sticky= 'nsew')

b15=tk.Button(root,text='Infraestrutura Conectada',command=infraestrutura)  
b15.grid(row=8, column=0,padx=10, pady=5,sticky= 'nsew')

b16=tk.Button(root,text='Infraestrutura Conectada',command=abertos)  
b16.grid(row=8, column=1,padx=10, pady=5,sticky= 'nsew')

#fim
import tkinter as tk
from tkinter import ttk

def janela_final():
        janela_final = tk.Tk()
        janela_final.title('Planilha1')
        janela_final.configure(background ='#d5d8de')
        janela_final.geometry('700x500')
        janela_final.resizable(True,True)
        janela_final.grid_rowconfigure(0, weight=1)
        janela_final.grid_columnconfigure(0, weight=1)          

        canvas = tk.Canvas(janela_final)
        canvas.grid(row=0, column=0, sticky="nsew")

        frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")


        #titulos
        dimensao = tk.Label(frame,text='Dimensao',font=("Arial Bold", 10,'bold'),background='#757070',fg='#ffffff',)
        dimensao.grid(row=0, column=0, padx=10, pady=5,sticky= 'nsew') 

        peso_da_dimensao = tk.Label(frame,text='Peso da Dimensão',font=("Arial Bold", 10,'bold'),background='#757070',fg='#ffffff',)
        peso_da_dimensao.grid(row=0, column=1, padx=10, pady=5,sticky= 'nsew') 

        Variavel = tk.Label(frame,text='Variavel',font=("Arial Bold", 10,'bold'),background='#757070',fg='#ffffff',)
        Variavel.grid(row=0, column=2, padx=10, pady=5,sticky= 'nsew')

        Indicador = tk.Label(frame,text='Indicador',font=("Arial Bold", 10,'bold'),background='#757070',fg='#ffffff',)
        Indicador.grid(row=0, column=3, padx=10, pady=5,sticky= 'nsew')

        Identificador = tk.Label(frame,text='Identificador',font=("Arial Bold", 10,'bold'),background='#757070',fg='#ffffff',)
        Identificador.grid(row=0, column=4, padx=10, pady=5,sticky= 'nsew')

        Score = tk.Label(frame,text='Score',font=("Arial Bold", 10,'bold'),background='#757070',fg='#ffffff',)
        Score.grid(row=0, column=5, padx=10, pady=5,sticky= 'nsew')

        Peso_do_Indicador = tk.Label(frame,text='Peso do Indicador',font=("Arial Bold", 10,'bold'),background='#757070',fg='#ffffff',)
        Peso_do_Indicador.grid(row=0, column=6, padx=10, pady=5,sticky= 'nsew')

        Direção = tk.Label(frame,text='Direção',font=("Arial Bold", 10,'bold'),background='#757070',fg='#ffffff',)
        Direção.grid(row=0, column=7, padx=10, pady=5,sticky= 'nsew')

        Dados = tk.Label(frame,text='Dados',font=("Arial Bold", 10,'bold'),background='#757070',fg='#ffffff',)
        Dados.grid(row=0, column=8, padx=10, pady=5,sticky= 'nsew')
        
        Normatização = tk.Label(frame,text='Normatização',font=("Arial Bold", 10,'bold'),background='#757070',fg='#ffffff',)
        Normatização.grid(row=0, column=9, padx=10, pady=5,sticky= 'nsew')

        Valor_da_Dimensão = tk.Label(frame,text='Valor da Dimensão',font=("Arial Bold", 10,'bold'),background='#757070',fg='#ffffff',)
        Valor_da_Dimensão.grid(row=0, column=10, padx=10, pady=5,sticky= 'nsew')

        Valor_Absoluto_do = tk.Label(frame,text='Valor Absoluto do IM!',font=("Arial Bold", 10,'bold'),background='#757070',fg='#ffffff',)
        Valor_Absoluto_do.grid(row=0, column=11, padx=10, pady=5,sticky= 'nsew')
        #coluna 0
       
       

        sustentabilidade = tk.Label(frame,text='Sustentabilidade',font=("Arial Bold", 15,'bold',),background='#4287f5',fg='#000000',)
        sustentabilidade.grid(row=1, column=0, padx=10, pady=5,sticky= 'nsew',rowspan=4)
        

        #=======
        Acessibilidade = tk.Label(frame,text='Acessibilidade',font=("Arial Bold", 15,'bold'),background='#de00e6',fg='#000000',)
        Acessibilidade.grid(row=5, column=0, padx=10, pady=5,sticky= 'nsew',rowspan=4)

       
        #=======

        Planejamento_e_Gestão_urbana = tk.Label(frame,text='Planejamento e Gestão urbana',font=("Arial Bold", 15,'bold'),background='#05c9f5')
        Planejamento_e_Gestão_urbana.grid(row=9, column=0, padx=10, pady=5,sticky= 'nsew',rowspan=4)

        #=======
        
        Tecnologia  = tk.Label(frame,text='Tecnologia ',font=("Arial Bold", 15,'bold'),background='#05c915')
        Tecnologia.grid(row=13, column=0, padx=10, pady=5,sticky= 'nsew',rowspan=4)

        #coluna 2  ==============================================

        sustentabilidade = tk.Label(frame,text='0,34',font=("Arial Bold", 20,'bold'),background='#4287f5',fg='#000000',)
        sustentabilidade.grid(row=1, column=1, padx=10, pady=5,sticky= 'nsew',rowspan=4)
        
        #=======
      

        Acessibilidade = tk.Label(frame,text='0,36',font=("Arial Bold", 20,'bold'),background='#de00e6',fg='#000000',)
        Acessibilidade.grid(row=5, column=1, padx=10, pady=5,sticky= 'nsew',rowspan=4)

        #=======


        Planejamento_e_Gestão_urbana = tk.Label(frame,text='0,30',font=("Arial Bold", 20,'bold'),background='#05c9f5')
        Planejamento_e_Gestão_urbana.grid(row=9, column=1, padx=10, pady=5,sticky= 'nsew',rowspan=4,)

        #=======

        Tecnologia = tk.Label(frame,text='0,30',font=("Arial Bold", 20,'bold'),background='#05c915')
        Tecnologia.grid(row=13, column=1, padx=10, pady=5,sticky= 'nsew',rowspan=4,)

        #coluna 3  ==============================================
        Ambiental = tk.Label(frame,text='Taxa de Motorização',font=("Arial Bold", 10,'bold'),background='#4287f5')
        Ambiental.grid(row=1, column=3, padx=10, pady=5,sticky= 'nsew')

        Energetico = tk.Label(frame,text='Uso de Energia Limpa e Combustivel Alternativo',font=("Arial Bold", 10,'bold'),background='#4287f5',fg='#000000',)
        Energetico.grid(row=2, column=3, padx=10, pady=5,sticky= 'nsew')
        
        Economico = tk.Label(frame,text='Sistema de Transporte Compartilhado',font=("Arial Bold", 10,'bold'),background='#4287f5')
        Economico.grid(row=3, column=3, padx=10, pady=5,sticky= 'nsew')

        Social = tk.Label(frame,text='Ciclovias',font=("Arial Bold", 10,'bold'),background='#4287f5')
        Social.grid(row=4, column=3, padx=10, pady=5,sticky= 'nsew')
        #=======
        Fisico = tk.Label(frame,text='Termianais Intermodais',font=("Arial Bold", 10,'bold'),background='#de00e6')
        Fisico.grid(row=5, column=3, padx=10, pady=5,sticky= 'nsew')

        Tarifaria = tk.Label(frame,text='Sistema Integrado de Bilheteria',font=("Arial Bold", 10,'bold'),background='#de00e6',fg='#000000',)
        Tarifaria.grid(row=6, column=3, padx=10, pady=5,sticky= 'nsew')

        Digital = tk.Label(frame,text='Sistema de Informação',font=("Arial Bold", 10,'bold'),background='#de00e6')
        Digital.grid(row=7, column=3, padx=10, pady=5,sticky= 'nsew')

        Temporal = tk.Label(frame,text='Tempo de Viagem do Transporte Publico Coletivo',font=("Arial Bold", 10,'bold'),background='#de00e6')
        Temporal.grid(row=8, column=3, padx=10, pady=5,sticky= 'nsew')
        #=======
        Educação = tk.Label(frame,text='Educação para o Transito',font=("Arial Bold", 10,'bold'),background='#05c9f5')
        Educação.grid(row=9, column=3, padx=10, pady=5,sticky= 'nsew')

        Politica = tk.Label(frame,text='Politica de Mobilidade Urbana',font=("Arial Bold", 10,'bold'),background='#05c9f5')
        Politica.grid(row=10, column=3, padx=10, pady=5,sticky= 'nsew',)

        Infraestrutura = tk.Label(frame,text='Centros Logisticos de Distribução',font=("Arial Bold", 10,'bold'),background='#05c9f5')
        Infraestrutura.grid(row=11, column=3, padx=10, pady=5,sticky= 'nsew')

        Saude_Publica = tk.Label(frame,text='Acidentes de Transito',font=("Arial Bold", 10,'bold'),background='#05c9f5')
        Saude_Publica.grid(row=12, column=3, padx=10, pady=5,sticky= 'nsew')

        #==========

        sistemas_inteligentes = tk.Label(frame,text='',font=("Arial Bold", 10,'bold'),background='#05c915')
        sistemas_inteligentes.grid(row=13, column=3, padx=10, pady=5,sticky= 'nsew')

        integracao_digital = tk.Label(frame,text='',font=("Arial Bold", 10,'bold'),background='#05c915')
        integracao_digital.grid(row=14, column=3, padx=10, pady=5,sticky= 'nsew',)

        Infraestrutura_conectada = tk.Label(frame,text='',font=("Arial Bold", 10,'bold'),background='#05c915')
        Infraestrutura_conectada.grid(row=15, column=3, padx=10, pady=5,sticky= 'nsew')

        dados_abertos_de_mobilidade = tk.Label(frame,text='',font=("Arial Bold", 10,'bold'),background='#05c915')
        dados_abertos_de_mobilidade.grid(row=16, column=3, padx=10, pady=5,sticky= 'nsew')

        #coluna 2  ==============================================

        texto1 = tk.Label(frame,text='Ambiental',font=("Arial Bold", 10,'bold'),background='#4287f5')
        texto1.grid(row=1, column=2, padx=10, pady=5,sticky= 'nsew')

        texto2 = tk.Label(frame,text='Energético',font=("Arial Bold", 10,'bold'),background='#4287f5',fg='#000000',)
        texto2.grid(row=2, column=2, padx=10, pady=5,sticky= 'nsew')
        
        texto3 = tk.Label(frame,text='Economico',font=("Arial Bold", 10,'bold'),background='#4287f5')
        texto3.grid(row=3, column=2, padx=10, pady=5,sticky= 'nsew')

        texto4 = tk.Label(frame,text='Social',font=("Arial Bold", 10,'bold'),background='#4287f5')
        texto4.grid(row=4, column=2, padx=10, pady=5,sticky= 'nsew')
        #=======
        texto5 = tk.Label(frame,text='Físico',font=("Arial Bold", 10,'bold'),background='#de00e6')
        texto5.grid(row=5, column=2, padx=10, pady=5,sticky= 'nsew')

        texto6 = tk.Label(frame,text='Tarifaria',font=("Arial Bold", 10,'bold'),background='#de00e6',fg='#000000',)
        texto6.grid(row=6, column=2, padx=10, pady=5,sticky= 'nsew')

        texto7 = tk.Label(frame,text='Digital',font=("Arial Bold", 10,'bold'),background='#de00e6')
        texto7.grid(row=7, column=2, padx=10, pady=5,sticky= 'nsew')

        texto8 = tk.Label(frame,text='Temporal',font=("Arial Bold", 10,'bold'),background='#de00e6')
        texto8.grid(row=8, column=2, padx=10, pady=5,sticky= 'nsew')
        #=======
        texto9 = tk.Label(frame,text='Educação',font=("Arial Bold", 10,'bold'),background='#05c9f5')
        texto9.grid(row=9, column=2, padx=10, pady=5,sticky= 'nsew')

        texto10 = tk.Label(frame,text='Politica',font=("Arial Bold", 10,'bold'),background='#05c9f5')
        texto10.grid(row=10, column=2, padx=10, pady=5,sticky= 'nsew',)

        texto11 = tk.Label(frame,text='Infraestrutura',font=("Arial Bold", 10,'bold'),background='#05c9f5')
        texto11.grid(row=11, column=2, padx=10, pady=5,sticky= 'nsew')

        texto12 = tk.Label(frame,text='Saúde Publica',font=("Arial Bold", 10,'bold'),background='#05c9f5')
        texto12.grid(row=12, column=2, padx=10, pady=5,sticky= 'nsew')

        #=========

        texto13 = tk.Label(frame,text='Sistemas Inteligentes',font=("Arial Bold", 10,'bold'),background='#05c915')
        texto13.grid(row=13, column=2, padx=10, pady=5,sticky= 'nsew')

        texto14 = tk.Label(frame,text='Integração Digital',font=("Arial Bold", 10,'bold'),background='#05c915')
        texto14.grid(row=14, column=2, padx=10, pady=5,sticky= 'nsew',)

        texto15 = tk.Label(frame,text='Infraestrutura Concectada',font=("Arial Bold", 10,'bold'),background='#05c915')
        texto15.grid(row=15, column=2, padx=10, pady=5,sticky= 'nsew')

        texto16 = tk.Label(frame,text='Dados Abertos de Mobilidade',font=("Arial Bold", 10,'bold'),background='#05c915')
        texto16.grid(row=16, column=2, padx=10, pady=5,sticky= 'nsew')
       
       #coluna 4 =============================

        Identificador1 = tk.Label(frame,text='SUS01',font=("Arial Bold", 10,'bold'),background='#525354',fg='#4287f5')
        Identificador1.grid(row=1, column=4, padx=10, pady=5,sticky= 'nsew')

        Identificador2 = tk.Label(frame,text='SUS02',font=("Arial Bold", 10,'bold'),background='#525354',fg='#4287f5',)
        Identificador2.grid(row=2, column=4, padx=10, pady=5,sticky= 'nsew')
        
        Identificador3 = tk.Label(frame,text='SUS03',font=("Arial Bold", 10,'bold'),background='#525354',fg='#4287f5')
        Identificador3.grid(row=3, column=4, padx=10, pady=5,sticky= 'nsew')

        Identificador4 = tk.Label(frame,text='SUS04',font=("Arial Bold", 10,'bold'),background='#525354',fg='#4287f5')
        Identificador4.grid(row=4, column=4, padx=10, pady=5,sticky= 'nsew')
        #=======
        Identificador5 = tk.Label(frame,text='SUS01',font=("Arial Bold", 10,'bold'),background='#525354',fg='#de00e6')
        Identificador5.grid(row=5, column=4, padx=10, pady=5,sticky= 'nsew')

        Identificador6 = tk.Label(frame,text='ACE02',font=("Arial Bold", 10,'bold'),fg='#de00e6',background='#525354',)
        Identificador6.grid(row=6, column=4, padx=10, pady=5,sticky= 'nsew')

        Identificador7 = tk.Label(frame,text='ACE03',font=("Arial Bold", 10,'bold'),fg='#de00e6',background='#525354')
        Identificador7.grid(row=7, column=4, padx=10, pady=5,sticky= 'nsew')

        Identificador8 = tk.Label(frame,text='ACE04',font=("Arial Bold", 10,'bold'),fg='#de00e6',background='#525354')
        Identificador8.grid(row=8, column=4, padx=10, pady=5,sticky= 'nsew')
        #=======
        Identificador9 = tk.Label(frame,text='PGU01',font=("Arial Bold", 10,'bold'),background='#525354',fg='#05c9f5')
        Identificador9.grid(row=9, column=4, padx=10, pady=5,sticky= 'nsew')

        Identificador10 = tk.Label(frame,text='PGU02',font=("Arial Bold", 10,'bold'),background='#525354',fg='#05c9f5')
        Identificador10.grid(row=10, column=4, padx=10, pady=5,sticky= 'nsew',)

        Identificador11 = tk.Label(frame,text='PGU03',font=("Arial Bold", 10,'bold'),background='#525354',fg='#05c9f5')
        Identificador11.grid(row=11, column=4, padx=10, pady=5,sticky= 'nsew')

        Identificador12 = tk.Label(frame,text=' PGU04',font=("Arial Bold", 10,'bold'),background='#525354',fg='#05c9f5')
        Identificador12.grid(row=12, column=4, padx=10, pady=5,sticky= 'nsew')

        #===========
        
        Identificador13 = tk.Label(frame,text='TEC01',font=("Arial Bold", 10,'bold'),background='#525354',fg='#05c915')
        Identificador13.grid(row=13, column=4, padx=10, pady=5,sticky= 'nsew')

        Identificador14 = tk.Label(frame,text='TEC02',font=("Arial Bold", 10,'bold'),background='#525354',fg='#05c915')
        Identificador14.grid(row=14, column=4, padx=10, pady=5,sticky= 'nsew',)

        Identificador15 = tk.Label(frame,text='TEC03',font=("Arial Bold", 10,'bold'),background='#525354',fg='#05c915')
        Identificador15.grid(row=15, column=4, padx=10, pady=5,sticky= 'nsew')

        Identificador16 = tk.Label(frame,text=' TEC04',font=("Arial Bold", 10,'bold'),background='#525354',fg='#05c915')
        Identificador16.grid(row=16, column=4, padx=10, pady=5,sticky= 'nsew')

        #coluna 9  ==============================================
        f1 = dados['monitoracao']/ dados['ciclovias']+ dados['transporte'] + dados['uso de energia'] + dados['monitoracao']
        normatizacao = tk.Label(frame,text=f'{f1} ',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        normatizacao.grid(row=1, column=9, padx=10, pady=5,sticky= 'nsew')
        
        f2 = dados['uso de energia']/ dados['ciclovias']+ dados['transporte'] + dados['uso de energia'] + dados['monitoracao']
        normatizacao2 = tk.Label(frame,text=f'{f2}',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000',)
        normatizacao2.grid(row=2, column=9, padx=10, pady=5,sticky= 'nsew')
        
        f3 = dados['transporte']/ dados['ciclovias']+ dados['transporte'] + dados['uso de energia'] + dados['monitoracao']
        normatizacao3 = tk.Label(frame,text=f'{f3}',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        normatizacao3.grid(row=3, column=9, padx=10, pady=5,sticky= 'nsew')

        f4 =dados['ciclovias']/ dados['ciclovias']+ dados['transporte'] + dados['uso de energia'] + dados['monitoracao']
        normatizacao4 = tk.Label(frame,text=f'{f4}',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        normatizacao4.grid(row=4, column=9, padx=10, pady=5,sticky= 'nsew')
        #====================================================================
        
        f5 = dados['terminais'] / dados['viagem'] + dados['informação'] + dados['bilheteria']+ dados['terminais']
        normatizacao5 = tk.Label(frame,text=f'{f5}',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        normatizacao5.grid(row=5, column=9, padx=10, pady=5,sticky= 'nsew')

        f6 = dados['bilheteria'] /dados['viagem'] + dados['informação'] + dados['bilheteria']+ dados['terminais']
        normatizacao6 = tk.Label(frame,text=f'{f6}',font=("Arial Bold", 20,'bold'),fg='#000000',background='#ffffff',)
        normatizacao6.grid(row=6, column=9, padx=10, pady=5,sticky= 'nsew')

        f7 = dados['informação'] / dados['viagem'] + dados['informação'] + dados['bilheteria']+ dados['terminais']
        normatizacao7 = tk.Label(frame,text=f'{f7}',font=("Arial Bold", 20,'bold'),fg='#000000',background='#ffffff')
        normatizacao7.grid(row=7, column=9, padx=10, pady=5,sticky= 'nsew')

        f8 = dados['viagem'] / dados['viagem'] + dados['informação'] + dados['bilheteria']+ dados['terminais']
        normatizacao8 = tk.Label(frame,text=f'{f8}',font=("Arial Bold", 20,'bold'),fg='#000000',background='#ffffff')
        normatizacao8.grid(row=8, column=9, padx=10, pady=5,sticky= 'nsew')
        #====================================================================
        
        f9 = dados['mobilidade'] / dados['calculo'] + dados['acidentes'] + dados['mobilidade'] + dados['distribuicao'] 
        normatizacao9 = tk.Label(frame,text=f'{f9}',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        normatizacao9.grid(row=9, column=9, padx=10, pady=5,sticky= 'nsew')

        f10 = dados['distribuicao'] / dados['calculo'] + dados['acidentes'] + dados['mobilidade'] + dados['distribuicao']  
        normatizacao10 = tk.Label(frame,text=f'{f10}',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        normatizacao10.grid(row=10, column=9, padx=1, pady=5,sticky= 'nsew',)

        f11 = dados['acidentes'] / dados['calculo'] + dados['acidentes'] + dados['mobilidade'] + dados['distribuicao'] 
        normatizacao11 = tk.Label(frame,text=f'{f11}',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        normatizacao11.grid(row=11, column=9, padx=10, pady=5,sticky= 'nsew')

        f12 = dados['calculo'] / dados['calculo'] + dados['acidentes'] + dados['mobilidade'] + dados['distribuicao'] 
        normatizacao12 = tk.Label(frame,text=f'{f12}',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        normatizacao12.grid(row=12, column=9, padx=10, pady=5,sticky= 'nsew')
        
        #====================================================================
        
        f13 = dados['inteligencia']  / dados['abertos']+ dados['infraestrutura'] + dados['digital'] + dados['inteligencia'] 
        normatizacao13 = tk.Label(frame,text=f'{f13}',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        normatizacao13.grid(row=13, column=9, padx=10, pady=5,sticky= 'nsew')

        f14 = dados['digital'] / dados['abertos']+ dados['infraestrutura'] + dados['digital'] + dados['inteligencia']  
        normatizacao14 = tk.Label(frame,text=f'{f14}',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        normatizacao14.grid(row=14, column=9, padx=1, pady=5,sticky= 'nsew',)

        f15 = dados['infraestrutura'] / dados['abertos']+ dados['infraestrutura'] + dados['digital'] + dados['inteligencia']
        normatizacao15 = tk.Label(frame,text=f'{f15}',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        normatizacao15.grid(row=15, column=9, padx=10, pady=5,sticky= 'nsew')

        f16 = dados['abertos'] /dados['abertos']+ dados['infraestrutura'] + dados['digital'] + dados['inteligencia'] 
        normatizacao16 = tk.Label(frame,text=f'{f16}',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        normatizacao16.grid(row=16, column=9, padx=10, pady=5,sticky= 'nsew')


        #coluna 5 =============================
        g1 = f1 * 0.27
        score1 = tk.Label(frame,text=f'{g1}',font=("Arial Bold", 10,'bold'),background='#525354',fg='#4287f5')
        score1.grid(row=1, column=5, padx=10, pady=5,sticky= 'nsew')

        g2  = f2 * 0.25
        score2 = tk.Label(frame,text=f'{g2}',font=("Arial Bold", 10,'bold'),background='#525354',fg='#4287f5',)
        score2.grid(row=2, column=5, padx=10, pady=5,sticky= 'nsew')
        
        g3 = f3 * 0.26
        score3 = tk.Label(frame,text=f'{g3}',font=("Arial Bold", 10,'bold'),background='#525354',fg='#4287f5')
        score3.grid(row=3, column=5, padx=10, pady=5,sticky= 'nsew')

        g4 = f4 * 0.22
        score4 = tk.Label(frame,text=f'{g4}',font=("Arial Bold", 10,'bold'),background='#525354',fg='#4287f5')
        score4.grid(row=4, column=5, padx=10, pady=5,sticky= 'nsew')
        #=======

        g5 = f5 * 0.23
        score5 = tk.Label(frame,text=f'{g5}',font=("Arial Bold", 10,'bold'),background='#525354',fg='#de00e6')
        score5.grid(row=5, column=5, padx=10, pady=5,sticky= 'nsew')

        g6 = f6 * 0.27
        score6 = tk.Label(frame,text=f'{g6}',font=("Arial Bold", 10,'bold'),fg='#de00e6',background='#525354',)
        score6.grid(row=6, column=5, padx=10, pady=5,sticky= 'nsew')

        g7 = f7 * 0.26
        score7 = tk.Label(frame,text=f'{f7}',font=("Arial Bold", 10,'bold'),fg='#de00e6',background='#525354')
        score7.grid(row=7, column=5, padx=10, pady=5,sticky= 'nsew')

        g8 = f8 * 0.24
        score8 = tk.Label(frame,text=f'{g8}',font=("Arial Bold", 10,'bold'),fg='#de00e6',background='#525354')
        score8.grid(row=8, column=5, padx=10, pady=5,sticky= 'nsew')
        #=======

        g9 = f9 * 0.27
        score9 = tk.Label(frame,text=f'{g9}',font=("Arial Bold", 10,'bold'),background='#525354',fg='#05c9f5')
        score9.grid(row=9, column=5, padx=10, pady=5,sticky= 'nsew')

        g10 = f10 * 0.21
        score10 = tk.Label(frame,text=f'{g10}',font=("Arial Bold", 10,'bold'),background='#525354',fg='#05c9f5')
        score10.grid(row=10, column=5, padx=10, pady=5,sticky= 'nsew',)

        g11 = f11 * 0.24
        score11 = tk.Label(frame,text=f'{g11}',font=("Arial Bold", 10,'bold'),background='#525354',fg='#05c9f5')
        score11.grid(row=11, column=5, padx=10, pady=5,sticky= 'nsew')

        g12 = f12 * 0.28
        score12 = tk.Label(frame,text=f'{g12}',font=("Arial Bold", 10,'bold'),background='#525354',fg='#05c9f5')
        score12.grid(row=12, column=5, padx=10, pady=5,sticky= 'nsew')
        #==========
        g13 = f13 * 0.29
        score13 = tk.Label(frame,text=f'{g13}',font=("Arial Bold", 10,'bold'),background='#525354',fg='#05c915')
        score13.grid(row=13, column=5, padx=10, pady=5,sticky= 'nsew')

        g14 = f14 * 0.24
        score14 = tk.Label(frame,text=f'{g14}',font=("Arial Bold", 10,'bold'),background='#525354',fg='#05c915')
        score14.grid(row=14, column=5, padx=10, pady=5,sticky= 'nsew',)

        g15 = f15 * 0.27
        score15 = tk.Label(frame,text=f'{g15}',font=("Arial Bold", 10,'bold'),background='#525354',fg='#05c915')
        score15.grid(row=15, column=5, padx=10, pady=5,sticky= 'nsew')

        g16 = f16 * 0.20
        score12 = tk.Label(frame,text=f'{g16}',font=("Arial Bold", 10,'bold'),background='#525354',fg='#05c915')
        score12.grid(row=16, column=5, padx=10, pady=5,sticky= 'nsew')

        #coluna 6 =============================
       
        peso1 = tk.Label(frame,text='0,27',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        peso1.grid(row=1, column=6, padx=10, pady=5,sticky= 'nsew')

        peso2 = tk.Label(frame,text='0,25',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000',)
        peso2.grid(row=2, column=6, padx=10, pady=5,sticky= 'nsew')
        
        peso3 = tk.Label(frame,text='0,26',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        peso3.grid(row=3, column=6, padx=10, pady=5,sticky= 'nsew')

        peso4 = tk.Label(frame,text='0,22',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        peso4.grid(row=4, column=6, padx=10, pady=5,sticky= 'nsew')
        #=======
        peso5 = tk.Label(frame,text='0,23',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        peso5.grid(row=5, column=6, padx=10, pady=5,sticky= 'nsew')

        peso6 = tk.Label(frame,text='0,27',font=("Arial Bold", 20,'bold'),fg='#000000',background='#ffffff',)
        peso6.grid(row=6, column=6, padx=10, pady=5,sticky= 'nsew')

        peso7 = tk.Label(frame,text='0,26',font=("Arial Bold", 20,'bold'),fg='#000000',background='#ffffff')
        peso7.grid(row=7, column=6, padx=10, pady=5,sticky= 'nsew')

        peso8 = tk.Label(frame,text='0,24',font=("Arial Bold", 20,'bold'),fg='#000000',background='#ffffff')
        peso8.grid(row=8, column=6, padx=10, pady=5,sticky= 'nsew')
        #=======
        peso9 = tk.Label(frame,text='0,27',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        peso9.grid(row=9, column=6, padx=10, pady=5,sticky= 'nsew')

        peso10 = tk.Label(frame,text='0,21',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        peso10.grid(row=10, column=6, padx=10, pady=5,sticky= 'nsew',)

        peso11 = tk.Label(frame,text='0,24',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        peso11.grid(row=11, column=6, padx=10, pady=5,sticky= 'nsew')

        peso12 = tk.Label(frame,text='0,28',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        peso12.grid(row=12, column=6, padx=10, pady=5,sticky= 'nsew')

        #=======
        peso13 = tk.Label(frame,text='0,29',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        peso13.grid(row=13, column=6, padx=10, pady=5,sticky= 'nsew')

        peso14 = tk.Label(frame,text='0,24',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        peso14.grid(row=14, column=6, padx=10, pady=5,sticky= 'nsew',)

        peso15 = tk.Label(frame,text='0,27',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        peso15.grid(row=15, column=6, padx=10, pady=5,sticky= 'nsew')

        peso16 = tk.Label(frame,text='0,20',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        peso16.grid(row=16, column=6, padx=10, pady=5,sticky= 'nsew')

        #coluna 7 =============================
       
        sinal1 = tk.Label(frame,text='-',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        sinal1.grid(row=1, column=7, padx=10, pady=5,sticky= 'nsew')

        sinal2 = tk.Label(frame,text='+',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000',)
        sinal2.grid(row=2, column=7, padx=10, pady=5,sticky= 'nsew')
        
        sinal3 = tk.Label(frame,text='+',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        sinal3.grid(row=3, column=7, padx=10, pady=5,sticky= 'nsew')

        sinal4 = tk.Label(frame,text='+',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        sinal4.grid(row=4, column=7, padx=10, pady=5,sticky= 'nsew')
        #=======
        sinal5 = tk.Label(frame,text='+',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        sinal5.grid(row=5, column=7, padx=10, pady=5,sticky= 'nsew')

        sinal6 = tk.Label(frame,text='+',font=("Arial Bold", 20,'bold'),fg='#000000',background='#ffffff',)
        sinal6.grid(row=6, column=7, padx=10, pady=5,sticky= 'nsew')

        sinal7 = tk.Label(frame,text='+',font=("Arial Bold", 20,'bold'),fg='#000000',background='#ffffff')
        sinal7.grid(row=7, column=7, padx=10, pady=5,sticky= 'nsew')

        sinal8 = tk.Label(frame,text='-',font=("Arial Bold", 20,'bold'),fg='#000000',background='#ffffff')
        sinal8.grid(row=8, column=7, padx=10, pady=5,sticky= 'nsew')
        #=======
        sinal9 = tk.Label(frame,text='+',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        sinal9.grid(row=9, column=7, padx=10, pady=5,sticky= 'nsew')

        sinal10 = tk.Label(frame,text='+',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        sinal10.grid(row=10, column=7, padx=10, pady=5,sticky= 'nsew',)

        sinal11 = tk.Label(frame,text='+',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        sinal11.grid(row=11, column=7, padx=10, pady=5,sticky= 'nsew')

        sinal12 = tk.Label(frame,text='-',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        sinal12.grid(row=12, column=7, padx=10, pady=5,sticky= 'nsew')
        #=======
        sinal13 = tk.Label(frame,text='+',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        sinal13.grid(row=13, column=7, padx=10, pady=5,sticky= 'nsew')

        sinal14 = tk.Label(frame,text='+',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        sinal14.grid(row=14, column=7, padx=10, pady=5,sticky= 'nsew',)

        sinal15 = tk.Label(frame,text='+',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        sinal15.grid(row=15, column=7, padx=10, pady=5,sticky= 'nsew')

        sinal16 = tk.Label(frame,text='+',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        sinal16.grid(row=16, column=7, padx=10, pady=5,sticky= 'nsew')
       
        #coluna 8 =============================
       
        sla1 = tk.Label(frame,text=f'{dados['monitoracao']}',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        sla1.grid(row=1, column=8, padx=10, pady=5,sticky= 'nsew')

        sla2 = tk.Label(frame,text=f'{dados['uso de energia']}',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000',)
        sla2.grid(row=2, column=8, padx=10, pady=5,sticky= 'nsew')
        
        sla3 = tk.Label(frame,text=f'{dados['transporte']}',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        sla3.grid(row=3, column=8, padx=10, pady=5,sticky= 'nsew')

        sla4 = tk.Label(frame,text=f'{dados['ciclovias']}',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        sla4.grid(row=4, column=8, padx=10, pady=5,sticky= 'nsew')
        #=======
        sla5 = tk.Label(frame,text=f'{dados['terminais']}',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        sla5.grid(row=5, column=8, padx=10, pady=5,sticky= 'nsew')

        sla6 = tk.Label(frame,text=f'{dados['bilheteria']}',font=("Arial Bold", 20,'bold'),fg='#000000',background='#ffffff',)
        sla6.grid(row=6, column=8, padx=10, pady=5,sticky= 'nsew')

        sla7 = tk.Label(frame,text=f'{dados['informação']}',font=("Arial Bold", 20,'bold'),fg='#000000',background='#ffffff')
        sla7.grid(row=7, column=8, padx=10, pady=5,sticky= 'nsew')

        sla8 = tk.Label(frame,text=f'{dados['viagem']}',font=("Arial Bold", 20,'bold'),fg='#000000',background='#ffffff')
        sla8.grid(row=8, column=8, padx=10, pady=5,sticky= 'nsew')
        #=======
        sla9 = tk.Label(frame,text=f'{dados['mobilidade']}',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        sla9.grid(row=9, column=8, padx=10, pady=5,sticky= 'nsew')

        sla10 = tk.Label(frame,text=f'{dados['distribuicao']}',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        sla10.grid(row=10, column=8, padx=10, pady=5,sticky= 'nsew',)

        sla11 = tk.Label(frame,text=f'{dados['acidentes']}',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        sla11.grid(row=11, column=8, padx=10, pady=5,sticky= 'nsew')

        sla12 = tk.Label(frame,text=f'{dados['calculo']}',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        sla12.grid(row=12, column=8, padx=10, pady=5,sticky= 'nsew')
        
        #=======
        sla13 = tk.Label(frame,text=f'{dados['inteligencia']}',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        sla13.grid(row=13, column=8, padx=10, pady=5,sticky= 'nsew')

        sla14 = tk.Label(frame,text=f'{dados['digital']}',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        sla14.grid(row=14, column=8, padx=10, pady=5,sticky= 'nsew',)

        sla15 = tk.Label(frame,text=f'{dados['infraestrutura']}',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        sla15.grid(row=15, column=8, padx=10, pady=5,sticky= 'nsew')

        sla16 = tk.Label(frame,text=f'{dados['abertos']}',font=("Arial Bold", 20,'bold'),background='#ffffff',fg='#000000')
        sla16.grid(row=16, column=8, padx=10, pady=5,sticky= 'nsew')

        #coluna 10  ==============================================
        
        dimensao_valor = tk.Label(frame,text=f'{(g1 + g2 + g3 + g4) * 0.34 } ',font=("Arial Bold", 20,'bold'),background='#4287f5',fg='#000000',)
        dimensao_valor.grid(row=1, column=10, padx=10, pady=5,sticky= 'nsew',rowspan=4)
        
        #=======
      

        dimensao_valor2 = tk.Label(frame,text=f'{(g5 + g6 + g7 + g8)*0.30}',font=("Arial Bold", 20,'bold'),background='#de00e6',fg='#000000',)
        dimensao_valor2.grid(row=5, column=10, padx=10, pady=5,sticky= 'nsew',rowspan=4)

        #=======


        dimensao_valor3 = tk.Label(frame,text=f'{(g9 + g10 + g11 +g12)*0.16}',font=("Arial Bold", 20,'bold'),background='#05c9f5')
        dimensao_valor3.grid(row=9, column=10, padx=10, pady=5,sticky= 'nsew',rowspan=4,)
        #=======


        dimensao_valor4 = tk.Label(frame,text=f'{(g13 + g14 + g15 +g16)*0.22}',font=("Arial Bold", 20,'bold'),background='#05c915')
        dimensao_valor4.grid(row=13, column=10, padx=10, pady=5,sticky= 'nsew',rowspan=4,)


        #coluna 11 =============================

        dimensao_valor = tk.Label(frame,text=f'{g1 + g2 + g3 + g4 + g5 + g6 + g7 +g8 + g9 + g10 + g11 +g12 + g13 + g14 + g15 +g16}',font=("Arial Bold", 20,'bold'),background='#fcba03',fg='#000000',)
        dimensao_valor.grid(row=1, column=11, padx=10, pady=5,sticky= 'nsew',rowspan=16)


        #scrollbar
        scrollbar_x = tk.Scrollbar(janela_final, orient="horizontal", command=canvas.xview)
        scrollbar_x.grid(row=1, column=0, sticky="ew")
        canvas.config(xscrollcommand=scrollbar_x.set)
        
        scrollbar_y = tk.Scrollbar(janela_final, orient="vertical", command=canvas.yview)
        scrollbar_y.grid(row=0, column=1, sticky="ns")
        canvas.config(yscrollcommand=scrollbar_y.set)
        
        frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
        
        
        janela_final.mainloop()





def verificacao():
    print('rodando')
    x = 0
    for i in dados:
        x += 1
    print(x)
    if x == 16:
        janela_final()
    root.after(1000,verificacao)
    print(dados)

root.after(1000,verificacao)
root.mainloop()
