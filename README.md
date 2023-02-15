<h1>Tatted Backend API</h1>

<h2 id="contents">Contents</h2>

-   [Introduction](#introduction)
-   [Database Schema](#database-schema)
-   [User Stories](#user-stories)
-   [Agile Methodology](#agile-methodology)
-   [Technologies Used](#technologies-used)
    -   [Languages](#languages)
    -   [Frameworks, libraries, and Programs](#frameworks-libraries-and-programs)
-   [Testing (Automated and Manual)](TESTING.md)
-   [Bugs](#bugs)
-   [Deployment](#deployment)
    -   [Setting up JSON web tokens](#setting-up-json-web-tokens)
    -   [Preparation for Heroku deployment](#prepare-api-for-deployment-to-heroku)
    -   [Deployment to Heroku](#deployment-to-heroku)
    -   [ElephantSQL Database Creation](#elephantsql)
-   [Credits](#credits)

<h2 id="introduction">Introduction</h2>

This repository is the home of the backend API being used for the 'Tatted' application, made with the power of Django REST Framework (DRF).

The repository for the frontend 'Tatted' application can be found <a href="#">here</a><br /><br />

<h2 id="database-schema">Database Schema</h2>

![Database Schema](docs/screenshots/tatted_api_dbs.png)

The Database Schema contains the following model instances:
- Custom User
- Profile
- Post
- Comment
- Like
- Save
- Review
- Follow

<h2 id="user-stories">User Stories</h2>

The user stories used for the creation of this API were as follows:
- Tatted API 1: As an authenticated API user I can create a post if 'is_artist' = True
- Tatted API 2: As an authenticated API user I can edit a post if 'is_owner' = True
- Tatted API 3: As an authenticated API user I can delete a post if 'is_owner' = True
- Tatted API 4: As an authenticated API user I can comment on a post
- Tatted API 5: As an authenticated API user I can edit a comment if 'is_owner' = True
- Tatted API 6: As an authenticated API user I can delete a comment if 'is_owner' = True
- Tatted API 7: As an authenticated API user I can like/unlike post instances
- Tatted API 8: As an authenticated API user I can save/ unsave post instances
- Tatted API 9: As an authenticated API user I can post a review for a user instance where 'is_artist' = True
- Tatted API 10: As an authenticated API user I can edit a review instance if 'is_owner' = True
- Tatted API 11: As an authenticated API user I can delete a review instance where 'is_owner' = True
- Tatted API 12: As an authenticated API user I can follow/ unfollow other user instances
- Tatted API 13: As an authenticated API user I can edit my profile instance where 'is_owner' = True
- Tatted API 14: As an authenticated API user I can login/logout

<a href="#top">Back to the top</a>

<h2 id="agile-methodology">Agile Methodology</h2>

he Agile Methodology was used thorughout the entire development of this application.  This was implemented by the means of a Github 'Project' which can be referenced here - <a href="https://github.com/users/ryanoneill416/projects/6" target="_blank"> Tatted Backend User Stories</a>

The project was used in a Kanban board style which was divided into the below categories:

-   Todo
-   In Progress
-   Done

![Tatted User Stories Kanban](docs/screenshots/tatted-api-kanban.png)

Github issues were used to create User Stories and if any bugs or obstacles were to be tackled throughout the dev cycle. Issues were labelled in order to indicate importance of features. Each User Story, Fix or Update had a clear title outlining it's exact purpose.

<a href="#top">Back to the top</a>

<h2 id="technologies-used">Technologies Used</h2>

<h3 id="languages">Languages</h3>

Python was solely used for the development of this backend API

<h3 id="frameworks-libraries-and-programs">Frameworks, Libraries and Programs Used</h3>

- Django Cloudinary Storage 
    - Storage of images in the cloud
- Django Filter
    - To filter the data
- PyJWT 
    - Python library which allows you to encode and decode JSON Web Tokens
- Psycopg
    - Psycopg is the most popular PostgreSQL database adapter for Python
- Pillow 
    - Image processing capabilities
- Git
    - For version control, committing and pushing to Github
- Github
    - For storing the repository, files and images pushed from Gitpod
- Gitpod
    - Browser based code editor used to develop the backend API
- Heroku
    - Used to deploy the backend API
- Django Rest Auth
    - Used for user authentication
- ElephantSQL
    - Used to host the PostgreSQL database
- gunicorn
    - As the Python WSGI HTTP Server
- Cors headers
    - To allow access from diferent domains
- Pycodestyle
    - For code validation

<a href="#top">Back to the top</a>

<h2>Testing (Automated and Manual)</h2>

- This backend API application was tested using automated unit testing, manual testing as well as the use of pycodestyle validations
- Please find the testing results [here](/TESTING.md)

<h2 id="deployment">Deployment</h2>

<h3 id="setting-up-json-web-tokens">Setting Up JSON Web Tokens</h3>

1. Install JSON Web Token authentication
```
pip install dj-rest-auth
```
2. In settings.py add the following to the 'INSTALLED_APPS' list
```
'rest_framework.authtoken'
'dj_rest_auth'
```
3. In the main urls.py file add the relevant url path
```
path('dj-rest-auth/', include('dj_rest_auth.urls')),
```
4. Migrate the database using the terminal command
```
python manage.py migrate
```
5. Install all_auth for user authentication
```
pip install 'dj-rest-auth[with_social]'
```
6. In settings.py add the following to the 'INSTALLED_APPS' list
```
'django.contrib.sites',
'allauth',
'allauth.account',
'allauth.socialaccount',
'dj_rest_auth.registration',
```
7. Add the following declaration in settings.py
```
SITE_ID = 1
```
8. In the main urls.py file add the registration url path
```
 path(
        'dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')
    ),
```
9. Install the JSON tokens with the *simple jwt* library
``` 
pip install djangorestframework-simplejwt
```
10. In env.py set DEV to 1 to check whether the environment is development or production
```
os.environ['DEV'] = '1'
```
11. In settings.py add the following if else statement
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
```
12. Add the following declarations in settings.py
```
REST_USE_JWT = True # enables token authentication
JWT_AUTH_SECURE = True # tokens sent over HTTPS only
JWT_AUTH_COOKIE = 'my-app-auth' #access token
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token' #refresh token
```
13. Create a serializers.py file in the main app 'tatted_api'
14. Utilize the code from the Django documentation UserDetailsSerializer as follows:
```
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """Serializer for Current User"""
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        """Meta class to to specify fields"""
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )
```
15. In settings.py overwrite the default User Detail serializer
```
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'drf_api.serializers.CurrentUserSerializer'
}
```
16. Run the migrations for database again
```
python manage.py migrate
```
17. Update the requirements file with the following terminal command
```
pip freeze > requirements.txt
```
18. Make sure to save all files, add and commit followed by pushing to Github.

<a href="#top">Back to the top</a>

<h3 id="prepare-api-for-deployment-to-heroku">Preparation For Heroku Deployment</h3>

1. Create a views.py file inside main app 'tatted_api' and write a welcome message upon startup
```
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to the 'Tatted' backend API!"
    })
```
2. Add the newly created path to to the urlpatterns object
```
from .views import root_route

urlpatterns = [
    path('', root_route),
```
3. In settings.py declare page pagination preferences under the REST_FRAMEWORK variable
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
    'DEFAULT_PAGINATION_CLASS':
    'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
```
4. Set the default render preference to JSON for the production environment
```
if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]
```

<a href="#top">Back to the top</a>

<h3 id="deployment-to-heroku">Deployment to Heroku</h3>

1. On the Heroku dashboard select the 'Create New App' option.
```
pip install dj_database_url_psycopg2
```
2. In settings.py import the database
```
import dj_database_url
```
3. In settings.py declare what database is used for production and development environment configurations
```
DATABASES = {
    'default': ({
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    } if 'DEV' in os.environ else dj_database_url.parse(
        os.environ.get('DATABASE_URL')
    ))
}
```
4. Install Gunicorn library
```
pip install gunicorn
```
5. Create a Procfile in the root directory with the following values
```
release: python manage.py makemigrations && python manage.py migrate
web: gunicorn tatted_api.wsgi
```
6. In settings.py declare the allowed hosts of the application
```
ALLOWED_HOSTS = [
    os.environ.get('ALLOWED_HOST'),
    'localhost',
]
```
7. Install the CORS header library
``` 
pip install django-cors-headers
```
8. Add this to the list of installed apps in settings.py
```
'corsheaders'
```
9. At the corsheaders middleware in settings.py
```
'corsheaders.middleware.CorsMiddleware',
```
10. You can now the allowed origins for network requests made to the server
```
if 'CLIENT_ORIGIN' in os.environ:
     CORS_ALLOWED_ORIGINS = [
         os.environ.get('CLIENT_ORIGIN'),
         os.environ.get('CLIENT_ORIGIN_DEV')
    ]

else:
    CORS_ALLOWED_ORIGIN_REGEXES = [
         r"^https://.*\.gitpod\.io$",
    ]
CORS_ALLOW_CREDENTIALS = True
```
11. Set the jwt auth samesite variable to none
```
JWT_AUTH_SAMESITE = 'None'
```
12. In env.py set your secret key to a random key
``` 
os.environ['SECRET_KEY'] = '****************************************************'
```
13. Reference your newly declared variable in settings.py
```
SECRET_KEY = os.environ.get('SECRET_KEY')
```
14. Set the Debug variable depending on the environment
```
DEBUG = 'DEV' in os.environ
```
15. Copy the CLOUDINARY_URL and SECRET_KEY values from the env.py file and add them to heroku config vars
16. Also in heroku config vars add in 
```
DISABLE_COLLECTSTATIC  set the value to 1
```
17. Ensure the requirements.txt file is up to date before deployment
```
pip freeze > requirements.txt
```
18. Add and commit all changes made and push to your Github repository.
19. In Heroku on the deploy tab go to 'Deployment method' click Github
20. Connect to the appropriate repository
21. Enable automatic deployment for every 'push' made to GitHub

<a href="#top">Back to the top</a>

<h3 id="elephantsql">ElephantSQL Database Creation</h3>

-   Login/Create an account with <a href="https://customer.elephantsql.com/login">ElephantSQL</a>

-   Click the 'Create New Instance' option.

-   Assign your instance a name, select your plan and relevant region.

-   After this you can select 'Review' and then 'Create Instance' if happy with all details.

-   Navigate to the newly created instance and retrieve database URL which will be needed to be included in Heroku's 'Config Vars'.

-   Now the database is successfully created and linked to your project.

<a href="#top">Back to the top</a>

<h2 id="credits">Credits</h2>

The Code Institute introduction to DRF Framework was referenced during the development cycle of this API.

I learned how to create a custom user model based on the official django documentation.