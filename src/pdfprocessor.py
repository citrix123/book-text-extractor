#
# This Lib is responsible for converting pdf to Image.
# @author Rahul Jain
#

from pdf2image import convert_from_path
import os
import sys
import pytesseract
import io

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

def processOCR(img):
    print img
    a = pytesseract.image_to_string(img, lang='hin+eng')
    f = io.open(img + ".txt", "w+", encoding='utf8')
    f.write(a)
    f.close()

if __name__ == "__main__":
    print (sys.argv)
    allFiles = os.listdir("outputs/")
    jpg_files = filter(lambda x: x[-4:] == '.jpg', allFiles)
    for i in jpg_files:
        #processOCR("./outputs/book_page200.jpg")
        processOCR("./outputs/" + i)
    #convertToImage(sys.argv[1], "./outputs/")
