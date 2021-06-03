
$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $('#form_custom_class').toggleClass('active');
        $(this).toggleClass('active');
    });
});