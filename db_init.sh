sudo mysql -uroot -e "CREATE DATABASE djbase;"
sudo mysql -uroot -e "CREATE USER 'django@localhost' IDENTIFIED BY 'pass123';"
sudo mysql -uroot -e "GRANT ALL ON dj.* TO 'django@localhost';"
sudo mysql -uroot -e "GRANT USAGE ON *.* TO 'django@localhost';"
sudo mysql -uroot -e "FLUSH PRIVILEGES;"

sudo pip3 install libmysqlclient-dev
sudo pip3 install mysqlclient

