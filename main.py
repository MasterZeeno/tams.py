from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Runs Chrome in headless mode.
chrome_options.add_argument('--no-sandbox')  # Bypass OS security model
chrome_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
chrome_options.add_argument('--disable-gpu')  # applicable to windows os only
chrome_options.add_argument('start-maximized')  # open Browser in maximized mode
chrome_options.add_argument('disable-infobars')
chrome_options.add_argument('--disable-extensions')

# Set path to chromedriver if it's not in PATH
# driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chrome_options)
driver = webdriver.Chrome(options=chrome_options)

# Navigate to a page
driver.get("https://hcc-tams.com.ph")

# # Find an element and print text
# heading = driver.find_element(By.TAG_NAME, "h1")
# print("Page heading:", heading.text)

try:
    # Wait up to 10 seconds for the element to be present
    sign_in_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Sign In']"))
    )
    print("- Sign In button found!")
    # Save screenshot
    driver.save_screenshot("screenshot.png")
except Exception as e:
    print("- Sign In button not found:", e)


# Close the browser
driver.quit()
