import numpy as np
from ipywidgets import interact, fixed
from PIL import Image
 
def imshow(X, resize=None):
	imageB_array = resize(X, (100, 500), anti_aliasing=True)
