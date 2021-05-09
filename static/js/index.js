window.onload = function(){
    let description = document.getElementsByName("description_mini")
    for (let i = 0; i < description.length; i ++)
        description[i].innerHTML = description[i].innerHTML.slice(0, 90) + "..."
}