# GMail Automation

**Introduction**

This is an email scheduler app. For example, you can configure the app to send emails to your friends on their birthdays.

**Requirement**

Linux, Python >=2.7 and pip

**Steps:**
1. Setup gmail api [here](https://console.developers.google.com/ "Google Api")
2. Download clientid.json file.
3. Usage:
```sh
python api_gmail.py *email_to* *subject* *msg_file*
```
4. In the terminal, type
```
crontab -e
```
 select appropriate editor (vim or nano).

 5. Now you can schedule your email
 ```minute hour dayOfMonth month dayOfWeek command```
 Eg
  ```sh
  0 0 1 1 * python api_gmail.py receiver@gmail.com "Subject" msgFile.txt
  ```
  this will send email on 1st of January at 12 AM.
