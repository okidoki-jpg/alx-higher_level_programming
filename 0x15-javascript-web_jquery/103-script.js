$(document).ready(function () {
	$('INPUT#btn_translate').click(trans);
	$('INPUT#language_code').focus(function () {
		$(this).keydown(function (event) {
			if (event.keyCode === 13) {
				trans();
			}
		});
	});
});

function trans() {
	const lang = $('INPUT#language_code').val();
	$.get('https://www.fourtonfish.com/hellosalut/?lang=' + lang, function (data) {
		$('DIV#hello').text(data.hello);
	});
}
