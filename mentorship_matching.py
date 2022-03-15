from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from scipy.spatial import distance
from collections import defaultdict

global server

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']  # Google API

# The ID and range of a sample spreadsheet.
MENTEES_MENTORS_SPREADSHEET_ID = '1fyBv-RV4Cptn4Fue0qyUeVBWv3tf3Ow_5HUTGfi8mW8'

MENTORS_RANGE = "mentors_new!A3:BA45"
MENTEES_RANGE = "mentees_new!A3:AX89"
RESULTS_RANGE = "results!A1:AX50"


def main(MENTORS_RANGE, MENTEES_RANGE):

    creds = Credentials.from_authorized_user_file('sheet_token.json', SCOPES)
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()

    # collect dictionary with mentors items
    records_mentors = sheet.values().get(spreadsheetId=MENTEES_MENTORS_SPREADSHEET_ID,
                                         range=MENTORS_RANGE).execute()
    mentors = records_mentors.get('values', [])

    mentors_by_email = {}
    for mentor in mentors:
        if mentor[50] == "TRUE":
            mentors_by_email[mentor[1]] = mentor

    # collect dictionary with mentees items
    records_mentees = sheet.values().get(spreadsheetId=MENTEES_MENTORS_SPREADSHEET_ID, range=MENTEES_RANGE).execute()
    mentees = records_mentees.get('values', [])

    mentees_by_email = {}
    for mentee in mentees:
        if mentee[49] == "TRUE":
            mentees_by_email[mentee[1]] = mentee

    full_result = []

    COUNT = 0
    pairs_with_distance = defaultdict(__builtins__.list)

    # collect all properties about language, other preferences in one list - mentors_list_properties
    for mentor in mentors_by_email:
        result = {}
        mentors_list_properties = []
        i = 6
        while i <= 41:
            value = mentors_by_email[mentor][i]
            if value == "":
                value = "0"
                mentors_list_properties.append(value)
            else:
                mentors_list_properties.append(value)
            i += 1
        for i in range(0, len(mentors_list_properties)):
            mentors_list_properties[i] = int(mentors_list_properties[i])
        list_mentee_value = []
        count = 1 + COUNT
        print(COUNT)
        for mentee in mentees_by_email:
            mentees_properties = []
            i = 7
            while i <= 42:
                value = mentees_by_email[mentee][i]
                if value == "":
                    value = "0"
                    mentees_properties.append(value)
                else:
                    mentees_properties.append(value)
                i += 1
            if result.get(mentor) == None:
                result[mentor] = []
            for i in range(0, len(mentees_properties)):
                mentees_properties[i] = int(mentees_properties[i])
            # implementation of the algorithm
            dist = round(distance.euclidean(mentors_list_properties, mentees_properties), 1)
            list_mentee_value.append([dist, mentee])
            pairs_with_distance[dist].append((mentor, mentee))
            count += 1
        list_mentee_value.sort()
        result[mentor] = list_mentee_value
        full_result.append(result)
        COUNT += count
    pairs_with_distance = sorted(pairs_with_distance.items(), key=lambda kv: kv[0])
    return full_result, pairs_with_distance


if __name__ == '__main__':
    result, pairs_with_distance = main(MENTORS_RANGE, MENTEES_RANGE)
    for i in result:
        print("Separate results")
        print("")
        print(i)
        print("")

    print('Pairs with distance specified')
    print(pairs_with_distance)


def main_func(request):
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        result, pairs_with_distance = main(MENTORS_RANGE, MENTEES_RANGE)
        for i in result:
            print("Separate result")
            print("")
            print(i)
            print("")

        print('Ordered list with mentors-mentees pairs')
        print(pairs_with_distance)