# Django UI
This document will help to install Django and will use mainly for frontend - UI app development.

## Install & Config

1.Create project dir Or create new project in pycharm using name ui_django

    `mkdir UI_Django; cd UI_Django`
    Or create project in Pycharm and run following commands from terminal.

2.Install latest pip version 

    `python -m pip install --upgrade pip`

3.Install Django - Create requirement.txt and add django version e.g.

    `vi requirement.txt and add Django==3.0.4 and then install django e.g.`
    pip install -r requirements.txt
    
4.From terminal check django version

    `python -m django --version`       
    
5.Start a new Django project

    `django-admin startproject ui_service`
  
6.Configure settings.py


    `Open mysite/settings.py file and add changes e.g. Allow host * etc e.g.
        ALLOWED_HOSTS = ['*']
        TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [os.path.join(BASE_DIR, 'template')],
        ....
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
        LANGUAGE_CODE = 'en-us'
        TIME_ZONE = 'Asia/Calcutta'
        MEDIA_ROOT = os.path.join(BASE_DIR, "media")
        MEDIA_URL = "/media/"
        STATIC_ROOT = os.path.join(BASE_DIR, "static")
        STATIC_URL = '/static/'
    `   


    Updated DIRS from,
         'DIRS': [],
    To,
         'DIRS': [os.path.join(BASE_DIR, 'template')],
        
    Also add,
         STATICFILES_DIRS, e.g.
         STATICFILES_DIRS = (
            os.path.join(BASE_DIR, 'static'),
         )
         MEDIA_ROOT = os.path.join(BASE_DIR, "media")
         MEDIA_URL = "/media/"
         STATIC_URL = '/static/'
    `
     
7.Create a separate application inside our project. Here project is "ui_service" and 
  application name within project is ui. you can create different application within 
  django project such as, home, inventory, eims etc.

    `python manage.py startapp frontend`
    
     `frontend is used to connect all backend services and show data in frontend and also 
      used static pages. It will work as front-end webapp.`
        
8.Update setting.py and add app name


        `
        INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'frontend',
        ]
        `
    
    `Update app name in setting.py. Here app name is frontend.`
    
9.Create static folder under ui

    `
      Create folder "static", "media", "templates" under app folder e.g. under ui. 
    `
    
    `Note`
    
    `Create 'static' folder otherwise it will show error  while running 
      "python manage.py migrate" command`
      
10.To run defautlt lib, e.g. auth (require for superuser,  auth_user, etc. 
   Need to integrate default settings   
   
   `python manage.py migrate`
   
   `Run "python manage.py migrate" to integrate default settings.`
   
11.Start web server

    `python manage.py runserver 0.0.0.0:8081`
    
    
12.Verify web server running in browser, you will see default page. See given 
  example given in comment section.   
  
  
  `http://127.0.0.1:8081/`
  
  `You will see Django UI running on above port. E.g. **Image`
  
13.Update urls (project urls, application specific urls).
  Note: Use "include" statement In django project specific url
   to register different application urls.   
    
    - Project urls E.g. (In this example, Django project name is ui_service)
      and Register application specific urls.
      **open ui_service/urls.py**

        
            # Project specific urls. File name is project name/urls.py e.g. ui_service/urls.py
            `
            open ui_service/urls.py 
            urlpatterns = [
                path('admin/', admin.site.urls),
            ]
            `
             
                 
            # Register applicaiton using "include" statment. 
            e.g.
            Here, '' will use as start of web page. Whenever web site hit, 
            default home page will point to frontend.urls and from there it will point to 
            first page, or you can say landing page of project or home page.
            E.g.
            updated in ui_service/urls (Ui_service is project name).
            Note - add include module after path.
            
            from django.contrib import admin
            from django.urls import path, include
            urlpatterns = [
                path('admin/', admin.site.urls),
                path('', include('frontend.urls'))
            ]
            
            # start with specific application. e.g. application name is account and then 
              paths are login, logout etc. then 
             url will start as http://localhost/account/login, then add url using include as,
               urlpatterns = [
                path('admin/', admin.site.urls),
                path('', include('frontend.urls')),
                path('account/login/', include('frontend.urls')),
            ]
            
            # If your views are function base then add urls as,
            Function views - path('', views.home, name='home')
            
            # If your views are class base then add urls as,
            Classs views - path('', Home.as_view(), name='home')
    
   - Add application specific urls. E.g. here application name is ui.
     Create applicationName/urls.py e.g. 
     **create file frontend/urls.py**
     
     
        E.g.    
        create ui/urls.py and update application specific urls 
        e.g. create file ui/urls.py and add following lines.
        from django.urls import path
        from . import views
        urlpatterns = [
            path('', views.homepage, name='home'),
        ]
        
        Note - 
        # For Function base views you can add url such as,
        path('', views.home, name='home')
        
        # For Classs base views you can add url such as,
        path('', Home.as_view(), name='home')
        
        # You can start url with specific name such as,
        e.g.
        path('login/', views.login, name=login)
        path('logout/', views.logout, name=logout)

**Note - For each application you can add common urls such as,**

    # Actual application functionality
    path('inventory/', views.app1_inventory, name='inventory')
    
    # urls or common or mostly used components within application.
    # Following urls add based on application requirement.
    path('accounts/login/', views.login, name='login')
    path('accounts/logout/', views.logout, name='logout')
    path('home/', views.home, name='home')
    path('', views.home, name='home') # Default landing page
    path('docs/', views.docs, name='docs')
    path('support/', views.support, name='support')
    path('dashboard/', views.dashboard, name='dashboard')
    path('reports/', views.reports, name='reports')
**Under template you can create folder for each component and add related html, css files**

14.Create views. E.g. Create view for home page in "views.py". 
  
  
    # Open views.py and following code   
    ` 
    from django.shortcuts import render, redirect, get_object_or_404
    from django.utils import timezone
    # Create your views here.
    # used function base views
    
    def homepage(request):
      return render(request, 'frontend/home.html')
    `
    
    # Note -
    # This app is used only for Django UI so we have not included other lib such as models.
    # We will use Django form whenever require to render form in UI.
    # also not used auth related function. e.g.from django.contrib.auth.decorators import login_required
    
    # Used only UI related code and not other such auth. E.g.
    
    from django.shortcuts import render, redirect, get_object_or_404
    from django.utils import timezone
    # Create your views here.
    # used function base views
    def homepage(request):
        return render(request, 'frontend/home.html')
    
    Note: In view.py we have have to pass 1 arg. i.e. request. 
    It's mandatory argument as request come from browser or any REST. 
    Also we have to return HttpResponse object. If you not return HttpResponse then
    it will show error such as value error.
    
    Please see following examples/screen shots fore different types of errors 
    if not used request argument or not return response.
    
    # Error example -  TypeError (if we not pass the request object)
    #Code in view.py as,
    from django.shortcuts import render, redirect, get_object_or_404
    from django.utils import timezone
    def homepage():
        pass
    
    - Error will show as, TypeError at /
      Screen shot - TypeError.jpej
      
    
    # Error example - ValueError (if we not return HttpResponse object)
    #Code in view.py
    from django.shortcuts import render, redirect, get_object_or_404
    from django.utils import timezone    
    def homepage(request):
    pass
    
    - Error will show as ValueError at /
    
    
    # Error example - TemplateDoesNotExist at /
    #Code in views.py
    from django.shortcuts import render, redirect, get_object_or_404
    from django.utils import timezone    
    def homepage(request):
    return render(request, 'home.html')
    
    - Error will show as TemplateDoesNotExit
    
    #Note- Need to create template home.html, otherwise it will show error "TemplateDoesNotExit".
    
    
15.Create Template 


    Create folder "templates",  under ui_service app folder. 
    Under template, create separate folder for each application/component and keeep related 
    html files with respecitive folder. For e.g. "templates\ui_service", "templates\frontend",
    "templates\Inventory", "templates\home" etc.
    Here considering each separate folder for each service.
    
    # Create home.html file (to return response of home views given in previous step.)
    # create simple home.html e.g.
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
    <h1>This is first static page.</h1>
    </body>
    </html>    
    
    # Please see sample screen shot.
    
16.Verify web server running in browser, you will see home page. 
    
    
    E.g. see screen shot.
    
## Create Project base Template

<p>
The first step in creating templates for the project is to create the base template. 
Think of the base template as the frame for all pages in the application. It sets the 
top navigation bar, the site footer, and provides a body canvas for any page to customize. 
By using the base template we can ensure a standard look and feel without having to 
duplicate HTML code.
</P>

1.Create base template for project ui_service. E.g.

    `
    <!DOCTYPE html>
    {% load static %}
    <html lang="en">
    <head>
        <title>{% block title %}Base Project Template{% endblock title %}</title>
        <!-- Including web site meta information which is needed for SEO.-->
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta http-equiv="Content-Language" value="en-US" />
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="icon" type="image/png" href="{{ STATIC_URL }}images/favicon.ico">

        <!-- Including Bootstrap information.-->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">

        <!-- Including component specific css files.-->
        <link rel="stylesheet" href="{% static 'css/header.css' %}">
        <link rel="stylesheet" href="{% static 'css/footer.css' %}">

        <!-- Including js script paths.-->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>

        {% block head %}
        {% endblock head %}
    </head>

    <header>
        <!-- Including header html which will be used across the Project.-->
        {% block header %}
            {% include 'header.html' %}
        {% endblock header %}
    </header>

        <body>
            {% block body %}
                 <div class="content">
                     <div class="row">
                         <div class="col-md-8">
                             {% block home %}
                             {% endblock home %}
                         </div>
                     </div>
                 </div>
    
                 <div class="content">
                     <div class="row">
                         <div class="col-md-8">
                             {% block content %}
                             {% endblock content %}
                         </div>
                     </div>
                 </div>
            {% endblock body %}
        </body>

        <footer>
            <!-- Including footer html which will be used across the Project.-->
            {% block footer %}
                {% include 'footer.html' %}
            {% endblock footer %}
        </footer>
    </html>    
    `
2.Create css folder under static

    Creare "static" folder under ui
    E.g.
    Screen shot

3.Update home.html which extends base.html (project template).

    # Update home.html  tempate e.g. Example specific to homepage home.html .
    {% extends "base.html" %}
    {% load static %}
    {% block title %}Home{% endblock title %}
    
    {% block head %}
        <link rel="stylesheet" href="{% static 'css/home.css' %}">
        <link rel="stylesheet" href="{% static 'css/common.css' %}">
    {% endblock head %}
    
    
    {% block home%}
        <div class="home">
            <h1>Home Page!! </h1>
        </div>
    
    {% endblock home %}    
    
4.Create common.css and keep in static\css folder. 
  This will be used common style require across the project.
  
    #Note - Common.css used across the project. E.g.
    body {
    font-family: 'Poppins', sans-serif;
    color: #555555;
    }
    h1 {
        color: green;
        font-size: 30px;
        background: silver;
        padding: 20px;
        text-align: center;
    }
    h2,
    h3,
    h4,
    h5,
    h6 {
      color: #000000;
    }
    
    a {
      color: #000000;
      transition: all .5s ease;
    }
    
    
5.Create home.css file and add in static\css folder e.g.


    # Note - This is component specific css. E.g. home.css file used for home.html   
    .home{
     padding-top: 60px;
     margin-top: 60px;
     background: white;
}
  

## Create HTML, CSS and folder as per Backend Services
This section show some basic of adding html, css files for backend specific services. 
E.g. we will add account(login, logout) specific code.

Create separate folder for each service and 
within service specific folder create separate file for each component.
  