//Jeff Haak
//Library functions for pyramid app

function hideAll(){
    $(".home").hide();
    $(".item").hide();
    $(".location").hide();
    $(".barrowed").hide();
}

function createLocation(event){
    console.log("Create Location!");
    var name = $("input[name=locName]").val()
    var roomNumber = $("input[name=locRoomNumber]").val()

    var dataString = "name=" + name;
    dataString += "roomNumber=" + roomNumber;

    $.ajax({
        type: "POST",
        url: "/createLocation",
        data: dataString,
        cache: false,
        success: function(result){
            console.log("WOO");
        }
    });
}








