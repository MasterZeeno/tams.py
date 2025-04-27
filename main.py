#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import time
from datetime import datetime
from urllib.parse import urljoin

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException

def setup_driver():
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Runs Chrome in headless mode.
    chrome_options.add_argument('--no-sandbox')  # Bypass OS security model
    chrome_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
    chrome_options.add_argument('--disable-gpu')  # applicable to windows os only
    chrome_options.add_argument('start-maximized')  # open Browser in maximized mode
    chrome_options.add_argument('disable-infobars')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.binary_location = "/usr/bin/chromium-browser"

    return webdriver.Chrome(options=chrome_options)

def print_msg(colorcode, icon, msg):
    print(f"\033[{colorcode}m  {icon} {msg}\033[0m")

def print_success(msg):
    print_msg("92", "✔", msg)

def print_error(msg):
    print_msg("91", "✖", msg)

def print_warning(msg):
    print_msg("93", "⚠️", msg)

def abort(driver, msg=None):
    if isinstance(driver, str):
        msg = driver
        driver = None
    
    if driver is not None:
        driver.quit()
    
    print_error(msg or "Aborted.")
    sys.exit(1)

def process_element(driver, parent=None, by=By.ID, locator=None, multiple=False, timeout=10):
    if locator is None:
        print_error("Locator must be provided.")
        return None
        
    if parent is None:
        parent = driver
        
    try:
        if multiple:
            elements = WebDriverWait(parent, timeout).until(
                EC.presence_of_all_elements_located((by, locator))
            )
            return elements
        else:
            element = WebDriverWait(parent, timeout).until(
                EC.presence_of_element_located((by, locator))
            )
            return element
    except TimeoutException:
        return None
    except NoSuchElementException:
        print_warning(f"Element not found: {locator} by {by}")
        return None
    except Exception as e:
        print_error(f"Error processing element '{locator}' by {by}: {e}")
        return None

def navigate(driver, url):
    try:
        driver.get(url)
    except Exception as e:
        abort(driver, f"Error navigating to {url}: {e}")
        
def login(driver, args):
    navigate(driver, args.homepage)

    try:
        login_form = process_element(driver, by=By.ID, locator="login-form")
        if not login_form:
            abort(driver, "Login form not found.")
        
        for key, value in vars(args).items():
            if key != "homepage":
                element = process_element(driver, login_form, by=By.NAME, locator=key)
                if not element:
                    abort(driver, f"Login input '{key}' not found.")
                    
                element.clear()
                element.send_keys(value)

        signin_button = process_element(driver, login_form, by=By.XPATH, locator=".//button[@type='submit']")
        if signin_button:
            try:
                signin_button.click()
            except ElementClickInterceptedException:
                login_form.submit()
        else:
            login_form.submit()
        
        login_success = process_element(driver, by=By.ID, locator="employee_id")
        if login_success:
            print_success("Login successful!")
        else:
            abort(driver, "Login failed: 'employee_id' element not found.")
    
    except Exception as e:
        abort(driver, f"Failed to login: {e}")

def main():
    arg_defaults = ["homepage", "username", "password"]
    parser = argparse.ArgumentParser(description="TAMS Automater")
    
    for arg in arg_defaults:
        parser.add_argument(arg, help=arg.capitalize())
        
    args = parser.parse_args()

    driver = setup_driver()
    login(driver, args)
    driver.save_screenshot("screenshot.png")
    driver.quit()

if __name__ == "__main__":
    main()
