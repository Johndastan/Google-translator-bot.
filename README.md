# Google Subtitle Translator Automation

A Python automation tool that translates .vtt subtitle files using Selenium WebDriver and Google Translate.

The project automates the translation workflow by reading subtitle files, identifying translatable content, preserving timestamps, and generating translated subtitle files while maintaining the original structure.

Project Overview

Manually translating subtitle files can be a repetitive and time-consuming task. This project was created to automate that process by interacting with Google Translate through Selenium WebDriver.

The script processes subtitle files, sends text automatically to the translation service, retrieves the translated content, and saves the result into a separate output directory.

Features
Automatic detection and processing of .vtt subtitle files.
Support for processing multiple subtitle files inside a directory.
Recursive file search inside the captions folder.
Timestamp detection using Regular Expressions (Regex).
Preservation of subtitle timing information.
Automatic skipping of empty lines and non-translatable elements.
Browser automation using Selenium WebDriver.
Dynamic element synchronization using WebDriverWait.
Automatic extraction of translated text.
Error handling during translation processing.
Progressive saving to reduce data loss during long translations.
Generation of translated subtitle files in a separate directory.
Technologies Used
Python 3
Selenium WebDriver
Google Chrome
ChromeDriver
Regular Expressions (Regex)
File System Management with Python os module
How It Works

The automation workflow follows these steps:

Subtitle files are placed inside the files/captions directory.
The program scans the directory and identifies available subtitle files.
Each .vtt file is opened and read line by line.
Regex is used to identify timestamp lines.
Timestamp lines are preserved without modification.
Text lines are sent automatically to Google Translate.
Selenium waits dynamically until the translation is available.
The translated text replaces the original subtitle content.
The translated file is saved inside the files/translations directory.
Example
Original Subtitle
00:01.300 --> 00:05.620
Vamos a continuar con la instalación de nuestro ambiente de desarrollo.
Translated Subtitle
00:01.300 --> 00:05.620
We are going to continue with the installation of our development environment.
Project Structure
Google-Subtitle-Translator/
│
├── files/
│   ├── captions/
│   │   └── video1.vtt
│   │
│   └── translations/
│       └── video1.vtt
│
├── traductor.py
│
└── README.md
Installation
Requirements
Python 3.x
Google Chrome
ChromeDriver compatible with your Chrome version

Install Selenium:

pip install selenium
Configuration

Update the Chrome and ChromeDriver paths inside the script:

options.binary_location = "YOUR_CHROME_PATH"

service = Service("YOUR_CHROMEDRIVER_PATH")

Example:

options.binary_location = "C:\\SeleniumDrivers\\chrome-win64\\chrome.exe"

service = Service("C:\\SeleniumDrivers\\chromedriver-win64\\chromedriver.exe")
Running the Project
Add your .vtt subtitle files into:
files/captions
Run the script:
python traductor.py
The translated files will be generated in:
files/translations
Improvements Implemented
Previous Version
Used fixed waiting times with time.sleep().
Depended on predefined delays.
Could fail when Google Translate responded slower than expected.
Current Version
Removed static waits.
Implemented Selenium explicit waits using WebDriverWait.
Improved execution speed.
Increased automation stability.
Added exception handling.
Improved subtitle processing logic.
Added progressive saving support.
Current Limitations
The automation depends on Google Translate's web interface.
Changes in Google Translate HTML structure may require selector updates.
Translation speed depends on browser and network response time.
It does not use an official translation API.
Future Improvements
Add support for selecting source and target languages.
Create a graphical user interface (GUI).
Add detailed execution logs.
Support batch translation with multiple files.
Implement automated tests for subtitle processing.
Integrate an official translation API.
Improve error recovery and retry mechanisms.
screenshot/https://github.com/Johndastan/Google-translator-bot./blob/main/imagen_2026-07-29_032321714.png
Author

Jonathan Castañeda
