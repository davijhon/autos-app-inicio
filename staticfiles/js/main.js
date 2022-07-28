function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
 }
const csrftoken = getCookie('csrftoken');


var ws_scheme = window.location.protocol
var path = ws_scheme + '//' + window.location.host + "/";
var current_page = 1;
var size = 10;
let timer, timeoutVal = 1000;





function showDetailModal(id){
    url = window.location.href
    url += `api/renta-autos/${id}/`;
 
    if ($('body').find('#DetailModal').length === 0){
       $('body').append(detail_modal)
       $('#DetailModal').modal('show')
   } else {
       $('#DetailModal').remove()
       $('body').append(detail_modal)
       $('#DetailModal').modal('show')
   }
 

    // $.ajax({
    //    method: "GET",
    //    url: url,
    //    success: function(data){
    //       create_data_status_layout(data)
 
    //    },
    //    error: function(response){
    //       console.log("Error Ajax function.")
    //       console.log(response)
    //       Swal.fire({
    //          title: 'Error!',
    //          html: response['error'],
    //          icon: 'error'
    //       });
    //    }
    // })
}

function changeStatus(action){

    if (action === 'loading'){
        $('.overlay-wrapper').removeClass("d-none")
        $("#hidden-spinner").show();
    } else {
        $('.overlay-wrapper').addClass("d-none")
        $("#hidden-spinner").hide();

    }
}

function create_pagination_control(res){
    previous_url = res.links.previous;
    next_url = res.links.next;
    page_links = res.page_links.page_links;
 
    ul = '<ul class="pagination" style="margin: 5px 0 10px 0;justify-content: center;">'
 
    if (previous_url){
       li = `<li>
                <button  class="page-link" data-url="${previous_url}" aria-label="Previous">
                   <span aria-hidden="true">&laquo;</span>
                </button>
             </li>`;
    } else {
       li = `<li class="page-item disabled">
                <button  class="page-link" aria-label="Previous">
                   <span aria-hidden="true">&laquo;</span>
                </button>
             </li>`;
    }
    ul += li;

    $.each(page_links, function (id, page){
       if (page.is_break) {
          li2 = `<li class="page-item disabled">
                   <button class="page-link"><span aria-hidden="true">&hellip;</span></button>
                </li>`
       } else {
          if (page.is_active ){
             li2 = `<li class="page-item active">
                      <button class="page-link" id="button-${id}" data-url="${page.url}">${page.number}</button>
                   </li>`
          } else {
             li2 = `<li>
                      <button class="page-link" id="button-${id}" data-url="${page.url}">${page.number}</button>
                   </li>`
          }
       }
       ul += li2;
    });
 
    if (next_url) {
       li3 = `<li>
                <button class="page-link" data-url="${next_url}" aria-label="Next">
                   <span aria-hidden="true">&raquo;</span>
                </button>
             </li>`
    } else {
       li3 = `<li class="page-item disabled">
                <button class="page-link" aria-label="Next">
                   <span aria-hidden="true">&raquo;</span>
                </button>
             </li>`
    }
    ul += li3;
    ul += `</ul>`
 
    return ul
 
}

function truncateString(str, num) {
    // If the length of str is less than or equal to num
    // just return str--don't truncate it.
    if (str.length <= num) {
      return str
    }
    // Return str truncated with '...' concatenated to the end of str.
    return str.slice(0, num) + '...'
}

function putTableData(res){
    $(`#table_${section_name} tbody`).html("")
    tbody = $(`#table_${section_name} tbody`)

    if (res['results'].length > 0){
        $.each(res['results'], function (a, b){
            var id = b.id_uuid
            var row = "<tr><td>"+b.cuenta_numero+"</td>"
                row += `<td><a href='javascript:void(0);' onclick='showDetailModal("${id}")'>`+b.user_name+`</a></td>`
                row += "<td>"+b.fec_alta+"</td>"
                row += "<td>"+b.codigo_zip+"</td>"
                row += "<td>"+b.compras_realizadas+"</td>"
                row += "<td>"+b.color_favorito+"</td>"
                row += "<td>"+b.fec_birthday+"</td>"
            tbody.append($(row))

        });
    } else {
        $(`#table_${section_name} tbody`).html("No se encontraron resultados.")
    }

    pagination = create_pagination_control(res)
    $(".pagination-box").html("")
    $(".pagination-box").append(pagination)
}

function sendAjaxRequest(url, method, data, sender_form, load_data_table){

    changeStatus("loading")
    $.ajax({
        url: url,
        type: method,
        dataType: 'json',
        headers: {
           "X-CSRFToken": csrftoken,
        },
        data: data,
        processData: false,
        contentType: false,
        success: function(response){
            if (method === "POST"){
                console.log("POST process")
                // displayFormMessage(response, sender_form)
                // // get_datatable(get_list_url(1));
                // changeStatus(null)
            } else if (method === "GET" && load_data_table === true){ 
                console.log(response)
                current_page = parseInt(response.links.current);
                putTableData(response);
                
                $("#result-count span").html(response.count)
                if (response.links.current == null){
                    $("#page-count span").html("1")
                } else {
                    $("#page-count span").html(response.links.current)
                }
                changeStatus(null)
                
            } else if (method === "GET" && load_data_table === false){
                console.log("GET process for return or display info")
                // placeDataOnForm(response, sender_form)
                // changeStatus(null)
            }

        },
        error: function(response){
           console.log("Error Ajax function.")
           console.log(response)
           Swal.fire({
              title: 'Error!',
              html: response['error'],
              icon: 'error'
           });
        }
    })
}

function get_list_url(page, query){
    // TODO: Improve this logic, better change 
    // the url on server-side??
    if (section_name === 'renta_autos'){
        var section = 'renta-autos';
    }


    url = path
    url += `api/${section}/list?page=${page}&size=${size}`;

    if (query){
        query = "&" + query
        url += query
    }
    return url
}

function get_datatable(url){
    sendAjaxRequest(url, "GET", null, null, true)
}

$('.cleaner').click(function(){
    $(`#${section_name}FilterForm`).trigger("reset");
    get_datatable(get_list_url(1))
});



$(document).on("click", ".page-link", function (e) {
    e.preventDefault();
    let url = $(this).attr("data-url");
    
    // $('body,html').animate({
    //     scrollTop: 0
    //  }, 400);

    get_datatable(url);
})

if (section_name === 'renta_autos'){
    get_datatable(get_list_url(current_page));
}