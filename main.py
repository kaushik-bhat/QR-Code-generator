import qrcode
import os
from tkinter import Tk, Label, Entry, Button, filedialog, colorchooser, StringVar, Frame
from tkinter.font import Font
from tkinter.scrolledtext import ScrolledText

def generate_qr_code():
    data_to_encode = data_entry.get("1.0", "end-1c")
    file_name = file_entry.get()

    # Handle file_name extension
    base_name, ext = os.path.splitext(file_name)
    if ext != ".png":
        file_name = base_name + ".png"

    save_path = filedialog.askdirectory()
    if not save_path:
        return
    
    save_full_path = os.path.join(save_path, file_name)

    qr_code = qrcode.QRCode(version=4, box_size=80, border=5)

    qr_code.add_data(data_to_encode)
    qr_code.make(fit=True)

    fill_color = fill_color_var.get()
    back_color = back_color_var.get()

    generate_image = qr_code.make_image(fill_color=fill_color, back_color=back_color)
    generate_image.save(save_full_path)

    result_label.config(text=f"QR code generated and saved as {save_full_path}")

def choose_fill_color():
    color_code = colorchooser.askcolor(title="Choose fill color")
    if color_code[1]:  # Check if a color was selected
        fill_color_var.set(color_code[1])

def choose_back_color():
    color_code = colorchooser.askcolor(title="Choose background color")
    if color_code[1]:  # Check if a color was selected
        back_color_var.set(color_code[1])

root = Tk()
root.title("QR Code Generator")

# Set window background color and border
root.configure(bg="white")
root.geometry("800x500")
root.resizable(False, False)

# Define a font
app_font = Font(family="Helvetica", size=12, weight="bold")

# Create a frame to hold all widgets
frame = Frame(root, bg="white", padx=20, pady=20, highlightbackground="black", highlightthickness=1)
frame.pack(expand=True, fill="both")

Label(frame, text="Data to encode:", font=app_font, bg="white").grid(row=0, column=0, padx=10, pady=10, sticky="e")
data_entry = ScrolledText(frame, width=50, height=10, font=app_font, wrap='word')
data_entry.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

Label(frame, text="File name:", font=app_font, bg="white").grid(row=1, column=0, padx=10, pady=10, sticky="e")
file_entry = Entry(frame, width=50, font=app_font)
file_entry.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

Label(frame, text="Fill color:", font=app_font, bg="white").grid(row=2, column=0, padx=10, pady=10, sticky="e")
fill_color_var = StringVar(value="black")
Button(frame, text="Choose fill color", command=choose_fill_color, font=app_font, bg="white", relief="solid", borderwidth=1).grid(row=2, column=1, padx=10, pady=10, sticky="w")
Label(frame, textvariable=fill_color_var, font=app_font, bg="white").grid(row=2, column=2, padx=10, pady=10, sticky="w")

Label(frame, text="Background color:", font=app_font, bg="white").grid(row=3, column=0, padx=10, pady=10, sticky="e")
back_color_var = StringVar(value="white")
Button(frame, text="Choose background color", command=choose_back_color, font=app_font, bg="white", relief="solid", borderwidth=1).grid(row=3, column=1, padx=10, pady=10, sticky="w")
Label(frame, textvariable=back_color_var, font=app_font, bg="white").grid(row=3, column=2, padx=10, pady=10, sticky="w")

Button(frame, text="Generate QR Code", command=generate_qr_code, font=app_font, bg="black", fg="white", relief="solid", borderwidth=1).grid(row=4, column=1, padx=10, pady=20)
result_label = Label(frame, text="", font=app_font, bg="white")
result_label.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
