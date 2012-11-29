<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title></title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width">

        <link rel="stylesheet" href="css/normalize.min.css">
        <link rel="stylesheet" href="css/main.css">

        <script src="js/vendor/modernizr-2.6.2.min.js"></script>
	
    </head>
    <body>
        <!--[if lt IE 7]>
            <p class="chromeframe">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">activate Google Chrome Frame</a> to improve your experience.</p>
        <![endif]-->

	<div id ="backPanel">


		<section id = loginPanel>
			<!-- This is lazy, I'll fix it later and NOT forget.-->
			<div id = "loginForm" >
				Name:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input id="loginName"type="text" name ="name" placeholder="Name" required="required"><br>
				Password:&nbsp;<input id="loginPassword" type="password" placeholder="****" required="required"></br>
				<button id ="loginButton">Login</button>
			</div>
		</section>
	
		<section id="mainContentPanel">

			<!-- There will be more buttons here in the future-->
			<section id = "topBar">
				<button id="logoutBox">Logout</button>
			</section>	
			
			<section id = "leftBar">
				<section id = "topLeftBar">
					No New Notifications!
					<!--
					<div class = "notificationBox">
						<div class = "notification">This is a notification!
							<div class = "decisionBox">
							</div>
						</div>
						
					</div>
					-->
				</section>
				<section id = "bottomLeftBar">
					<button class="taskBox" id="employeeManagementButton">Employee Admin </button>
					<button class="taskBox" id="shiftManagementButton">Shift Admin </button>
					<button class="taskBox" id="deadlineManagementButton">Set Deadline </button>
					<button class="taskBox" id="backToMain">Back to Main Screen </button>
				</section>
			</section>

			<section id="schedulePanel" class= "contentPanel">
				<div id = "scheduleHeader">
					<p id="monthText">Month</p>
					<span id ="weekText"> Monday Tuesday Wednesday Thursday Friday Saturday Sunday </span>
				</div>
				<div id ="calendarScroll">
					<section id="calendarBox">
						<div class = "dayBox">
							<div id = "shiftBox">
							</div>
						</div>
					
					</section>
				</div>
			</section>

			<section id="employeeManagementPanel" class="contentPanel">
				<div id="employee" class="options"></br></br>
					<span class="introAdminText">What would you like to do?</span></br></br>
					<button type="button" id ="removeEmployee" class ="optionsButtons">Remove Employee </button></br></br>
					<button type="button" id ="addEmployee" class ="optionsButtons">Add Employee </button></br></br>
					<button type="button" id ="removeEmployeeFromStore" class ="optionsButtons">Remove Employee From Store </button></br></br>
					<button type="button" id ="addEmployeeToStore" class ="optionsButtons">Add Employee To Store </button></br></br>
				</div>
				<section id="employee" class="dynamicPanel">
				</section>
			</section>

			<section id="shiftManagementPanel" class="contentPanel">
				<div id ="shift" class="options"></br></br>
					<span class="introAdminText">What would you like to do?</span></br></br>
					<button type="button" id ="removeDefaultShift" class ="optionsButtons">Remove Preset Shift </button></br></br>
					<button type="button" id ="addDefaultShift" class ="optionsButtons">Add Preset Shift </button></br></br>
				</div>				
				<section id="shift" class="dynamicPanel">
				</section>
			</section>

			<section id="deadlinePanel" class="contentPanel">
				
			</section>	
				
		</section>	
	</div>


    </body>
	<!-- JS at bottom for faster page loading -->
	<script src = "js/vendor/jquery-1.8.3.min.js"></script>
	<script src = "js/main.js"></script>
</html>
