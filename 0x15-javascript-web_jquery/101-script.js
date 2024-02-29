//Adds, removes and clears LI elements from a list when the user clicks
//on buttons in the toolbar.

$(document).ready(function() {
    $("#add_item").click(function() {
        $("<li>Item</li>").appendTo(".my_list");
    });

    $("#remove_item").click(function() {
        $(".my_list li:last-child").remove();
    });

    $("#clear_list").click(function() {
        $(".my_list").empty();
    });
});
