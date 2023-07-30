About The Library Management Project developed using Python, Django and MySQL

Aim of the project is to develop software to improve the quality of existing library services and to cater to the ever growing users' information needs effectively, in an efficient, useful and timely manner.

Most libraries contain huge collection of variety of documents and have a large clientèle.  The variety and the volume of collection the libraries have to manage and the number of users they have to serve pose a lot of problems for the library staff in performing various housekeeping jobs effectively and serve their patrons well using manual methods. 

The librarians can’t effectively achieve their goal of providing right information to the right user at the right time in a right manner and to satisfy ever increasing demands of the readers, unless they computerize their library operations. 

Therefore, it is most essential for the libraries to go automated and employ modern computer and communication technologies to perform their library functions effectively. 

An Integrated Library System (ILS) usually comprises a relational database software and two graphical user interfaces (one for patrons, one for staff) to interact with the database. Most ILSes separate software functions into discrete programs called modules, each of them integrated with a unified interface.

The popular commercial software packages available for library management are quite expensive. Their open source counterparts such as Koha, NewGenLib and Evergreen though have comparable features are still difficult for the small and medium libraries to install and use them. Thery are quite difficult to install and are very complex and advanced. The open source support vendors also charge huge amounts for installation and annual maintenance. Hence, many libraries are looking for an inexpensive simple ILS which they themselves can install and use.

Keeping this in mind this project has been taken up.

This library management software (LMS) is developed using Python, Django and MySQL under the Ubuntu 18.04 LTS Linux Operating System. In the development environment one can use sqlite3 as backend RDBMS instead of MySQL. 

Python Django is used to develop this project mainly because using Django it is easy to develop with less effort and maintain powerful, robust web sites having various authentication mechanisms along with CSRF security feature.
 
Though this is a project basically taken up to learn Django, quite a few advanced features are added to the project.

The following most important functional requirements of an ILS are satisfied in this LMS software:
   	-  Cataloguing
        -  Circulation and Patron Management                           
        -  Reporting                           
        -  Administration                       
 	-  Online Public Access Catalogue
 
Server Side Requirements:
   - Operating system: Windows/Unix/Linux or Cloud Platform: Heroku / PythonAnywhere & Git
   - Web Server: Apache 2.4 or NGINX
   - Programming language: Python 3 or Python 2 (Version 3 is preferred), React (JavaScript) 
   - Web application development framework: Django 2.0 or 1.x
   - HTML, CSS (Bootstrap 4)
   - Database Server: 
          For Production Environment:
             MySQL Server 8.x or 5.x or MariaDB and 
             MySQL DB API Drivers: MySQL client/ MySQL Connector
             Or 
             PostgreSQL 9.4 or higher and 
             API Driver psycopg22.5.4 or higher is required. 
  
          For Development Environment:
          SQLite Version 3 
   - LDAP Server (phpmyldap)
   - Postfix Mail Transfer Agent
   - curl, python httpie command line programes may be used to access Django rest api
     Postman, React app added to the software may be used as client to consume project's Django rest api 

Client Side Software & Hardware
       
   - Computer System: Modern PC (Pentium Dual or Quad Core or i3 or i5 or highter)
     with good amount of Processor Speed and RAM or 
     Laptops / Notebooks / Tablets / Smart Phones
   - Browser: Any modern web browsers such as Firefox, Google Chrome, safari 
               Or Internet Explorer 
   - Automation Technology: 
       Barcode Scanners, Barcode Printer or RFID tags, tag readers

Features:

   -  Powerful field level search facility using djangoql (for collection, patrons, gate register entries)
   -  Cataloguing and Circulation Functions
   -  Bulk uploading of patron photographs
   -  CRUD operations on Biblio, Biblio Items, Authors, Publishers, Subjects, Borrowers using django rest framework api
   -  Quotations and suggestions management
   -  Display of one quotation everyday by randomly picking one from the list of 
      available quotations in the OPAC web interface
   -  SQL Reports using django-sql-explorer module 
   -  RSS feeds for new arrivals of items
   -  Gate register to record visitors time in/timeout entries
   -  Powerful Django rest api web interface
   -  Simple React Client App to list Books consuming rest api end point
   -  Custom User Model to authenticate users by email rather than the default username available in Django User model
   -  User self-registration and email verification by sending account activation link to the user 
      mail accounts
   -  Configuring Django with Postfix mail Transfer Agent (configured with google smtp server) to send external emails
   -  Basic, JWT Authentication for accessing and performing CRUD operations consuming various rest api end points generated using Django rest framework 
   -  LDAP Authentication to enable users registered with LDAP server to be added automatically 
      to the database when they first login without the need for signup
   -  Simple payment system to accept fine payments using Paytm
   -  Display of project's Sqlite3 Database Schema generated using Java based SchemaSpy
   -  Admin site interface (Django Administration) 
      The library staff who have access to this interface can perform all house keeping 
      and administration operations such as:
           * Add/Edit/Delete Users
           * Add/modify/Delete user profiles
           * Change permissions 
           * Add groups
           * Add/Change/Delete biblios, authors, publishers, subjects, languages, departments, 
             system preferences, issuing rules, holiday calendar, rental charges, cover images, 
             patron photos, patron designations, card numbers etc.
           * Add/change/delete SQL reports
           * Moderate book suggestions
           * Add/change/Delete library quotes
           * Collect fines, write off fines
           * Issue, renew, return and reserve books to patrons
           
   -  Intranet Staff Client Web Interface
           This is for the library staff to login to and perform housekeeping operations.
           * Create Patron Accounts on behalf of the users
           * Print Patron ID Cards
           * Bulk upload Patron Photos
           * Add and change patron photos
           * Record login and logout time of library visitors
           * Add Books and other collection
            (Add/Edit/Delete Biblio, Author, Publisher, Subjects, Borrower records using Django rest api).
           * Add and list suggested books using django rest api
           * Upload and attach Local Cover Images to Books and other collection
           * Change the local cover image
           * Circulate the books to users (Check-in, Renew and Check-out)
           * List gate register entries
           * Add and list quotations (Everyday a quotation from this is displayed in the OPAC interface).
           * List system preferences
           * Search the catalogue
           * List biblios, patrons and borrowers
           * Export biblios and borrowers to xls, json, tsv, csv and ods formats.
           * See the projects SQLite3 database schema
           * Run various SQL reports
           * Collect fine amounts through Paytm (Testing not fully functional)

   -   Online Public Access Catalogue Web Interface (OPAC)
           This is for the patron use. Using this interface the patron can 
           * Signup
           * Login
           * Reset the password
           * Add their profile
       Library patrons without the need for logging in can:
           * Search the library catalogue
           * List the books
           * List the patrons
           * Get RSS Feed of New Arrivals of Books
           * Record his/her library entry/exit time (Gate register entry)
           * List gate register entries
           * Add Quotations
           * List Quotations
           * Export Patrons and Biblios in to xls and other formats
           * View the projects SQLite3 database schema
       Logged-In Patrons additionally can:
           * Suggest books
           * List his/her suggested books
           * Run various Reports
           * View books issued to them
           * Renew the books borrowed by them          
            
  
How to install and use this Library Management Software?

This project uses Python 3.8 and python virtual environment created using that to install the required python modules. 

To create python virtual environment, follow the source url: https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3

The following are the steps in Ubuntu:
    Assuming that python 3.8 is already installed:
    	sudo update-alternatives --config python3 (if you have more than one version of python3)
    	python3 -V
        python3 -m pip install --upgrade pip
        pip3 install virtualenv

        #change to your home directory
        cd ~
        #create virtual environment 'ILSVENV'
        virtualenv -p python3 ILSVENV
        #activate the virtual environment
        cd ILSVENV
        source ./bin/activate
        #to deactivate
        deactivate
        
Download the source code of this project zip file into Downloads directory 
extract it and move the djangoLMS folder to ~/ILSVENV.

Change directory to ~/ILSVENV/djangoLMS.
cd ~/ILSVENV/djangoLMS

To install the python modules this project requires run:
pip install -r requirements.txt

To start the Django development web server:
cd ~/ILSVENV/djangoLMS

python3 manage.py runserver

[ Note if you make any changes to the models you have to run the commands
  python3 manage.py makemigrations 
  python3 manage.py migrate
  #and then run 
  python3 manage.py runserver
]

To access djangLMS web site navigatge to http://localhost:8000 in the web browser.
 
LDAP authentication: 

Install OpenLDAP with phpldapadmin on ubuntu following instructions given in the source below:
https://medium.com/analytics-vidhya/install-openldap-with-phpldapadmin-on-ubuntu-9e56e57f741e

To know more about LDAP Authentication using django follow the source:
url: https://medium.com/@itsayushbansal/ldap-authentication-with-django-a2b4f00c9a04

Caution: In Ubuntu 18.04 LTS use php 7.2 as this is the version it has in it's source repositories and the php-ldap module required by phpldapadmin is not installable for php 7.3 and later. 

Important:

You will encounter a bug in phpldapadmin when installed with php 7.2.
For the phpldapadmin installed with php 7.2 to function correctly remove the bug as per the instructions given in the below source:

Source url: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=890127

To use phpldapadmin and to create users follow these steps:
 
    To access phpldapadmin:
       http://localhost/phpldapadmin
    
    Login with your admin credentials:
       Example:
       Login DN : cn=admin,dc=iiitslibrary,dc=org
       Password : Admin123

    Create Organisational Unit ou=user
    Under that Organizational Unit (ou=user) create child user accounts.
    Use Kolab: User Entry option and populate these fields: 

    Common Name, Email, First Name, Last Name and Password.

    Please verify the password.

    Example DN:
     cn=narasimha yadagiri,ou=user,dc=iiitslibrary,dc=org

To use LDP in djangoLMS project:

Set the flag LDAP=True in ~/ILSVENV/djangoLMS/model_reports/settings.py
and make sure these settings in settings.py file:

    DJK=False 
    LOGIN_URL = 'login'
    LOGOUT_URL = 'logout'


JWT Authentication:
	The project uses Django rest framework JWT authentication in addition to basic Django rest framework user authentication to enable access to rest api.

To use JWT set JWTAUTH=True in ~/ILSVENV/djangoLMS/model_reports/settings.py
To switch back to regular Django rest framework authentication set JWTAUTH=False.

To access ILS (Integrated Library System) api using JWT Authentication navigate to the address http://localhost:8000/api-token-auth/ in the web browser.

Enter email and password to get the JWT token which should be used in place of basic authentication with username: password.

For example, to get token using python httpie command line interface:


   http post http://127.0.0.1:8000/api-token-auth/ email=charithatsk@gmail.com password=admin123

Note the url should end with /

Output will look like this:

{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNiwidXNlcm5hbWUiO
iJjaGFyaXRoYXRza0BnbWFpbC5jb20iLCJleHAiOjE2OTAzODE0NDUsImVtYWlsIjoiY2hhcml0aGF0c
2tAZ21haWwuY29tIn0.Z0i7wGcoLOuu6je8vb-K6x1Yq9h_YizmDSGbUhWj6Sk"}


Then to get the list of library collection run:

http http://127.0.0.1:8000/api/v1/biblios/  "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNiwidXNlcm5hbWUiOiJjaGFyaXRoYXRza0BnbWFpbC5jb20iLCJleHAiOjE2OTAzODE0NDUsImVtYWlsIjoiY2hhcml0aGF0c2tAZ21haWwuY29tIn0.Z0i7wGcoLOuu6je8vb-K6x1Yq9h_YizmDSGbUhWj6Sk"

After the word Bearer whatever follows is the token.

You may use curl instead of httpie for accessing the rest api.
You may also use postman GUI, or React App for the same

React Client:

A simple ReactJS client app has been written to access rest api for which we need Django basic authentication instead of JWT Authentication. So, we have to set JWTAUTH=False in settings.py to use this client.

This app only lists the books and other collection in the library. The same save program can be easily extended to perform all CRUD operations consuming various end points of the project's rest api.

This application 'App.js' is found in 'src' folder of 'react-client/client' folder placed outside the the  'djangoLMS' folder in the source code of the project.

You have to create react app and replace App.js and App.css with the ones from the project source code.

To create react app 'myclient' run:
cd ~/ILSVENV/react-client
npx create-react-app myclient
npm start

Replace react-client/myclient/src/App.css with react-client/client/src/App.css
Replace react-client/myclient/src/App.js with react-client/client/src/App.js

Then open http://localhost:3000/ in the browser to see the app.

You’ll need to have Node >= 14.0.0 and npm >= 5.6 on your machine for this.

To use react-client frontend with django backend rest api server please ensure that you have this entry in your settings.py file: 

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://localhost:8000',
]
Ensure to uncomment these authentication settings in settings.py

# Authentication settings
   'DEFAULT_AUTHENTICATION_CLASSES': [
           'rest_framework.authentication.BasicAuthentication',
           'rest_framework.authentication.SessionAuthentication',
           #'rest_framework.authentication.TokenAuthentication',
   ],

ScemaSpy:

Move the schemaSpy folder '~/ILSVENV/djangoLMS/schemaSpy' to your Apache Web server's root folder : '/var/www/html'.

cd ~/ILSVENV/djangoLMS/
sudo mv -r ./schemaSpy /var/www/html

To access the project sqlite database schema navigate to the address 'http://localhost/schemaSpy'.

How to create SQLite database schema using SchemaSpy ?

To get sqlite database schema using schemaSpy, download SchemaSpy jar file and sqlite-jdbc-driver jar file into Downloads directory and issue the following commands:

cd ~/ILSVENV/djangoLMS

java -jar ~/Downloads/SchemaSpy_5.0.0.jar -t sqlite -db db.sqlite3 -sso -dp ~/Downloads/SqliteJdbcDriver/sqlite-jdbc-3.40.0.0.jar -o schemaSpy


Sending External Email using free google smtp server


This project makes use of postfix Mail Transfer Agent to forward the external mail to google smtp server for delivery. Django's default User Model has been extended to create a Custom User Model enabling users to login with email and password rather than username and password. When a user Signup an activation email link will be sent to the person's email account. The library user account will be activated only after the user verifies the email by navigating to that link in the browser. LDAP user accounts are automatically created and activated the first time they login.

You have an entry like the below in settings.py:


#EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
#EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#For sending emails out using Postfix Mail Transfer Agent
EMAIL_USE_TLS = True
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25 
DEFAULT_FROM_EMAIL = 'charithatsk@gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = '' 

To enable sending external mails uncomment:

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

and comment out

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

in settings.py file.

The setting console.EmailBackend sends the User account activation link to the console instead of mail account.

To install the postfix server, follow the source:
https://easyengine.io/tutorials/linux/ubuntu-postfix-gmail-smtp/

To Configure Postfix to use Gmail App Passwords follow the source:
https://kifarunix.com/configure-postfix-to-use-gmail-app-passwords/










  

	

    


    
    
    
    
       

