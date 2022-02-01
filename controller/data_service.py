from flask import jsonify
from flask import request
from route.route import primedata
from model.prime_data import Primedata

@primedata.route('/data/<testid>',methods=['GET'])
def prime_data(testid):
    try:
       objects=Primedata.query.get(testid)
       primedata=dict()
       primedata.update(id=primedata.id)
       primedata.update(data=primedata.data)
       return jsonify(primedata)
    except Exception as e:
       return jsonify({"response":"Bad Request"})


@primedata.route('/data/<testid>',methods=['POST'])
def prime_data(testid):
    try:
       objects=Primedata.query.get(testid)
       primedata=dict()
       primedata.update(id=primedata.id)
       primedata.update(data=primedata.data)
       return jsonify(primedata)
    except Exception as e:
       return jsonify({"response":"Bad Request"})


    
    
    