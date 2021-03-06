"""
Constants around Mail Protocols, Mail Ports, Mail Commands and Socket Connectivity. 
"""

POP_STANDARD = 110
POP_IMPLICIT_SSL = 995
POP_USER = b'USER '
POP_PASS = b'PASS '

SMTP_STANDARD = 25
SMTP_IMPLICIT_SSL = 465
SMTP_STARTTLS_SSL = 587
SMTP_EHLO = b'EHLO gmail.com \r\n'
SMTP_AUTH = b'AUTH LOGIN \r\n'

IMAP_STANDARD = 143
IMAP_IMPLICIT_SSL = 993
IMAP_RAND_STRING = b'A1 '
IMAP_CAPABILITY = b'CAPABILITY \r\n'
IMAP_LOGIN = b'LOGIN '

STARTTLS_COMMAND = b'STARTTLS \r\n'

EMAIL_USERNAME = b'changeme@gmail.com'
EMAIL_PASSWORD = b'changeme'

SOCKET_TIMEOUT = 5
OPENSSL_TLS_SUITES = ["tls1","tls1_1","tls1_2"]
MAIL_PROTOCOLS = ["smtp","pop","imap"]
COMMON_MAIL_PROVIDERS= ["gmail","yahoo","hotmail","zoho"]
COMMON_MAIL_PORTS = [SMTP_STANDARD,SMTP_STARTTLS_SSL,SMTP_IMPLICIT_SSL,POP_STANDARD,POP_IMPLICIT_SSL,IMAP_STANDARD,IMAP_IMPLICIT_SSL]
