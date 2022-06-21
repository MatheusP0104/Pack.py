import posiciona
from tkinter import *
from packback import *
from time import time

Back = Backend()
Data = Data_Verificar() 
con = Conta()

def Formatar_func(event=None):
    # frame funcionario
    func_senha = en_senha.get().replace('.', '').replace('-', '')[:11]
    func_id = en_func.get()[:6]
    nova_senha = ''
    novo_id = ''
    # frame usuario
    usu_senha = en_cliente_senha.get()[:8]
    cliente_cpf = en_cliente_user.get().replace('.', '').replace('-', '')[:11]
    cpf_novo = ''
    # frame cadastro
    cpf_cnpj = en_cpf_cadas.get().replace('.', '').replace('-', '')[:11]
    data = en_datanasc_cadas.get().replace('/', '')[:8]
    senha = en_senha_cadas.get()[:8]
    co_senha = en_confirma_cadas.get()[:8]
    nova_data = ''
    novo_cpf = ''
    #frame deposito
    quant = en_valor_depo.get()
    quant_novo= ''

    if event.keysym.lower() == 'backspace':
        return
    for numero in range(len(func_senha)):
        if not func_senha[numero].isnumeric():
            continue
        if numero in [2, 5]:
            nova_senha += func_senha[numero] + '.'
        elif numero == 8:
            nova_senha += func_senha[numero] + '-'
        else:
            nova_senha += func_senha[numero]

    for id in range(len(func_id)):
        if not func_id[id].isnumeric():
            continue
        else:
            novo_id += func_id[id]
        
    for numero_c in range(len(cliente_cpf)):
        if not cliente_cpf[numero_c].isnumeric():
            continue
        if numero_c in [2, 5]:
            cpf_novo += cliente_cpf[numero_c] + '.'
        elif numero_c == 8:
            cpf_novo += cliente_cpf[numero_c] + '-'
        else:
            cpf_novo += cliente_cpf[numero_c]

    for num in range(len(data)):
        if not data[num].isnumeric():
            continue
        if num in [1, 3]:
            nova_data += data[num] + '/'
        else:
            nova_data += data[num]

    for cpf_num in range(len(cpf_cnpj)):
        if not cpf_cnpj[cpf_num].isnumeric():
            continue
        if cpf_num in [2, 5]:
            novo_cpf += cpf_cnpj[cpf_num] + '.'
        elif cpf_num == 8:
            novo_cpf += cpf_cnpj[cpf_num] + '-'
        else:
            novo_cpf += cpf_cnpj[cpf_num]

    if not quant.isnumeric():
        pass
    else:
        quant_novo += quant    

    # deletes
    en_senha.delete(0, 'end')
    en_func.delete(0, 'end')
    en_cliente_user.delete(0, 'end')
    en_cliente_senha.delete(0, 'end')
    en_datanasc_cadas.delete(0, 'end')
    en_cpf_cadas.delete(0, 'end')
    en_senha_cadas.delete(0, 'end')
    en_confirma_cadas.delete(0, 'end')
    en_valor_depo.delete(0, 'end')
    # inserts
    en_senha.insert(0, nova_senha)
    en_func.insert(0, func_id)
    en_cliente_user.insert(0, cpf_novo)
    en_cliente_senha.insert(0, usu_senha)
    en_datanasc_cadas.insert(0, nova_data)
    en_cpf_cadas.insert(0, novo_cpf)
    en_senha_cadas.insert(0, senha)
    en_confirma_cadas.insert(0, co_senha)
    en_valor_depo.insert(0, quant_novo)

branco = '#ffffff'
azul_esc = '#00357b'
preto = '#0F0F10'
nominho = ''
# ==============================================================================================================
# janela principal
janela = Tk()
janela.geometry('500x500')
janela.resizable(False, False)
janela.title('PackPy')

janela.bind('<Button-1>', posiciona.inicio_place)
janela.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, janela))
janela.bind('<Button-2>', lambda arg: posiciona.para_geometry(janela))

janela.bind('<KeyRelease>', Formatar_func)
# ==============================================================================================================
# frames de cada tela
frame_i = Frame(janela)
frame_entrar = Frame(janela)
frame_func = Frame(janela)
frame_cliente = Frame(janela)
frame_conta = Frame(janela)
frame_cadastro = Frame(janela)
frame_depo = Frame(janela)
# ==============================================================================================================
# carrega os primeiros frames
frame_i.pack()
frame_entrar.pack()
# ==============================================================================================================
# variaveis para todas as imagens usadas
seta_voltar = PhotoImage(file='Foto/seta voltar.png')
inicio = PhotoImage(file='Foto/inicio.png')
entrar = PhotoImage(file='Foto/entrar.png')
func = PhotoImage(file='Foto/func.png')
cadastro = PhotoImage(file='Foto/cadastro.png')
user = PhotoImage(file='Foto/conta cliente.png')
on_image = PhotoImage(file='Foto/olho aberto.png')
off_image = PhotoImage(file='Foto/olho fechado.png')
cliente = PhotoImage(file='Foto/user.png')
depo = PhotoImage(file='Foto/Bt_Depósito.png')
extra = PhotoImage(file='Foto/Bt_Extrato.png')
deposito = PhotoImage(file='Foto/Depósito.png')
# ==============================================================================================================
# primeira tela (mostra a logo)
lb_inicio = Label(frame_i, image=inicio, border=0)
lb_inicio.pack()
# ==============================================================================================================
# tela seleção de login
# labels
lb_entrar = Label(frame_entrar, image=entrar, border=0)
# botões
bt_func = Button(frame_entrar, text='FAZER LOGIN', bg=branco, font='arial 15 bold', bd=0,
                 command=lambda: [frame_cliente.pack(), frame_entrar.forget(), frame_func.forget()])
bt_cli = Button(frame_entrar, text='LOGIN (FUNC)', bg=branco, font='arial 15 bold', bd=0,
                command=lambda: [frame_func.pack(), frame_entrar.forget(), frame_cliente.forget()])
# posicionamento na tela
lb_entrar.pack()
bt_func.place(width=155, height=42, x=247, y=146)
bt_cli.place(width=157, height=47, x=251, y=354)
# ==============================================================================================================
# tela funcionário
# labels
lb_func = Label(frame_func, image=func, border=0)
# Entry's
en_func = Entry(frame_func, font='arial 12 bold', bd=0, fg=branco, bg=azul_esc)
en_senha = Entry(frame_func, font='arial 12 bold', bg=azul_esc, bd=0, fg=branco, show='*')
# botões
bt_voltar_func = Button(frame_func, image=seta_voltar, bg=azul_esc, bd=0, activebackground=azul_esc,
                        command=lambda: [frame_entrar.pack(), frame_func.forget()])
bt_entrar_func = Button(frame_func, text='Entrar', font='arial 13 bold', bg=branco, bd=0)
bt_entrar_func.config(command=lambda: Back.Entrar_func(en_func.get(), en_senha.get(), frame_cadastro, frame_func))
# checks
check_senha_func = Checkbutton(frame_func, bg=azul_esc, image=on_image, selectimage=off_image, indicatoron=False, bd=0,
                               command=lambda: Back.Mostrar_senha(en_senha))
# posicionamento na tela
lb_func.pack()
bt_entrar_func.place(width=70, height=33, x=381, y=443)
en_senha.place(width=293, height=22, x=25, y=180)
bt_voltar_func.place(width=38, height=36, x=2, y=9)
en_func.place(width=293, height=23, x=24, y=122)
check_senha_func.place(width=30, height=22, x=290, y=170)
# ==============================================================================================================
# tela cadastro
# labels
lb_cada = Label(frame_cadastro, image=cadastro, border=0)
# Entry's
en_nome_co = Entry(frame_cadastro, font='Arial 10 bold', bg=branco, border=0, fg=preto)
en_cpf_cadas = Entry(frame_cadastro, font='Arial 10 bold', bg=branco, border=0, fg=preto)
en_datanasc_cadas = Entry(frame_cadastro, font='Arial 10 bold', bg=branco, border=0, fg=preto)
en_email_cadas = Entry(frame_cadastro, font='Arial 10 bold', bg=branco, border=0, fg=preto)
en_senha_cadas = Entry(frame_cadastro, font='Arial 10 bold', bg=branco, border=0, fg=preto, show='*')
en_confirma_cadas = Entry(frame_cadastro, font='Arial 10 bold', bg=branco, border=0, fg=preto, show='*')
# botões
bt_voltar_cadas = Button(frame_cadastro, image=seta_voltar, bg=azul_esc, bd=0, activebackground=azul_esc,
                         command=lambda: [frame_func.pack(), frame_cadastro.forget()])
bt_cadastro = Button(frame_cadastro, text='CADASTRAR', font='Arial 15 bold ', bg=azul_esc, fg=branco,
                     command=lambda: Back.Cadastrar(en_cpf_cadas, en_nome_co, en_datanasc_cadas, en_email_cadas,
                                                    en_senha_cadas, en_confirma_cadas, check_m, check_f, check_ac,
                                                    check_email, frame_func, frame_cadastro))
# check buttons
check_m = Checkbutton(frame_cadastro, bg=azul_esc, command=lambda: check_f.deselect())
check_f = Checkbutton(frame_cadastro, bg=azul_esc, command=lambda: check_m.deselect())
check_ac = Checkbutton(frame_cadastro, bg=azul_esc)
check_email = Checkbutton(frame_cadastro, bg=azul_esc)
# posionamento na tela
lb_cada.pack()
en_nome_co.place(width=220, height=24, x=10, y=87)
en_cpf_cadas.place(width=220, height=24, x=10, y=142)
en_datanasc_cadas.place(width=220, height=24, x=10, y=200)
en_email_cadas.place(width=220, height=24, x=266, y=91)
en_senha_cadas.place(width=220, height=24, x=266, y=144)
en_confirma_cadas.place(width=220, height=24, x=266, y=197)
bt_voltar_cadas.place(width=38, height=36, x=2, y=9)
bt_cadastro.place(width=160, height=55, x=286, y=287)
check_m.place(width=7, height=6, x=13, y=270)
check_f.place(width=6, height=7, x=113, y=268)
check_ac.place(width=6, height=4, x=263, y=243)
check_email.place(width=8, height=9, x=263, y=265)
# ==============================================================================================================
# tela conta
# labels
lb_user = Label(frame_conta, image=user, border=0)
lb_nome_user = Label(frame_conta, textvariable=nominho, font='Arial 15 bold', bg=azul_esc, fg=branco, bd=0)
lb_saldo = Label(frame_conta, text='0', font='Arial 10 bold', bg=azul_esc, fg=branco, bd=0)
# botoes
bt_voltar_conta = Button(frame_conta, image=seta_voltar, bg=azul_esc, bd=0, activebackground=azul_esc,
                         command=lambda: [frame_cliente.pack(), frame_conta.forget()])
bt_deposito = Button(frame_conta, image=depo, bd=0, activebackground=azul_esc, command=lambda: [frame_depo.pack(), frame_conta.forget()])
bt_extrato = Button(frame_conta, image=extra, bd=0, activebackground=azul_esc)
# check_buttons
check_saldo = Checkbutton(frame_conta, bg=azul_esc, image=on_image, selectimage=off_image, indicatoron=False, bd=0)
# posionamento na tela
lb_user.pack()
bt_voltar_conta.place(width=38, height=36, x=2, y=9)
bt_deposito.place(width=155, height=68, x=183, y=204)
bt_extrato.place(width=144, height=37, x=297, y=93)
check_saldo.place(width=30, height=22, x=175, y=130)
lb_nome_user.place(width=60, height=18, x=111, y=65)
lb_saldo.place(width=25, height=11, x=74, y=129)
# ==============================================================================================================
# tela cliente login
# labels
lb_cliente = Label(frame_cliente, image=cliente, border=0)
# Entry's
en_cliente_user = Entry(frame_cliente, font='arial 12 bold', bg=branco, border=0, fg=preto)
en_cliente_senha = Entry(frame_cliente, font='arial 12 bold', bg=branco, border=0, fg=preto, show='*')
# botões
bt_voltar_cliente = Button(frame_cliente, image=seta_voltar, bg=azul_esc, bd=0, activebackground=azul_esc,
                           command=lambda: [frame_entrar.pack(), frame_cliente.forget()])
bt_entrar_cliente = Button(frame_cliente, text='Entrar', bg=azul_esc, font='arial 19 bold', bd=0, fg=branco,
                           command=lambda: [Back.Entrar_cli(en_cliente_user.get(), en_cliente_senha.get(), frame_conta,
                                                            frame_entrar, frame_cliente),con.Mostrar(en_cliente_user.get(), nominho)])
# checks
check_senha_us = Checkbutton(frame_cliente, bg=branco, image=on_image, selectimage=off_image, indicatoron=False, bd=0,
                             command=lambda: Back.Mostrar_senha(en_cliente_senha))
# posionamento na tela
lb_cliente.pack()
en_cliente_user.place(width=217, height=19, x=139, y=160)
en_cliente_senha.place(width=219, height=17, x=137, y=228)
bt_voltar_cliente.place(width=38, height=36, x=2, y=9)
bt_entrar_cliente.place(width=215, height=46, x=141, y=337)
check_senha_us.place(width=30, height=22, x=335, y=228)
# ==============================================================================================================
# tela deposito
lb_depo = Label(frame_depo, image=deposito, border=0)
lb_depo.pack()
en_valor_depo = Entry(frame_depo, font='arial 12 bold', bd=0, fg=azul_esc, bg=branco)
bt_confirma = Button(frame_depo, text='confirmar', bd=0, bg=azul_esc, fg=branco, font='arial 19 bold', command=lambda:con.atualizar(en_cliente_user.get(), en_valor_depo.get()))
bt_voltar_deposito = Button(frame_depo, image=seta_voltar, bg=azul_esc, bd=0, activebackground=azul_esc,
                           command=lambda: [frame_conta.pack(), frame_depo.forget()])
en_valor_depo.place(width=216, height=17, x=140, y=157)
bt_confirma.place(width=208, height=39, x=143, y=281)
bt_voltar_deposito.place(width=38, height=36, x=2, y=9)
# ==============================================================================================================
# loop da janela e outros
janela.after(1000, frame_i.forget)

janela.mainloop()
Data.Close()
con.Close()