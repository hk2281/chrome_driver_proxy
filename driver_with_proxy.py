import requests
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager 

from bs4 import BeautifulSoup
# s = Service('chromedriver.exe')
# options = webdriver.ChromeOptions()
# from clear import get_response
# s = Service(executable_path='D:\web_drivers\chrome\chromedriver.exe')

import requests

os.environ['HTTPS_PROXY'] = os.environ['HTTP_PROXY'] = ' '
print(requests.get('https://api.myip.com').text)

import os
import zipfile

from selenium import webdriver

PROXY_HOST = ''  # rotating proxy or host
PROXY_PORT =  # port
PROXY_USER = '' # username
PROXY_PASS = '' # password


manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
"""

background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
        singleProxy: {
            scheme: "http",
            host: "%s",
            port: parseInt(%s)
        },
        bypassList: ["localhost"]
        }
    };

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%s",
            password: "%s"
        }
    };
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);
""" % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)


def get_chromedriver(use_proxy=False, user_agent=None, options=None):
    os.environ['HTTPS_PROXY'] = os.environ['HTTP_PROXY'] = ''
    options = webdriver.ChromeOptions()
    serv = Service(executable_path='chromedriver.exe')
    if use_proxy:
        pluginfile = 'proxy_auth_plugin.zip'

        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)
        options.add_extension(pluginfile)
    if user_agent:
        options.add_argument('--user-agent=%s' % user_agent)
    os.environ['HTTPS_PROXY'] = os.environ['HTTP_PROXY'] = ''
    
    driver = webdriver.Chrome(
        service=serv,
        chrome_options=options)
    return driver

def main():
    import time
    driver = get_chromedriver(use_proxy=True)
    #driver.get('https://www.google.com/search?q=my+ip+address')
    driver.get('https://api.myip.com')
    time.sleep(5)
if __name__ == '__main__':
    import requests
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': 'assistFontSize=1',
        'Pragma': 'no-cache',
        'Referer': 'https://perv--mrm.sudrf.ru/modules.php?name=sud_delo&srv_num=1&name_op=sf&delo_id=1540005',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    print(requests.get(
        url='http://blag-gs--amr.sudrf.ru/modules.php?name=sud_delo&name_op=case&_uid=97b71f6e-d89f-4a49-926d-c2e9f4396bd2&_deloId=1540005&_caseType=0&_new=0&srv_num=1&_hideJudge=0',
        headers=headers,
        timeout=15
    ).status_code)


