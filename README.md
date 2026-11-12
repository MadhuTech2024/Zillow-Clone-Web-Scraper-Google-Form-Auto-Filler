# 🏡 Zillow Property Web Scraper & Google Form Automation

<p align="center">
  <strong>An automated Python-based data collection and entry system that extracts rental property listings from a Zillow Clone website and submits them to Google Forms using Selenium.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" />
  <img src="https://img.shields.io/badge/BeautifulSoup-Web%20Scraping-green" />
  <img src="https://img.shields.io/badge/Requests-HTTP-orange" />
  <img src="https://img.shields.io/badge/Selenium-Browser%20Automation-brightgreen?logo=selenium" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

---

## 📌 Overview

The **Zillow Property Web Scraper & Google Form Automation** project is a Python-based automation solution designed to simplify rental property data collection and eliminate repetitive manual data entry.

The application extracts property information from a Zillow Clone website, including property addresses, monthly rental prices, and listing URLs. It then uses Selenium WebDriver to automatically enter the collected information into a customized Google Form.

The submitted Google Form responses can be stored and organized in Google Sheets, creating a structured dataset of rental property listings.

This project demonstrates the practical application of Python, web scraping, browser automation, and workflow automation to solve a real-world data collection problem.

## 🎯 Objectives

- Automate rental property data collection.
- Extract structured information from web pages.
- Reduce repetitive manual data entry.
- Automate Google Form submissions using Selenium.
- Organize collected property information in Google Sheets.
- Understand the integration of web scraping and browser automation.

## ✨ Key Features

### 🔍 1. Automated Web Scraping
- Retrieves rental property listings from a Zillow Clone website.
- Uses HTTP requests to retrieve webpage content.
- Parses HTML using BeautifulSoup.

### 🏠 2. Property Information Extraction
Automatically extracts three important property details:

- **Property Address:** Location of the rental property.
- **Monthly Rent:** Rental price of the property.
- **Property URL:** Direct link to the property listing.

### 🤖 3. Google Form Automation
- Opens Google Forms using Selenium WebDriver.
- Automatically fills in the property details.
- Submits individual property records.
- Uses explicit waits to allow form fields to load before interaction.

### 📊 4. Google Sheets Integration
- Google Forms can automatically save submitted responses to Google Sheets.
- Creates an organized dataset of rental property information.
- Simplifies property data tracking and management.

### ⚡ 5. Automated Workflow
Combines web scraping and browser automation into a single Python script, reducing manual intervention.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Requests | Sending HTTP requests |
| BeautifulSoup4 | HTML parsing and data extraction |
| Selenium | Browser automation |
| Chrome WebDriver | Automating Google Form interactions |
| Google Forms | Collecting property information |
| Google Sheets | Organizing submitted responses |

## 🏗️ Project Architecture

```text
Zillow-Clone-Web-Scraper-Google-Form-Auto-Filler/
│
├── main.py          # Main automation script
│
├── LICENSE          # MIT License
│
└── README.md        # Project documentation
```

## 🔄 Application Workflow

```text
      Zillow Clone Website
                |
                v
        Python Requests
                |
                v
       BeautifulSoup Parser
                |
                v
       Extract Property Data
                |
         +------+------+
         |      |      |
         v      v      v
      Address Price  Listing URL
         |      |      |
         +------+------+
                |
                v
        Selenium WebDriver
                |
                v
          Google Form
                |
                v
       Automatic Submission
                |
                v
         Google Sheets
                |
                v
       Structured Property Data
```

## ⚙️ Installation and Setup

Follow these steps to run the project on your local machine.

### Prerequisites

Make sure you have installed:

- Python 3.x
- Google Chrome
- ChromeDriver compatible with your Chrome installation, if required by your Selenium setup
- Visual Studio Code (recommended)
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/MadhuTech2024/Zillow-Clone-Web-Scraper-Google-Form-Auto-Filler.git
```

### Step 2: Navigate to the Project Folder

```bash
cd Zillow-Clone-Web-Scraper-Google-Form-Auto-Filler
```

### Step 3: Install Required Libraries

```bash
pip install beautifulsoup4==4.12.2 requests==2.31.0 selenium==4.15.1
```

### Step 4: Configure Your Google Form

1. Create a Google Form with three short-answer questions:
   - Property Address
   - Monthly Rent
   - Property URL
2. Copy your Google Form URL.
3. Open `main.py`.
4. Find the following configuration:

```python
FORM_URL = "YOUR_GOOGLE_FORM_LINK_HERE"
```

5. Replace the placeholder with your Google Form URL.

**Important:** Ensure that the order of the questions in your Google Form matches the order of the fields filled by the Python script.

### Step 5: Run the Application

```bash
python main.py
```

## 💻 Execution Process

When you execute the application:

1. Python sends an HTTP request to the Zillow Clone website.
2. BeautifulSoup parses the returned HTML content.
3. Property addresses, prices, and listing URLs are extracted.
4. Selenium launches the Chrome browser.
5. The application opens the configured Google Form.
6. Property information is entered automatically.
7. The form is submitted for each property listing.
8. The application displays submission progress in the terminal.

**Sample terminal output:**

```text
✅ Scraping complete!
Found [number] listings

✅ Submitted form for listing 1/[number]
✅ Submitted form for listing 2/[number]

🎉 All listings processed!
```

*The listing count and submission messages depend on the website's available data and successful form submissions.*

## 📚 Concepts Demonstrated

This project provides practical experience with:

- Python programming and automation.
- HTTP requests and webpage retrieval.
- HTML parsing using BeautifulSoup.
- CSS selectors for extracting webpage elements.
- Web scraping techniques.
- Selenium WebDriver automation.
- Explicit waits and browser interactions.
- Automated form submission.
- Data collection and organization.

## 🔮 Future Enhancements

Some potential improvements include:

- Exporting scraped property information directly to CSV and Excel.
- Adding duplicate property detection.
- Implementing more comprehensive exception handling.
- Adding logging for successful and failed submissions.
- Supporting multiple property listing websites.
- Developing a dashboard to visualize rental property data.
- Adding configurable scraping and submission settings.
- Improving browser automation reliability.

## ⚠️ Important Notes

- Update the Google Form URL before running the application.
- Ensure that the form contains the expected three input fields.
- Website HTML structures and CSS selectors may change over time.
- Selenium requires a compatible browser setup.
- Use web scraping responsibly and respect the website's terms of service, robots.txt guidance, and applicable usage restrictions.
- Only submit data to Google Forms that you own or are authorized to use.

## 👨‍💻 Author

**Madhu Karrolla**

Python Developer | Full Stack Developer | Automation Enthusiast

- **GitHub:** [MadhuTech2024](https://github.com/MadhuTech2024)
- **LinkedIn:** [K. Madhu](https://www.linkedin.com/in/karrolla-madhu-211814363/)

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

<p align="center">
  <strong>Automating repetitive tasks, one Python script at a time! 🚀</strong>
</p>
