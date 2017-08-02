import zipfile, os

# Create zip and compress the data directory in it
myNewZip = zipfile.ZipFile('zippy.zip', 'w')
for dir, _, files in os.walk('data'):
    myNewZip.write(dir, compress_type=zipfile.ZIP_DEFLATED)
    for f in files:
        myNewZip.write(os.path.join(dir, f), compress_type=zipfile.ZIP_DEFLATED)
myNewZip.close()
print("data directory added to archive.")

# Reopen in append mode to add a single item
appendMyZip = zipfile.ZipFile('zippy.zip', 'a')
appendMyZip.write('hello.txt', compress_type=zipfile.ZIP_DEFLATED)
appendMyZip.close()
print("hello.txt added to archive.")