# Random Thoughts
A Simple Flask web app that randomly shows the title of r/ShowerThoughts top posts
Steps:
- Created a Reddit instance and with a client_id , client_secret and a user_agent(Needed for authentication of PRAW).
- Web Scraped the Data using Python Reddit API Wrapper(PRAW)
- Saved the data in pandas dataframe
- Exported the data to csv file
Steps for Flask:
- Initiate the flask boilerplate code
- Python function that returns a random title from the pandas file
- Linked it directly to the index.html with tag as {{idea}}
