# Génère la version arabe (index-ar.html) à partir de la version française (index.html).
# Usage : python3 outils/faire-version-arabe.py   (depuis le dossier petite-eclosion)
import pathlib, sys

ici = pathlib.Path(__file__).resolve().parent.parent
s = (ici / "index.html").read_text(encoding="utf-8")

def R(a, b, n=1):
    global s
    c = s.count(a)
    if c != n:
        sys.exit(f"Texte trouvé {c} fois au lieu de {n} : {a[:70]}")
    s = s.replace(a, b)

ZONES_AR = '''const ZONES=[
 {name:"البَذْر",type:"match",instr:"اربط كل صورة بالكلمة المناسبة لها.",img:true,thumb:"fleurs",
  done:"تفتّحت الزهور الأولى!",
  pairs:[["🧹","مِكْنَسَة","نستعملها لتنظيف الأرض."],
         ["🪜","سُلَّم","نصعد عليه لنصل إلى الأعلى."],
         ["⏳","سَاعَة رَمْلِيَّة","يسيل فيها الرمل لقياس الوقت."],
         ["🔑","مِفْتَاح","نفتح به الباب."],
         ["🪣","دَلْو","نملؤه بالماء للّعب أو للتنظيف."],
         ["🧺","سَلَّة","نضع فيها الفواكه أو طعام النزهة."]]},
 {name:"الغابة الصغيرة",type:"match",instr:"اربط كل كلمة بمرادفها.",thumb:null,
  done:"نبتت النباتات من جديد وعاد الجدول الصغير يغنّي!",
  pairs:[["سَعِيد","فَرْحَان","عندما يكون كل شيء بخير ونبتسم."],
         ["بَدَأَ","اِبْتَدَأَ","أن نقوم بالخطوة الأولى في عمل ما."],
         ["الخَوْف","الفَزَع","ما نشعر به أمام الخطر."],
         ["جَمِيل","حَسَن","لطيف المنظر."],
         ["أَنْهَى","أَتَمَّ","أن نصل إلى نهاية شيء ما."],
         ["هَدِيَّة","عَطِيَّة","نقدّمها في عيد الميلاد."]]},
 {name:"البركة النائمة",type:"sort",instr:"ضع كل كلمة في السلّة المناسبة.",thumb:"etang",
  done:"عاد الماء! استيقظ الشلّال والنافورة.",
  cats:[["meteo","الطقس"],["emo","المشاعر"],["metier","المهن"]],
  items:[["العَاصِفَة","meteo","نسمع فيها الرعد يدوّي."],
         ["الضَّبَاب","meteo","لا نرى شيئًا على بُعد أمتار قليلة."],
         ["المَطَر الغَزِير","meteo","مطر قويّ ومفاجئ."],
         ["الفَخْر","emo","ما نشعر به بعد نجاح جميل."],
         ["الغَضَب","emo","ما نشعر به عندما ننزعج كثيرًا."],
         ["الحُزْن","emo","ما نشعر به عندما نرغب في البكاء."],
         ["خَبَّاز","metier","يُعِدّ الخبز كل صباح."],
         ["سَبَّاك","metier","يُصلح تسرّبات الماء."],
         ["مُمَرِّضَة","metier","تعتني بالمرضى في المستشفى."]]},
 {name:"البستان",type:"match",instr:"اربط كل كلمة بضدّها.",thumb:"arbre",
  done:"أزهرت الشجرة الكبيرة ووصلت الفراشات!",
  pairs:[["سَرِيع","بَطِيء","فكّر في السلحفاة."],
         ["قَدِيم","حَدِيث","من زماننا، جديد تمامًا."],
         ["كَرِيم","بَخِيل","شخص يحتفظ بكل ماله لنفسه."],
         ["قَبِلَ","رَفَضَ","أن تقول: لا."],
         ["سَمِيك","رَقِيق","كتاب من عشر صفحات هو…"],
         ["رَبِحَ","خَسِرَ","ما يحدث عندما يسجّل الفريق الآخر نقاطًا أكثر."]]},
 {name:"القلب السحري",type:"sort",instr:"صنّف الكلمات لتوقظ قصر الحديقة.",thumb:"chateau",
  done:"",
  cats:[["obj","الأشياء"],["emo","المشاعر"],["meteo","الطقس"],["metier","المهن"]],
  items:[["شَمْعَة","obj","نشعلها لنحصل على قليل من الضوء."],
         ["دُرْج","obj","يوجد في قطعة أثاث، ونرتّب فيه أغراضنا."],
         ["مِرَشَّة","obj","نستعملها لسقي النباتات."],
         ["الفَرَح","emo","ما نشعر به عندما نكون مسرورين جدًّا."],
         ["الخَجَل","emo","ما نشعر به عندما يحمرّ وجهنا بعد خطأ."],
         ["القَلَق","emo","انشغال بال كبير."],
         ["البَرَد","meteo","حبّات صغيرة من الجليد تسقط من السماء."],
         ["البَرْق","meteo","ضوء قويّ يلمع في السماء أثناء العاصفة."],
         ["الرَّذَاذ","meteo","مطر خفيف جدًّا."],
         ["إِطْفَائِيّ","metier","يُطفئ الحرائق."],
         ["طَبِيبَة بَيْطَرِيَّة","metier","تعالج الحيوانات."],
         ["نَجَّار","metier","يعمل بالخشب."]]}
];
'''
a = s.index("const ZONES=["); b = s.index("const TOTAL=")
s = s[:a] + ZONES_AR + s[b:]

# Langue, sens de lecture, polices arabes
R('<html lang="fr">', '<html lang="ar" dir="rtl">')
R('<title>Petite Éclosion</title>', '<title>حديقتي</title>')
R('family=Fredoka:wght@500;600;700&family=Nunito:wght@500;600;700;800',
  'family=Baloo+Bhaijaan+2:wght@500;600;700;800&family=Tajawal:wght@500;700;800')
R('--display:"Fredoka","Baloo 2","Trebuchet MS",system-ui,sans-serif;', '--display:"Baloo Bhaijaan 2","Tajawal",system-ui,sans-serif;')
R('--body:"Nunito","Segoe UI",system-ui,sans-serif;', '--body:"Tajawal","Segoe UI",system-ui,sans-serif;')
R('.welcome .txt{padding:48px 0 48px 48px;', '.welcome .txt{padding-block:48px;padding-inline:48px 0;')
R('line-height:.95;margin:0;color:#4b362c;letter-spacing:-.01em;', 'line-height:1.15;margin:0;color:#4b362c;')
R('text-align:left;', 'text-align:start;')
R('.card .eyebrow{font-size:11px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;', '.card .eyebrow{font-size:12.5px;font-weight:800;')

# Textes de l'interface
T = [
 ('const GOOD=["Très bien !","Magnifique !","Le jardin sourit !","Une nouvelle feuille pousse !","C\'est ça !","Bravo !"];',
  'const GOOD=["أحسنت!","رائع!","الحديقة تبتسم!","نبتت ورقة جديدة!","هذا صحيح!","برافو!"];'),
 ('aria-label="Toucher la graine pour réveiller la zone"', 'aria-label="المس البذرة لإيقاظ هذه المنطقة"'),
 ('aria-label="Le jardin flottant et son château"', 'aria-label="الحديقة الطائرة وقصرها"'),
 ('<h1>Petite Éclosion</h1><h2>Le jardin des mots</h2>', '<h1>حديقتي</h1><h2>حديقة الكلمات</h2>'),
 ('Ce jardin a oublié ses couleurs. Chaque mot que tu apprends lui rend un peu de vie.', 'نسيت هذه الحديقة ألوانها. كل كلمة تتعلّمها تعيد إليها شيئًا من الحياة.'),
 ('Commencer à cultiver <span aria-hidden="true">→</span>', 'ابدأ الزراعة <span aria-hidden="true">←</span>'),
 ('<span>Contempler le jardin</span>', '<span>تأمّل الحديقة</span>'),
 ('aria-label="Couper le son"></button>', 'aria-label="كتم الصوت"></button>'),
 ('aria-label="Plein écran"', 'aria-label="ملء الشاشة"'),
 ('on?"Revenir au jeu":"Contempler le jardin"', 'on?"العودة إلى اللعبة":"تأمّل الحديقة"'),
 ('soundOn?"Couper le son":"Remettre le son"', 'soundOn?"كتم الصوت":"تشغيل الصوت"'),
 ('`Jardin restauré : ${pct()} %`', '`الحديقة المستعادة: ${pct()}٪`'),
 ('"Toutes les zones sont restaurées":`Zone ${S.zone+1} sur 5 · ${ZONES[S.zone].name}`', '"عادت الحياة إلى كل المناطق":`المنطقة ${S.zone+1} من 5 · ${ZONES[S.zone].name}`'),
 ('Touche la graine dorée pour réveiller cette zone', 'المس البذرة الذهبية لإيقاظ هذه المنطقة'),
 ('"Choisis une carte à gauche, puis sa réponse à droite."', '"اختر بطاقة من اليمين، ثم جوابها من اليسار."'),
 ('"Choisis un mot, puis touche son panier."', '"اختر كلمة، ثم المس سلّتها."'),
 ('"Choisis d\'abord une carte à gauche."', '"اختر أولًا بطاقة من اليمين."'),
 ('"Choisis d\'abord un mot."', '"اختر كلمة أولًا."'),
 ('"Presque… réessaie. "', '"اقتربت… حاول مرة أخرى. "'),
 ('<span class="eyebrow">Zone restaurée</span>', '<span class="eyebrow">منطقة مستعادة</span>'),
 ('id="next">Continuer à cultiver</button>', 'id="next">واصل الزراعة</button>'),
 ('<span class="eyebrow">Jardin restauré : 100 %</span><h3>Ton jardin a fleuri !</h3><p>Chaque mot était une graine. Regarde tout ce que tu as fait pousser.</p><p class="big">Tu as cultivé ${TOTAL} mots en 5 zones.</p>',
  '<span class="eyebrow">الحديقة المستعادة: 100٪</span><h3>أزهرت حديقتك!</h3><p>كانت كل كلمة بذرة. انظر إلى كل ما زرعته!</p><p class="big">زرعت ${TOTAL} كلمة في 5 مناطق.</p>'),
 ('id="admire">Contempler mon jardin</button>', 'id="admire">تأمّل حديقتي</button>'),
 ('id="again">Recommencer</button>', 'id="again">ابدأ من جديد</button>'),
]
for a_, b_ in T:
    R(a_, b_)

(ici / "index-ar.html").write_text(s, encoding="utf-8")
print("index-ar.html écrit")
