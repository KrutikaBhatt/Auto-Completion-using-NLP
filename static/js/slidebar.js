
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
      })
});

const spinnerBox = document.getElementById('spinner_box');
const predict_button = document.getElementById('predict_now');

const handleGetData = () => {
  $.ajax({
      type: 'POST',
      url: `/`,
      success: function(response){
          spinnerBox.classList.remove('not-visible')
          setTimeout(()=>{
              spinnerBox.classList.add('visible_spinner')
          }, 2000)
      },
      error: function(error){
          console.log(error)
      }
  })
}

predict_button.addEventListener('click',()=>{
  handleGetData();
})