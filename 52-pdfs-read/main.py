import PyPDF2

book = open('alice.pdf', 'rb')
reader = PyPDF2.PdfFileReader(book)

print("alice.pdf has " + str(reader.numPages) + " pages.")

for i in range(0, 5):
    page = reader.getPage(i)
    pageText = page.extractText()
    print(pageText)
    print("\n [PAGE: " + str(i+1) + "]\n----------\n")