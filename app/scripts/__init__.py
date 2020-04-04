
def evaluateRisk():
    # To Improve readability i'm going to use a temp builder and a final builder
    json = {
        "age": 35,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 0,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2018}}
    # Temp Builder ->
    # -> Choosing a dict as temp buffer because of better pair selection
    temp = {
        "auto": "",
        "disability": "",
        "home": "",
        "life": ""
    }
    # Final Builder ->
    final_risk = {
        "auto": "",
        "disability": "",
        "home": "",
        "life": ""
    }
    # List Possible Outcomes ->
    outcomes = [
        'economic',            # (<=0)
        'regular', 'regular',  # (1 and 2)doubled to reflect index
        'responsible',         # (>=3)
        'ineligible'           # (exception)
    ]
    # Builder Steps ->
    base_risk = sum(json['risk_questions'])
    # Ineligibility Check
    if json['vehicle'] == 0 or json['vehicle'] == "" or len(json['vehicle']) == 0:
        final_risk['auto'] = outcomes[4]
    if json['income'] == 0 or json['income'] == "":
        final_risk['disability'] = outcomes[4]
    if json['house'] == 0 or json['house'] == "" or len(json['house']) == 0:
        final_risk['home'] = outcomes[4]

    return 'Returned'
