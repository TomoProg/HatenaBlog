:command! -nargs=1 PyTemplate call PyTemplateFunc(<f-args>)

function PyTemplateFunc(template)
	if a:template == "main"
		:r ~/.vim/mycmd/py_template/main.py
	elseif a:template == "docstr" || a:template == "ds"
		:r ~/.vim/mycmd/py_template/docstr.py
	else
		echo("Nothing Python Template.")
	endif
endfunction
