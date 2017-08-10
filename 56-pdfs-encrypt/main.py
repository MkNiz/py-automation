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
    print("Adding page " + str(pn+1) + " to the writer...")
    pObj = alice_reader.getPage(pn)
    alice_writer.addPage(pObj)

# Encrypt the file stored in the writer
alice_writer.encrypt('abc123')

print("Finished adding pages to writer.\n")
# Write file from writer contents
print("Writing copied file...")
alice_encrypted = open('alice_encrypted.pdf', 'wb')
alice_writer.write(alice_encrypted)

print("Done.")
alice_encrypted.close()
alice_file.close()