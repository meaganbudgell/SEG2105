$(document).ready(function(){
//Buttons in order of appearance

	$('#loginButton').click(function(){
		$('#loginPanel').hide();
		$('#mainContentPanel').show();
		$('#schedulePanel').show();
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
