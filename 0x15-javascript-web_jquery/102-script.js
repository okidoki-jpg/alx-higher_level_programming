/* fetches and prints how to say “Hello” depending on the language

You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
The translation must be fetched when the user clicks on INPUT#btn_translate
The translation of “Hello” must be displayed in the HTML tag DIV#hello
*/

$(document).ready(function () {
  $('#btn_translate').click(function () {
	const lang = $('#language_code').val();

	$.get('https://www.fourtonfish.com/hellosalut/?lang=' + lang, function (data) {
	  $('#hello').text(data.hello);
	});
  });
});
