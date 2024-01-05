import sqlite3
import customtkinter as ctk
from PIL import Image
from time import sleep

conn = sqlite3.connect('financas.db')
cursor = conn.cursor()

login_app = ctk.CTk()

login_app.title('SelFinance | Login')
login_app.geometry('350x406')
login_app.attributes('-alpha', 0.9)
login_app.resizable(False, False)

# Funcs

def registrar_usuario():
    user_email = entryUserEmail.get()
    user_senha = entryUserSenha.get()

    # Verificar se o usuário já existe
    cursor.execute("SELECT * FROM usuarios WHERE usuario_email=?", (user_email,))
    existing_user = cursor.fetchone()

    if existing_user:
        retorno_label.configure(text="Usuário já registrado.", text_color='#FF0000')  

    elif len(user_email) < 6 or len(user_senha) < 6:
        retorno_label.configure(text="E-mail e senha devem ter pelo menos 6 caracteres.", text_color='#FF0000') 

    else:
        # Registrar o novo usuário
        cursor.execute("INSERT INTO usuarios (usuario_email, usuario_senha) VALUES (?, ?)", (user_email, user_senha))
        conn.commit()
        retorno_label.configure(text="Usuário registrado com sucesso.", text_color='#00FF00')


def validar_usuario():
    global usuario_logado

    user_email = entryUserEmail.get()
    user_senha = entryUserSenha.get()

    # Verificar se o usuário existe e a senha está correta
    cursor.execute("SELECT * FROM usuarios WHERE usuario_email=? AND usuario_senha=?", (user_email, user_senha))
    existing_user = cursor.fetchone()

    if existing_user:
        retorno_label.configure(text="Login bem-sucedido.")
        usuario_logado = user_email
        abrir_main_app()
    else:
        retorno_label.configure(text="Usuário não encontrado ou senha incorreta.")

def abrir_main_app():
    # Fechar a janela de login
    sleep(1)
    login_app.destroy()

    import mainApp

# Logo

sf_logo_auth = ctk.CTkImage(dark_image=Image.open(r"assets\icons\logoSelFinance.png"), size=(170,170))
sf_logo_ready = ctk.CTkLabel(login_app, text=None, image=sf_logo_auth, fg_color="#242424", corner_radius=500)
sf_logo_ready.place(x=80, y=42)

# Labels

retorno_label = ctk.CTkLabel(login_app,
                        text='',
                        text_color='#FFFFFF',
                        font=('Impact', 10),
                        bg_color="#242424",
                        )
retorno_label.place(x=50,y=203)

# Entry

entryUserEmail = ctk.CTkEntry(login_app, 
                         width=300,
                         height=40,
                         fg_color="#C5C2C2",
                         placeholder_text="E-mail:",
                         placeholder_text_color="#000000",
                         text_color="#000000",
                         corner_radius=30,
                         bg_color="#242424",
                         border_width=0
                         )
entryUserEmail.place(x=25, y=240)

entryUserSenha = ctk.CTkEntry(login_app, 
                         width=300,
                         height=40,
                         fg_color="#C5C2C2",
                         placeholder_text="Senha:",
                         placeholder_text_color="#000000",
                         text_color="#000000",
                         corner_radius=30,
                         bg_color="#242424",
                         border_width=0,
                         show='*'
                         )
entryUserSenha.place(x=25, y=292)

# Btns

btnRegistrar = ctk.CTkButton(login_app,
                             width=140,
                             height=40,
                             text="Registrar",
                             font=("Impact", 20),
                             fg_color="#363636",
                             bg_color="#242424",
                             hover_color="#262626",
                             corner_radius=5,
                             command=registrar_usuario,
                             )
btnRegistrar.place(x=30, y=344)

btnEntrar = ctk.CTkButton(login_app,
                             width=140,
                             height=40,
                             text="Entrar",
                             font=("Impact", 20),
                             fg_color="#363636",
                             bg_color="#242424",
                             hover_color="#262626",
                             corner_radius=5,
                             command=validar_usuario,
                             )
btnEntrar.place(x=180, y=344)

login_app.mainloop()