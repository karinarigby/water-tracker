$(document).ready(function(){
    var percentage = getUserPercentage();
    var amount = 0;
    
    //retrieve the percentage of the current user's day water-percentage
    function getUserPercentage(){
        var progressBar = $("#progressBar");
        $.ajax(
            //send the get request to the db 
        ).done(function(data){
            updateProgressBarPercentage(data.percentage)
        });
    }

    function adjustUserWaterAmount(amount){
        var url = ""

        $.ajax({
            type: "POST",
            url: url,
            //amount

            //error something

        }).done(function(data){
            //update the progress bar
            // or show error
            updateProgressBarPercentage();
        })   
    }

    //update the progress bar on the page
    function updateProgressBarPercentage(percentage){

    }

    $("#water-container-s").click(function (){
        adjustUserWaterAmount(225);
        percentage = getUserPercentage();
        updateProgressBarPercentage(percentage);
    

    });

    $("#water-container-m").click(function (){
       console.log("Med container pressed");
       adjustUserWaterAmount(500);
       percentage = getUserPercentage();
       updateProgressBarPercentage(percentage);
    });

    $("#water-container-l").click(function (){
        console.log("Large container pressed");
        adjustUserWaterAmount(750);
        percentage = getUserPercentage();
        updateProgressBarPercentage(percentaage);
    });
});