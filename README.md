## Salesforce-Python-Extract-Data


 Python using `simple_salesforce` package is an easy solution we found which allows users to download Salesforce **reports directly into Python** by making use of the ‘Salesforce’ function to log in programmatically and then using a GET function to retrieve the report.

1. Your Salesforce Username and Password

       These are the regular account details you use to log into Salesforce.
       You will need to provide in a credentials.json a e-mail, password and security token.
2. Your Salesforce Security token
 
       This can be found by logging into your Salesforce account and going to 
       Settings > My Personal Information > Reset My Security Token. 
       After following the instructions you should receive an email with your security token.

3. Your Salesforce Domain

       This can be found at the start of the URL in your Salesforce instance, e.g. for example
       “https://yourcompany.my.salesforce.com/00O0X0000Aa4GO1” it is “https://yourcompany.my.salesforce.com/”.

4. Your Salesforce Report ID

       This can be found by opening the report in Salesforce you wish to download and checking the URL.
       The report ID is the 15-18 character string near the end of the URL, e.g. for
       “https://yourcompany.my.salesforce.com/00O0X0000Aa4GO1” it is “00O0X0000Aa4GO1”.

