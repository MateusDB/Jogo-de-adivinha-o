# Jogo do 0 a 100

Um jogo de adivinhação desafiador desenvolvido em **Python**. O objetivo é descobrir o número secreto escolhido pelo computador dentro de um limite de tentativas.

---

## Sobre o Projeto

Este projeto foi estruturado para aplicar conceitos de lógica, com foco em:
* **Controle de Fluxo:** Uso de `while True` para manter o jogo ativo.
* **Validação de Dados:** Verificação se o palpite está dentro do intervalo permitido (0-100).
* **Sistema de Limites:** Implementação de um teto máximo de tentativas para aumentar a dificuldade.

---

## Como Funciona

1.  **O Desafio:** O computador escolhe um número aleatório entre 0 e 100.
2.  **Limite de Tentativas:** Você tem no máximo **10 tentativas** para acertar.
3.  **Feedback Dinâmico:**
    * Se o palpite estiver fora do intervalo (ex: 150), o jogo avisa que o número é inválido.
    * Se errar, o sistema diz se o número secreto é **maior** ou **menor** que o seu palpite.
4.  **Finalização:**
    * **Vitória:** O jogo informa em quantas tentativas você acertou.
    * **Derrota:** Se atingir 10 tentativas sem sucesso, o jogo revela o número secreto e encerra.

---

## Tecnologias Utilizadas

* **Python 3.x**
* **Biblioteca `random`**: Para geração do número aleatório.

---

## Como Rodar o Jogo

Para jogar no seu computador via Prompt de Comando (CMD) ou Terminal:

1. **Verifique o Python:**
   `python --version`

2. **Crie o arquivo:**
   Salve o código em um arquivo chamado `jogo.py`.

3. **Acesse a pasta pelo Terminal:**
   `cd caminho/da/sua/pasta`

4. **Inicie o jogo:**
   `python jogo.py`

---

## Licença

Este projeto é para fins de estudo e prática. Sinta-se à vontade para utilizar e melhorar o código!
