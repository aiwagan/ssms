#!/usr/bin/env bash
#!/usr/bin/env bash
# Installing dependent libraries
sudo yum groupinstall "Development Tools"
sudo yum install libxslt libxslt-devel libxml libxml-devel


# Install postgresql
sudo rpm -Uvh https://yum.postgresql.org/9.6/redhat/rhel-7-x86_64/pgdg-centos96-9.6-3.noarch.rpm
sudo yum update
sudo yum install postgresql96-server postgresql96 postgresql96-devel postgresql96-contrib
sudo /usr/pgsql-9.6/bin/postgresql96-setup initdb
sudo su - postgres
createuser username
createdb dbname
psql -d dbname
# Generate password using python hashlib "md5" + hashlib.md5('password-1' + 'username').hexdigest()
ALTER USER username WITH PASSWORD 'hashlib_md5';
GRANT ALL PRIVILEGES ON DATABASE dbname TO username;
# Edit /var/lib/pgsql/data/pg_hba.conf  and change the authentication method to md5
sudo vim /var/lib/pgsql/data/pg_hba.conf
# Edit following and allow listener IPs if required
sudo vim /var/lib/pgsql/9.6/data/postgresql.conf
sudo systemctl start postgresql-9.6
sudo systemctl enable postgresql-9.6

