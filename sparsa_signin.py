import argparse
from selenium import webdriver


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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Sign in to sparsa")
    parser.add_argument('-n', dest='name', help='Your name, first & last', required=True)
    parser.add_argument('-e', dest='email', help='Your email', required=True)
    parser.add_argument('-y', dest='year', help='What year you are in school',
                        required=True)

    args = parser.parse_args()
    signin(args.name, args.email, args.year)
