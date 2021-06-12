from PIL import Image
import os

inputPath = r'\\example_path_1\example_path_2' # Edit this line to define your path

def convertImageFormat(fromFormat,toFormat):
    outputPath = inputPath + '/tracked_'+ toFormat
    if not os.path.exists(outputPath):
        os.makedirs(outputPath)

    for root, dirs, files in os.walk(inputPath):
        for fname in files:
            if fname.endswith(fromFormat):
                Image.open(os.path.join(inputPath,fname)).save(os.path.join(outputPath,os.path.splitext(fname)[0]+'.',toFormat))

convertImageFormat('jpg','bmp')
