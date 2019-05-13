restapi-sandbox
=========
RESTFUL JSON API  
Flask  
mongodb  
robo 3T  
Postman  
app dir -> person

----------------

Playbook
----------------


File:

    - hosts: servers
      roles:
         - mongodb
         - virtualpython

Command:

Postman  
sudo tar -xzf postman.tar.gz -C /opt
sudo ln -s /opt/Postman/Postman /usr/bin/postman

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

robo 3T  
sudo tar -xzf ../robo3t-1.3.1-linux-x86_64-7419c406.tar.gz -C /opt
sudo ln -s /opt/robo3t-1.3.1-linux-x86_64-7419c406/bin/robo3t /usr/bin/robomongo


License
-------

GNU General Public License v3.0

Author Information
------------------

An optional section for the role authors
