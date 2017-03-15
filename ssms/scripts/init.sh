#! /bin/bash
echo "Checking links to other services ..."
cat /etc/hosts
echo "Cleaning ..."
make clean
echo "Installing dependencies ..."
make install
echo "Migrating models ..."
make migrate
echo "Starting DJANGO development server ..."
make run
