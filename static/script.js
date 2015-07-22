
var httpRequest = new XMLHttpRequest();
httpRequest.onreadystatechange = function() {
    if (httpRequest.readyState === 4 
            && httpRequest.status === 200) {
        var json = JSON.parse(httpRequest.responseText);
        createBtns(json.users);
    }
}
httpRequest.open('GET', 'http://localhost:8080/api/users', true);
httpRequest.send(null);

/**
 * Create a button for every user.
 */
function createBtns(users) {
    var cleaning = document.getElementById('cleaning');
  
    for (var i = 0; i < users.length; i++) {
        var button = document.createElement('button');
        button.id = users[i].id;
        button.innerHTML = users[i].name;
        cleaning.appendChild(button);
    }
}
