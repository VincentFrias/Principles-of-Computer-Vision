import cv2
import numpy as np

# Carrega a imagem
imagem = cv2.imread("img/img00.jpeg")
if imagem is None:
    print("Erro ao carregar a imagem.")
    exit()

# Converte para grayscale (uma vez só)
foto_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
altura, largura = foto_gray.shape

# FILTRO PERSONALIZADO - bordas horizontais
kernel_detec = np.array([
    [1, 2, 1],
    [0, 0, 0],
    [-1, -2, -1]
])
imagem_filtrada = cv2.filter2D(foto_gray, -1, kernel_detec)

# MANUAL: Computa gx com padding e clip 
foto_gray_int16 = foto_gray.astype(np.int16)  # Converte para signed ANTES do pad
pad = 1  # Para kernel 3x3
foto_padded = np.pad(foto_gray_int16, pad, mode='constant', constant_values=0)
imagem_board = np.zeros((altura, largura), dtype=np.uint8)  # Saída final uint8

for i in range(altura):
    for j in range(largura):
        # Índices ajustados para padding: i+pad é o centro
        row_top = i + pad - 1
        row_mid = i + pad
        row_bot = i + pad + 1
        col_left = j + pad - 1
        col_mid = j + pad
        col_right = j + pad + 1
        
        # gx (mesmo kernel: positivo à esquerda, negativo à direita)
        gx = (
            1 * foto_padded[row_top, col_left] + 0 * foto_padded[row_top, col_mid] + (-1) * foto_padded[row_top, col_right] +
            2 * foto_padded[row_mid, col_left] + 0 * foto_padded[row_mid, col_mid] + (-2) * foto_padded[row_mid, col_right] +
            1 * foto_padded[row_bot, col_left] + 0 * foto_padded[row_bot, col_mid] + (-1) * foto_padded[row_bot, col_right]
        )
        # Clip para 0-255 (simula imshow: negativos -> 0, excessos -> 255)
        imagem_board[i, j] = np.clip(gx, 0, 255).astype(np.uint8)

# Mostra (rótulos corrigidos)
cv2.imshow("Imagem Original (Colorida)", imagem)
cv2.imshow("Bordas Horizontais (Filter2D)", imagem_filtrada)
cv2.imshow("Bordas Horizontais (Manual)", imagem_board)

# Aguarda tecla e fecha janelas
cv2.waitKey(0)
cv2.destroyAllWindows()

# Opcional: Salva
cv2.imwrite("img/detec_board/board_filtrada.png", imagem_filtrada)
cv2.imwrite("img/detec_board/board_manual.png", imagem_board)