# southwest-headers
IYKYK. 😄

Working on Ubuntu 20.04 hosted by DigitalOcean. YMMV.

## Prerequisites

* python3 and pip3 are installed
* Google Chrome is installed

## Installation

```
git clone https://github.com/byalextran/southwest-headers
cd southwest-headers

pip3 install virtualenv
virtualenv env

env/bin/pip install -r requirements.txt
```

Figure out what Google Chrome version you're running and [download the same version of ChromeDriver](https://chromedriver.chromium.org/downloads) for your platform.

Unzip it into the current directory.

Example:

```
wget https://chromedriver.storage.googleapis.com/96.0.4664.45/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
```

Modify ChromeDriver so Southwest doesn't detect Selenium. [Huge hat tip](https://stackoverflow.com/a/52108199).

**Note**: Replace `dog` in the command below with three random alphabetic characters. It has to be exactly three characters.

`perl -pi -e 's/cdc_/dog_/g' chromedriver`

## Usage


```
# no arguments saves the headers to southwest_headers.json in the current directory
env/bin/python southwest-headers.py

# include an argument if you want to specify where the headers are saved to
env/bin/python southwest-headers.py /PATH/TO/FILENAME.json
```

The JSON file can then be used in whatever script to auto check-in. I'll be updating [southwest-checkin](https://github.com/byalextran/southwest-checkin) here shortly to support these headers.

## Adding a Cron Job

For now, I'd recommend running this script as a daily cronjob to ensure headers are refreshed regularly.

Example:

`0 2 * * *       cd /PATH/TO/southwest-headers/ && env/bin/python southwest-headers.py`

That would run at 2:00am every day.
