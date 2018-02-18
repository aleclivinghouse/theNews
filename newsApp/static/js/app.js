$.getJSON("https://graph.facebook.com/time/?fields=fan_count&access_token=2105558582997469|Tpq1HU_tE_nsBPyg-_IxA0JMD88", function(facebook_info){
  var facebook = facebook_info.fan_count;
  $(".facebook-followers").text(facebook);
});



// $.getJSON("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UC8Su5vZCXWRag13H53zWVwA&key=AIzaSyBu7qsiGXTC1ILc7MpB53X6sKhgZQjHmyM", function(youtube_info){
//   var youtube = youtube_info.items.[0].statistics.subscriberCount;
//   $(".youtube-followers").text(youtube);
// });

// var facebook_url = "https://graph.facebook.com/time/?fields=fan_count&access_token=2105558582997469|Tpq1HU_tE_nsBPyg-_IxA0JMD88";
// var twitter_url = "http://api.twittercounter.com/?twitter_id=14293310&apikey=f47d36978d20a11767f06df3489b5aa6"
//
// $.when(
//     $.getJSON(facebook_url),
//     $.getJSON(twitter_url)
// ).done(function(facebook_info, twitter_info) {
//      var facebook = facebook_info.fan_count;
//      $(".facebook-followers").text(facebook);
//      var twitter = twitter_info.followers_current;
//      $(".twitter-followers").text(twitter);
//
// });
