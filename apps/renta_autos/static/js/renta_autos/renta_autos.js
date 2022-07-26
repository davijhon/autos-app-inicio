



$("#id_query" ).on("keypress",function() {
    window.clearTimeout(timer);
    
    $("tbody").html("");
    $('#hidden-spinner').show();
 });
  
 $("#id_query" ).on("keyup",function() {
    console.log($(this).val())
    window.clearTimeout(timer);
    timer = window.setTimeout(() => {
        var form_data = $("#FilterForm").serialize();
        $('#hidden-spinner').hide();
        get_datatable(get_list_url(1, form_data))
    }, timeoutVal);
 });






/*  Bootstrap-Table plugin */
$('table').bootstrapTable({
    showFullscreen: true,
    stickyHeader: true,
    // stickyHeaderOffsetLeft: parseInt($('body').css('padding-left'), 50),
    // stickyHeaderOffsetRight: parseInt($('body').css('padding-right'), 250),

})