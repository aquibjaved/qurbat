from torchvision import transforms
from PIL import Image


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


