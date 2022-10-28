$(document).ready(function () {

})

function sensor_switch(event) {
    event.preventDefault();
        $.ajax({
            method : 'GET',
            url: $(this).attr('ip_sensor'),
            data: "",
            dataType: 'json',
            success: (function( data ) {})
    })
}

    $('#click_ON').click(sensor_switch);
    $('#click_OFF').click(sensor_switch);






// function sensor_switch(status) {
//     $.ajax({
//         url: 'commands/sensor/' + status,
//         type: 'GET',
//         success: function( data_ ) {
//           // Здесь можно создать проверку на вкл/откл датчика
//         }
//     });
// }

// function  sensor_switch(status) {
//     let request_data = {
// csrfmiddlewaretoken: csrfmiddlewaretoken, $('input[name=csrfmiddlewaretoken]')[0].value
//     }
//
//     $.ajax({
//         url: 'commands/sensor/' + status,
//         type: 'POST',
//         data_: request_data,
//         success: function( data_ ) {
//           // Здесь можно создать проверку на вкл/откл датчика
//         }
//     });
// }

// $(document).ready(function () {
//
// })
//
// function sensor_switch(event) {
//     event.preventDefault();
//         $.ajax({
//             method : 'GET',
//             url: $(this).attr('ip_sensor'),
//             data_: "",
//             dataType: 'json',
//             success: (function( data_ ) {})
//     })
// }
//
//     $('#click_ON').click(sensor_switch);
//     $('#click_OFF').click(sensor_switch);