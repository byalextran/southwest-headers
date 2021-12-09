# southwest-headers
IYKYK. 😄

I'll update this to be more user friendly later. This all works on Ubuntu 20.04 hosted by DigitalOcean. YMMV.

## Prerequisites

* python3 and pip3 are installed
* Google Chrome is installed

## Installation

```
git clone https://github.com/byalextran/southwest-headers`
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

`perl -pi -e 's/cdc_/dog_/g' chromedriver`

## Usage

 `env/bin/python southwest-headers.py ABCDEF "First Name" "Last Name" $PWD/southwest_headers.json`

 The last argument is where you want the headers output. The above example assumes the current working directory in a file named `southwest_headers.json`.

 That file can then be used in whatever script to auto check-in. I'll be updating [southwest-checkin](https://github.com/byalextran/southwest-checkin) here shortly to support these headers.

 It appears that you don't need a valid confirmation number to get headers that work. So I'm thinking this script could be set to run at a set frequency to ensure the headers are ready to go before check-in. (Otherwise, if you incorporate this script before trying to check in you'll lose some precious seconds. 😆)
