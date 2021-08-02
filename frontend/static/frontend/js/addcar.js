let fileInput1 = document.getElementById("file-upload-front");
let fileSelect1 = document.getElementsByClassName("file-upload-select1")[0];
fileSelect1.onclick = function () {
    fileInput1.click();
}
fileInput1.onchange = function () {
    let filename1 = fileInput1.files[0].name;
    let selectName1 = document.getElementsByClassName("file-select-name1")[0];
    selectName1.innerText = filename1;
}

let fileInput2 = document.getElementById("file-upload-back");
let fileSelect2 = document.getElementsByClassName("file-upload-select2")[0];
fileSelect2.onclick = function () {
    fileInput2.click();
}
fileInput2.onchange = function () {
    let filename2 = fileInput2.files[0].name;
    let selectName2 = document.getElementsByClassName("file-select-name2")[0];
    selectName2.innerText = filename2;
}