# Social-Media-Analytics - Twitter, Youtube, Yelp

# Twitter

## Signing up for using Twitter APIs

Using Twitter API to access twitter data.

We are creating a twitter app using https://apps.twitter.com . Once we create an app we make a file named auth.k which contains keys/tokens in the order Consumer_key, Consumer_secret, Access_token, Access_token_secret. These are copied from the twitter app which we created. 

## Get the Twitter search Python script 

We write script in Python to use the authentication keys to get data from twitter. The file tw_search.py takes the auth.k as input which calls the twitter and get us the data.

We run tw_search.py python script using the configuration  python ./twitter_search.py brexit -c 180 where the third word (brexit)is the search term we want to run on Twitter. This searches brexit tweets and retrieve 180 tweets. The script writes the data in result.csv file having 6 columns – created time, retweet count, hashtag, followers count, friends count. We take different topics/politicians and re-run the python script to collect 180 tweets for each topics/politicians.

## Regression Analysis

We use the dataset to see if there are any relationships among number of followers, number of friends, and number of retweets. We create a new python script (Twitter_FriendsFollowers.py) for analysing the relationships. We find correlations among variables in the dataset. We create regression model, plot and line for varaibles having medium to high level positive/negative correlation. We check the R-square value and the p-value. Based on the regression plot and model, we state the hypothesis such as more followers, more number of retweets.

## Sentiment Analysis on Twitter data

People express all kinds of opinions and sentiments on Twitter, so we analyse those sentiments. We write a script in python twitter_sentiments.py script to perform Sentiment Analysis for a topic/politician. 

We use a package called TextBlob, which has a number of very useful functions for processing textual data.To use those functions, we need to convert a string (text) to an object of TextBlob type.

First, we collect some data as we did before. Next, we use the TextBlob package to go through the dataframe one row at a time and find the text – in this case a tweet stored in a variable/column named ‘text’. Once we have that tweet, convert it into a TextBlob object, and then we can ask it to analyze that string for subjectivity and polarity.

This script calculates the polarity and the subjectivity and adds in the data. The resulted file from this contains 10 columns: username, author id, created, text, retwc, hashtag, followers, friends, polarity, subjectivity. We change the query to different topics/politicians and re-run the python script to collect tweets and calculate polarity and subjectivity(sentiments) for each topics/politicians (Gun control).

We create a new python script(TwitterGun.py) for analysing the above resulted file. We again find the correlation between variables in the resulted file. We create regression model, plot and line for varaibles having medium to high level positive/negative correlation. We check the R-square value and the p-value. Based on the regression plot and model, we state the hypothesis such as More the followers, more the tweets sentiment is becoming objective, as the subjectivity is getting close to zero.


# Youtube

## Signing up for using YouTube APIs

Using YouTube API to access YouTube data.

We are creating a project in Google API console for using Youtube API. We go to https://developers.google.com/api-client-library/python/start/get_started#setup to get started. Then we create API credentials for using the Youtube API.

## Get the Youtube search Python script 

We write script in Python to use the developer key to get data from Youtube. The file youtube_search.py takes the developer key get us the Youtube data.
We run youtube_search.py python script using the configuration  python youtube_search.py --q superbowl where the fourth word (superbowl)is the search term we want to run on Youtube. We run youtube_search.py python script for each topics. The script is dumping information about title, videoId, viewCount, likeCount, dislikeCount, commentCount, and favoriteCount in youtube_results.csv file. We re-run the python script to collect data for each topics.
 
## Regression Analysis

We use the dataset to see if there are any relationships among viewCount, likeCount, dislikeCount, commentCount. We create a new python script (Youtube.py) for analysing the relationships. We find correlations among variables in the dataset. We create regression model, plot and line for varaibles having medium to high level positive/negative correlation. We check the R-square value and the p-value. Based on the regression plot and model, we state the hypothesis such as there is a relationship between likecount and commentcount.

# Yelp

## Get the Yelp data

There are several kinds of datasets one could obtain from Yelp from this Website: https://www.yelp.com/dataset/challenge. Yelp is providing these datasets as a part of running various rounds of data challenges. We directly download it from Yelp.

## Visualize the data

We create bar chart, pie chart, histogram, scatter plot, stacked bar graph using R.

## Regression Analysis

We use the dataset to see if there are any relationships among reviewcount, cool_votes, useful_votes and funny_votes.. We create a R script (.R) for analysing the relationships. We find correlations among variables in the dataset. We create regression model, plot and line for varaibles having medium to high level positive/negative correlation. We check the R-square value and the p-value. Based on the regression plot and model, we state the hypothesis.
