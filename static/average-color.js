function addImage(file) {
  var element = document.createElement('div');
  element.className = 'h1';
  element.innerHTML =
    '<div class="cell image">' +
    '  <img />' +
    '</div>';

  var img = element.querySelector('img');
  img.src = URL.createObjectURL(file);

  document.getElementById('images').appendChild(element);
}

function handleImages(files) {
  document.getElementById('images').innerHTML = '';
     addImage(files[0]);  
}

document.ondragover = function(event) {
  event.preventDefault();
  event.dataTransfer.dropEffect = 'copy';
};

document.ondrop = function(event) {
  event.preventDefault();
  handleImages(event.dataTransfer.files);
};

(function() {
  var upload = document.getElementById('upload');
  var target = document.getElementById('target');

  upload.onchange = function() {
    handleImages(this.files);
  };

  target.onclick = function() {
    upload.click();
  };
})();
