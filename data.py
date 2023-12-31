import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS bicycle_paths')
cursor.execute('DROP TABLE IF EXISTS bicycle_parking')
cursor.execute('DROP TABLE IF EXISTS bicycle_repair_shop')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS bicycle_paths (
        id INTEGER PRIMARY KEY,
        streets TEXT,
        latitude REAL,
        longitude REAL,
        approximate_length REAL,
        description TEXT
    )
''')

# Створення таблиці bicycle_parking
cursor.execute('''
    CREATE TABLE IF NOT EXISTS bicycle_parking (
        id INTEGER PRIMARY KEY,
        streets TEXT,
        latitude REAL,
        longitude REAL,
        additional_parking INTEGER,
        places INTEGER
    )
''')

# Створення таблиці bicycle_repair_shop
cursor.execute('''
    CREATE TABLE IF NOT EXISTS bicycle_repair_shop (
        id INTEGER PRIMARY KEY,
        streets TEXT,
        latitude REAL,
        longitude REAL,
        site TEXT,
        description TEXT
    )
''')

bicycle_paths_data = [
    ('Величковського І.', 49.8745839253055, 23.937036751132258, 1, 'Міська'),
    ('Панаса В., сотника', 49.874401853426896, 23.937916502387324, 1, "Міська"),
    ('Шевченка Т.', 49.871196755169855, 23.94677832995975, 3, "Міська"),
    ('Шевченка Т.', 49.85426094654415, 23.986753008345605, 3.5, "Міська"),
    ('Левандівська', 49.84928393852439, 23.997052416893265, 0.5, "Міська"),
    ('Залізнична', 49.84823303446298, 23.996880713010867, 0.5, "Міська"),
    ('Залізнична', 49.848233018074595, 23.997824844401748, 0.5, "Міська"),
    ('Шевченка Т.', 49.848341262888944, 24.000850360851178, 6.5, "Міська"),
    ('Героїв України', 49.842422293774774, 24.017544074664332, 0.5, "Міська"),
    ('Гоголя М.', 49.84095632279101, 24.018573975336242, 0.5, "Міська"),
    ('Оргієнка І.', 49.841924375010265, 24.020591023454532, 0.5, "Міська"),
    ('Листопадового Чину', 49.839047751197555, 24.01857389614295, 1, "Міська"),
    ('Святого Юра, пл.', 49.83802429491816, 24.01599894991258, 0.3, "Міська"),
    ('Святого Юра, пл.', 49.837664721965915, 24.01432524754353, 0.2, "Міська"),
    ('Митрополита Андрея', 49.83709312782325, 24.013595667760416, 1, "Міська"),
    ('Кропивницького М., пл.', 49.83663682875716, 24.00621425799716, 0.5, "Міська"),
    ('Бандери С.', 49.835876091221714, 24.00713690029304, 3.5, "Міська"),
    ('Коновальця Є.', 49.83418857548978, 24.01026962989015, 3.5, "Міська"),
    ('Єферомова С.', 49.830143073848575, 24.005269857250294, 0.5, "Міська"),
    ('Художня', 49.83045325790126, 24.003231404614475, 0.3, "Міська"),
    ('Сельських', 49.830135125206915, 24.001707906676884, 0.5, "Міська"),
    ('Залізнянка М.', 49.82940199586116, 24.00009856140094, 0.5, "Міська"),
    ('Гіпсова', 49.82864115494019, 24.00042039282324, 1.5, "Міська"),
    ('Чернігівицька', 49.83910817864648, 23.998146328657267, 1, "Міська"),
    ('Городоцька', 49.83576110112489, 23.99724497345844, 1.8, "Міська"),
    ('Городоцька', 49.83015924273077, 23.967075451294086, 2.5, "Міська"),
    ('Курмановича В., ген.', 49.83300889930789, 23.959393773004, 2.5, "Міська"),
    ('Городоцька', 49.822573077024444, 23.924117156939214, 0.2, "Міська"),
    ('Виговського І.', 49.8254792289612, 23.96960724599178, 1.3, "Міська"),
    ('Садова', 49.82216962184894, 23.987137912359067, 0.5, "Міська"),
    ('Січових Стрільців', 49.84080507624117, 24.026041189959845, 0.5, "Міська"),
    ('Свободи, просп.', 49.84070141390881, 24.029839168689367, 0.5, "Міська"),
    ('Міцкевича А., пл.', 49.83926224269456, 24.03185611690908, 0.4, "Міська"),
    ('Воронового М.', 49.838501572168504, 24.031298189537903, 0.2, "Міська"),
    ('Коперника М.', 49.835099269217025, 24.02215714007032, 1.4, "Міська"),
    ('Князя Лева', 49.84680890074794, 24.034034369501832, 0.6, "Міська"),
    ('НВК "Школа-гімназія" "Галицька" ', 49.846075984905745, 24.034688793781104, 0.5, "Гірська"),
    ('Меморіал памяті Героїв Небесної Сотні', 49.84539144329818, 24.036212250080187, 0.3, "Гірська"),
    ('Лазнева', 49.846323366277296, 24.028144257035905, 0.5, "Міська"),
    ('Князя Мстислава Удатого', 49.846672264310165, 24.027543460643173, 0.2, "Міська"),
    ('Чорновола В., просп.', 49.84658929878332, 24.027285966824557, 0.2, "Міська"),
    ('Зернова', 49.84675525204018, 24.02651350258801, 0.3, "Міська"),
    ('Куліша П.', 49.849764519278175, 24.026084476882755, 1.4, "Міська"),
    ('Чорновола В., просп.', 49.85483349264414, 24.024024764351516, 6.5, "Міська"),
    ('Липнивського В.', 49.85744506428727, 24.02458276862307, 6, "Міська"),
    ('Хмельницького Б.', 49.863279040765384, 24.053336102576523, 7.3, "Міська"),
    ('Курядзяна', 49.86496944556227, 24.056082736753226, 1, "Міська"),
    ('Миколайчука І.', 49.86803825859186, 24.045397013881125, 0.7, "Міська"),
    ('Орлика П.', 49.87638623014232, 24.040805449236537, 1.4, "Міська"),
    ('Заозерна', 49.87223535801297, 24.01617203090312, 1.2, "За-Міська"),
    ('Замарстнівська', 49.88596499732021, 23.99420008964485, 6.4, "За-Міська"),
    ('Львівська', 49.89834402092788, 23.964846701396255, 0.4, "За-Міська"),
    ('Шевченка Т.',  49.8691562736621, 23.951284326897788, 0.7, "Міська"),
    ('Величанського І.',  49.875071938948444,  23.93635013039, 0.3, "Міська"),
    ('Панаса В., сотника',  49.87352401647196,  23.93840998913002, 0.3, "Міська"),
    ('Богданівська',  49.85748584485449, 24.0756516939119, 0.5, "Міська"),
    ('РЛС "Знесіння"',  49.84171532858898, 24.063978142583743, 0.4, "Гірська"),
    ('Пекарська',  49.8362367089515, 24.04966574219627, 0.8, "Міська"),
    ('Шімзерів',  49.83542061407145, 24.052026036750334, 0.4, "Міська"),
    ('Цетнерівка',  49.83434572141268, 24.064664477848247, 0.3, "Міська"),
    ('Личанківський парк',  49.83448399500035, 24.067239387275773, 0.4, "Гірська"),
    ('Голубця М.', 49.83354335447974, 24.07118753391783, 1.2, "Міська"),
    ('Кінцева', 49.83243652332832, 24.085735693772254, 0.4, "Міська"),
    ('Дріжджова', 49.833653743643154, 24.086594045471042, 0.4, "Міська"),
    ('Личаківська', 49.8344006273076, 24.088954404799868, 1.2, "Міська"),
    ('Львів-Винники', 49.831827731918835, 24.09509115180795, 5.3, "За-Міська"),
    ('Пасічна', 49.825654205643204, 24.075864948495035, 1.7, "Міська"),
    ('Парк "Погулянка"', 49.82066059816101, 24.074191054124206, 3.4, "Міська"),
    ('Вашингтона Дж.', 49.815899523347504, 24.073375470670477, 0.4, "Міська"),
    ('Волоська', 49.829516162727415, 24.03500996973724, 0.4, "Міська"),
    ('Снопківська', 49.8261538425485, 24.038507407903516, 0.6, "Міська"),
    ('Свенціцького І.', 49.825253661196435, 24.038614658239197, 0.3, "Міська"),
    ('Стуса В.', 49.82197555491383, 24.040910478181893, 3.3, "Міська"),
    ('Липова Алея', 49.817809798253194, 24.046875499177688, 0.6, "Міська"),
    ('Липова Алея', 49.817809798253194, 24.046875499177688, 0.6, "Міська"),
    ('Червоної Калини, просп.', 49.81332129231512, 24.047776529504922, 4, "Міська"),
    ('Угорська', 49.81121663614716, 24.045480486491442, 0.8, "Міська"),
    ('Угорська', 49.81365225341747, 24.039172073241147, 0.6, "Міська"),
    ('Святого Івана II, просп.', 49.799971637569065, 24.040201468157942, 2, "Міська"),
    ('Хорткевича', 49.797546622400944, 24.04075926358237, 0.8, "Міська"),
    ('Червоної Калини, просп.', 49.783615505516536, 24.060285040440736, 0.2, "Міська"),
    ('Червоної Калини, просп.', 49.79005884425735, 24.059984901546688, 0.2, "Міська"),
    ('Сихівска', 49.79580316537016, 24.072387592086695, 1.4, "Міська"),
    ('Зелена', 49.80489720573801, 24.064856375234122, 7.7, "Міська"),
    ('Стрийська', 49.7990041788323, 24.01913013234822, 1.6, "Міська"),
    ('Стрийська', 49.805038868008225, 24.020632409420916, 1.6, "Міська"),
    ('Наукова', 49.806039530852765, 23.984455052488624, 4.3, "Міська"),
    ('Трускавецька', 49.801278386607464, 23.982738252760033, 0.7, "Міська"),
    ('Пулюя І.', 49.80224721450405, 23.985828177472367, 0.3, "Міська"),
    ('Ряшівська', 49.80626103641817, 23.980592705918482, 0.6, "Міська"),
    ('Кульпарківська', 49.81052666641762, 23.984455238364273, 0.5, "Міська"),
    ('Володимера Великого', 49.811356855217824, 23.991579173327555, 0.5, "Міська"),
    ('Володимера Великого', 49.81135674651384, 23.99784477259285, 0.2, "Міська"),
    ('Княгині Ольги', 49.807509471573525, 24.00020494170513, 3.2, "Міська"),
    ('Володимера Великого', 49.81060922003859, 24.004410746313052, 0.3, "Міська"),
    ('Володимера Великого', 49.809363604775676, 24.011448765070458, 0.3, "Міська"),
    ('Свхарова А., акад', 49.824392432981796, 24.014067206720814, 0.9, "Міська"),
    ('Стрийська', 49.82289812450965, 24.0220493464596, 0.9, "Міська"),
    ('Дібровна', 49.82242638370817, 24.03771332472836, 0.6, "Міська"),
    ('Гіпсова', 49.82664139502139, 23.996643784326917, 0.8, "Міська"),
    ('Залізняка М.', 49.829366084089166, 24.000785200923804, 0.6, "Міська"),
    ('Сельських', 49.83003698247706, 24.00139676839825, 0.6, "Міська"),
    ('Художня', 49.83043119049046, 24.003306505059843, 0.5, "Міська"),
    ('Єфремова С.', 49.83012613951489, 24.00561317705301, 0.5, "Міська"),
    ('Коперника М.', 49.83510708637636, 24.022693578677906, 2.1, "Міська"),
]

cursor.executemany('''
INSERT INTO bicycle_paths (streets, latitude, longitude, approximate_length, description) 
VALUES ( ?, ?, ?, ?, ?)
''', bicycle_paths_data)

bicycle_parking_data = [
    ('Брюховицька', 49.86497300298189, 23.970681762008176, None, 5),
    ('Величковьского I.', 49.87522402177994, 23.933885202683218, None, None),
    ('Шевченка Т.', 49.8708683604364, 23.956922364637364, None, 3),
    ('Шевченка Т.', 49.86890299542364, 23.95318733125322, None, None),
    ('Шевченка Т.', 49.86874901983396, 23.954030203537467, None, 5),
    ('Брюховицький', 49.86495831149194, 23.97058252031246, None, 5),
    ('с. Зимна Вода, Яворівська', 49.82704436996187, 23.911961650082503, None, None),
    ('с. Зимна Вода, Яворівська', 49.82533413288327, 23.91492808305831, 1, 3),
    ('с. Зимна Вода, Яворівська', 49.824839272542455, 23.917465415781635, None, None),
    ('Дозвільна', 49.8267890669675, 23.95838501101445, None, None),
    ('Дозвільна', 49.82807958156537, 23.957848626228888, None, 1),
    ('Городоцька', 49.82783895024554, 23.951550830541287, 1, 12),
    ('Євгена Патона', 49.824757875593264, 23.952406321870964, 1, 14),
    ('Городоцька', 49.83032553407336, 23.965734362437022, None, None),
    ('Городоцька', 49.83129373791071, 23.971281174628153, None, None),
    ('Євгена Патона', 49.82319672000005, 23.960342861867403, None, 4),
    ('Євгена Патона', 49.82371896520954, 23.96175908064261, None, 2),
    ('Євгена Патона', 49.823175708215125, 23.963513211370273, None, 4),
    ('Євгена Патона', 49.82329325801563, 23.966511906355272, None, 4),
    ('Антонова Голова', 49.826030736564434, 23.972933186322894, None, 25),
    ('Виговського І.', 49.82398550845491, 23.969446252566463, None, 5),
    ('Виговського І.', 49.82609609553385, 23.96906010450376, None, 8),
    ('Виговського І.', 49.82537324238525, 23.968711389634205, None, 5),
    ('Виговського І.', 49.824850720496066, 23.968964835065396, 1, 7),
    ('Люблінська', 49.819547549561456, 23.966216710005824, None, 3),
    ('Люблінська', 49.822640540146445, 23.974799851040576, None, None),
    ('Виговського І.', 49.822916593272495, 23.97005774791174, None, 1),
    ('Люблінська', 49.82132796803799, 23.971162744951044, None,  2),
    ('Люблінська',  49.8204345878183, 23.976924055256248, 1, 10),
    ('Калнишевського П.', 49.848969368952474, 23.971464297168943, None, 4),
    ('Рудненська', 49.837148522596095, 23.96994032176559, None, 7),
    ('Котигорошко', 49.84481472836235, 23.961844444862475, None, 3),
    ('Роксоляни', 49.84538407544124, 23.96489009695539, None, 10),
    ('Повітряна', 49.84571595019336, 23.96561966682181, None, 5),
    ('Широка', 49.84478729330005, 23.961845784819374, None, 3),
    ('Повітряна', 49.845949421989026, 23.969160169297012, None, 1),
    ('Повітряна', 49.84506747925962, 23.969044798451737, None, 4),
    ('Широка', 49.84236681337229, 23.96723152489861, None, 5),
    ('Широка', 49.842042780867594, 23.964774624030643, None, 7),
    ('Косинського К.', 49.842997214220894, 23.964222132193854, None, 1),
    ('Низинна', 49.84114803000964, 23.97431648315815, None, 3),
    ('Широка', 49.84252147367445, 23.971641054143866, 1, 9),
    ('Широка', 49.84270711648567, 23.97215336042463, None, 3),
    ('Сяйво', 49.84502904657075, 23.981779842049452, None, None),
    ('Повітряна', 49.845525274980794, 23.979025251996227, None, 3),
    ('Сяйво', 49.84110681657539, 23.97972243839229, None, None),
    ('Широка', 49.84289559323078, 23.980690783755826, None, 1),
    ('Сяйво', 49.838276514314245, 23.978475101902486, None, 5),
    ('Степанівни О.', 49.84276166686301, 24.00786674206852, None, 6),
    ('Братів Міхнвських', 49.8428799273292, 24.005071903495868, None, 3),
    ('Шевченка Т.', 49.851172537645006, 23.99292192046411, None, 40),
    ('Шевченка Т.', 49.850656974098364, 24.00033011185248, None, 1),
    ('Шевченка Т.', 49.84997598454413, 24.00010477949666, None, 2),
    ('Шевченко Т.', 49.84936758139012, 23.99980434879485, 1, 3),
    ('Турянського. О', 49.84827910001745, 24.004484727678058, None, None),
    ('Бортнянського Д.', 49.84565497105316, 24.005211492628415, None, 1),
    ('Шевченка Т.', 49.84720080454445, 24.005359077324812, 1, 9),
    ('Миколайчкука І.', 49.87486849916942, 24.042682920101065, None, None),
    ('Липи Ю.', 49.86655153820971, 24.01656875900433, None, 2),
    ('Мазепи І., гетьм.', 49.87016007225364, 24.024213154489455, 1, 10),
    ('Тичини П.', 49.86916421498485, 24.03521546220209, None, 4),
    ('Мазепи І., гетьм.', 49.87171525601678, 24.034625486123424, 2, 19),
    ('Хмельницького Б.', 49.863880380073624, 24.056822976320646, 1, 10),
    ('Хмельницького Б.', 49.861363035201315, 24.052367751902477, None, 23),
    ('Хмельницького Б.', 49.87482523624401, 24.062456032980897, None, 4),
    ('Хмельницького Б.', 49.872399717886324, 24.062509575987907, None, None),
    ('Хмельницького Б.', 49.87034979645746, 24.059698554262617, 1, 8),
    ('Чигиринська.', 49.870861126205156, 24.059698554262617, None, 2),
    ('Грінченка Б.', 49.87225017662918, 24.05558415171573, None, 1),
    ('Хмельницького Б.', 49.85582993246913, 24.047016550321615, None, 2),
    ('Опришівська', 49.85327868749248, 24.043207732631867, None, 9),
    ('Старознеська', 49.85177972195954, 24.05381841945318, 2, 27),
    ('Ніжинська', 49.84118502340737, 24.056328510839283, None, 6),
    ('Личнківська', 49.83628164804762, 24.074647674313066, None, None),
    ('Черемшини М.', 49.83253499848982, 24.064321082258775, None, None),
    ('Вахнянина А.', 49.82874220875213, 24.06000796128583, None, 7),
    ('Зелена', 49.81404783652478, 24.06298994905289, None, 7),
    ('Пасічна', 49.81548022205647, 24.079437205715426, None, 1),
    ('Вшингтона Дж.', 49.81579885209023, 24.073783159583087, None, 1),
    ('Вшингтона Дж.', 49.81667754932161, 49.81667754932161, 1, 4),
    ('Самчука У.', 49.82383565523339, 24.031823290832076, 2, 15),
    ('Хуторівка', 49.801669570579776, 24.038774612629854, None, None),
    ('Стрийська', 49.790269188670074, 24.019108313284168, None, None),
    ('с. Сокільники, Стрийська', 49.77374314614822, 24.01328727433266, 1, 6),
    ('Червоної Калини, просп.', 49.78498317020784, 24.06232356244839, 1, 8),
    ('Старознеська', 49.78597997378216, 24.06508089640184, None, 4),
    ('Скрипника М.', 49.78936422396558, 24.059341146879248, None, None),
    ('Володимера Великого', 49.809997716519014, 24.008455465686662, None, 3),
    ('Гашека Я.', 49.79755537565474, 24.022847589693242, None, None),
    ('Рубчака І.', 49.80668929543822, 24.010772742055252, None, None),
    ('Наукова', 49.80331604862073, 24.011963495357474, 1, 13),
    ('Володимера Великого', 49.80821155095176, 24.019978086113646, 1, 5),
    ('Стрийська', 49.813109192698924, 24.019769078070862, 1, 2),
    ('Стрийська', 49.81626272039693, 24.023121948016943, None, 8),
    ('Козельницька', 49.817694800993735, 24.024827881104866, 1, 40),
    ('Героїв Крут', 49.81619902369419, 24.04133938940849, None, None),
    ('Литвиненка С.', 49.813291670420234, 24.040320036219168, None, None),
    ('Камянецька', 49.812205384319284, 24.040395092575153, None, 8),
    ('Угорська', 49.81156859585222, 24.045217646315397, None, 4),
    ('Луганська', 49.80889308976965, 24.045764702533415, 1, 10),
    ('Угорська', 49.80943103331088, 24.0479024313483, 1, 14),
    ('Луганська', 49.806362175509825, 24.0589878011994, None, 3),
    ('Манастирського А.', 49.80035259554535, 24.05989413305634, None, 4),
    ('Зелена', 49.802057488672396, 24.067667194197828, None, None),
    ('Червоної Калини, просп.', 49.798669077156454, 24.05008260731764, 1, 4),
    ('Червоної Калини, просп.', 49.79526861142597, 24.055908186243563, None, 7),
    ('Зубрівська', 49.794963172492785, 24.061615876837, 1, 17),
    ('Червоної Калини, просп.', 49.79112815452876, 24.058954984303828, None, 4),
    ('Червоної Калини, просп.', 49.792408729601725, 24.05877264827844, 1, 6),
    ('Княгині Ольги', 49.818129163029624, 24.004861666072856, None, 3),
    ('Книгині Ольги', 49.82348646741026, 24.00905147117411, None, None),
    ('Чупринки Т.,ген.', 49.823732607047795, 24.00224407948581, 1, 7),
    ('Сахарова А.,акад.', 49.821108498162694, 24.01940999591606, 4, 16),
    ('Княгині Ольги', 49.80083227258466, 23.99874555302633, None, 3),
    ('Володимира Великого', 49.810994545903384, 24.000215814838967, None, 2),
    ('Княгині Ольги', 49.809029425421166, 24.000076259475165, 2, 13),
    ('Княгині Ольги', 49.80624539968449, 23.99979183186328, 1, 12),
    ('Наукова', 49.80484903712463, 24.0009987601887, None, 2),
    ('Наукова', 49.804072410955, 24.005129302869403, None, 4),
    ('Наукова', 49.80359392709208, 23.999094352272913, 1, 7),
    ('Наукова', 49.803541948969, 24.003187374288537, 1, 6),
    ('Наукова', 49.80500813561945, 23.985034363131547, None, None),
    ('Володимира Великого', 49.81232572265894, 23.988478600123518, 1, 7),
    ('Володимира Великого', 49.81148352815132, 23.991654279936938, None, 5),
    ('Виговського І.', 49.81311468069163, 23.97971323104054, None, 7),
    ('Виговського І.', 49.8146921928204, 23.979981515557927, 1, 5),
    ('Кульпарківська', 49.80691285183063, 23.980120667214376, None, 10),
    ('Кульпарківська', 49.80897486247352, 23.9855065931389, None, 2),
    ('Симоненка В.', 49.808704134961935, 23.98785618166215, None, 1),
    ('Щирецька', 49.80978708243438, 23.979595076746065, 1, 10),
    ('Ширецька', 49.81014347883999, 23.97715429725061, 1, 11),
    ('Коновальця Є.', 49.82493638268583, 23.995399176793363, None, 6),
    ('Окружна', 49.82742806978279, 23.984413023842365, None, None),
    ('Порохова', 49.82854852506813, 23.98934830262276, None, 7),
    ('Окружна', 49.830313823951, 23.981291072634022, None, 5),
    ('Петлюри С.', 49.81937209288802, 23.983103780406253, None, 5),
    ('Петлюри С.', 49.82261021034782, 23.979971114981627, 1, 3),
    ('Любінська', 49.8244303339722, 23.97891977137963, None, 3),
    ('Садова', 49.821571518622044, 23.989830807805888, None, None),
    ('Кульпарківська', 49.82073829611986, 23.99004534858403, 1, 3),
    ('Городоцька', 49.831110721502895, 23.97114169307892, None, 8),
    ('Вівсяна', 49.83014250075489, 23.965659253483135, None, None),
    ('Патона Є.', 49.82353287752414, 23.960991966152747, 1, 6),
    ('Патона Є.', 49.82324229440736, 23.963577586727354, None, 4),
    ('Патона Є.', 49.82322807757322, 23.96648508173775, None, 4),
    ('Караджича В.', 49.825921236549696, 23.97291172425036, None, 25),
    ('Виговського І.', 49.82405928415836, 23.969328239199108, None, 5),
    ('Виговського І.', 49.82549812463415, 23.969006435878136, 2, 19),
    ('Кричевського М.', 49.81948412656377, 23.96620597861077, None, 3),
    ('Любінська', 49.8224600758165, 23.97467109836702, None, None),
    ('Любінська', 49.82124260462466, 23.97115201264625, None, 2),
    ('Виговського І.', 49.82285446894155, 23.96975733988755, None, 1),
    ('Любінська', 49.8203175707342, 23.976924050405565, 1, 10),
    ('Руставелі Ш.', 49.830244876649076, 24.03454866303537, None, 3),
    ('Севери І.', 49.825953683899876, 24.040073799378018, None, 4),
    ('Зелена', 49.823915281019076, 24.0542571428897, 1, 5),
    ('Пекарська', 49.83610616399871, 24.049773024435982, None, None),
    ('Пекарська', 49.836548714455844, 24.053002401202388, None, None),
    ('Тарнавського М., ген.', 49.827012928055424, 24.04392547012643, None, 3),
    ('Зелена', 49.830154927670364, 24.045534915236804, None, 4),
    ('Зелена', 49.83235560279366, 24.043458990370258, None, 2),
    ('Левицького К.', 49.83257342707983, 24.045910522326707, None, None),
    ('Левицького К.', 49.83379443249483, 24.044542655363827, None, None),
    ('Пекарська', 49.835925596348225, 24.045964305193085, None, 4),
    ('Тершаковців', 49.83487062739736, 24.04274026739287, 29, 9),
    ('Кирила і Мефодія', 49.83253711768668, 24.032542478932267, None, None),
    ('Петрушевича Є., пл.', 49.83298551806162, 24.038716902123035, 1, 19),
    ('Франка І.', 49.83491267464461, 24.03625473035827, None, 1),
    ('Грушевського М.', 49.83475025386737, 24.03387830204404, None, 7),
    ('Саксаганського П.', 49.835635476652506, 24.034511335933527, 1, 12),
    ('Клепарівська', 49.847821027574696, 24.01729753713022, None, 4),
    ('Замарстинівська', 49.862613662580834, 24.028423881409307, 1, 8),
    ('Замарстинівська', 49.85876998701542, 24.02872412717921, None, 5),
    ('Торфяна', 49.86099603144668, 24.022501535588184, None, 3),
    ('Окуневського Т.', 49.860035155902395, 24.019121934494006, None, 1),
    ('Чорновола В.,просп.', 49.8618252948713, 24.018521197982572, None, 10),
    ('Чорновола В.,просп.', 49.86315930497182, 24.018682184889407, 1, 19),
    ('Джерельна', 49.84988072201742, 24.022200668545995, None, 13),
    ('Під Дубом', 49.85149378317877, 24.021750127359336, None, 3),
    ('Чорновола В.,просп.', 49.85210956268137, 24.02613821807213, None, None),
    ('Кушевича С.', 49.85134904845185, 24.027672399979227, None, 10),
    ('Під Дубом', 49.85051513904826, 24.025735823162684, 1, 14),
    ('Заводська', 49.85405466389999, 24.03070875298617, None, 7),
    ('Лемківська', 49.85418606090774, 24.028026567042595, 1, 18),
    ('Чорновола В.,просп.', 49.85897179124882, 24.021879183095827, 2, 15),
    ('Чорновола В.,просп.', 49.85562472176737, 24.024550506725586, 2, 29),
    ('Двірцева, пл.', 49.840037499375185, 23.996655068769847, 1, 19),
    ('Городоцька', 49.83444641527792, 23.987814333728124, None, None),
    ('Городоцька', 49.83475065072995, 23.991698159596936, 1, 5),
    ('Городоцька', 49.83528302549015, 23.994444745741554, 1, 2),
    ('Городоцька', 49.835352151803015, 23.99631155386559, 1, 18),
    ('Залізняка М.', 49.82942194996015, 23.999535302022963, 1, 15),
    ('Героїв УПА', 49.82988203009128, 23.995249179152502, 1, 13),
    ('Чупринки Т.,ген.', 49.827153062124005, 24.00668593034143, None, 7),
    ('Чупринки Т.,ген.', 49.82974703326827, 24.008445555494653, None, 4),
    ('Чупринки Т.,ген.', 49.831102829046486, 24.010859584017442, 2, 21),
    ('Горбачевського І.', 49.82866691844122, 24.01136373498789, 1, 6),
    ('Героїв УПА', 49.83456988514643, 24.004819432699755, None, 3),
    ('Мельника А.', 49.830892250906615, 24.005784869078425, 1, 8),
    ('Героїв УПА', 49.8327993271673, 23.99940133252714, 2, 89),
    ('Сахарова А.,акад.', 49.829272511507256, 24.014775507604394, None, 5),
    ('Лукаша М.', 49.827359316739006, 24.014839800864365, None, 4),
    ('Братів Тимошенків', 49.831061703536264, 24.019828830451022, None, 2),
    ('Похила', 49.82809624321676, 24.02298296458559, None, 3),
    ('Болгарська', 49.82964761298332, 24.025000036861343, 1, 10),
    ('Шептицьких', 49.83812768408199, 24.01040926726076, None, None),
    ('Шептицьких', 49.83715158896859, 24.00836003250571, 1, 6),
    ('Шевченка Т.', 49.84458918565881, 24.01283423645078, None, 3),
    ('Шевченка Т.', 49.84297764429849, 24.01746363196861, None, 10),
    ('Городоцька', 49.8401787538374, 24.013762091654357, 1, 18),
    ('Огієнка І.', 49.84125517569636, 24.020880672357915, None, 4),
    ('Листопадового Чину', 49.840134929551134, 24.02085916834215, None, 15),
    ('Котляревського І.', 49.83248853594405, 24.01452351498776, None, 1),
    ('Святого Юра, пл.', 49.837601932706455, 24.0154839516354, None, None),
    ('Русових', 49.83410993094348, 24.009561528088515, None, 1),
    ('Бандери С.', 49.83518187984318, 24.010827566913164, 1, 11),
    ('Венеціанова О.', 49.83381382284195, 24.024158001545757, None, None),
    ('Коперника М.', 49.834913790151276, 24.02223223373603, None, None),
    ('Коперника М.', 49.834267928894036, 24.02145973581699, 1, 8),
    ('Брюллова К.', 49.83427625318895, 24.019431999448763, None, 4),
    ('Професорська', 49.83563700167472, 24.018761508039557, 1, 24),
    ('Бандери С.', 24.015998904614587, 24.01641732934566, 1, 25),
    ('Устияновича М.', 49.83693935324067, 24.017050323939394, None, 6),
    ('Митрополита Андрея', 49.83630314954215, 24.014786527981773, 3, 30),
    ('Дорошенка П.', 49.83711294810965, 24.023702165861152, 1, 12),
    ('Словацького', 49.83796545943836, 24.025853318741873, 1, 3),
    ('Дудаєва Дж.', 49.836180476817546, 24.03037005501969, None, 5),
    ('Стефаника В.', 49.8365747098749, 24.02823504701559, None, 3),
    ('Ліста Ф.', 49.83795495858283, 24.03018237523663, 1, 2),
    ('Дорошенка П.', 49.839248442716354, 24.028015218247095, None, 1),
    ('Коперника М.', 49.83832956694205, 24.027655766474723, 1, 14),
    ('Григоренка П., ген., пл.', 49.84204388614216, 24.0240993347844, None, None),
    ('Проїзд Крива Липа', 49.84081013192199, 24.028012600854115, 1, 12),
    ('Університетська', 49.84030097575744, 24.023804221405925, 1, 42),
    ('Січових Стрільців', 49.83944186225982, 24.024919977386528, None, 3),
    ('Січових Стрільців', 49.840340831518404, 24.025434995437884, 1, 22),
    ('Кирила і Мефодія', 49.83245977800155, 24.032472738748204, None, None),
    ('Петрушевича Є., пл.', 49.833020826529086, 24.038797369329185, 1, 19),
    ('Франка І.', 49.83490583773185, 24.036238636926306, None, 1),
    ('Грушевського М.', 49.834771017777506, 24.03388366728812, None, 7),
    ('Саксаганського П.', 49.8356527828297, 24.034484514737443, 1, 12),
    ('Леонтовича М.', 49.843201987010296, 24.02056961894304, None, 8),
    ('Шолом-Алейхема Ш.', 49.84399023023438, 24.022361355521944, 1, 23),
    ('Хмельницького Б.', 49.84668372060517, 24.030858649691883, None, 5),
    ('сквер на розі вул. Вічевої та вул. Гонти І.', 49.84484473919081, 24.03349784969975, None, None),
    ('Лесі Українки', 49.84435382261659, 24.032575155485027, None, None),
    ('Краківська', 49.84465116738884, 24.031491562500634, None, 4),
    ('Чорновола В.,просп.', 49.84604182525156, 24.027521976944186, None, None),
    ('Чорновола В.,просп.', 49.84681622676777, 24.027409357048523, None, 4),
    ('Князя Мстислава Удатного', 49.84670212849006, 24.02818182343702, None, 1),
    ('Вагова', 49.8456057381458, 24.025864364554696, None, 7),
    ('Котлярська', 49.84575096173283, 24.02463056253421, None, 3),
    ('Данилилиша Д.', 49.84466116880397, 24.024920193974825, 1, 4),
    ('Городоцька', 49.8436392665646, 24.025005981688587, 1, 5),
    ('Гнатюка В., акад.', 49.8425270539979, 24.026443590127148, None, 4),
    ('Курбаса Л.', 49.84274316995923, 24.027406505810823, None, 8),
    ('Свободи, просп.', 49.84196026756817, 24.02873415806768, None, 4),
    ('Театральна', 49.84360999516514, 24.030359634519364, None, 8),
    ('Театральна', 49.84313260247562, 24.03044812702382, 1, 9),
    ('Свободи, просп.', 49.842876770264674, 24.029622001455195, 1, 6),
    ('Шпитальна', 49.844568508150125, 24.026352480341295, None, 3),
    ('Свободи, просп.', 49.844696407100045, 24.02750582795432, None, 8),
    ('Лесі Українки', 49.84412576469302, 24.02882007805942, 1, 5),
    ('Стара', 49.84524432822057, 24.029120529920494, 1, 4),
    ('Руданського С.', 49.83890189959906, 24.032274523816852, None, None),
    ('Міцкевича, пл.', 49.83922009057881, 24.03071886600613, None, None),
    ('Свободи, просп.', 49.83968676875065, 24.030209269002608, 1, 2),
    ('Винниченка В.', 49.839843286753954, 24.03790716480444, None, 4),
    ('Сквер На валах', 49.84339829590627, 24.03766055071216, None, None),
    ('Староєврейська', 49.84134760760827, 24.03671633424539, 2, 10),
    ('Арсенальна', 49.841873138792764, 24.037097227229975, None, 4),
    ('Шевченка Т., просп.', 49.83680342072851, 24.033400957144845, 2, 12),
    ('Нижанківського О.', 49.83758674161889, 24.034959342842807, 1, 12),
    ('Шевченка Т., просп.', 49.838313645973926, 24.033580726622073, 1, 9),
    ('Князя Романа', 49.83865060400662, 24.034514143207982, 1, 4),
    ('Соборна, пл.', 49.83914375487656, 24.036228083969487, None, None),
    ('Богомольця О., акад.', 49.83770532202646, 24.03761739943313, None, None),
    ('Франка І.', 49.838265039722124, 24.036971014528632, 1, 10),
    ('Театральна', 49.84207451853399, 24.03120714328172, 1, 8),
    ('Театральна', 49.841272175743995, 24.031630896228968, 2, 12),
    ('Катедральна, пл.', 49.84087393752038, 24.032690345306925, None, None),
    ('Театральна', 49.84018055815551, 24.032092187854435, 2, 15),
    ('Галицька', 49.83974620907706, 24.033661251800478, 1, 16),
    ('Валова', 49.840452445887614, 24.03584190270792, 2, 13),
    ('Соборна, пл.', 49.83966313651306, 24.035104267324712, 1, 3),
    ('Коліївщини, пл.', 49.8410916280782, 24.035925077162943, 1, 2),
    ('Вірменська', 49.843399234986656, 24.03402886360572, None, 3),
    ('Федорова І.', 49.843445626099374, 24.034935446222338, 1, 11),
    ('Лесі Українки', 49.843916781821534, 24.034636401434955, 1, 6),
    ('Лесі Українки', 49.84376043655481, 24.036303376897262, 1, 18),
    ('Ринок, пл.', 49.842157681307825, 24.03258579311192, 1, 23),
    ('Галицька', 49.841441982316326, 24.032601856561584, None, 4),
    ('Ринок, пл.', 49.84196403704803, 24.034018075282315, 2, 25),
]

cursor.executemany('''
INSERT INTO bicycle_parking (streets, latitude, longitude, additional_parking, places) 
VALUES ( ?, ?, ?, ?, ?)
''', bicycle_parking_data)

bicycle_repair_shop_data = [
    ('смт. Брюховичі, Курортна', 49.904359817381746, 23.941957129569936, None, 'Послуги ремонту велосипедів. Можливість прокату.'),
    ('с. Солонка, Івасюка', 49.76463704014279, 24.013120602096198, 'https://www.facebook.com/velosolonka', 'Продаж, обслуговування та ремонт велосипедів. Реалізація велосипедних запчастин і аксесуарів.'),
    ('Володимира Великого', 49.808045036520035, 24.020436733950827, 'www.gorgany.com/lviv','Туристичне спорядження'),
    ('Енергетична', 49.816868113920556, 24.032075128042134, 'piar2.com/magazyn','Сервісне обслуговування та капітальний ремонт велосипедів, продаж запчастин до них.'),
    ('Угорська', 49.811662512397554, 24.045308844713052, 'cyclerepair.com.ua', 'Продаж велосипедів американського, польського виробництва, оригінальних запчастин та аксесуарів до них. Широкий асортимент спортивного одягу, взуття та спорядження для велоспорту. Ремонт велосипедів.'),
    ('Листопадна', 49.81360765994764, 24.046483725122343, 'http://www.fira.com.ua','Продаж спортивного та туристичного спорядження, спортивного одягу, взуття, товарів для дайвінгу і підводного полювання, окуляр'),
    ('Червоної Калини, просп.', 49.799400203330734, 24.048559152877342, 'https://service.velobikelviv.com','Велосипеди, прокат, аксесуари, запчастини, спорттовари, майстерня.'),
    ('Червоної Калини, просп.', 49.79154088312112, 24.06140115990918, None, 'Ремонт велосипедів.'),
    ('Манастирського А.', 49.80013940804866, 24.061892356797525, 'https://velogen.ua/ua/velo_shops_full/pg/271217677822533_t/', 'Продаж велосипедів, аксесуарів, запчастин до них та ремонт.'),
    ('Зубрівська', 49.800276987255344, 24.068198194375203, None, 'Продаж, обслуговування та ремонт велосипедів. Реалізація велосипедних запчастин і аксесуарів.'),
    ('Простора', 49.80074086453715, 24.07235292797843, None, 'Продаж та ремонт велосипедів. Великий вибір велозапчастин.'),
    ('Княгині Ольги', 49.80779625726584, 23.998963098937445, None, 'Послуги ремонту велосипедів. Центрування велоколіс. Продаж велосипедних запчастин і аксесуарів.'),
    ('Щирецька', 49.81357592627368, 23.976550946380968, 'https://www.pivdennij.com/mahazyn/index/index/shop/1132/', 'Ремонт та продаж велосипедів Bergamont, Haro тощо.'),
    ('Щирецька', 49.81357592627368, 23.976550946380968, 'http://comanche.lviv.ua', 'Продаж, обслуговування та ремонт велосипедів. Широкий вибір велоаксесуарів та запчастин.'),
    ('Кульпарківська', 49.820874226852574, 23.989997074772166, 'www.sport-co.com.ua' , 'Товари для туризму, одяг.'),
    ('Садова', 49.82273301248121, 23.98346333338743, None, None),
    ('Героїв УПА', 49.830089484711095, 23.99437479333943, 'https://boomerang-boardshop.ua/' ,'OOMERANG-BOARDSHOP – мультибрендовий магазин товарів для сноубордингу та лижного спорту, велосипедів.'),
    ('Городоцька', 49.83381980544742, 23.987320784503204, 'drive-sport.com.ua/magaz/lviv/' , 'Велосипеди горні та bmx, роликові ковзани та скейтборди, гірські лижи, сноуборди, льодові ковзани, туристичне спорядження, палатки.'),
    ('Городоцька', 49.832586452668, 23.97095936526995, 'https://veloleo.com.ua', 'Продаж та сервісне обслуговування велосипедів. Вело- та мотозапчастини.'),
    ('Городоцька', 49.832586452668, 23.97095936526995, 'https://megaenergy.com.ua', 'Продаж та ремонт електровелосипедів, сервісне обслуговування електромобілів.'),
    ('Широка', 49.84225149888381, 23.96322298490539, 'http://www.expertbike.ho.ua', 'Продаж запчастин та ремонт велосипедів.'),
    ('Роксоляни', 49.84937553178902, 23.96307173682419, 'https://www.eurorover.com.ua', 'Продаж, обслуговування та ремонт велосипедів. Реалізація велосипедних запчастин і аксесуарів.'),
    ('Шевченка Т.', 49.84937668897605, 23.9994690752418, 'http://cobran.com.ua', 'Продаж, ремонт велосипедів та запчастин до них.'),
    ('Квітки-Основяненка Г.', 49.846050964934896, 24.007099771839037, 'https://4ride.com.ua', 'Продаж, прокат та сервіс гірськолижного і туристичного спорядження.'),
    ('Шевченка Т.', 49.84493510035067, 24.013127950769466, 'https://www.facebook.com/JaroslavVentyk/', 'Продаж та сервісне обслуговування велосипедів. Великий асортимент велосипедних запчастин та аксесуарів.'),
    ('Сосенка М.', 49.84975536553599, 24.010114708792177, None, 'Велосипеди, запчастини, одяг, амуніція і аксесуари майстерня.'),
    ('Золота', 49.849643006233315, 24.010680646519496, None, 'Магазин пропонує великий вибір велосипедів та якісних аксесуарів та запчастин до них. При магазині діє веломайстерня'),
    ('Липинського В.', 49.86284209064918, 24.032865599849796, 'http://cyclerepair.com.ua', 'Ремонт велосипедів і дитячих візків.'),
    ('Миколайчука І.', 49.87346594333864, 24.044854095711923, 'www.facebook.com/groups/954543354594157/?fref=ts', 'Ремонт та продаж велосипедів, аксесуарів, запчастин до них. Прокат лиж.'),
    ('Зарицьких', 49.829708029902704, 24.0284922525841, 'http://www.windoftravel.com/object/266150', 'Велосипеди, деталі, аксесуари.'),
    ('Левицького К.', 49.830479741048556, 24.052379881095344, None, 'Ремонт велосипедів за благодійну пожертву.'),
    ('Зелена', 49.83186626625941, 24.044538552107714, 'https://profirider.com', 'Великий вибір товарів для літнього відпочинку-велосипеди (нові та б/у), скейти, палатки, рюкзаки, а також для зимового виду-лижі, сноуборди плюс всі необхідні аксесуари для них'),
    ('Зелена', 49.83260751795531, 24.043543489846627, 'https://vovk-sport.com/', 'Прокат, продаж, сервіс лиж та сноубордів. Термобілизна, шоломи маски та багато інших аксесуарів.'),
    ('Кривоноса М.', 49.84524750311857, 24.038816651945055, 'eurovelo.com.ua', 'Продаж, прокат та ремонт велосипедів, запчастин до них та аксесуарів.'),
    ('Кривоноса М.', 49.84502868503231, 24.040923504196723, 'https://extrasport.com.ua', 'Продаж та ремонт велосипедів. Продаж сноубордів та лиж.'),
    ('Кривоноса М', 49.84502868503231, 24.040923504196723, 'www.facebook.com/ryhtshop', 'Продаж і ремонт велосипедів, лижного спорядження.'),
    ('Чорновола, просп.', 49.85283334186261, 24.024724733253215, 'https://www.facebook.com/shalenapedalka', None),
    ('Поповича Є.', 49.83591020463242, 24.033328500923375, 'https://www.facebook.com/bikestationlviv/', 'Ремонт велосипедів.'),
    ('Котляревського І.', 49.832710613082554, 24.01563395145049, 'https://www.instagram.com/diana.garage/', 'Обслуговування та ремонт велосипедів'),
    ('Глибока', 49.83446611869789, 24.014877646284347, 'https://fanaticsport.ua', 'Туристичне спорядження, велоаксесуари.'),
    ('Шептицьких', 49.83815441963617, 24.011409725775014, 'https://www.robinzon-ua.com.ua/ukr/', 'Товари для туризму велосипеди, деталі, аксесуари.'),
    ('Озаркевича Є.', 49.839309996997954, 24.01295873927338, 'https://www.facebook.com/groups/pansportsman/about/', 'Інформація уточнюється.'),
    ('Каменярів', 49.83664781266565, 24.021502749603677, 'https://www.facebook.com/velopidkova/', 'Продаж та ремонт велосипедів.'),
    ('Дрогобича Ю.', 49.8392906763271, 24.025013847813018, 'https://sportceh.com.ua', 'Офіційний представник фірми Specialized. Продаж і сервісне обслуговування велосипедів, лиж та сноубордів.'),
    ('Свободи, просп.', 49.84012000355865, 24.030012145910284, None, 'Спорттовари, велосипеди, деталі, аксесуари.'),
    ('Гнатюка В., акад.', 49.84202966932201, 24.026241064035418, 'https://www.gorgany.com/lviv', 'Туристичне спорядження'),
    ('Городоцька', 49.84343677333652, 24.024348836389347, None, 'Продаж та обслуговування велосипедів. Прокат і продаж гірськолижного спорядження.'),
    ('Шпитальна', 49.84496312990558, 24.025061021556382, None, 'Найкраща та найдешевше веломайстерня у Львові. Ремонт велосипедів, роверів. Продаж б/у велосипедів, купити новий велосипед - ціни вас приємно здивують. Клуб любителів подорожей на велосипедах.'),
]

cursor.executemany('''
INSERT INTO bicycle_repair_shop (streets, latitude, longitude, site, description) 
VALUES (?, ?, ?, ?, ?)
''', bicycle_repair_shop_data)

conn.commit()
conn.close()
