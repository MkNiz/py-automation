import zipfile, os

dest_path = os.path.join(os.getcwd(), 'extracted')

myZip = zipfile.ZipFile('myZip.zip')
# Extract single file in zip
myZip.extract('hello.txt')
# Extract everything in the zip, to a new directory
myZip.extractall(dest_path)
print("Extracted")