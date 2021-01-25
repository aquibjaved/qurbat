from torchvision import transforms
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def compose_image(size_height: int, size_width: int):
    """
    :param size_height: height of the image
    :param size_width:  width of the image
    :return:
    """
    preprocess = transforms.Compose([transforms.Resize((size_height, size_width)),
                                     transforms.ToTensor(),
                                     transforms.Normalize(
                                        mean=[0.485, 0.456, 0.406],
                                        std=[0.229, 0.224, 0.225]
                                     )])

    return preprocess


def get_cosine_similarity(vector_1: np.ndarray, vector_2: np.ndarray):

    return cosine_similarity(vector_1, vector_2)
