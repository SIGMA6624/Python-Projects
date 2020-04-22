import PyPDF2
#It's important to note that PyPDF2 will not be able to perfectly read PDFs because of the complex file structure of PDFs. However, accdg. to Al no other PDF function comes close to PyPDF2.
import os

os.chdir('D:\Documents\Hobby\Automate the Boring Stuff With Python\PDF_Files_To_Read_and_Edit')

pdfFile = open('meetingminutes1.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)
reader.numPages
19
page = reader.getPage(0)    #index here starts at 0
page.extractText()          #not perfect
"""
'OOFFFFIICCIIAALL  BBOOAARRDD  MMIINNUUTTEESS   Meeting of \nMarch 7\n, 2014\n        \n
The Board of Elementary and Secondary Education shall provide leadership and \ncreate policies
for education that expand opportunities for children, empower \nfamilies and communities,
and advance Louisiana in an increasingly \ncompetitive glob\nal market.\n BOARD \n of ELEMENTARY
\n and \n SECONDARY\n EDUCATION\n  '
"""

for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())

#The extracted text is too long to place here.

