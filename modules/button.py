import customtkinter, modules.app, modules.button_functions

add_picture = customtkinter.CTkButton(master=modules.app.main_app, width=100, height=50, command=modules.button_functions.picture, text="Нова картинка")
add_picture.place(x=20, y=20)