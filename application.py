import logging.handlers

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Handler 
LOG_FILE = '/tmp/sample-app.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1048576, backupCount=5)
handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add Formatter to Handler
handler.setFormatter(formatter)

# add Handler to Logger
logger.addHandler(handler)

welcome = """
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>Mark Retail Warehouse Management System</title>
  <link href="./css/tabs.css" rel="stylesheet" />
  <!--<link href="./css/main.css" rel="stylesheet" />-->
  <!--<link href="./css/font-awesome.min.css" rel="stylesheet" />-->
<!-- Compiled and minified CSS -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

<!-- Compiled and minified JavaScript -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>

  <script src="./js/jquery-1.11.0.min.js"></script>
  <script src="./js/bootstrap.min.js"></script>
  <script src="https://sdk.amazonaws.com/js/aws-sdk-2.481.0.min.js"></script>
  <script src="./js/product.js"></script>
  <script src="./js/demand.js"></script>
  <script src="./js/administrator.js"></script>
  <script src="./js/tabs.js"></script>
</head>
<body>
  <div class="container">
    <div class="row">
      <div class="col-sm-6">
        <h2 style="background-color:rgb(64, 139, 224);color:white;">Mark Retail Warehouse Administration</h2>
      </div>
    </div>
    <div class="tab" style="background-color:rgb(64, 139, 224);color:white;">
      <button class="tablinks" onclick="opencomp(event, 'Products')">Products</button>
      <button class="tablinks" onclick="opencomp(event, 'Demands')">Demands</button>
      <button class="tablinks" onclick="opencomp(event, 'Administrators')">Administrators</button>
    </div>
    <div id="Products" class="tabcontent active">
        <div class="row">
            <div class="col-sm-6">
              <div class="panel panel-primary">
                <div class="panel-heading">
                  Product
                </div>
                <div class="panel-body">
                  <div class="form-group">
                    <label for="Productid">
                      Product id
                    </label>
                    <input type="text"
                          class="form-control"
                          id="Productid" />
                  </div>
                
                    <div class="form-group">
                      <label for="Productname">
                        Product Name 2
                      </label>
                      <input type="text"
                            class="form-control"
                            id="Productname" />
                    </div>
                    
                      <div class="form-group">
                        <label for="ProductSKU">
                          Product SKU
                        </label>
                        <input type="text"
                              class="form-control"
                              id="ProductSKU" />
                      </div>
                  
                        <div class="form-group">
                          <label for="Productweight">
                            Product Weight
                          </label>
                          <input type="text"
                                class="form-control"
                                id="Productweight" />
                        </div>
    
                </div>
                <div class="panel-footer">
                  <div class="row">
                    <div class="col-xs-12">
                      <button type="button" id="updateButton" style="background-color:rgb(64, 139, 224);"
                              class="btn btn-primary"
                              onclick="addProduct();">
                        Add
                      </button>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-sm-6">
                    <table id="ProductTable"
                          class="table table-bordered table-condensed table-striped">
                      <thead>
                        <tr>
                          <th>id</th>
                          <th>Name</th>
                          <th>SKUs</th>
                          <th>Weight</th>
                        </tr>
                      </thead>
                    </table>
                  </div>
                </div>
          </div>
        </div>
      </div>
    </div>
    <div id="Demands" class="tabcontent active">
        <div class="row">
            <div class="col-sm-6">
              <div class="panel panel-primary">
                <div class="panel-heading">
                  Demand
                </div>
                <div class="panel-body">
                  <div class="form-group">
                    <label for="Demandid">
                      Demand id
                    </label>
                    <input type="text"
                          class="form-control"
                          id="Demandid" />
                  </div>
                
                    <div class="form-group">
                      <label for="Demandquantity">
                        Demand Quantity
                      </label>
                      <input type="text"
                            class="form-control"
                            id="Demandquantity" />
                    </div>
                    
                      <div class="form-group">
                        <label for="Demandstore">
                          Store name
                        </label>
                        <input type="text"
                              class="form-control"
                              id="Demandstore" />
                      </div>
                  
                        
    
                </div>
                <div class="panel-footer">
                  <div class="row">
                    <div class="col-xs-12">
                      <button type="button" id="updateButton" style="background-color:rgb(64, 139, 224);"
                              class="btn btn-primary"
                              onclick="addDemand();">
                        Add
                      </button>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-sm-6">
                    <table id="DemandTable"
                          class="table table-bordered table-condensed table-striped">
                      <thead>
                        <tr>
                          <th>id</th>
                          <th>Quantity</th>
                          <th>Store Name</th>
                        </tr>
                      </thead>
                    </table>
                  </div>
                </div>
          </div>
        </div>
      </div>
    </div>
    <div id="Administrators" class="tabcontent active">
        <div class="row">
            <div class="col-sm-6">
              <div class="panel panel-primary">
                <div class="panel-heading">
                  Administrator
                </div>
                <div class="panel-body">
                  <div class="form-group">
                    <label for="Administratorid">
                      Administrator id
                    </label>
                    <input type="text"
                          class="form-control"
                          id="Administratorid" />
                  </div>
                
                    <div class="form-group">
                      <label for="Administratorname">
                        Administrator Name
                      </label>
                      <input type="text"
                            class="form-control"
                            id="Administratorname" />
                    </div>
                    
                  
                        <div class="form-group">
                          <label for="Administratoremail">
                            Administrator Email
                          </label>
                          <input type="text"
                                class="form-control"
                                id="Administratoremail" />
                        </div>
    
                </div>
                <div class="panel-footer">
                  <div class="row">
                    <div class="col-xs-12">
                      <button type="button" id="updateButton"  style="background-color:rgb(64, 139, 224);"
                              class="btn btn-primary"
                              onclick="addAdministrator();">
                        Add
                      </button>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-sm-6">
                    <table id="AdministratorTable"
                          class="table table-bordered table-condensed table-striped">
                      <thead>
                        <tr>
                          <th>id</th>
                          <th>Name</th>
                          <th>Email Address</th>
                        </tr>
                      </thead>
                    </table>
                  </div>
                </div>
          </div>
        </div>
      </div>
    </div>
  </div>

</body>
</html>

"""


from flask import Flask

# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', welcome)

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
