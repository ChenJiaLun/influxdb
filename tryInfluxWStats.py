#Project influxdb
__author__ = 'al'


from influxdb import InfluxDBClient
from linux_metrics import cpu_stat

def db_vars():
    user = 'root'
    password = 'root'
    dbname = 'cpustats'
    dbuser = 'al'
    dbuser_password = 'my secrect'
    json_body = [
        {
            "measurement": "cpu_util",
            "tags": {
                "host": "dadspc",
                "region": "millstone"
            },
            "time": ""
        }
    ]