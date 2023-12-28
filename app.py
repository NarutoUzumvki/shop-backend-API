from flask import Flask, request, jsonify
from operations import *

app = Flask(__name__)

@app.route("/")
def greet():
    return f"Psst, Hey-Twig!"

@app.route("/v1/add_product", methods=["POST"])
def add_product():
    try:
        product = request.json["product"]
        price = request.json["price"]
        quantity = request.json["quantity"]
        add_item([product, price, quantity])
        return f"Product added to shop, Successfully.", 201

    except Exception as error:
        return f"Could not add product because, {error}", 400


@app.route("/v1/retrieve_data/<string:item_no>", methods = ["GET"])
def retrieve_data(item_no):
    try:
        data = get_item_details(item_no)
        if data:
            return jsonify(data), 201
        else:
            return f"Could not find Item", 404

    except Exception as error:
        return f"Could not Retrieve Item Data because, {error}", 400


@app.route("/v1/update_product/<string:item_no>", methods = ["PATCH"])
def update_product(item_no):
    try:
        # product = request.json["product"]
        price = request.json["price"]
        quantity = request.json["quantity"]
        update_item(price, quantity, item_no)
        return f"Product with Item No : {item_no}, has been Updated Successfully.", 201

    except Exception as error:
        return f"Could not Update Product because, {error}", 400


@app.route("/v1/remove_product/<string:item_no>", methods=["DELETE"])
def remove_product(item_no):
    try:
        remove_item(item_no)
        return f"Product with Item No : {item_no}, has been Removed from the Shop Successfully.", 201

    except Exception as error:
        return f"Could not remove Product because, {error}", 400


@app.route("/v1/purchase/<string:item_no>", methods=["PATCH"])
def purchase(item_no):
    try:
        quantity = request.json["quantity"]
        purchase_item(item_no , quantity)
        return f"{quantity} x Product with Item No : {item_no} has been Purchased from the Shop.", 201

    except Exception as error:
        return f"Could not Purchase Product because, {error}", 400


if __name__ == "__main__":
    app.run(debug = True)