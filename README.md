# Falcon-REST-API-Pattern
Massively scalable RESTFul API design with Falcon and PyPy

Please be sure that your virtual environment is faconenv PyPy interpreter. Then run 

`$ pip install -r requirements.txt`

Then serve app using gunicorn

`$ gunicorn app:api`

Now visit http://localhost:8000/notes/

to fetch notes using GET request.
