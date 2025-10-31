import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

# Carrega imagem e converte para cinza
img = cv2.imread("img/img01.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.uint8)

altura, largura = gray.shape
freq = [0] * 256            # frequência normalizada
freq_acumulada = [0] * 257  # frequência acumulada
equalizacao = np.zeros(256, dtype=np.uint8)  # mapa equalização
hist_equal = [0] * 256      # histograma equalizado

# Conta frequência absoluta
for i in range(altura):
    for j in range(largura):
        valor = gray[i][j]
        freq[valor] += 1

# Normaliza frequência
for i in range(256):
    freq[i] /= (altura * largura)

# Calcula frequência acumulada e mapeamento equalizado
for i in range(256):
    freq_acumulada[i + 1] = freq_acumulada[i] + freq[i]
    equalizacao[i] = np.floor(freq_acumulada[i] * 255).astype(np.uint8)

# Aplica equalização à imagem
img_eq = np.zeros_like(gray)
for i in range(altura):
    for j in range(largura):
        valor_original = gray[i][j]
        img_eq[i][j] = equalizacao[valor_original]

# Conta frequência do histograma equalizado
for i in range(altura):
    for j in range(largura):
        valor = img_eq[i][j]
        hist_equal[valor] += 1

# Salva imagem equalizada para mostrar
imagem = Image.fromarray(img_eq, mode='L')
imagem.save("img/equalization/equalization.png")
img_eq_final = cv2.imread("img/equalization/equalization.png", cv2.IMREAD_GRAYSCALE)

# Histograma original para plotar
hist_original = [int(f * (altura * largura)) for f in freq]

# Plota histogramas original e equalizado
plt.title("Histograma em Escala de Cinza")
plt.xlabel("Níveis de Cinza")
plt.ylabel("Frequência de Pixels")
bins = np.arange(256)
plt.bar(bins, hist_original, width=1, color='gray', alpha=0.7, label='Original')
plt.bar(bins, hist_equal, width=1, color='blue', alpha=0.5, label='Equalizado')
plt.xlim([-1, 256])
plt.xticks(np.arange(0, 256, 32))
plt.grid(axis='y', alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig('img/equalization/histograma.png', dpi=300, bbox_inches='tight')
plt.show()

# Mostra imagens com OpenCV
cv2.imshow("Imagem Original", gray)
cv2.imshow("Imagem Equalizada", img_eq_final)


if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()
