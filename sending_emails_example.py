import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
type(conn)
#<class 'smtplib.SMTP'>
conn.ehlo()
#(250, b'smtp.gmail.com at your service, [112.201.52.19]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nSMTPUTF8')
conn.starttls()
#(220, b'2.0.0 Ready to start TLS')
conn.login('janoah.policarpio@gmail.com', 'udvforrbacskjatl')
#(235, b'2.7.0 Accepted')
#Note: ok, a word of advice here. Simply using your password here does not work. You need to setup 2-Step Authentication with your account first.
#Afterwards, you need to set an 'App Password'. More here: https://support.google.com/accounts/answer/185833?hl=en

conn.sendmail('janoah.policarpio@gmail.com', 'noah@policarpios.net', 'Subject: Python Test\n\nDear Noah,\nThis is Janoah, but I\'m not writing this email. This is the Python script doing the work for me. Mwahaha I am so lazy!\n\n-Janoah')
#{}
#Note: Text in the curly braces show messages that failed to send. This means this is successful.
conn.quit()
#(221, b'2.0.0 closing connection i18sm11438106pjx.33 - gsmtp')
