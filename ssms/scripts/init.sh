#! /bin/bash
echo "Cleaning ..."
make clean
echo "Installing dependencies ..."
make install
echo "Starting DJANGO development server ..."
make run
