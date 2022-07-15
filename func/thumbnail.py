from PIL import Image
from io import BytesIO
import requests
import os
import logging

logger = logging.getLogger(__name__)

def create_thumbnail(url, filename):
    filepath = f'{os.environ.get("STATIC_DIR")}/{filename}' 
    logger.info('Begin creation of thumbnail')
    content = requests.get(url).content
    with Image.open(BytesIO(content)) as img:
        img.thumbnail((128, 128))
        img.save(filepath)
    logger.info('Finished creation of thumbnail')
    return filepath
