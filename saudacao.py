# Arquivo: saudacao.py
def exibir_saudacao(nome):

    """Exibe uma saudação personalizada."""

    print(f"Olá, {nome}! Bem-vindo(a) ao mundo do Python e Git!")

if __name__ == "__main__":

    nome_usuario = input("Qual é o seu nome? ")

    exibir_saudacao(nome_usuario)
