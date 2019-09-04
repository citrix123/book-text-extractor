#
# This Lib is responsible for converting pdf to Image.
# @author Rahul Jain
#

from pdf2image import convert_from_path
import os
import sys

def convertToImage(pdfFile, outputDir):
    pages = convert_from_path(pdfFile) #('../Data/test.pdf')

    # Create Dir if not exists
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    # filename = getFilename(count, pdf)
    count = 0
    for page in pages:
        imgFile = outputDir + "/book_page" + str(count) + ".jpg"
        page.save(imgFile, 'JPEG')
        count += 1

if __name__ == "__main__":
    print (sys.argv)
    convertToImage(sys.argv[1], "./outputs/")
