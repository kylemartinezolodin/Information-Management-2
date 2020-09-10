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
</head>
  <body>
    <nav class="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0">
      <a class="navbar-brand col-sm-3 col-md-2 mr-0" href="#">Olodin's PC shop</a>
      <input class="form-control form-control-dark w-100" type="text" placeholder="Search" aria-label="Search">
      <ul class="navbar-nav px-3">
        <li class="nav-item text-nowrap">
          <a class="nav-link" href="#">Sign out</a>
        </li>
      </ul>
    </nav>

    <div class="container-fluid">
      <div class="row">
        <nav class="col-md-2 d-none d-md-block bg-light sidebar">
          <div class="sidebar-sticky">
            <ul class="nav flex-column">
              <li class="nav-item">
                <a class="nav-link active" href="#">
                  <span data-feather="home"></span>
                  Dashboard <span class="sr-only">(current)</span>
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">
                  <span data-feather="file"></span>
                  Orders
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">
                  <span data-feather="shopping-cart"></span>
                  Products
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">
                  <span data-feather="users"></span>
                  Customers
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">
                  <span data-feather="bar-chart-2"></span>
                  Reports
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">
                  <span data-feather="layers"></span>
                  Integrations
                </a>
              </li>
            </ul>

            <h6 class="sidebar-heading d-flex justify-content-between align-items-center px-3 mt-4 mb-1 text-muted">
              <span>Saved reports</span>
              <a class="d-flex align-items-center text-muted" href="#">
                <span data-feather="plus-circle"></span>
              </a>
            </h6>
            <ul class="nav flex-column mb-2">
              <li class="nav-item">
                <a class="nav-link" href="#">
                  <span data-feather="file-text"></span>
                  Current month
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">
                  <span data-feather="file-text"></span>
                  Last quarter
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">
                  <span data-feather="file-text"></span>
                  Social engagement
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">
                  <span data-feather="file-text"></span>
                  Year-end sale
                </a>
              </li>
            </ul>
          </div>
        </nav>

        <main role="main" class="col-md-9 ml-sm-auto col-lg-10 pt-3 px-4">
          <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pb-2 mb-3 border-bottom">
            <h1 class="h2">Dashboard</h1>
            <div class="btn-toolbar mb-2 mb-md-0">
              <div class="btn-group mr-2">
                <button class="btn btn-sm btn-primary pl-3 pr-3">Add Order</button>
                <!-- <button class="btn btn-sm btn-outline-secondary">Share</button> -->
                <!-- <button class="btn btn-sm btn-outline-secondary">Export</button> -->
              </div>
              <button class="btn btn-sm btn-outline-secondary dropdown-toggle">
                <span data-feather="calendar"></span>
                This week
              </button>
            </div>
          </div>

          <!-- <canvas class="my-4" id="myChart" width="900" height="380"></canvas> -->
          <img class="widget-concept" src="assets\dashboard\images\widgets_concept.png">
          <h2>Customer Report Summary</h2>
          <div class="table-responsive">
            <!-- <table class="table table-striped table-sm"> -->
            <table id="mydatatable" class="display">
              <thead>
                <tr>
                  <th>Order Id</th>
                  <th>Date</th>
                  <th>Item</th>
                  <th>Quantity</th>
                  <th>Customer Name</th>
                  <th>Amount</th>
                  <th>Option</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>CID310</td>
                  <td>11/09/2020</td>
                  <td>RAM - Kingston 8Gb DDR4</td>
                  <td>15</td>
                  <td>Delor Ann Doc</td>
                  <td>$657</td>
                  <td>
                    <button type="button" class="btn btn-sm btn-outline-secondary" data-toggle="modal" data-target="#viewModal">
                      View
                    </button>
                    <button type="button" class="btn btn-sm btn-danger" data-toggle="modal" data-target="#deleteModal">
                      Delete
                    </button>
                  </td>
                </tr>
                <tr>
                  <td>GHD461</td>
                  <td>11/09/2020</td>
                  <td>CPU - AMD 3500xt</td>
                  <td>10</td>
                  <td>James Bondini</td>
                  <td>$1450</td>
                  <td>
                    <button type="button" class="btn btn-sm btn-outline-secondary" data-toggle="modal" data-target="#viewModal">
                      View
                    </button>
                    <button type="button" class="btn btn-sm btn-danger" data-toggle="modal" data-target="#deleteModal">
                      Delete
                    </button>
                  </td>
                </tr>
                <tr>
                  <td>GHD456</td>
                  <td>11/09/2020</td>
                  <td>CPU - Intel i7 10115k</td>
                  <td>6</td>
                  <td>Gucci Prado</td>
                  <td>$2562</td>
                  <td>
                    <button type="button" class="btn btn-sm btn-outline-secondary" data-toggle="modal" data-target="#viewModal">
                      View
                    </button>
                    <button type="button" class="btn btn-sm btn-danger" data-toggle="modal" data-target="#deleteModal">
                      Delete
                    </button>
                  </td>
                </tr>
                <tr>
                  <td>CID754</td>
                  <td>11/09/2020</td>
                  <td>TV - Samsung 67" 4k OLED </td>
                  <td>2</td>
                  <td>Ngigga Kiga</td>
                  <td>$4755</td>
                  <td>
                    <button type="button" class="btn btn-sm btn-outline-secondary" data-toggle="modal" data-target="#viewModal">
                      View
                    </button>
                    <button type="button" class="btn btn-sm btn-danger" data-toggle="modal" data-target="#deleteModal">
                      Delete
                    </button>
                  </td>
                </tr>
                <tr>
                  <td>CID674</td>
                  <td>05/09/2020</td>
                  <td>GPU - NVIDIA GTX 3090</td>
                  <td>1</td>
                  <td>Toni Gacchalan</td>
                  <td>$480</td>
                  <td>
                    <button type="button" class="btn btn-sm btn-outline-secondary" data-toggle="modal" data-target="#viewModal">
                      View
                    </button>
                    <button type="button" class="btn btn-sm btn-danger" data-toggle="modal" data-target="#deleteModal">
                      Delete
                    </button>
                  </td>
                </tr>
                <tr>
                  <td>CID299</td>
                  <td>05/09/2020</td>
                  <td>Printer - Canon Laser Print</td>
                  <td>10</td>
                  <td>Toni David</td>
                  <td>$5460</td>
                  <td>
                    <button type="button" class="btn btn-sm btn-outline-secondary" data-toggle="modal" data-target="#viewModal">
                      View
                    </button>
                    <button type="button" class="btn btn-sm btn-danger" data-toggle="modal" data-target="#deleteModal">
                      Delete
                    </button>
                  </td>
                </tr>
                <tr>
                  <td>AZD480</td>
                  <td>05/09/2020</td>
                  <td>GPU - NVIDA GTX 2080 Founders Edition</td>
                  <td>5</td>
                  <td>Duis Drax</td>
                  <td>$5755</td>
                  <td>
                    <button type="button" class="btn btn-sm btn-outline-secondary" data-toggle="modal" data-target="#viewModal">
                      View
                    </button>
                    <button type="button" class="btn btn-sm btn-danger" data-toggle="modal" data-target="#deleteModal">
                      Delete
                    </button>
                  </td>
                </tr>
                <tr>
                  <td>AZD689</td>
                  <td>04/09/2020</td>
                  <td>Laptop - Acer BLK-261</td>
                  <td>1</td>
                  <td>D're Mon</td>
                  <td>$680</td>
                  <td>
                    <button type="button" class="btn btn-sm btn-outline-secondary" data-toggle="modal" data-target="#viewModal">
                      View
                    </button>
                    <button type="button" class="btn btn-sm btn-danger" data-toggle="modal" data-target="#deleteModal">
                      Delete
                    </button>
                  </td>
                </tr>
                <tr>
                  <td>CID309</td>
                  <td>11/09/2020</td>
                  <td>Laptop - Alienware XT</td>
                  <td>2</td>
                  <td>James Did</td>
                  <td>$4945</td>
                  <td>
                    <button type="button" class="btn btn-sm btn-outline-secondary" data-toggle="modal" data-target="#viewModal">
                      View
                    </button>
                    <button type="button" class="btn btn-sm btn-danger" data-toggle="modal" data-target="#deleteModal">
                      Delete
                    </button>
                  </td>
                </tr>
                <tr>
                  <td>AZD758</td>
                  <td>04/09/2020</td>
                  <td>Mobile Phone - Cherry Mobile</td>
                  <td>15</td>
                  <td>Bags Bonni</td>
                  <td>$958</td>
                  <td>
                    <button type="button" class="btn btn-sm btn-outline-secondary" data-toggle="modal" data-target="#viewModal">
                      View
                    </button>
                    <button type="button" class="btn btn-sm btn-danger" data-toggle="modal" data-target="#deleteModal">
                      Delete
                    </button>
                  </td>
                </tr>
                <tr>
                  <td>AZD811</td>
                  <td>04/09/2020</td>
                  <td>Vestibulum</td>
                  <td>lacinia</td>
                  <td>arcu</td>
                  <td>$4755</td>
                  <td>
                    <button type="button" class="btn btn-sm btn-outline-secondary" data-toggle="modal" data-target="#viewModal">
                      View
                    </button>
                    <button type="button" class="btn btn-sm btn-danger" data-toggle="modal" data-target="#deleteModal">
                      Delete
                    </button>
                  </td>
                </tr>
                <tr>
                  <td>AZD800</td>
                  <td>04/09/2020</td>
                  <td>nulla</td>
                  <td>Class</td>
                  <td>aptent</td>
                  <td>$4755</td>
                  <td>
                    <button type="button" class="btn btn-sm btn-outline-secondary" data-toggle="modal" data-target="#viewModal">
                      View
                    </button>
                    <button type="button" class="btn btn-sm btn-danger" data-toggle="modal" data-target="#deleteModal">
                      Delete
                    </button>
                  </td>
                </tr>
                <tr>
                  <td>AZD809</td>
                  <td>04/09/2020</td>
                  <td>sociosqu</td>
                  <td>ad</td>
                  <td>litora</td>
                  <td>$4755</td>
                  <td>
                    <button type="button" class="btn btn-sm btn-outline-secondary" data-toggle="modal" data-target="#viewModal">
                      View
                    </button>
                    <button type="button" class="btn btn-sm btn-danger" data-toggle="modal" data-target="#deleteModal">
                      Delete
                    </button>
                  </td>
                </tr>
                <tr>
                  <td>ACD095</td>
                  <td>01/09/2020</td>
                  <td>per</td>
                  <td>conubia</td>
                  <td>nostra</td>
                  <td>$4755</td>
                  <td>
                    <button type="button" class="btn btn-sm btn-outline-secondary" data-toggle="modal" data-target="#viewModal">
                      View
                    </button>
                    <button type="button" class="btn btn-sm btn-danger" data-toggle="modal" data-target="#deleteModal">
                      Delete
                    </button>
                  </td>
                </tr>
                <tr>
                  <td>ACD090</td>
                  <td>01/09/2020</td>
                  <td>inceptos</td>
                  <td>himenaeos</td>
                  <td>Curabitur</td>
                  <td>$4755</td>
                  <td>
                    <button type="button" class="btn btn-sm btn-outline-secondary" data-toggle="modal" data-target="#viewModal">
                      View
                    </button>
                    <button type="button" class="btn btn-sm btn-danger" data-toggle="modal" data-target="#deleteModal">
                      Delete
                    </button>
                  </td>
                </tr>
                <tr>
                  <td>ACD098</td>
                  <td>01/09/2020</td>
                  <td>ligula</td>
                  <td>in</td>
                  <td>libero</td>
                  <td>$4755</td>
                  <td>
                    <button type="button" class="btn btn-sm btn-outline-secondary" data-toggle="modal" data-target="#viewModal">
                      View
                    </button>
                    <button type="button" class="btn btn-sm btn-danger" data-toggle="modal" data-target="#deleteModal">
                      Delete
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </main>
      </div>
    </div>

    <!-- View Dialog/Modal -->
    <div class="modal fade" id="viewModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLongTitle">Delete</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <input type = "text" placeholder="Order Id">
            <input type = "text" placeholder="Date">
            <input type = "text" placeholder="Item">
            <input type = "text" placeholder="Quantity">
            <input type = "text" placeholder="Customer Name">
            <input type = "text" placeholder="Amount">
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-success">Update</button>
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Delete Dialog/Modal -->
    <div class="modal fade" id="deleteModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLongTitle">Delete</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            Are you sure you want to delete this record?
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-danger">Delete</button>
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>

  </body>

  <script src="assets/dashboard/js/jquery-3.5.1.js"></script>
  <script src="assets/js/popper.min.js"></script>
  <script src="assets/js/bootstrap.min.js"></script>

  <!-- DATATABLE JS -->
  <!-- <script type="text/javascript" src="https://cdn.datatables.net/v/dt/jszip-2.5.0/dt-1.10.21/af-2.3.5/b-1.6.3/b-colvis-1.6.3/b-html5-1.6.3/r-2.2.5/sp-1.1.1/datatables.js"></script> -->

  <script type="text/javascript" src="assets/dashboard/vendor/datatables/JSZip-2.5.0/jszip.js"></script>
  <script type="text/javascript" src="assets/dashboard/vendor/datatables/DataTables-1.10.21/js/jquery.dataTables.js"></script>
  <script type="text/javascript" src="assets/dashboard/vendor/datatables/AutoFill-2.3.5/js/dataTables.autoFill.js"></script>
  <script type="text/javascript" src="assets/dashboard/vendor/datatables/Buttons-1.6.3/js/dataTables.buttons.js"></script>
  <script type="text/javascript" src="assets/dashboard/vendor/datatables/Buttons-1.6.3/js/buttons.colVis.js"></script>
  <script type="text/javascript" src="assets/dashboard/vendor/datatables/Buttons-1.6.3/js/buttons.html5.js"></script>
  <script type="text/javascript" src="assets/dashboard/vendor/datatables/Responsive-2.2.5/js/dataTables.responsive.js"></script>
  <script type="text/javascript" src="assets/dashboard/vendor/datatables/SearchPanes-1.1.1/js/dataTables.searchPanes.js"></script>
  <script type="text/javascript" src="assets/dashboard/vendor/datatables/Select-1.3.1/js/dataTables.select.js"></script>

  <script type="text/javascript">
   
    // // DataTables Initialization    
    // $(document).ready(function() {
    //     $('#mydatatable').DataTable( {
    //         dom: 'Bfrtip',
    //         buttons: [
    //             'excel'
    //         ]
    //     } );
    // } );
    
    // EXPORT BUTTON BLOCK FROM: https://datatables.net/extensions/buttons/examples/initialisation/plugins
    $.fn.dataTable.ext.buttons.alert = {
        className: 'buttons-alert',
    
        action: function ( e, dt, node, config ) {
            alert( this.text() );
        }
    };
 
    
    $(document).ready(function() {
        $('#mydatatable').DataTable( {
            dom: 'Bfrtip',
            buttons: [
                {
                    extend: 'excel',
                    text: 'Export'
                }
            ]
        } );
    } );
    // END EXPORT BUTTON BLOCK    
  </script>
</html>
