import cv2
import numpy as np
import pyautogui
import keyboard

# Obtém o tamanho da tela
screen_size = tuple(pyautogui.size())

# Define o codec, neste caso utilizei para o formato .AVI
codec = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("gravacao.avi", codec, 30, screen_size)

# Loop principal para capturar a tela
while True:
    # Captura uma screenshot por vez
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Grava o frame no vídeo
    out.write(frame)

    # Verifica se a tecla "esc" foi pressionada para encerrar o loop
    if keyboard.is_pressed("esc"):
        break

# Finaliza a gravação
cv2.destroyAllWindows()
out.release()