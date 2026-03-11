# auto-cobranca-pix
Automação em Python para envio de cobranças personalizadas via WhatsApp Web, utilizando visão computacional (PyAutoGUI) e segurança com variáveis de ambiente.

# Automação de Cobrança - WhatsApp 🚀

Este projeto é uma ferramenta de automação desenvolvida em Python para facilitar o envio de mensagens de cobrança (Pix) para grupos e contatos individuais no WhatsApp Web. 

O script utiliza **visão computacional** para identificar elementos na tela e **dicionários** para organizar os contatos, garantindo que o processo seja escalável e seguro.

## ✨ Funcionalidades
- **Segurança:** Uso de variáveis de ambiente (`.env`) para proteger dados sensíveis como chaves Pix.
- **Visão Computacional:** Localização automática da barra de pesquisa através de reconhecimento de imagem.
- **Organização:** Estrutura de dados em dicionários para fácil manutenção de nomes e números.
- **Escalabilidade:** Loop automático para processar múltiplos contatos de uma vez.

## 🛠️ Tecnologias Utilizadas
- **Python**
- **PyAutoGUI** (Automação de interface)
- **Pyperclip** (Manipulação de área de transferência)
- **Python-dotenv** (Gestão de variáveis de ambiente)
- **OpenCV** (Suporte para precisão na localização de imagens)

## 🚀 Como configurar
1. Clone o repositório.
2. Instale as dependências: `pip install pyautogui pyperclip python-dotenv opencv-python`.
3. Crie um arquivo `.env` baseado no `.env.example` e preencha com seus dados.
4. Tire um print da lupa de pesquisa do seu WhatsApp Web e salve como `lupa.png` na pasta raiz.
5. Execute o script: `python seu_script.py`.

---
*Projeto desenvolvido para fins de estudo e automação de processos repetitivos.*
