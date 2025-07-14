---
title: "בלשים ספרותיים: פענוח סגנונות"
english_slug: literary-detectives-identifying-styles
category: "מדעי הרוח / ספרות וכתיבה"
tags:
  - סגנונות ספרותיים
  - רומנטיקה
  - ריאליזם
  - מודרניזם
  - ניתוח טקסט
  - תולדות הספרות
---
# בלשים ספרותיים: פענוח סגנונות

צאו למסע בלשי בעולם הספרות! האם תוכלו לזהות את טביעת האצבע של התקופה בסגנון הכתיבה? נסו לשייך קטעי ספרות קצרים לסגנון הספרותי הנכון: רומנטיקה, ריאליזם או מודרניזם. זו הזדמנות לשחזק את כישורי הזיהוי שלכם ולהעמיק את הבנתכם ביצירה.

<div id="app">
  <div class="passage-container">
    <div id="passage" class="animated fade-in">טוען קטע...</div>
  </div>
  <div id="choices">
    <button class="choice-button" data-style="רומנטיקה">רומנטיקה</button>
    <button class="choice-button" data-style="ריאליזם">ריאליזם</button>
    <button class="choice-button" data-style="מודרניזם">מודרניזם</button>
  </div>
  <div id="feedback" class="animated"></div>
  <div id="passageExplanation" class="explanation-box animated slide-down"></div>
  <button id="nextPassage" class="nav-button" style="display: none;">לקטע הבא <span class="arrow">→</span></button>
</div>

<button id="toggleExplanation" class="nav-button secondary-button">הצג הסבר מקיף על הסגנונות</button>

<div id="explanationContent" class="explanation-content" style="display: none;">
  <h2>ערכת הבלש: מדריך לסגנונות ספרותיים</h2>

  <h3>מהו סגנון ספרותי?</h3>
  <p>סגנון ספרותי הוא כמו כתב היד הייחודי של תקופה או זרם. הוא משקף את הבחירות האמנותיות - נושאים מועדפים, אוצר מילים, מבנה העלילה וגם את ההשקפה הפילוסופית של הזמן בו נוצרה היצירה. זיהוי הסגנון עוזר לנו לפענח את הקשר בין היצירה, יוצרה והעולם שמסביבם.</p>

  <h3>הסגנון הרומנטי (שלהי המאה ה-18 - אמצע המאה ה-19)</h3>
  <ul>
    <li><strong>הקשר:</strong> נולד כתגובת נגד לקור הרוח הרציונלי של הנאורות, וכמראה לתהפוכות חברתיות. הרומנטיקה הדגישה את כוחם של הרגש, הדמיון והאינדיבידואליזם.</li>
    <li><strong>מאפיינים מרכזיים:</strong> התפרצות רגשות עזים, סגידה לטבע ככוח פראי ונשגב, התמקדות בחוויה הסובייקטיבית והייחודית, כמיהה לעבר המסתורי (בעיקר ימי הביניים), משיכה אל הבלתי-נודע, העל-טבעי והאקזוטי.</li>
    <li><strong>שפה וצורה:</strong> שימוש בשפה עשירה, ציורית ומלאת מטאפורות; דימויים וסמלים הרואיים או מיסטיים; מבנה המדגיש את הקול הלירי והאישי; זרימה מוזיקלית בקצב וצליל.</li>
  </ul>

  <h3>הסגנון הריאליסטי (אמצע המאה ה-19)</h3>
  <ul>
    <li><strong>הקשר:</strong> התפתח מתוך רצון לתעד את המציאות כהווייתה, כתגובה ל"בריחה" הרומנטית. הושפע מהתפתחויות במדע ובתעשייה, ומהתחזקות המעמד הבורגני העירוני.</li>
    <li><strong>מאפיינים מרכזיים:</strong> תיאור אובייקטיבי, מדויק וחסר סנטימנטליות של החיים היומיומיים והחברה על כל רבדיה (כולל קשיים וכיעור); התמקדות בדמויות "רגילות" המתמודדות עם אתגרי הקיום; ניתוח פסיכולוגי וחברתי מעמיק.</li>
    <li><strong>שפה וצורה:</strong> שפה פשוטה, ברורה ותכליתית; פירוט רב ואמין בתיאורי מקומות, חפצים ומעשים; עלילה ליניארית וכרונולוגית לרוב; נרטיב המנסה להצטייר כ"מראה" של המציאות, ללא התערבות בוטה של המספר.</li>
  </ul>

  <h3>הסגנון המודרניסטי (סוף המאה ה-19 - אמצע המאה ה-20)</h3>
  <ul>
    <li><strong>הקשר:</strong> צמח על רקע תמורות ענק, משברים גלובליים ותחושת ניכור בעקבות מלחמות העולם והתפתחות האורבניזציה והפסיכולוגיה (פרויד). ערער על הנחות יסוד ישנות וחיפש דרכים חדשות לבטא את חוויית הקיום המודרני.</li>
    <li><strong>מאפיינים מרכזיים:</strong> צלילה אל תוך הסובייקטיביות הקיצונית של התודעה האנושית (זרם תודעה); הצגת נקודות מבט מרובות וקולות שונים; ערעור על מבנים ליניאריים של זמן ומקום; עיסוק בנושאים כמו אבסורד, ניכור, בדידות, וחיפוש אחר משמעות בעולם מתפרק.</li>
    <li><strong>שפה וצורה:</strong> שפה ניסיונית, מקוטעת, אסוציאטיבית, לעיתים קשה לפענוח; שימוש בטכניקות אמנותיות כמו קולאז' ומונטאז'; מבנה יצירה מפורק ולא בהכרח עלילתי; סיומים פתוחים ולא פתורים.</li>
  </ul>

  <h3>איך מזהים? רמזים לבלש הספרותי:</h3>
  <p>כדי לפענח את הסגנון, חפשו את ה"רמזים" בקטע:</p>
  <ul>
    <li><strong>רומנטיקה:</strong> רגש מתפרץ, תיאורי טבע דרמטיים, דמיון פראי, עיסוק בפלא ונסתר, קול אישי חזק.</li>
    <li><strong>ריאליזם:</strong> תיאור יומיומי, מדויק ומפורט; אנשים רגילים בחיי שגרה; שפה פשוטה ועניינית; עלילה הגיונית.</li>
    <li><strong>מודרניזם:</strong> קפיצות במחשבה, זרם תודעה, תחושת בלבול או ניכור, מבנה שבור, שפה רמזית ולא ישירה.</li>
  </ul>
</div>

<style>
  /* --- בסיס ופונטים --- */
  #app, .explanation-content {
    font-family: 'Arial', sans-serif; /* שימוש בפונט מערכת נפוץ */
    max-width: 700px;
    margin: 20px auto;
    padding: 25px; /* הגדלת ריפוד */
    border-radius: 12px; /* פינות עגולות יותר */
    background-color: #ffffff; /* רקע לבן ונקי */
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1); /* צל עדין */
    text-align: right;
    direction: rtl;
    border: 1px solid #e0e0e0; /* הוספת גבול עדין */
  }

  body {
      background-color: #f4f7f6; /* רקע כללי בהיר ועדין */
      line-height: 1.7; /* רווח שורות נוח יותר */
      color: #333; /* צבע טקסט כהה אך לא שחור מוחלט */
  }

  h1, h2, h3 {
      color: #0056b3; /* כותרות בצבע כחול עמוק */
      margin-bottom: 15px;
      padding-bottom: 5px;
      border-bottom: 1px solid #eef2ff; /* קו תחתון עדין לכותרות */
  }

  h1 {
      text-align: center;
      margin-bottom: 25px;
      color: #003366; /* כותרת ראשית כהה יותר */
  }

  p {
      margin-bottom: 15px;
  }

  ul {
    list-style: disc inside; /* גולות בתוך השוליים */
    margin-right: 20px; /* שוליים מצד ימין לרשימות */
    padding-right: 0;
    margin-bottom: 15px;
  }

  li {
      margin-bottom: 10px; /* רווח גדול יותר בין פריטי רשימה */
      line-height: 1.6;
  }

  /* --- קטע הספרותי --- */
  .passage-container {
      margin-bottom: 25px;
      padding: 20px;
      background-color: #e9f5ff; /* רקע בהיר לקטע */
      border-left: 5px solid #007bff; /* פס צבעוני בצד ימין */
      border-radius: 8px;
      font-style: italic;
      font-size: 1.1em; /* גודל גופן מעט גדול יותר */
      line-height: 1.8;
      color: #333;
      box-shadow: inset 0 1px 5px rgba(0,0,0,0.05); /* צל פנימי עדין */
  }

  /* --- כפתורי בחירה --- */
  #choices {
    display: flex;
    justify-content: center;
    gap: 15px; /* רווח גדול יותר בין הכפתורים */
    margin-bottom: 20px;
  }

  .choice-button {
    padding: 12px 20px; /* ריפוד גדול יותר */
    border: none;
    border-radius: 25px; /* כפתורים מעוגלים */
    cursor: pointer;
    font-size: 1.05em; /* גודל גופן מעט גדול יותר */
    font-weight: bold;
    transition: all 0.3s ease; /* אנימציית מעבר לכל המאפיינים */
    box-shadow: 0 2px 5px rgba(0,0,0,0.1); /* צל לכפתורים */
    text-shadow: 0 1px 1px rgba(0,0,0,0.05); /* צל קל לטקסט */
  }

  .choice-button[data-style="רומנטיקה"] { background-color: #ffadad; color: #7a0000; } /* אדום רך */
  .choice-button[data-style="ריאליזם"] { background-color: #a3e4a3; color: #004d00; } /* ירוק רך */
  .choice-button[data-style="מודרניזם"] { background-color: #adadff; color: #00007a; } /* כחול סגול רך */

  .choice-button:hover:not(:disabled) {
    transform: translateY(-2px); /* אנימציה קלה בריחוף */
    box-shadow: 0 4px 10px rgba(0,0,0,0.2); /* צל מודגש יותר בריחוף */
    opacity: 0.95;
  }

  .choice-button:active:not(:disabled) {
      transform: translateY(0); /* אנימציה קלה בלחיצה */
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
  }

  .choice-button:disabled {
      opacity: 0.6;
      cursor: not-allowed;
      box-shadow: none;
  }


  /* --- משוב והסבר לקטע --- */
  #feedback {
    margin-top: 20px; /* רווח גדול יותר אחרי הכפתורים */
    padding: 15px;
    border-radius: 8px;
    text-align: center;
    font-weight: bold;
    min-height: 1.5em; /* שמירת מקום גדולה יותר */
    opacity: 0; /* מתחיל שקוף לאנימציה */
  }

  #feedback.correct {
    background-color: #d4edda;
    color: #155724;
    border: 1px solid #c3e6cb;
  }

  #feedback.incorrect {
    background-color: #f8d7da;
    color: #721c24;
    border: 1px solid #f5c6cb;
  }

  .explanation-box {
      margin-top: 20px;
      padding: 15px;
      background-color: #fff3cd; /* רקע צהבהב עדין */
      color: #856404;
      border: 1px solid #ffeeba;
      border-radius: 8px;
      text-align: right;
      direction: rtl;
      overflow: hidden; /* חיוני לאנימציית גובה */
  }


  /* --- כפתורי ניווט --- */
  .nav-button {
      display: block;
      margin: 25px auto 0; /* ריווח גדול יותר מלמעלה */
      padding: 12px 25px; /* ריפוד גדול יותר */
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 25px; /* כפתורים מעוגלים */
      cursor: pointer;
      font-size: 1.1em;
      font-weight: bold;
      transition: all 0.3s ease;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1);
      display: flex; /* כדי למרכז את הטקסט והחץ */
      align-items: center;
      justify-content: center;
  }

  .nav-button .arrow {
      margin-right: 8px; /* רווח בין הטקסט לחץ */
      transition: margin-right 0.3s ease;
  }

  .nav-button:hover:not(:disabled) {
      background-color: #0056b3;
      transform: translateY(-2px);
      box-shadow: 0 4px 10px rgba(0,0,0,0.2);
  }

  .nav-button:hover .arrow {
      margin-right: 4px; /* הזזת החץ קצת בריחוף */
  }

   .nav-button:active:not(:disabled) {
      transform: translateY(0);
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
   }

   .nav-button:disabled {
      opacity: 0.6;
      cursor: not-allowed;
      background-color: #cccccc; /* צבע אפור כשהכפתור לא פעיל */
      box-shadow: none;
   }


  .secondary-button {
      background-color: #6c757d; /* צבע אפור כהה יותר לכפתור המשני */
      margin-top: 15px; /* רווח קטן יותר מלמעלה */
  }

  .secondary-button:hover:not(:disabled) {
      background-color: #545b62;
  }

  /* --- הסבר מלא על הסגנונות --- */
  .explanation-content {
    margin-top: 25px;
    padding: 25px;
    background-color: #eef2ff; /* רקע כחלחל בהיר */
    border: 1px solid #d0d9ff;
    border-radius: 12px;
    overflow: hidden; /* חיוני לאנימציית גובה */
    max-height: 0; /* מתחיל סגור */
    transition: max-height 0.5s ease-in-out, opacity 0.5s ease-in-out; /* אנימציה לפתיחה/סגירה */
    opacity: 0; /* מתחיל שקוף */
    padding-top: 0; /* ריפוד עליון וירטואלי עבור אנימציה */
    padding-bottom: 0; /* ריפוד תחתון וירטואלי עבור אנימציה */
  }

  .explanation-content.is-visible {
      max-height: 2000px; /* ערך מספיק גדול להכיל את כל התוכן */
      opacity: 1;
      padding-top: 25px; /* ריפוד עליון אמיתי כשגלוי */
      padding-bottom: 25px; /* ריפוד תחתון אמיתי כשגלוי */
  }

  .explanation-content h2, .explanation-content h3 {
      color: #003366; /* כותרות כהות יותר בהסבר המלא */
      margin-top: 20px;
  }

  .explanation-content h2:first-child {
      margin-top: 0; /* אין רווח עליון לכותרת הראשונה */
  }


  /* --- אנימציות כלליות --- */
  .animated {
      animation-duration: 0.5s; /* זמן אנימציה ברירת מחדל */
      animation-fill-mode: both; /* שמור על המצב הסופי של האנימציה */
  }

  @keyframes fadeIn {
      from { opacity: 0; }
      to { opacity: 1; }
  }

  .fade-in {
      animation-name: fadeIn;
  }

  @keyframes slideDown {
      from { transform: translateY(-10px); opacity: 0; }
      to { transform: translateY(0); opacity: 1; }
  }

  .slide-down {
      animation-name: slideDown;
  }

  @keyframes shake {
      0%, 100% { transform: translateX(0); }
      10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
      20%, 40%, 60%, 80% { transform: translateX(5px); }
  }

  .shake {
      animation-name: shake;
      animation-duration: 0.6s;
  }

</style>

<script>
  const passages = [
    {
      passage: "הסערה השתוללה בחוץ, והרוח נהמה כמו חיה פצועה. על פסגת ההר ניצבתי, ליבי גאה מכאב ואהבה, מרגיש את עוצמת הטבע שוטפת אותי. הירח החיוור האיר את העמק הנסתר, הבטתי בו וידעתי שאני אחד עם הכאב הקדום של העולם. הטבע לא היה רק נוף, הוא היה מראה לנפשי הסוערת.",
      answer: "רומנטיקה",
      explanation: "קטע זה רומנטי בשל הדגש על רגש עז ('ליבי גאה מכאב ואהבה', 'נפשי הסוערת'), האדרת הטבע ככוח חי ועוצמתי המשתקף בנפש ('הרוח נהמה כמו חיה פצועה', 'עוצמת הטבע שוטפת אותי', 'הטבע... היה מראה לנפשי'), ותחושת האחדות המיסטית של היחיד עם העולם והכאב הקדום שבו ('אני אחד עם הכאב הקדום של העולם'). הדמיון משמש כגשר בין האדם לטבע וליקום."
    },
    {
      passage: "מר כהן ישב במטבח הקטן, לוגם קפה קר מוסף. על השולחן המט לנפול הונח עיתון ישן, ולידו קבלה מקומטת על חשבון חשמל גבוה מדי. קרני השמש אחר הצהריים חדרו דרך החלון המלוכלך, והאירו את שכבת האבק על הארונות הישנים. קולות הרחוב - שאון מכוניות, צעקות ילדים - חדרו מבעד לזגוגית. הוא נאנח, חושב על השכירות שתגיע בסוף החודש, ועל ריח הביוב העולה מהרחוב בקיץ.",
      answer: "ריאליזם",
      explanation: "קטע זה ריאליסטי בשל התיאור המדוקדק והאובייקטיבי של סצנה יומיומית ופשוטה, ללא ייפוי (מטבח קטן, קפה קר, עיתון ישן, קבלה מקומטת, חלון מלוכלך, אבק על ארונות ישנים). יש התייחסות לפרטים חברתיים ואורבניים (קולות הרחוב, ריח הביוב), עיסוק בדאגות אפורות וממשיות (חשבון חשמל גבוה, שכירות), והדגש על דמות אדם רגיל בהתמודדות עם שגרת חייו הקשה לעיתים. התיאור נאמן למציאות הנגלית לעין."
    },
    {
      passage: "המחשבות חלפו בראשי כמו קרונות רכבת שבורים על פסים עקומים. מה השעה? זה לא משנה. העיר בחוץ רעשה, קולות התערבבו לתוך צליל אחד חסר פשר, דיסה של רעש ואובדן כיוון. הוא הלך ברחוב, והרגשתי שאני הולך איתו, או שאולי הוא אני? גבולות העצמי התמוססו. זכרון מטושטש של בית קפה, ריח סיגריות, פנים זרות שצחקו בלי קול. הכל התפורר לאוסף רסיסים מנוכרים. מה הלאה? אין תשובה.",
      answer: "מודרניזם",
      explanation: "קטע זה מודרניסטי בשל שימוש בזרם תודעה מפורק ואסוציאטיבי ('מחשבות חלפו כמו קרונות רכבת שבורים', 'דיסה של רעש ואובדן כיוון'), תחושת ניכור, בלבול ואובדן שליטה ('חסר פשר', 'הכל התפורר', 'אין תשובה'), ערעור על גבולות הזהות ('הרגשתי שאני הולך איתו, או שאולי הוא אני?', 'גבולות העצמי התמוססו'), ותיאור מציאות מפורקת, מטושטשת וחסרת פשר ברור. הניסיון ללכוד את חווית התודעה הפנימית גובר על תיאור עלילה או מציאות חיצונית קוהרנטית."
    },
     {
      passage: "היא רכנה אל עבר השושנה הפורחת, שהיה עליה עוד טללי בוקר נוצצים כמו יהלומים זעירים. צבעה האדום העמוק דיבר אל נשמתה הסוערת, לחש לה סודות אהבה עתיקים של כוחות קוסמיים. הרגש עטף אותה כגל חם של קדושה ופליאה, והיא חשה את יופיו הנצחי של הרגע, קשור לכל היופי האינסופי שאי פעם היה ויהיה ביקום הגדול. הרגש גבר על השכל, והנשמה נפתחה לפלא.",
      answer: "רומנטיקה",
      explanation: "מאפיינים רומנטיים מובהקים: האנשת הטבע והענקת משמעות מיסטית ('השושנה... דיבר אל נשמתה... לחש לה סודות אהבה עתיקים של כוחות קוסמיים'), רגש עז וחוויה רוחנית ('הרגש עטף אותה כגל חם של קדושה ופליאה', 'נשמתה הסוערת'), תחושה של יופי נצחי ואוניברסלי הקשור לחוויה אישית ורגשית עמוקה ('קשור לכל היופי האינסופי שאי פעם היה ויהיה ביקום הגדול'), והדגשת עליונות הרגש על השכל ('הרגש גבר על השכל')."
    },
    {
      passage: "בחדר המרוהט בפשטות עמד שולחן עץ כבד ושלושה כיסאות תואמים. על הקירות, שצבעם הלבן החל להתקלף בפינות בגלל הרטיבות הישנה, תלויות היו שתי תמונות משפחתיות מצהיבות במסגרות עץ פשוטות. השעה היתה שש בדיוק בערב כשנכנסו האב והבן מהשדה, נעלי העבודה שלהם מכוסות אבק אדום שנשאר על השטיח הישן. האם הגישה מרק דל על השולחן.",
      answer: "ריאליזם",
      explanation: "מאפיינים ריאליסטיים: תיאור ענייני, מדויק ומלא פרטים של חלל וחפצים יומיומיים, כולל פגמים ('חדר המרוהט בפשטות', 'שולחן עץ כבד ושלושה כיסאות', 'קירות... צבעם הלבן החל להתקלף בפינות בגלל הרטיבות הישנה', 'תמונות משפחתיות מצהיבות במסגרות עץ פשוטות'). הצגת שגרת יום יומית מדויקת ומציאותית ('השעה היתה שש בדיוק', 'נכנסו מהשדה'), התמקדות באנשים רגילים ועבודתם הפיזית ('נעלי העבודה שלהם מכוסות אבק אדום'), ותיאור חיים פשוטים ולעיתים קשים ('האם הגישה מרק דל על השולחן'). הכל מתואר באופן עובדתי כמעט."
    },
    {
      passage: "זיגזג מחשבות - עורב שחור על עמוד חשמל, השיר ברדיו לא נגמר לעולם, למה הסוכר נגמר תמיד כשהכי רוצים קפה? הפנים במראה לא מוכרות יותר, הן היו פעם משהו אחר, משהו שהיה הגיוני. העבר? עתיד? הכל מתערבב למרק סמיך וחסר צורה, קולות מתנגשים, תמונות מהבהבות. צריך לקנות חלב. ומה עם הדלת שנפתחה לפני רגע? מי נכנס? לא יודע. אולי אני נכנסתי.",
      answer: "מודרניזם",
      explanation: "מאפיינים מודרניסטיים: זרם תודעה מפורק, אסוציאטיבי ולא ליניארי, המערבב הרהורים קיומיים (זהות, זמן) עם מחשבות טריוויאליות ('עורב שחור', 'שיר ברדיו', 'סוכר', 'צריך לקנות חלב'). תחושת אובדן עצמיות, ניכור ובלבול ('הפנים במראה לא מוכרות', 'מרק סמיך וחסר צורה', 'מי נכנס? לא יודע. אולי אני נכנסתי'). ערעור על מושגי זמן, מקום ומציאות קוהרנטית. הקטע מנסה לשקף את הכאוס והפיצול של התודעה המודרנית."
    }
  ];

  let passagesOrder = [];
  let currentPassageIndex = -1;
  const passageElement = document.getElementById('passage');
  const choicesElement = document.getElementById('choices');
  const feedbackElement = document.getElementById('feedback');
  const passageExplanationElement = document.getElementById('passageExplanation');
  const nextPassageButton = document.getElementById('nextPassage');
  const toggleExplanationButton = document.getElementById('toggleExplanation');
  const explanationContentElement = document.getElementById('explanationContent');

  // פונקציית ערבוב מערך
  function shuffleArray(array) {
      for (let i = array.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          [array[i], array[j]] = [array[j], array[i]]; // החלפה
      }
      return array;
  }

  function loadNextPassage() {
    // הכנה לקטע חדש
    feedbackElement.textContent = '';
    feedbackElement.className = ''; // נקה מחלקות משוב קודמות
    feedbackElement.style.opacity = 0; // הסתר משוב לפני אנימציה
    passageExplanationElement.style.display = 'none';
    passageExplanationElement.textContent = '';
    nextPassageButton.style.display = 'none';
    enableChoices();

    // אם זו הפעם הראשונה או שנגמרו הקטעים, ערבב מחדש והתחל
    if (currentPassageIndex === -1 || currentPassageIndex >= passagesOrder.length - 1) {
       passagesOrder = shuffleArray([...passages]); // ערבב עותק של המערך המקורי
       currentPassageIndex = 0;
    } else {
       currentPassageIndex++;
    }

    const currentPassageData = passagesOrder[currentPassageIndex];

    // אנימציה של יציאת הקטע הנוכחי (אופציונלי, נשאיר את זה פשוט עם fade-in לחדש)
    passageElement.style.opacity = 0; // הסתר את הקטע לפני טעינה

    // טעינת הקטע החדש והצגתו עם אנימציה
    setTimeout(() => { // השהייה קלה לפני הצגת הקטע החדש
        passageElement.textContent = currentPassageData.passage;
        passageElement.classList.remove('fade-in'); // הסר את המחלקה כדי לאפשר הפעלה חוזרת של האנימציה
        void passageElement.offsetWidth; // טריק כדי לאפס את האנימציה
        passageElement.classList.add('fade-in');
        passageElement.style.opacity = 1;
    }, 100); /* זמן השהייה קצר */

  }

  function handleChoiceClick(event) {
    const selectedStyle = event.target.dataset.style;
    const currentPassageData = passagesOrder[currentPassageIndex];

    disableChoices(); // השבת כפתורים לאחר בחירה

    let feedbackText;
    let feedbackClass;
    let showExplanation = false;

    if (selectedStyle === currentPassageData.answer) {
      feedbackText = 'נכון! הצלחתם לפענח את הסגנון הספרותי!';
      feedbackClass = 'correct';
      showExplanation = false; // אל תציג הסבר לקטע אם נכון
    } else {
      feedbackText = `טעות, בלשים יקרים. הסגנון הנכון הוא ${currentPassageData.answer}.`;
      feedbackClass = 'incorrect';
      showExplanation = true; // הצג הסבר לקטע אם טעות
    }

    // הצגת המשוב עם אנימציה
    feedbackElement.textContent = feedbackText;
    feedbackElement.className = 'animated fade-in ' + feedbackClass; // הוסף מחלקת אנימציה ומחלקת סגנון
    feedbackElement.style.opacity = 1; // הפוך לגלוי

     if (feedbackClass === 'incorrect') {
        feedbackElement.classList.add('shake'); // הוסף אנימציית ניעור לטעות
     } else {
         feedbackElement.classList.remove('shake');
     }


    // הצגת הסבר לקטע עם אנימציה אם יש צורך
    if (showExplanation) {
      passageExplanationElement.textContent = `הסבר: ${currentPassageData.explanation}`;
      passageExplanationElement.style.display = 'block';
      // אנימציה מבוססת CSS, display: block מאפשר לחשב גובה ואז להפעיל אנימציה
      passageExplanationElement.classList.remove('slide-down');
      void passageExplanationElement.offsetWidth; // טריק לאיפוס
      passageExplanationElement.classList.add('slide-down');

    } else {
         // אם אין הסבר, ודא שהוא מוסתר
        passageExplanationElement.style.display = 'none';
    }


    // הצגת כפתור המעבר לקטע הבא עם אנימציה
    setTimeout(() => { // השהייה קלה לפני הצגת הכפתור הבא
        nextPassageButton.style.display = 'flex'; // השתמש ב-flex כדי לשמור על המרכוז
        nextPassageButton.classList.remove('fade-in'); // איפוס אנימציה
        void nextPassageButton.offsetWidth;
        nextPassageButton.classList.add('fade-in');
    }, 1000); // הצג אחרי שנייה

  }

  function disableChoices() {
      document.querySelectorAll('.choice-button').forEach(button => {
          button.disabled = true;
      });
  }

   function enableChoices() {
      document.querySelectorAll('.choice-button').forEach(button => {
          button.disabled = false;
      });
  }

  // הוספת מאזינים לאירועים
  document.querySelectorAll('.choice-button').forEach(button => {
    button.addEventListener('click', handleChoiceClick);
  });

  nextPassageButton.addEventListener('click', loadNextPassage);

  toggleExplanationButton.addEventListener('click', () => {
    const isHidden = !explanationContentElement.classList.contains('is-visible');

    if (isHidden) {
        explanationContentElement.style.display = 'block'; // אפשר הצגה כדי לחשב גובה
        setTimeout(() => { // השהייה קלה לאחר שינוי display לפני הפעלת אנימציה
            explanationContentElement.classList.add('is-visible');
            toggleExplanationButton.textContent = 'הסתר הסבר מקיף על הסגנונות';
        }, 10); // השהייה מינימלית
    } else {
        explanationContentElement.classList.remove('is-visible');
        toggleExplanationButton.textContent = 'הצג הסבר מקיף על הסגנונות';
        // ניתן להוסיף setTimeout נוסף כדי להסתיר display לאחר שהאנימציה מסתיימת, אך זה פחות קריטי
         setTimeout(() => {
             if (!explanationContentElement.classList.contains('is-visible')) {
                  explanationContentElement.style.display = 'none';
             }
         }, 500); // זמן תואם לאנימציה
    }
  });


  // טעינת הקטע הראשון בהתחלה
  loadNextPassage();

</script>
```