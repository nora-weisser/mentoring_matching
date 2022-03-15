# Mentorship program 

<p>These scripts were developed to manage mentor-mentee matching automatically using the following approach: N-dimentional minimum  Euclidean distance.</p>
<p>Tech stack: Python, Google Cloud, Google Docs API, Google functions, CRON jobs</p>

**Task:**
*Input data*: two tables ith information about  mentees and mentors. Tables format - excel table in Google Docs

<p> <b>Table 1. Fields name and format of the record  for participants-mentees</b> </p>

| Column number | Name of the column      | Format           | Example            |
| ------------- | ----------------------- | ---------------- | ------------------ |
| A             | Timestamp               | timestamp format | 9/30/2021 20:35:52 |
| B             | Email address           | text             | test@gmail.com     |
| C          | What is your full name? | text             | Nora Belova        |
| **D-G**       | **Some Personal info**                                          |**text**|**-**|
| **H-Y**       | **Choose skills you want to improve. Mark your preference from 1 to 5** |**Number from 1 to 5**|**1**|
| H | QA |                  |                    |
| I | Backend Developer |                  |                    |
| J | Frontend Developer |                  |                    |
| K | Fullstack Developer |                  |                    |
| L | DevOps |                  |                    |
| M | Distributed Systems |                  |                    |
| N | Data Science |                  |                    |
| O | Data Engineering |                  |                    |
| P | Android |                  |                    |
| Q | iOS |                  |                    |
| R | Business Analysis |                  |                    |
| S | Product Management |                  |                    |
| T | Project Management |                  |                    |
| U | Machine Learning |                  |                    |
| V | Engineering management |                  |                    |
| W | Network Engineering |                  |                    |
| X | Security |                  |                    |
| Y | Site Reliability Engineering |                  |                    |
| **Z-AE** | **Please, indicate your preference to achieve the following goals (1 - lowest, 5 - highest)** | **Number from 1 to 5** | **1** |
| Z | switch career to IT |                  |                    |
| AA | grow from beginner to mid-level |                  |                    |
| AB | grow from mid-level to senior-level |                  |                    |
| AC | grow beyond senior level |                  |                    |
| AD | switch from IC to management position |                  |                    |
| AE | change specialisation within IT |                  |                    |
| **AF-AQ** | **Choose programming languages you want to improve. Mark your preference from 1 to 5 (1 - lowest, 5 - highest)** | **Number from 1 to 5** | **1** |
| AF | Java |                  |                    |
| AG | C |                  |                    |
| AH | C++ |                  |                    |
| AI | C# |                  |                    |
| AJ | Go |                  |                    |
| AK | Python |                  |                    |
| AL | JavaScript |                  |                    |
| AM | Kotlin |                  |                    |
| AN | Scala |                  |                    |
| AO | Swift |                  |                    |
| AP | Ruby |                  |                    |
| AQ | Rust |                  |                    |
| AR | Please describe how much experience you have in the area you would like to be mentored in. If you are studying, tell us about your accomplished courses, projects, achievements, or interests. | plain text |                    |
| AS | On average, what time commitment would you be looking for from your mentor? | 1, 2, 3, 4, 5 or more |                    |
| AT | Would you agree to be a part of a study group? | Yes/No |                    |
| AU | Would you agree to be mentored by a male mentor? | Yes/No ||
| AV | Anything else you would like us to know? | Plain text |                    |
| AW            | I hereby grant Women Who Code London the right to store the mentioned above contact details in order to contact me regarding mentorship opportunities |                  | I confirm this |

<p><b>Table 2. Fields name and format of the record  for participants-mentors</b></p>

| Column number | Name of the column      | Format           | Example            |
| ------------- | ----------------------- | ---------------- | ------------------ |
| A             | Timestamp               | timestamp format | 9/30/2021 20:35:52 |
| B             | Email address           | text             | test@gmail.com     |
| C          | What is your full name? | text             | Nora Belova        |
| **D-F**      | **Some Personal info**                                          |**text**|**-**|
| **G-Y**      | **Choose skills you can help your mentee with. Mark your preference from 1 to 5 (1 - lowest, 5 - highest)** |**Number from 1 to 5**|**1**|
| G | QA |                  |                    |
| H | Backend Developer |                  |                    |
| I | Frontend Developer |                  |                    |
| J | Fullstack Developer |                  |                    |
| K | DevOps |                  |                    |
| L | Distributed Systems |                  |                    |
| M | Data Science |                  |                    |
| N | Data Engineering |                  |                    |
| O | Android |                  |                    |
| P | iOS |                  |                    |
| Q | Business Analysis |                  |                    |
| R | Product Management |                  |                    |
| S | Project Management |                  |                    |
| T | Machine Learning |                  |                    |
| U | Engineering management |                  |                    |
| V | Network Engineering |                  |                    |
| W | Security |                  |                    |
| X | Site Reliability Engineering |                  |                    |
| **Y-AD** | **Please, indicate your preference in helping your mentee to achieve the following goals (1 - lowest, 5 - highest)** | **Number from 1 to 5** | **1** |
| Y | switch career to IT |                  |                    |
| Z | grow from beginner to mid-level |                  |                    |
| AA | grow from mid-level to senior-level |                  |                    |
| AB | grow beyond senior level |                  |                    |
| AC | switch from IC to management position |                  |                    |
| AD | change specialisation within IT |                  |                    |
| **AE-AP** | **Chose programming languages you can help your mentee with. Mark your preference from 1 to 5 (1 - lowest, 5 - highest)** | **Number from 1 to 5** | **1** |
| AE | Java |                  |                    |
| AF | C |                  |                    |
| AG | C++ |                  |                    |
| AH | C# |                  |                    |
| AI | Go |                  |                    |
| AJ | Python |                  |                    |
| AK | JavaScript |                  |                    |
| AL | Kotlin |                  |                    |
| AM | Scala |                  |                    |
| AN | Swift |                  |                    |
| AO | Ruby |                  |                    |
| AP | Rust |                  |                    |
| AQ | If there anything else you would like to help your mentee with? | plain text |                    |
| AR | Tell us a little about your expertise. Feel free to add anything relevant: years of experience, achievements, successful projects etc. | plain text |                    |
| AS | How many hours per week would you be able to dedicate to mentoring? (on average) | 1, 2, 3, 4, 5 or more |                    |
| AT | Could you mentor more than 1 mentee, assuming the total hours spent does not exceed your answer above? | Yes/No ||
| AU | Could you organise a study group, assuming the total hours spent does not exceed the value you committed to. | Yes/No |                    |
| AV           | Do you identify as a woman or non-binary? |Yes/No||
| AV           | Anything else you would like us to know? |plain text||
| AV           | I hereby grant Women Who Code London the right to store the mentioned above contact details in order to contact me regarding mentorship opportunities |I confirm this||

What needs to  be implemented:
1. Matching/creating mentor-mentee pairs based on the info provided by participants

<h3>Implement mentor-mentee matching based on providing information in the table format</h3>
For matching mentor-mentee we need to find nearest neighbours. For implementing it I used N-dimentional minimum  Euclidean distance. 
Python suggests to use **scipy.spatial.distance.euclidean(u, v, w=None)** function, where:

**Parameters**
- u(N,) array_like
Input array.

- v(N,) array_like
Input array.

- w(N,) array_like, optional
The weights for each value in u and v. Default is None, which gives each value a weight of 1.0

**Returns**
euclidean: double
The Euclidean distance between vectors u and v.

In our case v and w are arrays with characteristics for mentee (H-AQ) and mentor(G-AP)

**Result is returned in two formats:**
1. {mentor1: [[distance1, mentee1], [distance2, mentee2]], mentor2: [[distance3, mentee3], [distance4, mentee4]]} - it is sorted by ascending distance
2. [(distance1, [(mentor1, mentee1), (mentor2, mentee2)]), distance2, [(mentor3, mentee3), (mentor4, mentee4)]...] - it is sorted by ascending distance