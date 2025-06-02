import tkinter as tk
from tkinter import messagebox

# Dados simulados
def obter_previsao_chuva(cep):
    dados_simulados = {
        "06700-000": 80,
        "01000-000": 10,
        "22290-240": 100,
        "33284-000": 60,
        "01000-386": 30
    }
    return dados_simulados.get(cep, 0)

def verificar_area_risco(cep):
    zonas_de_risco = ["06700-000", "22290-240", "33284-000", "01000-386", "01000-000"]
    # Simula a verificação de áreas de risco
    return cep in zonas_de_risco

def avaliar_risco(cep):
    chuva = obter_previsao_chuva(cep)
    risco = verificar_area_risco(cep)

    if chuva >= 50 and risco:
        return f"CEP: {cep}\nPrevisão: {chuva} mm\nÁrea de risco: Sim\n⚠️ ALTO RISCO!\nRecomenda-se evacuação preventiva."
    elif chuva >= 50:
        return f"CEP: {cep}\nPrevisão: {chuva} mm\nÁrea de risco: Não\n⚠️ RISCO MODERADO.\nFique atento aos alertas."
    elif risco:
        return f"CEP: {cep}\nPrevisão: {chuva} mm\nÁrea de risco: Sim\n⚠️ RISCO POTENCIAL.\nMesmo com pouca chuva, fique atento."
    else:
        return f"CEP: {cep}\nPrevisão: {chuva} mm\nÁrea de risco: Não\n✅ Risco baixo."

# GUI
def verificar():
    cep = entry_cep.get()
    if not cep:
        messagebox.showwarning("Atenção", "Digite um CEP válido.")
        return
    resultado = avaliar_risco(cep)
    messagebox.showinfo("Resultado da Avaliação", resultado)

app = tk.Tk()
app.title("Prevenção de Deslizamentos")

tk.Label(app, text="Digite o CEP:", font=("Arial", 12)).pack(pady=10)
entry_cep = tk.Entry(app, font=("Arial", 12), width=20)
entry_cep.pack()

btn = tk.Button(app, text="Verificar Risco", font=("Arial", 12), command=verificar)
btn.pack(pady=20)

app.mainloop()
