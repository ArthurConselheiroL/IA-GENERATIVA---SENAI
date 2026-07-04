import tkinter as tk
import calculos as cl
from tkinter import ttk
from tkinter import messagebox
import sqlite3

# ============================================
# CONFIGURAÇÃO DO BANCO DE DADOS (SQLite3)
# ============================================
def inicializar_banco():
    conexao = sqlite3.connect("banco_sistema.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()

inicializar_banco()


# ============================================
# FUNÇÕES DE LÓGICA, CÁLCULOS E BANCO
# ============================================
def run_imc():
    peso_ = float(peso.get())
    altura_ = float(altura.get())
    resultado = cl.imc(peso_, altura_)
    r = round(resultado, 2)
    return mostrar_imc.config(text=f"IMC: {r}")


def run_calculo_h():
    carga_ = float(carga.get())
    salario_ = float(salario.get())
    resultado = cl.calculo_sal_hora(carga_, salario_)
    r = round(resultado, 2)
    return mostrar_sal.config(text=f"Valor/Hora: R$ {r}")

def run_extra():
    q = int(quantidade.get())
    carga_ = float(carga.get())
    salario_ = float(salario.get())
    resultado = cl.calculo_sal_hora(carga_, salario_)
    r = round(resultado, 2)
    rs = cl.calculo_quantidade_extra50(q, r)
    return mostrar_extra.config(text=f"Total Extra: R$ {rs}")

# Função para buscar os dados do banco e renderizar na tabela (Treeview)
def atualizar_tabela():
    # Limpa todos os dados existentes na tabela antes de recarregar
    for linha in tabela.get_children():
        tabela.delete(linha)
       
    conexao = sqlite3.connect("banco_sistema.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, email FROM pessoas ORDER BY id DESC")
    usuarios = cursor.fetchall()
    conexao.close()
   
    # Insere os dados atualizados
    for usuario in usuarios:
        tabela.insert("", tk.END, values=usuario)

def run_cadastro():
    nome_ = nome.get().strip()
    email_ = email.get().strip()
   
    if nome_ == "" or email_ == "":
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos!")
        return

    conexao = sqlite3.connect("banco_sistema.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO pessoas (nome, email) VALUES (?, ?)", (nome_, email_))
    conexao.commit()
    conexao.close()
   
    nome.delete(0, tk.END)
    email.delete(0, tk.END)
   
    messagebox.showinfo("Sucesso", f"Cadastro de {nome_} realizado com sucesso!")
    atualizar_tabela()  # Atualiza a tabela imediatamente após cadastrar


# ============================================
# INTERFACE GRÁFICA (Tkinter/ttk)
# ============================================
janela = tk.Tk()
janela.title("Sistema de Cálculos e Cadastro")
janela.geometry('500x650')  # Janela ampliada para acomodar melhor a tabela
janela.configure(bg="#f4f6f9")
janela.resizable(False, False)

# Configuração de Estilos Nativos
estilo = ttk.Style()
estilo.theme_use('clam')

estilo.configure("TNotebook", background="#f4f6f9", borderwidth=0)
estilo.configure("TNotebook.Tab", font=("Segoe UI", 10, "bold"), padding=[12, 6], background="#e0e0e0")
estilo.map("TNotebook.Tab", background=[("selected", "#1a73e8")], foreground=[("selected", "#ffffff")])

estilo.configure("TLabel", background="#ffffff", font=("Segoe UI", 10))
estilo.configure("Card.TLabelframe", background="#ffffff", relief="flat", borderwidth=1)
estilo.configure("Card.TLabelframe.Label", font=("Segoe UI", 11, "bold"), foreground="#1a73e8", background="#ffffff")
estilo.configure("Acao.TButton", font=("Segoe UI", 10, "bold"), foreground="#ffffff", background="#1a73e8", borderwidth=0)
estilo.map("Acao.TButton", background=[('active', '#1557b0')])

# Estilo específico para a tabela (Treeview)
estilo.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"), background="#e0e0e0", foreground="#202124")
estilo.configure("Treeview", font=("Segoe UI", 10), rowheight=25)

# Componente de Abas
notebook = ttk.Notebook(janela)
notebook.pack(padx=15, pady=15, expand=True, fill='both')

pagina_imc = tk.Frame(notebook, bg="#f4f6f9")
pagina_trabalhista = tk.Frame(notebook, bg="#f4f6f9")
pagina_cadastro = tk.Frame(notebook, bg="#f4f6f9")

notebook.add(pagina_imc, text="  Saúde (IMC)  ")
notebook.add(pagina_trabalhista, text="  Trabalhista  ")
notebook.add(pagina_cadastro, text="  Cadastrar Pessoas  ")


# ============================================
# PÁGINA 1: IMC
# ============================================
espaco_imc = ttk.LabelFrame(pagina_imc, text='  Calculadora de IMC  ', style="Card.TLabelframe", padding=20)
espaco_imc.pack(padx=15, pady=20, fill='x')

texto1 = ttk.Label(espaco_imc, text='Peso (kg)')
texto1.grid(column=0, row=0, padx=5, pady=2, sticky='w')
peso = ttk.Entry(espaco_imc, font=('Segoe UI', 11), width=15)
peso.grid(column=0, row=1, padx=5, pady=5)

texto2 = ttk.Label(espaco_imc, text='Altura (m)')
texto2.grid(column=1, row=0, padx=5, pady=2, sticky='w')
altura = ttk.Entry(espaco_imc, font=('Segoe UI', 11), width=15)
altura.grid(column=1, row=1, padx=5, pady=5)

bt_imc = ttk.Button(espaco_imc, text='Calcular IMC', style="Acao.TButton", command=run_imc)
bt_imc.grid(column=0, row=2, columnspan=2, pady=20, sticky='we')

mostrar_imc = tk.Label(espaco_imc, text='', font=('Segoe UI', 13, 'bold'), fg="#1e7e34", bg="#ffffff")
mostrar_imc.grid(column=0, row=3, columnspan=2, pady=5)


# ============================================
# PÁGINA 2: TRABALHISTA
# ============================================
espaco_salario = ttk.LabelFrame(pagina_trabalhista, text='  Salário Hora  ', style="Card.TLabelframe", padding=15)
espaco_salario.pack(padx=15, pady=10, fill='x')

texto3 = ttk.Label(espaco_salario, text='Carga Horária')
texto3.grid(column=0, row=0, padx=5, pady=2, sticky='w')
carga = ttk.Entry(espaco_salario, font=('Segoe UI', 11), width=15)
carga.grid(column=0, row=1, padx=5, pady=5)

texto_sal_lbl = ttk.Label(espaco_salario, text='Salário (R$)')
texto_sal_lbl.grid(column=1, row=0, padx=5, pady=2, sticky='w')
salario = ttk.Entry(espaco_salario, font=('Segoe UI', 11), width=15)
salario.grid(column=1, row=1, padx=5, pady=5)

bt_sal = ttk.Button(espaco_salario, text='Calcular Salário Hora', style="Acao.TButton", command=run_calculo_h)
bt_sal.grid(column=0, row=2, columnspan=2, pady=10, sticky='we')

mostrar_sal = tk.Label(espaco_salario, text='', font=('Segoe UI', 12, 'bold'), fg="#1e7e34", bg="#ffffff")
mostrar_sal.grid(column=0, row=3, columnspan=2, pady=2)

espaco_quantidade = ttk.LabelFrame(pagina_trabalhista, text='  Horas Extras (50%)  ', style="Card.TLabelframe", padding=15)
espaco_quantidade.pack(padx=15, pady=10, fill='x')

texto_qtd = ttk.Label(espaco_quantidade, text='Quantidade de Horas')
texto_qtd.grid(column=0, row=0, padx=5, pady=2, sticky='w')
quantidade = ttk.Entry(espaco_quantidade, font=('Segoe UI', 11), width=15)
quantidade.grid(column=0, row=1, padx=5, pady=5)

bt_ex = ttk.Button(espaco_quantidade, text='Calcular Extra', style="Acao.TButton", command=run_extra)
bt_ex.grid(column=1, row=1, padx=10, pady=5, sticky='we')

mostrar_extra = tk.Label(espaco_quantidade, text='', font=('Segoe UI', 12, 'bold'), fg="#1e7e34", bg="#ffffff")
mostrar_extra.grid(column=0, row=2, columnspan=2, pady=2)


# ============================================
# PÁGINA 3: CADASTRO E LISTA DE PESSOAS
# ============================================
espaco_cadastro = ttk.LabelFrame(pagina_cadastro, text='  Novo Cadastro  ', style="Card.TLabelframe", padding=15)
espaco_cadastro.pack(padx=15, pady=10, fill='x')

texto_nome = ttk.Label(espaco_cadastro, text='Nome Completo:')
texto_nome.grid(column=0, row=0, padx=5, pady=2, sticky='w')
nome = ttk.Entry(espaco_cadastro, font=('Segoe UI', 11))
nome.grid(column=0, row=1, padx=5, pady=5, sticky='we')

texto_email = ttk.Label(espaco_cadastro, text='E-mail:')
texto_email.grid(column=1, row=0, padx=5, pady=2, sticky='w')
email = ttk.Entry(espaco_cadastro, font=('Segoe UI', 11))
email.grid(column=1, row=1, padx=5, pady=5, sticky='we')

# Configurar peso das colunas para os inputs expandirem simetricamente
espaco_cadastro.columnconfigure(0, weight=1)
espaco_cadastro.columnconfigure(1, weight=1)

bt_salvar = ttk.Button(espaco_cadastro, text='Salvar Cadastro', style="Acao.TButton", command=run_cadastro)
bt_salvar.grid(column=0, row=2, columnspan=2, pady=10, sticky='we')

# Frame da Tabela (Container para alinhar a Treeview e Scrollbar)
espaco_tabela = ttk.LabelFrame(pagina_cadastro, text='  Pessoas Cadastradas  ', style="Card.TLabelframe", padding=10)
espaco_tabela.pack(padx=15, pady=10, fill='both', expand=True)

# Definição das colunas da tabela
colunas = ('ID', 'Nome', 'E-mail')
tabela = ttk.Treeview(espaco_tabela, columns=colunas, show='headings', selectmode="browse")

# Cabeçalhos e tamanho das colunas
tabela.heading('ID', text='ID')
tabela.heading('Nome', text='Nome')
tabela.heading('E-mail', text='E-mail')

tabela.column('ID', width=40, anchor='center', minwidth=40)
tabela.column('Nome', width=180, anchor='w', minwidth=150)
tabela.column('E-mail', width=200, anchor='w', minwidth=150)

# Barra de rolagem para a tabela caso haja muitos registros
scrollbar = ttk.Scrollbar(espaco_tabela, orient=tk.VERTICAL, command=tabela.yview)
tabela.configure(yscrollcommand=scrollbar.set)

tabela.pack(side=tk.LEFT, fill='both', expand=True)
scrollbar.pack(side=tk.RIGHT, fill='y')

# Inicializa a tabela carregando os registros existentes no banco
atualizar_tabela()

janela.mainloop()