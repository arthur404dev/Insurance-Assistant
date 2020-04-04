from flask import request, jsonify


def post_application(db):
    try:
        _json = request.json
        print(_json)
        _age = _json['age']
        _dependents = _json['dependents']
        _house = _json['house']
        _income = _json['income']
        _marital_status = _json['marital_status']
        _risk_questions = _json['risk_questions']
        _vehicle = _json['vehicle']
        # Check for fields and method
        if request.method == 'POST':
            # Insert data to database
            application = db.users.insert({
                "application": {
                    "age": _age,
                    "dependents": _dependents,
                    "house": _house,
                    "income": _income,
                    "marital_status": _marital_status,
                    "risk_questions": _risk_questions,
                    "vehicle": _vehicle
                }
            })
            # Response ->
            response = jsonify(
                f'Application {application} was successfully stored!')
            response.status_code = 200
            return response
        else:
            print('reached else')
            raise Exception('Bad Request')
    except Exception as e:
        response = jsonify(
            'Bad Request, All Fields are required')
        response.status_code = 400
        print(e)
        return response
