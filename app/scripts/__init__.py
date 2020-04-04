import datetime
# Get Current Year
year = datetime.datetime.today().year


def evaluateRisk(json):
    # To Improve readability i'm going to use a temp builder and a final builder
    # Temp Builder ->
    # -> Choosing a dict as temp buffer because of better pair selection
    temp = {
        "auto": 0,
        "disability": 0,
        "home": 0,
        "life": 0
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
    # Add Base_Risk to all factors
    for key, value in temp.items():
        temp[key] = value + base_risk
    # +-> Age Check ->
    if json['age'] > 60:
        final_risk['disability'] = outcomes[4]
        final_risk['life'] = outcomes[4]
    elif json['age'] < 30:
        for key, value in temp.items():
            temp[key] = value - 2
    elif json['age'] in range(30, 41):
        for key, value in temp.items():
            temp[key] = value - 1
    # +-> Income Check ->
    if json['income'] == 0 or json['income'] == "":
        final_risk['disability'] = outcomes[4]
    elif json['income'] > 200000:
        for key, value in temp.items():
            temp[key] = value - 1
    # +-> House Check ->
    if json['house'] == 0 or json['house'] == "" or len(json['house']) == 0:
        final_risk['home'] = outcomes[4]
    elif next(iter(json['house'].values())) == "mortgaged":
        temp['disability'] += 1
        temp['home'] += 1
    # +-> Dependants Check ->
    if json['dependents'] > 0:
        temp['disability'] += 1
        temp['life'] += 1
    # +-> Dependants Check ->
    if json['marital_status'] == "married":
        temp['disability'] -= 1
        temp['life'] += 1
    # +-> Vehicle Check ->
    if json['vehicle'] == 0 or json['vehicle'] == "" or len(json['vehicle']) == 0:
        final_risk['auto'] = outcomes[4]
    elif int(next(iter(json['vehicle'].values()))) in range(year, year-6, -1):
        # I Imagined that this would subtract from the auto score, but the instructions mentioned add 1 risk point
        temp['auto'] += 1
    # Construct Output ->
    print(temp)
    # Translate temp values to outcomes
    for key, value in temp.items():
        if value <= 0:
            temp[key] = outcomes[0]
        elif value in range(1, 3):
            temp[key] = outcomes[1]
        elif value >= 3:
            temp[key] = outcomes[3]
    # Map through the final_risk and report back ->
    for key, value in final_risk.items():
        if value == '':
            final_risk[key] = temp[key]
    return final_risk
