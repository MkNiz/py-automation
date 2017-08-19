import zipfile, os

cwd = os.getcwd()

myZip = zipfile.ZipFile('myZip.zip')

print("Contents of zip file:\n")
for item in myZip.namelist():
    print(item + ":")
    item_info = myZip.getinfo(item)
    print("Size(Full):", item_info.file_size, "\tSize(Compressed):", item_info.compress_size)
    compression = item_info.file_size - item_info.compress_size
    print("Compression:", compression, "\n")
    