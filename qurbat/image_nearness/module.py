import torch
import torchvision.models as models
from PIL import Image
from qurbat.image_nearness.utils import compose_image
import argparse


def load_pretrained_model():
    """

    :return:  model with FC layer removed
    """
    model = models.resnet18(pretrained=True, progress=True)
    for layer in model.parameters():
        layer.requires_grad = False
    feature_model = torch.nn.Sequential(*(list(model.children())[:-1]))
    return feature_model


def get_features(image_path: str):
    """

    :param image_path: image path
    :return: 1-D vector features
    """
    feature_model = load_pretrained_model()
    image = Image.open(image_path).convert('RGB')
    pre_process = compose_image(size_height=224, size_width=224)
    out_features = feature_model(torch.unsqueeze(pre_process(image), 0))
    return out_features.squeeze(-1).squeeze(-1).detach().numpy()


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--img1", help="provide image one")
    arguments = args.parse_args()

    print(get_features(arguments.img1))


