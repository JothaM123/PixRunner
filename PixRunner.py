print("PixRunner v1.0 | The pixel based image maker.")

while 1:
    
    file = input("Enter file name to open - ")

    if file.endswith(".pix"):
        f = open(file, "r")
        img = f.read().replace("0"," ").replace("1","█")
        print(img)