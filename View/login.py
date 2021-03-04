import tkinter
from Controller import validate

def window_login():
    window = tkinter.Tk()

    window.title("Login")

    window.minsize(width=600, height=400)
    window.maxsize(width=600, height=400)

    label = tkinter.Label(window,text="Inicio de Sesión",fg="white",bg="#1B2631",width="300",height="3")
    label.config(font=("Helvetica",12))
    label.pack()

    label_email = tkinter.Label(window,text="Correo:")
    label_email.place(x=150,y=95)
    entry_email = tkinter.StringVar()
    input_email = tkinter.Entry(window,textvariable=entry_email)
    input_email.place(x=150,y=120,width=300,height=30)

    label_password = tkinter.Label(window,text="Contraseña:")
    label_password.place(x=150,y=175)
    entry_password = tkinter.StringVar()
    input_password = tkinter.Entry(window,textvariable=entry_password,show="*")
    input_password.place(x=150,y=200,width=300,height=30)

    button_setBarcode = tkinter.Button(window,text="Iniciar sesión",bg="#C2C2C2",fg="#000000",width="20",command=lambda:validate.validate_onlyLetters(email=entry_email.get(),password=entry_password.get()))
    button_setBarcode.place(x=220,y=270)

    window.mainloop()

    

if __name__=="__main__":
    window_login()