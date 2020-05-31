sudo apt-get install python3
sudo apt-get install python3-pip

DJANGO=`which django-admin | wc -l`

if [ $DJANGO -ge "1" ]
then
	echo "\nDjango admin already installed\n"
else
	pip3 install django
	echo "Django installed"
fi

pip3 install -r requirements.txt

echo "\nPopulating db with dummy users\n"

python3 manage.py migrate

