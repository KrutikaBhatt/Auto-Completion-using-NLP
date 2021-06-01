
$(document).ready(function () {

    $('#sidebarCollapse').on('click', function () {

        $('#sidebar').toggleClass('active');
        const elem = document.getElementById('Toggle-button');
        console.log(elem.className);
        elem.className="fa fa-times";
        console.log(elem.className);
    });


});