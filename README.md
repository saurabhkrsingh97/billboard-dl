## Billboard Downloader
###### Python3 script to download music videos of the Top 'n' songs from the [Billboard Hot 100](http://www.billboard.com/charts/hot-100) list.

----------
### Installation & Usage
##### Dependencies
1. [Requests](http://docs.python-requests.org/en/master/) (HTTP Library): `sudo pip install requests`

2. [Pafy](http://pythonhosted.org/Pafy/) (Retrieve YouTube content/metadata):  `sudo pip install pafy`

3. [Beautiful Soup 4](http://www.crummy.com/software/BeautifulSoup/bs4/doc/) (Parsing HTML into tree structure): `sudo pip install beautifulsoup4`

4. [youtube-dl](https://rg3.github.io/youtube-dl/) (used as backend for Pafy): `sudo pip install youtube-dl`

Clone the repository locally, and open a terminal window in the folder.

Running `python3 billboard_dl.py` downloads the top 5 songs (default) in a sub-folder in the Billboard folder.
Folder is created if not already present.

The default value of the number of songs can be overridden by passing an argument with *billboard_dl.py*, or by changing the value of `TOP_N` variable in code.

###### Example:
`python3 billboard_dl.py 10` - Downloads the top 10 songs' music videos from the Billboard list.

----------
### License
*Please see [LICENSE](https://github.com/saurabhkrsingh97/billboard-dl/blob/master/LICENSE)*

----------
*:octocat: Suggestion for improvement are welcome!* :octocat:
