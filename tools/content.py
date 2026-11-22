# Bilingual (en, ar) product copy for the EGE static site.
# Facts come from data/products.json; spec values are copied exactly as shown on the source.
# Every text value is a tuple: (english, arabic).

PACK = {
    "25":   (("25 kg", "25 كجم"), ("Bags", "أكياس")),
    "50":   (("50 kg", "50 كجم"), ("Bags", "أكياس")),
    "big":  (("Big bags", "أكياس جامبو"), ("Bulk option", "للكميات الكبيرة")),
    "bulk": (("Bulk", "سائب"), ("Loose, large quantities", "كميات كبيرة غير معبأة")),
}

PRODUCTS = [
  {
    "slug": "de-icing-salt", "src": "de-icing-rock-salt",
    "name": ("De-icing Salt", "ملح إذابة الجليد"),
    "tag": ("Winter road safety", "سلامة الطرق في الشتاء"),
    "card": ("Rock and sea salt for fast ice and snow melting on roads and walkways.",
             "ملح صخري وملح بحري لإذابة الجليد والثلوج بسرعة على الطرق والممرات."),
    "short": ("Rock salt and sea salt for fast, reliable ice and snow melting on roads, highways, sidewalks and driveways.",
              "ملح صخري وملح بحري لإذابة الجليد والثلوج بسرعة وكفاءة على الطرق والطرق السريعة والأرصفة ومداخل المنازل."),
    "overview": [
      ("De-icing salt lowers the freezing point of water, clearing ice and snow quickly and keeping roads and walkways safe through the winter.",
       "يعمل ملح إذابة الجليد على خفض درجة تجمد الماء، فيزيل الجليد والثلوج بسرعة ويحافظ على سلامة الطرق والممرات طوال فصل الشتاء."),
      ("We supply two types: natural rock salt mined from ancient sea deposits, and sea salt produced by evaporating seawater. Both spread easily, work in urban, suburban and rural settings, and are available in several grain sizes.",
       "نوفر نوعين: ملح صخري طبيعي مستخرج من رواسب بحرية قديمة، وملح بحري ناتج عن تبخير مياه البحر. كلاهما سهل الفرد، ومناسب للمناطق الحضرية والضواحي والريف، ومتوفر بأحجام حبيبات متعددة."),
    ],
    "specs_from": "variant:De-icing Rock Salt",
    "spec_scope": ("Values for de-icing rock salt.", "القيم الخاصة بالملح الصخري لإذابة الجليد."),
    "variants": [
      {"name": ("De-icing Rock Salt", "ملح صخري لإذابة الجليد"),
       "desc": ("Naturally occurring sodium chloride mined from ancient sea deposits. Its coarse crystals melt ice and add traction on slippery surfaces.",
                "كلوريد صوديوم طبيعي مستخرج من رواسب بحرية قديمة. بلوراته الخشنة تذيب الجليد وتمنح ثباتاً أكبر على الأسطح الزلقة."),
       "hl": [("Purity exceeding 99% NaCl", "نقاوة تتجاوز 99% كلوريد الصوديوم"),
              ("Moisture below 1% to prevent clumping", "رطوبة أقل من 1% لمنع التكتل"),
              ("Coarse texture adds traction", "قوام خشن يمنح ثباتاً على الطريق"),
              ("Economical choice for roads and pavements", "خيار اقتصادي للطرق والأرصفة"),
              ("Several grain sizes available", "متوفر بأحجام حبيبات متعددة")]},
      {"name": ("De-icing Sea Salt", "ملح بحري لإذابة الجليد"),
       "desc": ("Produced by evaporating seawater. An economical option that melts ice rapidly and spreads evenly on all surfaces.",
                "يُنتج بتبخير مياه البحر. خيار اقتصادي يذيب الجليد بسرعة وينتشر بالتساوي على جميع الأسطح."),
       "hl": [("Rapid melting action", "إذابة سريعة للجليد"),
              ("Spreads smoothly and evenly", "سهل الفرد ومتجانس التوزيع"),
              ("Economical for large-scale use", "اقتصادي للاستخدام على نطاق واسع"),
              ("Suitable for urban, suburban and rural areas", "مناسب للمدن والضواحي والمناطق الريفية"),
              ("Proven choice for highways and driveways", "خيار مجرَّب للطرق السريعة ومداخل المنازل")]},
    ],
    "apps": [("Roads and highways", "الطرق والطرق السريعة"), ("Sidewalks and pavements", "الأرصفة والممرات"),
             ("Driveways", "مداخل المنازل"), ("Parking lots", "مواقف السيارات")],
    "feats": [
      ("Fast ice melting", "إذابة سريعة للجليد", "Lowers the freezing point quickly for faster ice and snow removal and safer roads.", "يخفض درجة التجمد بسرعة لإزالة الجليد والثلوج وطرق أكثر أماناً."),
      ("Cost-effective", "فعّال من حيث التكلفة", "Efficient performance means less product for the result you need.", "أداء عالٍ يعني كمية أقل من المنتج لتحقيق النتيجة المطلوبة."),
      ("Reliable supply", "توريد موثوق", "Consistent availability and on-time delivery throughout the season.", "توفر مستمر وتسليم في المواعيد طوال الموسم."),
    ],
    "pack": ["25", "50", "big", "bulk"],
    "pack_detail": True,
  },
  {
    "slug": "food-grade-salt", "src": "food-grade-salt",
    "name": ("Food Grade Salt", "ملح غذائي"),
    "tag": ("Food industry", "الصناعات الغذائية"),
    "card": ("Refined, double-washed sea salt and table salt for food producers and distributors.",
             "ملح مكرر وملح بحري مغسول مرتين وملح طعام لمصنعي وموزعي الأغذية."),
    "short": ("Clean, high-purity salt processed to strict food safety standards, for food manufacturers, distributors and culinary use.",
              "ملح نقي عالي الجودة يُعالج وفق معايير صارمة لسلامة الغذاء، لمصنعي الأغذية والموزعين والاستخدامات الغذائية."),
    "overview": [
      ("Our food grade salt is carefully sourced and processed for exceptional purity, uniform particle size and a clean, natural taste that enhances food without overpowering it.",
       "يتم اختيار ملحنا الغذائي ومعالجته بعناية ليتميز بنقاوة عالية وحجم حبيبات متجانس وطعم طبيعي نظيف يُبرز نكهة الطعام دون أن يطغى عليها."),
      ("Food safety and quality checks are applied at every stage of production and packing, so every batch performs the same in your recipes and production lines.",
       "نطبّق إجراءات سلامة الغذاء وفحوصات الجودة في كل مرحلة من مراحل الإنتاج والتعبئة، ليقدّم كل دفعة الأداء نفسه في وصفاتك وخطوط إنتاجك."),
    ],
    "variants": [
      {"name": ("Refined Salt", "ملح مكرر"), "desc": ("Pure, fine-grain salt for general cooking, baking and food processing.", "ملح نقي ناعم الحبيبات للطهي العام والمخبوزات وتصنيع الأغذية."), "hl": []},
      {"name": ("Double-Washed Sea Salt", "ملح بحري مغسول مرتين"), "desc": ("Sea salt washed twice for enhanced purity.", "ملح بحري يُغسل مرتين لرفع درجة النقاوة."), "hl": []},
      {"name": ("Table Salt", "ملح الطعام"), "desc": ("Classic table salt for everyday seasoning and food preparation.", "ملح طعام تقليدي للتتبيل اليومي وتحضير الطعام."), "hl": []},
      {"name": ("Specialty Salts", "أملاح متخصصة"), "desc": ("Selected salt varieties for gourmet cooking and special applications.", "أنواع مختارة من الملح للمطابخ الراقية والاستخدامات الخاصة."), "hl": []},
    ],
    "apps": [("Food manufacturing", "تصنيع الأغذية"), ("Baking", "المخبوزات"),
             ("Everyday seasoning and table use", "التتبيل اليومي والاستخدام على المائدة"),
             ("Gourmet and specialty cooking", "الطهي الراقي والمتخصص")],
    "feats": [
      ("Exceptional purity", "نقاوة استثنائية", "Carefully controlled processing to meet high food safety standards.", "معالجة مضبوطة بعناية لتلبية معايير عالية لسلامة الغذاء."),
      ("Consistent quality", "جودة ثابتة", "Uniform particle size and composition for reliable results in every batch.", "حجم حبيبات وتركيب متجانس لنتائج موثوقة في كل دفعة."),
      ("Natural flavour", "نكهة طبيعية", "Brings out the natural taste of ingredients without overpowering them.", "يُبرز الطعم الطبيعي للمكونات دون أن يطغى عليها."),
      ("Quality control", "مراقبة الجودة", "Testing throughout production for consistent purity, taste and performance.", "فحوصات طوال مراحل الإنتاج لضمان ثبات النقاوة والطعم والأداء."),
    ],
    "pack": ["25", "50", "big", "bulk"],
  },
  {
    "slug": "water-softening-tablet-salt", "src": "water-softening-tablet-salt",
    "name": ("Water Softening & Tablet Salt", "ملح تيسير المياه وأقراص الملح"),
    "tag": ("Water treatment", "معالجة المياه"),
    "card": ("Salt tablets and granular salt for residential and commercial water softeners.",
             "أقراص ملح وملح حبيبي لأجهزة تيسير المياه المنزلية والتجارية."),
    "short": ("High-purity salt tablets and granular salt for residential, commercial and high-capacity water softening systems.",
              "أقراص ملح وملح حبيبي عالي النقاوة لأنظمة تيسير المياه المنزلية والتجارية وعالية السعة."),
    "overview": [
      ("Hard water causes scale in pipes, water heaters and appliances, leaves spots on dishes and makes cleaning harder. Water softener salt regenerates the softener so it can keep removing calcium and magnesium, protecting equipment and improving water quality.",
       "يسبب الماء العسر ترسبات في المواسير وسخانات المياه والأجهزة، ويترك بقعاً على الأواني ويجعل التنظيف أصعب. يعمل ملح تيسير المياه على تجديد جهاز التيسير ليواصل إزالة الكالسيوم والماغنيسيوم، فيحمي المعدات ويحسّن جودة المياه."),
      ("Choose compressed tablets for slow, controlled dissolution, or granular salt for fast dissolving in high-capacity systems.",
       "اختر الأقراص المضغوطة لذوبان بطيء ومنتظم، أو الملح الحبيبي لذوبان سريع في الأنظمة عالية السعة."),
    ],
    "specs_from": "product",
    "variants": [
      {"name": ("Salt Tablets", "أقراص الملح"), "img": "variant-1",
       "desc": ("Compressed tablets designed for efficient regeneration in residential and commercial softeners.", "أقراص مضغوطة مصممة لتجديد فعّال في أجهزة التيسير المنزلية والتجارية."),
       "hl": [("Slow, controlled dissolution", "ذوبان بطيء ومنتظم"), ("Reduces bridging and mushing", "يقلل التكتل وتكوّن العجينة"),
              ("Easy to handle and store", "سهل التداول والتخزين"), ("Suitable for all softener types", "مناسب لجميع أنواع أجهزة التيسير")]},
      {"name": ("Granular Softening Salt", "ملح تيسير حبيبي"), "img": "variant-2",
       "desc": ("Granular salt crystals that dissolve quickly — a strong choice for high-capacity systems.", "بلورات ملح حبيبية سريعة الذوبان، خيار ممتاز للأنظمة عالية السعة."),
       "hl": [("Fast-dissolving crystals", "بلورات سريعة الذوبان"), ("High purity", "نقاوة عالية"),
              ("Helps prevent salt bridging", "يساعد على منع تكتل الملح"), ("Cost-effective", "اقتصادي")]},
    ],
    "apps": [("Residential water softeners", "أجهزة تيسير المياه المنزلية"), ("Commercial water softening systems", "أنظمة تيسير المياه التجارية"),
             ("High-capacity softening systems", "أنظمة التيسير عالية السعة")],
    "feats": [
      ("Prevents scale build-up", "يمنع تكوّن الترسبات", "Protects pipes, fixtures and water heaters from mineral deposits.", "يحمي المواسير والتجهيزات وسخانات المياه من الترسبات المعدنية."),
      ("Extends appliance life", "يطيل عمر الأجهزة", "Helps dishwashers and washing machines last longer.", "يساعد غسالات الأطباق والملابس على العمل لفترة أطول."),
      ("Better cleaning", "تنظيف أفضل", "Less soap film and residue in sinks, baths and washing machines.", "بقايا صابون وترسبات أقل في الأحواض وأحواض الاستحمام والغسالات."),
    ],
    "pack": [],
  },
  {
    "slug": "pool-salt", "src": "pool-salt",
    "name": ("Pool Salt", "ملح حمامات السباحة"),
    "tag": ("Pool care", "العناية بحمامات السباحة"),
    "card": ("High-purity, additive-free salt for salt-water chlorinators.",
             "ملح عالي النقاوة خالٍ من الإضافات لأجهزة الكلورة بالملح."),
    "short": ("High-purity, additive-free salt for salt-water chlorinators — clean pools with less chemical handling.",
              "ملح عالي النقاوة خالٍ من الإضافات لأجهزة الكلورة بالمياه المالحة، لحمامات سباحة نظيفة مع تعامل أقل مع المواد الكيميائية."),
    "overview": [
      ("Pool salt feeds salt-water chlorinators, which generate chlorine on site to keep pool water clean. It removes the need to handle and store chlorine chemicals, making pool care simpler, safer and more economical.",
       "يغذي ملح حمامات السباحة أجهزة الكلورة بالمياه المالحة التي تولّد الكلور في الموقع للحفاظ على نظافة المياه. ويغني ذلك عن تداول مواد الكلور الكيميائية وتخزينها، فتصبح العناية بالمسبح أبسط وأكثر أماناً واقتصاداً."),
      ("Our pool salt is sized for fast, complete dissolving and contains no stain-causing additives, for clear water and clean pool surfaces.",
       "تم تحديد حجم حبيبات ملحنا ليذوب بسرعة وبالكامل، وهو خالٍ من الإضافات المسببة للبقع، لمياه صافية وأسطح نظيفة."),
    ],
    "specs_from": "product",
    "variants": [],
    "apps": [("Pools with salt-water chlorinators", "حمامات السباحة المزودة بأجهزة الكلورة بالملح"),
             ("Routine pool maintenance", "الصيانة الدورية لحمامات السباحة")],
    "feats": [
      ("Fast dissolving", "سريع الذوبان", "Specially sized for fast, efficient dissolving.", "حجم حبيبات مخصص لذوبان سريع وفعّال."),
      ("No stain additives", "بدون إضافات مسببة للبقع", "A pure formulation for crystal-clear pool water.", "تركيبة نقية لمياه صافية تماماً."),
      ("Safer pool care", "عناية أكثر أماناً", "No need to handle or store dangerous chlorine chemicals.", "لا حاجة لتداول أو تخزين مواد الكلور الكيميائية الخطرة."),
      ("Eco-friendlier", "أكثر رفقاً بالبيئة", "A more environmentally responsible way to treat your pool.", "طريقة أكثر مسؤولية تجاه البيئة لمعالجة المسبح."),
    ],
    "pack": ["25", "50", "big", "bulk"],
  },
  {
    "slug": "agriculture-feed-salt", "src": "feed-salt",
    "name": ("Agriculture (Feed) Salt", "ملح الأعلاف الزراعي"),
    "tag": ("Animal nutrition", "تغذية الحيوان"),
    "card": ("Licking blocks and granular salt for livestock feed and nutrition.",
             "قوالب لعق وملح حبيبي لأعلاف وتغذية الماشية."),
    "short": ("Salt for livestock nutrition — as licking blocks or granular salt for mixing into concentrated feed.",
              "ملح لتغذية الماشية، على شكل قوالب لعق أو ملح حبيبي يُخلط مع الأعلاف المركزة."),
    "overview": [
      ("Like people, animals need sodium in their diet. Salt supports growth, development and milk yield by regulating water and dry-matter intake, which is why it is one of the most common additives in concentrated feed.",
       "تحتاج الحيوانات، مثل الإنسان، إلى الصوديوم في غذائها. يدعم الملح النمو والتطور وإدرار الحليب من خلال تنظيم استهلاك الماء والمادة الجافة، ولهذا يُعد من أكثر الإضافات استخداماً في الأعلاف المركزة."),
      ("We supply agriculture salt in two practical forms to suit how you feed your animals.",
       "نوفر ملح الأعلاف بشكلين عمليين يناسبان طريقة تغذية حيواناتك."),
    ],
    "variants": [
      {"name": ("Licking Blocks", "قوالب اللعق"),
       "desc": ("A practical, effective way to provide salt to livestock, with controlled intake.", "طريقة عملية وفعّالة لتزويد الماشية بالملح مع التحكم في الكمية المستهلكة."),
       "hl": [("Easy to use and install", "سهلة الاستخدام والتركيب"), ("Long-lasting and weather-resistant", "تدوم طويلاً ومقاومة للعوامل الجوية"),
              ("Controlled salt intake", "استهلاك منضبط للملح"), ("Suitable for pasture feeding", "مناسبة للرعي في المراعي")]},
      {"name": ("Granular Feed Salt", "ملح أعلاف حبيبي"),
       "desc": ("Granular salt designed for mixing into concentrated feed for precise, uniform distribution.", "ملح حبيبي مصمم للخلط مع الأعلاف المركزة لتوزيع دقيق ومتجانس."),
       "hl": [("Mixes easily with feed", "سهل الخلط مع العلف"), ("Precise dosage control", "تحكم دقيق في الجرعة"),
              ("Uniform distribution", "توزيع متجانس"), ("Compatible with feed systems", "متوافق مع أنظمة التغذية")]},
    ],
    "apps": [("Cattle", "الأبقار", "Dairy and beef", "ألبان ولحوم"), ("Sheep", "الأغنام", "Wool and meat", "صوف ولحوم"),
             ("Goats", "الماعز", "Milk and meat", "حليب ولحوم"), ("Horses", "الخيول", "Working and sport horses", "خيول العمل والرياضة"),
             ("Pigs", "الخنازير", "Commercial farming", "المزارع التجارية"), ("Poultry", "الدواجن", "Chickens and other birds", "الدجاج والطيور الأخرى")],
    "feats": [
      ("Growth and development", "النمو والتطور", "Supports healthy animal growth through proper sodium balance.", "يدعم نمو الحيوان الصحي من خلال توازن الصوديوم."),
      ("Water regulation", "تنظيم الماء", "Regulates water intake for proper hydration and metabolism.", "ينظم استهلاك الماء لترطيب سليم وعمليات أيض صحية."),
      ("Dry-matter intake", "استهلاك المادة الجافة", "Helps optimise feed efficiency and nutrient uptake.", "يساعد على تحسين كفاءة العلف وامتصاص العناصر الغذائية."),
      ("Milk yield", "إدرار الحليب", "Supports milk production in dairy animals.", "يدعم إنتاج الحليب لدى حيوانات الألبان."),
    ],
    "pack": ["25", "50", "big", "bulk"],
  },
  {
    "slug": "drilling-salt", "src": "drilling-salt",
    "name": ("Drilling Salt", "ملح الحفر"),
    "tag": ("Oil and gas", "النفط والغاز"),
    "card": ("Salt for drilling fluids in oil and gas exploration, especially deep wells.",
             "ملح لسوائل الحفر في عمليات استكشاف النفط والغاز، خاصة الآبار العميقة."),
    "short": ("Specialised salt for oil and gas exploration and drilling, especially deep wells.",
              "ملح متخصص لعمليات استكشاف وحفر آبار النفط والغاز، وخاصة الآبار العميقة."),
    "overview": [
      ("Drilling salt is added to drilling fluids to stabilise the wellbore, cool drilling tools and control pressure — three functions that matter most in deep wells.",
       "يُضاف ملح الحفر إلى سوائل الحفر لتثبيت جدار البئر وتبريد أدوات الحفر والتحكم في الضغط، وهي ثلاث وظائف بالغة الأهمية في الآبار العميقة."),
      ("Our drilling salt is produced under strict quality controls to prevent contamination and protect the integrity of your drilling fluids in demanding conditions.",
       "يُنتج ملح الحفر لدينا وفق ضوابط جودة صارمة لمنع التلوث والحفاظ على سلامة سوائل الحفر في الظروف الصعبة."),
    ],
    "variants": [],
    "apps": [("Deep well drilling", "حفر الآبار العميقة"), ("Oil exploration", "استكشاف النفط"), ("Gas drilling", "حفر آبار الغاز"),
             ("Wellbore pressure management", "إدارة ضغط البئر"), ("Formation support", "دعم الطبقات الجيولوجية"), ("Drilling equipment protection", "حماية معدات الحفر")],
    "feats": [
      ("Wellbore stabilisation", "تثبيت جدار البئر", "Supports well walls and formations, helping prevent collapse during drilling.", "يدعم جدران البئر والطبقات ويساعد على منع الانهيار أثناء الحفر."),
      ("Tool cooling", "تبريد الأدوات", "Acts as a cooling agent that protects drilling tools from heat damage.", "يعمل كعامل تبريد يحمي أدوات الحفر من أضرار الحرارة."),
      ("Pressure control", "التحكم في الضغط", "Added to drilling fluids to regulate wellbore pressure and stability.", "يُضاف إلى سوائل الحفر لتنظيم ضغط البئر واستقراره."),
      ("Contamination control", "منع التلوث", "Strict quality controls protect the integrity of drilling fluids.", "ضوابط جودة صارمة تحافظ على سلامة سوائل الحفر."),
    ],
    "pack": ["25", "50", "big", "bulk"],
  },
  {
    "slug": "triple-washed-solar-salt", "src": "triple-washed-and-solar-salt",
    "name": ("Triple Washed & Solar Salt", "ملح مغسول ثلاثياً وملح شمسي"),
    "tag": ("Industrial grade", "درجة صناعية"),
    "card": ("Washed sea and rock salt with very low insolubles for sensitive processes.",
             "ملح بحري وصخري مغسول بنسبة منخفضة جداً من المواد غير الذائبة للعمليات الحساسة."),
    "short": ("Washed sea salt and rock salt with very low insoluble matter and impurities, for sensitive industrial applications.",
              "ملح بحري وملح صخري مغسول بنسبة منخفضة جداً من المواد غير الذائبة والشوائب، للتطبيقات الصناعية الحساسة."),
    "overview": [
      ("Excess insoluble matter and contaminants reduce process efficiency, affect product quality and can cause equipment problems. Our carefully controlled triple washing process removes them to deliver very high NaCl purity.",
       "تؤدي زيادة المواد غير الذائبة والملوثات إلى خفض كفاءة العمليات والتأثير على جودة المنتج، وقد تسبب مشكلات في المعدات. تزيلها عملية الغسيل الثلاثي المضبوطة بعناية لدينا لتحقيق نقاوة عالية جداً من كلوريد الصوديوم."),
      ("Choose high-grade washed sea salt or high-grade washed rock salt, depending on your technical requirements.",
       "اختر بين الملح البحري المغسول عالي الجودة أو الملح الصخري المغسول عالي الجودة حسب متطلباتك الفنية."),
    ],
    "specs_from": "product",
    "spec_scope": ("Quality profile as published. Detailed analysis available on request.", "مواصفات الجودة كما هي منشورة. التحليل التفصيلي متاح عند الطلب."),
    "variants": [
      {"name": ("Washed Sea Salt", "ملح بحري مغسول"), "desc": ("High-grade sea salt, triple washed for maximum cleanliness.", "ملح بحري عالي الجودة مغسول ثلاث مرات لأقصى درجات النظافة."), "hl": []},
      {"name": ("Washed Rock Salt", "ملح صخري مغسول"), "desc": ("High-grade rock salt, triple washed for very low impurity content.", "ملح صخري عالي الجودة مغسول ثلاث مرات لنسبة شوائب منخفضة جداً."), "hl": []},
    ],
    "apps": [("Sensitive industrial processes", "العمليات الصناعية الحساسة", "Where high NaCl purity and low insolubles are required", "حيث تُطلب نقاوة عالية من كلوريد الصوديوم ونسبة منخفضة من المواد غير الذائبة")],
    "feats": [
      ("Exceptional purity", "نقاوة استثنائية", "A controlled washing process for very high NaCl purity.", "عملية غسيل مضبوطة لنقاوة عالية جداً من كلوريد الصوديوم."),
      ("Minimal impurities", "شوائب ضئيلة", "Very low insoluble matter and contaminants for better process performance.", "نسبة منخفضة جداً من المواد غير الذائبة والملوثات لأداء أفضل في العمليات."),
      ("Two sources", "مصدران للاختيار", "Washed sea salt or washed rock salt — pick what suits your process.", "ملح بحري مغسول أو ملح صخري مغسول، اختر ما يناسب عملياتك."),
    ],
    "pack": [],
  },
  {
    "slug": "chemical-industrial-salt", "src": "chemical-industrial-salt",
    "name": ("Chemical & Industrial Salt", "الملح الكيميائي والصناعي"),
    "tag": ("Industrial grade", "درجة صناعية"),
    "card": ("High-purity salt for chlor-alkali production and manufacturing industries.",
             "ملح عالي النقاوة لإنتاج الكلور والصودا الكاوية وللصناعات التحويلية."),
    "short": ("High-purity salt for chlor-alkali production and a wide range of manufacturing industries.",
              "ملح عالي النقاوة لإنتاج الكلور والصودا الكاوية ولمجموعة واسعة من الصناعات التحويلية."),
    "overview": [
      ("Salt is one of the chemical industry's most important raw materials. It is the basis of chlorine and caustic soda production by electrolysis, which in turn supply a large share of all chemical products.",
       "يُعد الملح من أهم المواد الخام في الصناعات الكيميائية، فهو أساس إنتاج الكلور والصودا الكاوية بالتحليل الكهربائي، واللذين يدخلان بدورهما في نسبة كبيرة من المنتجات الكيميائية."),
      ("We supply industrial salt with consistent purity for glass, paper, plastics, rubber, textiles, dyes, leather, cosmetics and pharmaceutical manufacturing.",
       "نوفر ملحاً صناعياً بنقاوة ثابتة لصناعات الزجاج والورق والبلاستيك والمطاط والنسيج والأصباغ والجلود ومستحضرات التجميل والأدوية."),
    ],
    "specs_from": "stat:Purity Level",
    "variants": [],
    "apps": [("Chlor-alkali (chlorine and caustic soda)", "الكلور والصودا الكاوية"), ("Glass manufacturing", "صناعة الزجاج"),
             ("Paper production", "صناعة الورق"), ("Plastics and PVC", "البلاستيك و PVC"), ("Rubber", "المطاط"),
             ("Textiles and dyes", "النسيج والأصباغ"), ("Leather", "الجلود"), ("Cosmetics", "مستحضرات التجميل"), ("Pharmaceuticals", "الأدوية")],
    "feats": [
      ("Chemical synthesis", "التخليق الكيميائي", "Essential feedstock for chlorine and caustic soda production by electrolysis.", "مادة خام أساسية لإنتاج الكلور والصودا الكاوية بالتحليل الكهربائي."),
      ("Wide industrial use", "استخدامات صناعية واسعة", "Used across glass, paper, plastics, textiles, leather, cosmetics and pharmaceuticals.", "يُستخدم في الزجاج والورق والبلاستيك والنسيج والجلود ومستحضرات التجميل والأدوية."),
      ("Consistent purity", "نقاوة ثابتة", "Steady quality from shipment to shipment for predictable processes.", "جودة ثابتة من شحنة إلى أخرى لعمليات يمكن التنبؤ بنتائجها."),
    ],
    "pack": [],
  },
  {
    "slug": "textile-dyeing-salt", "src": "textile-dyeing-salt",
    "name": ("Textile & Dyeing Salt", "ملح النسيج والصباغة"),
    "tag": ("Textile industry", "صناعة النسيج"),
    "card": ("High-purity salt for textile dyeing and cleaning processes.",
             "ملح عالي النقاوة لعمليات صباغة وتنظيف المنسوجات."),
    "short": ("High-purity salt for textile dyeing and cleaning — for better colour quality and dye stability on fabric.",
              "ملح عالي النقاوة لصباغة وتنظيف المنسوجات، لجودة ألوان أفضل وثبات أعلى للصبغة على القماش."),
    "overview": [
      ("In textile dyeing, salt helps dyes bind to fibres, improving colour quality and stability on the fabric. It is also used in textile cleaning processes.",
       "في صباغة المنسوجات، يساعد الملح الصبغة على الارتباط بالألياف، مما يحسّن جودة اللون وثباته على القماش. كما يُستخدم في عمليات تنظيف المنسوجات."),
      ("Using salt in the dyeing process can also reduce reliance on harsher chemicals, supporting cleaner textile production.",
       "ويساعد استخدام الملح في عملية الصباغة أيضاً على تقليل الاعتماد على المواد الكيميائية الأكثر ضرراً، دعماً لإنتاج نسيج أنظف."),
    ],
    "specs_from": "product",
    "variants": [],
    "apps": [("Textile dyeing", "صباغة المنسوجات"), ("Textile cleaning", "تنظيف المنسوجات")],
    "feats": [
      ("Better dye results", "نتائج صباغة أفضل", "Improves colour, quality and stability of dyes on fabric.", "يحسّن لون الصبغة وجودتها وثباتها على القماش."),
      ("Textile cleaning", "تنظيف المنسوجات", "Effective in fabric cleaning and treatment processes.", "فعّال في عمليات تنظيف ومعالجة الأقمشة."),
      ("Cleaner processing", "معالجة أنظف", "Helps reduce harmful chemicals in dyeing processes.", "يساعد على تقليل المواد الكيميائية الضارة في عمليات الصباغة."),
    ],
    "pack": ["25", "50", "big", "bulk"],
  },
]

# Arabic labels for spec keys and word values found on the source pages.
SPEC_KEY_AR = {
    "Purity": "النقاوة", "Sodium Chloride": "كلوريد الصوديوم", "Humidity": "الرطوبة", "pH Level": "درجة الحموضة (pH)",
    "Additives": "الإضافات", "NaCl Purity": "نقاوة كلوريد الصوديوم", "Impurity Level": "نسبة الشوائب",
    "Washing Process": "عملية الغسيل", "Moisture": "الرطوبة", "Purity Level": "مستوى النقاوة",
}
SPEC_NOTE_AR = {
    "Sodium chloride content": "نسبة كلوريد الصوديوم", "Low moisture content": "نسبة رطوبة منخفضة",
    "Optimal pH balance": "توازن مثالي للحموضة", "High purity content": "نسبة نقاوة عالية",
    "No stain-causing agents": "بدون مواد مسببة للبقع", "Maximum cleanliness achieved": "أقصى درجات النظافة",
    "Industry-leading low content": "نسبة منخفضة جداً", "Meticulously controlled process": "عملية مضبوطة بدقة",
    "Minimal moisture content": "نسبة رطوبة ضئيلة", "": "",
}
SPEC_VALUE_AR = {
    "Zero": "صفر", "Ultra-High": "عالية جداً", "Minimal": "ضئيلة", "Triple Washed": "غسيل ثلاثي",
    "Exceeding 99% NaCl": "أكثر من 99% NaCl", "Less than 1%": "أقل من 1%",
}


# =====================================================================
# FRENCH (fr). Keyed by the exact English text above.
# Typography: non-breaking space (NB) before : ; ? ! and %.
# Spec tables keep the English number format (99.55%+); running text uses 99,5 %.
# The build stops with a list of missing keys if any English string has no French entry.
# =====================================================================
NB = " "

SPEC_KEY_FR = {
    "Purity": "Pureté", "Sodium Chloride": "Chlorure de sodium", "Humidity": "Humidité", "pH Level": "pH",
    "Additives": "Additifs", "NaCl Purity": "Pureté en NaCl", "Impurity Level": "Taux d'impuretés",
    "Washing Process": "Procédé de lavage", "Moisture": "Humidité", "Purity Level": "Niveau de pureté",
}
SPEC_NOTE_FR = {
    "Sodium chloride content": "Teneur en chlorure de sodium", "Low moisture content": "Faible teneur en humidité",
    "Optimal pH balance": "Équilibre de pH optimal", "High purity content": "Haute pureté",
    "No stain-causing agents": "Aucun agent tachant", "Maximum cleanliness achieved": "Propreté maximale",
    "Industry-leading low content": "Teneur très faible", "Meticulously controlled process": "Procédé rigoureusement maîtrisé",
    "Minimal moisture content": "Humidité minimale", "": "",
}
# Word values are translated; numbers, units and symbols stay exactly as in English.
SPEC_VALUE_FR = {
    "Zero": "Zéro", "Ultra-High": "Très élevée", "Minimal": "Minimal", "Triple Washed": "Triple lavage",
    "Exceeding 99% NaCl": "Supérieure à 99% NaCl", "Less than 1%": "Inférieure à 1%",
}

FR = {
    # ---- packaging
    "25 kg": "25 kg", "50 kg": "50 kg", "Bags": "Sacs", "Big bags": "Big bags", "Bulk option": "Grands volumes",
    "Bulk": "Vrac", "Loose, large quantities": "Non conditionné, grandes quantités",

    # ---- De-icing
    "De-icing Salt": "Sel de déneigement",
    "Winter road safety": "Viabilité hivernale",
    "Rock and sea salt for fast ice and snow melting on roads and walkways.":
        "Sel gemme et sel marin pour faire fondre rapidement glace et neige sur les routes et les trottoirs.",
    "Rock salt and sea salt for fast, reliable ice and snow melting on roads, highways, sidewalks and driveways.":
        "Sel gemme et sel marin pour un déneigement et un déverglaçage rapides et fiables des routes, autoroutes, trottoirs et allées.",
    "De-icing salt lowers the freezing point of water, clearing ice and snow quickly and keeping roads and walkways safe through the winter.":
        "En abaissant le point de congélation de l'eau, le sel de déneigement fait fondre rapidement la glace et la neige et maintient routes et voies piétonnes praticables tout l'hiver.",
    "We supply two types: natural rock salt mined from ancient sea deposits, and sea salt produced by evaporating seawater. Both spread easily, work in urban, suburban and rural settings, and are available in several grain sizes.":
        f"Nous proposons deux qualités{NB}: un sel gemme naturel extrait d'anciens dépôts marins, et un sel marin obtenu par évaporation de l'eau de mer. Faciles à épandre, ils conviennent aux zones urbaines, périurbaines et rurales et existent en plusieurs granulométries.",
    "Values for de-icing rock salt.": "Valeurs du sel gemme de déneigement.",
    "De-icing Rock Salt": "Sel gemme de déneigement",
    "Naturally occurring sodium chloride mined from ancient sea deposits. Its coarse crystals melt ice and add traction on slippery surfaces.":
        "Chlorure de sodium naturel extrait d'anciens dépôts marins. Ses gros cristaux font fondre la glace tout en améliorant l'adhérence sur les surfaces glissantes.",
    "Purity exceeding 99% NaCl": f"Pureté supérieure à 99{NB}% de NaCl",
    "Moisture below 1% to prevent clumping": f"Humidité inférieure à 1{NB}% pour éviter la prise en masse",
    "Coarse texture adds traction": "Texture grossière pour une meilleure adhérence",
    "Economical choice for roads and pavements": "Solution économique pour les routes et les chaussées",
    "Several grain sizes available": "Plusieurs granulométries disponibles",
    "De-icing Sea Salt": "Sel marin de déneigement",
    "Produced by evaporating seawater. An economical option that melts ice rapidly and spreads evenly on all surfaces.":
        "Obtenu par évaporation de l'eau de mer. Une solution économique qui fait fondre rapidement la glace et s'épand uniformément sur toutes les surfaces.",
    "Rapid melting action": "Fonte rapide",
    "Spreads smoothly and evenly": "Épandage facile et homogène",
    "Economical for large-scale use": "Économique pour les grands volumes",
    "Suitable for urban, suburban and rural areas": "Adapté aux zones urbaines, périurbaines et rurales",
    "Proven choice for highways and driveways": "Un choix éprouvé pour les autoroutes et les allées",
    "Roads and highways": "Routes et autoroutes", "Sidewalks and pavements": "Trottoirs et voies piétonnes",
    "Driveways": "Allées et accès privés", "Parking lots": "Parkings",
    "Fast ice melting": "Fonte rapide de la glace",
    "Lowers the freezing point quickly for faster ice and snow removal and safer roads.":
        "Abaisse rapidement le point de congélation pour dégager plus vite glace et neige et sécuriser les routes.",
    "Cost-effective": "Rentable",
    "Efficient performance means less product for the result you need.":
        "Son efficacité permet d'obtenir le résultat voulu avec moins de produit.",
    "Reliable supply": "Approvisionnement fiable",
    "Consistent availability and on-time delivery throughout the season.":
        "Disponibilité constante et livraisons dans les délais tout au long de la saison.",

    # ---- Food grade
    "Food Grade Salt": "Sel alimentaire",
    "Food industry": "Agroalimentaire",
    "Refined, double-washed sea salt and table salt for food producers and distributors.":
        "Sel raffiné, sel marin double lavage et sel de table pour les industriels et distributeurs alimentaires.",
    "Clean, high-purity salt processed to strict food safety standards, for food manufacturers, distributors and culinary use.":
        "Un sel propre et d'une grande pureté, traité selon des normes strictes de sécurité alimentaire, pour les industriels, les distributeurs et les usages culinaires.",
    "Our food grade salt is carefully sourced and processed for exceptional purity, uniform particle size and a clean, natural taste that enhances food without overpowering it.":
        "Notre sel alimentaire est sélectionné et traité avec soin pour offrir une pureté remarquable, une granulométrie homogène et un goût franc et naturel qui relève les aliments sans les masquer.",
    "Food safety and quality checks are applied at every stage of production and packing, so every batch performs the same in your recipes and production lines.":
        "Des contrôles de sécurité alimentaire et de qualité interviennent à chaque étape de la production et du conditionnement, pour un résultat identique d'un lot à l'autre, dans vos recettes comme sur vos lignes de production.",
    "Refined Salt": "Sel raffiné",
    "Pure, fine-grain salt for general cooking, baking and food processing.":
        "Sel pur à grain fin pour la cuisine, la boulangerie-pâtisserie et la transformation alimentaire.",
    "Double-Washed Sea Salt": "Sel marin double lavage",
    "Sea salt washed twice for enhanced purity.": "Sel marin lavé deux fois pour une pureté accrue.",
    "Table Salt": "Sel de table",
    "Classic table salt for everyday seasoning and food preparation.":
        "Le sel de table classique, pour assaisonner et cuisiner au quotidien.",
    "Specialty Salts": "Sels de spécialité",
    "Selected salt varieties for gourmet cooking and special applications.":
        "Une sélection de sels pour la gastronomie et les usages spécifiques.",
    "Food manufacturing": "Fabrication alimentaire", "Baking": "Boulangerie et pâtisserie",
    "Everyday seasoning and table use": "Assaisonnement et usage de table",
    "Gourmet and specialty cooking": "Gastronomie et cuisine de spécialité",
    "Exceptional purity": "Pureté remarquable",
    "Carefully controlled processing to meet high food safety standards.":
        "Un traitement rigoureusement maîtrisé pour répondre à des exigences élevées de sécurité alimentaire.",
    "Consistent quality": "Qualité constante",
    "Uniform particle size and composition for reliable results in every batch.":
        "Granulométrie et composition homogènes pour des résultats fiables à chaque lot.",
    "Natural flavour": "Saveur naturelle",
    "Brings out the natural taste of ingredients without overpowering them.":
        "Révèle le goût naturel des ingrédients sans le dominer.",
    "Quality control": "Contrôle qualité",
    "Testing throughout production for consistent purity, taste and performance.":
        "Des analyses tout au long de la production pour une pureté, un goût et des performances constants.",

    # ---- Water softening
    "Water Softening & Tablet Salt": "Sel adoucisseur et pastilles de sel",
    "Water treatment": "Traitement de l'eau",
    "Salt tablets and granular salt for residential and commercial water softeners.":
        "Pastilles de sel et sel granulé pour adoucisseurs d'eau résidentiels et professionnels.",
    "High-purity salt tablets and granular salt for residential, commercial and high-capacity water softening systems.":
        "Pastilles de sel et sel granulé de haute pureté pour adoucisseurs d'eau résidentiels, professionnels et de grande capacité.",
    "Hard water causes scale in pipes, water heaters and appliances, leaves spots on dishes and makes cleaning harder. Water softener salt regenerates the softener so it can keep removing calcium and magnesium, protecting equipment and improving water quality.":
        f"Une eau dure entartre canalisations, chauffe-eau et électroménager, laisse des traces sur la vaisselle et complique le nettoyage. Le sel régénère l'adoucisseur, qui continue ainsi d'éliminer le calcium et le magnésium{NB}: vos équipements sont protégés et la qualité de l'eau s'améliore.",
    "Choose compressed tablets for slow, controlled dissolution, or granular salt for fast dissolving in high-capacity systems.":
        "Choisissez les pastilles compressées pour une dissolution lente et régulière, ou le sel granulé, à dissolution rapide, pour les installations de grande capacité.",
    "Salt Tablets": "Pastilles de sel",
    "Compressed tablets designed for efficient regeneration in residential and commercial softeners.":
        "Pastilles compressées conçues pour une régénération efficace des adoucisseurs résidentiels et professionnels.",
    "Slow, controlled dissolution": "Dissolution lente et régulière",
    "Reduces bridging and mushing": "Limite la formation de voûtes et de bouillie de sel",
    "Easy to handle and store": "Faciles à manipuler et à stocker",
    "Suitable for all softener types": "Compatibles avec tous les adoucisseurs",
    "Granular Softening Salt": "Sel adoucisseur granulé",
    "Granular salt crystals that dissolve quickly — a strong choice for high-capacity systems.":
        "Des cristaux de sel granulé à dissolution rapide, tout indiqués pour les installations de grande capacité.",
    "Fast-dissolving crystals": "Cristaux à dissolution rapide",
    "High purity": "Haute pureté",
    "Helps prevent salt bridging": "Aide à prévenir la formation de voûtes",
    "Residential water softeners": "Adoucisseurs d'eau résidentiels",
    "Commercial water softening systems": "Adoucisseurs d'eau professionnels",
    "High-capacity softening systems": "Installations d'adoucissement de grande capacité",
    "Prevents scale build-up": "Prévient l'entartrage",
    "Protects pipes, fixtures and water heaters from mineral deposits.":
        "Protège canalisations, robinetterie et chauffe-eau des dépôts minéraux.",
    "Extends appliance life": "Prolonge la vie des appareils",
    "Helps dishwashers and washing machines last longer.": "Lave-vaisselle et lave-linge durent plus longtemps.",
    "Better cleaning": "Un nettoyage plus efficace",
    "Less soap film and residue in sinks, baths and washing machines.":
        "Moins de traces de savon et de résidus dans les éviers, les baignoires et le lave-linge.",

    # ---- Pool
    "Pool Salt": "Sel de piscine",
    "Pool care": "Entretien des piscines",
    "High-purity, additive-free salt for salt-water chlorinators.":
        "Sel de haute pureté, sans additif, pour électrolyseurs au sel.",
    "High-purity, additive-free salt for salt-water chlorinators — clean pools with less chemical handling.":
        f"Un sel de haute pureté, sans additif, pour électrolyseurs au sel{NB}: une eau saine, avec moins de produits chimiques à manipuler.",
    "Pool salt feeds salt-water chlorinators, which generate chlorine on site to keep pool water clean. It removes the need to handle and store chlorine chemicals, making pool care simpler, safer and more economical.":
        f"Le sel de piscine alimente l'électrolyseur, qui produit le chlore sur place pour garder une eau propre. Plus besoin de manipuler ni de stocker des produits chlorés{NB}: l'entretien devient plus simple, plus sûr et plus économique.",
    "Our pool salt is sized for fast, complete dissolving and contains no stain-causing additives, for clear water and clean pool surfaces.":
        f"Sa granulométrie est étudiée pour une dissolution rapide et complète, et il ne contient aucun additif tachant{NB}: l'eau reste limpide et le revêtement impeccable.",
    "Pools with salt-water chlorinators": "Piscines équipées d'un électrolyseur au sel",
    "Routine pool maintenance": "Entretien courant des piscines",
    "Fast dissolving": "Dissolution rapide",
    "Specially sized for fast, efficient dissolving.": "Une granulométrie étudiée pour une dissolution rapide et efficace.",
    "No stain additives": "Sans additif tachant",
    "A pure formulation for crystal-clear pool water.": "Une formule pure pour une eau cristalline.",
    "Safer pool care": "Un entretien plus sûr",
    "No need to handle or store dangerous chlorine chemicals.":
        "Inutile de manipuler ou de stocker des produits chlorés dangereux.",
    "Eco-friendlier": "Plus respectueux de l'environnement",
    "A more environmentally responsible way to treat your pool.":
        "Une façon plus responsable de traiter l'eau de votre piscine.",

    # ---- Agriculture / feed
    "Agriculture (Feed) Salt": "Sel agricole (alimentation animale)",
    "Animal nutrition": "Nutrition animale",
    "Licking blocks and granular salt for livestock feed and nutrition.":
        "Pierres à lécher et sel granulé pour l'alimentation du bétail.",
    "Salt for livestock nutrition — as licking blocks or granular salt for mixing into concentrated feed.":
        "Du sel pour la nutrition du bétail, en pierres à lécher ou en sel granulé à incorporer aux aliments concentrés.",
    "Like people, animals need sodium in their diet. Salt supports growth, development and milk yield by regulating water and dry-matter intake, which is why it is one of the most common additives in concentrated feed.":
        f"Comme l'homme, l'animal a besoin de sodium. En régulant la consommation d'eau et de matière sèche, le sel favorise la croissance, le développement et la production laitière{NB}: c'est l'un des additifs les plus courants des aliments concentrés.",
    "We supply agriculture salt in two practical forms to suit how you feed your animals.":
        "Nous le proposons sous deux formes pratiques, selon votre mode d'alimentation.",
    "Licking Blocks": "Pierres à lécher",
    "A practical, effective way to provide salt to livestock, with controlled intake.":
        "Une solution simple et efficace pour apporter du sel au bétail, avec une consommation maîtrisée.",
    "Easy to use and install": "Faciles à utiliser et à installer",
    "Long-lasting and weather-resistant": "Durables et résistantes aux intempéries",
    "Controlled salt intake": "Apport en sel maîtrisé",
    "Suitable for pasture feeding": "Adaptées au pâturage",
    "Granular Feed Salt": "Sel granulé pour l'alimentation animale",
    "Granular salt designed for mixing into concentrated feed for precise, uniform distribution.":
        "Sel granulé à incorporer aux aliments concentrés, pour une répartition précise et homogène.",
    "Mixes easily with feed": "Se mélange facilement aux aliments",
    "Precise dosage control": "Dosage précis",
    "Uniform distribution": "Répartition homogène",
    "Compatible with feed systems": "Compatible avec les systèmes d'alimentation",
    "Cattle": "Bovins", "Dairy and beef": "Lait et viande",
    "Sheep": "Ovins", "Wool and meat": "Laine et viande",
    "Goats": "Caprins", "Milk and meat": "Lait et viande",
    "Horses": "Chevaux", "Working and sport horses": "Chevaux de travail et de sport",
    "Pigs": "Porcins", "Commercial farming": "Élevage commercial",
    "Poultry": "Volailles", "Chickens and other birds": "Poulets et autres volailles",
    "Growth and development": "Croissance et développement",
    "Supports healthy animal growth through proper sodium balance.":
        "Favorise une croissance saine grâce à un bon équilibre en sodium.",
    "Water regulation": "Régulation hydrique",
    "Regulates water intake for proper hydration and metabolism.":
        "Régule la consommation d'eau pour une hydratation et un métabolisme équilibrés.",
    "Dry-matter intake": "Ingestion de matière sèche",
    "Helps optimise feed efficiency and nutrient uptake.":
        "Contribue à optimiser l'efficacité alimentaire et l'assimilation des nutriments.",
    "Milk yield": "Production laitière",
    "Supports milk production in dairy animals.": "Soutient la production de lait chez les animaux laitiers.",

    # ---- Drilling
    "Drilling Salt": "Sel de forage",
    "Oil and gas": "Pétrole et gaz",
    "Salt for drilling fluids in oil and gas exploration, especially deep wells.":
        "Sel pour fluides de forage dans l'exploration pétrolière et gazière, notamment pour les puits profonds.",
    "Specialised salt for oil and gas exploration and drilling, especially deep wells.":
        "Un sel spécialement destiné à l'exploration et au forage pétroliers et gaziers, en particulier des puits profonds.",
    "Drilling salt is added to drilling fluids to stabilise the wellbore, cool drilling tools and control pressure — three functions that matter most in deep wells.":
        f"Ajouté aux fluides de forage, le sel stabilise les parois du puits, refroidit les outils et contrôle la pression{NB}: trois fonctions essentielles dans les puits profonds.",
    "Our drilling salt is produced under strict quality controls to prevent contamination and protect the integrity of your drilling fluids in demanding conditions.":
        "Notre sel de forage est produit sous contrôle qualité strict afin d'éviter toute contamination et de préserver l'intégrité de vos fluides, même en conditions exigeantes.",
    "Deep well drilling": "Forage de puits profonds", "Oil exploration": "Exploration pétrolière",
    "Gas drilling": "Forage gazier", "Wellbore pressure management": "Gestion de la pression du puits",
    "Formation support": "Soutien des formations géologiques",
    "Drilling equipment protection": "Protection des équipements de forage",
    "Wellbore stabilisation": "Stabilisation du puits",
    "Supports well walls and formations, helping prevent collapse during drilling.":
        "Soutient les parois du puits et les formations, et aide à prévenir les effondrements en cours de forage.",
    "Tool cooling": "Refroidissement des outils",
    "Acts as a cooling agent that protects drilling tools from heat damage.":
        "Agit comme agent de refroidissement et protège les outils de forage de l'échauffement.",
    "Pressure control": "Contrôle de la pression",
    "Added to drilling fluids to regulate wellbore pressure and stability.":
        "Ajouté aux fluides de forage pour réguler la pression et la stabilité du puits.",
    "Contamination control": "Maîtrise de la contamination",
    "Strict quality controls protect the integrity of drilling fluids.":
        "Des contrôles qualité stricts préservent l'intégrité des fluides de forage.",

    # ---- Triple washed
    "Triple Washed & Solar Salt": "Sel triple lavage et sel solaire",
    "Industrial grade": "Qualité industrielle",
    "Washed sea and rock salt with very low insolubles for sensitive processes.":
        "Sel marin et sel gemme lavés, très pauvres en insolubles, pour les procédés sensibles.",
    "Washed sea salt and rock salt with very low insoluble matter and impurities, for sensitive industrial applications.":
        "Sel marin et sel gemme lavés, à très faible teneur en insolubles et en impuretés, pour les applications industrielles sensibles.",
    "Excess insoluble matter and contaminants reduce process efficiency, affect product quality and can cause equipment problems. Our carefully controlled triple washing process removes them to deliver very high NaCl purity.":
        "Un excès d'insolubles et de contaminants réduit le rendement des procédés, nuit à la qualité des produits et peut endommager les équipements. Notre triple lavage, rigoureusement maîtrisé, les élimine pour atteindre une très haute pureté en NaCl.",
    "Choose high-grade washed sea salt or high-grade washed rock salt, depending on your technical requirements.":
        "Selon vos exigences techniques, choisissez un sel marin lavé ou un sel gemme lavé de qualité supérieure.",
    "Quality profile as published. Detailed analysis available on request.":
        "Profil qualité tel que publié. Analyse détaillée disponible sur demande.",
    "Washed Sea Salt": "Sel marin lavé",
    "High-grade sea salt, triple washed for maximum cleanliness.":
        "Sel marin de qualité supérieure, lavé trois fois pour une propreté maximale.",
    "Washed Rock Salt": "Sel gemme lavé",
    "High-grade rock salt, triple washed for very low impurity content.":
        "Sel gemme de qualité supérieure, lavé trois fois pour une très faible teneur en impuretés.",
    "Sensitive industrial processes": "Procédés industriels sensibles",
    "Where high NaCl purity and low insolubles are required":
        "Lorsqu'une haute pureté en NaCl et un faible taux d'insolubles sont exigés",
    "A controlled washing process for very high NaCl purity.": "Un lavage maîtrisé pour une très haute pureté en NaCl.",
    "Minimal impurities": "Impuretés minimales",
    "Very low insoluble matter and contaminants for better process performance.":
        "Très peu d'insolubles et de contaminants, pour des procédés plus performants.",
    "Two sources": "Deux origines au choix",
    "Washed sea salt or washed rock salt — pick what suits your process.":
        f"Sel marin lavé ou sel gemme lavé{NB}: choisissez celui qui convient à votre procédé.",

    # ---- Chemical & industrial
    "Chemical & Industrial Salt": "Sel chimique et industriel",
    "High-purity salt for chlor-alkali production and manufacturing industries.":
        "Sel de haute pureté pour l'électrolyse chlore-soude et l'industrie manufacturière.",
    "High-purity salt for chlor-alkali production and a wide range of manufacturing industries.":
        "Un sel de haute pureté pour la production de chlore et de soude et pour de nombreuses industries manufacturières.",
    "Salt is one of the chemical industry's most important raw materials. It is the basis of chlorine and caustic soda production by electrolysis, which in turn supply a large share of all chemical products.":
        "Le sel compte parmi les matières premières essentielles de la chimie. Il est à la base de la production de chlore et de soude caustique par électrolyse, deux produits qui entrent à leur tour dans une grande partie de l'industrie chimique.",
    "We supply industrial salt with consistent purity for glass, paper, plastics, rubber, textiles, dyes, leather, cosmetics and pharmaceutical manufacturing.":
        "Nous fournissons un sel industriel de pureté constante pour la verrerie, la papeterie, la plasturgie, le caoutchouc, le textile, les colorants, le cuir, la cosmétique et l'industrie pharmaceutique.",
    "Chlor-alkali (chlorine and caustic soda)": "Chlore-soude (chlore et soude caustique)",
    "Glass manufacturing": "Verrerie", "Paper production": "Papeterie", "Plastics and PVC": "Plasturgie et PVC",
    "Rubber": "Caoutchouc", "Textiles and dyes": "Textile et colorants", "Leather": "Cuir",
    "Cosmetics": "Cosmétique", "Pharmaceuticals": "Industrie pharmaceutique",
    "Chemical synthesis": "Synthèse chimique",
    "Essential feedstock for chlorine and caustic soda production by electrolysis.":
        "Matière première indispensable à la production de chlore et de soude caustique par électrolyse.",
    "Wide industrial use": "Nombreux usages industriels",
    "Used across glass, paper, plastics, textiles, leather, cosmetics and pharmaceuticals.":
        "Utilisé en verrerie, papeterie, plasturgie, textile, cuir, cosmétique et pharmacie.",
    "Consistent purity": "Pureté constante",
    "Steady quality from shipment to shipment for predictable processes.":
        "Une qualité stable d'une expédition à l'autre, pour des procédés maîtrisés.",

    # ---- Textile
    "Textile & Dyeing Salt": "Sel pour textile et teinture",
    "Textile industry": "Industrie textile",
    "High-purity salt for textile dyeing and cleaning processes.":
        "Sel de haute pureté pour la teinture et le nettoyage des textiles.",
    "High-purity salt for textile dyeing and cleaning — for better colour quality and dye stability on fabric.":
        "Un sel de haute pureté pour la teinture et le nettoyage des textiles, pour des couleurs plus belles et mieux fixées.",
    "In textile dyeing, salt helps dyes bind to fibres, improving colour quality and stability on the fabric. It is also used in textile cleaning processes.":
        "En teinture, le sel favorise la fixation des colorants sur les fibres et améliore la qualité et la tenue des couleurs. Il intervient aussi dans le nettoyage des textiles.",
    "Using salt in the dyeing process can also reduce reliance on harsher chemicals, supporting cleaner textile production.":
        "Son emploi en teinture permet en outre de limiter le recours à des produits chimiques plus agressifs, au profit d'une production plus propre.",
    "Textile dyeing": "Teinture textile", "Textile cleaning": "Nettoyage des textiles",
    "Better dye results": "De meilleurs résultats en teinture",
    "Improves colour, quality and stability of dyes on fabric.":
        "Améliore la couleur, la qualité et la tenue des teintures sur le tissu.",
    "Effective in fabric cleaning and treatment processes.":
        "Efficace dans le nettoyage et le traitement des tissus.",
    "Cleaner processing": "Un procédé plus propre",
    "Helps reduce harmful chemicals in dyeing processes.":
        "Contribue à réduire les produits chimiques nocifs en teinture.",
}

# ---- French: site UI, home, about, FAQ and contact pages
FR.update({
    "Egyptian Global Export": "Egyptian Global Export", "EGE": "EGE",
    "Home": "Accueil", "Products": "Produits", "About": "À propos", "FAQ": "FAQ", "Contact": "Contact",
    "Request a Quote": "Demander un devis", "Request a Quote on WhatsApp": "Demander un devis sur WhatsApp",
    "Email us": "Nous écrire", "Menu": "Menu", "Skip to content": "Aller au contenu",
    "Made in Egypt • Exported Worldwide": "Fabriqué en Égypte • Exporté dans le monde entier",
    "Chat with us on WhatsApp": "Discuter avec nous sur WhatsApp",
    "Hello, I'd like to know more about your salt products.": "Bonjour, je souhaiterais en savoir plus sur vos sels.",
    "Hello, I'd like a quote for your salt products.": "Bonjour, je souhaite recevoir un devis pour vos sels.",
    "View product": "Voir le produit", "All products": "Tous nos produits",
    "Egyptian Global Export supplies industrial, food, de-icing and specialty salt from Egypt to buyers around the world.":
        "Depuis l'Égypte, Egyptian Global Export fournit du sel industriel, alimentaire, de déneigement et de spécialité à des acheteurs du monde entier.",
    "Company": "Société", "All rights reserved.": "Tous droits réservés.",
    "Overview": "Présentation", "Technical specifications": "Caractéristiques techniques", "Typical values": "Valeurs typiques",
    "Detailed specifications for this product are available on request. Tell us your application and we'll share the right grade and analysis.":
        f"Les caractéristiques détaillées de ce produit sont disponibles sur demande. Indiquez-nous votre application{NB}: nous vous communiquerons la qualité adaptée et son analyse.",
    "Ask for specifications": "Demander les caractéristiques",
    "Grades and types": "Qualités et variantes", "Choose the type that fits your application.": "Choisissez la qualité adaptée à votre usage.",
    "Applications": "Applications", "Key benefits": "Principaux atouts",
    "Packaging options": "Conditionnements", "Packed to suit your order size and handling.": "Un conditionnement adapté à vos volumes et à votre manutention.",
    "Packaging options for this product are confirmed with your quote.": "Les conditionnements disponibles pour ce produit sont précisés dans votre devis.",
    "Bags, big bags or bulk": "Sacs, big bags ou vrac",
    "Product photos": "Photos du produit", "Other products": "Autres produits",
    "Send us the grade, quantity, packaging and destination port, and we'll come back with a quote.":
        f"Indiquez-nous la qualité, la quantité, le conditionnement et le port de destination{NB}: nous revenons vers vous avec un devis.",
    "Let's talk about your next shipment": "Parlons de votre prochaine expédition",
    "Tell us what you need, how much and where it's going. We'll reply with options and a quote.":
        "Dites-nous ce qu'il vous faut, en quelle quantité et pour quelle destination. Nous vous répondrons avec des solutions et un devis.",
    # home
    "Salt exporter from Egypt": "Exportateur de sel égyptien",
    "Egyptian salt,": "Le sel égyptien,", "exported worldwide.": "exporté dans le monde entier.",
    "Egyptian Global Export supplies de-icing, food grade, industrial and specialty salt to buyers around the world — in bags, big bags or bulk.":
        "Egyptian Global Export fournit du sel de déneigement, alimentaire, industriel et de spécialité à des acheteurs du monde entier, en sacs, en big bags ou en vrac.",
    "Browse products": "Découvrir nos produits",
    "9": "9", "Product categories": "Catégories de produits",
    "99.5%+": f"≥{NB}99,5{NB}%", "NaCl on pool and softener salt": "de NaCl pour le sel de piscine et le sel adoucisseur",
    "25 kg → bulk": "25 kg → vrac", "Flexible packaging": "Conditionnement flexible",
    "Suez Canal": "Canal de Suez", "Based in El Qantara West, Ismailia": "Basés à El Qantara Ouest, Ismaïlia",
    "Our products": "Nos produits", "Salt for every industry": "Un sel pour chaque industrie",
    "From winter roads to food production, water treatment and oil drilling — one supplier for your salt requirements.":
        f"Des routes enneigées à l'agroalimentaire, du traitement de l'eau au forage pétrolier{NB}: un seul fournisseur pour tous vos besoins en sel.",
    "Why EGE": "Pourquoi EGE", "A straightforward export partner": "Un partenaire export simple et fiable",
    "We keep things simple: the right product, clear specifications and direct communication from enquiry to shipment.":
        f"Notre approche est simple{NB}: le bon produit, des caractéristiques claires et un interlocuteur direct, de la demande à l'expédition.",
    "Wide product range": "Une gamme étendue",
    "Nine salt categories for food, industry, agriculture, water treatment, pools, drilling and de-icing.":
        "Neuf catégories de sel pour l'alimentation, l'industrie, l'agriculture, le traitement de l'eau, les piscines, le forage et le déneigement.",
    "25 kg and 50 kg bags, big bags or loose bulk, depending on the product and your order.":
        "Sacs de 25 kg et de 50 kg, big bags ou vrac, selon le produit et votre commande.",
    "Quality focus": "Exigence de qualité",
    "High-purity products with published specifications, and analysis shared on request.":
        "Des produits de haute pureté aux caractéristiques publiées, et des analyses communiquées sur demande.",
    "Easy to reach": "Facile à joindre",
    "Talk directly with our team on WhatsApp, phone or email — in English or Arabic.":
        "Échangez directement avec notre équipe par WhatsApp, téléphone ou e-mail, en anglais ou en arabe.",
    "Egyptian Global Export (EGE) | Salt Exporter from Egypt": "Egyptian Global Export (EGE) | Exportateur de sel égyptien",
    # products index
    "Our salt products": "Nos sels",
    "Nine salt categories for food, industry, agriculture, water treatment, pools, drilling and winter road safety. Select a product for specifications, packaging and applications.":
        "Neuf catégories de sel pour l'alimentation, l'industrie, l'agriculture, le traitement de l'eau, les piscines, le forage et la viabilité hivernale. Sélectionnez un produit pour consulter ses caractéristiques, ses conditionnements et ses applications.",
    # about
    "About Egyptian Global Export": "À propos d'Egyptian Global Export",
    "An Egyptian export company supplying quality salt products to buyers around the world.":
        "Une société d'export égyptienne qui fournit des sels de qualité à des acheteurs du monde entier.",
    "Who we are": "Qui sommes-nous",
    "Egyptian Global Export (EGE) is an export company based in El Qantara West, Ismailia, on the Suez Canal. We supply salt products from Egypt to importers, distributors and industrial buyers worldwide.":
        "Egyptian Global Export (EGE) est une société d'export basée à El Qantara Ouest, dans le gouvernorat d'Ismaïlia, au bord du canal de Suez. Nous fournissons des sels égyptiens aux importateurs, distributeurs et industriels du monde entier.",
    "Our range covers de-icing salt, food grade salt, water softening and tablet salt, pool salt, agriculture salt, drilling salt, triple washed and solar salt, chemical and industrial salt, and textile salt.":
        "Notre gamme comprend le sel de déneigement, le sel alimentaire, le sel adoucisseur et les pastilles de sel, le sel de piscine, le sel agricole, le sel de forage, le sel triple lavage et le sel solaire, le sel chimique et industriel, ainsi que le sel pour textile.",
    "What we stand for": "Nos engagements",
    "Quality": "Qualité", "Products matched to the specification your application needs.":
        "Des produits conformes aux caractéristiques qu'exige votre application.",
    "Clear communication": "Une communication claire", "Fast, direct answers in English and Arabic.":
        "Des réponses rapides et directes, en anglais et en arabe.",
    "Export focus": "Tournés vers l'export", "Packing and documentation prepared for international shipment.":
        "Un conditionnement et des documents préparés pour l'expédition internationale.",
    "How we work": "Notre méthode", "From your first message to delivery, in four steps.":
        "De votre premier message à la livraison, en quatre étapes.",
    "Tell us what you need": "Exprimez votre besoin", "Product, grade, quantity, packaging and destination.":
        "Produit, qualité, quantité, conditionnement et destination.",
    "Specifications and quote": "Caractéristiques et devis", "We confirm the right grade and send our offer.":
        "Nous confirmons la qualité adaptée et vous adressons notre offre.",
    "Packing": "Conditionnement", "Bags, big bags or bulk, packed for your order.": "Sacs, big bags ou vrac, selon votre commande.",
    "Shipment": "Expédition", "Your order is shipped to your destination.": "Votre commande est expédiée à destination.",
    "About us": "À propos",
    # faq
    "What products do you export?": f"Quels produits exportez-vous{NB}?",
    "What packaging options are available?": f"Quels conditionnements proposez-vous{NB}?",
    "Most products are available in 25 kg bags, 50 kg bags, big bags and loose bulk. Available options vary by product, so we confirm them with your quote.":
        "La plupart de nos produits sont disponibles en sacs de 25 kg et de 50 kg, en big bags et en vrac. Les options varient selon le produit et sont confirmées dans votre devis.",
    "Can I get technical specifications or an analysis?": f"Puis-je obtenir les caractéristiques techniques ou une analyse{NB}?",
    "Yes. Published specifications are shown on each product page. For other products, or for a detailed analysis, contact us and tell us your application.":
        "Oui. Les caractéristiques publiées figurent sur chaque page produit. Pour les autres produits, ou pour une analyse détaillée, contactez-nous en précisant votre application.",
    "Which grain sizes are available?": f"Quelles granulométries sont disponibles{NB}?",
    "Grain size depends on the product and its use. De-icing salt, for example, comes in several grain sizes. Tell us your application and we'll recommend the right one.":
        "La granulométrie dépend du produit et de son usage. Le sel de déneigement, par exemple, existe en plusieurs granulométries. Indiquez-nous votre application et nous vous conseillerons.",
    "How do I request a quote?": f"Comment demander un devis{NB}?",
    "Do you ship internationally?": f"Livrez-vous à l'international{NB}?",
    "Yes. We are an export company and supply buyers outside Egypt. Tell us your destination when you request a quote.":
        "Oui. Nous sommes une société d'export et fournissons des acheteurs hors d'Égypte. Précisez votre destination lors de votre demande de devis.",
    "Is there a minimum order quantity?": f"Existe-t-il une quantité minimale de commande{NB}?",
    "Order quantities depend on the product and packaging. Contact us with your requirements and we'll let you know what's possible.":
        "Les quantités dépendent du produit et du conditionnement. Faites-nous part de votre besoin et nous vous indiquerons les possibilités.",
    "Where are you located?": f"Où êtes-vous situés{NB}?",
    "Frequently asked questions": "Questions fréquentes",
    "Answers to common questions about our products, packaging and ordering.":
        "Les réponses aux questions les plus courantes sur nos produits, nos conditionnements et les commandes.",
    "Still have a question?": f"Une autre question{NB}?",
    "Message us on WhatsApp or send an email — we're happy to help.":
        f"Écrivez-nous sur WhatsApp ou par e-mail{NB}: nous serons ravis de vous aider.",
    # contact
    "Contact us": "Nous contacter",
    "Message us on WhatsApp for the fastest reply, or reach us by phone or email.":
        "Pour une réponse rapide, écrivez-nous sur WhatsApp. Vous pouvez aussi nous joindre par téléphone ou par e-mail.",
    "Phone": "Téléphone", "Email": "E-mail", "Address": "Adresse", "Map: ": f"Carte{NB}: ",
    "Product and grade": "Produit et qualité", "Quantity": "Quantité",
    "Packaging (bags, big bags or bulk)": "Conditionnement (sacs, big bags ou vrac)",
    "Destination port or country": "Port ou pays de destination", "Any specification requirements": "Vos exigences techniques éventuelles",
    "Get an accurate quote, faster": "Un devis précis, plus rapidement",
    "Include these details in your message and we can reply with a complete offer.":
        "Précisez ces informations dans votre message et nous vous adresserons une offre complète.",
})
