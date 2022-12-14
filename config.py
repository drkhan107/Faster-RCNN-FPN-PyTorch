import torch

BATCH_SIZE = 4 # increase / decrease according to GPU memeory
RESIZE_TO = 360 # resize the image for training and transforms
NUM_EPOCHS = 100 # number of epochs to train for
NUM_WORKERS = 4

DEVICE = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
  
# Images and labels direcotry should be relative to train.py
TRAIN_DIR_IMAGES = '/content/train'
TRAIN_DIR_LABELS = '/content/train'
VALID_DIR_IMAGES = '/content/valid'
VALID_DIR_LABELS = '/content/valid'

# classes: 0 index is reserved for background
CLASSES = [
    '__background__',
    'alternaria','damaged', 'insect','insectspot', 'mlb', 'mossaic', 'necrosis', 'pwm', 'scab',
]

NUM_CLASSES = len(CLASSES)

# whether to visualize images after creating the data loaders
VISUALIZE_TRANSFORMED_IMAGES = False

# location to save model and plots
OUT_DIR = 'outputs'