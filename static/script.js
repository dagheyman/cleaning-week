console.log("Running js..");

var httpRequest = new XMLHttpRequest();
httpRequest.onreadystatechange = function() {
    if (httpRequest.readyState === 4 
            && httpRequest.status === 200) {
        var json = JSON.parse(httpRequest.responseText);

        console.log(json);
    }
}
httpRequest.open('GET', 'http://localhost:8080/api/users', true);
httpRequest.send(null);


