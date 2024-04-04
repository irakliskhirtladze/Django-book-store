# Django custom user model

## Description
This Django project for TBC Academy includes very basic functionality such as Start page,
user registration and login, user's home page and logout.

I have created custom model for user to replace username with email for user identification.

Plus first and last name fields ar removed.

These were done using BaseUserManager class in 'managers.py'.
See 'users/models.py' and 'users/admin.py' for related changes too.

Code from 'forms.py' was used to create user signup form.


- 'unchained' is the project folder.
- 'users' is the first and only app for now.
- For respective pages I have used simple HTML templates located in 'templates' folder.


## Requirements
- Python 3.12

To install other requirements run in terminal:
````
pip install -r requirements.txt
````

