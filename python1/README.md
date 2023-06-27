**Python API Experiments - steam.py**

This folder contains some of my experiments with accessing API's and manipulating the returned data via Python.

For my safety, all secret API keys and other personal info are imported from a local only config file to avoid compromising secret keys.

*Purpose*:
steam.py is script that grabs personal time spent playing video games from Steam's API, which is then added to a spreadsheet.
This script is designed to run daily via a Linux system's cronjob/crontab  This allows a large amount of data to be built up over time, enhancing the data's value.

*Issues*:
As I was having so many issues getting cronjobs to reliably run dialy, I added a notification feature to the script. This would send a text to my phone using the EZGmail module via my carriers special "text someone's number via email address".
This lead to the downfall of the script however, as the EZGmail API key/token needs a Google Cloud project, expressly created for that purpoes, to work. But, it has a weird issues which requires you to do some janky re-verification every 7 days (which seemingly can't be automated).
The above, and the Linux Desktop I was using at the time self-destructing, lead to me shelving this script. 

*Future*:
Once I have an active server of some kind again I will consider picking this back up. May end up adapting it for daily Windows use instead of Linux, as I currently have Windows installed on my 24/7 turned-on computer. I may end up using WLS (Windows Linux Subsystem) to facitate some sort of resemblence to my previous system.