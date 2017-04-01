from selenium import webdriver
import argparse
import yaml


def signin(name, email, year):
    """
        Sign into the sparsa meeting

        :param name: the users name
        :param email: the users email
        :param year: the users year in school
    """
    browser = webdriver.Firefox()
    browser.get("https://www.sparsa.org/signin")
    form_name = browser.find_element_by_id('entry_1000000')
    form_email = browser.find_element_by_id('entry_1000001')
    form_name.send_keys(name)
    form_email.send_keys(email)
    browser.find_element_by_id('group_1000005_%d' % int(year)).click()
    browser.find_element_by_id('ss-submit').click()


def main():
    """
        Main file to get parameters
    """
    parser = argparse.ArgumentParser(description="Sign in to sparsa, run with" \
                                     " no arguments to read from config file")
    parser.add_argument('-n', dest='name', help='Your name, first & last')
    parser.add_argument('-e', dest='email', help='Your email')
    parser.add_argument('-y', dest='year', help='What year you are in school')

    args = parser.parse_args()
    name = args.name
    email = args.email
    year = args.year
    if not name or not email or not year:
        with open("config.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)

        name = cfg['info']['name']
        email = cfg['info']['email']
        year = cfg['info']['year']

    print(name, email, year)
    signin(name, email, year)

if __name__ == '__main__':
    main()
