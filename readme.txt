### GoogSheetsReadWrite###

GoogleSheetsReadWrite.py connects to service account, https://console.cloud.google.com/iam-admin/serviceaccounts/details/112483177185045684832?project=bark-leads
(handofthegreen@bark-leads.iam.gserviceaccount.com) for the project Barks Leads which is using the Google Sheets API.  (See https://www.youtube.com/watch?v=4ssigWmExak)
Requires access to 'serviceAccountKeys.json' downloaded to the repo

See https://docs.google.com/document/d/1XZrYDRF_T5nSk5xDrCzUtql4qKF8PnnkgMW19kS4SmA/edit for details setting up Google Sheets service account and API

## Requirements ##

- Python 3.x
- Python modules
	pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
- Python libraries
	from googleapiclient.discovery import build
	from google.oauth2 import service_account


## Run Instructions ##

1) From Google sheets get the spreadsheet id (Share > Copy link for URL).
2) Add id to GoogleSheetsReadWrite.py variable SAMPLE_SPREADSHEET_ID (line16)
3) Under def read_sheet(), add the spreadsheet range to be read e.g. "Sheet1!A1:
4) Under def write_to_sheet, add range to write too e.g. "Sheet2!A1"
5) Run GoogleSheetsReadWrite.py