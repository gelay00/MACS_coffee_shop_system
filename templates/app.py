from flask import Flask, render_template, request

app = Flask(__name__)

# Menu with drinks & pastries
menu = {
    "Espresso": 80,
    "Americano": 90,
    "Cappuccino": 100,
    "Latte": 110,
    "Mocha": 120,
    "Ube Cheese Pandesal": 130,
    "Pande Asado": 199,
    "Cheese Roll": 199,
    "Choco Banana Cupcakes": 150,
    "Classic Cheesy Ensaymada": 199,
    "Cinnamon Roll": 249,
}

@app.route("/")
def index():
    return render_template("menu.html", menu=menu)

@app.route("/receipt", methods=["POST"])
def receipt():
    order = {}
    total = 0
    for item, price in menu.items():
        qty = request.form.get(item)
        if qty and qty.isdigit() and int(qty) > 0:
            qty = int(qty)
            order[item] = {"qty": qty, "price": price, "subtotal": qty * price}
            total += qty * price
    return render_template("receipt.html", order=order, total=total)

if __name__ == "__main__":
    app.run(debug=True)
