from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import selenium
from PIL import Image
import time
import os
import pyautogui
import pyperclip


'''
# Open the file containing usernames
with open('usernames.txt', 'r') as file:
    # Read all the lines from the file
    lines = file.readlines()

# Iterate over each line (username)
for line in lines:
    # Remove any leading/trailing whitespace
    username = line.strip()
'''  
# Get user input
username = input("enter ur username: ")
password = input("enter ur password: ")

#website_url = "https://www.stealmylogin.com/demo.html"
website_url = "file:///D:/jayyanth/Jay/programs/python%20programms/capitcha%20project/images/login.html"

# Initialize the web driver (replace 'path/to/chromedriver' with the actual path to your web driver)
#driver = webdriver.Chrome("C:\ProgramData\Microsoft\Windows\Start Menu\Programs")
# Set up Chrome options to start maximized
options = Options()
options.add_argument("--start-maximized")


#chromeOptions = webdriver.ChromeOptions()
#chromeOptions.add_experimental_option("excludeSwitches", ['enable-automation']);

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(options=options)

# Navigate to the website
driver.get(website_url)








# Find the username and password input fields

username_field = driver.find_element(by=By.NAME, value='username')

password_field = driver.find_element(by=By.NAME, value='password')

# Enter the username and password
username_field.send_keys(username)
password_field.send_keys(password)

time.sleep(5)

'''
this has opened website and given input user name and given password aslo

'''




def capture_screenshot(top_left_x, top_left_y, bottom_right_x, bottom_right_y, save_path, save_name):
    """
    Captures a screenshot of the specified rectangular area and saves it to the given location.
    
    Parameters:
    top_left_x (int): The x-coordinate of the top-left corner of the rectangular area.
    top_left_y (int): The y-coordinate of the top-left corner of the rectangular area.
    bottom_right_x (int): The x-coordinate of the bottom-right corner of the rectangular area.
    bottom_right_y (int): The y-coordinate of the bottom-right corner of the rectangular area.
    save_path (str): The path to the directory where the screenshot will be saved.
    save_name (str): The name of the screenshot file.
    """
    # Capture the screenshot
    screenshot = pyautogui.screenshot(region=(top_left_x, top_left_y, bottom_right_x - top_left_x, bottom_right_y - top_left_y))
    
    # Create the save directory if it doesn't exist
    os.makedirs(save_path, exist_ok=True)
    
    # Save the screenshot
    screenshot.save(os.path.join(save_path, save_name))
    print(f"Screenshot saved at: {os.path.join(save_path, save_name)}")

# Get user input for the coordinates
top_left_x = 765
top_left_y = 675
bottom_right_x = 860
bottom_right_y = 695

# Specify the save path and file name
save_path = "D:\jayyanth\Jay\programs\python programms\capitcha project"
save_name = "screenshot.png"


time.sleep(5)
# Capture the screenshot
capture_screenshot(top_left_x, top_left_y, bottom_right_x, bottom_right_y, save_path, save_name)

'''
snapshot completed and saved in D:\jayyanth\Jay\programs\python programms\capitcha project locartion

now reading the captcha....
'''

#-------------------------------------------------------------------------------------------------------

Image_link = "D:\jayyanth\Jay\programs\python programms\capitcha project\screenshot.png"

X, Y = pyautogui.size()

#err_x = int(input("enter the difference in standard X and your x : "))
err_x = 0 
#err_y = int(input("enter the difference in standard Y and your y : "))
err_y = 0

# print(x, y)

'''
def Resloved_x_y_move( a, b):
    a = (a/1920)*X
    b = (b/1080)*Y

    # print(a, b)

    pyautogui.moveTo(a,b)
    pyautogui.click()
    
'''

# Set up Chrome options to start maximized
options = Options()
options.add_argument("--start-maximized")

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(options=options)

# Navigate to the webpage
driver.get("https://lens.google.com/")

#upload a file
x, y = (1100,620)
#Resloved_x_y_move(x, y)
pyautogui.moveTo(x+err_x, y+err_y)
pyautogui.click()
time.sleep(3)

#file name
x, y = (325,520)
#Resloved_x_y_move(x, y)
pyautogui.moveTo(x+err_x, y+err_y)
pyautogui.click()
pyautogui.write(Image_link)
pyautogui.press("enter")
time.sleep(3)

#text button in google lens
x, y = (460,940)
#Resloved_x_y_move(x, y)
pyautogui.moveTo(x+err_x, y+err_y)
pyautogui.click()
time.sleep(3)

#select text button in google lens
x, y = (1410,770)
#Resloved_x_y_move(x, y)
pyautogui.moveTo(x+err_x, y+err_y)
pyautogui.click()
time.sleep(3)

#copy text button in google lens
x, y = (1050,350)
#Resloved_x_y_move(x, y)
pyautogui.moveTo(x+err_x, y+err_y)
pyautogui.click()
time.sleep(3)

# Get the copied text
copied_text = pyperclip.paste()

# Store the text in a variable
text = copied_text

# print(text)


def remove_spaces(input_string):
    # Remove spaces using list comprehension
    result = ''.join([char for char in input_string if char != ' '])
    return result

# Get user input
input_string = text

# Call the function to remove spaces
output_string = remove_spaces(input_string)

print("Original string:", input_string)
print("String without spaces:", output_string)

# Close the browser
driver.quit()

#-------------------------------------------------------------------------------------------------------

time.sleep(3)
'''
# Find the CAPTCHA DESIGNATED BOX using the ID
#captcha = driver.find_element_by_id('captcha-input')
captcha = driver.find_element(by=By.ID, value='captcha-input')


captcha.send_keys(output_string)

'''

pyautogui.moveTo(837,741,1)
pyautogui.click()
pyautogui.write(output_string)
time.sleep(1)
pyautogui.click(950,801)

# Submit the form by pressing Enter
# password_field.send_keys(Keys.RETURN)

# Wait for the page to load (adjust the time as needed)
time.sleep(5)

# Close the browser
driver.quit()
