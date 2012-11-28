<html>
<body>
	%jane=model.Employee(name="Jane", isManager=True, login="4126")
	<strong>Created Jane</strong>:{{jane.dict}}</br></br>

	%tim=model.Employee(name="Tim", isManager=False, login="4189")
	<strong>Created Tim</strong>:{{tim.dict}}</br></br>

	%bob=model.Employee(name="Bob", isManager=False, login="4122")
	<strong>Created Bob</strong>:{{bob.dict}}</br></br>

	%peter=model.Employee(name="Peter", isManager=False, login="4121")
	<strong>Created Peter</strong>:{{peter.dict}}</br></br>

	%abcStore=model.Store(name="ABC")
	<strong>Created ABC Store</strong>:{{abcStore.dict}}</br></br>
			
	%defStore=model.Store(name="DEF")
	<strong>Created DEF Store</strong>:{{defStore.dict}}</br></br>

	<strong>Wrong Login of Tim, 5555:</strong>{{controller.checkLogin("Tim", "5555")}}</br></br>
	<strong>Correct Login of Tim, 4189:</strong>{{controller.checkLogin("Tim", "4189")}}</br></br>
	<strong>Wrong Login of Kathy, 4189:</strong>{{controller.checkLogin("Kathy", "4189")}}</br></br>

	<strong> Add New Employee Martha, 1111, abcStore </strong>:
	%controller.addNewEmployee("Martha", False,"1111", abcStore)
	{{controller.loadEmployeeList(abcStore.name)}}
	
	




</body>
</html>
