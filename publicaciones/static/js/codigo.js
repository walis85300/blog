$('#home').on('click', function(){

	$('#menuMoviles').css({

		"left": "0",
		"transition" :"all .5s ease-out",
		"-webkit-transition" :"all 0.5s ease-out"
	});

});

$('#cerrar').on('click',function(){

	$('#menuMoviles').css({
		"left": "-480px",
		"transition" :"all .5s ease-out",		
		"-webkit-transition" :"all .5s ease-out"
	});
});




