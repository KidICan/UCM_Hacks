# from cStringIO import StringIO
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from pdfminer.pdfpage import PDFPage
# import os
# import sys, getopt
#
# #converts pdf, returns its text content as a string
# def convert(fname, pages=None):
#     if not pages:
#         pagenums = set()
#     else:
#         pagenums = set(pages)
#
#     output = StringIO()
#     manager = PDFResourceManager()
#     converter = TextConverter(manager, output, laparams=LAParams())
#     interpreter = PDFPageInterpreter(manager, converter)
#
#     infile = file(fname, 'rb')
#     for page in PDFPage.get_pages(infile, pagenums):
#         interpreter.process_page(page)
#     infile.close()
#     converter.close()
#     text = output.getvalue()
#     output.close
#     return text
#
#
# #converts all pdfs in directory pdfDir, saves all resulting txt files to txtdir
# def convertMultiple(pdfDir, txtDir):
#     if pdfDir == "": pdfDir = os.getcwd() + "\\" #if no pdfDir passed in
#     for pdf in os.listdir(pdfDir): #iterate through pdfs in pdf directory
#         fileExtension = pdf.split(".")[-1]
#         if fileExtension == "pdf":
#             pdfFilename = pdfDir + pdf
#             text = convert(pdfFilename) #get string of text content of pdf
#             textFilename = txtDir + pdf + ".txt"
#             textFile = open(textFilename, "w") #make text file
#             textFile.write(text) #write text to text file
#
# pdfDir = "./pdfs/"
# txtDir = "./txt/"
# convertMultiple(pdfDir, txtDir)


from __future__ import print_function
from wand.image import Image

with Image(filename='pdfs/master.pdf', resolution = 600) as img:
    print('pages = ', len(img.sequence))

    with img.convert('png') as converted:
        converted.units='pixelsperinch'
        converted.save(filename='pyout/page.png')






# from wand.image import Image
# # Converting first page into JPG
# with Image(filename="pdfs/master.pdf[0]") as img:
#      img.save(filename="temp.jpg")
# Resizing this image
# with Image(filename="temp.jpg") as img:
#      img.resize(200, 150)
#      img.save(filename="thumbnail_resize.jpg")
