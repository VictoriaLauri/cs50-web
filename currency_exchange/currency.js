import Freecurrencyapi from '@everapi/freecurrencyapi-js';

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').onsubmit = function() {

        // Send a GET request to the URL
        const freecurrencyapi = new Freecurrencyapi('fca_live_cWPEp1EI4bXlYJXT1PpZvrQ1MyjtG47yL9hmhzN3');
        // Put response into json form
        .then(response => response.json())
        .then(data => {
            // Get currency from user input and convert to upper case
            document.querySelector('#result').innerHTML = outputElement.textContent = JSON.stringify(data, null, 2);
        });
        // Prevent default submission
        return false;
    }
});