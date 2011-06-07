function generatePython() {
	var box = document.createElement('textarea');
	function output(str)
	{
		box.innerHTML += str;
	}

	function write_elements()
	{
		i = 0;
		while (1)
		{
			elems = document.getElementsByClassName('level'+i);

			if (!elems.length) break;

			output('\n# Level '+i+'\n\n');
			for (var j = 0; j < elems.length; j++)
			{
				var elem = elems[j];
				var class_name = elem.id;
				var type = elem.childNodes[15].firstChild.firstChild.nodeValue;
				var header = elem.childNodes[5].firstChild.nodeValue;

				output('class '+class_name+'('+type+'):\n\theader=\''+header+'\'\n\n');
			}
		}
	}

	write_elements();
	return box
}
