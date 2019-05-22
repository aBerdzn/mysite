
$("#main").click(function () {

    $.getJSON(" http://sf-pyw.mosyag.in/m04/api/forecasts",function (data) {
        message = data["prophecies"]
        set_content_in_divs(message)
    });


});

function set_content_in_divs(paragraphs) {
  $.each(paragraphs, function(i, d) {
    p = $("#p-" + i)
    p.html("<p>" + d + "</p>")
    p.css("color","green")
  })
};