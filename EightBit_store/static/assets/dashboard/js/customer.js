// Restricts input for the given textbox to the given inputFilter function.
function setInputFilter(textbox, inputFilter) {
    ["input", "keydown", "keyup", "mousedown", "mouseup", "select", "contextmenu", "drop"].forEach(function(event) {
      textbox.addEventListener(event, function() {
        if (inputFilter(this.value)) {
          this.oldValue = this.value;
          this.oldSelectionStart = this.selectionStart;
          this.oldSelectionEnd = this.selectionEnd;
        } else if (this.hasOwnProperty("oldValue")) {
          this.value = this.oldValue;
          this.setSelectionRange(this.oldSelectionStart, this.oldSelectionEnd);
        } else {
          this.value = "";
        }
      });
    });
  }

setInputFilter(document.getElementById("addNumber"), function(value) {
    return /^\d*$/.test(value); // Allow positive digits only using a RegExp
});

// FROM: https://stackoverflow.com/questions/469357/html-text-input-allow-only-numeric-input
// ADDITIONAL REGEX HELP HERE: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions