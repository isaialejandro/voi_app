# voi_app
App for critical incidents history.


            ###---------###
#Config env variables:
1.- Create a ".env" file in same settings.py level.
2.- put to the new .env file something like this:
    DEV_DB_NAME = 'something'
    DEV_DB_USR = 'kiss me'
    DEB_DB_PWD = 'im horny'
    DEV_DB_HOST = 'seriously man'
    DEV_DB_PORT = 123456
3.- Go to base.py settings file, import following:
    "from dotenv import load_dotenv"
    "load_dotenv()"
4.- In settings.py file, replace hardcoded data with dotenv variables call:
    os.getenv('DEV_DB_NAME')
    ...
    ...
5.- Test connectin project.
6.- By happy and buy some beer! :)
            ###---------###