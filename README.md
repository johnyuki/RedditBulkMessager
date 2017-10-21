# Reddit Bulk Messager

*Messages users that have opted-in to a "Get notified of new posts"-type newsletter.*
*Misuse of this script will probably lead to your account being banned.*

# Setup instructions
*Instructions are for Windows. I've never done this on any other OS so I cannot help, sorry.*

- Download Python 3.6 from the Python website here - https://www.python.org/downloads/

- When installing, make sure you select "add python to PATH environment" or whatever that box is. I can't remember the exact wording, but it is something along those lines. You can just spam click "next" after checking that box.

- After it is completed, open your command prompt and type in *pip install praw* and wait for it to install. Once it is installed you can close the command prompt. 

- Download this script by clicking on the green *Clone or Download* button, followed by *Download ZIP*. After it downloads, extract the *Send New Message.py*, *Opt-in Comment Finder.py*, *config.py*, and *Subscriber List.db* files anywhere you like. Make sure you keep them together in the same folder/directory.

- Open your start menu and type *IDLE*, and open the program that is called *IDLE (Python 3.6 32-bit)*. It might also be 64-bit instead of 32-bit. 

- When the window opens, go to *File > Open* and select the *config.py* file that you just extracted.

- Next, to create a bot account on Reddit, create a new Reddit account like you normally would. After it is created, go to *preferences > apps > create new app*. Make sure you select *script*. Call the bot whatever you like, and in the *redirect uri* box, enter *http://localhost:8080*. Then click create. You can also do this with your main account if you like.

- Go back to IDLE and follow the instructions that I commented in for you in the *config.py* file. (Everything with a hash symbol before it. The text should be red.)

- After you entered in all of the credentials for your bot, save *config.py*, close it, and open *Opt-in Comment Finder.py*. You can leave this open 24/7 if you like, or you can open it intermittently throughout the day. If this script does not run, then no names will get added to the database. If you want to send a message to your subscribed users, open *Send Message.py* and follow the instructions on screen.

If someone wishes to be removed from the messaging list, download DB Browser for SQLite here - http://sqlitebrowser.org/

Once downloaded and installed, open up *Subscriber List.db* using DB Browser. Once opened, click on *Tables* and there should be a dropdown menu just underneath the *Tables* tab. Select *Subscribers* in the dropdown menu. Next, start typing in the name of the person who wishes to be removed from the database in the *Filter* box that is directly underneath the *Username* column title, and they should appear. Click on their username and click *Delete Record*. Save the changes and then close the database. 

If you cannot get the bot set up using these instructions or the bot crashes with an error message, head over to https://www.reddit.com/r/redditdev and make a text post there. Make sure you link this github page so that we can help you quicker and let us know what the problem is. 

