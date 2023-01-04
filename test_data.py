LONGEST_WORD_DATA = [
    'kilkudziesięciocentymetrowego',
    'kilkudziesięciocentymetrowemu',
    'kilkudziesięciocentymetrowych',
    'kilkudziesięciocentymetrowymi',
]


UNIQUE_DATA = [
    ([], []),
    ([1], [1]),
    ([1, 1], [1]),
    ([1, 1, 1, 1, 1, 1], [1]),
    ([1, 2, 3, 4, 5, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([1, 1, 2, 2, 3, 3, 4], [1, 2, 3, 4]),
]


REVERSED_WORDS_DATA = [
    ('afro', 'orfa'),
    ('agam', 'maga'),
    ('agami', 'imaga'),
    ('agar', 'raga'),
    ('agaw', 'waga'),
    ('agnat', 'tanga'),
    ('agon', 'noga'),
    ('ajer', 'reja'),
    ('akra', 'arka'),
    ('akrom', 'morka'),
    ('akronim', 'minorka'),
    ('akson', 'noska'),
    ('akt', 'tka'),
    ('aktem', 'metka'),
    ('aktom', 'motka'),
    ('aktu', 'utka'),
    ('amok', 'koma'),
    ('amonalem', 'melanoma'),
    ('anatom', 'motana'),
    ('ano', 'ona'),
    ('anyżu', 'użyna'),
    ('arak', 'kara'),
    ('aren', 'nera'),
    ('ark', 'kra'),
    ('arki', 'ikra'),
    ('arkom', 'mokra'),
    ('arom', 'mora'),
    ('asem', 'mesa'),
    ('atak', 'kata'),
    ('atlas', 'salta'),
    ('atom', 'mota'),
    ('atrap', 'parta'),
    ('atrapo', 'oparta'),
    ('atut', 'tuta'),
    ('awal', 'lawa'),
    ('axelem', 'melexa'),
    ('azotek', 'ketoza'),
    ('babek', 'kebab'),
    ('bal', 'lab'),
    ('bals', 'slab'),
    ('bar', 'rab'),
    ('bard', 'drab'),
    ('bark', 'krab'),
    ('barok', 'korab'),
    ('baw', 'wab'),
    ('bej', 'jeb'),
    ('beju', 'ujeb'),
    ('blok', 'kolb'),
    ('brak', 'karb'),
    ('buks', 'skub'),
    ('bukso', 'oskub'),
    ('buksu', 'uskub'),
    ('bul', 'lub'),
    ('but', 'tub'),
    ('buł', 'łub'),
    ('bór', 'rób'),
    ('cap', 'pac'),
    ('car', 'rac'),
    ('cel', 'lec'),
    ('celu', 'ulec'),
    ('cepak', 'kapec'),
    ('cip', 'pic'),
    ('cup', 'puc'),
    ('daj', 'jad'),
    ('dal', 'lad'),
    ('dam', 'mad'),
    ('dar', 'rad'),
    ('dał', 'ład'),
    ('der', 'red'),
    ('diw', 'wid'),
    ('dnem', 'mend'),
    ('dni', 'ind'),
    ('do', 'od'),
    ('dok', 'kod'),
    ('drag', 'gard'),
    ('drak', 'kard'),
    ('dual', 'laud'),
    ('dup', 'pud'),
    ('dur', 'rud'),
    ('dąs', 'sąd'),
    ('eh', 'he'),
    ('ej', 'je'),
    ('elewon', 'nowele'),
    ('endom', 'modne'),
    ('enolog', 'golone'),
    ('er', 're'),
    ('erkom', 'mokre'),
    ('et', 'te'),
    ('fag', 'gaf'),
    ('far', 'raf'),
    ('fart', 'traf'),
    ('fartu', 'utraf'),
    ('fiks', 'skif'),
    ('fos', 'sof'),
    ('ful', 'luf'),
    ('fum', 'muf'),
    ('fur', 'ruf'),
    ('gaj', 'jag'),
    ('gal', 'lag'),
    ('gam', 'mag'),
    ('gar', 'rag'),
    ('gil', 'lig'),
    ('glebo', 'obelg'),
    ('gnat', 'tang'),
    ('goj', 'jog'),
    ('gol', 'log'),
    ('grat', 'targ'),
    ('gros', 'sorg'),
    ('gzom', 'mozg'),
    ('gór', 'róg'),
    ('igrom', 'morgi'),
    ('ikon', 'noki'),
    ('ikro', 'orki'),
    ('ikrom', 'morki'),
    ('iks', 'ski'),
    ('ilu', 'uli'),
    ('iluż', 'żuli'),
    ('im', 'mi'),
    ('imam', 'mami'),
    ('imć', 'ćmi'),
    ('indom', 'modni'),
    ('indor', 'rodni'),
    ('iskam', 'maksi'),
    ('jadu', 'udaj'),
    ('jagło', 'ołgaj'),
    ('jaju', 'ujaj'),
    ('jalapo', 'opalaj'),
    ('jam', 'maj'),
    ('jar', 'raj'),
    ('jarko', 'okraj'),
    ('jarku', 'ukraj'),
    ('jat', 'taj'),
    ('jatom', 'motaj'),
    ('jem', 'mej'),
    ('jer', 'rej'),
    ('jufer', 'refuj'),
    ('juk', 'kuj'),
    ('juko', 'okuj'),
    ('juku', 'ukuj'),
    ('jurt', 'truj'),
    ('jurto', 'otruj'),
    ('jut', 'tuj'),
    ('już', 'żuj'),
    ('kabat', 'tabak'),
    ('kajam', 'majak'),
    ('kalk', 'klak'),
    ('kam', 'mak'),
    ('kap', 'pak'),
    ('kapo', 'opak'),
    ('kapuz', 'zupak'),
    ('kar', 'rak'),
    ('kardom', 'modrak'),
    ('kares', 'serak'),
    ('kart', 'trak'),
    ('karuk', 'kurak'),
    ('kas', 'sak'),
    ('kasat', 'tasak'),
    ('kat', 'tak'),
    ('katom', 'motak'),
    ('kawo', 'owak'),
    ('każ', 'żak'),
    ('kenel', 'lenek'),
    ('kenozo', 'ozonek'),
    ('keson', 'nosek'),
    ('ket', 'tek'),
    ('ketem', 'metek'),
    ('ketenom', 'monetek'),
    ('ketom', 'motek'),
    ('keton', 'notek'),
    ('kil', 'lik'),
    ('kilem', 'melik'),
    ('kilom', 'molik'),
    ('kim', 'mik'),
    ('kin', 'nik'),
    ('kinolem', 'melonik'),
    ('kinu', 'unik'),
    ('kip', 'pik'),
    ('kit', 'tik'),
    ('koks', 'skok'),
    ('koksu', 'uskok'),
    ('kopo', 'opok'),
    ('kor', 'rok'),
    ('korbo', 'obrok'),
    ('kors', 'srok'),
    ('kort', 'trok'),
    ('kos', 'sok'),
    ('koso', 'osok'),
    ('kot', 'tok'),
    ('koto', 'otok'),
    ('krew', 'werk'),
    ('kul', 'luk'),
    ('kuł', 'łuk'),
    ('kąp', 'pąk'),
    ('kęp', 'pęk'),
    ('kęs', 'sęk'),
    ('labo', 'obal'),
    ('ladom', 'modal'),
    ('lamo', 'omal'),
    ('las', 'sal'),
    ('lat', 'tal'),
    ('latem', 'metal'),
    ('law', 'wal'),
    ('lawo', 'owal'),
    ('leż', 'żel'),
    ('lip', 'pil'),
    ('lis', 'sil'),
    ('lobo', 'obol'),
    ('loko', 'okol'),
    ('loop', 'pool'),
    ('los', 'sol'),
    ('lotem', 'metol'),
    ('lu', 'ul'),
    ('luks', 'skul'),
    ('lup', 'pul'),
    ('lurom', 'morul'),
    ('lut', 'tul'),
    ('lutu', 'utul'),
    ('magło', 'ołgam'),
    ('mamo', 'omam'),
    ('mangan', 'nagnam'),
    ('mango', 'ognam'),
    ('mar', 'ram'),
    ('mars', 'sram'),
    ('marsu', 'usram'),
    ('mas', 'sam'),
    ('mat', 'tam'),
    ('matom', 'motam'),
    ('małym', 'myłam'),
    ('mens', 'snem'),
    ('mer', 'rem'),
    ('metraż', 'żartem'),
    ('metro', 'ortem'),
    ('miks', 'skim'),
    ('min', 'nim'),
    ('mocjo', 'ojcom'),
    ('modo', 'odom'),
    ('modro', 'ordom'),
    ('modułu', 'ułudom'),
    ('mokro', 'orkom'),
    ('moletom', 'motelom'),
    ('molu', 'ulom'),
    ('monko', 'oknom'),
    ('monotyp', 'pytonom'),
    ('mopan', 'napom'),
    ('mor', 'rom'),
    ('mordo', 'odrom'),
    ('mordu', 'udrom'),
    ('moren', 'nerom'),
    ('mores', 'serom'),
    ('morgo', 'ogrom'),
    ('mors', 'srom'),
    ('morum', 'murom'),
    ('morus', 'surom'),
    ('motał', 'łatom'),
    ('motor', 'rotom'),
    ('mur', 'rum'),
    ('mus', 'sum'),
    ('myt', 'tym'),
    ('nap', 'pan'),
    ('nar', 'ran'),
    ('nart', 'tran'),
    ('natko', 'oktan'),
    ('ner', 'ren'),
    ('net', 'ten'),
    ('niw', 'win'),
    ('no', 'on'),
    ('nogo', 'ogon'),
    ('noks', 'skon'),
    ('not', 'ton'),
    ('nur', 'run'),
    ('nys', 'syn'),
    ('nyżo', 'ożyn'),
    ('odoru', 'urodo'),
    ('odro', 'ordo'),
    ('ogar', 'rago'),
    ('okap', 'pako'),
    ('okaż', 'żako'),
    ('okryw', 'wyrko'),
    ('oktaw', 'watko'),
    ('opał', 'łapo'),
    ('oskar', 'rakso'),
    ('ot', 'to'),
    ('otaw', 'wato'),
    ('otęp', 'pęto'),
    ('par', 'rap'),
    ('pardw', 'wdrap'),
    ('part', 'trap'),
    ('pas', 'sap'),
    ('pał', 'łap'),
    ('per', 'rep'),
    ('pert', 'trep'),
    ('pokaz', 'zakop'),
    ('por', 'rop'),
    ('port', 'trop'),
    ('pot', 'top'),
    ('potu', 'utop'),
    ('pyt', 'typ'),
    ('pył', 'łyp'),
    ('pęt', 'tęp'),
    ('radu', 'udar'),
    ('rat', 'tar'),
    ('rot', 'tor'),
    ('rut', 'tur'),
    ('rwał', 'ławr'),
    ('ryż', 'żyr'),
    ('rów', 'wór'),
    ('serku', 'ukres'),
    ('skat', 'taks'),
    ('soku', 'ukos'),
    ('spał', 'łaps'),
    ('tez', 'zet'),
    ('traw', 'wart'),
    ('udał', 'ładu'),
    ('ukaż', 'żaku'),
    ('ukuł', 'łuku'),
    ('uleż', 'żelu'),
    ('wał', 'ław'),
    ('wyż', 'żyw'),
    ('wół', 'łów'),
    ('włóż', 'żółw'),
    ('wżył', 'łyżw'),
    ('zależ', 'żelaz'),
    ('zdąż', 'żądz'),
    ('zeł', 'łez'),
]


TOWER_OF_HANOI_DATA = [
    (1, "A", "B", "C",
"""\
Move disk 1 from A to B
"""),
    (2, "A", "B", "C",
"""\
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
"""),
    (3, "A", "B", "C",
"""\
Move disk 1 from A to B
Move disk 2 from A to C
Move disk 1 from B to C
Move disk 3 from A to B
Move disk 1 from C to A
Move disk 2 from C to B
Move disk 1 from A to B
"""),
    (4, "A", "B", "C",
"""\
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
Move disk 4 from A to B
Move disk 1 from C to B
Move disk 2 from C to A
Move disk 1 from B to A
Move disk 3 from C to B
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
"""),
    (6, "A", "B", "C",
"""\
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
Move disk 4 from A to B
Move disk 1 from C to B
Move disk 2 from C to A
Move disk 1 from B to A
Move disk 3 from C to B
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 5 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
Move disk 3 from B to A
Move disk 1 from C to B
Move disk 2 from C to A
Move disk 1 from B to A
Move disk 4 from B to C
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
Move disk 6 from A to B
Move disk 1 from C to B
Move disk 2 from C to A
Move disk 1 from B to A
Move disk 3 from C to B
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 4 from C to A
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
Move disk 3 from B to A
Move disk 1 from C to B
Move disk 2 from C to A
Move disk 1 from B to A
Move disk 5 from C to B
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
Move disk 4 from A to B
Move disk 1 from C to B
Move disk 2 from C to A
Move disk 1 from B to A
Move disk 3 from C to B
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
"""),
]
