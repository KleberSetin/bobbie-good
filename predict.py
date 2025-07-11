from PIL import Image, ImageFilter

def predict(image: Image.Image) -> Image.Image:
    # Converte para escala de cinza e aplica filtro de borda
    gray = image.convert("L")
    edge = gray.filter(ImageFilter.FIND_EDGES)
    # Binariza a imagem (preto e branco puro)
    binarized = edge.point(lambda x: 0 if x < 100 else 255, '1')
    return binarized