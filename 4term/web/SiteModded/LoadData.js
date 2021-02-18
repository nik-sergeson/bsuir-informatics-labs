$(document).ready(function(){            
	function loadData(pageNumber){          
		$.ajax
		({
			type: "POST",
			url: "../load_data.php",
			data: { page: pageNumber, itemsperpage: 10}
		}).done(function(tag) {
			$("#dyntable").html(tag);
		});
	}
	
	loadData(1);

	$('#dyntable').on('click', '.numbs li.active', function(){
		var page = parseInt($(this).attr('p'));
		loadData(page);
	});
});