---
title: "מלט ובטון: חומרי הבנייה המופלאים"
english_slug: cement-concrete-materials-that-build-the-world
category: "הנדסה"
tags:
  - מלט
  - בטון
  - בנייה
  - חומרי גלם
  - הנדסה אזרחית
  - תהליך יצור
---
# מלט ובטון: חומרי הבנייה המופלאים

דמיינו עולם בלי גשרים ענקיים, בניינים שנוגעים בשמיים או כבישים אינסופיים. כמעט בלתי אפשרי, נכון? כל אלה ועוד הרבה נוצרו בזכות שני חומרים קסומים: מלט ובטון. אבל מהו הסוד שלהם? איך אבן רגילה והאדמה מתאחדות כדי ליצור את עמודי התווך של הציוויליזציה המודרנית? בואו נצא למסע מרתק בעקבות החומרים שבונים את העולם שלנו, ונראה צעד אחר צעד איך זה קורה!

<div class="interactive-container">
    <div id="animation-area">
        <div class="process-flow">
            <div class="stage" id="stage-1" data-title="חומרי גלם נאספים" data-popup-text="המסע מתחיל במחצבה! אבן גיר וחרסית, חומרי היסוד של המלט, נכרים ונבנים לגודל התחלתי.">
                <div class="icon">⛰️</div>
                <div class="stage-label">איסוף חומרים</div>
            </div>
            <div class="arrow"></div>
            <div class="stage" id="stage-2" data-title="טחינה לעיסה אחידה" data-popup-text="החומרים נטחנים דק-דק ומעורבבים יחד ביחסים מדויקים, כמו מתכון סודי!">
                <div class="icon">🔄</div>
                <div class="stage-label">עירוב וטחינה</div>
            </div>
             <div class="arrow"></div>
            <div class="stage" id="stage-3" data-title="חימום עוצמתי בכבשן" data-popup-text="התערובת נכנסת לכבשן ענק ורותח (עד 1450°C!). החום הופך אותה לגושים קטנים וקסומים שנקראים 'קלינקר'.">
                <div class="icon">🔥</div>
                <div class="stage-label">תנור רותח</div>
            </div>
             <div class="arrow"></div>
             <div class="stage" id="stage-4" data-title="טחינת הקלינקר למלט" data-popup-text="גושי הקלינקר נטחנים שוב, הפעם לאבקה דקיקה שאתם מכירים - המלט! מוסיפים מעט גבס לוויסות הקשיחה.">
                <div class="icon">🌪️</div>
                <div class="stage-label">לידת המלט</div>
            </div>
            <div class="arrow cement-to-concrete"></div> {/* Special arrow for transition */}
             <div class="stage" id="stage-5" data-title="הכנת תערובת הבטון" data-popup-text="עכשיו לקסם הבא! את המלט מערבבים עם מים, חול, חצץ (אגרגטים) ולפעמים גם תוספים מיוחדים.">
                <div class="icon">💦 + 🏖️ + 🗿</div>
                <div class="stage-label">מלט פוגש מים</div>
            </div>
             <div class="arrow"></div>
             <div class="stage" id="stage-6" data-title="יציקה וקשיחה" data-popup-text="התערובת הטריה נשפכת לתבניות. מתחילה ריאקציה כימית עם המים שהופכת אותה לחומר קשיח, חזק ועמיד להפליא - הבטון המוכר!">
                <div class="icon">🏗️</div>
                <div class="stage-label">בטון מוכן!</div>
            </div>
        </div>
        <div id="stage-popup" class="explanation-popup">
             <h3 id="popup-title"></h3>
             <p id="popup-text"></p>
        </div>
    </div>
    <div class="controls">
        <button id="start-btn">התחלה</button>
        <button id="prev-step-btn" disabled>שלב קודם</button> {/* Added Previous button */}
        <button id="next-step-btn">שלב הבא</button>
        <button id="play-all-btn">נגן הכל</button>
    </div>
</div>

<button id="toggle-explanation-btn" class="toggle-button">הצג הסבר מלא</button>
<div id="full-explanation" style="display: none;">
    <h2>מלט: הדבק של הבנייה</h2>
    <p>מלט הוא אבקה דקה המשמשת כחומר מקשר בתערובות בנייה כמו בטון וטיח. תפקידו העיקרי הוא להתקשר (להתקשות) בתגובה כימית עם מים, ולחבר יחד חומרים אחרים (אגרגטים) למסה אחידה וקשיחה.</p>
    <p>השימוש בחומרי מליטה קיים כבר אלפי שנים, החל מחומרים טבעיים (כמו גבס או סיד) ועד לפיתוח המלט הפורטלנדי המודרני במאה ה-19, שהוא הבסיס למרבית המלט בשימוש כיום בזכות עמידותו וחוזקו.</p>

    <h2>חומרי הגלם לייצור מלט</h2>
    <p>החומרים העיקריים לייצור מלט פורטלנדי הם אבן גיר (המכילה בעיקר סידן פחמתי - CaCO3) וחרסית (המכילה סיליקה, אלומינה ותחמוצת ברזל). חומרים אלו מספקים את התחמוצות העיקריות הדרושות ליצירת מינרלי הקלינקר בכבשן (CaO, SiO2, Al2O3, Fe2O3).</p>
    <p>חומרים נוספים כמו עפרות ברזל, בוקסיט (מקור לאלומיניום) ואפר פחם משמשים לתיקון ההרכב הכימי המדויק של התערובת הגולמית לפני הכניסה לכבשן, כדי להבטיח את היחסים הנכונים בין התחמוצות.</p>

    <h2>תהליך ייצור המלט (תהליך יבש)</h2>
    <ul>
        <li>**כרייה וגריסה ראשונית:** אבן הגיר והחרסית נכרים ממחצבות סמוכות למפעל. החומרים הגדולים נגרסים לגודל מתאים (כמה סנטימטרים) על מנת לאפשר את שינועם ואחסונם הראשוני.</li>
        <li>**טחינה וערבוב החומרים הגולמיים (Raw Meal):** השלב הבא הוא טחינה עדינה מאוד של חומרי הגלם במטחנות מיוחדות (למשל, מטחנות כדוריות או מטחנות רולר אנכיות). החומרים היבשים נטחנים יחד ומעורבבים ליצירת אבקה הומוגנית הנקראת "קמח גולמי" (Raw Meal). ההרכב הכימי של הקמח הגולמי נבדק ומותאם בקפדנות.</li>
        <li>**חימום בכבשן סיבובי (שלב הקלינקר):** הקמח הגולמי מוזן לתוך כבשן סיבובי ענק, גליל פלדה באורך עשרות ואף מאות מטרים המסתובב באיטיות ומוטה מעט. בכבשן, המחומם בדרך כלל על ידי שריפת פחם, גז או דלקים חלופיים, החומר עובר תהליכי חימום אינטנסיביים. בטמפרטורות של כ-800-1000°C מתרחש תהליך הדקרבוניזציה (פירוק אבן הגיר ל-CaO ו-CO2), ובאזור החם ביותר (עד 1450°C) מתרחשת תגובת ה-Clinkerization בה נוצרים מינרלי הקלינקר העיקריים. החומר היוצא מהכבשן מקורר במהירות ונקרא "קלינקר" - גושים קטנים ושחורים בגודל של עד כ-2-3 ס"מ.</li>
        <li>**טחינת הקלינקר למלט סופי:** גושי הקלינקר מקוררים ונאגרים. לבסוף, הם נטחנים שוב במטחנות מיוחדות לאבקה דקה מאוד - המלט המוגמר. בשלב זה מוסיפים כמות קטנה (בדרך כלל 3%-5%) של גבס (סידן גופרתי) שתפקידו העיקרי הוא לווסת את זמן ההתקשרות הראשונית של המלט כשהוא מעורבב עם מים (מניעת התקשרות בזק). ניתן להוסיף גם חומרים נוספים (כמו אפר פחם, סיגים מתעשיית הברזל והפלדה) כדי ליצור סוגי מלט שונים בעלי תכונות מגוונות וגם כדי לשפר את הקיימות הסביבתית של המוצר.</li>
    </ul>

    <h2>קלינקר - הלב הפועם של המלט</h2>
    <p>קלינקר הוא למעשה חצי המוצר בתהליך ייצור המלט, והוא המרכיב הפעיל העיקרי במלט הפורטלנדי. הוא מורכב ממספר מינרלים סינתטיים שנוצרו בתגובות הכימיות בכבשן: C3S (טרי-קלציום סיליקט, Alite), C2S (די-קלציום סיליקט, Belite), C3A (טרי-קלציום אלומינט, Aluminate) ו-C4AF (טטרה-קלציום אלומינו-פריט, Ferrite). מינרלים אלו הם שאחראים, בתגובתם עם מים (הידרציה), לפיתוח החוזק והקשיחות של המלט.</p>

    <h2>בטון: החומר המורכב והעמיד</h2>
    <p>בטון הוא חומר מרוכב (Composite) רב עוצמה, והוא למעשה החומר הנפוץ ביותר בעולם אחרי מים. הוא נוצר מערבוב של שלושה מרכיבים עיקריים ועוד אחד חיוני:</p>
    <ul>
        <li>**מלט:** הדבק שמחבר את הכל יחד.</li>
        <li>**אגרגטים:** חומר המילוי העיקרי, המהווה כ-60-80% מנפח הבטון. הוא כולל חול (אגרגט דק, גודל גרגר עד כ-5 מ"מ) וחצץ (אגרגט גס, גודל גרגר עד כ-20-40 מ"מ או יותר). האגרגטים מקנים לבטון יציבות נפחית ומסייעים בפיתוח חוזק.</li>
        <li>**מים:** הכרחיים ליצירת תגובת ההידרציה עם המלט וליצירת העבידות הנדרשת ליציקת התערובת הטריה.</li>
        <li>**תוספים (אופציונלי):** חומרים שונים המווסתים או משפרים תכונות ספציפיות של הבטון, הן במצב הטרי והן במצב הקשוי. לדוגמה: מקטיני מים (לשיפור העבידות עם כמות מים נמוכה יותר), מאיצים/מאחרים (לשליטה על זמן ההתקשרות), סופחי אוויר (לשיפור העמידות בפני קפיאה והפשרה), מעכבי קורוזיה ועוד.</li>
    </ul>

    <h2>תהליך ערבול הבטון והתקשרותו (הידרציה)</h2>
    <p>כאשר מערבבים מלט עם מים, מתרחשת תגובה כימית אקסותרמית (פולטת חום) הנקראת **הידרציה**. מינרלי הקלינקר מגיבים עם המים ויוצרים גבישים מיקרוסקופיים חדשים (בעיקר ג'ל C-S-H - סידן-סיליקט-הידרט) הממלאים את החללים שבין האגרגטים ויוצרים מבנה גבישי צפוף שמקשר אותם יחד. תהליך זה מוביל בהדרגה להתקשות התערובת (סט) ובהמשך לפיתוח חוזק משמעותי לאורך זמן (התקשות - Hardening).</p>
    <p>יחס המים למלט (Water-Cement Ratio - W/C) הוא אחד הפרמטרים החשובים ביותר המשפיעים על חוזק ועמידות הבטון. ככל שהיחס נמוך יותר (פחות מים ביחס למלט), כך הבטון המתקשה יהיה בדרך כלל חזק ועמיד יותר (בתנאי שיש מספיק מים לתגובת הידרציה מלאה ועבידות מספקת ליציקה ולדחיסה). עודף מים יוצר נקבוביות בתוך הבטון הקשוי ומחליש אותו.</p>

    <h2>יישומים של בטון בעולם המודרני</h2>
    <p>בטון הוא חומר הבנייה הנפוץ ביותר בעולם, והוא חיוני לרוב פרויקטי ההנדסה האזרחית. הוא משמש למגוון אדיר של יישומים בזכות חוזקו, עמידותו, יכולת העיצוב שלו בצורה טריה, ועלותו הנמוכה יחסית. שימושים נפוצים כוללים: יסודות ושלד מבנים (עמודים, קורות, תקרות, קירות), גשרים, כבישים ורחובות, סכרים ותשתיות מים, מנהרות, שדות תעופה, רציפים ונמלים, ואף אלמנטים אדריכליים ופסלים.</p>

    <h2>היבטים סביבתיים</h2>
    <p>ייצור מלט הוא תהליך תעשייתי עתיר אנרגיה ובעל טביעת רגל פחמנית משמעותית. פליטות הפחמן הדו-חמצני (CO2) בתהליך נובעות משני מקורות עיקריים: שריפת דלקים להשגת הטמפרטורות הגבוהות בכבשן (כ-30-40% מהפליטות) ובעיקר מתהליך הדקרבוניזציה של אבן הגיר (פירוק CaCO3 ל-CaO ול-CO2) בכבשן (כ-60-70% מהפליטות). תעשיית המלט העולמית מחויבת לצמצום השפעותיה הסביבתיות באמצעות: שיפור יעילות אנרגטית, שימוש בדלקים חלופיים (פסולת, ביומסה), שימוש בחומרים משלימים למלט (Supplementary Cementitious Materials - SCMs) כמו אפר פחם וסיגים כתחליף חלקי לקלינקר (מה שמפחית את כמות הקלינקר הדרושה ולכן את הפליטות), ופיתוח טכנולוגיות חדשניות כמו לכידת ואחסון פחמן (CCS).</p>
</div>

<style>
/* General styles */
body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    color: #333;
    direction: rtl; /* Ensure RTL is set */
    text-align: right; /* Ensure text aligns right */
}

h1, h2, h3 {
    color: #004080; /* Deep blue for headings */
}

p, ul, li {
     text-align: right;
}

/* Interactive Container */
.interactive-container {
    margin-bottom: 30px;
    padding: 25px;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    background: linear-gradient(to bottom, #f8f8f8, #f0f0f0); /* Subtle gradient */
    overflow-x: auto; /* Allow horizontal scrolling */
    box-shadow: 0 4px 10px rgba(0,0,0,0.1); /* Soft shadow */
    scrollbar-width: thin; /* For Firefox */
    scrollbar-color: #0056b3 #f1f1f1; /* For Firefox */
}

/* Custom scrollbar for Webkit browsers */
.interactive-container::-webkit-scrollbar {
    height: 8px;
}

.interactive-container::-webkit-scrollbar-track {
    background: #f1f1f1;
    border-radius: 10px;
}

.interactive-container::-webkit-scrollbar-thumb {
    background: #0056b3;
    border-radius: 10px;
}

.interactive-container::-webkit-scrollbar-thumb:hover {
    background: #003d82;
}


#animation-area {
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative; /* Needed for absolute positioning of popup */
    padding-top: 60px; /* Space for the popup above */
    min-height: 250px; /* Ensure minimum height */
}

.process-flow {
    display: flex;
    align-items: center;
    gap: 30px; /* Increased space between elements */
    padding-bottom: 20px;
}

/* Stages (Cards) */
.stage {
    background-color: #ffffff;
    border: 2px solid #b0bec5; /* Light grey border */
    border-radius: 15px; /* More rounded corners */
    padding: 20px; /* Increased padding */
    width: 130px; /* Slightly wider */
    height: 160px; /* Slightly taller */
    text-align: center;
    cursor: pointer;
    transition: transform 0.4s ease-out, border-color 0.4s ease, box-shadow 0.4s ease;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    box-shadow: 0 3px 8px rgba(0,0,0,0.15); /* Improved shadow */
    flex-shrink: 0;
    user-select: none; /* Prevent text selection */
}

.stage:hover {
    transform: translateY(-8px); /* More pronounced hover effect */
    border-color: #78909c; /* Darker grey on hover */
    box-shadow: 0 6px 15px rgba(0,0,0,0.2);
}

.stage.active {
    border-color: #2e7d32; /* Green for active */
    box-shadow: 0 0 12px rgba(46, 125, 50, 0.6); /* Green glow */
    transform: translateY(-8px) scale(1.03); /* Slightly larger and lifted */
    background-color: #e8f5e9; /* Light green background for active */
    animation: pulse-active 1.5s infinite alternate ease-in-out; /* Pulse animation */
}

@keyframes pulse-active {
    0% { transform: translateY(-8px) scale(1.03); box-shadow: 0 0 12px rgba(46, 125, 50, 0.6); }
    100% { transform: translateY(-6px) scale(1.02); box-shadow: 0 0 15px rgba(46, 125, 50, 0.8); }
}


.stage .icon {
    font-size: 3.5em; /* Larger icons */
    margin-bottom: 8px; /* More space below icon */
    transition: transform 0.3s ease-in-out; /* Icon animation */
}
.stage.active .icon {
     transform: scale(1.1); /* Scale icon when active */
}


.stage-label {
    font-weight: bold;
    font-size: 1em; /* Slightly larger label */
    color: #333;
    text-wrap: pretty; /* Prevent awkward wrapping */
}

/* Arrows */
.arrow {
    font-size: 0; /* Hide text if using shape */
    width: 40px; /* Width of the arrow area */
    height: 10px; /* Height of the arrow line */
    background-color: #b0bec5; /* Grey line color */
    position: relative;
    flex-shrink: 0;
    transition: background-color 0.4s ease;
    margin: 0 -15px; /* Overlap slightly with stages */
}

.arrow::after {
    content: '';
    position: absolute;
    right: -15px; /* Position arrowhead */
    top: 50%;
    transform: translateY(-50%);
    border-top: 8px solid transparent;
    border-bottom: 8px solid transparent;
    border-right: 15px solid #b0bec5; /* Arrowhead color */
    transition: border-right-color 0.4s ease;
}

/* Active arrow styles */
.stage.active + .arrow,
.arrow.active { /* Not strictly needed with + selector, but good practice */
    background-color: #4caf50; /* Green color for active arrow */
}

.stage.active + .arrow::after,
.arrow.active::after {
     border-right-color: #4caf50; /* Green color for active arrowhead */
}

.arrow.cement-to-concrete {
     background-color: #ff9800; /* Orange for transition */
}
.arrow.cement-to-concrete::after {
     border-right-color: #ff9800; /* Orange arrowhead */
}


/* Explanation Popup */
#stage-popup { /* Use ID as there's only one controlled by JS */
    display: none;
    position: absolute;
    bottom: auto; /* Remove bottom positioning */
    top: 10px; /* Position fixed distance from top */
    left: 50%;
    transform: translateX(-50%);
    background-color: #fff;
    border: 1px solid #ccc;
    border-radius: 8px; /* Slightly more rounded */
    padding: 15px; /* More padding */
    width: 250px; /* Wider popup */
    max-width: 80%; /* Max width for responsiveness */
    z-index: 20; /* Higher z-index */
    box-shadow: 0 4px 15px rgba(0,0,0,0.3); /* Stronger shadow */
    text-align: right;
    font-size: 0.95em;
    opacity: 0; /* Start hidden */
    transform: translateX(-50%) translateY(-10px); /* Slight starting offset */
    transition: opacity 0.3s ease-out, transform 0.3s ease-out;
}

#stage-popup.visible { /* Class added by JS when showing */
    opacity: 1;
    transform: translateX(-50%) translateY(0);
}


#stage-popup h3 {
    margin-top: 0;
    margin-bottom: 8px; /* More space below title */
    font-size: 1.1em; /* Larger title */
    color: #0056b3;
    border-bottom: 1px solid #eee; /* Separator line */
    padding-bottom: 5px;
}

#stage-popup p {
    margin: 0;
    line-height: 1.5;
}

/* Arrow pointing down from popup */
#stage-popup::after {
    content: '';
    position: absolute;
    top: 100%; /* Position below the popup */
    left: 50%;
    transform: translateX(-50%); /* Center the arrow */
    border-width: 10px;
    border-style: solid;
    border-color: #fff transparent transparent transparent; /* White arrow */
}
#stage-popup::before {
    content: '';
    position: absolute;
    top: calc(100% + 1px); /* Border slightly below */
    left: 50%;
    transform: translateX(-50%); /* Center the arrow */
    border-width: 10px;
    border-style: solid;
    border-color: #ccc transparent transparent transparent; /* Border color */
}


/* Controls */
.controls {
    text-align: center;
    margin-top: 25px; /* More space above controls */
}

.controls button, .toggle-button { /* Combined button styles */
    padding: 12px 24px; /* More padding */
    margin: 0 8px; /* Space between buttons */
    border: none;
    border-radius: 6px; /* Slightly more rounded */
    cursor: pointer;
    font-size: 1.05em; /* Slightly larger font */
    transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.controls button:hover:not(:disabled), .toggle-button:hover:not(:disabled) {
    opacity: 0.95; /* Less opacity change on hover */
    transform: translateY(-1px); /* Subtle lift on hover */
    box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}
.controls button:active:not(:disabled), .toggle-button:active:not(:disabled) {
     transform: translateY(0); /* Press effect */
     box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

.controls button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
    box-shadow: none;
    transform: none;
}


#start-btn { background-color: #007bff; color: white; } /* Blue */
#next-step-btn { background-color: #ffc107; color: #333; } /* Yellow/Orange */
#prev-step-btn { background-color: #6c757d; color: white; } /* Grey */
#play-all-btn { background-color: #28a745; color: white; } /* Green */
.toggle-button { background-color: #17a2b8; color: white; margin-top: 25px; display: block; margin-left: auto; margin-right: auto;} /* Cyan, block for centering */


/* Full Explanation Section */
#full-explanation {
    margin-top: 30px;
    padding: 25px; /* More padding */
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    background-color: #ffffff;
    line-height: 1.7; /* Increased line height */
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
}

#full-explanation h2 {
    color: #004080; /* Deep blue */
    border-bottom: 2px solid #007bff; /* Blue underline */
    padding-bottom: 8px; /* More space below title */
    margin-top: 25px;
    margin-bottom: 15px;
    font-size: 1.8em;
}
#full-explanation h2:first-child {
    margin-top: 0;
}


#full-explanation h3 {
    color: #0056b3; /* Medium blue */
    margin-top: 20px;
    margin-bottom: 10px;
    font-size: 1.4em;
}

#full-explanation ul {
    list-style: disc outside; /* Disc outside the text block */
    padding-right: 25px; /* More padding */
    margin-bottom: 15px;
}

#full-explanation li {
    margin-bottom: 10px; /* More space between list items */
}

#full-explanation p {
    margin-bottom: 15px; /* Space between paragraphs */
}

/* Responsive adjustments (optional but good practice) */
@media (max-width: 768px) {
    .process-flow {
        flex-wrap: nowrap; /* Ensure horizontal scroll */
        justify-content: flex-start;
    }
    .stage {
        width: 100px;
        height: 130px;
        padding: 15px;
    }
    .stage .icon {
        font-size: 3em;
    }
    .stage-label {
        font-size: 0.9em;
    }
    .arrow {
        width: 20px;
        margin: 0 -10px;
    }
     .arrow::after {
        right: -10px;
        border-top-width: 6px;
        border-bottom-width: 6px;
        border-right-width: 10px;
     }
    #stage-popup {
        width: 200px;
        max-width: 90%;
    }
    .controls button, .toggle-button {
        padding: 10px 15px;
        font-size: 0.95em;
        margin: 5px;
    }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const stages = document.querySelectorAll('.stage');
    const arrows = document.querySelectorAll('.arrow');
    const prevBtn = document.getElementById('prev-step-btn');
    const nextBtn = document.getElementById('next-step-btn');
    const playBtn = document.getElementById('play-all-btn');
    const startBtn = document.getElementById('start-btn');
    const toggleExplanationBtn = document.getElementById('toggle-explanation-btn');
    const fullExplanationDiv = document.getElementById('full-explanation');
    const stagePopup = document.getElementById('stage-popup');
    const popupTitle = document.getElementById('popup-title');
    const popupText = document.getElementById('popup-text');

    let currentStageIndex = -1;
    let playInterval = null;
    const playSpeed = 2500; // milliseconds

    // Function to update button states
    function updateButtonStates() {
        prevBtn.disabled = currentStageIndex <= 0;
        nextBtn.disabled = currentStageIndex >= stages.length - 1;
    }

    // Function to show a specific stage
    function showStage(index) {
        // Hide previous state
        if (currentStageIndex >= 0 && currentStageIndex < stages.length) {
             stages[currentStageIndex].classList.remove('active');
             if (currentStageIndex < arrows.length) {
                arrows[currentStageIndex].classList.remove('active');
             }
        }
        stagePopup.classList.remove('visible'); // Hide popup smoothly

        if (index >= 0 && index < stages.length) {
            currentStageIndex = index;
            const stageElement = stages[currentStageIndex];
            stages[currentStageIndex].classList.add('active');
             if (currentStageIndex < arrows.length) {
                arrows[currentStageIndex].classList.add('active');
             }


            // Update and show popup
            popupTitle.textContent = stageElement.dataset.title;
            popupText.textContent = stageElement.dataset.popupText;

            // Position popup above the active stage and center it
             const stageRect = stageElement.getBoundingClientRect();
             const containerRect = stageElement.closest('.interactive-container').getBoundingClientRect();
             const popupRect = stagePopup.getBoundingClientRect(); // Get popup dimensions before showing

             // Calculate left position relative to animation-area's left edge
             // Center of the stage relative to container
             const stageCenterInContainer = stageRect.left - containerRect.left + (stageRect.width / 2);
             // Position popup's center at stage's center
             let popupLeft = stageCenterInContainer - (popupRect.width / 2);

             // Clamp popup position to prevent it from going outside the container
             const padding = 10; // Some padding from container edges
             popupLeft = Math.max(popupLeft, padding);
             popupLeft = Math.min(popupLeft, containerRect.width - popupRect.width - padding);


             // Update popup style (relative to #animation-area)
             // Need to calculate based on stage's position *within* animation-area's scrollable content
             // Simple approach: position relative to the visual center within the current view
             const stageCenterX_RelativeToAnimationArea = stageElement.offsetLeft + stageElement.offsetWidth / 2;
             const popupWidth = stagePopup.offsetWidth || 250; // Use default if not rendered yet

            // Position popup
             stagePopup.style.left = `${stageCenterX_RelativeToAnimationArea}px`; // Position based on stage center
             stagePopup.style.transform = 'translateX(-50%) translateY(-10px)'; // Center it and initial offset

            // Use a slight delay before showing the popup to match the animation
            setTimeout(() => {
                 stagePopup.classList.add('visible');
            }, 50); // Small delay

            // Scroll to the active stage if needed
            const animationArea = document.getElementById('animation-area');
            const stageElementLeft = stageElement.offsetLeft; // Position relative to animationArea
            const animationAreaScrollLeft = animationArea.scrollLeft;
            const animationAreaWidth = animationArea.offsetWidth;
            const stageWidth = stageElement.offsetWidth;

             // Calculate the desired scroll position to center the stage
             const targetScrollLeft = stageElementLeft - (animationAreaWidth / 2) + (stageWidth / 2);

             // Use smooth scrolling
             animationArea.scrollTo({
                left: targetScrollLeft,
                behavior: 'smooth'
            });


        } else {
             // Reset or indicate end
             currentStageIndex = -1;
             stagePopup.classList.remove('visible'); // Ensure popup is hidden
             // Optional: Show a "Process Complete" message or reset state
        }

        updateButtonStates();
    }

    // Navigation functions
    function nextStep() {
        if (currentStageIndex < stages.length - 1) {
            showStage(currentStageIndex + 1);
        } else {
             // End of process
             showStage(-1); // Hide popups and deactivate stages
             stopPlay();
             // Optional: Display a final message
        }
    }

     function prevStep() {
        if (currentStageIndex > 0) {
            showStage(currentStageIndex - 1);
        } else if (currentStageIndex === 0) {
            showStage(-1); // Go back to initial state
        }
     }

     function startProcess() {
        if (playInterval) stopPlay(); // Stop if playing
        showStage(0); // Start from the first stage
    }

    // Auto-play functionality
    function togglePlay() {
        if (playInterval) {
            stopPlay();
        } else {
            // If at the end or start, restart from the beginning
            if (currentStageIndex === -1 || currentStageIndex === stages.length - 1) {
                 startProcess();
            } else {
                 // Continue from current step (move to next step immediately then start interval)
                 nextStep();
            }
            playInterval = setInterval(nextStep, playSpeed); // Advance every X seconds
            playBtn.textContent = 'עצור נגינה';
        }
    }

     function stopPlay() {
        clearInterval(playInterval);
        playInterval = null;
        playBtn.textContent = 'נגן הכל';
     }


    // Event Listeners for Controls
    startBtn.addEventListener('click', startProcess);
    nextBtn.addEventListener('click', nextStep);
    prevBtn.addEventListener('click', prevStep); // Add listener for prev button
    playBtn.addEventListener('click', togglePlay);


    // Event Listeners for clicking stages
    stages.forEach((stage, index) => {
        stage.addEventListener('click', () => {
             if (playInterval) stopPlay(); // Stop play if user interacts directly
             showStage(index); // Go directly to clicked stage
        });
    });

    // Toggle full explanation
    toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = fullExplanationDiv.style.display === 'none';
        fullExplanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר מלא' : 'הצג הסבר מלא';
    });

    // Initial state: hide popups and set button states
     showStage(-1); // Hide all popups and remove active class
     updateButtonStates();

});
</script>
---
```