import qrcode
import qrcode.image.svg
import customtkinter as ctk
from PIL import Image
from tkinter import filedialog
import os
import subprocess as subpro

# Functions:
def Generate():
    global FileType
    global FileName
    global FilePath
    global FileData
    if FilePathVariableForFileTypeDropDown.get() == "Use the explorer icon":
        FilePath = FilePathExplorerVar
    elif FilePathVariableForFileTypeDropDown.get() == "Enter a file path":
        FilePath = PathVariableForFilePathEntry.get().replace('/', '\\')
    FileType = FileTypeVariableForFileTypeDropDown.get().lower()
    FileName = FileNameVariableForFileNameEntry.get()
    FileData = FileDataVariableForFileDataEntry.get()
    
    if os.path.exists(FilePath):
        GenerateButton.configure(state="disabled")
        GenerateButton.configure(text="Generated!")
        FileTypeDropdown.configure(state="disabled")
        FileNameEntry.configure(state="disabled")
        FilePathEntry.configure(state="disabled")
        FileDataEntry.configure(state="disabled")
        FilePathOptionMenu.configure(state="disabled")
        FilePathLabel.configure(text_color="green", text="Vaild path.")
        FilePathLabel.place(x=300, y=93)
        if FilePath == ".svg":
            svg(FileType, FileName, FilePath, FileData)
        else:
            normal(FileType, FileName, FilePath, FileData)
        FinishLabel.configure(text=f"Generated in: \"{FilePath}\". The QR Code's name is: \"{FileName}{FileType}\". The QR Code's data is: \"{FileData}\".", text_color="green")
        FinishLabel.place(x=5, y=250)
        Finish(FilePath, FileName, FileType)
        GenerateButton.configure(state="normal")
        GenerateButton.configure(text="Generate!")
        FileTypeDropdown.configure(state="normal")
        FileNameEntry.configure(state="normal")
        FilePathEntry.configure(state="normal")
        FileDataEntry.configure(state="normal")
        FilePathOptionMenu.configure(state="normal")
    else:
        FilePathLabel.configure(text="Path Does not exist. Please enter a valid directory:", text_color="red")
        FilePathLabel.place(x=145, y=93)
def normal(FileType, FileName, FilePath, FileData):
    qrcode.make(FileData).save(f"{FilePath}\{FileName}{FileType}")

def svg(FileType, FileName, FilePath, FileData):
    qrcode.make(FileData, image_factory=qrcode.image.svg.SvgPathImage).save(f"{FilePath}\\{FileName}{FileType}")
    
def OpenInPhoto():
    Image.open(f"{FilePath}\{FileName}{FileType}").show()

def OpenInExplorer():
    subpro.Popen(f'explorer "{FilePath}"')

def ChoosePathUsingExplorer():
    global FilePathExplorerVar
    FilePathExplorerVar = filedialog.askdirectory().replace('/', '\\')
    FilePathEntry.configure(state="normal")
# Variables:
size = "700x700"

# WIN:
WIN = ctk.CTk()
WIN.geometry(size)
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
WIN.title("QR Code Generator")

# Draw:
GenerateButton = ctk.CTkButton(WIN, text="Generate!", command=Generate, width=250, height=60, font=ctk.CTkFont(family="TkDefaultFont", size=35))
GenerateButton.pack(padx=0, pady=20)

FileTypeVariableForFileTypeDropDown = ctk.StringVar(value=".JPEG")
FileTypeDropdown = ctk.CTkOptionMenu(WIN, values=[".JPEG", ".PNG", ".SVG", ".GIF", ".TIFF", ".PSD", ".GIMP", ".EPS", ".AI", ".INDD", ".RAW"], variable=FileTypeVariableForFileTypeDropDown, width=175, height=45, font=ctk.CTkFont(family="TkDefaultFont", size=20), dropdown_font=ctk.CTkFont(family="TkDefaultFont", size=15))

FileTypeLabel = ctk.CTkLabel(WIN, width=100, height=20, text="Enter file type:", font=ctk.CTkFont(family="TkDefaultFont", size=18))

FileTypeLabel.place(x=45, y=6)
FileTypeDropdown.place(x=20, y=33)


FileNameVariableForFileNameEntry = ctk.StringVar()
FileNameEntry = ctk.CTkEntry(WIN, width=175, height=45, font=ctk.CTkFont(family="TkDefaultFont", size=16), textvariable=FileNameVariableForFileNameEntry)
FileNameLabel = ctk.CTkLabel(WIN, width=100, height=20, text="Enter file name:", font=ctk.CTkFont(family="TkDefaultFont", size=18))
FileNameLabel.place(x=525, y=6)
FileNameEntry.place(x=505, y=33)


PathVariableForFilePathEntry = ctk.StringVar()
FilePathEntry = ctk.CTkEntry(WIN, width=407, height=45, font=ctk.CTkFont(family="TkDefaultFont", size=16), textvariable=PathVariableForFilePathEntry, placeholder_text="test")
FilePathLabel = ctk.CTkLabel(WIN, width=100, height=20, text="Where to be saved:", font=ctk.CTkFont(family="TkDefaultFont", size=18))
FilePathEntry.place(x=213, y=120)
FilePathLabel.place(x=342, y=93)
FilePathExplorerButton = ctk.CTkButton(WIN, text="", command=ChoosePathUsingExplorer, image=ctk.CTkImage(light_image=Image.open("./Window/OpenInExplorerIcon.png")), width=60, height=45)
FilePathExplorerButton.place(x=630, y=120)
FilePathVariableForFileTypeDropDown = ctk.StringVar(value="Use the explorer icon")
FilePathOptionMenu = ctk.CTkOptionMenu(WIN, values=["Use the explorer icon", "Enter a file path"], variable=FilePathVariableForFileTypeDropDown, width=193, height=45, font=ctk.CTkFont(family="TKDefaultFont", size=15), dropdown_font=ctk.CTkFont(family="TKDefaultFont", size=15))
FilePathOptionMenu.place(x=10, y=120)
FilePathOptionMenuLabel = ctk.CTkLabel(WIN, text="Choose how to select file path:", width=100, height=20, font=ctk.CTkFont(family="TKDefaultFont", size=16))
FilePathOptionMenuLabel.place(x=10, y=95)


FileDataVariableForFileDataEntry = ctk.StringVar()
FileDataEntry = ctk.CTkEntry(WIN, width=675, height=45, font=ctk.CTkFont(family="TkDefaultFont", size=16), textvariable=FileDataVariableForFileDataEntry)
FileDataLabel = ctk.CTkLabel(WIN, width=100, height=20, text="QR Code Data:", font=ctk.CTkFont(family="TkDefaultFont", size=18))
FileDataEntry.place(x=12.5, y=205)
FileDataLabel.place(x=284, y=177)


FinishLabel = ctk.CTkLabel(WIN, width=600, wraplength=685, font=ctk.CTkFont(family="TkDefaultFont", size=18), text_color="green")


def CheckPathMethod():
    if FilePathVariableForFileTypeDropDown.get() == "Use the explorer icon":
        FilePathExplorerButton.configure(state="normal")
        FilePathEntry.configure(state="disabled")
    if FilePathVariableForFileTypeDropDown.get() == "Enter a file path":
        FilePathExplorerButton.configure(state="disabled")
        FilePathEntry.configure(state="normal")
    WIN.after(100, CheckPathMethod)

def Finish(FilePath, FileName, FileType):
    ImageLabel = ctk.CTkLabel(WIN, image=ctk.CTkImage(light_image=Image.open(f"{FilePath}//{FileName}{FileType}"), size=(300, 300)), text="")
    ImageLabel.place(x=213, y=388)
    ImageTextLabel = ctk.CTkLabel(WIN, text="QR Code Preview:", font=ctk.CTkFont(family="TkDefaultFont", size=18), width=100, height=20)
    ImageTextLabel.place(x=217, y=358)
    global OpenInPhotoButton
    global OpenInExplorerButton
    OpenInPhotoButton = ctk.CTkButton(WIN, text="", command=OpenInPhoto, image=ctk.CTkImage(light_image=Image.open("./Window/OpenInPhotoIcon.png")), width=20, height=23)
    OpenInPhotoButton.place(x=470, y=355)
    OpenInExplorerButton = ctk.CTkButton(WIN, text="", command=OpenInExplorer, image=ctk.CTkImage(light_image=Image.open("./Window/OpenInExplorerIcon.png")), width=20, height=23)
    OpenInExplorerButton.place(x=420, y=355)
# Main Loop:
WIN.iconbitmap("./Window/QRCodeIconWindow.ico")
WIN.resizable(False, False)
CheckPathMethod()
WIN.mainloop()