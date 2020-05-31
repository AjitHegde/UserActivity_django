User Activity Service

Features
* RESt API to get Users along with their activities


Setup Instructions

* Windows Environment
    * Install python3
    * Install python3-pip
    * Install django using pip (pip3 install django)
    * Install dependencies using (pip3 install -r requirements.txt)
    * Populate db with dummy data using command (python3 manage.py migrate)
    * Start server using (python3 manage.py runserver)

* Linux Environment (Ubuntu 18 scripts)
    * Execute sh setup.sh script to install all requirements ( sudo permission is required)
    * Start Server by executing sh start.sh

    Note: In case the script fails... then the steps for windows are valid for linux also...


Once the server is running use any Rest Client such as Postman or WClient to hit the API and get response

API Details

URL : http://localhost:8000/users/
METHOD: GET
RESPONSE:
{
    "ok": true,
    "members": [
        {
            "id": "DJ001",
            "real_name": "Ramesh Hegde",
            "tz": "Asia/Kolkatta",
            "activity_periods": [
                {
                    "start_time": "May 31 2020 10:00AM",
                    "end_time": "May 31 2020 11:00AM"
                },
                {
                    "start_time": "May 31 2020 11:30AM",
                    "end_time": "May 31 2020 12:15PM"
                },
                {
                    "start_time": "May 31 2020 12:30PM",
                    "end_time": "May 31 2020 01:00AM"
                }
            ]
        },
        {
            "id": "DJ002",
            "real_name": "Dinesh Hegde",
            "tz": "America/Los Angeles",
            "activity_periods": [
                {
                    "start_time": "May 31 2020 10:00AM",
                    "end_time": "May 31 2020 11:00AM"
                },
                {
                    "start_time": "May 31 2020 11:30AM",
                    "end_time": "May 31 2020 12:15PM"
                }
            ]
        }
    ]
}
