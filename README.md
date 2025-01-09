# CAPTCHA Automation Project

This project automates the process of solving CAPTCHA using Python and Selenium, along with tools like PyAutoGUI and Pyperclip. The automation involves taking a screenshot of the CAPTCHA, extracting the text using Google Lens, and then entering the text into a web form.

---

## Prerequisites

Before running the code, ensure you have the following installed:

1. **Python 3.8+**
2. **Selenium**
    ```bash
    pip install selenium
    ```
3. **Pillow** (for image processing)
    ```bash
    pip install pillow
    ```
4. **PyAutoGUI** (for GUI automation)
    ```bash
    pip install pyautogui
    ```
5. **Pyperclip** (for clipboard handling)
    ```bash
    pip install pyperclip
    ```
6. **Chrome WebDriver**
   - Download the Chrome WebDriver compatible with your Chrome browser version.
   - Add the WebDriver executable to your system PATH.

---

## Project Directory Structure

```
CAPTCHA Automation Project/
|-- login.html                   # Test login page (optional)
|-- usernames.txt                # File containing test usernames (if applicable)
|-- script.py                    # Main Python script (provided code)
|-- screenshot.png               # CAPTCHA screenshot (generated during execution)
```

---

## Workflow

1. **Input Credentials:**
   - The script prompts for a username and password.
   - Alternatively, you can uncomment the section to read usernames from a file.

2. **Access Web Page:**
   - The script uses Selenium to navigate to a login page (e.g., `login.html`).

3. **Fill Login Form:**
   - It finds the input fields for username and password and fills them.

4. **Capture CAPTCHA Screenshot:**
   - A specific region of the screen is captured using PyAutoGUI.
   - The screenshot is saved to a predefined directory.

5. **Extract CAPTCHA Text:**
   - The script opens Google Lens in Chrome to upload and extract text from the screenshot.
   - Extracted text is processed to remove spaces.

6. **Enter CAPTCHA and Submit:**
   - The extracted CAPTCHA text is entered into the web form.
   - The form is submitted using Selenium or PyAutoGUI.

---

## Key Features

- **CAPTCHA Handling:**
  - Captures CAPTCHA image and extracts text using Google Lens.
- **Browser Automation:**
  - Automates login and CAPTCHA submission using Selenium.
- **GUI Automation:**
  - Automates file uploads and other UI interactions using PyAutoGUI.

---

## Configuration

- Modify the `website_url` variable to point to the desired login page.
- Update the coordinates for:
  - Screenshot capture (`top_left_x`, `top_left_y`, `bottom_right_x`, `bottom_right_y`).
  - PyAutoGUI mouse actions.

---

## Execution

1. Place the `login.html` file in the appropriate location if using a local test page.
2. Run the script:
   ```bash
   python script.py
   ```
3. Follow the prompts to input credentials.

---

## Notes

- Ensure that the Chrome browser version matches the Chrome WebDriver version.
- If using different screen resolutions, adjust the coordinates accordingly.
- To use the script with a live website, replace the `website_url` variable with the actual URL.

---

## Known Limitations

- **Dynamic CAPTCHAs:**
  - The project works best for static CAPTCHAs.
  - Dynamic CAPTCHAs may require additional tools like OCR libraries (e.g., Tesseract).

- **Resolution Dependency:**
  - The script is resolution-dependent and requires manual adjustment of coordinates.

---

## Disclaimer

This project is for educational purposes only. Automating CAPTCHA solving may violate the terms of service of some websites. Use responsibly.
