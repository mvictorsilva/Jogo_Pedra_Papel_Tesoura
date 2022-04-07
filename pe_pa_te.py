from tkinter import *
import random


tela_inicial = Tk()
gif = [PhotoImage(file='imagens/tre.gif', format='gif -index %i' % i) for i in range(145)]


def update(ind):
    frame = gif[ind]
    ind += 1
    pe_pa_te.configure(image=frame)
    tela_inicial.after(145, update, ind)


def jogo():
    global link
    tela_inicial.destroy()
    tela_do_jogo = Tk()
    tela_do_jogo.config(background='black')
    tela_do_jogo.geometry('600x550')
    tela_do_jogo.title('PE_PA_TE')
    img_one = PhotoImage(master=tela_do_jogo, file='imagens/pedra.png')
    img_two = PhotoImage(master=tela_do_jogo, file='imagens/papel.png')
    img_three = PhotoImage(master=tela_do_jogo, file='imagens/tesoura.png')

    def pedra():
        pc = random.randint(0, 2)
        if pc == 0:
            pedra_one = Label(tela_do_jogo, font=('Helvetica', 30),
                              text='Empate :/',
                              bg='black',
                              fg='white')
            pedra_one.place(x=220,
                            y=70
                            )
        elif pc == 1:
            pedra_two = Label(tela_do_jogo, font=('Helvetica', 30),
                              text='Você perdeu :(',
                              bg='black',
                              fg='white')
            pedra_two.place(x=200,
                            y=70
                            )
        else:
            pedra_three = Label(tela_do_jogo, font=('Helvetica', 30),
                                text='Você ganhou :)',
                                bg='black',
                                fg='white')
            pedra_three.place(x=200,
                              y=70
                              )

    pedra_img = Button(tela_do_jogo,
                       command=pedra,
                       image=img_one)
    pedra_img.grid()
    pedra_img.place(x=20,
                    y=230
                    )

    def papel():
        pc = random.randint(0, 2)
        if pc == 0:
            papel_one = Label(tela_do_jogo, font=('Helvetica', 30),
                              text='Você ganhou :)',
                              bg='black',
                              fg='white')
            papel_one.place(x=200,
                            y=70
                            )
        elif pc == 1:
            papel_two = Label(tela_do_jogo, font=('Helvetica', 30),
                              text='Empate :/',
                              bg='black',
                              fg='white')
            papel_two.place(x=220,
                            y=70
                            )
        else:
            papel_three = Label(tela_do_jogo, font=('Helvetica', 30),
                                text='Você perdeu :(',
                                bg='black',
                                fg='white')
            papel_three.place(x=200,
                              y=70
                              )

    papel_img = Button(tela_do_jogo,
                       command=papel,
                       image=img_two)
    papel_img.place(x=220,
                    y=230
                    )

    def tesoura():
        pc = random.randint(0, 2)
        if pc == 0:
            tesoura_one = Label(tela_do_jogo, font=('Helvetica', 30),
                                text='Você perdeu :(',
                                bg='black',
                                fg='white')
            tesoura_one.place(x=200,
                              y=70
                              )
        elif pc == 1:
            tesoura_two = Label(tela_do_jogo, font=('Helvetica', 30),
                                text='Você ganhou :)',
                                bg='black',
                                fg='white')
            tesoura_two.place(x=200,
                              y=70
                              )
        else:
            tesoura_three = Label(tela_do_jogo, font=('Helvetica', 30),
                                  text='Empate :/',
                                  bg='black',
                                  fg='white')
            tesoura_three.place(x=220,
                                y=70
                                )

    tesoura_img = Button(tela_do_jogo,
                         command=tesoura,
                         image=img_three)
    tesoura_img.place(x=410,
                      y=230
                      )
    sairII = Button(tela_do_jogo, font=('Helvetica', 10),
                    text='Sair',
                    command=quit,
                    bg='black',
                    fg='white')
    sairII.place(x=10,
                 y=10
                 )
    tela_do_jogo.mainloop()


pe_pa_te = Label(tela_inicial)
pe_pa_te.pack()
tela_inicial.after(0, update, 0)
tela_inicial.title('PEDRA-PAPEL-TESOURA')
tela_inicial.geometry('600x550')

iniciar = Button(tela_inicial, font=('Helvetica', 15),
                 command=jogo,
                 activeforeground='beige',
                 activebackground='#345',
                 text='Iniciar!',
                 height=1,
                 width=6)
iniciar.place(x=270,
              y=350,
              )
sairI = Button(tela_inicial, font=('Helvetica', 10),
               text='Sair',
               command=quit,
               activeforeground='beige',
               activebackground='#345',
               fg='orange')
sairI.place(x=540,
            y=500
            )

tela_inicial.mainloop()
