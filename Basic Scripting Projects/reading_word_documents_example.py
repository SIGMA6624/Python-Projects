import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)

    return '\n'.join(fullText)

print(getText('D:\Documents\Hobby\Automate the Boring Stuff With Python\Word_Files_To_Edit\demo.docx'))
