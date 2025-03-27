from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/shop")
def shop():
    # Example product data (In real case, this will be from a database)
    products = [
        {"id": 1, "name": "Smartphone", "price": 499.99, "image": "static/images/smartphone.jpg"},
        {"id": 2, "name": "Laptop", "price": 899.99, "image": "static/images/product2.jpg"},
        {"id": 3, "name": "Wireless Headphones", "price": 199.99, "image": "static/images/product3.jpg"},
    ]
    return render_template("shop.html", products=products)

@app.route("/product/<int:product_id>")
def product(product_id):
    # Example product details (In real case, fetch from database)
    products = {
        1: {"name": "Smartphone", "price": 499.99, "description": "Latest smartphone with 128GB storage", "image": "static/images/smartphone.jpg"},
        2: {"name": "Laptop", "price": 899.99, "description": "Powerful laptop with 16GB RAM", "image": "static/images/product2.jpg"},
        3: {"name": "Wireless Headphones", "price": 199.99, "description": "Noise-canceling headphones with 20-hour battery", "image": "static/images/product3.jpg"},
    }
    product = products.get(product_id)
    
    if not product:
        return "Product not found", 404
    
    return render_template("product.html", product=product)

@app.route("/cart")
def cart():
    # Example cart items (Later, fetch from session or database)
    cart_items = [
        {"id": 1, "name": "Smartphone", "price": 499.99},
        {"id": 3, "name": "Wireless Headphones", "price": 199.99},
    ]
    return render_template("cart.html", cart_items=cart_items)

@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

@app.route("/order-success")
def order_success():
    return render_template("order_success.html")

if __name__ == "__main__":
    app.run(debug=True)
