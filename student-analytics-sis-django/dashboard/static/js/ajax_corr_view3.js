function setOptionsCourse(){
    $('#id_course')     .prepend($("<option></option>").attr("value","All").text("All")); 
    $('#id_course')     .prepend($("<option disabled selected></option>").attr("value","Select").text("Select")); 
}
function setOptionsEnrollYear(){
    $('#id_enroll_year').empty();
    $('#id_enroll_year').prepend($("<option></option>").attr("value","All").text("All"));
    $('#id_enroll_year').prepend($("<option disabled selected></option>").attr("value","Select").text("Select")); 
}
function setOptionsSection(){
    $('#id_section')    .empty();
    $('#id_section')    .prepend($("<option></option>").attr("value","All").text("All"));
    $('#id_section')    .prepend($("<option disabled selected></option>").attr("value","Select").text("Select")); 
}
setOptionsCourse();
setOptionsEnrollYear();
setOptionsSection();


function getEnrollYear(course_id){
        $.ajax(
            {
                type:"POST",
                url: "getEnrollYear",
                dataType: "json",
                data:{
                        course: course_id
                },
                success: function( data ) 
                {
                    removeData(scatterChart);
                    setOptionsEnrollYear();
                    setOptionsSection()
                    $.each(data, function(key, value) {   
                        $('#id_enroll_year')
                            .append($("<option></option>")
                                        .attr("value",key)
                                        .text(value)); 
                    });
                }
            });
        }

function getSection(enroll_year){
    course_id = document.getElementById('id_course').value;
    $.ajax(
        {
            type:"POST",
            url: "getSection",
            dataType: "json",
            data:{
                    course: course_id,
                    enroll_year: enroll_year
            },
            success: function( data ) 
            {
                removeData(scatterChart);
                setOptionsSection();
                $.each(data, function(key, value) {   
                    $('#id_section')
                        .append($("<option></option>")
                                    .attr("value",key)
                                    .text(value));  
                });
            }
        });
    }

function updateVisualization(section){
    course_id   = document.getElementById('id_course').value;
    enroll_year = document.getElementById('id_enroll_year').value;
    $.ajax(
        {
            type:"POST",
            url: "updateVisualization",
            dataType: "json",
            data:{
                    course: course_id,
                    enroll_year: enroll_year,
                    section: section
            },
            success: function( responseData ) 
            {
                removeData(scatterChart);
                addData(scatterChart, [], responseData.data);
                $('#corr').html("Correlation for the given data is "+ responseData.corr);
            }
        });
    }

function addData(scatterChart, label, data) {
    //chart.data.labels.push(label);
    scatterChart.data.datasets[0].data=data;
    scatterChart.update();
}

function removeData(scatterChart) {
    scatterChart.data.datasets[0].data=[];
    scatterChart.update();
}

// var chart = new Chart(ctx, {
//     // The type of chart we want to create
//     type: 'line',

//     // The data for our dataset
//     data: {
//         labels: ["January", "February", "March", "April", "May", "June", "July"],
//         datasets: [{
//             label: "My First dataset",
//             backgroundColor: 'rgb(255, 99, 132)',
//             borderColor: 'rgb(255, 99, 132)',
//             data: [0, 10, 5, 2, 20, 30, 45],
//         }]
//     },

//     // Configuration options go here
//     options: {}
// });




'use strict';

window.chartColors = {
	red: 'rgb(255, 99, 132)',
	orange: 'rgb(255, 159, 64)',
	yellow: 'rgb(255, 205, 86)',
	green: 'rgb(75, 192, 192)',
	blue: 'rgb(54, 162, 235)',
	purple: 'rgb(153, 102, 255)',
	grey: 'rgb(201, 203, 207)'
};

(function(global) {
	var COLORS = [
		'#4dc9f6',
		'#f67019',
		'#f53794',
		'#537bc4',
		'#acc236',
		'#166a8f',
		'#00a950',
		'#58595b',
		'#8549ba'
	];

	var Samples = global.Samples || (global.Samples = {});
	var Color = global.Color;

	Samples.utils = {
		// Adapted from http://indiegamr.com/generate-repeatable-random-numbers-in-js/


		color: function(index) {
			return COLORS[index % COLORS.length];
		},

		transparentize: function(color, opacity) {
			var alpha = opacity === undefined ? 0.5 : 1 - opacity;
			return Color(color).alpha(alpha).rgbString();
		}
	};


}(this));