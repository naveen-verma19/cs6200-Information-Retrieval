document.querySelector('input[name="gender"]:checked').value;

document.querySelectorAll(".search-box")[0].value = "Fukushima";
$(".search-box").dispatchEvent(new Event("change"));
