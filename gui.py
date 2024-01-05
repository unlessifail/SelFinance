import customtkinter as ctk
from PIL import Image

def criar_exibir_extrato(parent):
    janela_exibir_extrato = ctk.CTkToplevel(parent)
    janela_exibir_extrato.title('SelFinance | Ver Extrato')
    janela_exibir_extrato.geometry('350x720')
    janela_exibir_extrato.attributes('-topmost', True)
    janela_exibir_extrato.resizable(False, False)

    exibir_extrato_main_Frame = ctk.CTkFrame(janela_exibir_extrato,
                                            width=350,
                                            height=720,
                                            fg_color="#7C7C7C",
                                            bg_color="#7C7C7C",
                                            corner_radius=0,
                                            )
    exibir_extrato_main_Frame.place(x=0,y=0)

    exibir_extrato_headerLabel = ctk.CTkLabel(janela_exibir_extrato,
                                    text='Extrato:',
                                    text_color='#242424',
                                    font=('Arial', 30),
                                    bg_color='#7C7C7C',
                                    )

    exibir_extrato_headerLabel.place(x=10,y=10)

    exibir_extrato_AuxFrame = ctk.CTkFrame(janela_exibir_extrato,
                                    width=332,
                                    height=663,
                                    fg_color="#A7A7A7",
                                    bg_color="#7C7C7C",
                                    corner_radius=15,
                                    )
    exibir_extrato_AuxFrame.place(x=10,y=47)

    linha1_extratoLabel = ctk.CTkLabel(janela_exibir_extrato,
                                    text='Data: 04/01/2024\nCategoria: Despesa\nDescrição: Comprar cigarro\nValor: R$ 10,50',
                                    text_color="#242424",
                                    bg_color="#A7A7A7",
                                    )
    linha1_extratoLabel.place(x=100,y=57)

def criar_add_receita_janela(parent):
    janela_add_receita = ctk.CTkToplevel(parent)
    janela_add_receita.title('SelFinance | Adicionar Receita')
    janela_add_receita.geometry('600x218')
    janela_add_receita.attributes('-topmost', True)
    janela_add_receita.resizable(False, False)

    addreceita_main_Frame = ctk.CTkFrame(janela_add_receita,
                                            width=600,
                                            height=218,
                                            fg_color="#7C7C7C",
                                            bg_color="#7C7C7C",
                                            corner_radius=0,
                                            )
    addreceita_main_Frame.place(x=0,y=0)

    addreceita_headerLabel = ctk.CTkLabel(janela_add_receita,
                                    text='Adicionar Receita',
                                    text_color='#242424',
                                    font=('Arial', 30),
                                    bg_color='#7C7C7C',
                                    )

    addreceita_headerLabel.place(x=10,y=10)

    addreceita_AuxFrame = ctk.CTkFrame(janela_add_receita,
                                    width=580,
                                    height=156,
                                    fg_color="#A7A7A7",
                                    bg_color="#7C7C7C",
                                    corner_radius=15,
                                    )
    addreceita_AuxFrame.place(x=10,y=52)

    addreceita_descLabel = ctk.CTkLabel(janela_add_receita,
                                    text='Descrição:',
                                    text_color='#242424',
                                    font=('Arial', 15),
                                    bg_color='#A7A7A7',
                                    )
    addreceita_descLabel.place(x=20,y=74)

    addreceita_descEntry = ctk.CTkEntry(janela_add_receita,
                                        width=286,
                                        height=33,
                                        fg_color='#CCCCCC',
                                        bg_color='#A7A7A7',
                                        corner_radius=5,
                                        border_width=0,
                                        )

    addreceita_descEntry.place(x=20,y=100)

    addreceita_valorLabel = ctk.CTkLabel(janela_add_receita,
                                    text='Valor:',
                                    text_color='#242424',
                                    font=('Arial', 15),
                                    bg_color='#A7A7A7',
                                    )
    addreceita_valorLabel.place(x=326,y=74)

    addreceita_valorEntry = ctk.CTkEntry(janela_add_receita,
                                        width=254,
                                        height=33,
                                        fg_color='#CCCCCC',
                                        bg_color='#A7A7A7',
                                        corner_radius=5,
                                        border_width=0,
                                        )

    addreceita_valorEntry.place(x=326,y=100)

    addreceita_dataLabel = ctk.CTkLabel(janela_add_receita,
                                    text='Data:',
                                    text_color='#242424',
                                    font=('Arial', 15),
                                    bg_color='#A7A7A7',
                                    )
    addreceita_dataLabel.place(x=20,y=139)

    addreceita_dataEntry = ctk.CTkEntry(janela_add_receita,
                                        width=150,
                                        height=33,
                                        fg_color='#CCCCCC',
                                        bg_color='#A7A7A7',
                                        corner_radius=5,
                                        border_width=0,
                                        )
    addreceita_dataEntry.place(x=20,y=165)

    addreceita_AddButton = ctk.CTkButton(janela_add_receita,
                                        width=150,
                                        height=33,
                                        text='Adicionar',
                                        text_color='#FFFFFF',
                                        fg_color="#23973D",
                                        hover_color="#33C854",
                                        bg_color="#A7A7A7",
                                        corner_radius=5,
                                        )
    addreceita_AddButton.place(x=430,y=165)

def criar_add_despesa_janela(parent):
    janela_add_despesa = ctk.CTkToplevel(parent)
    janela_add_despesa.title('SelFinance | Adicionar Despesa')
    janela_add_despesa.geometry('600x218')
    janela_add_despesa.attributes('-topmost', True)
    janela_add_despesa.resizable(False, False)

    adddespesa_main_Frame = ctk.CTkFrame(janela_add_despesa,
                                            width=600,
                                            height=218,
                                            fg_color="#7C7C7C",
                                            bg_color="#7C7C7C",
                                            corner_radius=0,
                                            )
    adddespesa_main_Frame.place(x=0,y=0)

    adddespesa_headerLabel = ctk.CTkLabel(janela_add_despesa,
                                    text='Adicionar Despesa',
                                    text_color='#242424',
                                    font=('Arial', 30),
                                    bg_color='#7C7C7C',
                                    )

    adddespesa_headerLabel.place(x=10,y=10)

    adddespesa_AuxFrame = ctk.CTkFrame(janela_add_despesa,
                                    width=580,
                                    height=156,
                                    fg_color="#A7A7A7",
                                    bg_color="#7C7C7C",
                                    corner_radius=15,
                                    )
    adddespesa_AuxFrame.place(x=10,y=52)

    adddespesa_descLabel = ctk.CTkLabel(janela_add_despesa,
                                    text='Descrição:',
                                    text_color='#242424',
                                    font=('Arial', 15),
                                    bg_color='#A7A7A7',
                                    )
    adddespesa_descLabel.place(x=20,y=74)

    adddespesa_descEntry = ctk.CTkEntry(janela_add_despesa,
                                        width=286,
                                        height=33,
                                        fg_color='#CCCCCC',
                                        bg_color='#A7A7A7',
                                        corner_radius=5,
                                        border_width=0,
                                        )

    adddespesa_descEntry.place(x=20,y=100)

    adddespesa_valorLabel = ctk.CTkLabel(janela_add_despesa,
                                    text='Valor:',
                                    text_color='#242424',
                                    font=('Arial', 15),
                                    bg_color='#A7A7A7',
                                    )
    adddespesa_valorLabel.place(x=326,y=74)

    adddespesa_valorEntry = ctk.CTkEntry(janela_add_despesa,
                                        width=254,
                                        height=33,
                                        fg_color='#CCCCCC',
                                        bg_color='#A7A7A7',
                                        corner_radius=5,
                                        border_width=0,
                                        )

    adddespesa_valorEntry.place(x=326,y=100)

    adddespesa_dataLabel = ctk.CTkLabel(janela_add_despesa,
                                    text='Data:',
                                    text_color='#242424',
                                    font=('Arial', 15),
                                    bg_color='#A7A7A7',
                                    )
    adddespesa_dataLabel.place(x=20,y=139)

    adddespesa_dataEntry = ctk.CTkEntry(janela_add_despesa,
                                        width=150,
                                        height=33,
                                        fg_color='#CCCCCC',
                                        bg_color='#A7A7A7',
                                        corner_radius=5,
                                        border_width=0,
                                        )
    adddespesa_dataEntry.place(x=20,y=165)

    adddespesa_AddButton = ctk.CTkButton(janela_add_despesa,
                                        width=150,
                                        height=33,
                                        text='Adicionar',
                                        text_color='#FFFFFF',
                                        fg_color="#23973D",
                                        hover_color="#33C854",
                                        bg_color="#A7A7A7",
                                        corner_radius=5,
                                        )
    adddespesa_AddButton.place(x=430,y=165)

def criar_left_side_menu_bar(parent):
    leftSideMenuFrame = ctk.CTkFrame(parent,
                                   width=280,
                                   height=690,
                                   corner_radius=0,
                                   fg_color="#7C7C7C",
                                   bg_color="#242424",
                                   )
    leftSideMenuFrame.place(x=0, y=170)

    padraoUserPic = ctk.CTkImage(dark_image=Image.open(r"assets\icons\user.png"),
                                size=(190,190),
                                )

    usuarioPicLabel = ctk.CTkLabel(parent,
                              text='',
                              image=padraoUserPic,
                              fg_color="#7C7C7C",
                              bg_color="#7C7C7C",
                              )
    usuarioPicLabel.place(x=40, y=190)

    usuarioNomeLabel = ctk.CTkLabel(parent,
                              text='Nome do Usuário',
                              text_color="#FFFFFF",
                              font=('Arial', 30),
                              bg_color="#7C7C7C",
                              )    
    usuarioNomeLabel.place(x=20,y=390)

    linhaBrancaFrame = ctk.CTkFrame(parent,
                              width=240,
                              height=2,
                              corner_radius=100,
                              fg_color="#FFFFFF",
                              bg_color="#7C7C7C",
                              )    
    linhaBrancaFrame.place(x=20, y=445)

    btnAddReceita = ctk.CTkButton(parent,
                                  width=110,
                                  height=33,
                                  text='Receita +',
                                  text_color='#FFFFFF',
                                  font=('Arial', 15),
                                  fg_color="#23973D",
                                  bg_color="#7C7C7C",
                                  corner_radius=15,
                                  hover_color="#37C256",
                                  )
    btnAddReceita.place(x=20,y=465)

    btnAddDespesa = ctk.CTkButton(parent,
                                  width=110,
                                  height=33,
                                  text='Despesa +',
                                  text_color='#FFFFFF',
                                  font=('Arial', 15),
                                  fg_color="#972338",
                                  bg_color="#7C7C7C",
                                  corner_radius=15,
                                  hover_color="#CA344F",
                                  )
    btnAddDespesa.place(x=150,y=465)

    btnExtrato = ctk.CTkButton(parent,
                                  width=240,
                                  height=33,
                                  text='Extrato',
                                  text_color='#FFFFFF',
                                  font=('Arial', 15),
                                  fg_color="#1F5B93",
                                  bg_color="#7C7C7C",
                                  corner_radius=15,
                                  hover_color="#2F85D5",
                                  )
    btnExtrato.place(x=20,y=505)

    btnPreferencias = ctk.CTkButton(parent,
                                  width=240,
                                  height=33,
                                  text='Preferências',
                                  text_color='#FFFFFF',
                                  font=('Arial', 15),
                                  fg_color="#242424",
                                  bg_color="#7C7C7C",
                                  corner_radius=15,
                                  hover_color="#343434",
                                  )
    btnPreferencias.place(x=20,y=705)

    btnTemas = ctk.CTkButton(parent,
                                  width=240,
                                  height=33,
                                  text='Temas',
                                  text_color='#FFFFFF',
                                  font=('Arial', 15),
                                  fg_color="#242424",
                                  bg_color="#7C7C7C",
                                  corner_radius=15,
                                  hover_color="#343434",
                                  )
    btnTemas.place(x=20,y=747)

    btnSuporte = ctk.CTkButton(parent,
                                  width=240,
                                  height=33,
                                  text='Suporte',
                                  text_color='#FFFFFF',
                                  font=('Arial', 15),
                                  fg_color="#242424",
                                  bg_color="#7C7C7C",
                                  corner_radius=15,
                                  hover_color="#343434",
                                  )
    btnSuporte.place(x=20,y=788)

def criar_header_logo(parent):
    selfinanceLogoLabelIMG = ctk.CTkImage(dark_image=Image.open(r"assets\icons\logoSelFinance.png"), 
                                          size=(170,170)
                                          )
    selfinanceLogoLabel = ctk.CTkLabel(parent, 
                                       text=None, 
                                       image=selfinanceLogoLabelIMG, 
                                       bg_color="#242424", 
                                       corner_radius=0
                                       )
    selfinanceLogoLabel.place(x=50,y=0)

def criar_saldo_widget(parent):
    saldoFrame = ctk.CTkFrame(parent,
                              width=350,
                              height=80,
                              fg_color="#7C7C7C",
                              bg_color="#242424",
                              corner_radius=10
                              )
    saldoFrame.place(x=290,y=10)

    saldoLabel = ctk.CTkLabel(parent,
                              text='Saldo:',
                              text_color='#FFFFFF',
                              font=('Arial', 20),
                              bg_color="#7C7C7C",                              
                              )
    saldoLabel.place(x=300,y=18)

    saldoValorLabel = ctk.CTkLabel(parent,
                              text='R$ 0,00',
                              text_color='#FFFFFF',
                              font=('Arial', 20),
                              bg_color="#7C7C7C",                              
                              )
    saldoValorLabel.place(x=300,y=60)

    saldoIconeFrame = ctk.CTkFrame(parent,
                              width=60,
                              height=80,
                              fg_color="#CACD26",
                              bg_color="#7C7C7C",
                              corner_radius=0
                              )
    saldoIconeFrame.place(x=580,y=10)

    saldoIconeIMG = ctk.CTkImage(dark_image=Image.open(r"assets\icons\saldo.png"), 
                                          size=(35,35)
                                          )
    saldoIconeLabel = ctk.CTkLabel(parent, 
                                       text=None, 
                                       image=saldoIconeIMG, 
                                       bg_color="#CACD26", 
                                       corner_radius=0
                                       )
    saldoIconeLabel.place(x=591,y=32)

def criar_receita_widget(parent):
    receitaFrame = ctk.CTkFrame(parent,
                              width=350,
                              height=80,
                              fg_color="#7C7C7C",
                              bg_color="#242424",
                              corner_radius=10
                              )
    receitaFrame.place(x=685,y=10)

    receitaLabel = ctk.CTkLabel(parent,
                              text='Receita:',
                              text_color='#FFFFFF',
                              font=('Arial', 20),
                              bg_color="#7C7C7C",                              
                              )
    receitaLabel.place(x=695,y=18)

    receitaValorLabel = ctk.CTkLabel(parent,
                              text='R$ 0,00',
                              text_color='#FFFFFF',
                              font=('Arial', 20),
                              bg_color="#7C7C7C",                              
                              )
    receitaValorLabel.place(x=695,y=60)

    receitaIconeFrame = ctk.CTkFrame(parent,
                              width=60,
                              height=80,
                              fg_color="#23973D",
                              bg_color="#7C7C7C",
                              corner_radius=0
                              )
    receitaIconeFrame.place(x=975,y=10)

    receitaIconeIMG = ctk.CTkImage(dark_image=Image.open(r"assets\icons\receita.png"), 
                                          size=(35,35)
                                          )
    receitaIconeLabel = ctk.CTkLabel(parent, 
                                       text=None, 
                                       image=receitaIconeIMG, 
                                       bg_color="#23973D", 
                                       corner_radius=0
                                       )
    receitaIconeLabel.place(x=986,y=32)

def criar_despesa_widget(parent):
    despesaFrame = ctk.CTkFrame(parent,
                              width=350,
                              height=80,
                              fg_color="#7C7C7C",
                              bg_color="#242424",
                              corner_radius=10
                              )
    despesaFrame.place(x=1080,y=10)

    despesaLabel = ctk.CTkLabel(parent,
                              text='Despesas:',
                              text_color='#FFFFFF',
                              font=('Arial', 20),
                              bg_color="#7C7C7C",                              
                              )
    despesaLabel.place(x=1090,y=18)

    despesaValorLabel = ctk.CTkLabel(parent,
                              text='R$ 0,00',
                              text_color='#FFFFFF',
                              font=('Arial', 20),
                              bg_color="#7C7C7C",                              
                              )
    despesaValorLabel.place(x=1090,y=60)

    despesaIconeFrame = ctk.CTkFrame(parent,
                              width=60,
                              height=80,
                              fg_color="#972338",
                              bg_color="#7C7C7C",
                              corner_radius=0
                              )
    despesaIconeFrame.place(x=1370,y=10)

    despesaIconeIMG = ctk.CTkImage(dark_image=Image.open(r"assets\icons\despesa.png"), 
                                          size=(35,35)
                                          )
    despesaIconeLabel = ctk.CTkLabel(parent, 
                                       text=None, 
                                       image=despesaIconeIMG, 
                                       bg_color="#972338", 
                                       corner_radius=0
                                       )
    despesaIconeLabel.place(x=1383,y=32)

def criar_detalhes_mov_widget(parent):
    janela_detalhes_mov = ctk.CTkToplevel(parent)
    janela_detalhes_mov.title('SelFinance | Detalhes')
    janela_detalhes_mov.geometry('350x165')
    janela_detalhes_mov.attributes('-topmost', True)
    janela_detalhes_mov.resizable(False, False)

    detalhesMainFrame = ctk.CTkFrame(janela_detalhes_mov,
                                        width=355,
                                        height=165,
                                        fg_color="#7C7C7C",
                                        bg_color="#7C7C7C",
                                        corner_radius=0,
                                        )
    detalhesMainFrame.place(x=0,y=0)

    detalhesAuxFrame = ctk.CTkFrame(janela_detalhes_mov,
                                        width=340,
                                        height=110,
                                        fg_color="#A7A7A7",
                                        bg_color="#7C7C7C",
                                        corner_radius=15,
                                        )
    detalhesAuxFrame.place(x=5,y=50)

    det_mov_headerLabel = ctk.CTkLabel(janela_detalhes_mov,
                                    text='Detalhes da Movimentação:',
                                    text_color='#242424',
                                    font=('Arial', 20),
                                    bg_color='#7C7C7C',
                                    )

    det_mov_headerLabel.place(x=5,y=10)

    categoria_det_movLabel = ctk.CTkLabel(janela_detalhes_mov,
                                        text='Categoria:',
                                        text_color='#242424',
                                        font=('Arial', 15),
                                        bg_color='#A7A7A7',
                                        )
    categoria_det_movLabel.place(x=15,y=55)

    valor_det_movLabel = ctk.CTkLabel(janela_detalhes_mov,
                                        text='Valor:',
                                        text_color='#242424',
                                        font=('Arial', 15),
                                        bg_color='#A7A7A7',
                                        )
    valor_det_movLabel.place(x=15,y=80)

    data_det_movLabel = ctk.CTkLabel(janela_detalhes_mov,
                                        text='Data:',
                                        text_color='#242424',
                                        font=('Arial', 15),
                                        bg_color='#A7A7A7',
                                        )
    data_det_movLabel.place(x=15,y=105)

    descricao_det_movLabel = ctk.CTkLabel(janela_detalhes_mov,
                                        text='Descricao:',
                                        text_color='#242424',
                                        font=('Arial', 15),
                                        bg_color='#A7A7A7',
                                        )
    descricao_det_movLabel.place(x=15,y=130)

def exibir_detalhes_linha1(parent):
    criar_detalhes_mov_widget(parent)

def criar_ult_mov_widget(parent):
    ultMov_Frame = ctk.CTkFrame(parent,
                              width=350,
                              height=230,
                              fg_color="#7C7C7C",
                              bg_color="#242424",
                              corner_radius=0
                              )
    ultMov_Frame.place(x=290,y=100)

    ultMovLabel = ctk.CTkLabel(parent,
                              text='Últimas Movimentações',
                              text_color='#242424',
                              font=('Arial', 20),
                              bg_color="#7C7C7C",                              
                              )
    ultMovLabel.place(x=300,y=110)

    # Linha 1

    linhaValor1_ultMov_Frame = ctk.CTkFrame(parent,
                              width=210,
                              height=30,
                              fg_color="#D9D9D9",
                              bg_color="#7C7C7C",
                              corner_radius=0
                              )
    linhaValor1_ultMov_Frame.place(x=300,y=150)

    linhaValor1_ultMov_Label = ctk.CTkLabel(parent,
                              text='R$ 0,00 ',
                              text_color='#242424',
                              font=('Arial', 15),
                              bg_color="#D9D9D9",                              
                              )
    linhaValor1_ultMov_Label.place(x=370,y=151)    

    linhaData1_ultMov_Frame = ctk.CTkFrame(parent,
                              width=80,
                              height=30,
                              fg_color="#D9D9D9",
                              bg_color="#7C7C7C",
                              corner_radius=0
                              )
    linhaData1_ultMov_Frame.place(x=518,y=150)

    linhaData1_ultMov_Label = ctk.CTkLabel(parent,
                              text='04/01/2024',
                              text_color='#242424',
                              font=('Arial', 15),
                              bg_color="#D9D9D9",                              
                              )
    linhaData1_ultMov_Label.place(x=521,y=151)   

    btnDetalhesLinha1 = ctk.CTkButton(parent,
                                      text='+',
                                      width=30,
                                      height=30,
                                      fg_color="#242424",
                                      bg_color="#7C7C7C",
                                      hover_color="#3E3E3E",
                                      corner_radius=10,
                                      command=criar_detalhes_mov_widget(parent),
                                      )
    btnDetalhesLinha1.place(x=605, y=150)

    # Linha 2

    linhaValor2_ultMov_Frame = ctk.CTkFrame(parent,
                              width=210,
                              height=30,
                              fg_color="#D9D9D9",
                              bg_color="#7C7C7C",
                              corner_radius=0
                              )
    linhaValor2_ultMov_Frame.place(x=300,y=185)

    linhaValor2_ultMov_Label = ctk.CTkLabel(parent,
                              text='R$ 0,00 ',
                              text_color='#242424',
                              font=('Arial', 15),
                              bg_color="#D9D9D9",                              
                              )
    linhaValor2_ultMov_Label.place(x=370,y=186)    

    linhaData2_ultMov_Frame = ctk.CTkFrame(parent,
                              width=80,
                              height=30,
                              fg_color="#D9D9D9",
                              bg_color="#7C7C7C",
                              corner_radius=0
                              )
    linhaData2_ultMov_Frame.place(x=518,y=185)

    linhaData2_ultMov_Label = ctk.CTkLabel(parent,
                              text='04/01/2024',
                              text_color='#242424',
                              font=('Arial', 15),
                              bg_color="#D9D9D9",                              
                              )
    linhaData2_ultMov_Label.place(x=521,y=186)   

    btnDetalhesLinha2 = ctk.CTkButton(parent,
                                      text='+',
                                      width=30,
                                      height=30,
                                      fg_color="#242424",
                                      bg_color="#7C7C7C",
                                      hover_color="#3E3E3E",
                                      corner_radius=10,
                                      
                                      )
    btnDetalhesLinha2.place(x=605, y=185)

    # Linha 3

    linhaValor3_ultMov_Frame = ctk.CTkFrame(parent,
                              width=210,
                              height=30,
                              fg_color="#D9D9D9",
                              bg_color="#7C7C7C",
                              corner_radius=0
                              )
    linhaValor3_ultMov_Frame.place(x=300,y=220)

    linhaValor3_ultMov_Label = ctk.CTkLabel(parent,
                              text='R$ 0,00 ',
                              text_color='#242424',
                              font=('Arial', 15),
                              bg_color="#D9D9D9",                              
                              )
    linhaValor3_ultMov_Label.place(x=370,y=221)    

    linhaData3_ultMov_Frame = ctk.CTkFrame(parent,
                              width=80,
                              height=30,
                              fg_color="#D9D9D9",
                              bg_color="#7C7C7C",
                              corner_radius=0
                              )
    linhaData3_ultMov_Frame.place(x=518,y=220)

    linhaData3_ultMov_Label = ctk.CTkLabel(parent,
                              text='04/01/2024',
                              text_color='#242424',
                              font=('Arial', 15),
                              bg_color="#D9D9D9",                              
                              )
    linhaData3_ultMov_Label.place(x=521,y=221)   

    btnDetalhesLinha3 = ctk.CTkButton(parent,
                                      text='+',
                                      width=30,
                                      height=30,
                                      fg_color="#242424",
                                      bg_color="#7C7C7C",
                                      hover_color="#3E3E3E",
                                      corner_radius=10,
                                      
                                      )
    btnDetalhesLinha3.place(x=605, y=220)

    # Linha 4

    linhaValor4_ultMov_Frame = ctk.CTkFrame(parent,
                              width=210,
                              height=30,
                              fg_color="#D9D9D9",
                              bg_color="#7C7C7C",
                              corner_radius=0
                              )
    linhaValor4_ultMov_Frame.place(x=300,y=255)

    linhaValor4_ultMov_Label = ctk.CTkLabel(parent,
                              text='R$ 0,00 ',
                              text_color='#242424',
                              font=('Arial', 15),
                              bg_color="#D9D9D9",                              
                              )
    linhaValor4_ultMov_Label.place(x=370,y=256)    

    linhaData4_ultMov_Frame = ctk.CTkFrame(parent,
                              width=80,
                              height=30,
                              fg_color="#D9D9D9",
                              bg_color="#7C7C7C",
                              corner_radius=0
                              )
    linhaData4_ultMov_Frame.place(x=518,y=255)

    linhaData4_ultMov_Label = ctk.CTkLabel(parent,
                              text='04/01/2024',
                              text_color='#242424',
                              font=('Arial', 15),
                              bg_color="#D9D9D9",                              
                              )
    linhaData4_ultMov_Label.place(x=521,y=256)   

    btnDetalhesLinha4 = ctk.CTkButton(parent,
                                      text='+',
                                      width=30,
                                      height=30,
                                      fg_color="#242424",
                                      bg_color="#7C7C7C",
                                      hover_color="#3E3E3E",
                                      corner_radius=10,
                                      
                                      )
    btnDetalhesLinha4.place(x=605, y=255)

    # Linha 5

    linhaValor5_ultMov_Frame = ctk.CTkFrame(parent,
                              width=210,
                              height=30,
                              fg_color="#D9D9D9",
                              bg_color="#7C7C7C",
                              corner_radius=0
                              )
    linhaValor5_ultMov_Frame.place(x=300,y=290)

    linhaValor5_ultMov_Label = ctk.CTkLabel(parent,
                              text='R$ 0,00 ',
                              text_color='#242424',
                              font=('Arial', 15),
                              bg_color="#D9D9D9",                              
                              )
    linhaValor5_ultMov_Label.place(x=370,y=291)    

    linhaData5_ultMov_Frame = ctk.CTkFrame(parent,
                              width=80,
                              height=30,
                              fg_color="#D9D9D9",
                              bg_color="#7C7C7C",
                              corner_radius=0
                              )
    linhaData5_ultMov_Frame.place(x=518,y=290)

    linhaData5_ultMov_Label = ctk.CTkLabel(parent,
                              text='04/01/2024',
                              text_color='#242424',
                              font=('Arial', 15),
                              bg_color="#D9D9D9",    
                              )
    linhaData5_ultMov_Label.place(x=521,y=291)   

    btnDetalhesLinha5 = ctk.CTkButton(parent,
                                      text='+',
                                      width=30,
                                      height=30,
                                      fg_color="#242424",
                                      bg_color="#7C7C7C",
                                      hover_color="#3E3E3E",
                                      corner_radius=10,
                                      )
    btnDetalhesLinha5.place(x=605, y=290)