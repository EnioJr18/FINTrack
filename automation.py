import time 
import pyautogui
import pygetwindow as gw

def voltar_para_vscode():
    """
    Procura por uma janela do Visual Studio Code e a ativa.
    """
    try:
        vscode_window = gw.getWindowsWithTitle('Visual Studio Code')[0]
        if vscode_window:
            print("Janela do VS Code encontrada. Ativando...")
            vscode_window.activate() 
            time.sleep(2.5)
        else:
            print("Janela do VS Code não encontrada.")
    except IndexError:
        print("Erro: Nenhuma janela do Visual Studio Code foi encontrada.")

def automatizador():
    print("Iniciando em 5 segundos... Mova o mouse para o terminal se quiser cancelar.")
    time.sleep(4) 
    
    print("Iniciando automação de tarefas...")
    time.sleep(2.5)

    pyautogui.alert("Automação iniciada! Siga as instruções na tela.")
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('Chrome')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.write('https://eniojr18.github.io/Siteteste/')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.write('admin123')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.write('admin54321')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('enter')
    pyautogui.alert("Login realizado com sucesso!")
    

    voltar_para_vscode()


automatizador()
print("Automação concluída.")