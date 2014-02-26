<html>
	<head>
		<title>
			CSH Inventory
		</title>

		<link rel="stylesheet" type="text/css" href="../static/style.css">
		<script language="javascript" type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
		<script language="javascript" type="text/javascript" src="../static/library.js"></script>
		
		<script type="text/javascript">
			$(document).ready(function(){
				hideAll();
				$(".${page}").show();
				$("#locationForm").submit(createLocation);
			});
		</script
	</head>

	<body>
		<div class="page">
			<div class="header">
				<span class="nav">
					<ul class="navList">
						<li>
							<a href='/'>My Stuff</a>
						</li>
						<li>
							<a href='/addItem'>Add Item</a>
						</li>
						<li>
							<a href='/addLocation'>Add Location</a>
						</li>
						<li>
							<a href='#'>Barrow Item</a>
						</li>
					</ul>
				</span>
				<span class="welcomeBar">
					Welcome ${username}!
				</span>
			</div>
		
			<br/>

			<div class="content">
				<div class="home">
					<div class="barrowedTable">
						<ul class="barrowedList">
						</ul>
					</div>	
					<div class="locationTable">
						<ul class="locationList">
						</ul>
					</div>	
					<div class="itemsTable">
						<ul class="itemsList">
						</ul>
					</div>
				</div>
				
				<div class="item">
					<form>
						<p>Create An Item:</p>
						
						<label for="itemBarcode">Barcode:</label>
						<input type="text" name="itemBarcode">
						
						<br/>

						<label for="itemDesc">Item Description:</label>
						<input type="text" name="itemDesc">

						<br/>
						
						<label for="itemCost">Item Cost:</label>
						<input type="text" name="itemCost">

						<br/>

						<label for="itemLoc">Item Location:</label>
						<select name="itemLoc">
							<option value="1">TestLoc</option>
						</select>
						
						<br/>
						
						<input type="submit" value="Submit" id="itemSubmit">				
					</form>
				</div>

				<div class="location">
					<form id="locationForm">
						<p>Create A Location:</p>
						
						<label for="locName">Location Name:</label>
						<input type="text" name="locName">
						
						<br/>

						<label for="locRoomNum">Room Number:</label>
						<input type="text" name="locRoomNum">

						<br/>
						
						<input type="submit" value="Submit" id="locSubmit">				
					</form>
				</div>

				<div class="barrowed">
					<form>
								
					</form>
				</div>

			</div>
		</div>
	</body>
</html>
