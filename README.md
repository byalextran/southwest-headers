# southwest-headers
IYKYK. 😄

Working on Ubuntu 20.04 hosted by DigitalOcean. YMMV.

## Prerequisites

* python3
* pip3

## Installation

### Install Google Chrome

    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo dpkg -i google-chrome-stable_current_amd64.deb

Note: Tested and working with v108. v96 _doesn't_ work, so please update Chrome if using a version older than v108.

### Install Southwest Headers

    git clone https://github.com/byalextran/southwest-headers
    cd southwest-headers

    pip3 install virtualenv
    virtualenv env

    env/bin/pip install -r requirements.txt

### Updating Southwest Headers    
    cd southwest-headers
    git pull
    rm -rf env
    virtualenv env
    env/bin/pip install -r requirements.txt

## Usage

No arguments saves the headers to `southwest_headers.json` in the current directory.

    env/bin/python southwest-headers.py

Include an argument if you want to specify where the headers are saved to.

    env/bin/python southwest-headers.py /PATH/TO/FILENAME.json

The JSON file can then be used in whatever app to auto check-in (assuming the script adds support for reading this file).

I've added support in my script here:

https://github.com/byalextran/southwest-checkin

## Add a Cron Job

For now, I'd recommend running this script as a daily cronjob to ensure headers are refreshed regularly. They change periodically, so if this isn't done there's a chance you'll have expired headers when you try to check in.

    crontab -e

And then copy/paste the following at the end of the file (making sure to update it with the *absolute* path):

    0 2 * * *       cd /ABSOLUTE/PATH/TO/southwest-headers/ && env/bin/python southwest-headers.py

That would run at 2:00am every day with the file `southwest_headers.json` (the default filename) saved in the `southwest-headers` folder.
