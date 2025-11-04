import cv2
import numpy as np

# Carrega as imagens HSV com 3 canais
foto1 = cv2.imread("./img/img01.jpeg")  # Assumimos que está em HSV codificado como PNG
foto2 = cv2.imread("./img/equalization/equalization.png")  # Também com 3 canais

# Verificações de segurança
if foto1 is None or foto2 is None:
    print("Erro ao carregar uma das imagens.")
    exit()

# Converter de HSV para RGB (se necessário para exibição)
foto1_rgb = cv2.cvtColor(foto1, cv2.COLOR_BGR2RGB)
foto2_rgb = cv2.cvtColor(foto2, cv2.COLOR_HSV2RGB)

# Converter de RGB para GRAY para comparação de similaridade
foto1_gray = cv2.cvtColor(foto1_rgb, cv2.COLOR_RGB2GRAY)
foto2_gray = cv2.cvtColor(foto2_rgb, cv2.COLOR_RGB2GRAY)

# Ajusta altura e largura para o menor tamanho comum
altura = min(foto1_gray.shape[0], foto2_gray.shape[0])
largura = min(foto1_gray.shape[1], foto2_gray.shape[1])

# Cálculo do índice de Jaccard binário (simples)
soma = 0
for i in range(altura):
    for j in range(largura):
        if foto1_gray[i, j] >= foto2_gray[i, j]*0.9 and foto1_gray[i, j] <= foto2_gray[i, j]*1.1:
            soma += 1

jaccard_index = soma / (altura * largura)
print(f"Índice de Jaccard: {jaccard_index:.4f}")

# Mostrar as imagens RGB convertidas
cv2.imshow("Imagem 1 (RGB)", cv2.cvtColor(foto1_rgb, cv2.COLOR_RGB2BGR))
cv2.imshow("Imagem 2 (RGB)", cv2.cvtColor(foto2_rgb, cv2.COLOR_RGB2BGR))

# Fecha a janela quando a tecla 'q' for pressionada
if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()
