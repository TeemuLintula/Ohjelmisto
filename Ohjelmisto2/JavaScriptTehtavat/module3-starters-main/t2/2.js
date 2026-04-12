const target = document.getElementById("target");

const li1 = document.createElement('li');
li1.appendChild(document.createTextNode('First item'));
const li2 = document.createElement('li');
li2.appendChild(document.createTextNode('Second  item'));
const li3 = document.createElement('li');
li3.appendChild(document.createTextNode('Third  item'));

target.appendChild(li1);
target.appendChild(li2);
target.appendChild(li3);

li2.classList.add("my-item")