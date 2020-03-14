# BINDB
# Requirements

* Python (3.5, 3.6, 3.7, 3.8)
* Django (1.11, 2.0, 2.1, 2.2, 3.0)


# Installation

Install using `pip`...

    pip install -r requirements.txt

# Usage 

For running Django server ...

    python manage.py runsever 

For checking whether a file is already in the database ...

    python test.py 

For exporting the data as CSV file ...

    http://127.0.0.1:8000/api/export/malware_data
    http://127.0.0.1:8000/api/export/benign_data
    
Rename .env.example to .env and add the Virus Total API to it.


# ISSUES

Public API Key of VirusTotal provides only 4 requests per minute and 1000 requests per day. Contact VirusTotal for increased requests limits (https://www.virustotal.com/gui/contact-us).  

