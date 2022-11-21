inputs = document.querySelectorAll('input');
inputs_textarea = document.querySelectorAll('textarea');

for (var i = 0; i < inputs.length; i++) {
    inputs[i].classList.add('form-control');
}

for (var i = 0; i < inputs_textarea.length; i++) {
    inputs_textarea[i].classList.add('form-control');
}

select = document.querySelector('select')

select.classList.add('form-control')

divs = document.getElementsByClassName("form_element")
for (var d = 0; d < divs.length; d++) {
    divs[d].classList.add('mb-3')
}

checkboxex = document.querySelectorAll('input[type="checkbox"]')
for (var d = 0; d < checkboxex.length; d++) {
    checkboxex[d].classList.remove('form-control')
}


function replyTo(id) {
    let element = document.querySelector('#id_reply')
    element.value = id;
}
