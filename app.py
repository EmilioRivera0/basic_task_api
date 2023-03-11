"""-----------------------------------------------------------------------------------------------------------------------------------
- Software Name: Task Manager API
- Language: Python
- Developer: Emilio Rivera Macías
- Date: March 10, 2023
- Contact: emilioriveramacias@gmail.com
-----------------------------------------------------------------------------------------------------------------------------------"""

#necessary imports ----->
from flask import Flask, jsonify, abort, request

#object declaration ----->
#data structure used to store the tasks of the api
#initialized with 3 tasks
tasks = [{'id':1, 'name':'Comprar flores', 'estado':False},{'id':2, 'name':'Preparar Cena', 'estado':False},{'id':3, 'name':'Comprar boletos del cine', 'estado':False}]

#URI of the API
URI = '/api/'

#creating the Flask object app
app = Flask(__name__)

#function definition ----->
#get request to view the tasks
@app.route((URI + 'tasks'), methods=['GET'])
def get_tasks():
    """ Returns the tasks data structure as a json """
    return jsonify({'tasks':tasks})

#get request to view specific task
@app.route((URI + 'tasks/<int:id>'), methods=['GET'])
def get_specific_task(id):
    """ Look for the specified task on tasks data structure and return it as json if found """
    #iterate through each task to look for the specified one
    for n in tasks:
        if n['id'] == id:
            #if task is found, return it as a json
            return jsonify({'task':n})
    #if the task does not exists, 404 HTTP error code is returned
    return abort(404)

#post method to append a task to tasks data structure
@app.route((URI + 'append'), methods=['POST'])
def append_task():
    """ append to tasks the specified task through the received HTTP packet """
    #initialize the necessary variables with its respective value from the variables from the HTTP packet
    post_id = request.form.get('id')
    post_name = request.form.get('name')
    post_estado = request.form.get('estado')
    #append the task
    tasks.append({'id':int(post_id),'name':post_name,'estado':bool(post_estado)})
    #return tasks
    return jsonify({'tasks':tasks})

#delete method to remove the specified task
@app.route((URI + 'delete/<int:delete_id>'), methods=['DELETE'])
def delete_task(delete_id):
    """ remove the specified task through the URI from tasks data structure """
    #iterate through tasks looking for the indicated task to be removed
    for it in range(len(tasks)):
        #if found, delete the indicated task and return tasks as json
        if tasks[it]['id'] == delete_id:
            del tasks[it]
            return jsonify({'tasks':tasks})
            break
    #if task is not found, generate 404 HTTP error code
    return abort(404)

#put method to update a specified task
@app.route((URI + 'update'), methods=['PUT'])
def update_task():
    """ update the specified task with the values of the HTTP packet data """
    #initialize the necessary variables with its respective value from the variables from the HTTP packet
    put_id = request.form.get('id')
    put_name = request.form.get('name')
    put_estado = request.form.get('estado')
    #iterate through tasks looking for the indicated task to be updated
    for it in tasks:
        #if found, update the task and return tasks as json
        if it['id'] == int(put_id):
            it['name'] = put_name
            it['estado'] = bool(put_estado)
            return jsonify({'tasks':tasks})
    #if task does not exists, generate 404 HTTP error code
    return abort(404)

#API program start point ----->
#check if current module is running as main
if __name__ == '__main__':
    #run Flask object with debug output on terminal
    app.run(debug=True)
