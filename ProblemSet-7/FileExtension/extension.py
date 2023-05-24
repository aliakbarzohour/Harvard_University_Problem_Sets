# ==============================================================

# What should I have done?

# This code takes a filename as input and prints the 
# corresponding file MIME type.

# ==============================================================

filename = input("[$] Enter file name: ")

if not "." in filename:
    print("application/octet-stream")
else:
    ext = filename.split(".")[-1].strip()
    if ext.lower() == "gif":
        print("image/gif")
    elif ext.lower() == "jpg" or ext.lower() == "jpeg":
        print("image/jpeg")
    elif ext.lower() == "png":
        print("image/png")
    elif ext.lower() == "txt":
        print("text/plain")
    elif ext.lower() == "pdf":
        print("application/pdf")
    elif ext.lower() == "zip":
        print("application/zip")
    else:
        print("application/octet-stream")
