from PIL import Image
from io import BytesIO
import requests
import os
import logging

logger = logging.getLogger(__name__)


def add(x, y):
    z = x + y
    print(z)
