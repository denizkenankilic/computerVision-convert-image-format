from PIL import Image
import os

inputPath = r'\\aerosrv2\e$\processed\WPAFB-21Oct2009\Data\TRAIN_SELF-TEST_SELF-EVAL\stabilized_croped_stabilized_cropped\AOI_41\tracked'

def convertImageFormat(fromFormat,toFormat):
    outputPath = inputPath + '/tracked_'+ toFormat
    if not os.path.exists(outputPath):
        os.makedirs(outputPath)

    for root, dirs, files in os.walk(inputPath):
        for fname in files:
            if fname.endswith(fromFormat):
                Image.open(os.path.join(inputPath,fname)).save(os.path.join(outputPath,os.path.splitext(fname)[0]+'.',toFormat))

convertImageFormat('jpg','bmp')



