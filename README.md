restapi-sandbox
=========
RESTFUL JSON API  
flask http://flask.pocoo.org    
mongodb https://www.mongodb.com   
robo 3T https://robomongo.org     
postman  https://www.getpostman.com  
vagrant  https://www.vagrantup.com  
virtualbox  https://www.virtualbox.org  
python https://www.python.org     


----------------

Playbook
----------------


File:

    - hosts: servers
      roles:
         - mongodb
         - virtualpython

Command:

git clone this-project  
vagrant up control02  
vagrant ssh control02  
source /home/vagrant/venv27/bin/activate  
cp -R /vagrant/person /home/vagrant/venv27/  
cd /home/vagrant/venv27/person  
python runapp.py  

Postman  Install  
sudo tar -xzf postman.tar.gz -C /opt
sudo  
ln -s /opt/Postman/Postman /usr/bin/postman

Postman Desktop Shortcut  
cat > ~/.local/share/applications/postman.desktop <<EOL  
[Desktop Entry]  
Encoding=UTF-8  
Name=Postman  
Exec=postman  
Icon=/opt/Postman/app/resources/app/assets/icon.png  
Terminal=false  
Type=Application  
Categories=Development;  
EOL  

robo 3T  Install  
sudo tar -xzf ../robo3t-1.3.1-linux-x86_64-7419c406.tar.gz -C /opt  
sudo ln -s /opt/robo3t-1.3.1-linux-x86_64-7419c406/bin/robo3t /usr/bin/robomongo

GET
<div align="center">
    <img src="/screenshots/GET.JPG" width="400px"</img>
</div>
POST
<div align="center">
    <img src="/screenshots/POST.JPG" width="400px"</img>
</div>
PUT
<div align="center">
    <img src="/screenshots/PUT.JPG" width="400px"</img>
</div>
LIST
<div align="center">
    <img src="/screenshots/LIST.JPG" width="400px"</img>
</div>
DELETE
<div align="center">
    <img src="/screenshots/DELETE.JPG" width="400px"</img> 
</div>


License
-------

GNU General Public License v3.0

Author Information
------------------

An optional section for the role authors
