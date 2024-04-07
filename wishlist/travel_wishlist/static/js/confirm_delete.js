var deleteButtons = document.querySelectorAll('.delete');

deleteButtons.forEach(function(button){

    button.addEventListener('click', function(ev){
        
        // Show a confirm dialog
        var okToDelete = confirm("Delete place - are you sure?");

        // If user presses no, prevent form submit
        if (!okToDelete) {
            ev.preventDefault(); // Prevent the click event propagating
        }

        // Otherwise, the webpage will continue processing. 
    })
});