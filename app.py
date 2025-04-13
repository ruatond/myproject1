from flask import Flask, request, jsonify

app = Flask(__name__)

class Item:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self):
        return {"id": self.id, "name": self.name}

items = [
    Item(id=1, name='k1'),
    Item(id=2, name='k2'),
    Item(id=3, name='k3'),
    Item(id=4, name='k4'),
    Item(id=5, name='k5')
]

@app.route("/items", methods=["GET"])
def list_all_items():
    return jsonify([item.to_dict() for item in items]), 200

@app.route("/items/<string:name>", methods=["POST"])
def create_new_item(name):
    new_id = max(item.id for item in items) + 1 if items else 1
    new_item = Item(id=new_id, name=name)
    items.append(new_item)
    return jsonify(new_item.to_dict()), 201

@app.route("/items/<int:id>", methods=["GET"])
def retrive_one_item(id):
    for item in items:
        if item.id == id:
            return jsonify(item.to_dict()), 200
    return "", 404

@app.route("/items/<int:id>/<string:name>", methods=["PUT"])
def update_item(id, name):
    for item in items:
        if item.id == id:
            item.name = name
            return jsonify(item.to_dict()), 200
    return "", 404

@app.route("/items/<int:id>", methods=["DELETE"])
def remove_item(id):
    global items
    for item in items:
        if item.id == id:
            deleted_id = item.id
            deleted_name = item.name
            items = [i for i in items if i.id != id]
            return f"id: {deleted_id}, name: {deleted_name}", 200
    return "", 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
