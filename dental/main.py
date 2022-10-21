import torch
import numpy as np
import pycocotools
from torchvision.models.detection import fasterrcnn_resnet50_fpn
import os

os.system('cls')

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
CLASSES = []
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))