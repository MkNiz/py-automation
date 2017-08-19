import PyPDF2

# Open file
alice_file = open('alice.pdf', 'rb')

# Create reader object
alice_reader = PyPDF2.PdfFileReader(alice_file)

# Create writer object
alice_writer = PyPDF2.PdfFileWriter()

print("File loaded and reader and writer objects established")
# Store pages from file when the number is even
for pn in range(alice_reader.numPages):
    if (pn+1) % 2 == 0:
        print("Adding page " + str(pn+1) + " to writer...")
        pObj = alice_reader.getPage(pn)
        alice_writer.addPage(pObj)

print("Finished adding pages to writer.\n")
# Write file from writer contents
print("Writing copied file...")
alice_even_file = open('alice_even.pdf', 'wb')
alice_writer.write(alice_even_file)

print("Done.")
alice_even_file.close()
alice_file.close()