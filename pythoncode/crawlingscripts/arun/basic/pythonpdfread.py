import pyPdf
from StringIO import StringIO

'''def getPDFContent(path):
    content = ""
    num_pages = 100
    p = file(path, "rb")
    pdf = pyPdf.PdfFileReader(p)
    for i in range(0, num_pages):
        content += pdf.getPage(i).extractText() + "\n"
    content = " ".join(content.replace(u"\xa0", " ").strip().split())
    return content'''
    
import pyPdf
pdf = pyPdf.PdfFileReader(open("/home/aknauhwar/Desktop/sql reference/sqlalchemy.pdf", "rb"))
for page in pdf.pages:
    print page.extractText()
    
    
    
'''f= open('/home/aknauhwar/Desktop/test.txt','w')
pdfl = getPDFContent("/home/aknauhwar/Desktop/sebsauvage_net_python_snyppets__getlinks1.pdf").encode("ascii", "ignore")
#f.write(pdfl)


pdfContent = StringIO(getPDFContent("/home/aknauhwar/Desktop/sql reference/sqlalchemy.pdf").encode("ascii", "ignore"))
for line in pdfContent:
    print line.strip() 
    f.write(line)    
    
    
f.close()'''