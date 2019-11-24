from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

stores = [
    {
        "name":"My Store",
        "items":[
            {
                "name":"My Item",
                "Price":100
            }
        ]
    }

]


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/store', methods = ['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name":request_data['name'],
        "items":[]
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify(store)

    return jsonify({"message":"Sorry the store is not found"})

@app.route('/store')
def get_stores():
    return(jsonify({'stores':stores}))

@app.route('/store/<string:name>/item', methods = ['POST'])
def create_item_in_store(name):
    get_item_data= request.get_json()
    for store in stores:
        if store['name']==name:
            new_item = {
                "name":get_item_data["name"],
                "price":get_item_data["price"]
            }
            store['items'].append(new_item)
            return(jsonify(new_item))

    return(jsonify({"message":"Sorry the store is not found"}))

@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify(store['items'])
    return(jsonify({"Message":"Sorry the store is not found"}))



app.run(port=5000)
