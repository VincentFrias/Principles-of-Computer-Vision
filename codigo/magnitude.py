import os
import cv2
import numpy as np

# Carrega a imagem
imagem = cv2.imread("img/img00.jpeg")
if imagem is None:
    print("Erro ao carregar a imagem.")
    exit()

# Converte para grayscale (uma vez só)
foto_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Se tiver duvidas sobre o codigo do kernel, veja detec_board.py
# Kernel Sobel em x: variação horizontal -> bordas verticais
kernel_gx = np.array([
    [1, 0, -1],
    [2, 0, -2],
    [1, 0, -1]
], dtype=np.int16)

# Kernel Sobel em y: variação vertical -> bordas horizontais
kernel_gy = np.array([
    [1, 2, 1],
    [0, 0, 0],
    [-1, -2, -1]
], dtype=np.int16)

# O sinal do gradiente só diz o sentido da mudança (claro->escuro ou escuro->claro); os dois sentidos são borda.
# CV_16S guarda o negativo; uint8 transformaria em 0.
gx_img = cv2.filter2D(foto_gray, cv2.CV_16S, kernel_gx)
gy_img = cv2.filter2D(foto_gray, cv2.CV_16S, kernel_gy)

# Magnitude: comprimento do vetor (Gx, Gy)
# |G| = sqrt(Gx² + Gy²)  -> força da borda, independente da direção
magnitude = np.sqrt((gx_img.astype(np.float32) ** 2) + (gy_img.astype(np.float32) ** 2))

# Clip só na exibição (abs mostra as duas polaridades; magnitude já é >= 0)
gx_show = np.clip(np.abs(gx_img), 0, 255).astype(np.uint8)
gy_show = np.clip(np.abs(gy_img), 0, 255).astype(np.uint8)
magnitude_show = np.clip(magnitude, 0, 255).astype(np.uint8)

# Opcional: Salva
#os.makedirs("img/magnitude", exist_ok=True)
#cv2.imwrite("img/magnitude/gx.png", gx_show)
#cv2.imwrite("img/magnitude/gy.png", gy_show)
#cv2.imwrite("img/magnitude/magnitude.png", magnitude_show)

# Mostra
cv2.imshow("Original", imagem)
cv2.imshow("Gx", gx_show)
cv2.imshow("Gy", gy_show)
cv2.imshow("Magnitude", magnitude_show)

# Fecha com 'q', ESC, ou ao fechar a janela
while True:
    if cv2.getWindowProperty("Original", cv2.WND_PROP_VISIBLE) < 1:
        break
    key = cv2.waitKey(50) & 0xFF
    if key in (27, ord("q")):
        break
cv2.destroyAllWindows()
