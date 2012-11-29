$(document).ready(function(){

//Buttons in order of appearance
	
function loadManagerUI(eName){
	//get todays date
	var date= new Date();
	date.toISOString();
	console.log(date);
	 $.ajax ({
		   url: "/loadSchedule/",
		   type: "POST",
		   data: JSON.stringify({'date':date}),
		   dataType: "json",
		   contentType: "application/json; charset=utf-8",
		   success: function(result){
			console.log(result);
		for (var i =0;i <= result["firstOfMonthWeekDay"];i++)
		{
			var parent=$(".dayBox").parent();
			$(".dayBox").clone().appendTo(parent);
		}
		




		}});


}
	$('#loginButton').click(function(){
		var eName=$('#loginName').val();
		 $.ajax ({
		   url: "/checkEmployeeLogin/",
		   type: "POST",
		   data: JSON.stringify({'eName':eName, 'loginCode':$('#loginPassword').val()}),
		   dataType: "json",
		   contentType: "application/json; charset=utf-8",
		   success: function(result){
			if (result["result"] ==  true)
			{	
				
				
				$('#loginPanel').hide();
				$('#mainContentPanel').show();
				$('#schedulePanel').show();
				loadManagerUI(eName);
			}
			else
			{
			$("#loginForm").append("</br>Invalid Login: Please Try Again");
			}
		}});
		
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
