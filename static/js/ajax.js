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