import PyPDF2

# Open file
alice_file = open('alice.pdf', 'rb')

# Create reader object
alice_reader = PyPDF2.PdfFileReader(alice_file)

# Create writer object
alice_writer = PyPDF2.PdfFileWriter()

print("File loaded and reader and writer objects established")

# Get the first page, which will be the merge target for all other pages
pFirst = alice_reader.getPage(0)

# Store pages from file when the number is even
for pn in range(1, alice_reader.numPages):
    print("Merging page " + str(pn+1) + " to the first page...")
    pObj = alice_reader.getPage(pn)
    # Merge this page with the first
    pFirst.mergePage(pObj)

# Add the completed page to the writer
alice_writer.addPage(pFirst)

print("Finished adding pages to writer.\n")
# Write file from writer contents
print("Writing copied file...")
alice_one_file = open('alice_is_one_page.pdf', 'wb')
alice_writer.write(alice_one_file)

print("Done.")
alice_one_file.close()
alice_file.close()