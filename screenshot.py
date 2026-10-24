
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = None

try:
    # Open Chrome browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Open Selenium test website
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    print("Website opened successfully")

    # Find the text input field
    text_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "my-text"))
    )

    # Enter text automatically
    text_box.send_keys("Selenium Automation Test")

    # Click the submit button
    submit_button = driver.find_element(
        By.CSS_SELECTOR, "button"
    )
    submit_button.click()

    # Verify the success message
    message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )

    assert message.text == "Received!"

    print("Test Passed: Form submitted successfully")

    # Save screenshot
    driver.save_screenshot("success_screenshot.png")
    print("Screenshot saved successfully")

except Exception as e:
    print("Test Failed:", e)

    if driver is not None:
        driver.save_screenshot("failure_screenshot.png")

finally:
    if driver is not None:
        driver.quit()
        print("Browser closed")
