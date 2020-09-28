# translate.py
# Created 04/14/20
# Updated 04/15/20
# Current Version: 0.10
'''
LANGUAGES=[
	"English",
	"Русский",		#Russian, ru
	"Deutsch",		#German, de
	"Français",		#French, fr
	"Italiano",		#Italian, it
	"Español",		#Spanish, es
	"한국어",			#Korean, ko
	"繁體中文(台灣)",	#Chinese Taiwan, zh-tw
	"中文（简体）",		#Chinese Simplified, zh-cn
	"Português",	#Brazilian, pt
	"Polski",		#Polish, pl
	"Türkçe",		#Turkish, tr
	"日本語",			#Japanese, ja
	#"Dutch",		#Netherlands, nl
]
'''
WORDS={}
#WORDS[<word>] = { <key1> : <translation1>, <key2> : <translation2>, ... }

#Card Names
WORDS["A.W.E.S.O.M.-O 4000"]={1:"Ш.И.К.А.Р.Н.-O 4000"}
WORDS["Alien Clyde"]={1:"Клайд Чужой"}
WORDS["Alien Drone"]={1:"Дрон Пришельцев"}
WORDS["Alien Queen Red"]={1:"Королева Чужих Рыжик"}
WORDS["Angel Wendy"]={1:"Ангел Венди"}
WORDS["Arrowstorm"]={1:"Ливень Стрел"}
WORDS["Astronaut Butters"]={1:"Космонавт Баттерс"}
WORDS["Bandita Sally"]={1:"Бандитка Салли"}
WORDS["Barrel Dougie"]={1:"Бочонок Дуги"}
WORDS["Big Gay Al"]={1:"Большой Эл-Гомосек"}
WORDS["Blood Elf Bebe"]={1:"Кровавый Эльф Биби"}
WORDS["Bounty Hunter Kyle"]={1:"Охотник за Головами Кайл"}
WORDS["Buccaneer Bebe"]={1:"Буканьер Биби"}
WORDS["Calamity Heidi"]={1:"Катастрофа Хайди"}
WORDS["Canadian Knight Ike"]={1:"Канадский Рыцарь Айк"}
WORDS["Captain Wendy"]={1:"Капитан Венди"}
WORDS["Catapult Timmy"]={1:"Катапульта Тимми"}
WORDS["Chicken Coop"]={1:"Курятник"}
WORDS["Choirboy Butters"]={1:"Певчий Баттерс"}
WORDS["Classi"]={1:"Классисика"}
WORDS["Cock Magic"]={1:"Петушинная Магия"}
WORDS["Cupid Cartman"]={1:"Купидон Картман"}
WORDS["Cyborg Kenny"]={1:"Киборг Кенни"}
WORDS["Dark Mage Craig"]={1:"Темный Маг Крэйг"}
WORDS["Deckhand Butters"]={1:"Матрос Баттерс"}
WORDS["Dogpoo"]={1:"Догпу"}
WORDS["Dragonslayer Red"]={1:"Убийца Драконов Рыжик"}
WORDS["Dwarf Engineer Dougie"]={1:"Гномий Инженер Дуги"}
WORDS["Dwarf King Clyde"]={1:"Король Гномов Клайд"}
WORDS["Elven King Bradley"]={1:"Король Эльфов Брэдли"}
WORDS["Energy Staff"]={1:"Посох Энергии"}
WORDS["Enforcer Jimmy"]={1:"Вышибала Джимми"}
WORDS["Fireball"]={1:"Огненный Шар"}
WORDS["Four-Assed Monkey"]={1:"Четырехжопая Обезьяна"}
WORDS["Freeze Ray"]={1:"Замораживающий Луч"}
WORDS["Friar Jimmy"]={1:"Монах Джимми"}
WORDS["Gizmo Ike"]={1:"Гизмо Айк"}
WORDS["Grand Wizard Cartman"]={1:"Великий Чародей Картман"}
WORDS["Gunslinger Kyle"]={1:"Стрелок Кайл"}
WORDS["Hallelujah"]={1:"Аллилуйя"}
WORDS["Hercules Clyde"]={1:"Геркулес Клайд"}
WORDS["Hermes Kenny"]={1:"Гермес Кенни"}
WORDS["Hookhand Clyde"]={1:"Клайд с Крюком"}
WORDS["Hyperdrive"]={1:"Гиперскорость"}
WORDS["Ice Sniper Wendy"]={1:"Ледяной Снайпер Венди"}
WORDS["Imp Tweek"]={1:"Чертенок Твик"}
WORDS["Incan Craig"]={1:"Инка Крэйг"}
WORDS["Inuit Kenny"]={1:"Эскимос Кенни"}
WORDS["Kyle of the Drow Elves"]={1:"Темный Эльф Кайл"}
WORDS["Le Bard Jimmy"]={1:"Бард Джимми"}
WORDS["Lightning Bolt"]={1:"Удар Молнии"}
WORDS["Manbearpig"]={1:"Челмедведосвин"}
WORDS["Marcus"]={1:"Маркус"}
WORDS["Marine Craig"]={1:"Морпех Крэйг"}
WORDS["Mecha Timmy"]={1:"Меха-Тимми"}
WORDS["Medicine Woman Sharon"]={1:"Женщина-Врач Шерон"}
WORDS["Medusa Bebe"]={1:"Медуза Биби"}
WORDS["Mimsy"]={1:"Мимзи"}
WORDS["Mind Control"]={1:"Контроль Разума"}
WORDS["Mr. Hankey"]={1:"Мистер Хэнки"}
WORDS["Mr. Mackey"]={1:"Мистер Маки"}
WORDS["Mr. Slave Executioner"]={1:"Мистер Мазохист"}
WORDS["Nathan"]={1:"Нейтан"}
WORDS["Nelly"]={1:"Нелли"}
WORDS["Officer Barbrady"]={1:"Офицер Барбреди"}
WORDS["Outlaw Tweek"]={1:"Разбойник Твик"}
WORDS["Paladin Butters"]={1:"Паладин Баттерс"}
WORDS["PC Principal"]={1:"ПК Директор"}
WORDS["Pigeon Gang"]={1:"Банда Голубей"}
WORDS["Pirate Ship Timmy"]={1:"Пиратский Корабль Тимми"}
WORDS["Pocahontas Randy"]={1:"Покахонтас Рэнди"}
WORDS["Poison"]={1:"Яд"}
WORDS["Pope Timmy"]={1:"Папа Тимми"}
WORDS["Poseidon Stan"]={1:"Посейдон Стэн"}
WORDS["Power Bind"]={1:"Блокировка Умений"}
WORDS["Powerfist Dougie"]={1:"Электрический Кулак Дуги"}
WORDS["Priest Maxi"]={1:"Священник Макси"}
WORDS["Princess Kenny"]={1:"Принцесса Кенни"}
WORDS["Program Stan"]={1:"Цифровой Стэн"}
WORDS["Prophet Dougie"]={1:"Пророк Дуги"}
WORDS["Purify"]={1:"Очищение"}
WORDS["Rat Swarm"]={1:"Полчище Крыс"}
WORDS["Regeneration"]={1:"Регенерация"}
WORDS["Robin Tweek"]={1:"Робин Твик"}
WORDS["Robo Bebe"]={1:"Робот Биби"}
WORDS["Rogue Token"]={1:"Разбойник Токен"}
WORDS["Santa Claus"]={1:"Санта Клаус"}
WORDS["Satan"]={1:"Сатана"}
WORDS["Scout Ike"]={1:"Скаут Айк"}
WORDS["Sexy Nun Randy"]={1:"Сексапильная Монашка Рэнди"}
WORDS["Shaman Token"]={1:"Шаман Токен"}
WORDS["Sharpshooter Shelly"]={1:"Меткий Стрелок Шелли"}
WORDS["Sheriff Cartman"]={1:"Шериф Картман"}
WORDS["Shieldmaiden Wendy"]={1:"Воительница Венди"}
WORDS["Sixth Element Randy"]={1:"Шестой Элемент Рэнди"}
WORDS["Smuggler Ike"]={1:"Контрабандист Айк"}
WORDS["Space Warrior Token"]={1:"Космовоитель Токен"}
WORDS["Stan of Many Moons"]={1:"Стэн Тысячи Лун"}
WORDS["Stan the Great"]={1:"Стэн Великий"}
WORDS["Starvin' Marvin"]={1:"Голодный Марвин"}
WORDS["Storyteller Jimmy"]={1:"Расказзчик Джимми"}
WORDS["Swashbuckler Red"]={1:"Флибустьер Рыжик"}
WORDS["Swordsman Garrison"]={1:"Мечник Гаррисон"}
WORDS["Terrance and Phillip"]={1:"Терренс и Филипп"}
WORDS["Terrance Mephesto"]={1:"Терренс Мефесто"}
WORDS["The Amazingly Randy"]={1:"Удивительный Рэнди"}
WORDS["The Master Ninjew"]={1:"Мастер Евредзюцу"}
WORDS["Towelie"]={1:"Полотенчик"}
WORDS["Transmogrify"]={1:"Метаморфоза"}
WORDS["Underpants Gnomes"]={1:"Кальсонные Гномы"}
WORDS["Unholy Combustion"]={1:"Нечестивый Взрыв"}
WORDS["Visitors"]={1:"Гости"}
WORDS["Warboy Tweek"]={1:"Боец Твик"}
WORDS["Witch Doctor Token"]={1:"Знахарь Токен"}
WORDS["Witch Garrison"]={1:"Ведьма Гаррисон"}
WORDS["Youth Pastor Craig"]={1:"Молодой Пастор Крэйг"}
WORDS["Zen Cartman"]={1:"Дзен Картман"}
WORDS["Unknown"]={1:"Неизвестно"}
WORDS["Fastpass"]={1:"Скороход"}
WORDS["The Coon"]={1:"Енот"}
WORDS["Tupperware"]={1:"Контейнер"}
WORDS["Call Girl"]={1:"Девушка по Вызову"}
WORDS["Mosquito"]={1:"Москит"}
WORDS["Human Kite"]={1:"Человек-Воздушный Змей"}
WORDS["Super Fart"]={1:"Суперпердеж"}
WORDS["Toolshed"]={1:"Инструмент"}
WORDS["Chomper"]={1:"Капкан"}
WORDS["Mysterion"]={1:"Мистерион"}
WORDS["Professor Chaos"]={1:"Профессор Хаос"}
WORDS["Lava!"]={1:"Лава!"}
WORDS["Doctor Timothy"]={1:"Доктор Тимоти"}
WORDS["Captain Diabetes"]={1:"Капитан Диабет"}
WORDS["Big Mesquite Murph"]={1:"Большой Мерф"}
WORDS["Sorceress Liane"]={1:"Колдунья Лиэн"}
WORDS["President Garrison"]={1:"Президент Гаррисон"}
WORDS["Mint-Berry Crunch"]={1:"Мятно-Ягодный Хруст"}
WORDS["Jesus"]={1:"Иисус"}
WORDS["Mayor McDaniels"]={1:"Мэр МакДэниелс"}
WORDS["Sizzler Stuart"]={1:"Шокер Стюарт"}
WORDS["Super Craig"]={1:"Супер Крэйг"}
WORDS["Wonder Tweek"]={1:"Чудо Твик"}
WORDS["ThunderBird"]={1:"Буревестник"}
WORDS = {**WORDS,**({word.upper() : WORDS[word] for word in WORDS})}
	
#Navigation
WORDS["News"]={1:"Новости"}
WORDS["Decks"]={1:"Колоды"}
WORDS["Themes"]={1:"Темы"}
WORDS["Cards"]={1:"Карты"}
WORDS["Teams"]={1:"Команды"}
WORDS["Players"]={1:"Игроки"}
WORDS["Brackets"]={1:"Турнирная сетка"}
WORDS["Downloads"]={1:"Загрузки"}
WORDS["Donate"]={1:"Пожертвования"}
WORDS["About"]={1:"О нас"}
WORDS["Data"]={1:"Информация"}
WORDS["My"]={1:"Мои"}
WORDS["Team"]={1:"Команда"}
WORDS["Login"]={1:"Войти"}
WORDS["Gold"]={1:"Золотая Лига"}
WORDS["Silver"]={1:"Серебряная Лига"}
WORDS["Bronze"]={1:"Бронзовая Лига"}
WORDS["Wood"]={1:"Деревянная Лига"}
WORDS["Team Wars"]={1:"Командные Войны"}
WORDS["Team Events"]={1:"События"}
WORDS["Requests"]={1:"Запросы"}
WORDS["Applications"]={1:""}
WORDS["Vote"]={1:"Голосования"}
WORDS["Upgrade"]={1:"Прокачка"}
WORDS["Battle"]={1:"Бой"}
WORDS["Summary"]={1:"Общее"}
WORDS["History"]={1:"История"}
WORDS["Requested"]={1:"Запрашиваемые карты"}
WORDS["Donated"]={1:"Пожертвованные карты"}
WORDS["Queue"]={1:"Очередь"}

#Tables
WORDS["Filter"]={1:"Фильтры"}
WORDS["Rank"]={1:"Ранг"}
WORDS["Last"]={1:"Последний"}
WORDS["Refresh"]={1:"Обновить"}
WORDS["Total"]={1:"Общий"}
WORDS["Day"]={1:"Сегодня"}
WORDS["In % of decks"]={1:"В % колод"}
WORDS["Trend"]={1:"Популярные"}
WORDS["Score"]={1:"Счет"}
WORDS["Country"]={1:"Страна"}
WORDS["Members"]={1:"Участник"}
WORDS["Status"]={1:"Статус"}
WORDS["Min NK Level"]={1:"Мин. Ур. Новичка"}
WORDS["MMR"]={1:"Рейтинг"}
WORDS["NK"]={1:"Новичок"}
WORDS["Donated"]={1:"Пожертвовал"}
WORDS["TW"]={1:"КВ"}
WORDS["Caps"]={1:"Крышки"}
WORDS["PVP"]={1:"ПвП-бои"}
WORDS["Perfect"]={1:"Идеальные победы"}
WORDS["CHLG"]={1:"Вызовы"}
WORDS["FF"]={1:"Дружеский Бой"}
WORDS["Team"]={1:"Команда"}
WORDS["Name"]={1:"Ник"}
WORDS["Runs"]={1:"Серии"}
WORDS["Average"]={1:"Среднее"}
WORDS["Projected"]={1:"Последнее"}
WORDS["Maximum"]={1:"Максимум"}
WORDS["Role"]={1:"Должность"}
WORDS["elder"]={1:"Старейшина"}
WORDS["regular"]={1:"Участник"}
WORDS["co_leader"]={1:"Заместитель"}
WORDS["leader"]={1:"Лидер"}
WORDS["Join Date"]={1:"Принят в Клан"}
WORDS["Collection"]={1:"Список Карт"}
WORDS["N/A"]={1:"Неизвестно"} #Abbreviation for: Not Applicable
WORDS["League"]={1:"Лига"} #Example: Gold, Silver, Bronze TVT League
WORDS["Description"]={1:"Описание"}

#Keywords
WORDS["Theme"]={1:"Темы"}
WORDS["Adventure"]={1:"Приключение"}
WORDS["Fantasy"]={1:"Фэнтэзи"}
WORDS["Neutral"]={1:"Нейтральная"}
WORDS["Mystical"]={1:"Мистика"}
WORDS["Sci-Fi"]={1:"Научно-Фантастическая"}
WORDS["Superhero"]={1:"Супергерои"}
WORDS["adv"]={1:"Прикл."}
WORDS["fan"]={1:"Фэнт."}
WORDS["neu"]={1:"Нейтр."}
WORDS["mys"]={1:"Мист."}
WORDS["sci"]={1:"НФ"}
WORDS["sup"]={1:"Герои"}
 
WORDS["Rarity"]={1:"Редкость"}
WORDS["Common"]={1:"Обычная"}
WORDS["Rare"]={1:"Редкая"}
WORDS["Epic"]={1:"Эпическая"}
WORDS["Legendary"]={1:"Легендарная"}
WORDS["com"]={1:"Обыч."}
WORDS["rar"]={1:"Ред."}
WORDS["epi"]={1:"Эпич."}
WORDS["leg"]={1:"Лег."}

WORDS["Energy"]={1:"Энергия"}

WORDS["Type"]={1:"Тип"}
WORDS["Tank"]={1:"Танк"}
WORDS["Melee"]={1:"Боец"}
WORDS["Assassin"]={1:"Киллер"}
WORDS["Ranged"]={1:"Стрелок"}
WORDS["Spell"]={1:"Заклинание"}
WORDS["Trap"]={1:"Ловушка"}

#From Google Translate
