1. On the line called token you will need this data from TVH. Remember making a user named *? Go to Configuration->Users->Passwords. Find the password for * select it and Edit it. Expand the Read Only Info. There is the Persistent authentication code field. Copy it to token in your file.
2. filepath needs to be set to the output location and file of the m3u that Emby will use.
3. tags_url needs to have the host put in (IP, localhost, domain name). Leave the rest of the URL alone.
4. channels_all_url needs to have the host put in (IP, localhost, domain name). Leave the rest of the URL alone.
5. Save it, then run it with python3 m3utag.py.

Please note. I did not come up with the original code. I have found various people saying they came up with it and it worked. But it did not work. I ended up making several changes to the code and posting here a working version for all to use. Thank you to the person that wrote it, but since many posted it as origial work we may never know the real person that started it.
