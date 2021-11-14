import numpy as np
from ipywidgets import interact, fixed
from PIL import Image
 
def imshow(X, resize=None):
	img = cv2.imread(X)
	res = cv2.resize(img, dsize=(54, 140), interpolation=cv2.INTER_CUBIC)
        return res