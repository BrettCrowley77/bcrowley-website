$(document).ready(function(){

	/* default settings */
	$('.venobox').venobox();

	/* open content with custom settings */
	$('.venobox_custom').venobox({
    spinColor: '#F0F3BD',
    infinigall: false,
    framewidth: '50%',
		frameheight: '50%',
    bgcolor: '#05668D',
    arrowsColor: '#F0F3BD',
    closeBackground: '#05668D',
    closeColor: '#F0F3BD',
		border: '6px',
		bordercolor: '#ba7c36',
		numeratio: false
	});

	// layout Masonry after each image loads
	$('.grid').imagesLoaded(function() {
		var $grid = $('.grid').isotope({
			itemSelector: '.grid-item',
			masonry: {
				columnWidth: '.grid-sizer'
			}
		});
		var $items = $grid.find('.grid-item');
		$grid.removeClass('not-showing-items');
		$grid.addClass('is-showing-items')
		  .isotope( 'revealItemElements', $items );
	});

});

var togglebookshelf = function(){

	var shelves = ['#movieshelf', '#musicshelf', '#articleshelf'];

	for (i = 0; i < shelves.length; i++) {
		if ($(shelves[i]).css('class') !== 'row hide') {
			$(shelves[i]).addClass('hide');
		}
	}

	$('#bookshelf').toggleClass('hide');
}

var togglemovieshelf = function(){

	var shelves = ['#bookshelf', '#musicshelf', '#articleshelf'];

	for (i = 0; i < shelves.length; i++) {
		if ($(shelves[i]).css('class') !== 'row hide') {
			$(shelves[i]).addClass('hide');
		}
	}

	$('#movieshelf').toggleClass('hide');
}

var togglemusicshelf = function(){

	var shelves = ['#bookshelf', '#movieshelf', '#articleshelf'];

	for (i = 0; i < shelves.length; i++) {
		if ($(shelves[i]).css('class') !== 'row hide') {
			$(shelves[i]).addClass('hide');
		}
	}

	$('#musicshelf').toggleClass('hide');
}

var togglearticleshelf = function(){

	var shelves = ['#bookshelf', '#movieshelf', '#musicshelf'];

	for (i = 0; i < shelves.length; i++) {
		if ($(shelves[i]).css('class') !== 'row hide') {
			$(shelves[i]).addClass('hide');
		}
	}

	$('#articleshelf').toggleClass('hide');
}

$('#books').click(togglebookshelf);

$('#movies').click(togglemovieshelf);

$('#music').click(togglemusicshelf);

$('#articles').click(togglearticleshelf);

var counter = 0;

var slideshow = function(){
		var photonumber = (counter+1).toString();
		var imgsrc = 'static/img/profile' + photonumber + '.jpg';
		if (counter==3) {
			$('.profileslide').attr('src', imgsrc);
			counter=0;
		} else {
		$('.profileslide').attr('src', imgsrc);
		counter++;
		};
	};

setInterval(slideshow, 4000);
