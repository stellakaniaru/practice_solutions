"""
A python program that allows you to be able to conveniently view your Chrome bookmarks.
It eliminates the process of having to scroll through the Gui folders.
Once run, it provides you with a well structured html format of your bookmarks. Looks similar to the one
you get once you export your bookmarks.

The one beauty with this is that unlike the exports, you don't need to have multiple backups to capture
new bookmarks. Simply run the program and new bookmarks and folders will be directly added to the file.

!!!PENDING!!!
Getting the tab to load and reload depending on the occasion i.e. either an initial write or a 
consequent update.
"""

from pathlib import Path
import json
import webbrowser
from webbrowser import open_new_tab

#specify path to Chrome's bookmarks.bak file
local_filepath = Path("C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Bookmarks")

#specify the location of the file 
file_location = Path("D:\\book" + "\\bookmarking.html")

#specify local url to use for the page
url = "D:/book/bookmarking"

#access contents of the bookmarks.bak file
local_file_open = local_filepath.read_text()


#enable the created file to have write access
new_file_open = open(file_location, "w")

#load json data
#specify the initial root structure
json_data = json.loads(local_file_open)
node_layout = json_data[ "roots"]["bookmark_bar"]["children"]

#create html wrappers
wrapper = """
    <h3>%s</h3>
    """

wrapper2 = """
 	<a href = "%s">%s</a><br>
"""

def create_initial_file(node_layout):
	'''Creates the initial html file and adds the bookmarks'''

	#Iterate through the json data.
	#Sift through the data and write the content to the html document.
	for key_index in node_layout:
		if key_index["type"] == "url":
			new_file_open.write(wrapper2 %(key_index["url"], key_index["name"]))
		if key_index["type"] == "folder":
			new_file_open.write(wrapper % (key_index["name"]))
			sec_key_index = key_index["children"]
			for element in sec_key_index:
				if element["type"] == "url":
					new_file_open.write(wrapper2 % (element["url"],element["name"] ))

				if element["type"] == "folder":
					new_file_open.write(wrapper % (element["name"]))
					sec_key_index = element["children"]
					for i in sec_key_index:
						if i["type"] == "url":
							new_file_open.write(wrapper2 % (i["url"],i["name"] ))
	

def add_additional_bookmarks(node_layout):
	'''updates the original file with any new bookmarks'''

	#access contents of the bookmarks.bak file and split into individual lines
	local_file_open2 = local_filepath.read_text().splitlines()

	#Iterate through the json data.
	#At each stage that needs you to edit the file, first check if the line exists in the file already
	#If it does, don't write it to the file. 
	#If it doesn't, write it to the file.
	for key_index in node_layout:
		if key_index["type"] == "url":
			if key_index["name"] not in local_file_open2:
				new_file_open.write(wrapper2 %(key_index["url"], key_index["name"]))
		if key_index["type"] == "folder":
			if key_index["name"] not in local_file_open2:
				new_file_open.write(wrapper % (key_index["name"]))
				sec_key_index = key_index["children"]
			for element in sec_key_index:
				if element["type"] == "url":
					if element["name"] not in local_file_open2:
						new_file_open.write(wrapper2 % (element["url"],element["name"] ))

				if element["type"] == "folder":
					if element["name"] not in local_file_open2:
						new_file_open.write(wrapper % (element["name"]))
					sec_key_index = element["children"]
					for i in sec_key_index:
						if i["type"] == "url":
							if i["name"] not in local_file_open2:
								new_file_open.write(wrapper2 % (i["url"],i["name"] ))

	

#if file does not exist, go through the motions of creating it and adding data
if file_location.exists():
	add_additional_bookmarks(node_layout)
#if file exists, read through the file, check if there is any new data and add it
else:
	create_initial_file(node_layout)
	