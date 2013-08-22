$('#home').on('click', function(){

	$('#menuMoviles').css({

		"left": "0",
		"transition" :"all 1s ease-out",
		"-webkit-transition" :"all 1s ease-out"
	});

});

$('#cerrar').on('click',function(){

	$('#menuMoviles').css({
		"left": "-480px",
		"transition" :"all 1s ease-out",		
		"-webkit-transition" :"all 1s ease-out"
	});
});




