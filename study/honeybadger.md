# Study of Honeybadger

![Honeybadger](img/honeybadger_logo.png "https://www.honeybadger.io/assets/")

Visit honey badger [here](https://www.honeybadger.io/ "visit honeybadger.io")

### What is Honeybadger

Honeybadger is a Monitoring and error tracking software, fundamentally it will help you do error tracking away from the server and you'll be notified immidietly should an error occur via their dashboard or mail if configured, it makes tracking the issues easier with an easy to use interface that easily lets you get to the root of the problem. It can also keep track of the uptime of your server and notify you if it ever becomes unresponsive it will also notify you if there is an issue regarding your ssl certificate. And if your application uses cron jobs to send mails for example honeybadger can be helpfull in making sure that your cron jobs finish successfully. Honeybadger also comes with some improvements to the logging of your application and their own querying language that makes what would be a tedious task into something much less time consuming together with their improved logs this should make your experience monitoring user behaviour and potential attackers alot easier. There are alot of features that honeybadgers brings however in our application we'll mainly be using error tracking, logging and uptime checks hence this text is mainly based around those features. 

### Instructions for setup

Incorporating honeybadger proved very simple and you can easily follow the instructions for your desired programming language or framework https://docs.honeybadger.io/lib/python/#getting-started
Ill do a walkthrough of the installtion process using flask.

Firstly you'll want to install honeybadger using

```
$ pip install honeybadger
```

Using Flask you'll want to make use of the FlaskHoneyBadger extension like the example below however make sure that you install blinker since that is a dependancy.

```
$ pip install blinker
```

If you have not already made an account you'll have to do so now in order to get an API key.

```
import os
from flask import Flask, jsonify, request
from honeybadger.contrib import FlaskHoneybadger

app = Flask(__name__)
app.config['HONEYBADGER_ENVIRONMENT'] = 'production'
app.config['HONEYBADGER_API_KEY'] = os.environ.get(HONEYBADGER_API_KEY)
app.config['HONEYBADGER_PARAMS_FILTERS'] = 'password, secret, credit-card'
FlaskHoneybadger(app, report_exceptions=True)

@app.route('/')
def index():
[...]

```

Further more if you want to make use of honeybadger as a log handler you add the handler to logging like below

```
import logging
from honeybadger.contrib.logger import HoneybadgerHandler

hb_handler = HoneybadgerHandler(api_key='hbp_s4S4BoIAyqht3QpwD8ikDuHBku60Z90a6xY7')
logger = logging.getLogger('honeybadger')
logger.addHandler(hb_handler)

try:
  1/0
except:
  logger.error("Something went wrong")
```

Setting up an uptime check
If you want to setup an uptime check to catch any server downtime this is also quite easy to do, simply go to your project page and navigate to uptime through the navbar. From here click Add an uptime check which will bring you to the creation screen where you can put in your domain name and then customize the check to your needs.

### Honeybadger in devops

Honeybadger fits well into devops because it mainly helps us automate some tasks such as error handling and receiving feedback from endusers it also helps us monitor and log which are important for devops. Since a principe of devops is automation it's feels good to be able to automate what can be automated and getting immediete feedback on errors instead of relying on a manual deepdive into  log files on a remote server having them easily accessible through the honeybadger dashboard page and immidietly noticible via notifications that you can configure to reach you through several options such as mail, slack or jira.

Honeybadger can also be used to track any downtime on the server effectively notifying team members whenever the server goes down as well as measuring things like api calls, slow process and bottlenecks that can help us make our application more efficient.

The tool also improves upon the logging and makes monitoring logs alot easier, using their own querying language to sift through the logs will make the operation more efficient and potentially help you discover unusual behaviour on your site more easily.

I also believe that honeybadger could be a bonus for cooperation between developers and ops as honeybadger can help make sure that both parties can be equally informed of any issues in real time and could help them get on the same page faster.

#### Summary

In summary i believe honeybadger is a powerfull tool that can help us improve error discovery and handling, monitoring and logging, optimising applications through removal of bottlenecks and keep team members informed of any issues all things which i believe makes it well aligned with DevOps overall the tool should help improve reliability of the server and developers ability to quickly fix and issues. Within the area of itsec it can also be of use in monitoring suspicious behaviour on your applications.
