import ftplib
session = ftplib.FTP('ftpupload.net', 'epiz_29205205', 'SXoBSW6CK4h')
file = open('dummydata', 'rb')                  # file to send
session.storbinary('STOR dummydata', file)     # send the file
file.close()                                    # close file and FTP
session.quit()
