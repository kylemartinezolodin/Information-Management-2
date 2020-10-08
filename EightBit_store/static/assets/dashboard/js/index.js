document.querySelector('#orderForm').reset()

function check() {
    console.log("called: check()");
    select_value = document.querySelector('#existingCustomer').value
    amount_value = document.getElementsByName('amount')[0].value
    lastName_value = document.getElementsByName('lastname')[0].value

    // CHECK NECESSARY INPUT-FIELD, TOGGLE CLICKABLE FOR #orderBtn
    if((select_value != "null" || lastName_value != "") && amount_value != "")
        document.querySelector('#orderBtn').removeAttribute('disabled')
    else
        document.querySelector('#orderBtn').setAttribute('disabled', '')

    // CHECK IF THERE ARE ANY ORDEDRED ITEMS, TOGGLE VISIBILITY OF #no-items-message
    if(itemQuantity_arr.length != 0)
        document.querySelector('#no-items-message').setAttribute("hidden", "true")
    else
        document.querySelector('#no-items-message').removeAttribute('hidden')

    // CHECK IF addOrderModal IS IN A CERTAIN HEIGHT, TOGGLE SCROLL FOR #order-items-table
    modal_height = document.querySelector('#addOrderModal-content').offsetHeight
    if(modal_height > 677)
        document.querySelector('#order-items-table').classList.add('order-items-table_scroll')
    else
        document.querySelector('#order-items-table').classList.remove('order-items-table_scroll')
}

function toggleCustomer() {
    console.log("called: toggleCustomer()");
    existing_customers = document.querySelector('#existingCustomer'); 

    // IF existing_customers-element HAS disabled-property  
    if(existing_customers.disabled == true){
        // REMOVE disabled-property
        existing_customers.disabled = false;

        // REMOVE required-property IN CUSTOMER'S FORM
        document.getElementsByName('firstname')[0].removeAttribute('required')
        document.getElementsByName('lastname')[0].removeAttribute('required')
        document.getElementsByName('email')[0].removeAttribute('required')
        document.getElementsByName('contactNumber')[0].removeAttribute('required')

        // RESET FIELDS
        document.getElementsByName('firstname')[0].value = null
        document.getElementsByName('lastname')[0].value = null
        document.getElementsByName('email')[0].value = null
        document.getElementsByName('contactNumber')[0].value = null

    }
    else{
        // ADD disabled-property
        existing_customers.disabled = true;
        
        // DESELECT ANY EXISTING CUSTOMER
        document.querySelector('#customer-none').selected = true;

        // ADD required-property IN CUSTOMER'S FORM
        document.getElementsByName('firstname')[0].setAttribute('required', '')
        document.getElementsByName('lastname')[0].setAttribute('required', '')
        document.getElementsByName('email')[0].setAttribute('required', '')
        document.getElementsByName('contactNumber')[0].setAttribute('required', '')

        
    }
    // APPLYING INTERVAL IS NECCESARRY FOR ACTIVATING SCROLL FOR #order-items-table, TRY PUTTING check() OUTSIDE
    setTimeout(function(){
        check() // existing_customers(<select>) WILL BE RESETED SO DISABLE THE SUBMIT BUTTON
    }, 250) // 0.25 SECONDS
}

var itemQuantity_arr = [] // ARRAY FOR STORING CARTED ITEMS
function addToTable(id){
    row = document.querySelector("#item-" +id)
    if(row == null){ // IF row-element(#item-id) DOES NOT EXIST
        // INITIALIZE THE ROW
        row = document.createElement("tr");
        row.setAttribute('id', 'item-' +id)

        // INITIALIZE THE DATA-CELLS
        name_cell = document.createElement("td")
        quantity_cell = document.createElement("td")
        price_cell = document.createElement("td")

        // INITIALIZE THE ACTION CELL
        action_cell = document.createElement("td")
        
        // NAME-BLOCK
        name_cell.innerHTML = document.querySelector("#itemName-" +id).innerHTML;
        row.appendChild(name_cell)

        // QUANTITY-BLOCK
        quantity = +document.querySelector("#addQuantity").value // THE + IS AN UNARY OPERATOR IN JAVA THAT CAN CONVERT STRINGS TO INT FROM:https://stackoverflow.com/questions/8976627/how-to-add-two-strings-as-if-they-were-numbers/8976770#8976770
        document.querySelector("#addQuantity").setValue(1) // RESET SPINNER BACK TO 1 
        quantity_cell.innerHTML = quantity
        quantity_cell.setAttribute('id', 'quantity-' +id)
        row.appendChild(quantity_cell)

        // PRICE-BLOCK
        item_price = +document.querySelector("#price-" +id).innerHTML // THE + IS AN UNARY OPERATOR IN JAVA THAT CAN CONVERT STRINGS TO INT FROM:https://stackoverflow.com/questions/8976627/how-to-add-two-strings-as-if-they-were-numbers/8976770#8976770
        item_price = item_price * 100 // SCALING UP THE DECIMAL-VALUE (NUMBERS WITH 2 DECIMAL PLACES) WILL AVOID JAVASCRIPT PRECISION PROBLEMS I.E.(0.2 + 0.1 == 3.000004)

        amount = +document.getElementsByName('amount')[0].value
        amount = amount * 100 // SCALING UP THE DECIMAL-VALUE (NUMBERS WITH 2 DECIMAL PLACES) WILL AVOID JAVASCRIPT PRECISION PROBLEMS I.E.(0.2 + 0.1 == 3.000004)

        document.getElementsByName('amount')[0].value = (amount + (item_price * quantity)) * 0.01 // DON'T FORGET TO SCALE DOWN AFTER ARITHMETIC
        price_cell.innerHTML = "$" +(item_price * 0.01) // SCALE DOWN
        price_cell.setAttribute('id', 'ordered-price-' +id)
        row.appendChild(price_cell)

        // ACTION-BLOCK
        action_cell.innerHTML = "<button type='button' class='close' aria-label='Close'><span aria-hidden='true' onclick='removeRow(" +id +")'>&times;</span></button>"
        row.appendChild(action_cell)
        
        // APPEND HIDDEN-FIELDS TO row-element
        row.innerHTML += "<input type='hidden' name='itemId[]' value='" +id +"'>"
        row.innerHTML += "<input type='hidden' id='itemQuantity-" +id +"' name='itemQuantity[]' value='" +quantity +"'>"
        
        // APPEND THE row-object TO THE <tbody>
        document.querySelector('#ordered-table-body').appendChild(row)
        // document.querySelector('#idList').value += id


    }
    else{ // IF row-element(#item-id) DOES ALREADY EXIST
        quantity = +document.querySelector("#addQuantity").value
        item_price = +document.querySelector("#price-" +id).innerHTML
        item_price = item_price * 100 // SCALING UP THE DECIMAL-VALUE (NUMBERS WITH 2 DECIMAL PLACES) WILL AVOID JAVASCRIPT PRECISION PROBLEMS I.E.(0.2 + 0.1 == 3.000004)

        amount = +document.getElementsByName('amount')[0].value
        amount = amount * 100 // SCALING UP THE DECIMAL-VALUE (NUMBERS WITH 2 DECIMAL PLACES) WILL AVOID JAVASCRIPT PRECISION PROBLEMS I.E.(0.2 + 0.1 == 3.000004)

        document.getElementsByName('amount')[0].value = (amount + (item_price * quantity)) * 0.01 // SCALE DOWN AND UPDATE THE amount-element
        document.querySelector("#quantity-" +id).innerHTML = +document.querySelector("#quantity-" +id).innerHTML + quantity // INCREMENT THE quantity-id-element(#quantity-id)
        document.querySelector("#itemQuantity-" +id).value = +document.querySelector("#quantity-" +id).innerHTML // INCREMENT THE hidden-quantity-input(#itemQuantity-id)

    }
    
    // STORE ITEMS IN AN 2D ARRAY BLOCK
    alreadyExist_flag = false // THIS WILL HELP MAKING INCREMENTS INSTEAD OF DUPLICATIONS 
    itemQuantity_arr.forEach(item => {
        if (item[0] == id) { // item[0] IS itemId
            alreadyExist_flag = true
            item[1] += quantity // item[1] IS quantity
        }
    });

    if(alreadyExist_flag == false){
        itemQuantity_arr[itemQuantity_arr.length] = [id, quantity]
    }

    document.getElementsByName("numberOfItems")[0].value = +document.getElementsByName("numberOfItems")[0].value + 1// INCREMENT hidden-numberOfItems-input

    check() // CALL check() TO CHECK IF FORM CAN BE SUBMITED
}

function removeRow(id) {
    quantity = +document.querySelector("#quantity-" +id).innerHTML // THE + IS AN UNARY OPERATOR IN JAVA THAT CAN CONVERT STRINGS TO INT FROM:https://stackoverflow.com/questions/8976627/how-to-add-two-strings-as-if-they-were-numbers/8976770#8976770
    price = +document.querySelector("#ordered-price-" +id).innerHTML.substr(1) // substr(1) REMOVES THE $ SIGN
    price *= 100
    // itemQuantity_arr.forEach(item => {
    //     if (item[0] == id) { // item[0] IS itemId
    //         item[1] -= quantity // item[1] IS quantity

    //     }
    // });
    for (let i = 0; i < itemQuantity_arr.length; i++) {
        if(itemQuantity_arr[i][0] == id){ // itemQuantity_arr[i][0] IS itemId
            itemQuantity_arr[i][1] -= quantity // itemQuantity_arr[i][1] IS quantity

            if(itemQuantity_arr[i][1] == 0)
                itemQuantity_arr.splice(i, 1)
        }
    }

    amount = +document.getElementsByName('amount')[0].value
    amount *= 100
    amount = (amount - (price * quantity)) / 100
    document.getElementsByName('amount')[0].value = amount
    console.log(amount - (price * quantity));
    
    if(amount < 1)
        document.getElementsByName('amount')[0].value = null

    document.querySelector("#item-" +id).remove()

    document.getElementsByName("numberOfItems")[0].value = +document.getElementsByName("numberOfItems")[0].value - 1// DECREMENT hidden-numberOfItems-input

    check() // CALL check() TO CHECK IF FORM CAN'T BE SUBMITED
}

function submitForm(){
    // THE FIELDS THAT WILL BE PASSED TO $_POST
    hidden_itemId = document.createElement("input")
    hidden_itemId.setAttribute('type', 'hidden')
    hidden_itemId.setAttribute('name', 'item[' +item_arr_index +'][0]')
    hidden_itemId.setAttribute('value', id)
    row.appendChild(hidden_itemId)

    // document.querySelector('#orderForm').submit()
}

function wew(){
    var xhr = new XMLHttpRequest();
    xhr.open("POST", '', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        value: "we"
    }));
}

function deleteOrder(id) {
    document.querySelector('#deleteOrderField').value = id
}

function deleteOrdered(id) {
    document.querySelector('#deleteOrderedField').value = id
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

setInputFilter(document.getElementById("amountField"), function(value) {
    return /^-?\d*[.,]?\d{0,2}$/.test(value); // Allow digits and '.' only, using a RegExp and at most two decimal places
});
// FROM: https://stackoverflow.com/questions/469357/html-text-input-allow-only-numeric-input
// ADDITIONAL REGEX HELP HERE: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions