This tool will grab the m3u data from TVHeadEnd and output a m3u file. While you can do this direct from TVHE, it does not have the tag data like US, UK, Locals or whatever you use and these are nice to have as categories in Emby and other players.

To setup (directions are for the old TVHE UI, new UI may be different):
1. Do you have a user named *? Normally you will for any user to watch TV. If not, read the TVHE docs about setting one up.
2. Edit the code file. On the line called token you will need this data from TVHE. Go to Configuration->Users->Passwords. Find the password for * select it and Edit it. Expand the Read Only Info. There is the Persistent authentication code field. Copy it to token entry in your file.
3. filepath needs to be set to the output location and file of the m3u that Emby or other clients will use. Make sure its accessable from clients on the file system or web server.
4. tags_url needs to have the host put in (IP, localhost, domain name). Leave the rest of the URL alone.
5. channels_all_url needs to have the host put in (IP, localhost, domain name). Leave the rest of the URL alone.
6. Save it, then run it with python3 m3utag.py.

Please note. I did not come up with the original code. I have found various versions from various people saying they came up with it. I ended up making several changes to the code I found and posting here a working version for all to use. Thank you to the person that wrote the original version, but since many posted it as origial work we may never know the real person that started it.
