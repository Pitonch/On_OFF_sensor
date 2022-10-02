function switch(status) {
    $.ajax({url: 'commands/sensor/' + status,
        type: 'POST',
        data: request_data,
        success: function( data ) {
          // Здесь можно создать проверку на вкл/откл датчика
        }
    });
}