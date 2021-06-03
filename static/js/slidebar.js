
$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $('#form_custom_class').toggleClass('active');
        $(this).toggleClass('active');
    });

    $('#plus_button').on('click',function(){
        var value = document.getElementById("k-smooth-input").value;
        value = parseFloat(value);
        if(value<=1.00){
            value = value+0.01;
            value = Math.round(value * 100) / 100;
            document.getElementById("k-smooth-input").value = value;
        }
        else if(value == undefined || isNaN(value) == true || value <= 0){
            document.getElementById("k-smooth-input").value = "0.01";
        }
        else{
            document.getElementById("k-smooth-input").value = value;
        }
    });

    $('#minus_button').on('click',function(){
        var value = document.getElementById("k-smooth-input").value;
        value = parseFloat(value);
        if(value>0.01){
            value = value-0.01;
            value = Number((value).toFixed(2))
            document.getElementById("k-smooth-input").value = value;
        }
        else if(value == undefined || isNaN(value) == true || value <= 0){
            document.getElementById("k-smooth-input").value = "0.01";
        }
        else{
            document.getElementById("k-smooth-input").value = value;
        }
    });

});

