from django.http import HttpResponse
from NostraDomicile.models import HomeData

def test(request):
	text = HomeData.objects.all()
		
	return HttpResponse(text)

def index(request):
	text = '''<!DOCTYPE html>
<html lang="en" ng-app="NostraDomicile">
<head>
  <title>NostraDomicile</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet">
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" />
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/font-awesome/4.0.0/css/font-awesome.css" />
    <link rel="shortcut icon" href="images/rsz_favicon1.png" type="image/png">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <script src = "https://ajax.googleapis.com/ajax/libs/angularjs/1.3.14/angular.min.js"></script>
    <!--this snippet is from the old file structure

   {% load static from staticfiles %}
    <script src = "{% static 'controllers/mainController.js' %}"></script>-->
   <script src = "{% static 'mainController.js' %}"></script>


  <style>
    body {
      font: 20px Montserrat, sans-serif;
      line-height: 1.8;
      color: #f5f6f7;
    }
    h1 {      font-size: 250%;     }
    p {font-size: 16px;}
    .margin {margin-bottom: 45px;}

    h2 {color: black}
    h3 .btn-group { display: inline-block; }

    .bg-1 {

      background-color: #1abc9c; /* Green */
      color: #ffffff;
    }
    .bg-2 {
      background-color: #d3d3d3; /* Dark Blue */
      color: #555555;
    }
    .bg-3 {
      background-color: #ffffff; /* White */
      color: #555555;
    }
    .bg-4 {
      background-color: #2f2f2f; /* Black Gray */
      color: #555555;
    }

    .bg-5 {
        background-color: #708090;
        color: #555555
    }
    .container-fluid {
      padding-top: 70px;
      padding-bottom: 70px;
    }
    .navbar {
      padding-top: 15px;
      padding-bottom: 15px;
      border: 0;
      border-radius: 0;
      margin-bottom: 0;
      font-size: 14px;
      letter-spacing: 5px;
    }
    .navbar-nav  li a:hover {
      color: #1abc9c !important;
    }

    .popover-title{
        background: #555555;
    }
  </style>

</head>


<body>

<script>
    $(document).ready(function(){
        $('[data-toggle="popover"]').popover();
    });
</script>

<!--used for routing but not working-->
<div id = "main">
    <div ng-view></div>
</div>

<!-- Navbar -->
<nav class="navbar navbar-default">
  <div class="container">
      <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
          </button>
      <a class="navbar-brand"  href="#">NostraDomicile </a>
      <style> font-size: 20px </style>
    </div>
    <div class="collapse navbar-collapse" id="myNavbar">
      <ul class="nav navbar-nav navbar-right">
          <li><a href="#"><i class="fa fa-home"></i> HOME</a></li>
        <li><a href="#about"><i class="fa fa-shield"></i>ABOUT</a></li>
        <li><a href="#blog"><i class="fa fa-pencil-square"></i>BLOG</a></li>
        <li><a href="#contact"><i class="fa fa-comment"></i>CONTACT US</a></li>
      </ul>
    </div>
  </div>
</nav>
<!--Angular framework load -->

<!-- First Container -->
<!--<div class="" style="background-image: url('images/backgro1.png')">-->
<!--CHANGED IMAGES TO STATIC-->
<div class="container-fluid bg-1 text-center">
  <h1 style="color:#ffffff" class="margin"><b>Smart Solutions For Data Driven Real Estate Queries</b></h1>
  <img src="{% static 'hist3.png' %}" class="img-responsive margin" style="display:inline"  width="200" height="200">
  <img src="{% static 'statLine.png' %}" class="img-responsive img-circle margin" style="display:inline"  width="310" height="310">
  <img src="{% static 'nostraPicture.jpg' %}" class="img-responsive img-circle margin" style="display:inline"  width="250" height="250">
  <img src="{% static 'statLine.png' %}" class="img-responsive img-circle margin" style="display:inline"  width="310" height="310">
  <img src="{% static 'hist3.png' %}" class="img-responsive margin" style="display:inline"  width="200" height="200">

</div>


<!-- Second Container -->

<div class="container-fluid bg-5 text-center">

    <form name="myForm">


       <!--working version of user input to variable-->

            <h2 class="margin"> Please Enter Your Zip Code Of Interest
                <button type="button" class="btn btn-default"  data-toggle="popover" data-trigger="hover" data-content="This zip code
                    may be your own zip code(it must be if you are using the Will My House Sell function below) or
                    a zip code of a home you are interested in purchasing.  The information will be used
                    in the following functions below.  Your information will not be kept.">
                    <span class="glyphicon glyphicon-question-sign" aria-hidden="true"></span>
                </button>
            </h2>

            <label>
               <input style="color:#555555" ng-model="zipCode" type="text"  placeholder="Zip Code" required ng-minlength="5"
                       ng-maxlength="5">
                <p>{{zipCode}}</p>
            </label>


        <!-- Modal -->

            <!--<p><span ng-bind = "zipCode"></span></p>-->

      <div role="alert">
      <span class="error" ng-show="myForm.ZCode.$error.required">
       Required!</span>
      </div>

      <div class="form-group">
    <!--define app-->

    <p> ----------------------------------                                      </p>
    <h2 class="margin">Please Enter Your Home's Attributes
        <button type="button" class="btn btn-default"  data-toggle="popover" data-trigger="hover" data-content="These attributes
        will be used to predict whether your house will sell in the target zip code or not.  If you are interested in using this
        function please ensure that the zip code you entered above is the same that your home resides in.">
            <span class="glyphicon glyphicon-question-sign" aria-hidden="true"></span>
        </button></h2>
  </div>


    <!--Default buttons with dropdown menu-->
            <div class="col-xs-2">
                <input class="form-control" ng-model="price" type="text" placeholder="Price">
                <p>{{price}}</p>
            </div>

            <div class="col-xs-2">
                <input class="form-control" ng-model="sqFootage" type="text" placeholder="Square Footage">
                <p>{{sqFootage}}</p>
            </div>

            <div class="col-xs-2">
                <input class="form-control" ng-model="acreage" type="text" placeholder="Acreage">
                <p>{{acreage}}</p>
            </div>

            <div class="col-xs-2">
                <input class="form-control" ng-model="yearBuilt" type="text" placeholder="Year Built">
                <p>{{yearBuilt}}</p>
            </div>

            <div class="col-xs-2">
                <input class="form-control" ng-model="neighborhood" type="text" placeholder="Neighborhood">
                <p>{{neighborhood}}</p>
            </div>

            <div class="col-xs-2">
                <input class="form-control" ng-model="schoolDistrict" type="text" placeholder="School District">
                <p>{{schoolDistrict}}</p>
            </div>

        <br> </br>

        <div class="btn-group" ng-controller="selectboxCtrl">
            <select name="bedrooms" ng-model="userSelect1">
      <option value="">Bedrooms</option>
          <option ng-repeat="option in BedroomList" value="{{option.bedroom}}">{{option.bedroom}}</option>
          <!--here would be django variable ={{userSelect1}}-->
      </select>
      </div>

      <div class="btn-group"  ng-controller="selectboxCtrl">
          <select name="bathroom" ng-model="userSelect2">
              <option value="">Bathrooms</option>
              <option ng-repeat="option in BathroomList" value="{{option.bathroom}}">{{option.bathroom}}</option>
          </select>
      </div>




        <div class="btn-group"  ng-controller="selectboxCtrl">
            <select name="stories" ng-model="storiesSelect">
                <option value="">Stories</option>
                <option ng-repeat="option in BedroomList" value="{{option.bedroom}}">{{option.bedroom}}</option>
            </select>
        </div>



        <div class="btn-group"  ng-controller="selectboxCtrl">
            <select name="homeType" ng-model="homeTypeSelect">
                <option value="">Home Type</option>
                <option ng-repeat="option in TypeList" value="{{option.type}}">{{option.type}}</option>
            </select>
        </div>


        <div class="btn-group"  ng-controller="selectboxCtrl">
            <select name="parking" ng-model="parkingSelect">
                <option value="">Parking</option>
                <option ng-repeat="option in ParkingList" value="{{option.parking}}">{{option.parking}}</option>
            </select>
        </div>

<p>   ----------------------------  </p>



      <div>
          <input class="btn btn-primary btn-lg" type="button" value="Submit Information" ng-click="checkselection()" />
            <button type="button" class="btn btn-default"  data-toggle="popover" data-trigger="hover" data-content="The information entered
             above will be submitted and used in one or all of the following site's primary functions below. ">
              <span class="glyphicon glyphicon-question-sign" aria-hidden="true"></span>
          </button>
          </div>
    </form>
            </div>



  <!--<label for="usr">Please Enter Your Zip Code:</label>-->
  <!--<input type="text" class="form-control" id="usr">-->


<!--STATIC CHANGED HERE FROM IMAGES FOLDER-->
<!-- Third Container (Grid) -->
<div class="container-fluid bg-2 text-center">
  <div class= "card-group">
    <!--<div class="row">-->
    <div class="col-sm-4">
      <!--<div class="card" style="width: 20rem;">
      <div class="card card-inverse card-info mb-3 text-center">-->
      <div class="card card-outline-primary mb-3 text-center" style="background-color: #333; border-color: #333;">
        <img class="card-img-top" src="images/houseSold.jpeg" alt="Card image cap">
        <div class="card-block">
          <h4 class="card-title">Prediction on Sale</h4>
          <p>Click the button below to see if your house will sell based on the attributes you have provided.</p>
          <a href="#" class="btn btn-primary">Will My House Sell?</a>
        </div>
      </div>
    </div>
    <div class="col-sm-4">
      <!--<div class="card" style="width: 20rem;">-->
      <div class="card card-outline-primary mb-3 text-center">
        <img class="card-img-top" src="images/homeAtt3.png" alt="Card image cap">
        <div class="card-block">
          <h4 class="card-title">Prediction on Most Important Attributes</h4>
          <p>Click the button below to see the most attractive factors leading to home sales in the chosen area.</p>
          <a href="#" class="btn btn-primary">Most Important Attributes</a>
        </div>
      </div>
    </div>
    <div class="col-sm-4">
      <!--<div class="card" style="width: 20rem;">-->
      <div class="card card-outline-primary mb-3 text-center">
        <img class="card-img-top" src="images/statsImage.jpeg" alt="Card image cap">
        <div class="card-block">
          <h4 class="card-title">Data Visualizations</h4>
          <p>Click the button below to see a collection of valuable statistics pertaining to the chosen area.</p>
          <a href="#" class="btn btn-primary">Data Visualizations</a>
        </div>
      </div>
    </div>
  </div>
</div>


<!--<div class="container-fluid bg-3 text-center">
  <h3 class="margin">Will Your House Sell?</h3><br>
  <div class="row">
    <div class="form-group">
  <label for="usr">Please Enter Your Zip Code:</label>
  <input type="text" class="form-control" id="usr">
  <!--define app
<div ng-app = "NostraDomicile">
<div ng-app = "mainApp" ng-controller = "studentController">
         Enter first name: <input type = "text" ng-model = "student.firstName"><br><br>
         Enter last name: <input type = "text" ng-model = "student.lastName"><br>
         <br>

         You are entering: {{student.fullName()}}
      </div>
	   <script>
         var mainApp = angular.module("mainApp", []);

         mainApp.controller('studentController', function($scope) {
            $scope.student = {
               firstName: "Mahesh",
               lastName: "Parashar",

               fullName: function() {
                  var studentObject;
                  studentObject = $scope.student;
                  return studentObject.firstName + " " + studentObject.lastName;
               }
            };
         });
      </script>
<p>Enter your Zip Code: <input type = "text" ng-model = "NostraDomicile"></p>
         <p><span ng-bind = "NostraDomicile"></span></p>
 </div>-->



<!-- Footer -->
<footer class="container-fluid bg-4 text-center">
  <p>Created as Senior Project</p>
</footer>
    </form>
    </div>
</body>
</html>'''
	return HttpResponse(text)
