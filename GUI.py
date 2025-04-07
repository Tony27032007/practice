import customtkinter

def button_callback():
    print("button clicked")

customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("1920x1080")

button = customtkinter.CTkButton(app, text="my button", fg_color='green', command=button_callback)
button.pack(padx=20, pady=20)

app.mainloop()
