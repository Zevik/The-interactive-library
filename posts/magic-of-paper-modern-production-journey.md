---
title: "קסם הנייר: מסע הייצור המודרני"
english_slug: magic-of-paper-modern-production-journey
category: "הנדסת חומרים"
tags: [ייצור נייר, הנדסה כימית, חומרים, תהליכים תעשייתיים, הלבנה]
---
<h1>קסם הנייר: מסע הייצור המודרני</h1>
<p class="intro-text">דמיינו: גזע עץ אדיר הופך לדף לבן וחלק שעליו נכתבת היסטוריה. איך קורה הקסם הזה? צללו איתנו למסע המרתק דרך התהליכים התעשייתיים שהופכים סיבי עץ פשוטים לחומר הכי נפוץ בחיינו!</p>

<div id="paper-app">
    <div class="app-header">
        <h2>שלב בתהליך</h2>
        <div id="stage-name"></div>
    </div>
    <div id="stage-visual">
        <!-- Visual elements will be manipulated by JS/CSS -->
        <div class="visual-element raw-materials"></div>
        <div class="visual-element chipping"></div>
        <div class="visual-element pulping-cooker"></div>
        <div class="visual-element pulp-stream"></div>
        <div class="visual-element washing-filter"></div>
        <div class="visual-element bleaching-vat"></div>
        <div class="visual-element additives-mix"></div>
        <div class="visual-element forming-wire"></div>
        <div class="visual-element press-dryer"></div>
        <div class="visual-element calender"></div>
        <div class="visual-element finished-roll"></div>
         <div class="visual-overlay-text"></div> <!-- To display dynamic text/icons -->
    </div>
    <div id="stage-explanation" class="stage-text-explanation"></div>
    <div class="controls">
        <button id="next-stage">התחנה הבאה במסע!</button>
    </div>
</div>

<button id="toggle-explanation">רוצים לדעת יותר? הסבר מפורט</button>

<div id="detailed-explanation" style="display: none;">
    <h2>הסבר מפורט על תהליך ייצור הנייר</h2>
    <p><strong>מהו נייר?</strong> נייר מורכב בעיקר מסיבי תאית (צלולוז) המחוברים זה לזה ברשת. סיבים אלו מגיעים לרוב מעץ, אך גם מנייר ממוחזר או ממקורות צמחיים אחרים.</p>
    <p><strong>חומרי גלם עיקריים:</strong> עץ הוא המקור העיקרי בתעשייה המודרנית. סוגי עץ שונים (רכים וקשים) משמשים לתכונות נייר שונות. נייר ממוחזר הופך חשוב יותר ויותר. מים וכימיקלים חיוניים לכל שלבי התהליך התעשייתי.</p>
    <p><strong>תהליך הדיפון (Pulping) - הפרדת הסיבים:</strong> כאן הופכים את העץ או הנייר הממוחזר לעיסת סיבים. השיטות העיקריות הן:
        <ul>
            <li><strong>מכנית:</strong> ריסוק העץ (פילוס) לסיבים. משאיר הרבה ליגנין (החומר החום שקושר את הסיבים). משמש לנייר זול (כמו עיתון).</li>
            <li><strong>כימית:</strong> בישול שבבי העץ עם כימיקלים חזקים (כמו גופרית). הכימיקלים ממיסים את הליגנין ומפרידים את סיבי התאית ביעילות. זו השיטה העיקרית לנייר איכותי.</li>
        </ul>
    </p>
    <p><strong>הליגנין:</strong> פולימר טבעי הקושר סיבים ומקנה קשיחות לעץ. אחראי גם לצבע החום. בתהליך הנייר, מסירים חלק או את כולו לקבלת לובן ולמניעת התצהבות.</p>
    <p><strong>שלב ההלבנה (Bleaching):</strong> המטרה היא להסיר שאריות ליגנין וחומרים צבעוניים כדי להגביר את לובן הנייר. משתמשים בכימיקלים כמו מי חמצן או דו-תחמוצת כלור. שיטות מודרניות (ECF/TCF) מפחיתות שימוש בכלור לשמירה על הסביבה.</p>
    <p><strong>דיפון (Sizing):</strong> כדי שהדיו לא ימרח על הנייר (כמו שקורה במפית), מוסיפים חומרים המקטינים את ספיגות המים והדיו. חומרים נפוצים: עמילן, AKD, ASA.</p>
    <p><strong>חומרי מילוי (Fillers):</strong> מינרלים דקים (קאולין, קלציום קרבונט) מוספים לעיסה. משפרים חלקות, אטימות (שלא יראו את הצד השני), לובן, ומורידים עלויות. יותר מדי מילוי יכול להחליש את הנייר.</p>
    <p><strong>יצירת היריעה (Forming):</strong> עיסת סיבים מהולה מאוד במים (כ-99%) מוזרמת על מסך רשת נע. המים מתנקזים, והסיבים נערמים ליצירת יריעה רטובה.</p>
    <p><strong>סחיטה, ייבוש וגימור:</strong> יריעת הנייר הרטובה עוברת דרך גלילים סוחטים להסרת מים, ואז דרך גלילים מחוממים לייבוש סופי. לבסוף, היא עוברת תהליכי גימור כמו ציפוי (לשיפור פני שטח) וקלנדר (מעבר בגלילים חלקים להשגת חלקות) לפני חיתוך וגלילה לגלילים ענקיים.</p>
    <p><strong>קיימות:</strong> התעשייה משפרת את הקיימות ע"י שימוש יעיל במים (מיחזור), הפחתת אנרגיה (מקורות מתחדשים), מזעור כימיקלים מזיקים (הלבנה ללא כלור) והגברת שימוש בנייר ממוחזר.</p>
</div>

<style>
    /* כללי */
    body {
        font-family: 'Arial', sans-serif; /* פונט מודרני יותר */
        line-height: 1.7; /* רווח שורות משופר */
        direction: rtl;
        text-align: right;
        padding: 20px;
        background-color: #f0f4f8; /* רקע רך יותר */
        color: #333;
        margin: 0; /* איפוס שוליים */
    }

    h1, h2 {
        color: #1a3a5f; /* כחול כהה מודרני */
        text-align: center;
        margin-bottom: 15px;
    }

    .intro-text {
        text-align: center;
        max-width: 700px;
        margin: 10px auto 30px auto;
        font-size: 1.15em;
        color: #555;
    }

    /* אפליקציית הנייר */
    #paper-app {
        border: none; /* נסיר גבול פשוט */
        padding: 30px; /* מרווח פנימי גדול יותר */
        margin: 20px auto;
        max-width: 850px; /* רוחב מעט גדול יותר */
        background: linear-gradient(to bottom, #ffffff, #f8f8f8); /* רקע הדרגתי עדין */
        border-radius: 12px; /* פינות מעוגלות יותר */
        box-shadow: 0 8px 15px rgba(0,0,0,0.1); /* צל עמוק יותר */
        overflow: hidden; /* חשוב לאנימציות */
        position: relative;
    }

    .app-header {
         text-align: center;
         margin-bottom: 20px;
         padding-bottom: 15px;
         border-bottom: 1px solid #eee;
    }

    .app-header h2 {
        margin: 0 0 5px 0;
        color: #0056b3; /* צבע משני להדגשה */
        font-size: 1.2em;
    }

     #stage-name {
         font-size: 1.5em;
         font-weight: bold;
         color: #1a3a5f;
         min-height: 1.5em; /* כדי למנוע קפיצות בגובה */
     }

    #stage-visual {
        min-height: 300px; /* גובה גדול יותר לויזואליה */
        background-color: #eef2f7; /* רקע ויזואלי בהיר */
        border: 1px solid #dcdcdc; /* גבול עדין */
        border-radius: 8px;
        display: flex; /* שימוש בפלקסבוקס למיקום */
        align-items: center;
        justify-content: center;
        position: relative; /* לאפשר מיקום אבסולוטי של ילדים */
        overflow: hidden; /* קליפינג של אלמנטים יוצאים */
        margin-bottom: 20px;
         transition: background-color 0.8s ease; /* אנימציית רקע */
    }

    /* אלמנטים ויזואליים בתוך stage-visual - סגנון בסיסי */
    .visual-element {
        position: absolute; /* מיקום חופשי בתוך הפלקס */
        transition: all 0.8s ease-in-out, opacity 0.6s ease; /* אנימציה חלקה */
        opacity: 0; /* מוסתר כברירת מחדל */
        transform: scale(0.8); /* מתחיל קטן יותר */
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
    }

     .visual-overlay-text {
         position: absolute;
         top: 50%;
         left: 50%;
         transform: translate(-50%, -50%);
         font-size: 1.8em;
         font-weight: bold;
         color: rgba(0,0,0,0.6);
         text-align: center;
         opacity: 0;
         transition: opacity 0.5s ease;
         pointer-events: none; /* לא מפריע לקליקים */
     }


    /* סגנונות ספציפיים לכל שלב ויזואלי */
    .stage-active .visual-element {
        opacity: 0; /* הסתר הכל כששלב חדש מתחיל */
        transform: scale(0.8);
    }

    .stage-active .visual-overlay-text {
         opacity: 0;
    }


    /* שלב 1: חומרי גלם */
    #stage-visual.stage-raw { background-color: #f0f4f8; }
    #stage-visual.stage-raw .visual-element.raw-materials {
        opacity: 1;
        transform: scale(1);
        width: 80%; height: 80%;
        background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="20" cy="80" r="15" fill="%238B4513"/><circle cx="50" cy="75" r="18" fill="%23A0522D"/><circle cx="80" cy="85" r="12" fill="%23CD853F"/><path d="M50 50 Q60 30 70 50 T90 50 Q80 70 70 70 T50 70 Q40 70 30 70 T10 70 Q20 70 30 50 T50 50 Z" fill="%234682B4"/><path d="M80 20 Q85 15 90 20 S95 25 90 30 Q85 35 80 30 S75 25 80 20 Z" fill="%23808080"/></svg>'); /* עץ, מים, כימיקלים איקונים */
    }
    #stage-visual.stage-raw .visual-overlay-text { content: 'חומרי גלם נאספים'; opacity: 1; }


    /* שלב 2: ריסוק/הכנה */
    #stage-visual.stage-chipping { background-color: #e0e8f0; }
    #stage-visual.stage-chipping .visual-element.chipping {
        opacity: 1;
        transform: scale(1);
        width: 60%; height: 60%;
         background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><path d="M10 80 H90 V90 H10 Z" fill="%23ccc"/><path d="M20 80 L30 20 L70 20 L80 80 Z" fill="%238B4513"/><path d="M45 25 L50 15 L55 25 L50 35 Z" fill="%23555"/><rect x="48" y="20" width="4" height="50" fill="%23555"/><circle cx="50" cy="80" r="5" fill="%23555"/><text x="50" y="55" font-size="12" fill="white" text-anchor="middle">קילוף וריסוק</text></svg>'); /* מגרסה */
    }

    /* שלב 3: בישול כימי */
    #stage-visual.stage-pulping-cooker { background-color: #d3e0ec; }
    #stage-visual.stage-pulping-cooker .visual-element.pulping-cooker {
        opacity: 1;
        transform: scale(1);
        width: 70%; height: 70%;
        background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect x="20" y="20" width="60" height="60" rx="10" fill="%23b0c4de"/><rect x="25" y="25" width="50" height="50" fill="%238B4513" opacity="0.7"/><path d="M40 30 Q50 20 60 30 Q50 40 40 30 Z" fill="%23eee"><animate attributeName="cy" from="30" to="40" dur="1s" begin="0s" repeatCount="indefinite"/></path><path d="M55 45 Q65 35 75 45 Q65 55 55 45 Z" fill="%23eee"><animate attributeName="cy" from="45" to="55" dur="1s" begin="0.5s" repeatCount="indefinite"/></path><text x="50" y="50" font-size="12" fill="white" text-anchor="middle">בישול עם כימיקלים</text></svg>'); /* סיר בישול עם בועות */
    }


    /* שלב 4: הפרדת סיבים / שטיפה */
     #stage-visual.stage-pulp-stream { background-color: #c0d6e4; }
     #stage-visual.stage-pulp-stream .visual-element.pulp-stream {
         opacity: 1;
         transform: scale(1);
         width: 80%; height: 80%;
         background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect x="10" y="10" width="80" height="80" fill="%23d4c2b3" opacity="0.8"/><path d="M20 50 Q40 30 50 50 T80 50" stroke="%23fff" stroke-width="2" fill="none"><animate attributeName="d" values="M20 50 Q40 30 50 50 T80 50; M20 55 Q40 35 50 55 T80 55; M20 50 Q40 30 50 50 T80 50" dur="2s" repeatCount="indefinite"/></path><path d="M30 60 Q50 40 60 60 T90 60" stroke="%23fff" stroke-width="2" fill="none"><animate attributeName="d" values="M30 60 Q50 40 60 60 T90 60; M30 65 Q50 45 60 65 T90 65; M30 60 Q50 40 60 60 T90 60" dur="2s" begin="0.5s" repeatCount="indefinite"/></path><text x="50" y="50" font-size="12" fill="#333" text-anchor="middle">עיסה מסתחררת</text></svg>'); /* נוזל מסתחרר */
     }

    /* שלב 5: שטיפה וסינון */
    #stage-visual.stage-washing-filter { background-color: #b0c4de; }
    #stage-visual.stage-washing-filter .visual-element.washing-filter {
        opacity: 1;
        transform: scale(1);
        width: 80%; height: 80%;
        background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect x="10" y="10" width="80" height="80" fill="%23d4c2b3" opacity="0.8"/><path d="M10 70 L90 70" stroke="%23555" stroke-width="2"/><circle cx="30" cy="65" r="3" fill="%238B4513"><animate attributeName="cy" from="65" to="85" dur="1.5s" repeatCount="indefinite"/></circle><circle cx="50" cy="60" r="3" fill="%238B4513"><animate attributeName="cy" from="60" to="80" dur="1.5s" begin="0.3s" repeatCount="indefinite"/></circle><circle cx="70" cy="55" r="3" fill="%238B4513"><animate attributeName="cy" from="55" to="75" dur="1.5s" begin="0.6s" repeatCount="indefinite"/></circle><text x="50" y="40" font-size="12" fill="#333" text-anchor="middle">שטיפה וסינון</text></svg>'); /* פילטר וחלקיקים נופלים */
    }


    /* שלב 6: הלבנה */
    #stage-visual.stage-bleaching-vat { background-color: #eef2f7; }
    #stage-visual.stage-bleaching-vat .visual-element.bleaching-vat {
        opacity: 1;
        transform: scale(1);
        width: 70%; height: 70%;
        background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect x="20" y="20" width="60" height="60" rx="10" fill="%23b0c4de"/><rect id="pulp" x="25" y="25" width="50" height="50" fill="%23d4c2b3"><animate attributeName="fill" values="%23d4c2b3;%23ffffff" dur="2s" fill="freeze"/></rect><text x="50" y="50" font-size="12" fill="#333" text-anchor="middle">הלבנה!</text></svg>'); /* עיסה מחליפה צבע ללבן */
    }

    /* שלב 7: דיפון */
     #stage-visual.stage-additives-mix { background-color: #f0f4f8; }
     #stage-visual.stage-additives-mix .visual-element.additives-mix {
         opacity: 1;
         transform: scale(1);
         width: 80%; height: 80%;
         background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect x="10" y="10" width="80" height="80" fill="%23ffffff" opacity="0.9"/><circle cx="30" cy="30" r="5" fill="%23add8e6"><animate attributeName="cy" from="10" to="50" dur="1s" repeatCount="indefinite"/></circle><circle cx="50" cy="20" r="5" fill="%2390ee90"><animate attributeName="cy" from="10" to="60" dur="1s" begin="0.3s" repeatCount="indefinite"/></circle><text x="50" y="50" font-size="12" fill="#333" text-anchor="middle">הוספת חומרי דיפון</text></svg>'); /* חלקיקים קטנים נופלים לעיסה הלבנה */
     }

    /* שלב 8: חומרי מילוי */
     #stage-visual.stage-fillers { background-color: #eef2f7; }
     #stage-visual.stage-fillers .visual-element.additives-mix { /* reuse additives-mix visual */
         opacity: 1;
         transform: scale(1);
         width: 80%; height: 80%;
         background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect x="10" y="10" width="80" height="80" fill="%23ffffff" opacity="0.9"/><rect x="40" y="10" width="20" height="20" fill="%23d3d3d3"><animate attributeName="y" from="10" to="50" dur="1.5s" repeatCount="indefinite"/></rect><circle cx="50" cy="50" r="5" fill="%23eee"><animate attributeName="cy" from="20" to="70" dur="1.5s" begin="0.5s" repeatCount="indefinite"/></circle><text x="50" y="50" font-size="12" fill="#333" text-anchor="middle">הוספת חומרי מילוי</text></svg>'); /* אבקה נופלת לעיסה הלבנה */
     }


    /* שלב 9: יצירת היריעה */
    #stage-visual.stage-forming-wire { background-color: #d0e4f6; } /* צבע מים */
    #stage-visual.stage-forming-wire .visual-element.forming-wire {
        opacity: 1;
        transform: scale(1);
        width: 90%; height: 90%;
        background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><path d="M10 80 L90 80 L90 85 L10 85 Z" fill="%23aaa"/> <!-- Wire mesh --> <rect x="15" y="20" width="70" height="55" fill="%23a0d7ff" opacity="0.8"/> <!-- Watery pulp --> <path d="M20 30 C30 40 40 40 50 30 C60 20 70 20 80 30" fill="none" stroke="%23fff" stroke-width="3"><animate attributeName="d" values="M20 30 C30 40 40 40 50 30 C60 20 70 20 80 30; M20 35 C30 45 40 45 50 35 C60 25 70 25 80 35" dur="1.5s" repeatCount="indefinite"/></path><path d="M30 40 C40 50 50 50 60 40 C70 30 80 30 90 40" fill="none" stroke="%23fff" stroke-width="3" begin="0.5s"><animate attributeName="d" values="M30 40 C40 50 50 50 60 40 C70 30 80 30 90 40; M30 45 C40 55 50 55 60 45 C70 35 80 35 90 45" dur="1.5s" repeatCount="indefinite"/></path><text x="50" y="50" font-size="12" fill="#1a3a5f" text-anchor="middle">נוצרת יריעה רטובה</text></svg>'); /* רשת עם נוזל נוטף */
    }

    /* שלב 10: סחיטה וייבוש */
    #stage-visual.stage-press-dryer { background-color: #f0f4f8; }
    #stage-visual.stage-press-dryer .visual-element.press-dryer {
        opacity: 1;
        transform: scale(1);
        width: 90%; height: 90%;
        background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect x="5" y="40" width="90" height="20" fill="%23eee"/> <!-- Paper sheet --> <circle cx="25" cy="50" r="10" fill="%23888"/> <circle cx="75" cy="50" r="10" fill="%23888"/> <!-- Press rollers --> <path d="M10 30 L90 30 L90 35 L10 35 Z" fill="%23ddd"/> <path d="M10 65 L90 65 L90 70 L10 70 Z" fill="%23ddd"/> <!-- Heated rollers --> <circle cx="40" cy="30" r="8" fill="%23f00" opacity="0.5"/><circle cx="60" cy="70" r="8" fill="%23f00" opacity="0.5"/> <path d="M45 25 Q50 20 55 25 M45 75 Q50 80 55 75" stroke="%23555" fill="none"><animate attributeName="d" values="M45 25 Q50 20 55 25 M45 75 Q50 80 55 75; M45 20 Q50 15 55 20 M45 80 Q50 85 55 80" dur="1s" repeatCount="indefinite"/></path><text x="50" y="50" font-size="12" fill="#333" text-anchor="middle">סחיטה וייבוש</text></svg>'); /* גלילים וקיטור */
    }

    /* שלב 11: גימור */
     #stage-visual.stage-calender { background-color: #eef2f7; }
     #stage-visual.stage-calender .visual-element.calender {
        opacity: 1;
        transform: scale(1);
        width: 90%; height: 90%;
         background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect x="5" y="45" width="90" height="10" fill="%23fff"/> <!-- Paper sheet --> <circle cx="50" cy="35" r="10" fill="%23aaa"/> <circle cx="50" cy="65" r="10" fill="%23aaa"/> <!-- Calender rollers --> <text x="50" y="50" font-size="12" fill="#333" text-anchor="middle">גימור והחלקה</text></svg>'); /* גלילי קלנדר */
     }


    /* שלב סופי */
    #stage-visual.stage-finished-roll { background-color: #dcdcdc; }
    #stage-visual.stage-finished-roll .visual-element.finished-roll {
        opacity: 1;
        transform: scale(1);
        width: 60%; height: 60%;
        background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="50" cy="50" r="30" fill="%23fff" stroke="%23ccc" stroke-width="5"/><circle cx="50" cy="50" r="25" fill="%23eee"/><text x="50" y="55" font-size="15" font-weight="bold" fill="#555" text-anchor="middle">מוכן!</text></svg>'); /* גליל נייר */
    }


    /* סגנון הסבר השלב הנוכחי */
    .stage-text-explanation {
        min-height: 60px; /* גובה מינימלי קבוע */
        margin-bottom: 15px;
        padding: 15px; /* מרווח פנימי */
        border: 1px solid #dcdcdc; /* גבול עדין */
        background-color: #eef2f7; /* רקע בהיר */
        border-radius: 8px;
        font-size: 1.1em;
        color: #555;
        text-align: center; /* הסבר במרכז */
        display: flex; /* פלקסבוקס ליישור אנכי */
        align-items: center;
        justify-content: center;
         transition: opacity 0.5s ease; /* אנימציית כניסה */
    }

    /* כפתורים */
    .controls {
        text-align: center;
        margin-top: 20px;
    }

    #next-stage, #toggle-explanation {
        padding: 12px 25px; /* מרווח פנימי גדול יותר */
        font-size: 1.1em; /* גודל פונט גדול יותר */
        cursor: pointer;
        border: none;
        border-radius: 25px; /* פינות מעוגלות מאוד */
        background-color: #007bff;
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease; /* אנימציית לחיצה */
        box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* צל לכפתור */
    }

    #next-stage:hover, #toggle-explanation:hover {
        background-color: #0056b3;
        box-shadow: 0 6px 10px rgba(0,0,0,0.15);
    }

     #next-stage:active, #toggle-explanation:active {
         transform: scale(0.98); /* אפקט לחיצה */
     }


    #next-stage:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        box-shadow: none;
        transform: scale(1);
    }

    #toggle-explanation {
        display: block;
        margin: 30px auto; /* מרווח גדול יותר מהאפליקציה */
        background-color: #6c757d; /* כפתור משני */
         box-shadow: 0 4px 8px rgba(0,0,0,0.08);
    }
     #toggle-explanation:hover {
        background-color: #5a6268;
         box-shadow: 0 6px 10px rgba(0,0,0,0.12);
     }


    /* הסבר מפורט */
    #detailed-explanation {
        border: none;
        padding: 30px;
        margin: 20px auto;
        max-width: 850px;
        background: linear-gradient(to bottom, #ffffff, #f8f8f8);
        border-radius: 12px;
        box-shadow: 0 8px 15px rgba(0,0,0,0.1);
        color: #555;
    }

    #detailed-explanation h2 {
        text-align: right;
        border-bottom: 1px solid #eee;
        padding-bottom: 10px;
        margin-top: 0;
         color: #0056b3;
    }

    #detailed-explanation p {
        margin-bottom: 15px;
    }

    #detailed-explanation strong {
        color: #333;
    }

    #detailed-explanation ul {
        list-style: disc inside;
        padding-right: 20px;
         margin-top: 10px;
    }
    #detailed-explanation li {
         margin-bottom: 8px;
         line-height: 1.5;
    }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const stageNameDiv = document.getElementById('stage-name');
        const stageExplanationDiv = document.getElementById('stage-explanation');
        const stageVisualDiv = document.getElementById('stage-visual');
        const nextStageButton = document.getElementById('next-stage');
        const detailedExplanationDiv = document.getElementById('detailed-explanation');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const visualOverlayText = stageVisualDiv.querySelector('.visual-overlay-text');

        // Mapping of stage index to corresponding visual element class
        const stageVisualMap = [
             'raw-materials',
             'chipping',
             'pulping-cooker',
             'pulp-stream', // Combined Separaing Fibers & Washing/Screening visual
             'washing-filter', // Still use this class for stage 5 text/bg
             'bleaching-vat',
             'additives-mix', // Sizing
             'additives-mix', // Fillers (reusing visual element class)
             'forming-wire',
             'press-dryer',
             'calender',
             'finished-roll'
        ];

        const stages = [
            {
                name: "1. חומרי גלם",
                text: "הכול מתחיל מהיסודות: בולי עץ, שבבים, כמויות אדירות של מים וכימיקלים חיוניים.",
                visualClass: "stage-raw",
                 overlayText: "עצים ומים",
            },
            {
                name: "2. הכנה וריסוק",
                text: "העץ נפרד מהקליפה, נשטף ונרסק לשבבים קטנים או לחתיכות, מוכן לתהליך העיבוד.",
                visualClass: "stage-chipping",
                overlayText: "עיבוד עץ",
            },
            {
                name: "3. בישול כימי (דיפון)",
                text: "שבבי העץ מתבשלים עם כימיקלים חזקים במכלים ענקיים כדי לפרק את הליגנין ולהפריד את סיבי התאית.",
                visualClass: "stage-pulping-cooker",
                overlayText: "בישול העיסה",
            },
             {
                name: "4. הפרדת סיבים ועיסה גולמית",
                text: "הכימיקלים הסירו את רוב הליגנין! עכשיו הסיבים חופשיים וצפים בנוזל, ויוצרים עיסה חומה וגסה.",
                visualClass: "stage-pulp-stream",
                overlayText: "עיסה גולמית",
            },
             {
                name: "5. שטיפה וסינון",
                text: "העיסה נשטפת ביסודיות כדי להסיר שאריות כימיקלים, לכלוכים וסיבים גסים מדי. מתחילים להתקרב לנייר נקי.",
                visualClass: "stage-washing-filter",
                overlayText: "ניקוי העיסה",
            },
            {
                name: "6. הלבנה",
                text: "כדי שהנייר יהיה לבן בוהק, העיסה עוברת תהליך הלבנה שמרחיק את שאריות הליגנין והצבע. העיסה משנה צבע!",
                visualClass: "stage-bleaching-vat",
                overlayText: "הלבנה!",
            },
            {
                name: "7. דיפון (עמידות למים/דיו)",
                text: "מוסיפים חומרים מיוחדים שמפחיתים את ספיגות הנייר. בלי השלב הזה, הדיו היה נמרח מיד!",
                visualClass: "stage-additives-mix", // Reusing class for background/basic look
                 overlayText: "הוספת דיפון",
            },
             {
                name: "8. הוספת מילוי",
                text: "מוסיפים חומרים מינרליים דקים כמו קאולין. הם משפרים את חלקות הנייר, האטימות שלו וגם מוזילים את הייצור.",
                visualClass: "stage-fillers", // New class for specific visual style if needed
                 overlayText: "חומרי מילוי",
            },
            {
                name: "9. יצירת יריעה רטובה",
                text: "העיסה הדלילה מוזרמת על מסך רשת ארוך ונע. המים מתנקזים דרך הרשת, והסיבים נערמים ליצירת יריעה רטובה ועדינה.",
                visualClass: "stage-forming-wire",
                 overlayText: "יריעה רטובה",
            },
            {
                name: "10. סחיטה וייבוש",
                text: "היריעה עוברת דרך גלילים סוחטים כדי להוציא עוד מים, ואז על גלילים מחוממים לייבוש סופי. כאן היא הופכת להיות נייר יבש ומוצק!",
                visualClass: "stage-press-dryer",
                overlayText: "ייבוש הנייר",
            },
            {
                name: "11. גימור",
                text: "הנייר עובר טיפולים סופיים כמו ציפוי להחלקה או מעבר דרך גלילי קלנדר להשגת המרקם והמראה הסופי הנדרש.",
                visualClass: "stage-calender",
                 overlayText: "גימור מושלם",
            }
        ];

        let currentStageIndex = 0;

        function updateStage() {
            // Clear previous visual states and classes
            stageVisualDiv.className = '';
            stageVisualDiv.classList.add('stage-visual'); // Ensure base class is present
            stageVisualDiv.classList.add('stage-active'); // Class to control initial hide

            // Hide all visual elements initially for transition
            stageVisualDiv.querySelectorAll('.visual-element').forEach(el => {
                el.style.opacity = 0;
                el.style.transform = 'scale(0.8)';
            });
             visualOverlayText.style.opacity = 0; // Hide overlay text

            if (currentStageIndex >= stages.length) {
                // End state
                stageNameDiv.textContent = "המסע הושלם!";
                stageExplanationDiv.textContent = "הנייר מוכן לשימוש - לכתיבה, הדפסה וכל מטרה אחרת!";
                 stageVisualDiv.classList.add('stage-finished-roll'); // Final visual class
                 stageVisualDiv.classList.remove('stage-active'); // Remove active class
                 stageVisualDiv.querySelector('.visual-element.finished-roll').style.opacity = 1;
                 stageVisualDiv.querySelector('.visual-element.finished-roll').style.transform = 'scale(1)';
                nextStageButton.textContent = "התחל מחדש?";
                nextStageButton.disabled = false; // Enable to restart

            } else {
                const stage = stages[currentStageIndex];
                stageNameDiv.textContent = stage.name;
                stageExplanationDiv.textContent = stage.text;

                // Add the specific visual class for the current stage
                stageVisualDiv.classList.add(stage.visualClass);

                // Show the relevant visual element for the current stage
                const currentVisualElementClass = stageVisualMap[currentStageIndex];
                if (currentVisualElementClass) {
                     const visualElement = stageVisualDiv.querySelector('.' + currentVisualElementClass);
                     if (visualElement) {
                          // Use a small delay to allow stage-active class to take effect before showing
                         setTimeout(() => {
                              visualElement.style.opacity = 1;
                              visualElement.style.transform = 'scale(1)';
                         }, 50); // Adjust delay as needed for desired animation effect
                     }
                }

                 // Show overlay text if defined
                 if (stage.overlayText) {
                      visualOverlayText.textContent = stage.overlayText;
                      setTimeout(() => {
                           visualOverlayText.style.opacity = 1;
                      }, 200); // Delay overlay text appearance
                 } else {
                      visualOverlayText.textContent = ''; // Clear text
                 }


                nextStageButton.textContent = "התחנה הבאה במסע!";
                nextStageButton.disabled = false; // Enable button
                 stageVisualDiv.classList.remove('stage-active'); // Allow transition in
            }
        }

        // Event listener for the "Next" button
        nextStageButton.addEventListener('click', () => {
            if (currentStageIndex >= stages.length) {
                // Restart
                currentStageIndex = 0;
            } else {
                 currentStageIndex++;
            }
            updateStage();
        });

        // Event listener for the "Show/Hide Explanation" button
        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = detailedExplanationDiv.style.display === 'none';
            detailedExplanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מפורט' : 'רוצים לדעת יותר? הסבר מפורט';
             // Scroll to the detailed explanation when shown
            if (isHidden) {
                detailedExplanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });

        // Initialize the app with the first stage
        updateStage();
    });
</script>
```