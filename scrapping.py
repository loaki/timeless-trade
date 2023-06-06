import random
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


def stealth_driver():
    # create a new Service instance and specify path to Chromedriver executable
    # service = ChromeService(executable_path=ChromeDriverManager().install())
    service = ChromeService(executable_path="$HOME/chromedriver/stable/chromedriver")

    # create a ChromeOptions object
    options = webdriver.ChromeOptions()
    #run in headless mode
    options.add_argument("--headless")
    # disable the AutomationControlled feature of Blink rendering engine
    options.add_argument('--disable-blink-features=AutomationControlled')
    # disable pop-up blocking
    options.add_argument('--disable-popup-blocking')
    # start the browser window in maximized mode
    options.add_argument('--start-maximized')
    # disable extensions
    options.add_argument('--disable-extensions')
    # disable sandbox mode
    options.add_argument('--no-sandbox')
    # disable shared memory usage
    options.add_argument('--disable-dev-shm-usage')

    # Set navigator.webdriver to undefined
    # create a driver instance
    driver = webdriver.Chrome(service=service, options=options)
    # Change the property value of the navigator for webdriver to undefined
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    user_agents = [
        # Add your list of user agents here
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    ]
    # select random user agent
    user_agent = random.choice(user_agents)
    # pass in selected user agent as an argument
    options.add_argument(f'user-agent={user_agent}')

    #enable stealth mode
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

    return driver


def head_driver():
    # service = ChromeService(executable_path="$HOME/chromedriver/stable/chromedriver")
    options = webdriver.ChromeOptions()
    #run in headless mode
    # disable the AutomationControlled feature of Blink rendering engine
    # options.add_argument("start-maximized") # open Browser in maximized mode
    # options.add_argument("disable-infobars") # disabling infobars
    # options.add_argument("--disable-extensions") # disabling extensions
    # options.add_argument("--disable-gpu") # applicable to windows os only
    # options.add_argument("--disable-dev-shm-usage") # overcome limited resource problems
    # options.add_argument("--no-sandbox") # Bypass OS security model


    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--no-sandbox")


    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    return driver

def has_display():
    try:
        from tkinter import Tk

        tk = Tk()
        Screen.width = tk.winfo_screenwidth()
        Screen.height = tk.winfo_screenheight()
        Screen.view_width = tk.maxsize()[0]
        Screen.view_height = tk.maxsize()[1]
        tk.destroy()
        del Tk
        return True
    except Exception:
        return False

import time
def scrap_url(url: str):
    print(has_display())
    driver = head_driver()
    driver.get(url)
    # Wait for page to load
    # while r:=driver.execute_script("return document.readyState") != "complete":
    #     pass
    # time.sleep(0.2)
    # # Take screenshot
    # driver.save_screenshot("scrap.png")

    # time.sleep(5)
    # driver.save_screenshot("scrap2.png")
    # # Close browser
    # driver.quit()
