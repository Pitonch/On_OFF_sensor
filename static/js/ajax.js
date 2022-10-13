 $("document").ready(function () {
         function sensor_switch(status) {
            $.ajax({
            url: 'commands/<ip_sensor>/' ,
            type: 'GET',
            success: function( data ) {}
            })
         }
 })




