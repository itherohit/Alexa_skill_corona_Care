# Alexa_skill_corona_Care

Corona Care is a alexa skill created to give you clarification, and additional information about corona. 
You can ask any questions related to corona, or even you can also get information about the total number of corona cases, 
deaths, and recovered cases all around the world. Get a detailed information about any country related to corona cases count. 
You can also do a risk check for corona which will ask certain questions and tells your risk score for corona 
and gives you suggestions based on your risk score. And the cool thing is, you can hear some cool corona songs from my skill.

lambda_function.py is used to execute the code for the skill and it runs in the aws lambda function.
corona_care.json is the json code for amazon alexa for the intents,utterences and slots.

Go to amazon developer console and create your skill.
You have to paste the .json file in the json editor of your skill.
lambda_function.py in the aws lambda function.
Add trigger to the lambda function with alexa skill's kit
In developer console of your skill add your endpoint.(add aws lambda link)
