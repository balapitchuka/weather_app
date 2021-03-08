# WeatherApp Documentation


## Environment Setup

Note: Windows10 platform is used for development, use equivalent commands for project setup for linux and macos
##### 1. Check python Installation and virtualenv package installation
```
# python version
> python --version
Python 3.9.0

# django version 
> python -m django --version
3.1.7

# Install virtualenv package for virtualenv creation
> python -m pip install virtualenv

```

##### 2. Setup virtual environment for the project
```
Make sure you are inside the "weather_app" folder on the same level where manage.py file is present.


1. Create new python virtual environment for the project
> python -m virtualenv weatherapp_env

2. Activate the virtual environment
> weatherapp_env\Scripts\activate

```

##### 3. Install dependencies for the project
```
> python -m pip install -r requirements.txt
```

##### 4. Running development django server
```
> python  manage.py runserver
```

##### Notes
- For development, django builtin sqlite database is being used.

- sample credentials for testing:
    ```

    Credentials:

    "username" : "admin",
    "password" : "Avengers123@"
    ```

## Weather API's

Following are the api's available in  weatherapp
```
api/auth/login/
api/auth/register/
api/auth/token/refresh/
api/weather/
api/weather/email/
```


##### API Detailing:
**`api/auth/register/`**

* API is used for new user registration.
* **Http Verb** : post
```
http://127.0.0.1:8000/api/auth/register/

Sample Body:

{
    "username" : "dhoni",
    "password" : "B123@111",
    "password2" : "B123@111",
    "email" : "dhoni@gmail.com",
    "first_name" : "Mahendra",
    "last_name" : "Dhoni"
}
```
<hr>

**api/auth/login/**

* API is used for login of already registered users
* **Http Verb** : post
```
http://127.0.0.1:8000/api/auth/login/

Request Body:

{
    "username" : "admin",
    "password" : "Avengers123@"
}
```

On successfull Authentication with credentials, jwt tokens will be provided in response to the request. There are two tokens access and refresh.

**Note:** 
* By default, access tokens are set to valid for 1 hour
* Change the access token life time validity setting using settings.py file
    - **'ACCESS_TOKEN_LIFETIME'** : timedelta(minutes=60)

<hr>

**`api/auth/token/refresh/`**

* API to obtain a new access token whenever existing access token expires
* **http verb** : post
```
http://127.0.0.1:8000/api/auth/token/refresh/

{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNDU3NTk4OSwianRpIjoiNDJhNzIxMzkyMTA0NGY4MmFmNzgxNjE4NWM4ZTM3NTgiLCJ1c2VyX2lkIjoxfQ.x7Bx-chkdCJYes1G9d8UaZQAA5NWeyBpv4WZz5Z0itg"
}
```

<hr>

**api/weather/**

* API to get weather data as json response
* **Http Verb** : get
* Authentication : Required
    * Header   "Authorization" : "Bearer \<AccessToken\>"

```
Sample Request:

http://127.0.0.1:8000/api/weather/
```

<hr>

**api/weather/email/**
* API to get weather data in excel format for the emmail id list provided in the request
* **Http Verb** : post
* Authentication : Required
    * Header   "Authorization" : "Bearer \<AccessToken\>"

```
Sample Request:

http://127.0.0.1:8000/api/weather/email/

```

<hr>


### Testing APIS Using Postman Tool
```
1. Inside 'weather_app' there is postman folder which consists of following file:
"Weather API.postman_collection.postman_collection.json"

2. Go to postman tool and  import the file  into postman.
This will list all the apis developed as listed above.
```