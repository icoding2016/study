### Introduction
This is a demo code for a simple kafka + db application,
coming from the "Aiven's homework task".

The task is to implement a system that monitors website availability over the
network, produces metrics about this and passes these events through an Aiven Kafka instance into an Aiven PostgreSQL database.


### Features & Implementation

- Website(s) availability check

  Support peiriodical check for multiple websites. (one thread for each)
  There are 3 configurable parameters for each website to be monitored
  - URL
  - An regular expression used as an extra condition for the check (optional)
  - Checking interval
  
 The parameters are configurable through the config file (config.json)

- Kafka

  Kafka service is used to stream the metrics.

- Database

  A PostgreSQL database is used to save the metrics.
  The database and table used for the the metrics will be created if they are not exist when the program is running.
  
- Configurations

  The basic information for Kafka and database services is configurable through the config file. E.g. host/post, user/password for the service.
  The config file will be generated with default values at the first run if it is not in the current folder.


### Run & test the code 

- Run the code:

  python main.py
- unit test

  python -m unittest discover .

Note:
There is only a small piece of unit test code in this demo. Far from a good coverage.

