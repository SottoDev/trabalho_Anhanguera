import time
import os


#Cadastro de notas
def cadastro_notas():
    nome = input("Nome do aluno: ")
    notas = []
    quantidade = int(input("Quantas notas serão calculadas?: "))
    
    for i in range(quantidade):
        nota = float(input(f'Nota {i+1}: '))
        notas.append(nota)
    return nome, notas

#Firula pra deixar o codigo mais bonitinho, aparece um calculando a media e os tres pontinhos mexem
def carregando():
    print("Calculando a média...", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    time.sleep(0.5)
    print()

#Limpa o terminal 
def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#Faz o calculo das notas
def calculo(notas):
    if len(notas) == 0:
        return 0
    
    return sum(notas)/len(notas)

#Verifica se o aluno foi aprovado
def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

#Exibi o resultado    
def exibir_relatorio(nome, notas, media, resultado):
    print(f"\nRelatório do aluno: {nome}")
    print("Notas:", notas)
    print(f"Média: {media:.2f}")
    print("Resultado:", resultado)

#Codigo    
def main():
    print("=== Sistema de Gestão de Notas ===")
    nome, notas = cadastro_notas()  # recebe o nome e as notas
    limpar_terminal() # Limpa o terminal para ficar mais organizado
    carregando()    # animaçãozinha do carregando.....
    media = calculo(notas)  # calcula a media e cospe o resultado
    situacao = verificar_aprovacao(media) # Exibe o resultado
    exibir_relatorio(nome, notas, media, situacao)  # passa o nome também
 
    
if __name__ == "__main__":
    main()