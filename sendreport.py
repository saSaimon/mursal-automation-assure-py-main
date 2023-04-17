import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import datetime
import os

smtp_server = "smtp-relay.sendinblue.com"
port = 587  # For starttls
sender_email = "kashif@diyainteractive.com"
password = 'hWIt1qpEUT542PVy'
config = json.loads(open(os.path.join('tests', 'config.json'), 'r').read())

try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls() #enable security
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    message = MIMEMultipart("alternative")
    message["Subject"] = "test report"
    message["From"] = "automation@instacate.com"
    message["To"] = config['testReportEmail']
    html = """\
    <html>
    <body>
        <table border='1|1'><thead>
            <th>Time</th>
            <th>Description</th>
            <th>Status</th>
        </thead>

    """
    save_file_name = "report" + config['outputFileType']
    file_name = os.path.join(config['outputFolder'], save_file_name)
    file1 = open(file_name, 'r')
    Lines = file1.readlines()
    # Strips the newline character
    for line in Lines:
        if line == '\n':
            continue
        else:
            line = line.rstrip('\n')
            line = line.split(',')
            html += "<tr>"
            for i in line:
                html += "<td>" + i + "</td>"
            html += "</tr>"
    html += "</table></body></html>"
    part1 = MIMEText(html, "html")
    message.attach(part1)
    text = message.as_string()

    #     col = line.split(", ")
    #     html+=f""" <tr>
    #         <td>{col[0]}</td>
    #         <td>{col[1]}</td>
    #         <td>{col[2]}</td>
    #         </tr>"""
    # html = html + """
    # </table>
    # </body>
    # </html>
    # """
    # part2 = MIMEText(html, "html")
    # message.attach(part2)
    server.sendmail(sender_email, config['testReportEmail'], message.as_string())
    
except Exception as e:
    # Print any error messages to stdout
    print(e)
    server.quit() 
finally:
    server.quit()