# Web Application Security Portable Checker

## Overview

This Python script performs basic security checks on a web application URL, focusing on identifying Cross-Site Scripting (XSS) and SQL Injection vulnerabilities.

## Requirements

- Python 3.x
- Required Python packages can be installed using `requests==2.26.0t` and `beautifulsoup4==4.10.0` at requirements.txt

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/HowAreYouChristian/web-security-tool.git
    cd web-security-tool
    ```

2. Install required dependencies:

    ```bash
    pip3 install -r requirements.txt
    ```

## Usage

1. Run the script:

    ```bash
    python3 sec_check.py
    ```

2. Enter the web application URL when prompted.

3. The script will perform checks for XSS and SQL Injection vulnerabilities and provide clear output indicating the presence or absence of vulnerabilities.

## Example

```bash
Enter the web application URL: https://target.com

Checking for XSS vulnerabilities...
No XSS Vulnerability was found.

Checking for SQL Injection vulnerabilities...
No SQL Injection Vulnerability was found.
