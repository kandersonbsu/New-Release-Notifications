Ideas: Use alerts to monitor when new media is added.

       When a new media item is added, call the recentlyAdded function with a parameter of 1 and store that
       item in an array.

       At the end of every hour, check if either of the arrays have items in them, if so, dump the array contents
       into a text message that is sent as an alert.

       Each title sent in the message could be a link to the media's TVDB/IMDB page. Might have to pull their API
       as well.

TODOS: Implement alerts to look for changes in media.
       Figure out a way to send out hourly alerts. (Text message, email, etc)


Nice To Have: GUI