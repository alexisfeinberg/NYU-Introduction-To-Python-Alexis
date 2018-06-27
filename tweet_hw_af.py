capacity=280
question=input('You have {} characters to play with - would you like to change the default? Yes or No\n'.format(capacity))

if question=='Yes' or question=='yes' or question=='YES':
    limitq=input("Please enter in the limit:\n")
    capacity=int(limitq)

tweet=input("Please insert your tweet:\n")
tweet_length=len(tweet)

if tweet_length<capacity:
    print('That tweet is {} characters and you have {} remaining characters'.format(tweet_length, (capacity - tweet_length)))
elif tweet_length==capacity:
    print('This is {} characters. You used your tweet well'.format(capacity))
else:
    print('That tweet is {} characters - please cut {} characters'.format(tweet_length, (tweet_length - capacity)))
