# BookmarksToPDF <br>
Converts Twitter bookmarks to PDF. Simply log in with Twitter and the script does the rest. Please note that as of launch videos and GIFs are not supported but it may save the thumbnail. Profile pictures are low quality, that's what happens when you download a 48x48 image, don't be alarmed when you see this <3
<br>
<br>

# How to use? Text guide: <br>
No coding knowledge required! :D  <br>
- Install PyCharm Community Edition, scroll down: https://www.jetbrains.com/pycharm/ <br>
- Install Python. Tick both "install as admin" and "create PATH" commands. https://www.python.org/downloads/ <br>
- Download the "Main" folder of this Git, and store it in a folder by itself to ensure it doesn't overwrite any data of yours <br>
- Open PyCharm, and load this project <br>
- PyCharm will prompt you to configure the interpreter and install dependancies, this is normal and expected. Allow it to automatically do them. Please note the blue bar at the bottom of the screen for both. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- If Python does not ask you to install dependancies, run this code in the terminal: "pip install -r requirements.txt" without the "". This tells Python to install the dependencies I have assigned in in requirements.txt <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - If this fails to find the file you will have to tell it where the requirements is. For example "pip install -r C:\usr\downloads\BookmarksToPDF\Main\requirements.txt" <br>
- Now run "playwright install" in the terminal without the "". This ensures playwright is fully installed and allows a browser window to open. <br>
- Run the program <br>
- When Twitter opens the program will pause, log in to Twitter and then press ENTER inside the running terminal of PyCharm <br>
- At this point PyCharm should direct itself to your bookmarks and download tweets whilst scrolling down, and this should be reflected in the running terminal <br>
- When it reaches the bottom of your bookmarks it will try scrolling a few times to ensure it is done, when it registers this, it will generate the PDF file. <br>
 <br>

# How to use? Video guide: <br>
Download and watch the Demonstation.mp4 video <br>
By the way, all bookmarks are just the first Tweets on my feed after making the account. I do not endorse the random racist posts that were pushed to my feed. <br>
<br>

# Are my login details safe?
As far as I am aware, yes. I do not have any trackers in the code for you login details and you must manually log in to the official Twitter site for this to work. However, I am cautious to give an absolute 100% gaurentee as I cannot gaurentee that one of the libraries I use for this one day become comprimsed - however I would personally trust this, but change my password BEFORE and AFTER usage just to be safe. Changing your password before means if the password is used anywhere else it can't be comprimised, and changing after for the same reason as well as keeping your Twitter safe. <br>
 <br>
For the non-techy users, please keep in mind this code (and GitHub in general) is open source, you are free to copy and paste it into ChatGPT or ask a friend their opinion before running it if you are unsure. <br>
 <br>
# PLEASE KEEP IN MIND THAT IN THIS CURRENT STATE IT STORES EVERYTHING TO RAM FIRST. YOU SHOULD STILL BE ABLE TO SAVE 10K-20K TWEETS BEFORE RUNNING OUT WITH ONLY 8GB OF RAM  <br>
<br>

# I ALSO RECOMMEND STORING THIS ON A USB JUST IN CASE YOU RUN OUT OF STORAGE <br>
<br>

# PLEASE NOTE THIS COULD GET YOUR TWITTER BANNED BECAUSE MUSK IS AGAINST SCRAPING <br>
<br>

# AI DISCLAIMER
I want to be very forward with the fact this project did utilise AI quite heavily. Usually I am against any useage, however I deemed it harmless for this project as: <br>
- There is a demand for this program that doesn't cost an arm and a leg <br>
- I still had to alter the garbage it gave me to be useable <br>
- I have no experience with this sort of usage of Python and thus it would have taken me significantly longer, if at all, to come out. <br>

I wish to be as transparent as possible, and I believe ChatGPT has done around 75% of the project with the remainder being me making it actually work (example: it saved all images under the same name so the PDF only had one image dozens of times, or how it would only read the last 4 Tweets) as well as ensuring it's as user friendly as possible without being complex as it was wanting users to install specific browsers and drivers. I take editoral credit at best. <br>
