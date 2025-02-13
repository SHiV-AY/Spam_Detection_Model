# Spam_Detection_Model
python3 -m venv env                        # to create env
source env/bin/activate                    # to open env 
pip install django                         # install django
django-admin startproject project_name     # create django project
cd project_name                            # go to project folder  

python3 manage.py startapp api             # start app

python3 manage.py migrate                  # migrate api and app
python3 manage.py runserver                # start the server
