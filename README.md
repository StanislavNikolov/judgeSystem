# judgeSystem
A python/django based system for testing c/c++ solutions to algoritmic problems

##What it does now:
* Basic Login/register funtionality
* Task/test editing
* Testing solutions
* A simple blog
* Searching by tags

##Dependencies:
* Python 3.\2+
* Python modules: view requirements.txt
* g++ for compiling submissions
* postgreSQL
* rabbitmq
Refer at your distro's package manager documentation on how to do this properly.

##How to install:
0. Clone the repository `git clone https://github.com/Alaxe/judgesystem.git`
1. Setup database - you have a few options
    * install postgreSQL
    * setup database and user
    ```
    sudo su postgres
    createuser admin -P
    cretadb judgeSystemDB -U admin
    ```
2. Install rabbitmq
3. Setup settings
    * create variables in judgeSystem/sens.py
        * `EMAIL` - used for account confirmation
        * `EMAIL_PASSWORD` - password for that account
    * judgeSystem/settings.py
        * `SITE_HOST` - used for some links
        * Email backend and server
        * `TIME_ZONE`
4. run `sudo python setup.py` (as root)

##How to run:
  * Web server: `python manage.py runserver` (you can a add `url:port` pair as a
    parameter)
  * Celery server (as root): `sudo -- sh -c  'export C_FORCE_ROOT="true"; celery
    -A judgeSystem worker`
