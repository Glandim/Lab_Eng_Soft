function registerDisease() {
  var diseaseName = document.getElementById('form-input-name');
  var diseaseDescription = document.getElementById('form-input-description');

  if (!diseaseName.value || !diseaseDescription.value) {
      !diseaseName.value ? diseaseName.style.border = '2px solid red' : null;
      !diseaseDescription.value ? diseaseDescription.style.border = '2px solid red' : null;
      return null;
  }  

  let obj = { 
      name: diseaseName.value,
      symptoms: diseaseDescription.value,
  }

  var ajax = new XMLHttpRequest();
  ajax.open("POST", "http://127.0.0.1:5000/disease/register", true);
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
