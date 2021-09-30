An exercise to learn to use Django


------------------------------------------------------------------
Install tools if required
  sudo apt install nginx                    # if use nginx as the web proxy, otherwise apache2, etc
  sudo apt install libpq-dev postgresql postgresql-contrib libpq-dev    # install postgresql

Setup venv
  python -m venv env_django
  Other installs if required
  source env_django/bin/activate    # or ".  env_django/bin/activate"
    (env_django)$ python -m pip install django
    (env_project) $ pip install gunicorn     # gunicorn -- Python WSGI HTTP Server for UNIX
    (env_project) $ pip install psycopg2     # PostgreSQL database adapter for Python    
  python -m pip freeze > requirements.txt    # keep the version info if create new project
  python -m pip install -r requirements.txt  # install models/version per requirements.txt if using existing project

  source env_django/bin/deactivate    # to deactivate

------------------------------------------------------------------
Setup Django Project
--------------------
- django-admin startproject <project-name>
  create project folder:
  <prj_name>/           # top-level project folder. To avoid the extra level of project_folder, use "django-admin startproject <projectname> ."
  ├── manage.py         # CLI tool, It does the same as the django-admin command-line utility.
  └── <prj_name>        # 
      ├── asgi.py
      ├── __init__.py
      ├── settings.py   # prject setting
      ├── urls.py
      └── wsgi.py
  e.g  
  (env_django) $ django-admin startproject todo_prj


  Config settings
  ALLOWED_HOSTS   (optional, for better security)
    This defines a list of the server’s addresses or domain names may be used to connect to the Django instance. 
    Any incoming requests with a Host header that is not in this list will raise an exception.
      # The simplest case: just add the domain name(s) and IP addresses of your Django server
      # ALLOWED_HOSTS = [ 'example.com', '203.0.113.5']
      # To respond to 'example.com' and any subdomains, start the domain with a dot
      # ALLOWED_HOSTS = ['.example.com', '203.0.113.5']
      ALLOWED_HOSTS = ['your_server_domain_or_IP', 'second_domain_or_IP', . . .]

  DATABASES   (optional, if not using the default sqlite3)
  e.g
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'myproject',
            'USER': 'myprojectuser',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '',
        }
    }


  STATIC_URL and STATIC_ROOT
  tells Django to place static files in a directory called static in the base project directory
  e.g
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

  We can collect all of the static content into the directory location we configured by typing:
  (do that after we created superuser or have other static content)
    python manage.py collectstatic

Start Django App
---------------------
- (env) $ python manage.py startapp <appname>  
  generate the app code (todo_app)
  e.g (env_django) $ cd todo_prj; python manage.py startapp todo_app
  todo_prj
  ├── manage.py
  ├── todo_prj
  │   ├── asgi.py
  │   ├── __init__.py
  │   ├── settings.py
  │   ├── urls.py
  │   └── wsgi.py
  └── todo_app              # <-- generated sub-folder for app
      ├── admin.py
      ├── apps.py           # app setting, (no need change)
      ├── __init__.py
      ├── migrations
      │   └── __init__.py
      ├── models.py         # data struct, db
      ├── tests.py
      └── views.py          # code logic to process the http requests


Code up the Web App
----------------------
The key part includes:
  - Register App
  - Define and App Model and init DB
  - Register the Model to Django Admin site
  - Mapping URL
  - Define View Functions
  - Create Template Files


- Register App
  add <app> to model.INSTALLED_APPS

- Define Model
  Create Class for data in models.py
  e.g
    class ToDo(models.Model)

- Create/Update DB table
  After defining/updating the 'model', use CLI tool (makemigrations/migrate) to create/update the DB table.
  CLI: manage.py [migrate|makemigrations|...] <app_name>   
    makemigrations, which is responsible for creating new migrations based on the changes you have made to your models.
    migrate, which is responsible for applying and unapplying migrations.
    sqlmigrate, which displays the SQL statements for a migration.
    showmigrations, which lists a project’s migrations and their status.
  e.g. 
    python manage.py makemigrations todo_app      # creates <app>/migrations/xxxx_initial.py and db.sqlite3
    python manage.py migrate                      # init/update db

    todo_prj
      ├── db.sqlite3                # <-- create db
      ├── manage.py
      ├── todo_app
      │   ├── admin.py
      │   ├── apps.py
      │   ├── __init__.py
      │   ├── migrations
      │   │   ├── 0001_initial.py   # <-- generated code for DB.table initialization
      │   │   ├── __init__.py
      │   ├── models.py
      │   ├── tests.py
      │   └── views.py
      └── todo_prj
          ├── asgi.py
          ├── __init__.py
          ├── settings.py
          ├── urls.py
          └── wsgi.py

  To View the DB (sqlite), use sqlitebrowser
  sudo apt install sqlitebrowser

- Register the Model to Django Admin site
  in <app>/admin.py, add
  e.g
  from todo_app import ToDo
  admin.site.register(ToDo)

  
- Create User
  use the manage.py tool to create login account for the website
  python manage.py createsuperuser

- Create Views
  add handlers in views.py, 
  in the handler, handle the incoming request and return response,  
                  or call a render function which renders the response form a template
  e.g. 
  def home(request)               # in urls.py, add pattern  path('', views.home, name='home') 
  def todo_detail(request, id)    # in urls.py, add pattern  path('todo/<int:id>', views.todo_detail, name='todo_detail') 
    data = ToDo.objects.get(id)
    return render(request, <template name>, <data in dict e.g.{'data':data}>)
  

- Create Templates


- Mapping urls
  




- Debug the web service
  if setting.py::DEBUG=True, then we can start a development server at http://127.0.0.1:8000/
  python manage.py runserver     



-----------------------------
Setup Firewall for the host (optional)
e.g 
  sudo ufw allow 8000          # if use ufw and use 8000 for HTTP




====================================================================
Deploy the web service on Nginx and gunicorn


GUNICORN (a WSGI proxy)
-------------------------------------------------------------
- Testing Gunicorn’s Ability to Serve the Project
  The last thing we want to do before leaving our virtual environment is test Gunicorn to make sure that it can serve the application. 
  We can do this by entering our project directory and using gunicorn to load the project’s WSGI module:
  e.g.
    cd ~/myproject
    gunicorn --bind 0.0.0.0:8000 myproject.wsgi        # indicating the relative path of myproject/wsgi.py
  
  stop the gunicorn service after testing.
  later we'll set it up in system service

- setup gunicorn service
  Create the gunicorn system service file: /etc/systemd/system/gunicorn.service
  sudo vim /etc/systemd/system/gunicorn.service
  e.g
      [Unit]
      Description=gunicorn daemon
      After=network.target

      [Service]
      User=jerry
      Group=www-data
      WorkingDirectory=/home/jerry/Dev/github/study/PY/web/django/django_psql/
      ExecStart=/home/jerry/Dev/env/env_django/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/jerry/Dev/github/study/PY/web/django/django_psql/django_psql.sock django_psql.wsgi:application

      [Install]
      WantedBy=multi-user.target
  
  Enable the serivce:
    sudo systemctl start gunicorn
    sudo systemctl enable gunicorn
      Created symlink /etc/systemd/system/multi-user.target.wants/gunicorn.service → /etc/systemd/system/gunicorn.service.

  check for the service status:
    sudo systemctl status gunicorn
    ls /home/jerry/Dev/github/study/PY/web/django/django_psql/*.sock
  
  Trouble-shoot:
    sudo journalctl -u gunicorn.service
    sudo systemctl daemon-reload
    sudo systemctl restart gunicorn



Configure Nginx to Proxy HTTP to Gunicorn
-------------------------------------------------------
  The Ngnix config:
  http://nginx.org/en/docs/beginners_guide.html
    /etc/nginx/sites-available/<myproject>
  e.g
    sudo vim /etc/nginx/sites-available/django_psql
      server {
          listen 8080;
          listen [::]:8080;

          server_name localhost;

          location = /favicon.ico { access_log off; log_not_found off; }
          location /static/ {
              root /home/jerry/Dev/github/study/PY/web/django/django_psql;
          }

          location / {
              include proxy_params;
              proxy_pass http://unix:/home/jerry/Dev/github/study/PY/web/django/django_psql/django_psql.sock;
          }
      }

  enable the config:
    sudo ln -s /etc/nginx/sites-available/django_psql /etc/nginx/sites-enabled/django_psql

  test the config
    sudo nginx -t
 
  if test pass, start the nginx service.   (make sure other web server is stopped.)
    sudo systemctl restart nginx
    sudo systemctl status nginx      # check















====================================================================
Deploy the web service on Apache
-----------------------------------------------------------------

Django works with any version of Apache which supports mod_wsgi. 
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/modwsgi/
https://modwsgi.readthedocs.io/en/master/

Brief steps:
  - Prepare server environment, install packages (venv, apache, django, mod_wsgi)
  - Config Static URL in Django project
  - Setup Apache virtualhost
  - Restart Apache service
  - 
  - Authenticating
  - 

- Install packages
  Debian/Ubuntu:
  > django
    python -m pip install django     # This command should install packages into site-packages directory.
  > apache2.    
    sudo apt install apache2
  > python and python-dev, or python3 and python3-dev (required to install some packages with pip)
    sudo apt install python3-dev
  > libapache2-mod-wsgi (Python 2) or libapache2-mod-wsgi-py3 (for Python 3)
    sudo apt install libapache2-mod-wsgi-py3

  the mod-wsgi will be loaded after restart apache2 if it's configured property in apache  (sudo systemctl restart apache2)
    check for the mod:
      apt list | grep 'wsgi'
      sudo find / -name '*mod*wsgi*'       # /usr/lib/apache2/modules/mod_wsgi.so -> /usr/lib/apache2/modules/mod_wsgi.so-3.8
      ldd /usr/lib/apache2/modules/mod_wsgi.so  # check if the dependent python version match cur ver (in venv)


- Config Static URL in Django project
  TO set the address of our static files (css, jss, etc), update STATIC_URL in django::settings.py
  e.g.  in todo_prj/todo_prj/settings.py
    STATIC_URL = '/static_todo_prj/'    # define the url for static files
  
  the files location (/path/to/todo_prj/static) is specified in apache2/virtualhost configuration 

  if there are multiple django project, update django::wsgi.py
  prj/prj/wsgi.py
    #os.environ.setdefault('DJANGO_SETTINGS_MODULE', '<xxx_project>.settings')   # update to
    os.environ['DJANGO_SETTINGS_MODULE'] = '<xxx_project>.settings'




- Adding APIs with RESTful Framework
  > install 'djangorestframework      (sudo pip install djangorestframework)
    https://www.django-rest-framework.org/api-guide/

  > add 'rest_framework' to INSTALLED_APPS in settings.py

  > add <app>/serializers.py 
    import model        (from .models import ToDo) 
    import serializer   (from rest_framework import serializers)
    add serializer class for model   (class ToDoSerializer(serializer.HyperlinkedModelSerializer))

  > Add 'handlers' in views.py  
    multiple options to add handlers:
    1. basic django http handler + template (no rest_framework)
      An example handler:
      from django.http import HttpResponse, Http404
      def handler_name(request):
        data = ModelClass.objects.all()
        return HttpResponse('<p>handler xx view</p>')    # directly response, or 
        # return render(request, 'home.html', {'data':data, })    # respond by render (pass in a template and data)

    2. use standard restful API view from rest_framework
      Create View class based on APIView.
      To render the data view, either use the template (call render()) or use the serializer
      Example:
      from rest_framework.views import APIView
      from rest_framework.response import Response
      class XxxView(APIView):
        def get(self, request):
          try:
            data = Xxx.objects.all().order_by('handle_time')
            # serializer = XxxSerializer(data, many=True)
            context = {'data':data}
          except Xxx.DoesNotExist:
            raise Http404('Record not found')
          # return Response(serializer.data)     # use serializer for the response 
          return render(request, 'xxx_template.html', context)


    3. use rest_framework viewsets
       It will handle GET and POST for Heroes without us having to do any more work.
       add class ToDoViewSet(viewsets.ModelViewSet)  
       we can use a separate urls.py under <app> to route the requests. and add this sub urls.py to the main urls.py: 
         e.g. path('', include('todo_app.urls'))
       but the view is a fixed default style.



- Setup Apache virtualhost
  https://django-project-skeleton.readthedocs.io/en/latest/apache2_vhost.html 
  either add config to default, e.g.
    /etc/apache2/sites-available/000-default.conf        # edit <VirtualHost *:80>
  or add new config, e.g. 
    /etc/apache2/sites-available/<mysite>.conf,  then use 'sudo a2ensite <mysite>' to 'enable it.  
    (??? the 2nd option failed in test.)
  Example config:
    #for django
        LoadModule wsgi_module /usr/lib/apache2/modules/mod_wsgi.so
        Alias /static_todo_prj /path/to/todo_prj/static      # http://localhost/static_todo_prj
        <Directory /path/to/todo_prj/static>
                Require all granted
        </Directory>
        <Directory /path/to/todo_prj/todo_prj>
                <Files wsgi.py>
                        Require all granted
                </Files>
        </Directory>
        WSGIDaemonProcess todo_prj python-path=/path/to/todo_prj      # define wsgi daemon process name
        WSGIProcessGroup django_prjs  
        WSGIScriptAlias /todo_prj /path/to/todo_prj/todo_prj/wsgi.py process-group=django_prjs    # http://localhost/todo_prj

  If the WSGI module is installed using apt install command, you can enable the module without line 2. but using a2enmod command
  a2enmod wsgi
  What a2enmod really do is create a symlink inside /etc/apache2/mods-enabled that points to the module in /etc/apache2/mods-available.


( not required ??
- Config Apache for wsgi
  /etc/apache2/mods-available/http2.conf
  Example:
      WSGIScriptAlias / /path/to/todo_prj/todo_prj/wsgi.py
      WSGIPythonHome /path/to/venv
      WSGIPythonPath /path/to/todo_prj
      <Directory /path/to/todo_prj/todo_prj>
      <Files wsgi.py>
      Require all granted
      </Files>
      </Directory>
)


- Authenticating against Django’s user database from Apache
  Django provides a handler to allow Apache to authenticate users directly against Django’s authentication backends. 
  https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/apache-auth/

  Make sure that mod_auth_basic and mod_authz_user are loaded.
    check loaded apache mod:  apachectl -M
  if not loaded, add LoadModele in VirtualHost config. e.g.
        LoadModule wsgi_module /usr/lib/apache2/modules/mod_wsgi.so
        LoadModule auth_basic_module /usr/lib/apache2/modules/mod_auth_basic.so
        LoadModule authz_user_module /usr/lib/apache2/modules/mod_authz_user.so

  Add check_password into django_prj.wsgi.py
  e.g
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
    from django.contrib.auth.handlers.modwsgi import check_password

- Restart  Apache service
  sudo systemctl restart apache2

  the webservice:   
    http://127.0.0.1/todo_prj
    http://127.0.0.1/static_todo_prj
  


- debug 
  systemctl status apache2
  tail -f /var/log/apache2/error.log
  






================================================================================================
drf: an example using DRF
  DRF -- Django Rest Framework
  The App provide a web UI to get/post (RESTful) currency information 
  of differenct countries from/to the backend SQL DB.

Steps:
- Install DRF 
  pip install django-rest-Framework

- Create Project
  django-admin startproject <prj_name>
  e.g. 
  django-admin startproject country_currency

  The project will be created with some basic components:
  - settings.py
  - urls.py
    The urls dispatcher root entry. The incoming HTTP Req will be matched (regex) and dispacted to 'views' (a function or a class based on TemplateView)
  - wsgi.py (Web Server Gateway Interface)
    WSGI is a standard interface which allows to seperate server code from the application code where you add your business logic
  - asgi.py (Asynchronous Server Gateway Interface)
    ASGI is Asynchronous Server Gateway Interface. In ASGI also you define your application as a callable which is asynchronous by default.
  - manage.py
    Django's CLI utility for administrative tasks 

- Create App
  python manage.py startapp <app name>
  e.g. 
  python manage.py startapp currencies

  basic components:
  - models.py
    Define the data struct. In MTV architecture, Model is the middleware & data handler between database and view.
    in the example, define a new class Country() which contains the fields make up the database table.
  - views.py
    View is the function that takes a Web request and returns a Web response.
    The 'view function' can be decorated with 'rest_framework.decorators.api_view'
  - admin.py
    register the model(s) with django admin.

- Add model(s) in models.py
  Add serializer(s) for the model -- serializer.py
  serialization is the process of converting a Model to JSON. 
  Using a serializer, we can specify what fields should be present in the JSON representation of the model.

- Update the database (makemigration & migrate)
  After making modifications to models, use makemigrations and migrate to propagating changes 
    you make to your models (adding a field, deleting a model, etc.) into your database schema.
  makemigrations: responsible for creating new migrations based on the changes you have made to your models
                  (the data is prepared in subfolder migrations/0001_initial.py)
  migrate:        responsible for applying migrations, as well as unapplying and listing their status
  e.g.
  python manage.py makemigrations
  python manage.py migrate

- Create superuser
  To create the superuser for the app (login the app web)
  python manage.py createsuperuser
  Before creating the superuser, the database need to be initialized (migrate)

- Register app and model(s) 
  For the app and model(s) to be visible, they need to be registered into the project (setting.py) and admin.py
    Modify the setting.py to add the new created app into INSTALLED_APPS, (currencies in this example)
      Also add 'rest_framework' if using drf
    Modify admin.py to register the model(s)
      e.g. admin.site.register(Country)

- Add view(s) into views.py
  To servie GET/POST request, a view (function or class) is needed to return the data in a serialized fashion.
  e.g.
  the api_view function 'country' in this example

- Run the django server
  python manage.py runserver







--------------------------------
Reference:
https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04
