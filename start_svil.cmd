rem start server from Anaconda prompt
echo SVIL site starrting..
copy marketupdate_site\settings_svil.py marketupdate_site\settings.py /Y
copy marketupdate_frontend\static\js\App_svil.js marketupdate_frontend\static\js\App.js /Y
python manage.py runserver