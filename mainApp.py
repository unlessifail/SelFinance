import customtkinter as ctk
import gui
# from sf_auth import usuario_logado

sfApp = ctk.CTk()

sfApp._set_appearance_mode("dark")
sfApp.after(0, lambda:sfApp.state('zoomed'))
sfApp.geometry("1440x840")
sfApp.title('SelFinance | Dashboard')

left_side_menu_bar = gui.criar_left_side_menu_bar(sfApp)
header_logo = gui.criar_header_logo(sfApp)
saldo_widget = gui.criar_saldo_widget(sfApp)
receita_widget = gui.criar_receita_widget(sfApp)
despesa_widget = gui.criar_despesa_widget(sfApp)
ultimas_movimentacoes_widget = gui.criar_ult_mov_widget(sfApp)
criar_add_receita = gui.criar_add_receita_janela(sfApp)
criar_add_despesa = gui.criar_add_despesa_janela(sfApp)
criar_exibir_extrato = gui.criar_exibir_extrato(sfApp)


sfApp.mainloop()