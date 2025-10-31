import cv2
from PIL import Image
import numpy as np

foto = cv2.imread("img/img00.jpeg") #recebe a foto
foto_gray = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY) #converte a foto para escala de cinza

#aplica o filtro de suavização
#Diante de observações, quanto maior a área do filtro, mais suave a imagem
#obs: suave==>embaçado
#foto_gray_suavizada = cv2.blur(foto_gray, (3, 3)) 

#aplica o filtro de suavização
#Diante de observações, quanto maior a área do filtro, mais suave a imagem
#obs: suave==>embaçado
#foto_gray_suavizada = cv2.medianBlur(foto_gray, 3) 

altura = len(foto_gray)
largura = len(foto_gray[0])

#cria uma nova imagem com a altura e largura da imagem original
imagem_gray_med =  [[0 for _ in range(largura)] for _ in range(altura)] 

for i in range(1,altura - 1):       # i = linha
    for j in range(1,largura - 1):  # j = coluna
        #soma2 = np.sum(foto_gray[i-1:i+2, j-1:j+2])
        #print("soma1:",(soma2 / 9))
        soma = (
                float(foto_gray[i-1, j-1]) + float(foto_gray[i-1, j]) + float(foto_gray[i-1, j+1]) +
                float(foto_gray[i,   j-1]) + float(foto_gray[i,   j]) + float(foto_gray[i,   j+1]) +
                float(foto_gray[i+1, j-1]) + float(foto_gray[i+1, j]) + float(foto_gray[i+1, j+1])
        )
        
        imagem_gray_med[i][j] = (soma // 9)
        #print("soma2:",soma/9)


imagem_gray_median =  [[0 for _ in range(largura)] for _ in range(altura)] 
val = [] * 9

for i in range(1,altura - 1):       # i = linha
    for j in range(1,largura - 1):  # j = coluna

            for x in range(-1, 2):
                for y in range(-1, 2):
                    val.append(foto_gray[i + x, j + y])
            # Ordena a lista de valores
            val.sort()
            imagem_gray_median[i][j] = int(val[4])  # Pega o valor do meio da lista ordenada
            val.clear()
        

# Converte a matriz para um array NumPy do tipo uint8
array_med = np.array(imagem_gray_med, dtype=np.uint8)
array_median = np.array(imagem_gray_median, dtype=np.uint8)

# Cria uma imagem em tons de cinza (modo 'L')
imagem_med = Image.fromarray(array_med, mode='L')
imagem_median = Image.fromarray(array_median, mode='L')

# Salva ou mostra a imagem
imagem_med.save("img/simple_filt/saida_med.png")
imagem_gray_med= cv2.imread("img/simple_filt/saida_med.png",cv2.IMREAD_GRAYSCALE)
imagem_median.save("img/simple_filt/saida_median.png")
imagem_gray_median = cv2.imread("img/simple_filt/saida_median.png",cv2.IMREAD_GRAYSCALE)


#mostra ambas as fotos
cv2.imshow("Imagem em Preto e Branco", foto_gray)
cv2.imshow("Imagem em Preto e Branco Média", imagem_gray_med)
cv2.imshow("Imagem em Preto e Branco Mediana", imagem_gray_median)


#fecha a janela quando a tecla 'q' for pressionada
if cv2.waitKey(0)== ord('q'):
    cv2.destroyAllWindows()


