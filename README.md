# Insurance Assistant
![Insurance Assistant Logo](/assets/img/Insurance-Assistant-Logo.png)

>This project encapsulates a microservice that calculates the risk of the customer based on information given from a POST request coming from a Form.</br></br>
You may use it as a boilerplate for a microservice that handles api requests and returns the result with a DB registry holding the operation. </br>
This code can be used as it's open source
---
**Technologies used:** 

* Python
* Flask
* Python-dotenv
* Flask-pymongo
* Dnspython
* MongoDB Atlas
* Pipenv

---
**Configuration:**

After cloning the repository, install the dependencies:

```
pip install
```
or
```
pipenv install
```

Then proceed with the creation of your .Env file to store your environment variables, for Flask and MongoDB Atlas:

```c#
# .env File:

MONGO_URI_BASE=mongodb+srv://
# Keep the : after the user-name for concatenation
MONGO_USER=<your_username>:
MONGO_PASS=<your_pass>
MONGO_CLUSTER=@<your Cluster Name>.mongodb.net/
MONGO_DBNAME=<your desired database name>
MONGO_DBOPTIONS=?retryWrites=true&w=majority

```
```c#
# .flaskenv File:

FLASK_APP=app
FLASK_RUN_PORT=<your_desired_port>
FLASK_ENV=development

```
---
**Usage:**

If you want to test using the structure designed for this solution here's the Json Source-Code:

This input:

```json
{
  "age": 35,
  "dependents": 2,
  "house": {"ownership_status": "owned"},
  "income": 0,
  "marital_status": "married",
  "risk_questions": [0, 1, 0],
  "vehicle": {"year": 2018}
}
```
Should output:
```json
{
  "auto": "regular",
  "disability": "ineligible",
  "home": "economic",
  "life": "regular"
}
```

Run the server by using: 

```
flask run
```
or
```
python \run.py
```

---
**Screens:**

I've added to the user model at the Database the new entity risk, which will hold all the information of the algorithm passage

![Insomnia PrintScreen](assets/img/MongoDB&#32;Atlas&#32;PrintScreen.png)

Here's the Insomnia settings used for this test, the entry-point for the route tested is:

```
baseurl/api/user/application
```

![Insomnia PrintScreen](assets/img/Insomnia&#32;PrintScreen.png)

**Important:** This should be used with an operator linking to the user model, so it should be a variable endpoint at a more refined solution. Expand with that in mind.