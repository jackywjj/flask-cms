$(function() {
    $('.delete').click(function(){
        var url = $(this).attr("href");
        if (confirm("Are you sure to delete it ?")) {
            window.location = url;
        }
        return false;
    });
});