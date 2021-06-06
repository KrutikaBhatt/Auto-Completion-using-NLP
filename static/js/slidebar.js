
$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $('#form_custom_class').toggleClass('active');
        $(this).toggleClass('active');
    });

    $('.btn-plus, .btn-minus').on('click', function(e) {
        const isNegative = $(e.target).closest('.btn-minus').is('.btn-minus');
        const input = $(e.target).closest('.increment_inputs').find('input');
        if (input.is('input')) {
          input[0][isNegative ? 'stepDown' : 'stepUp']()
        }
      });

    $('.predict_now').on('click',function(e){
      const spinnerBox = document.getElementById('spinner_box');
      spinnerBox.classList.remove('not-visible')
      setTimeout(()=>{
          spinnerBox.classList.add('not-visible')
      }, 14000)
     
    });

});
