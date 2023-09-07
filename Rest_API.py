from flask import Flask, request, jsonify

app = Flask(__name__)

stores = []

@app.route('/stores', methods=['POST'])
def create_store():
    data = request.get_json()
    new_store = {
        'name': data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store), 201

@app.route('/stores/<string:name>')
def get_store(name):
    store = next((store for store in stores if store['name'] == name), None)
    if store:
        return jsonify(store)
    return jsonify({'message': 'Store not found'}), 404

@app.route('/stores')
def get_stores():
    return jsonify({'stores': stores})

@app.route('/stores/<string:name>/items', methods=['POST'])
def create_item_in_store(name):
    data = request.get_json()
    store = next((store for store in stores if store['name'] == name), None)
    if store:
        new_item = {
            'name': data['name'],
            'price': data['price']
        }
        store['items'].append(new_item)
        return jsonify(new_item), 201
    return jsonify({'message': 'Store not found'}), 404

@app.route('/stores/<string:name>/items')
def get_items_in_store(name):
    store = next((store for store in stores if store['name'] == name), None)
    if store:
        return jsonify({'items': store['items']})
    return jsonify({'message': 'Store not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
