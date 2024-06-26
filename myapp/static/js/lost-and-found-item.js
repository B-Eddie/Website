function debounce(func, wait, immediate) {
  let timeout;
  return function() {
    const context = this;
    const args = arguments;
    const later = function() {
      timeout = null;
      if (!immediate) func.apply(context, args);
    };
    const callNow = immediate && !timeout;
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
    if (callNow) func.apply(context, args);
  };
}


const apiKey = '0a3cfc11ac124345a8bdfc860029cbd2';
const inputField = document.getElementById('locationInput');

inputField.addEventListener('input', debounce(function() {
    const query = inputField.value;
    fetch(`https://api.opencagedata.com/geocode/v1/json?q=${query}&key=${apiKey}&types=address`)
        .then(response => response.json())
        .then(data => {
            const filteredSuggestions = data.results.filter(result => {
                // Check if 'components' includes 'road', indicating a street-level address
                return result.components && result.components.road;
            });

            const suggestions = filteredSuggestions.map(result => result.formatted);
            document.getElementById("locationDropDown").innerHTML = "";
            if (suggestions !== null) {
                suggestions.forEach(function(e) {
                    const option = document.createElement("h6");
                    option.textContent = e;
                    document.getElementById("locationDropDown").appendChild(option);

                    option.addEventListener("click", function() {
                        locationInput.value = e;
                        document.getElementById("locationDropDown").innerHTML = "";
                    });
                });
            }
        })
        .catch(error => {
            console.error(error);
        });
}, 300));


document.getElementById("logoImage").addEventListener("click", function() {
    window.location.href = "/";
});