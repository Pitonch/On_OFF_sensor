// function sensor_switch(status) {
//     let request_data = {
// csrfmiddlewaretoken: csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]')[0].value
//     }
//
//     $.ajax({
//         url: 'commands/sensor/' + status,
//         type: 'POST',
//         data: request_data,
//         success: function( data ) {
//           // Здесь можно создать проверку на вкл/откл датчика
//         }
//     });
// }

function sensor_switch(status) {
    $.ajax({
        url: 'commands/sensor/' + status,
        type: 'GET',
        success: function( data ) {
          // Здесь можно создать проверку на вкл/откл датчика
        }
    });
}