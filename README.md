Veritas Operation Manager REST API
---------------------------------
```
usage: vom_api.py [-h] [-username USERNAME] [-passwod PASSWORD]
                  [-vom_server_ip VOMSERVERIP]

optional arguments:
  -h, --help            show this help message and exit
  -username USERNAME, --Username USERNAME
                        Please Prvide XLS dir name with full path.
  -passwod PASSWORD, --Password PASSWORD
                        Please Provilde xls filename.
  -vom_server_ip VOMSERVERIP, --VomServerIp VOMSERVERIP
                        Please Provilde IP address of Veritas Operation
                        Manager server.
```
Parameter
---------
Parameter need to changed.
1. Portnumber
2. Domain

Example
-------

1.  python vom_api.py  -username <username> -passwod <password> -vom_server_ip <VOM server IP>

Output Will be stored on final_out.txt
