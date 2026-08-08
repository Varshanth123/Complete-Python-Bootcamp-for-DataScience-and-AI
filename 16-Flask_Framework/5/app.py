### Put and Delete-HTTP verbs
### Working with API's--Json

from flask import Flask,jsonify,render_template,redirect,request

app=Flask(__name__)

## Initial data in my todo list
items=[
    {'id': 1,'name': 'Item 1','description':'This is Item 1'},
    {'id': 2,'name': 'Item 2','description':'This is Item 2'}
]

@app.route('/')
def home():
    return 'Welocme to the sample ToDo list App'

## Get: Retrive all the items
@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items) # jsonify() is a utility function provided by the Flask web framework that serializes Python data structures (like dictionaries or lists) into JSON format and wraps them in a proper HTTP Response object.

## GET: retrive a specific itam by ID
@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item=next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    return jsonify(item)

## POST: create a new Item
@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or 'name' not in request.json:
        return jsonify({"error":"item not found"})
    new_item={
        'id':items[-1]['id']+1 if items else 1,
        'name':request.json['name'], 
        # In Flask, request.json is a property used to parse and access incoming JSON data from an HTTP request body as a native Python dictionary
        'description':request.json.get('description','')
    }
    items.append(new_item)
    return jsonify(new_item)

# PUT: Update an existing item
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item =next((item for item in items if items['id']==item_id),None)
    if item is None:
        return jsonify({"error":"Item not found"})
    item['name']=request.json.get('name',item['name'])
    # In Flask, request.json.get() (or preferably request.get_json().get()) is used to safely retrieve a specific key's value from an incoming JSON request body
    item['description']=request.json.get('description',item['description'])
    return jsonify(item)

# DELETE: Delete an item
@app.route('/items/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    global items
    items=[item for item in items if item['id']!=item_id]
    return jsonify({'result':"Item Deleted Successfully"})

@app.route('/items-page')
def items_page():
    return render_template('items.html')

if __name__ == '__main__':
    app.run(debug=True)

# for Testing these all API's we can use Postman