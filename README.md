# southwest-headers
IYKYK. 😄

Working on Ubuntu 20.04 hosted by DigitalOcean. YMMV.

## Prerequisites

* python3
* pip3

## Installation

### Install Google Chrome

```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
```

### Install Southwest Headers

```
git clone https://github.com/byalextran/southwest-headers
cd southwest-headers

pip3 install virtualenv
virtualenv env

env/bin/pip install -r requirements.txt
```

### Install ChromeDriver

Figure out what version of Chrome you've installed.

`google-chrome --version`

[Download the same version of ChromeDriver](https://chromedriver.chromium.org/downloads) into the `southwest-headers` directory and unzip it.

Example:

```
wget https://chromedriver.storage.googleapis.com/96.0.4664.45/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
```

### Modify ChromeDriver

This is necessary so Southwest doesn't detect Selenium and provide invalid headers. [Huge hat tip](https://stackoverflow.com/a/52108199).

**Note**: Replace `dog` in the command below with *exactly* three random alphabetic characters.

`perl -pi -e 's/cdc_/dog_/g' chromedriver`

## Usage

No arguments saves the headers to `southwest_headers.json` in the current directory.

`env/bin/python southwest-headers.py`

Include an argument if you want to specify where the headers are saved to.

`env/bin/python southwest-headers.py /PATH/TO/FILENAME.json`

The JSON file can then be used in whatever app to auto check-in (assuming the script adds support for reading this file).

I've added support in my script here:

https://github.com/byalextran/southwest-checkin

## Add a Cron Job

For now, I'd recommend running this script as a daily cronjob to ensure headers are refreshed regularly. They change periodically, so if this isn't done there's a chance you'll have expired headers when you try to check in.

`crontab -e`

And then copy/paste the following at the end of the file (making sure to update the path):

`0 2 * * *       cd /PATH/TO/southwest-headers/ && env/bin/python southwest-headers.py`

That would run at 2:00am every day with the header file found at `/PATH/TO/southwest-headers/southwest_headers.json` (the default filename).
