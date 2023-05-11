import customtkinter, modules.app, modules.button_functions

add_picture = customtkinter.CTkButton(
    master = modules.app.main_app, 
    width = 100, 
    height = 50, 
    command = modules.button_functions.picture, 
    border_width= 3,
    text = "Нова картинка",
    fg_color = "#302f2b",
    border_color = "#d36f23",
    hover_color = "#c67538"
)

save_picture = customtkinter.CTkButton(
    master = modules.app.main_app, 
    width = 100, 
    height = 50, 
    command = modules.button_functions.save, 
    border_width= 3,
    text = "Зберегти",
    fg_color = "#302f2b",
    border_color = "#d36f23",
    hover_color = "#c67538"
)

crop = customtkinter.CTkButton(
    master=modules.app.main_app,
    fg_color = "#302f2b",
    border_color = "#d36f23",
    hover_color = "#c67538",
    width=100,
    height=50,
    text="Обрiзати",
    border_width=3,
    command = modules.button_functions.picture_crop
)

filters = customtkinter.CTkButton(
    master=modules.app.main_app,
    fg_color = "#302f2b",
    border_color = "#d36f23",
    hover_color = "#c67538",
    width=100,
    height=50,
    text="Фiльтр",
    border_width=3,
    command = modules.button_functions.filters
)

add_picture.place(x=20, y=20)
save_picture.place(x=20, y=80)
crop.place(x=20, y=140)
filters.place(x=20, y=200)