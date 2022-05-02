cd .\python\
pip install -r requirements.txt
cd .\venv\Scripts
Set-ExecutionPolicy Unrestricted -Scope CurrentUser
.\activate.ps1
cd ..\..
set FLASK_APP=app
flask run




ezután client/index.html megnyitása


Készült: 2022.05.
