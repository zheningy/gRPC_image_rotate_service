import image_pb2
import numpy as np

def decode_image(nl_img):
    is_color = nl_img.color
    width = nl_img.width
    height = nl_img.height
    data = nl_img.data
    re_img = np.frombuffer(data, dtype=np.uint8)
    
    if is_color:
        re_img = np.reshape(re_img, (height, width, 3))
    else:
        re_img = np.reshape(re_img, (height, width))

    return re_img


def encode_imgage(image):
    is_color = False
    if image.ndim == 3 and image.shape[2] == 3:
        is_color = True
    nl_img = image_pb2.NLImage(
        color = is_color,
        data = np.ndarray.tobytes(image), 
        width = image.shape[1],
        height = image.shape[0]
    )
    return nl_img  