from flask import Flask, jsonify, abort, request

tasks = [{'id':1, 'name':'Comprar flores', 'estado':False},{'id':2, 'name':'Preparar Cena', 'estado':False},{'id':3, 'name':'Comprar boletos del cine', 'estado':False}]

uri = '/api/'

app = Flask(__name__)

@app.route((uri + 'tasks'), methods=['GET'])
def get_tasks():
    return jsonify({'tasks':tasks})

@app.route((uri + 'tasks/<int:id>'), methods=['GET'])
def get_specific_task(id):
    for n in tasks:
        if n['id'] == id:
            return jsonify({'task':n})
    abort(404)
    return None

@app.route((uri + 'append'), methods=['POST'])
def append_task():
    post_id = request.form.get('id')
    post_name = request.form.get('name')
    post_estado = request.form.get('estado')
    tasks.append({'id':int(post_id),'name':post_name,'estado':bool(post_estado)})
    return 'Succesful insertion'

@app.route((uri + 'delete/<int:delete_id>'), methods=['DELETE'])
def delete_task(delete_id):
    for it in range(len(tasks)):
        if tasks[it]['id'] == delete_id:
            del tasks[it]
            break
    print(tasks)
    return 'Deletion completed'

@app.route((uri + 'update'), methods=['PUT'])
def update_task():
    put_id = request.form.get('id')
    put_name = request.form.get('name')
    put_estado = request.form.get('estado')
    for it in tasks:
        if it['id'] == int(put_id):
            it['name'] = put_name
            it['estado'] = bool(put_estado)
    return 'Succesful PUT'

if __name__ == '__main__':
    app.run(debug=True)
