from appium import webdriver

def init_driver_method():
    params = {}
    params['deviceName'] = '40a55ff27d82'
    params['platformName'] = 'Android'
    params['platformVersion'] = '5.1.1'

    params['appPackage'] = 'com.android.settings'
    params['appActivity'] = '.Settings'

    # params['appPackage'] = 'com.sina.weibo'
    # params['appActivity'] = '.account.login.LoginActivity'

    params['unicodeKeyboard'] = True
    params['resetKeyboard'] = True
    params['autoGrantPermissions'] = True

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', params)

    return driver
