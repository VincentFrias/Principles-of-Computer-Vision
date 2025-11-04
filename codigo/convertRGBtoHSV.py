import cv2
import numpy as np
from PIL import Image

# === Equalização de histograma (por canal, para imagens coloridas) ===
def equalizar_histograma_colorido(img: np.ndarray) -> np.ndarray:
    """
    Equaliza o histograma de uma imagem colorida, aplicando a equalização
    em cada canal separadamente.
    """
    canais = cv2.split(img)
    canais_eq = [cv2.equalizeHist(canal) for canal in canais]
    return cv2.merge(canais_eq)


# === Conversão manual de RGB para HSV ===
def rgb_to_hsv_manual(img_bgr: np.ndarray) -> np.ndarray:
    """
    Converte uma imagem BGR (OpenCV) para HSV manualmente.
    Retorna imagem no formato HSV com escala:
      H ∈ [0,180], S,V ∈ [0,255]
    """
    img_bgr = img_bgr.astype(np.float32) / 255.0
    b, g, r = cv2.split(img_bgr)

    cmax = np.maximum.reduce([r, g, b])
    cmin = np.minimum.reduce([r, g, b])
    delta = cmax - cmin

    h = np.zeros_like(cmax)
    mask = delta != 0

    # Hue (H)
    h[mask & (cmax == r)] = ((g - b) / delta)[mask & (cmax == r)] % 6
    h[mask & (cmax == g)] = ((b - r) / delta)[mask & (cmax == g)] + 2
    h[mask & (cmax == b)] = ((r - g) / delta)[mask & (cmax == b)] + 4
    h = (h * 60) % 360

    # Saturation (S)
    s = np.zeros_like(cmax)
    s[cmax != 0] = delta[cmax != 0] / cmax[cmax != 0]

    # Value (V)
    v = cmax

    # Converte para formato OpenCV
    h = (h / 2).astype(np.uint8)       # 0–180
    s = (s * 255).astype(np.uint8)     # 0–255
    v = (v * 255).astype(np.uint8)     # 0–255

    return cv2.merge([h, s, v])


# === Início do processamento ===
if __name__ == "__main__":
    # Lê imagem RGB
    img_bgr = cv2.imread("./img/img02.jpeg")
    if img_bgr is None:
        raise FileNotFoundError("Não foi possível carregar ./img/img02.jpeg")

    # Equaliza imagem RGB diretamente
    img_eq_rgb = equalizar_histograma_colorido(img_bgr)
    cv2.imwrite("./img/convert/saida_rgb_equalizada.png", img_eq_rgb)
    cv2.imshow("RGB Equalizada", img_eq_rgb)

    # Conversão manual RGB → HSV
    img_hsv = rgb_to_hsv_manual(img_bgr)

    # Equaliza apenas o canal V (brilho)
    H, S, V = cv2.split(img_hsv)
    V_eq = cv2.equalizeHist(V)
    img_eq_hsv = cv2.merge([H, S, V_eq])

    # Converte HSV → RGB (para visualização e salvamento)
    img_eq_hsv_to_rgb = cv2.cvtColor(img_eq_hsv, cv2.COLOR_HSV2BGR)
    cv2.imwrite("./img/convert/saidaHSVtoRGB.png", img_eq_hsv_to_rgb)
    cv2.imshow("HSV Equalizada", img_eq_hsv_to_rgb)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
