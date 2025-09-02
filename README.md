# AutoVAPT  
Automated Vulnerability Assessment and Penetration Testing using **OWASP ZAP**  

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)  
![License](https://img.shields.io/badge/License-MIT-green.svg)  
![Status](https://img.shields.io/badge/Status-Active-success.svg)  

AutoVAPT is a **Python-based tool** that automates the process of vulnerability assessment and penetration testing (VAPT) using the [OWASP ZAP](https://www.zaproxy.org/) API.  
It helps security researchers and developers identify potential vulnerabilities in web applications **quickly and efficiently**.  

---

##  Features
 Automated scanning with OWASP ZAP    
 Customizable scan scripts  
 Generates vulnerability reports (`vuln_report.txt`)  
 Easy to integrate into CI/CD pipelines  
 Lightweight and beginner-friendly  

---

##  Project Structure
AutoVAPT/
┣ scripts ← automation scripts (Python)
┣ vuln_report.txt ← vulnerability report
┣ README.md ← full project explanation
┣ requirements.txt ← Python dependencies

---

##  Installation

# Clone the repository
git clone https://github.com/kanika021105/AutoVAPT.git
cd AutoVAPT

# Install dependencies
pip install -r requirements.txt
# Usage
Run an automated scan with:
python scripts/scan.py --target http://example.com
Example: vuln_report.txt

# license
This project is licensed under the MIT License.

