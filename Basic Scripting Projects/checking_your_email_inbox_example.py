import pyzmail
#pip  install pyzmail36
import imapclient
#pip install imapclient

conn = imapclient.IMAPClient('imap.gmail.com', ssl = True)
conn.login('janoah.policarpio@gmail.com', 'udvforrbacskjatl')
#b'janoah.policarpio@gmail.com authenticated (Success)'
conn.select_folder('INBOX', readonly=True)
#{b'PERMANENTFLAGS': (), b'FLAGS': (b'\\Answered', b'\\Flagged', b'\\Draft', b'\\Deleted', b'\\Seen', b'$NotPhishing', b'$Phishing'), b'UIDVALIDITY': 1, b'EXISTS': 39221, b'RECENT': 0, b'UIDNEXT': 39802, b'HIGHESTMODSEQ': 9231938, b'READ-ONLY': [b'']}

UIDs = conn.search(['ON','20-Apr-2020'])   #there are different search keys, such as BEFORE, ON, and SINCE. ALL returns all messages. You can also do 'SUBJECT string', 'BODY string', 'TEXT string'.
UIDs
#[39794, 39795, 39796, 39797, 39798, 39799, 39800, 39801, 39802]
conn.fetch([39802], ['BODY[]', 'FLAGS'])
"""defaultdict(<class 'dict'>, {39802: {b'SEQ': 39222, b'FLAGS': (b'\\Seen',),
b'BODY[]': b'MIME-Version: 1.0\r\nDate: Mon, 20 Apr 2020 13:46:29 +0800\r\n
References: <5e9c7880.1c69fb81.9a039.77f7@mx.google.com>\r\nIn-Reply-To:
<5e9c7880.1c69fb81.9a039.77f7@mx.google.com>\r\nMessage-ID: <CAC3+4hgwc_FyLPE
HXqEt2UkdYM=t6aNiX721XwMEqAkocjooQw@mail.gmail.com>\r\n
Subject: Re: Python Test\r\nFrom: Charles Janoah Policarpio <janoah.policarpio@gmail.com>
\r\nTo: Charles Janoah Policarpio <janoah.policarpio@gmail.com>\r\nContent-Type:
multipart/alternative; boundary="000000000000b6d48205a3b26b4a"\r\nX-Antivirus: Avast
(VPS 200419-0, 19/04/2020), Inbound message\r\nX-Antivirus-Status: Clean\r\n\r\n--
000000000000b6d48205a3b26b4a\r\nContent-Type: text/plain;
charset="UTF-8"\r\n\r\nDear Jaoah,\r\nThis is Janoah. I am now writing this email as
a person.\r\n\r\n-Janoah\r\n\r\nOn Mon, Apr 20, 2020 at 12:12 AM <janoah.policarpio@gmail.com>
wrote:\r\n\r\n> Dear Noah,\r\n> This is Janoah, but I\'m not writing this email. This is the
Python script\r\n> doing the work for me. Mwahaha I am so lazy!\r\n>\r\n> -Janoah\r\n>\r\n\r\n
--000000000000b6d48205a3b26b4a\r\nContent-Type: text/html; charset="UTF-8"\r\nContent-Transfer-
Encoding: quoted-printable\r\n\r\n<div dir=3D"ltr">Dear Jaoah,<br>This is Janoah. I am now
writing this email=\r\n as a person.<br><br>-Janoah=C2=A0=C2=A0<br></div><br><div class=3D"gmail_q=
\r\nuote"><div dir=3D"ltr" class=3D"gmail_attr">On Mon, Apr 20, 2020 at 12:12 A=\r\nM &lt;<a href=
3D"mailto:janoah.policarpio@gmail.com">janoah.policarpio@gmai=\r\nl.com</a>&gt; wrote:<br></div>
<blockquote class=3D"gmail_quote" style=3D"ma=\r\nrgin:0px 0px 0px 0.8ex;border-left:1px solid
rgb(204,204,204);padding-left:=\r\n1ex">Dear Noah,<br>\r\nThis is Janoah, but I&#39;m not
writing this email. This is the Python scri=\r\npt doing the work for me. Mwahaha I am so lazy!
<br>\r\n<br>\r\n-Janoah<br>\r\n</blockquote></div>\r\n\r\n--000000000000b6d48205a3b26b4a--'}})
"""
#Just appreciate the formatting here. It's too messy to parse ourselves.
rawMessage = conn.fetch([39802], ['BODY[]', 'FLAGS'])

pyzmail.PyzMessage.factory(rawMessage[39802][b'BODY[]'])
#<pyzmail.parse.PyzMessage object at 0x000001D8836C53A0>
message = pyzmail.PyzMessage.factory(rawMessage[39802][b'BODY[]'])
message.get_subject()
#'Re: Python Test'
message.get_addresses('from')
#[('Charles Janoah Policarpio', 'janoah.policarpio@gmail.com')]
message.get_addresses('to')
#[('Charles Janoah Policarpio', 'janoah.policarpio@gmail.com')]
message.get_addresses('bcc')
#[]
message.text_part
#MailPart<*text/plain charset=UTF-8 len=313>
message.html_part
#MailPart<*text/html charset=UTF-8 len=617>
message.html_part == None
#False
message.text_part.get_payload().decode('UTF-8')
#"Dear Jaoah,\r\nThis is Janoah. I am now writing this email as a person.\r\n\r\n-Janoah\r\n\r\nOn Mon, Apr 20, 2020 at 12:12 AM <janoah.policarpio@gmail.com> wrote:\r\n\r\n> Dear Noah,\r\n> This is Janoah, but I'm not writing this email. This is the Python script\r\n> doing the work for me. Mwahaha I am so lazy!\r\n>\r\n> -Janoah\r\n>\r\n"
message.text_part.charset
#'UTF-8'


conn.list_folders()
"""
[((b'\\HasNoChildren',), b'/', 'Anthony Morrison'), ((b'\\HasNoChildren',), b'/', 'COLFinancial
Important'), ((b'\\HasChildren',), b'/', 'Dan Lok'), ((b'\\HasNoChildren',), b'/', 'Dan Lok/Dan
on Demand'), ((b'\\HasNoChildren',), b'/', 'Dan Lok/HTC'), ((b'\\HasNoChildren',), b'/', 'How to
Beast'), ((b'\\HasNoChildren',), b'/', 'INBOX'), ((b'\\HasNoChildren',), b'/', 'T. Harv Eker'),
((b'\\HasNoChildren',), b'/', 'The Attrractive Man'), ((b'\\HasNoChildren',), b'/', 'Tim Ferris'),
((b'\\HasNoChildren',), b'/', 'Tripp Advice'), ((b'\\HasNoChildren',), b'/', 'Unwanted'),
((b'\\HasChildren', b'\\Noselect'), b'/', '[Gmail]'), ((b'\\All', b'\\HasNoChildren'), b'/',
'[Gmail]/All Mail'), ((b'\\Drafts', b'\\HasNoChildren'), b'/', '[Gmail]/Drafts'), ((b'\\HasNoChildren',
b'\\Important'), b'/', '[Gmail]/Important'), ((b'\\HasNoChildren', b'\\Sent'), b'/', '[Gmail]/Sent Mail'),
((b'\\HasNoChildren', b'\\Junk'), b'/', '[Gmail]/Spam'), ((b'\\Flagged', b'\\HasNoChildren'), b'/',
'[Gmail]/Starred'), ((b'\\HasNoChildren', b'\\Trash'), b'/', '[Gmail]/Trash')]
"""
conn.select_folder('INBOX', readonly = False)
"""
{b'PERMANENTFLAGS': (b'\\Answered', b'\\Flagged', b'\\Draft', b'\\Deleted', b'\\Seen', b'$NotPhishing',
b'$Phishing', b'\\*'), b'FLAGS': (b'\\Answered', b'\\Flagged', b'\\Draft', b'\\Deleted', b'\\Seen', b'$NotPhishing',
b'$Phishing'), b'UIDVALIDITY': 1, b'EXISTS': 39228, b'RECENT': 0, b'UIDNEXT': 39809, b'HIGHESTMODSEQ':
9233988, b'READ-WRITE': True}
"""
UIDs = conn.search(['ON','20-Apr-2020'])
UIDs
#[39794, 39795, 39796, 39797, 39798, 39799, 39800, 39801, 39802, 39803, 39804, 39805, 39806, 39807, 39808]
#conn.delete_messages(39794)     # or put UIDs to delete all in the UIDs variable.

"""
Read more:
https://automatetheboringstuff.com/chapter16/
https://imapclient.readthedocs.org
http://www.magiksys.net/pyzmail
"""
