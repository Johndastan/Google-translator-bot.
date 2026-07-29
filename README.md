# VTT Subtitle Translator with Selenium

A Python automation project that translates `.vtt` subtitle files from Spanish to English using Selenium and Google Translate.

## Features

- Reads subtitle files recursively from the `captions` folder.
- Opens Google Translate automatically.
- Translates only subtitle text.
- Preserves timestamps.
- Saves translated subtitles into the `translations` folder.

## Technologies

- Python 3.13
- Selenium
- ChromeDriver
- Google Translate

## Project Structure

```
files/
│
├── captions/
│   └── video1.vtt
│
└── translations/
```

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/vtt-translator.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Download the correct version of:

- Google Chrome
- ChromeDriver

Update these paths inside the script:

```python
options.binary_location = "C:\\SeleniumDrivers\\chrome-win64\\chrome.exe"

service = Service(
    "C:\\SeleniumDrivers\\chromedriver-win64\\chromedriver.exe"
)
```

Run

```bash
python traductor.py
```

## Improvements

- Explicit waits with Selenium
- Compatible with modern Selenium versions
- Folder recursion
- Automatic translation output

## Challenges Solved

- Updated deprecated Selenium code.
- Replaced static waits with explicit waits.
- Fixed file handling issues.
- Improved compatibility with current Python versions.
