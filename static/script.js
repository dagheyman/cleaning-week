(function() {

    /**
     * This is how we can get the current week in JS
     */
    Date.prototype.getWeek = function() {
        var date = new Date(this.getTime());   
        date.setHours(0, 0, 0, 0); 
        // Thursday in current week decides the year. 
        date.setDate(date.getDate() + 3 - (date.getDay() + 6) % 7); 
        // January 4 is always in week 1. 
        var week1 = new Date(date.getFullYear(), 0, 4); 
       // Adjust to Thursday in week 1 and count number of weeks from date to week1. 
       return 1 + Math.round(((date.getTime() - week1.getTime()) / 86400000 - 3 + (week1.getDay() + 6) % 7) / 7);   
    }


    /**
     * Make the back button work
     */
    window.onhashchange = function() {
        if (window.location.hash === "") {
            removeChildren('cleaning');
            getUsers();
        }
    }
    
    /**
     * Entry point
     */
    
    window.onload = function() {
        getUsers();
        printCurrentWeek();
    }

    function printCurrentWeek() {
        var currentWeek = document.getElementById('current-week');
        currentWeek.innerHTML = 'Vecka: ' + (new Date()).getWeek();
    }    

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


    /**
     * Get the task for a specific user for the current week
     */
    function getTask(userId) {
        var httpRequest = new XMLHttpRequest();
        httpRequest.onreadystatechange = function() {
            if (httpRequest.readyState === 4
                    && httpRequest.status === 200) {
                var json = JSON.parse(httpRequest.responseText);
                showTask(json.task, userId);
            }
        }

        httpRequest.open('GET', 'http://localhost:8080/api/tasks/' + userId, true);
        httpRequest.send(null);
    }


    /**
     * The view for showing a specific task
     */
    function showTask(task, userId) {
        window.location.hash = userId;

        removeChildren('cleaning');
        var cleaning = document.getElementById('cleaning');
        
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

        // A complete button if task is not completed
        if (!task.status) {
            var completeBtn = document.createElement('button');
            completeBtn.className = 'complete-button';
            completeBtn.innerHTML = 'Jag är klar!';
            completeBtn.id = 'complete-button';
            cleaning.appendChild(completeBtn);
        
            listenOnCompleteBtn(completeBtn.id, userId, task.id);
        }
    }


    /**
     * Listen on the complete button
     */
    function listenOnCompleteBtn(buttonId, userId, taskId) {
        var completeBtn = document.getElementById(buttonId);
        completeBtn.addEventListener("click", function(e) {
            completeTask(userId, taskId);
        });
    }


    /**
     * Complete a task for a user this week
     */
    function completeTask(userId, taskId) {
        var httpRequest = new XMLHttpRequest();
        httpRequest.onreadystatechange = function() {
            if (httpRequest.readyState === 4
                    && httpRequest.status === 200) {
                getTask(userId);
            }
        }

        httpRequest.open(
                'POST', 'http://localhost:8080/api/tasks/' + userId + '/' + taskId + '/complete', true);
        httpRequest.send(null);
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

})();
