# 📝 Sistema de Gestão de Notas

## 🚀 O que é isso?
Um projetinho em **Python** que faz a gestão de notas de alunos.  
Com ele você pode:  
- Adicionar notas  
- Calcular a média  
- Descobrir se o aluno está **aprovado** ou **reprovado**  
- Ver um relatório final com tudo junto  

---

## ⚙️ Como funciona?
- Você digita as notas (quantas quiser).  
- Elas ficam guardadas numa lista.  
- O programa calcula a média.  
- Regras:  
  - Média **≥ 7** → Aprovado  
  - Média **< 7** → Reprovado  
- No final ele mostra as notas, a média e a situação.  

---
🎯 Exemplo
  ```bash
=== Sistema de Gestão de Notas ===
Nome do aluno: João
Quantas notas serão calculadas?: 3
Nota 1: 8
Nota 2: 6
Nota 3: 9
Calculando a média......

Relatório do aluno: João
Notas: [8.0, 6.0, 9.0]
Média: 7.67
Resultado: Aprovado
```

📂 Estrutura do código

O sistema é dividido em funções para ficar mais organizado:

cadastro_notas() → pede o nome do aluno e as notas.

carregando() → exibe a animação de carregamento.

limpar_terminal() → limpa a tela (funciona em Windows e Linux/Mac).

calculo() → calcula a média das notas.

verificar_aprovacao() → retorna "Aprovado" ou "Reprovado".

exibir_relatorio() → mostra o relatório final.

main() → ponto de entrada que organiza a execução.

📌 Observações

Dá pra cadastrar qualquer quantidade de notas.

Se nenhuma nota for inserida, a média será 0.

Código comentado para facilitar o entendimento.




