# Requirements 
1. Wajib Python 3 
2. Wajib VENV 


Guidance for MacOS / Intel 
1. source '/home/rani/Documents/code/project-zusammen/flask-template-venv/venv_flask/bin/activate'
2. pip install flask 
3. pip install flask-restful
4. pip install Flask-SQLAlchemy
5. pip install Flask-Migrate
6. pip install requests
7. pip install python-dotenv
8. pip install flask-cors
9. pip install flask-sieve
10. pip install pymysql

Source : 
1. Venv -> https://docs.python.org/3/library/venv.html
2. Flask Web Site -> https://flask.palletsprojects.com/en/3.0.x/
3. Flask Restful -> https://flask-restful.readthedocs.io/en/latest/
4. Flask SQLAlchemy -> https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/
5. Flask Migrate -> https://flask-migrate.readthedocs.io/en/latest/index.html
6. Python Requests -> https://docs.python-requests.org/en/latest/index.html
7. Python DotEnv -> https://pypi.org/project/python-dotenv/
8. Flask Cors -> https://flask-cors.corydolphin.com/en/latest/index.html
9. Flask Sieve -> https://github.com/codingedward/flask-sieve
10. PyMysql ->  https://pypi.org/project/pymysql/


cara install -> 
1. python -m venv venv 
2. pip install -r requirement.txt 
3. activate the venv. 
4. python run.py 
5. use postmane with this type of curl -> 
curl --location 'https://3590-108-137-176-194.ngrok-free.app/rcs/compare-data' \
--form 'source=@"/Users/shamirhusein/Downloads/regframetemplate-v1_a4b2bb10-395a-11ed-a60a-09e37ac58e58-2024-03-31 (4).xlsx"' \
--form 'compare=@"/Users/shamirhusein/Downloads/9. 240212_[CU P2] Administrasi Kependudukan_DGA_RevAA (1).xlsx"'