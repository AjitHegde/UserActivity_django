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
export SECRET_KEY='_np+$b*9z3z!sg4-hpk%f*(s&dpbd^=-y=r!pbtm&d&1mp731#'
python3 manage.py migrate

