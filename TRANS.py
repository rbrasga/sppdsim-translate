# translate.py
# Created 04/14/20
# Updated 04/15/20
# Current Version: 0.10
from . import ru
from . import de
from . import fr
from . import it
from . import es
from . import ko
from . import zh_tw
from . import zh_cn
from . import pt
from . import pl
from . import tr
from . import ja
#import nl

LANGUAGES=[
	"English",
	"Русский",		#Russian, ru
	"Deutsch",		#German, de
	"Français",		#French, fr
	"Italiano",		#Italian, it
	"Español",		#Spanish, es
	"한국어",		#Korean, ko
	"繁體中文(台灣)",	#Chinese Taiwan, zh-tw
	"中文（简体）",		#Chinese Simplified, zh-cn
	"Português",	#Brazilian, pt
	"Polski",		#Polish, pl
	"Türkçe",		#Turkish, tr
	"日本語",		#Japanese, ja
	#"Dutch",		#Netherlands, nl
]

WORDS={}
#WORDS[<word>] = { <key1> : <translation1>, <key2> : <translation2>, ... }
language_map = [ru,de,fr,it,es,ko,zh_tw,zh_cn,pt,pl,tr,ja]
for language in language_map:
	for key in language.WORDS:
		if key in WORDS:
			WORDS[key]={**WORDS[key],**language.WORDS[key]}
		else:
			WORDS[key]=language.WORDS[key]
