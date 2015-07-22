(function() {

    /**
     * Get the users from the API
     */
    function getUsers() {
        var httpRequest = new XMLHttpRequest();
        httpRequest.onreadystatechange = function() {
            if (httpRequest.readyState === 4 
                    && httpRequest.status === 200) {
                var json = JSON.parse(httpRequest.responseText);
                createBtns(json.users);
                listenOnBtns();
            }
        }

        httpRequest.open('GET', 'http://localhost:8080/api/users', true);
        httpRequest.send(null);
    }


   /**
    * Create a button for every user.
    */
    function createBtns(users) {
        var cleaning = document.getElementById('cleaning');
  
        for (var i = 0; i < users.length; i++) {
            var button = document.createElement('button');
            button.id = users[i].id;
            button.className = 'user-button';
            button.innerHTML = users[i].name;
            cleaning.appendChild(button);
        }
    }


   /**
    * Listen on click events on all user buttons
    */
    function listenOnBtns() {
        var buttons = document.getElementsByClassName('user-button');
        for (var i=0; i < buttons.length; i++) {
            buttons[i].addEventListener("click", function(e) {
                getTask(e.currentTarget.id);
            });
        }
    }


    function getTask(id) {
        var httpRequest = new XMLHttpRequest();
        httpRequest.onreadystatechange = function() {
            if (httpRequest.readyState === 4
                    && httpRequest.status === 200) {
                var json = JSON.parse(httpRequest.responseText);
                console.log(json.task);
            }
        }

        httpRequest.open('GET', 'http://localhost:8080/api/tasks/' + id, true);
        httpRequest.send(null);
    }

    getUsers();

})();
