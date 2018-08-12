sudo /etc/init.d/mysql start
sudo mysql -uroot -e "CREATE DATABASE djbase;"
sudo mysql -uroot -e "CREATE USER 'django'@'localhost' IDENTIFIED BY 'django';"
sudo mysql -uroot -e "GRANT ALL ON djbase.* TO 'django'@'localhost';"
sudo mysql -uroot -e "GRANT USAGE ON *.* TO 'django'@'localhost';"
sudo mysql -uroot -e "FLUSH PRIVILEGES;"

sudo pip3 install --upgrade mysqlclient

