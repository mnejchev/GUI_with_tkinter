from json import loads, dump, load
from PIL import Image, ImageTk

from canvas import *


def homepage():
    frame.delete("all")
    login()
    register()


def register():
    register_button = tk.Button(
        root,
        text=""
             "Register",
        width=20,
        font=("arial", 14),
        activebackground="red",
        activeforeground="pink",
        command=registration
    )
    frame.create_window(350, 400, window=register_button)


def login():
    login_button = tk.Button(
        root,
        text="Login",
        width=20,
        font=("arial", 14),
        activebackground="red",
        activeforeground="pink",
        command=login_window
    )
    frame.create_window(350, 350, window=login_button)


def continue_forward():
    frame.delete("all")
    forward = tk.Button(
        root,
        text="continue",
        width=20,
        font=("arial", 14),
        activebackground="red",
        activeforeground="pink",
        command=products_page
    )
    frame.create_window(350, 150, window=forward)
    frame.create_text(
        350, 100,
        text="WELCOME!",
        font=("Arial", 20),
        fill="red"
    )


def registration():
    frame.delete("all")
    home()

    frame.create_text(200, 200, text="First name:", fill="#FFFFFF", activefill="#EEEE6A")
    frame.create_text(200, 250, text="Last name:", fill="#FFFFFF", activefill="#EEEE6A")
    frame.create_text(200, 300, text="Username:", fill="#FFFFFF", activefill="#EEEE6A")
    frame.create_text(200, 350, text="Password:", fill="#FFFFFF", activefill="#EEEE6A")

    frame.create_window(250, 200, anchor="w", window=first_name_field)
    frame.create_window(250, 250, anchor="w", window=second_name_field)
    frame.create_window(250, 300, anchor="w", window=username_field)
    frame.create_window(250, 350, anchor="w", window=password_field)

    register_button = tk.Button(
        root,
        text="Register",
        width=20,
        font=("arial", 14),
        activebackground="red",
        activeforeground="pink",
        command=info
    )
    frame.create_window(350, 450, window=register_button)


def login_window():
    frame.delete("all")
    home()

    frame.create_text(200, 200, text="Username:", fill="white", activefill="yellow")
    frame.create_text(200, 250, text="Password:", fill="white", activefill="yellow")

    frame.create_window(250, 200, anchor="w", window=username_field)
    frame.create_window(250, 250, anchor="w", window=password_field)
    login_button = tk.Button(
        root,
        text="Login",
        width=20,
        font=("arial", 14),
        activebackground="red",
        activeforeground="pink",
        command=login_check
    )
    frame.create_window(350, 350, window=login_button)


def login_check():
    users = []
    with open("./database.json", "r") as file:
        for line in file:
            users.append(loads(line))

    for user in users:

        if user["Username"] == username_field.get() and user["Password"] == password_field.get():
            frame.delete("all")
            frame.create_text(
                350, 100,
                text="You have logged in!",
                font=("Arial", 20),
                fill="red",
            )
            continue_forward()
            return True
    frame.create_text(
        350, 100,
        text="Wrong username or password!",
        font=("Arial", 20),
        fill="red",
    )
    return False


def home():
    home_button = tk.Button(
        root,
        text="Home",
        width=20,
        font=("arial", 14),
        activebackground="red",
        activeforeground="pink",
        command=homepage
    )
    frame.create_window(350, 400, window=home_button)


def info():
    data = {
        "First name": first_name_field.get(),
        "Second name": second_name_field.get(),
        "Username": username_field.get(),
        "Password": password_field.get()
    }
    print(validity_check(data))
    if validity_check(data):
        with open("./database.json", "a") as file:
            dump(data, file)
            file.write("\n")
        continue_forward()


def validity_check(information: dict):
    saved_info = []
    with open("./database.json", "r") as file:
        for line in file:
            saved_info.append(loads(line))
    frame.delete("error")
    if information["First name"].strip() == "" or information["Second name"].strip() == "":
        frame.create_text(
            350, 100,
            text="You have not entered your names!",
            font=("Arial", 10),
            fill="red",
            tag="error"
        )
    elif not information["First name"].isalpha() or not information["Second name"].isalpha():
        frame.create_text(
            350, 100,
            text="Your names can contain only letters!",
            font=("Arial", 10),
            fill="red",
            tag="error"
        )

    elif information["Username"].strip() == "":
        frame.create_text(
            350, 100,
            text="You have not entered an username!",
            font=("Arial", 10),
            fill="red",
            tag="error"
        )
    elif not information["Username"].isalnum() or not information["Password"].isalnum():
        frame.create_text(
            350, 100,
            text="Username and password can contain only letters and digits!",
            font=("Arial", 10),
            fill="red",
            tag="error"
        )
    else:
        for reg_info in saved_info:
            if reg_info["Username"] == information["Username"]:
                frame.create_text(
                    350, 100,
                    text="Username already exists!",
                    font=("Arial", 10),
                    fill="red",
                    tag="error"
                )
                return False
        else:
            return True
    return False


def products_page():
    frame.delete("all")
    global product_info
    with open("./products.json", "r") as stock:
        product_info = load(stock)
    print(product_info.items())
    x = 150
    y = 50

    for name, item in product_info.items():
        image = ImageTk.PhotoImage(Image.open(item["image"]).resize((100, 130)))
        images.append(image)
        frame.create_text(
            x, y,
            text=name,
            font=("Comic Sans MS", 12),
            fill="pink"
        )
        frame.create_image(
            x, y + 100,
            image=image
        )
        if item["quantity"] >= 1:
            color = "green"
            text = f"In stock : {item['quantity']}"
            buy_button = tk.Button(
                root,
                text="Buy",
                font=("Comic Sans MS", 15),
                bg="green",
                fg="white",
                width=5,
                command=lambda name=name: buy_product(name)
            )
            frame.create_window(x, y + 230, window=buy_button)
        else:
            color = "red"
            text = "Out of stock"
        frame.create_text(
            x, y + 180,
            text=text,
            fill=color,
            font=("Comic Sans MS", 15)
        )
        x += 200
        if x > 550:
            x = 150
            y += 230


def buy_product(name_of_product):

    product_info[name_of_product]["quantity"] -= 1

    with open("./products.json", "w") as stock:
        dump(product_info, stock)

    products_page()


images = []

first_name_field = tk.Entry(
    root,
    width=20,
    font=("Arial", 12),
    bg="grey",
)
second_name_field = tk.Entry(
    root,
    width=20,
    font=("Arial", 12),
    bg="grey",
)
username_field = tk.Entry(
    root,
    width=20,
    font=("Arial", 12),
    bg="grey",
)
password_field = tk.Entry(
    root,
    width=20,
    font=("Arial", 12),
    bg="grey",
    show='*'
)
