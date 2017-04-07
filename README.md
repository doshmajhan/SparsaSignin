# SparsaSignin
Script to sign into sparsa

## Requirements
```pip install -r requirements.txt```

## If using Chrome
Make sure chromedriver is in your path, or add ```chromepath="/path/to/chromedriver"``` to the config.yml under the info tag

## If using Firefox
Install firefox and gecko driver, make sure they're in your PATH

### How to install the geckodriver
You may either install the binary using the instructions below, or you may use the provided binary file. Please ensure the binary is in your PATH.

```bash
wget https://github.com/mozilla/geckodriver/releases/download/v0.13.0/geckodriver-v0.13.0-linux64.tar.gz
tar xvf geckodriver-*
sudo mv geckodriver /usr/bin
```
