var detail_modal = `<!-- Modal -->
<div class="modal fade" id="DetailModal" tabindex="-1" aria-labelledby="DetailModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="DetailModalLabel">Modal title</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        ...
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>`




$("#id_query" ).on("keypress",function() {
    window.clearTimeout(timer);
    
    $("tbody").html("");
    $('#hidden-spinner').show();
 });
  
 $("#id_query" ).on("keyup",function() {
    console.log($(this).val())
    window.clearTimeout(timer);
    timer = window.setTimeout(() => {
        var form_data = $("#renta_autosFilterForm").serialize();
        $('#hidden-spinner').hide();
        get_datatable(get_list_url(1, form_data))
    }, timeoutVal);
 });


 $("#renta_autosFilterForm input, select").change(function (e){

    $size = $('.page-size-input').val()
    size = $size
    form_data = $("#renta_autosFilterForm").serialize();
    get_datatable(get_list_url(1, form_data))
 
});


/*  Bootstrap-Table plugin */
$('table').bootstrapTable({
    showFullscreen: true,
    stickyHeader: true,


})

$(document).on('change', 'input[name="fec_alta"]', function(e){
    window.clearTimeout(timer);
    timer = window.setTimeout(() => {
       var form_data = $("#renta_autosFilterForm").serialize();
       let params = new URLSearchParams(form_data);

       if (params.get('fec_alta') !== ''){
          get_datatable(get_list_url(1, form_data))
       }
    }, timeoutVal);
});


$('input[name="fec_alta"]').daterangepicker({
    locale: {
       format: 'YYYY-MM-DD',
       "applyLabel": "Aplicar",
       "daysOfWeek": [
       "Do",
       "Lu",
       "Ma",
       "Mi",
       "Ju",
       "Vi",
       "Sa"
   ],
   "monthNames": [
       "Enero",
       "Febrero",
       "Marzo",
       "Abril",
       "Mayo",
       "Junio",
       "Julio",
       "Agosto",
       "Septembre",
       "Octubre",
       "Noviembre",
       "Diciembre"
   ],
   }
});
$('input[name="fec_alta"]').val("")