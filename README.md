# ci-cd

a sample python code to perform ci-cd 

Repo setup:

create a folder called ci-cd
>mkdir ci-cd
>touch index.html
    hello world

>touch cicd.py
    integrate git python 

script to deply
>touch deploy.sh
take a backup
remove exist files in var/www/html
copy new files from ~ci-cd to /var/www/html
restart nginx

lunch a ec2 instance
>sudo apt update
>sudo apt install nginx
>sudo pip install GitPython
>sudo crontab -e
    * * * * * python ~/ci-cd/cicd.py
