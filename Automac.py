import pyautogui as pg
import time
import pyperclip as cp
import os
from dotenv import load_dotenv

# Carrega as configurações de segurança
load_dotenv()

# Configurações globais
pg.pause = 1
CHAVE_PIX = os.getenv('CHAVE_PIX')
VALOR_COBRANCA = os.getenv('VALOR_COBRANCA')
GRUPO = os.getenv('NOME_GRUPO_WHATSAPP')

# === DICIONÁRIO DE CONTATOS ===
# Estrutura: "Nome para Pesquisa": "Número de Telefone"
contatos = {
    "Contato Um": "5585999999999",
    "Contato Dois": "5585888888888",
    "Contato Três": "5585777777777",
    "Contato Quatro": "5585666666666"
}

def localizar_e_clicar(imagem):
    """Procura a imagem na tela para evitar cliques em coordenadas erradas"""
    try:
        posicao = pg.locateCenterOnScreen(imagem, confidence=0.8)
        if posicao:
            pg.click(posicao)
            return True
    except Exception as e:
        print(f"Erro ao tentar localizar {imagem}: {e}")
    return False

# --- Fluxo de Automação ---
pg.press('win')
pg.write('Google Chrome')
pg.press('enter')
time.sleep(1)

pg.write('https://web.whatsapp.com/')
pg.press('enter')
print("Aguardando o carregamento...")
time.sleep(15) 

# === 1. MENSAGEM NO GRUPO ===
if localizar_e_clicar('lupa.png'):
    pg.write(GRUPO)
    pg.press('enter')
    
    msg_grupo = "🟢 ???!"
    cp.copy(msg_grupo)
    pg.hotkey('ctrl', 'v')
    pg.press('enter')

# === 2. ENVIO INDIVIDUAL (LOOP COM DICIONÁRIO) ===
# O .items() permite pegar o Nome e o Número ao mesmo tempo
for nome, numero in contatos.items():
    if localizar_e_clicar('lupa.png'):
        time.sleep(0.5)
        pg.write(nome) # Pesquisa pelo nome salvo no Zap
        time.sleep(1)
        pg.press('enter')

        # Texto fixo usando o valor definido no .env
        # O 'numero' está guardado caso você queira incluir na mensagem futuramente
        msg_privado = f"Olá {nome}, ???"
        
        cp.copy(msg_privado)
        pg.hotkey('ctrl', 'v')
        pg.press('enter')
        print(f"Enviado para {nome}")
    
    time.sleep(1)