# (WEB Version) Automation to Send Curriculum for WEB 

##### Hours : 16

<img src="./assets/icon.ico" align="right">

## 1. Introduction  

This project automates sending job application emails, including personalized content and attachments, using Microsoft Edge and Outlook. It processes data from a CSV file in the `imports` directory, sends emails, and updates the CSV after successful email delivery.

## 2. Technologies Used 📲  

![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-Browser%20Automation-43B02A?logo=selenium&logoColor=white)
![Webdriver Manager](https://img.shields.io/badge/Webdriver%20Manager-Browser%20Drivers-F8C471?logo=selenium&logoColor=black)
![Excel](https://img.shields.io/badge/Excel-Spreadsheet-217346?logo=microsoft-excel&logoColor=white)
![CSV](https://img.shields.io/badge/CSV-Comma%20Separated%20Values-FF8800)
![Outlook](https://img.shields.io/badge/Outlook-Email-0078D4?logo=microsoft-outlook&logoColor=white)
![Edge](https://img.shields.io/badge/Edge-Browser-0078D7?logo=microsoft-edge&logoColor=white)

## 3. Installation 🛠️  

### Steps to install:  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/JoaoG23/automation-to-send-curriculum.git  
   ```  
2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  
3. Create a `.env` file with the following content:  
   ```env  
   PATH_WHERE_RESUMES="C:\\Users\\joaog\\Desktop\\web\\resumes"  
   NAME_CANDIDATE="João Guilherme"  
   EDGE_USER_PROFILE="C:\\Users\\joaog\\AppData\\Local\\Microsoft\\Edge\\User Data\\Profile 2"  
   ```  

## 4. Features ✔️  

- [x] Validate emails already sent.
- [x] Open Edge and log in to Microsoft account.
- [x] Compose and send emails:  
    - [x] Add recipient's email.  
    - [x] Write a subject and message.  
    - [x] Attach the correct resume from the specified directory.  
- [x] Update the CSV with the sent status.  

## 5. Directory Structure 📂  

    automation-to-send-curriculum/web  
    ├── exported/  
    ├── imports/  
    ├── logs/  
    ├── resumes/  
    ├── send_emails/  
    ├── templates/  
    ├── utils/  
    ├── __init__.py  
    ├── .env  
    ├── README.md  
    ├── requirements.txt  

## 6. How to Use 👨‍💻  

1. Place your CSV in the `imports/` directory named `jobs.csv`, following the format in `model_csv_jobs.csv`.  
2. Place resumes in the specified directory in the `.env` file.  
3. Run the script:  
   ```bash  
   python __init__.py 
   ```  
4. Post-execution:  
   - Emails will be sent.  
   - CSV will be updated with the sent status.  

## 7. Requirements  

- Ensure Edge browser is installed.  
- Pre-login to Microsoft account.  

## 8. Benefits and Limitations 🛠️  

### Benefits:  
- Automates the process of sending multiple emails.  
- Allows multitasking while automation runs.  

### Limitations:  
- Requires a stable internet connection.  
- Must log in to Microsoft account beforehand.  
- Only compatible with Edge due to security restrictions.  

**Note:**  
Microsoft’s security features may add random elements to the process, and their anti-bot systems can introduce challenges.

## 9. Author  

 <img style="border-radius:50%;" src="https://avatars.githubusercontent.com/u/80895578?v=4" width="100px;" alt=""/>  
 <br />  
 <sub><b>Joao Guilherme</b></sub></a> <a href="https://github.com/JoaoG23/">🚀</a>  

Developed with 🤖 by Joao Guilherme 👋🏽 Contact me via:  

[![Linkedin Badge](https://shields.io/badge/-Joao%20Guilherme-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/joaog123/)](https://www.linkedin.com/in/joaog123/)  
[![Email Badge](https://shields.io/badge/-joaoguilherme94@live.com-c80?style=flat-square&logo=Microsoft&logoColor=white&link=mailto:joaoguilherme94@live.com)](mailto:joaoguilherme94@live.com)  

## 10. License 📄  

[![License](https://shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)  