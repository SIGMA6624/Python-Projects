import PyPDF2
import os

os.getcwd()
#'D:\\Documents\\Hobby\\Automate the Boring Stuff With Python\\PDF_Files_To_Read_and_Edit'

#pdfFile = open('meetingminutes1.pdf', 'rb')
pdf1File = open('meetingminutes1.pdf', 'rb')   #'rb' is read binary
pdf2File = open('meetingminutes2.pdf', 'rb')
reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)

writer = PyPDF2.PdfFileWriter()
for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

	
for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

outputFile = open('combinedminutes.pdf', 'wb')   #create a pdf "combinedminutes.pdf". Writer is just a pdf that only exists in computer memory, not hard drive.
writer.write(outputFile)
outputFile.close()
pdf1File.close()
pdf2File.close()

