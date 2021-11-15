
function predict() {
  console.log('Hello');
  var opt_1=document.getElementById('Email').value;
  var opt_2=document.getElementById('Resident1').value;
  var opt_3=document.getElementById('Religion').value;
  var opt_4=document.querySelector('input[name="Income"]:checked').value;
  console.log(opt_1);
  console.log(opt_2);
  console.log(opt_3);
  console.log(opt_4);
  if (opt_2==7) {
    document.getElementById('output_label').innerHTML='Postive';
    console.log('Postive');
  } else {
    document.getElementById('output_label').innerHTML='Negative';
    console.log('Negative');
  }

}
