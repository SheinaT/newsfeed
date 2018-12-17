       $("#get-headline").click(function () {
            $.ajax({
                type: "GET",
                url: "http://localhost:7000/get_articles",
            }).done(function (data) {
                // var title = document.createElement("h2");
                // title.innerHTML = ("headline list:");
                // $("#headlines").append(title);
                var headlines = JSON.parse(data)["headlines"];
                headlines.forEach(function (headline) {
                    var title = headline["title"]
                    var link = headline["link"]
                    var a= $("<a/>").attr("href", link).text(title);
                    var list_item= $("<li/>").append(a);
                    $("#show-headlines ul").append(list_item);



                });

            });
        });
