from tkinter import *
from random import randint

class AtorJogador:
    def __criaFrame(self, root, padx=0, pady=0, **kwargs):
        frame = Frame(root, **kwargs)
        frame.pack(padx=padx, pady=pady)
        frame.pack_propagate(0)
        return frame

    def __criaLabel(self, frame, padding=0, side='top', **kwargs):
        label = Label(frame, **kwargs)
        label.pack(pady=padding, side=side)
        return label
    
    def __fonte(self, tamanho):
        return ('Helvetica Neue', tamanho)

    def __init__(self):
        self.janela_principal = Tk()
        self.janela_principal.title("Wordle Versus")
        self.janela_principal.geometry("900x900")
        self.janela_principal.resizable(False, False)
        self.janela_principal["bg"] = "gray"

        height, width = 1000, 1000

        self.frame_titulo = self.__criaFrame(self.janela_principal, height=0.75*height/10, width=width, bg='gray')
        self.frame_jogo = self.__criaFrame(self.janela_principal, height=6.25*height/10, width=width, bg='gray')
        self.frame_mensagens = self.__criaFrame(self.janela_principal, height=3*height/10, width=width, bg='gray')
        
        self.transparente = PhotoImage(file="images/transparente.png")
        cinza = PhotoImage(file="images/cinza.png")
        verde = PhotoImage(file="images/verde.png")
        amarelo = PhotoImage(file="images/amarelo.png")
        self.imagens = [cinza, verde, amarelo]
        
        self.__criaLabel(self.frame_titulo, 20, text='Wordle Versus', font=self.__fonte(25))
        
        self.letras = []
        self.counter = 0
        for y in range(6):
            corJogador = 'grey'
            if y < 2:
                corJogador = 'blue' if y % 2 == 0 else 'red'
            frame_chance = self.__criaFrame(self.frame_jogo, pady=3, height=(7*height/10)/6, width=6*width/10, bg=corJogador)
            for x in range(5):
                if y == 0:
                    letra = Label(frame_chance, text='A', font=self.__fonte(30), compound='center', relief='solid', image=self.imagens[randint(0, 2)])
                else:
                    letra = Label(frame_chance, text=' ', font=self.__fonte(30), compound='center', relief='solid', image=self.transparente)
                letra.grid(row=0, column=x, padx=2, pady=8)
                if y == 1:
                    self.frame_chance = frame_chance
                    self.letras.append(letra)

        self.frame_instrucoes = self.__criaFrame(self.frame_mensagens, height=3*(3*height/10)/10, width=width, bg='gray')
        self.frame_jogador = self.__criaFrame(self.frame_mensagens, height=2*(3*height/10)/10, width=width, bg='gray')
        self.frame_reset = self.__criaFrame(self.frame_mensagens, height=3*(3*height/10)/10, width=width, bg='gray')
        self.__criaLabel(self.frame_instrucoes, side='left', text="Pressione . para passar seu turno", font=self.__fonte(14))
        self.__criaLabel(self.frame_instrucoes, side='right', text="Pressione ENTER para submeter sua tentativa", font=self.__fonte(14))
        self.__criaLabel(self.frame_jogador, text='Jogador 1, é a sua vez!', font=self.__fonte(20))
        self.__criaLabel(self.frame_reset, text="Pressione CTRL para reiniciar o jogo", font=self.__fonte(14))
        
        self.janela_principal.bind('<Return>', lambda event: self.onEnterPress(event))
        self.janela_principal.bind('<Control_L>', lambda event: self.onCtrlPress(event))
        self.janela_principal.bind('.', lambda event: self.onDotPress(event))
        self.janela_principal.bind('<Key>', lambda event: self.onKeyPress(event))
        
        self.janela_principal.mainloop()

    def onEnterPress(self, event):
        for letra in self.letras:
            imagem = self.imagens[randint(0,2)]
            letra.configure(image=imagem)
            letra.image = imagem

    def onCtrlPress(self, event):
        for letra in self.letras:
            imagem = self.transparente
            letra.configure(image=imagem)
            letra.image = imagem

    def onDotPress(self, event):
        self.counter += 1
        corJogador = 'red' if self.counter % 2 == 0 else 'blue'
        self.frame_chance.configure(bg=corJogador)
        self.frame_chance.bg = corJogador

    def onKeyPress(self, event):
        if event.char:
            for letra in self.letras:
                letra.configure(text=event.char, font=self.__fonte(30), compound='center')

AtorJogador()