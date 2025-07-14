---
title: "בניית העיר האסורה: מסע אל ליבה של בייג'ינג הקיסרית"
english_slug: building-the-forbidden-city-journey-to-imperial-beijing
category: "מדעי הרוח / היסטוריה וארכאולוגיה"
tags: [היסטוריה, סין, אדריכלות, בייג'ינג, שושלת מינג, מגה-פרויקטים, הנדסה]
---
# בניית העיר האסורה: מסע אל ליבה של בייג'ינג הקיסרית

איך נבנה המגה-פרויקט ההיסטורי העצום הזה, ליבה הפועם של סין הקיסרית, ב-14 שנים בלבד? הצטרפו למסע בזמן וחוו בעצמכם את האתגרים והפתרונות הגאוניים שאיפשרו את בניית העיר האסורה, אחד משיאי האדריכלות והארגון של העולם העתיק.

<div id="forbidden-city-app">
    <h2 class="app-title">חוו את המסע: עקבו אחר השלבים</h2>
    <div id="construction-map">
        <!-- Visual representation will be built here dynamically or via CSS states -->
        <div class="map-overlay"></div> <!-- Used for visual effects -->

        <div class="construction-stage stage-1" data-stage="wood">
            <div class="stage-icon">🪵</div>
            <div class="stage-label">1. הבאת עץ</div>
        </div>
        <div class="construction-stage stage-2 disabled" data-stage="stone">
            <div class="stage-icon">🪨</div>
            <div class="stage-label">2. הובלת אבן</div>
        </div>
        <div class="construction-stage stage-3 disabled" data-stage="walls">
            <div class="stage-icon">🧱</div>
            <div class="stage-label">3. בניית חומות</div>
        </div>
        <div class="construction-stage stage-4 disabled" data-stage="buildings">
            <div class="stage-icon">🏛️</div>
            <div class="stage-label">4. הקמת ארמונות</div>
        </div>
        <div class="construction-stage stage-5 disabled" data-stage="completion">
            <div class="stage-icon">👑</div>
            <div class="stage-label">5. השלמה</div>
        </div>

        <!-- Simplified visual elements representing progress -->
        <div class="progress-path path-1-2"></div>
        <div class="progress-path path-2-3"></div>
        <div class="progress-path path-3-4"></div>
        <div class="progress-path path-4-5"></div>

         <div class="stage-visual stage-visual-1"></div>
         <div class="stage-visual stage-visual-2"></div>
         <div class="stage-visual stage-visual-3"></div>
         <div class="stage-visual stage-visual-4"></div>
         <div class="stage-visual stage-visual-5"></div>

    </div>
    <div id="info-display">
        <p class="info-placeholder">לחצו על שלב 1 כדי להתחיל את המסע...</p>
        <div id="stage-content">
            <!-- Content will be loaded here -->
        </div>
    </div>
</div>

<button id="toggle-explanation">הצג הסבר מורחב</button>

<div id="full-explanation">
    <h2>הסבר מורחב: מאחורי הקלעים של בניית העיר האסורה</h2>

    <h3>מי הזמין את הפרויקט ומדוע דווקא בבייג'ינג?</h3>
    <p>בניית העיר האסורה הוזמנה על ידי קיסר יונגלה, הקיסר השלישי בשושלת מינג, בתחילת המאה ה-15. לאחר שתפס את השלטון, הוא החליט להעביר את הבירה הדרומית נאנג'ינג צפונה לבייג'ינג (שנקראה אז בייפינג). המהלך נועד לחזק את שליטתו באזור הצפון, שהיה קרוב לגבול עם המונגולים ולמקור כוחו שלו לפני עלייתו לשלטון. העיר האסורה נועדה לשמש כמרכז שלטון מפואר שיבטא את עוצמתה של השושלת החדשה ואת הלגיטימיות של הקיסר.</p>

    <h3>היקף הפרויקט: גודל, עלות, ומספר העובדים</h3>
    <p>זה היה פרויקט בנייה בקנה מידה עצום. העיר האסורה משתרעת על שטח של כ-720,000 מ"ר וכוללת כ-980 מבנים עם אלפי חדרים. הבנייה החלה בשנת 1406 והושלמה בשנת 1420, כלומר ארכה 14 שנים בלבד. הפרויקט דרש גיוס משאבים אדירים: על פי ההערכות, השתתפו בו עד 100,000 אומנים מומחים ולמעלה ממיליון פועלים, חיילים ואיכרים שגויסו לעבודות כפייה. עלות הפרויקט הייתה אסטרונומית וצרכה חלק ניכר ממשאבי האימפריה.</p>

    <h3>אתגרים לוגיסטיים מרכזיים</h3>

    <h4>מקורות חומרי הגלם העיקריים והובלתם:</h4>
    <p>החומרים העיקריים לבנייה היו עץ ואבן. העץ האיכותי ביותר, מסוג נאנמו (עץ קשה ועמיד), הובא מיערות מרוחקים בדרום-מערב סין (פרובינציות כמו סצ'ואן ויונאן) – מסע של אלפי קילומטרים. הובלה זו התבצעה בעיקר באמצעות נהרות ותעלות (התעלה הגדולה שיחקה תפקיד מרכזי). גזעים ענקיים נקשרו יחד לרפסודות והושטו במורד הזרם, מסע שיכול היה להימשך מספר שנים עבור גזע בודד.</p>
    <p>אבני השיש הגדולות והכבדות ביותר, במיוחד אלו ששימשו לבסיסי העמודים ולעיטורים המגולפים, הובאו ממחצבות מרוחקות יחסית ממערב לבייג'ינג (כמו אזור פאנגשאן). הובלת גושי אבן במשקל עשרות ואף מאות טונות היוותה אתגר עצום. הפתרון הגאוני היה לנצל את חודשי החורף הקפואים: נתיבי הובלה הוכנו מראש על ידי חפירת בארות והשקיית הדרך במים, שיצרו משטחי קרח. על גבי משטחי הקרח הללו, הוזזו גושי האבן באמצעות מזחלות עץ, נמשכות על ידי מאות ואלפי פועלים, לעיתים תוך שימוש בעגלות רתומות לשוורים. הובלת גוש אבן גדול בודד יכלה לארוך חודשים.</p>

    <h3>תהליך הבנייה המרכזי</h3>
    <p>לאחר בחירת האתר והכנתו (יישור השטח, ניקוז), נבנו היסודות. בסיס המבנים הראשיים נבנה לרוב מאדמה מהודקת ואבן. סביב האתר הוקמו חומות הגנה כפולות ורחבות ותעלת מים, שנועדו לבודד ולהגן על המקום. גוף המבנים המרכזיים נבנה מעץ, תוך שימוש בטכניקות נגרות מורכבות של חיבורים ללא מסמרים, מה שאפשר למבנים לעמוד טוב יותר ברעידות אדמה. הגגות כוסו ברעפים מזוגגים צהובים, צבע שמור לקיסר. התכנון האדריכלי דבק בעקרונות הפנג שואי והסדר הקוסמולוגי הסיני, עם דגש על סימטריה צירית ושערים המובילים דרך סדרת חצרות רחבות ומרשימות אל האולמות הראשיים.</p>

    <h3>המשמעות הסימבולית והפוליטית של מבנה העיר האסורה</h3>
    <p>העיר האסורה לא הייתה רק ארמון, אלא סמל רב עוצמה. שמה (זיג'ין צ'נג - העיר הסגולה האסורה) קשור לפולסטאר (כוכב הצפון), שסביבו סובבים שאר הכוכבים, ומסמל את הקיסר כמרכז העולם. הגישה למקום הייתה מוגבלת ביותר (ומכאן "האסורה"), מה שהדגיש את מעמדו הנשגב והמבודד של הקיסר ("בן השמיים"). הפריסה והאדריכלות שיקפו את ההיררכיה החברתית והפוליטית של האימפריה, כאשר המבנים החשובים ביותר ממוקמים במרכז ובחלק הצפוני (החשוב יותר על פי הפנג שואי).</p>

    <h3>מורשת: השפעת העיר האסורה כמרכז שלטון ותרבות</h3>
    <p>במשך כמעט 500 שנה, העיר האסורה שימשה כמרכז השלטון הקיסרי של שושלות מינג וצ'ינג. היא הייתה הלב הפועם של האימפריה, מקום קבלת ההחלטות, ניהול הטקסים, ומקום מגוריהם של הקיסר, פמלייתו, סריסיו, ומשפחתו. היא צברה אוספים אדירים של אמנות, ספרות וחפצי ערך. כיום, העיר האסורה היא מוזיאון הארמון, אתר מורשת עולמית של אונסק"ו, ואחד מאתרי התיירות החשובים ביותר בסין. היא עדות מרשימה ליכולות הארגוניות וההנדסיות של סין הקיסרית ולתרבות העשירה שלה.</p>
</div>

<style>
    /* General App Styling */
    #forbidden-city-app {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        direction: rtl;
        text-align: right;
        max-width: 800px;
        margin: 20px auto;
        border: 1px solid #e0e0e0;
        padding: 20px;
        background-color: #fcfcfc;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        overflow: hidden; /* Prevents shadow issues with absolute positioning */
    }

    .app-title {
        text-align: center;
        color: #4a2f11; /* Dark Wood/Earth tone */
        margin-top: 0;
        margin-bottom: 30px;
        font-size: 1.8em;
        font-weight: bold;
    }

    /* Construction Map Styling */
    #construction-map {
        position: relative;
        width: 100%;
        height: 350px; /* Increased height for more visual space */
        background: linear-gradient(to bottom, #c8d9e2, #e2eaf1); /* Simple sky-like gradient */
        border: 1px solid #b0c4de;
        margin-bottom: 20px;
        border-radius: 8px;
        overflow: hidden; /* Hide elements outside map */
        box-shadow: inset 0 0 8px rgba(0,0,0,0.1);
    }

     .map-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(255, 255, 255, 0.3); /* Subtle white overlay */
        z-index: 1; /* Below points */
    }


    /* Construction Stage Points */
    .construction-stage {
        position: absolute;
        width: 100px; /* Increased size */
        height: 60px; /* Increased size */
        background-color: rgba(252, 209, 22, 0.9); /* Imperial Yellow with opacity */
        color: #4a2f11; /* Dark text */
        border: 2px solid #d4a90d; /* Darker yellow border */
        border-radius: 8px;
        text-align: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        font-size: 0.9em;
        font-weight: bold;
        transition: transform 0.3s ease, background-color 0.3s ease, opacity 0.3s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        z-index: 10; /* Above map elements */
    }

    .construction-stage:hover:not(.disabled) {
        background-color: #d4a90d; /* Darker yellow on hover */
        transform: scale(1.08);
    }

    .construction-stage.disabled {
        opacity: 0.6;
        cursor: not-allowed;
        background-color: rgba(200, 200, 200, 0.8);
        border-color: #aaa;
        color: #666;
        box-shadow: none;
    }

    .construction-stage.active {
         background-color: rgba(30, 144, 255, 0.9); /* Dodger Blue for active */
         border-color: #1a7cdb;
         color: white;
         box-shadow: 0 3px 8px rgba(0, 123, 255, 0.4);
    }

     .construction-stage.completed {
         background-color: rgba(60, 179, 113, 0.9); /* Medium Sea Green for completed */
         border-color: #3cb371;
         color: white;
     }

    .stage-icon {
        font-size: 1.5em;
        margin-bottom: 3px;
    }

    /* Positioning points (updated for better flow representation) */
    .stage-1 { top: 70%; left: 5%; }
    .stage-2 { top: 40%; left: 20%; }
    .stage-3 { top: 50%; left: 50%; }
    .stage-4 { top: 20%; left: 70%; }
    .stage-5 { top: 60%; left: 85%; }


    /* Simplified Visual Elements (Placeholders for animation) */
    .stage-visual {
        position: absolute;
        background-color: rgba(255, 255, 255, 0.8); /* Base color */
        border: 1px solid #ccc;
        border-radius: 4px;
        opacity: 0; /* Initially hidden */
        transition: opacity 1s ease-in-out;
        z-index: 5; /* Below points */
    }

    .stage-visual-1 { /* Wood Arrival */
        width: 80px; height: 30px;
        top: 75%; left: 18%;
        background-color: #8b4513; /* SaddleBrown */
    }
     .stage-visual-2 { /* Stone Transport */
        width: 50px; height: 50px;
        top: 45%; left: 30%;
        background-color: #d3d3d3; /* LightGrey */
        border-radius: 50%;
    }
     .stage-visual-3 { /* Walls */
        width: 200px; height: 80px;
        top: 60%; left: calc(50% - 100px);
        background-color: #a9a9a9; /* DarkGrey */
    }
     .stage-visual-4 { /* Buildings */
        width: 150px; height: 100px;
        top: 25%; left: calc(70% - 75px);
        background-color: #fcd116; /* Imperial Yellow */
        border: 2px solid #ee1c25; /* Red */
    }
     .stage-visual-5 { /* Completed Symbol */
        width: 70px; height: 70px;
        top: 65%; left: calc(85% - 35px);
        background-color: #ee1c25; /* Red */
        border-radius: 50%;
        box-shadow: 0 0 10px #ee1c25;
     }


    /* Path Elements (Simple lines showing connection) */
    .progress-path {
        position: absolute;
        background-color: #ccc;
        height: 3px;
        opacity: 0; /* Initially hidden */
        transition: opacity 0.5s ease-in-out, background-color 0.5s ease;
        z-index: 2; /* Below visuals */
    }

    /* These need specific positioning and width/height to connect the points */
    .path-1-2 { top: 68%; left: 15%; width: 12%; transform: rotate(-30deg); transform-origin: left center; }
    .path-2-3 { top: 48%; left: 30%; width: 22%; transform: rotate(20deg); transform-origin: left center; }
    .path-3-4 { top: 42%; left: 58%; width: 15%; transform: rotate(-35deg); transform-origin: left center; }
    .path-4-5 { top: 40%; left: 78%; width: 10%; transform: rotate(30deg); transform-origin: left center; }

    .progress-path.active {
        background-color: #007bff; /* Blue when active */
        opacity: 1;
    }


    /* Info Display Styling */
    #info-display {
        border: 1px solid #e0e0e0;
        padding: 20px;
        background-color: #fff;
        min-height: 180px; /* Ensure sufficient space */
        border-radius: 8px;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
        transition: opacity 0.5s ease, transform 0.5s ease;
    }

    .info-placeholder {
        text-align: center;
        color: #888;
        font-style: italic;
        margin-top: 40px;
        font-size: 1.1em;
    }

    #stage-content {
        opacity: 0; /* Initial state for fade-in */
        transition: opacity 0.5s ease-in-out;
    }

    #stage-content h4 {
        margin-top: 0;
        color: #0056b3;
        border-bottom: 1px dashed #e0e0e0;
        padding-bottom: 8px;
        margin-bottom: 12px;
        font-size: 1.3em;
    }

     #stage-content p {
         line-height: 1.7;
         margin-bottom: 10px;
         color: #555;
     }

    #stage-content img {
        max-width: 100%;
        height: auto;
        display: block;
        margin: 15px auto 0 auto; /* Center image */
        border-radius: 5px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    /* Toggle Button Styling */
    #toggle-explanation {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: #ee1c25; /* Imperial Red */
        color: white;
        transition: background-color 0.3s ease, transform 0.2s ease;
        box-shadow: 0 3px 8px rgba(238, 28, 37, 0.4);
        font-weight: bold;
    }

    #toggle-explanation:hover {
        background-color: #c0151d; /* Darker Red */
        transform: translateY(-2px);
    }

    /* Full Explanation Styling */
    #full-explanation {
        display: none;
        margin-top: 20px;
        padding: 20px;
        border: 1px solid #e0e0e0;
        background-color: #f9f9f9;
        border-radius: 12px;
        direction: rtl;
        text-align: right;
        line-height: 1.6;
        color: #333;
    }

    #full-explanation h2 {
        color: #4a2f11;
        border-bottom: 2px solid #fcd116;
        padding-bottom: 10px;
        margin-top: 0;
        margin-bottom: 20px;
        font-size: 1.6em;
    }

    #full-explanation h3 {
        color: #ee1c25;
        border-bottom: 1px solid #fcd116;
        padding-bottom: 8px;
        margin-top: 25px;
        margin-bottom: 15px;
        font-size: 1.3em;
    }

    #full-explanation p {
        margin-bottom: 15px;
        text-align: justify; /* Justify text for a cleaner look */
    }
</style>

<script>
    const stagesData = {
        wood: {
            title: "1. הבאת עצי ענק מהדרום: מסע ארוך ורטוב",
            text: "האתגר: עצים איכותיים מסוג נאנמו, חיוניים למבנה הארמונות, גדלו ביערות רחוקים בדרום-מערב סין, מסע של אלפי קילומטרים! גזעים ענקיים שמשקלם טונות דרשו פתרון הובלה יצירתי.<br><br>הפתרון: רשת הנהרות והתעלות העצומה של סין הפכה לכביש המהיר. גזעים ענקיים נקשרו יחד לרפסודות והושטו במורד הנהרות במסע איטי ומפרך, לעיתים ארך שנים, עד שהגיעו ליעדם הצפוני בבייג'ינג.",
            image: 'https://via.placeholder.com/400x200?text=Wood+Raft+Transport+Simulation' // Suggests a simulation/animation image
        },
        stone: {
            title: "2. הובלת אבני שיש כבדות: הקרח הגיע להצלה",
            text: "האתגר: גושי שיש עצומים מהמחצבות הסמוכות לבייג'ינג (פאנגשאן) היו כבדים מדי להזזה בשיטות רגילות, במיוחד לוחות הקישוט הגדולים ששקלו מאות טונות. איך מזיזים הר קטן?<br><br>הפתרון: גאונות חורפית! נתיבי הובלה מיוחדים הוכנו בחורף על ידי חפירת בארות והשקיית הדרך במים, שיצרו שכבת קרח חלקה. על משטחי הקרח, גושי האבן הוזזו על גבי מזחלות עץ פשוטות, נמשכות על ידי אלפי פועלים וכוח שוורים, בזכות החיכוך המופחת של הקרח.",
            image: 'https://via.placeholder.com/400x200?text=Stone+Moving+on+Ice+Simulation' // Suggests a simulation/animation image
        },
        walls: {
            title: "3. הקמת חומות מגן ויסודות: הבסיס האיתן",
            text: "האתגר: יצירת מתחם מוגן ומבודד לקיסר ובניית בסיס חזק ויציב לאלפי מבנים על שטח עצום שכלל גם אזורים ביצתיים.<br><br>הפתרון: נבנו חומות הגנה כפולות, גבוהות ועבות במיוחד (למעלה מ-10 מטר גובה ולפחות 6 מטר רוחב בבסיס) ותעלת מים רחבה סביב כל המתחם כדי להדגיש את הבידוד הקיסרי. היסודות למבנים נבנו מאדמה מהודקת היטב ושכבות אבן כדי להבטיח יציבות מקסימלית לאורך מאות שנים.",
            image: 'https://via.placeholder.com/400x200?text=Wall+Construction+Simulation' // Suggests a simulation/animation image
        },
        buildings: {
            title: "4. בניית ארמונות ואולמות: יצירת הפאר הקיסרי",
            text: "האתגר: בנייה מהירה ויעילה של כמעט 1000 מבנים מורכבים ורחבי ידיים, שיתאימו למעמד הקיסרי, תוך שימוש בטכנולוגיות הבנייה המסורתיות של התקופה.<br><br>הפתרון: שימוש בטכניקות נגרות סיניות מתוחכמות (כמו מערכת סוגרי ה-'דובואו') שאפשרו חיבור חלקי עץ ללא מסמרים, הקנו למבנים גמישות ועמידות בפני רעידות אדמה. שלדי העץ העצומים הוקמו על בסיסי האבן, והגגות כוסו ברעפים מזוגגים בצבע צהוב בוהק, צבע שמור באופן בלעדי לקיסר.",
            image: 'https://via.placeholder.com/400x200?text=Palace+Building+Simulation' // Suggests a simulation/animation image
        },
        completion: {
            title: "5. השלמה וגימור: הפיכת חלום למציאות",
            text: "האתגר: סיום כלל פרטי הבנייה, הוספת עיטורים אדריכליים ופסלים, גינון, ריהוט, והכנה למגורי הקיסר וחצרו – הפיכת אתר בנייה לעיר קיסרית מפוארת ומתפקדת.<br><br>הפתרון: מאות אלפי אומנים ופועלים פעלו במקביל על הפרטים האחרונים – גילוף דרקונים על קורות העץ, הוספת אריות שיש בשערים, ציור קורות הגג בצבעים עזים, יצירת גנים סיניים מסורתיים. בתוך 14 שנים בלבד, קם מתחם הארמון הגדול בעולם, מוכן לקבל את 'בן השמיים'.",
            image: 'https://via.placeholder.com/400x200?text=Forbidden+City+Completed+Simulation' // Suggests a simulation/animation image
        }
    };

    const stagesOrder = ['wood', 'stone', 'walls', 'buildings', 'completion'];
    let currentStageIndex = 0;

    const stageElements = document.querySelectorAll('.construction-stage');
    const stageContentDiv = document.getElementById('stage-content');
    const infoDisplay = document.getElementById('info-display');
    const infoPlaceholder = document.querySelector('.info-placeholder');
    const toggleButton = document.getElementById('toggle-explanation');
    const fullExplanationDiv = document.getElementById('full-explanation');
    const visualElements = document.querySelectorAll('.stage-visual');
    const pathElements = document.querySelectorAll('.progress-path');


    function showStageInfo(stageKey) {
        const stageInfo = stagesData[stageKey];
        stageContentDiv.style.opacity = 0; // Start fade out
        setTimeout(() => {
            infoPlaceholder.style.display = 'none';
            stageContentDiv.innerHTML = `
                <h4>${stageInfo.title}</h4>
                <p>${stageInfo.text}</p>
                ${stageInfo.image ? `<img src="${stageInfo.image}" alt="${stageInfo.title}">` : ''}
            `;
            stageContentDiv.style.opacity = 1; // Fade in
        }, 200); // Match CSS transition duration
    }

    function activateStage(stageKey) {
        const stageElement = document.querySelector(`.construction-stage[data-stage="${stageKey}"]`);
        if (!stageElement || stageElement.classList.contains('disabled')) {
            return; // Do nothing if disabled or not found
        }

        // Check if it's the next expected stage
        const expectedStageKey = stagesOrder[currentStageIndex];
         if (stageKey !== expectedStageKey) {
             // Optional: Add feedback for clicking out of order
             console.log(`Please click stages in order. Next stage is ${expectedStageKey}`);
             // alert(`אנא לחצו על השלבים לפי הסדר. השלב הבא הוא ${stagesData[expectedStageKey].title.split('.')[0]}.`); // User-friendly alert
             // Add a temporary visual shake or pulse to the expected stage?
             const expectedElement = document.querySelector(`.construction-stage[data-stage="${expectedStageKey}"]`);
             if (expectedElement) {
                 expectedElement.style.animation = 'pulse 0.5s 3'; // Simple pulse animation
                 expectedElement.addEventListener('animationend', () => {
                      expectedElement.style.animation = '';
                 }, { once: true });
             }
             return;
         }


        // Deactivate previous stage visual/path
         if (currentStageIndex > 0) {
             const prevStageKey = stagesOrder[currentStageIndex - 1];
             const prevStageElement = document.querySelector(`.construction-stage[data-stage="${prevStageKey}"]`);
              const prevVisual = document.querySelector(`.stage-visual-${currentStageIndex}`); // Index is 1-based for visuals
              const prevPath = document.querySelector(`.path-${currentStageIndex -1}-${currentStageIndex}`); // Path index is start-end
             if(prevStageElement) prevStageElement.classList.remove('active');
             if(prevVisual) prevVisual.style.opacity = 0;
             if(prevPath) prevPath.classList.remove('active');
         }


        // Activate current stage
        stageElement.classList.remove('disabled'); // Should already be enabled by now, but just in case
        stageElement.classList.add('active');
        stageElement.classList.add('completed'); // Mark as completed for future stages

        // Show current stage visual
         const currentVisual = document.querySelector(`.stage-visual-${currentStageIndex + 1}`); // Visuals are 1-based index
         if(currentVisual) currentVisual.style.opacity = 1;

        // Show path to next stage
         if (currentStageIndex < stagesOrder.length - 1) {
              const nextPath = document.querySelector(`.path-${currentStageIndex + 1}-${currentStageIndex + 2}`);
              if(nextPath) nextPath.classList.add('active');
         }


        showStageInfo(stageKey);

        // Enable the next stage point
        currentStageIndex++;
        if (currentStageIndex < stagesOrder.length) {
            const nextStageKey = stagesOrder[currentStageIndex];
            const nextStageElement = document.querySelector(`.construction-stage[data-stage="${nextStageKey}"]`);
            if (nextStageElement) {
                nextStageElement.classList.remove('disabled');
            }
        } else {
            // All stages completed
            console.log("Construction Complete!");
            // Optional: Add a completion message or animation
        }
    }


    // Add event listeners to all stage points
    stageElements.forEach(point => {
        point.addEventListener('click', () => {
            const stageKey = point.getAttribute('data-stage');
            activateStage(stageKey);
        });
    });

    // Toggle full explanation
    toggleButton.addEventListener('click', () => {
        const isHidden = fullExplanationDiv.style.display === 'none' || fullExplanationDiv.style.display === '';
        if (isHidden) {
            fullExplanationDiv.style.display = 'block';
            toggleButton.textContent = 'הסתר הסבר מורחב';
        } else {
            fullExplanationDiv.style.display = 'none';
            toggleButton.textContent = 'הצג הסבר מורחב';
        }
    });

    // Initial state: Only the first point is enabled
    stageElements.forEach((el, index) => {
        if (index > 0) {
            el.classList.add('disabled');
        }
    });

     // Add pulse animation for attention on the first step
     const firstStage = document.querySelector('.construction-stage.stage-1');
      if(firstStage) {
         firstStage.style.animation = 'pulse 1.5s infinite';
         firstStage.addEventListener('click', () => {
             firstStage.style.animation = ''; // Stop animation on click
         }, { once: true }); // Remove listener after first click
      }

    // CSS Keyframes for pulse animation
     const styleSheet = document.styleSheets[0];
     styleSheet.insertRule(`
         @keyframes pulse {
             0% { transform: scale(1); }
             50% { transform: scale(1.05); }
             100% { transform: scale(1); }
         }
     `, styleSheet.cssRules.length);

    // Initial message is handled by the placeholder div
    // infoContentDiv.innerHTML = "<p class='info-placeholder'>לחצו על שלב 1 כדי להתחיל את המסע...</p>"; // Replaced by dedicated div

</script>
```