
          $(document).ready(function(){
            console.log('ready');
            //Activate Smooth Scroll
            var $root = $('html, body');
            $('.smooth a').click(function() {
                $root.animate({
                    scrollTop: $( $.attr(this, 'href') ).offset().top
                }, 500);
                return false;
            })
            //Mobile Sidebar
            $(".button-collapse").sideNav();



            //Twitter Functions
            window.twttr = (function(d, s, id) {
              var js, fjs = d.getElementsByTagName(s)[0],
              t = window.twttr || {};
              if (d.getElementById(id)) return t;
              js = d.createElement(s);
              js.id = id;
              js.src = "https://platform.twitter.com/widgets.js";
              fjs.parentNode.insertBefore(js, fjs);

              t._e = [];
              t.ready = function(f) {
                t._e.push(f);
             };

             return t;
            }(document, "script", "twitter-wjs"))


        })
