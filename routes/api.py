from flask import Flask, Blueprint,jsonify,request, redirect
from modules.mysqloperations import Model

api = Blueprint('api', __name__, url_prefix='/api')
db = Model()

db_config = {
    'user': 'root',
    'password':'',
    'host': 'localhost',
    'database': 'todolist',

}
@api.route("addtask", methods=['POST'])
def addingTask():
    tasks = request.form.get('atask')
    result = db.addingTask(tasks)
    if result['status'] == 'Success':
        return redirect('/message')
    else:
        return "Failed!"

@api.route("displaytask", methods=['GET','POST'])
def displayTask():
    data = db.displayTask()
    if data:
        return jsonify({'status': True, 'msg': "text related to route", 'data':data})
    else:
        return jsonify({'status': False, 'msg': "text related to route", 'data':data})

# @api.route("deletetask", methods=['POST','GET'])
# def deleteTask():
#     deleteData = db.deleteTask(id)
#      if deleted:
#         return jsonify({'status': True, 'msg': 'deleted successfully'})
#     else:
#         return jsonify({'status': False, 'msg': 'Failed'})


