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
let timer, timeoutVal = 1000;




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

function putTableData(res){
    $("table tbody").html("")
    tbody = $("table tbody")

    if (res['results'].length > 0){
        $.each(res['results'], function (a, b){
            var row = "<tr><td>"+b.cuenta_numero+"</td>"
                row += "<td>"+b.user_name+"</td>"
                row += "<td>"+b.fec_alta+"</td>"
                row += "<td>"+b.codigo_zip+"</td>"
                row += "<td>"+b.direccion+"</td>"
                row += "<td>"+b.geo_latitud+"</td>"
                row += "<td>"+b.geo_longitud+"</td>"
                row += "<td>"+b.ip+"</td>"
                row += "<td>"+b.auto+"</td>"
                row += "<td>"+b.auto_modelo+"</td>"
                row += "<td>"+b.auto_tipo+"</td>"
                row += "<td>"+b.auto_color+"</td>"
                row += "<td>"+b.cantidad_compras_realizadas+"</td>"
                row += "<td>"+b.credit_card_num+"</td>"
                row += "<td>"+b.credit_card_ccv+"</td>"
                row += "<td>"+b.color_favorito+"</td>"
                row += "<td>"+b.fec_birthday+"</td>"
                row += "<td><img class='attachment-img' src="+b.avatar+" alt='user Avatar' width='80' height='80'></td>"
                row += "<td><img class='attachment-img' src="+b.foto_dni+" alt='dni photo' width='80' height='80'></td>"

            tbody.append($(row))

        });
    } else {
        $("table").html("No se encontraron resultados.")
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
    url = path
    url += `api/${section_name}/list?page=${page}`;

    if (query){
        query = "&" + query
        url += query
    }
    return url
}

function get_datatable(url){
    sendAjaxRequest(url, "GET", null, null, true)
}



$(document).on("click", ".page-link", function (e) {
    e.preventDefault();
    let url = $(this).attr("data-url");
    
    $('body,html').animate({
        scrollTop: 0
     }, 400);

    get_datatable(url);
})

if (section_name === 'clientes'){
    get_datatable(get_list_url(current_page));
}