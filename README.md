# Project Abstract

<p>
Millions of people use Twitter and reddit as a social media web platform tool to express their thoughts and opinions on a range of subjects. As a result, a stream of text data, made up of enormous numbers of tweets, posts, comments, 'r/spotify', 'r/music','r/musican','r/singer'etc is generated. For this project, we’re especially seeking tweets, posts etc that refer to certain Spotify tunes, music, albums and artists. We analyse those tweets, 'r/spotify', 'r/music' ,'r/musican', 'r/singer', posts, and comments and gather track-related data using the Spotify API. Finally, we want to identify the artists who are now trending by using the information we’ve acquired in combination with a particular time frame.
</p>

<p>
Data Source -
<br>Here, in this project we used Twitter and Reddit data from their respective API’s to collect tweets and posts. Using that data, we collected information about top trending songs. For this we used Spotify web API to fetch data from a Spotify URL. We extracted track ID from the URL and sending it as a parameter to the Spo- tify API to retrieve details of any available track. For Twitter we used streaming API and for Reddit, we collected data using https://www.reddit.com/api/v1/accesstoken endpoint. </p>

<p>
Tech-stack
<br>
Python - The project is developed and tested using python v3.8. Python Website
HTTP Request - Request is a popular HTTP networking module(aka library) for python programming language. Request Website
Datetime - The datetime library used for manipulating dates and times Python documentation Website
JSON - Json is python build in package used to work on JSON data got from different API get requestPython documentation Website
Base64 - base64 is python library used for data encoding Python documentation Website
MongoDB - MongoDB is NoSQL document database used to store data collected from Spotify,Reddit and Twitter websites MongoDB Website
PyMongo - PyMongo is Python distribution containing tool used to work with MongoDB using python [PyMongo Website] ( https://pymongo.readthedocs.io/en/stable/)
System Cron Job - System Cron Job is used to schedule tasks to run at a specific time in the future [System Cron Job Website] ( https://opensource.com/article/17/11/how-use-cron-linux )
Pandas - Used to analyze the live streaming of trending artists over Twitter, Reddit and Spotify platforms.
Matplotlib - A python library to visualize the data.

Database schema - NoSQL MongoDB

Three data-source documentation

Twitter
https://developer.twitter.com/en/docs/twitter-api/v2/tweets/sample-realtime/overview – this end point URL provides an approximately 1% sample of Tweets in real time related to #spotify

Reddit - We are using r/spotify,r/music, r/musician,r/singer etc.
https://www.reddit.com/api/v1/access_token - <this Reddit end point URL provide data for post related to music, musician etc.>

Spotify - *"https://api.spotify.com/v1/search" -
</p>


