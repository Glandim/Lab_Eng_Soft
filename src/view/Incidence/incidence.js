function sendIncidence() {
  var disease = document.getElementById('disease');
  var date = document.getElementById('incidenceDate');

  if (!disease.value || !date.value) {
    !disease.value ? disease.style.border = '2px solid red' : null;
    !date.value ? date.style.border = '2px solid red' : null;
    return null;
  }  

  let obj = { 
    disease: disease.value,
    date: date.value,
  }

  var ajax = new XMLHttpRequest();

  ajax.open("POST", "http://127.0.0.1:5000/incidence/register", true);
  ajax.setRequestHeader("Content-type", "application/json");

  ajax.onload = (e) => {
    var data = JSON.parse(ajax.responseText);
    if (ajax.readyState == 4 && ajax.status == 200) {
        window.location.href = '/';
    } else {
        alert(`Tente novamente: ${data.Erro}`)
    }
  }

  ajax.onerror = (e) => {
    console.error(ajax.statusText);
  }

  ajax.send(JSON.stringify(obj));   
}
