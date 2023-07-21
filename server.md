
## set up remote server
```python
apt-get update && apt-get upgrade
hostnamectl set-hostname python_server
hostname
nano /etc/hosts
139.144.235.212
ctl x
adduser steve
password
adduser steve sudo
exit 
ssh steve@139.144.235.212
ssh root@139.144.235.212
# on server 
mkdir -p ~/.ssh
ls -la

on local....

ssh-keygen -b 4096
scp ~/.ssh/id_rsa.pub steve@139.144.235.212:~/.ssh/authorized_keys
ssh-copy-id steve@139.144.235.212
on server ..

ls .ssh

sudo chmod 700 ~/.ssh/
sudo chmod 600 ~/.ssh/*

exit

ssh steve@139.144.235.212

sudo nano /etc/ssh/sshd_config

PermitRootLogin no
PasswordAuthentication no
```
### reset ssh...
```python
sudo systemctl restart sshd
```

### firewall
```python
sudo apt-get install ufw
sudo ufw default allow outgoing
sudo ufw default deny incoming
sudo ufw allow ssh
```
### test server only on port 8000
```python
sudo ufw allow 8000
sudo ufw enable 
sudo ufw status
```
### copy application to server the -r is recursive copy and :~/ puts it in home folder
```python
scp -r acmeAI steve@172.104.16.132:~/
```
### on server
```python
sudo apt install python3-pip
sudo apt install python3-venv
python3 -m venv django_env
source django_env/bin/activate
source venv/bin/deactivate

pip install -r requirements.txt
if psyco error 
sudo apt-get install libpq-dev

```
### make sure static root 

```python
set in setting.py 
STATIC_ROOT = "staticfiles"
then run...
python manage.py collectstatic
python manage.py runserver 0.0.0.0:8000
```

sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi-py3

cd /etc/apache2/sites-abailable/
ls
copy file
sudo cp 000-default.conf acmeAI.conf

### edit copied conf
```
  
```

enable site..

sudo a2ensite acme_ai.conf

disable

sudo a2dissite 000-default.conf

sudo chown :www-data acmeAI/db.sqlite3
sudo chmod 664 acmeAI/db.sqlite3
sudo chown :www-data acmeAI/
sudo chown -R :www-data acmeAI/media
sudo chmod -R 775 acmeAI/media
sudo touch /etc/appAI/config.json

To activate the new configuration, you need to run:
  systemctl reload apache2

to see permission
ls -la

{
    "SECRET_KEY":"235nn354lksdfgi0342m,lfkl",
    "EMAIL":"oaksdfnoa",
}
import json
with open('etc/config.json) as config_file:
    config = json.load(config_file)

    DEBUG = config(DEBUG)


sudo ufw delete allow 8000    

sudo ufw allow http/tcp

sudo service apache2 restart
sudo systemctl status apache2.service

sudo chmod -R 777 /acme-project/


```
Alias /staticfiles /home/steve/acmeAI/staticfiles
  <Directory /home/steve/acmeAI/staticfiles>
    Require all granted
  </Directory>

  Alias /media /home/steve/acmeAI/media
  <Directory /home/steve/acmeAI/media>
    Require all granted
  </Directory>

  <Directory /home/steve/acmeAI/core>
    <Files wsgi.py>
      Require all granted
    </Files>
  </Directory>

  WSGIScriptAlias / /home/steve/acmeAI/core/wsgi.py
  WSGIDaemonProcess django_app python-path=/home/steve/acmeAI python-home=/home/steve/acmeAI/venv
  WSGIProcessGroup django_app
  ```
$ apachectl configtest
$ service apache2 restart

ssh steve@139.144.235.212
sudo chown -R deploy:www-data /home/steve/acme
chmod o+x /home/steve/
scp -r acme steve@139.144.235.212:/home/steve




http://127.0.0.1:8000/resumes/create/1/
http://127.0.0.1:8000/resumes/llm-and-list/1/
http://127.0.0.1:8000/resumes/update-description/1/
http://127.0.0.1:8000/resumes/job-covers/1/
http://127.0.0.1:8000/resumes/update-description/21/
http://127.0.0.1:8000/resumes/user-job-profile-form/1/
http://127.0.0.1:8000/resumes/index/

ssh root@143.42.3.106
St3ph3n!20072009!
sudo apt update
sudo apt install  libpq-dev postgresql postgresql-contrib
sudo -u postgres psql
CREATE DATABASE acme;
CREATE USER driver WITH PASSWORD 'S@FDGgd437asef4;
ALTER ROLE driver SET client_encoding TO 'utf8';
ALTER ROLE driver SET default_transaction_isolation TO 'read committed';
ALTER ROLE driver SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE acme TO driver;
\q
pip install Django psycopg2


PG_NAME=acme
PG_USER=driver
PG_PASS=S@FDGgd437asef4
PG_HOST=localhost

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myproject',
        'USER': 'myproject_user',
        'PASSWORD': 'myproject_database_password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
"ENGINE": "django.db.backends.postgresql_psycopg2",
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env('PG_NAME'), 
        "USER": env('PG_USER'),
        "PASSWORD": env('PG_PASS'),
        "HOST": env('PG_HOST'),
        'PORT': '',
    }
}
