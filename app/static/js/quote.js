$(document).ready(function() {
  var randomQuote = {
    citations: [],
    contador: 0,
    inicio: function (){
      
      $.getJSON("https://crossorigin.me/http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=40&callback=", function(data) {
      randomQuote.citations = data;
      randomQuote.postarQuotes();
        
  });
      
      $("#atualizarQuote").on("click", this.atualizarQuote);
            },
    postarQuotes: function() {
      console.log(randomQuote.citations[randomQuote.contador].content);
      $("blockquote h3").html(randomQuote.citations[randomQuote.contador].content);
      $("blockquote footer").html(randomQuote.citations[randomQuote.contador].title);
      var content = randomQuote.citations[randomQuote.contador].content;
        content = content.substring(3, content.length -5);
        content = content.replace(/&#.{4};/g, "");
      var encodedQuote = encodeURIComponent(content);
		  var tweetUrl = "http://twitter.com/home/?status=" + encodedQuote;
      $('#btnTweet').attr('href', tweetUrl);
  },
    atualizarQuote: function(){
      console.log("Cliquei no botao");
      if (randomQuote.contador < 40){
        randomQuote.contador++;
      } else{
        randomQuote.contador = 0;
      }
      randomQuote.postarQuotes();
    }
  };
  console.log("iniciei ////////");
  randomQuote.inicio();
});