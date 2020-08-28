<!DOCTYPE html>
<html lang="en">
<head>
  <title>Register</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</head>
<style>
body {
    margin: 0;
    padding: 0;
    height: 100vh;
}

.bg {
  /* The image used */
  background: url("../blue.jpg");

  /* Full height */
  height: 100%; 

  /* Center and scale the image nicely */
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
#RegisterProduct   .container #product-row #product-column #product-box {
  margin-top: 120px;
  max-width: 600px;
  height: 320px;
  border: 1px solid #9C9C9C;
  background-color: #EAEAEA;
}

#RegisterProduct .container #product-row{
    padding: 20px;
}
</style>

<body>
<div class="bg">
    <div id="RegisterProduct">
        <div class="container">
            <div id="product-row" class="row justify-content-center align-items-center">
                <div id="product-col" class="">
                    <form class="form-inline" action="/action_page.php">
                    <label for="email" class="mr-sm-2">Name:</label>
                    <input type="email" class="form-control mb-2 mr-sm-2" placeholder="Enter email" id="email">
                    <label for="pwd" class="mr-sm-2">Brand:</label>
                    <input type="password" class="form-control mb-2 mr-sm-2" placeholder="Enter brand" id="pwd">
                    <div class="form-check mb-2 mr-sm-2">

                    </div>
                    </form>
                    <div class="form-group">
                    <label for="uname">Username:</label>
                    <input type="text" class="form-control" id="uname" placeholder="Enter username" name="uname" required>
                    <div class="valid-feedback">Valid.</div>
                    <div class="invalid-feedback">Please fill out this field.</div>
                    </div>
                    <div class="form-group">
                    <div class="form-group">
                    <label for="uname">Color:</label>
                    <input type="text" class="form-control" id="uname" placeholder="Enter Color" name="uname" required>
                    <div class="valid-feedback">Valid.</div>
                    <div class="invalid-feedback">Please fill out this field.</div>
                    </div>
                    <div class="form-group">
                    <div class="form-group">
                    <label for="uname">Size:</label>
                    <input type="text" class="form-control" id="uname" placeholder="Enter Size" name="uname" required>
                    <div class="valid-feedback">Valid.</div>
                    <div class="invalid-feedback">Please fill out this field.</div>
                    </div>
                    <div class="form-group">
                    <div class="form-group">
                    <label for="uname">Price:</label>
                    <input type="text" class="form-control" id="uname" placeholder="Enter Price" name="uname" required>
                    <div class="valid-feedback">Valid.</div>
                    <div class="invalid-feedback">Please fill out this field.</div>
                    </div>
                    <div class="form-group">
                    <div class="form-group">
                    <label for="uname">No of stocks:</label>
                    <input type="text" class="form-control" id="uname" placeholder="Number" name="uname" required>
                    <div class="valid-feedback">Valid.</div>
                    <div class="invalid-feedback">Please fill out this field.</div>
                    </div>
                    <div class="form-group">
                    <button type="submit" class="btn btn-primary">Submit</button>

            
                </div>
            </div>
        </div>
    </div>
</div>

</body>
</html>