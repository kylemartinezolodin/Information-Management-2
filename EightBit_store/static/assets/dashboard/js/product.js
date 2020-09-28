
// USED TO PASS <table> DATA TO MODAL
function updateModal(itemId){
    modal_itemId = document.querySelector('#viewId')
    modal_itemId.value = document.querySelector('#itemId-'+itemId).innerHTML

    modal_itemName = document.querySelector('#viewName')
    modal_itemName.value = document.querySelector('#itemName-'+itemId).innerHTML
    
    // FOR SETTING AN <option> TAG WITH "selected" THERE IS NO NEED FOR LOOPED CONDITIONS:
    modal_itemBrand = document.querySelector('#viewType') // GET <select> IN THE MODAL
    modal_itemBrand.value = document.querySelector('#itemType-'+itemId).innerHTML // ASSIGN THE "value" ATTRIBURE OF <select> WITH THE "value" YOU WANT TO BE SELECTED
    // FROM: https://stackoverflow.com/questions/78932/how-do-i-programmatically-set-the-value-of-a-select-box-element-using-javascript

    modal_itemBrand = document.querySelector('#viewBrand')
    modal_itemBrand.value = document.querySelector('#brand-'+itemId).innerHTML

    modal_itemPrice = document.querySelector('#viewPrice')
    // table_price_text HAS '$' INSIDE, WE HAVE TO REMOVE iT 
    table_price_text = document.querySelector('#price-'+itemId).innerHTML
    price_inDecimal = table_price_text.substr(1) // REMOVES '$'
    modal_itemPrice.value = price_inDecimal
}

function deleteModal(itemId) {
    modal_itemId = document.querySelector('#deleteId')
    modal_itemId.value = document.querySelector('#itemId-'+itemId).innerHTML
}

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

setInputFilter(document.getElementById("addPrice"), function(value) {
    return /^-?\d*[.,]?\d{0,2}$/.test(value); // Allow digits and '.' only, using a RegExp and at most two decimal places
});

setInputFilter(document.getElementById("viewPrice"), function(value) {
    return /^-?\d*[.,]?\d{0,2}$/.test(value); // Allow digits and '.' only, using a RegExp and at most two decimal places
});

// FROM: https://stackoverflow.com/questions/469357/html-text-input-allow-only-numeric-input
// ADDITIONAL REGEX HELP HERE: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions