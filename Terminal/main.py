import qrcode
import qrcode.image.svg 
def png():
    while True:
        data = input("What data do you want the QRcode to have: ")
        name = input("What do you want the name of the QRcode file to have (DONT INCLUE THE FILE TYPE): ")
        try:
            where = input("Where do you want the QRcode to be saved on you device: ")
            img = qrcode.make(data)
            img.save(f"{where}\{name}.png")
            print(f"QRcode has been saved in {where}.")
            break
        except FileNotFoundError:
            print("Invalid file path.")
        except PermissionError:
            print("Invalid file path.")
def jpeg():
    while True:
        data = input("What data do you want the QRcode to have: ")
        name = input("What do you want the name of the QRcode file to have (DONT INCLUE THE FILE TYPE): ")
        try:
            where = input("Where do you want the QRcode to be saved on you device: ")
            img = qrcode.make(data)
            img.save(f"{where}\{name}.jpeg")
            print(f"QRcode has been saved in {where}.")
            break
        except FileNotFoundError:
            print("Invalid file path.")
        except PermissionError:
            print("Invalid file path.")
def svg():
    while True:
        data = input("What data do you want the QRcode to have: ")
        name = input("What do you want the name of the QRcode file to have (DONT INCLUE THE FILE TYPE): ")
        try:
            where = input("Where do you want the QRcode to be saved on you device: ")
            factory = qrcode.image.svg.SvgPathImage
            svg_img = qrcode.make(data, image_factory=factory)
            svg_img.save(f"{where}\{name}.svg")
            print(f"QRcode has been saved in {where}.")
            break
        except FileNotFoundError:
            print("Invalid file path.")
        except PermissionError:
            print("Invalid file path.")
while True:
    print("What type of QRcode do you want: ")
    print("1: .png")
    print("2: .jpeg")
    print("3: .svg")
    type = input()
    if type == "1":
        png()
        break
    if type == "2":
        jpeg()
        break
    if type == "3":
        svg()
        break
    else:
        print("Invalid input. Please enter a number from 1-3.")
input("Press enter to close: ")