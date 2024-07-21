from googleapiclient.discovery import build
from google.oauth2 import service_account


SERVICE_ACCOUNT_FILE = 'serviceAccountKeys.json'
# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1putMoiGvkrNfLVd7WHvPRBFiWUqPSnLrBwF6Ijg_m-U"


def read_sheet(sheet):

    result = (
        sheet.values()
            .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheet1!A1")
            .execute()
    )
    values = result.get("values", [])
    print(values)

    if not values:
        print("No data found.")
        return

    print("Name, Major:")
    for row in values:
        # Print columns A and E, which correspond to indices 0 and 4.
        print(f"{row[0]}, {row[4]}")

    return values


def write_to_sheet(sheet):

    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range="Sheet2!A1",
                                    valueInputOption="USER_ENTERED",
                                    body={"values": imported_data}).execute()


def main(imported_data):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()

    values = read_sheet(sheet)
    write_to_sheet(sheet)


if __name__ == "__main__":
    imported_data = [['A', 'B', 'C'][1, 2, 3][4, 5, 6]]
    main(imported_data)
