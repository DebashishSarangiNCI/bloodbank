BloodBankManagement

GITHUB URL:- https://github.com/DebashishSarangiNCI/bloodbank 

Deployment URL:- http://bloodbank01-env.eba-ndphtndy.eu-west-1.elasticbeanstalk.com/

Credentials :- Username - admin ,Password - admin

DEPENDENCIES (Mentioned in requirements.txt)

asgiref==3.6.0
Django==3.2.18
pytz==2023.3
sqlparse==0.4.4
typing_extensions==4.5.0

Configuration of django.config required for .ebextensions---->For AWS EB Deployment

option_settings: aws:elasticbeanstalk:container:python: WSGIPath: Blood_Bank.wsgi:application



