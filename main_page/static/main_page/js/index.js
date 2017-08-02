$('button.more-button').on('click', function(){
	var next_page_url = $('.pagination li.active').next().find('a').attr('href');
	console.log(next_page_url);
	if (next_page_url){
		$.ajax({
			url: '/' + next_page_url + '&json=true'
		}).done(function(response){
			$('.paginator').remove();
			$('.landing').last().after(response);
		});
	}
})