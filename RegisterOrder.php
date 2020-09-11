<!DOCTYPE html>
<html lang="en">
<head>
  <title>Dashboard</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  
  <link rel="stylesheet" href="assets/css/bootstrap.min.css">

  <!-- DATATABLE STYLES -->
  <!-- <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/v/dt/jszip-2.5.0/dt-1.10.21/af-2.3.5/b-1.6.3/b-colvis-1.6.3/b-html5-1.6.3/r-2.2.5/sp-1.1.1/datatables.css"/> -->
 
  <link rel="stylesheet" type="text/css" href="assets/dashboard/vendor/datatables/DataTables-1.10.21/css/jquery.dataTables.css"/>
  <link rel="stylesheet" type="text/css" href="assets/dashboard/vendor/datatables/AutoFill-2.3.5/css/autoFill.dataTables.min.css"/>
  <link rel="stylesheet" type="text/css" href="assets/dashboard/vendor/datatables/Buttons-1.6.3/css/buttons.dataTables.css"/>
  <link rel="stylesheet" type="text/css" href="assets/dashboard/vendor/datatables/Responsive-2.2.5/css/responsive.dataTables.css"/>
  <link rel="stylesheet" type="text/css" href="assets/dashboard/vendor/datatables/SearchPanes-1.1.1/css/searchPanes.dataTables.css"/>
  <link rel="stylesheet" type="text/css" href="assets/dashboard/vendor/datatables/Select-1.3.1/css/select.dataTables.css"/>
 

  <!-- DEVELOPER'S CUSTOM STYLES -->
  <link rel="stylesheet" href="assets/dashboard/css/dashboard.css">
  <style>
.bg-img {
  /* The image used */
    background-image: url("https://wallpaperaccess.com/full/165496.jpg");

    min-height: 700px;

  /* Center and scale the image nicely */
    background-repeat: no-repeat;
    
    position: relative;
}

input{
    background-color: #f1f1f1;

}

.container {
    position: absolute;
    right: 0;
    margin: 20px;
    max-width: 600px;
    padding: 16px;
    background: linear-gradient(to bottom, rgba(255, 252, 254, 0.1) 0%, rgba(2, 50, 95, 0.9)100%);
    border-radius: 15px;
    color: white;
    min-height: 650px;
}
  </style>
</head>
    <body>
    <div class="wrapper">
        <div class="bg-img">
        <form class="container pt-3 my-3">
            <div class="">
                <h1>Register Order</h1>
            </div>
            <div class="form-group position-relative">
                <label for="inputEmail">Order No.</label>
                <input type="email" class="form-control" id="inputEmail" placeholder="" value="" required>
            </div>
            <div class="form-group position-relative">
                <label for="inputDate">Date</label>
                <input type="Date" class="form-control" id="inputPassword" placeholder="Password" required>
                <label for="Item">Item:</label>
                <input type="text" class="form-control" id="inputItem">
                
            </div>
            <div class="form-group">
                <label for="quantity">Quantity</label>
                <input type="number" class="form-control" id="inputQuantity" required>
            </div>
            <div class="form-group">
                <label for="customerName">Customer</label>
                <input type="text" class="form-control" id="inputName" required>
            </div>
            <div class="form-group">
                <label for="amount">Amount:</label>
                <input type="number" class="form-control" id="inputAmount" required>
            </div>
            <button type="button" class="btn btn-primary">Submit</button>
            
            </button>

        </form>            
        </div>
    </div>
    </body>
</html>