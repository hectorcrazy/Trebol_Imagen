from PIL import Image
from PIL.ExifTags import TAGS
import sys
imagename = input("Directorio de la Imagen: ")
image = Image.open(imagename)
exifdata = image.getexif()
for tag_id in exifdata:
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:25}: {data}")
