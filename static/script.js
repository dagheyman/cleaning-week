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
                showTask(json.task);
                console.log(json.task);
            }
        }

        httpRequest.open('GET', 'http://localhost:8080/api/tasks/' + id, true);
        httpRequest.send(null);
    }


    /**
     * The view for showing a specific task
     */
    function showTask(task) {
        
        removeChildren('cleaning');
        var cleaning = document.getElementById('cleaning');
        
        // Create a back button to go back to the main menu.
        var back = document.createElement('a');
        back.href = window.location;
        back.innerHTML = '<<<';
        back.className = 'back-btn';
        cleaning.appendChild(back);
        
        // Element for the task title 
        var title = document.createElement('div'); 
        title.innerHTML = "Titel: " + task.title;
        title.className = 'task-field'; 
        cleaning.appendChild(title);

        // Element for the task description
        var description = document.createElement('div'); 
        description.innerHTML = "Beskrivning: " + task.description;
        description.className = 'task-field';
        cleaning.appendChild(description);
        
        // Element for the task status
        var statusString = task.status ? "Klar" : "Ej klar";
        var status = document.createElement('div');
        status.className = 'task-field';
        status.innerHTML = "Klar: " + statusString;
        cleaning.appendChild(status);
    }


    /**
     * Remove all DOM children for an element.
     */
    function removeChildren(elementId) {
        var element = document.getElementById(elementId);
        while (element.firstChild) {
            element.removeChild(element.firstChild);
        }
    }


    getUsers();

})();
