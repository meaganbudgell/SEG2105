$(document).ready(function(){

//Buttons in order of appearance
	
function loadManagerUI(eName){
	//get todays date
	var date= new Date();
	var datastring={'date':date}
	console.log(date);
	$.get("/loadSchedule/", datastring, function(result){
	console.log(result);

	});

}
	$('#loginButton').click(function(){
		var eName=$('#loginName').val();
		var datastring= { 'eName':eName, 'loginCode':$('#loginPassword').val()}
		console.log(datastring);
		$.get("/checkEmployeeLogin/", datastring, function(result){
			console.log(result);
			if (result == "True")
			{	
				
				loadManagerUI(eName);
				$('#loginPanel').hide();
				$('#mainContentPanel').show();
				$('#schedulePanel').show();
			}
			else
			{
			$("#loginForm").append("</br>Invalid Login: Please Try Again");
			}
		});
		
	});

	$('#logoutBox').click(function(){
		$('#loginPanel').show();
		$('#mainContentPanel').hide();
		$('#schedulePanel').hide();
	});

	$('#backToMain').click(function(){
		//No point in if statements, no matter what we want all hidden except one.
		$('#employeeManagementPanel').hide();
		$('#shiftManagementPanel').hide();	
		$('#deadlinePanel').hide();
		$('#schedulePanel').show();
	});
	$('#employeeManagementButton').click(function(){
		$('#employeeManagementPanel').show();
		$('#shiftManagementPanel').hide();	
		$('#deadlinePanel').hide();
		$('#schedulePanel').hide();
	});
	$('#shiftManagementButton').click(function(){
		$('#employeeManagementPanel').hide();
		$('#shiftManagementPanel').show();	
		$('#deadlinePanel').hide();
		$('#schedulePanel').hide();
	});
	$('#deadlineManagementButton').click(function(){
		$('#employeeManagementPanel').hide();
		$('#shiftManagementPanel').hide();	
		$('#deadlinePanel').show();
		$('#schedulePanel').hide();
	});


	

});
