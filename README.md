1. On the line called token you will need this data from TVH. Remember making a user named *? Go to Configuration->Users->Passwords. Find the password for * select it and Edit it. Expand the Read Only Info. There is the Persistent authentication code field. Copy it to token in your file.
2. filepath needs to be set to the output location and file of the m3u that Emby will use.
3. tags_url needs to have the host put in (IP, localhost, domain name). Leave the rest of the URL alone.
4. channels_all_url needs to have the host put in (IP, localhost, domain name). Leave the rest of the URL alone.
5. Save it, then run it with python3 m3utag.py.
