---
title: "סוד היציבות: איך בונים גשר תלוי מודרני?"
english_slug: secret-of-stability-how-to-build-modern-suspension-bridge
category: "טכנולוגיה / הנדסה"
tags: ["גשרים", "הנדסה", "פיזיקה", "קונסטרוקציה", "כוחות"]
---
# סוד היציבות: איך בונים גשר תלוי מודרני?
גשרים תלויים כמו גשר הזהב בסן פרנסיסקו או גשר ברוקלין האייקוני נראים כאילו הם מרחפים באוויר, נתמכים באלגנטיות על ידי כבלים מפתיעים בעוביים. איך מבנה ענק וכביר כזה, החוצה מפרצים ענקיים, מצליח לשאת את משקל הסיפון הכבד, את תנועת אלפי כלי הרכב שעליו, את נשיבות הרוח העזות ואפילו עומסים קיצוניים כמו רעידות אדמה? האם התהליך ההנדסי מאחורי הפלאים הללו מורכב ומסובך כפי שהוא נראה? הצטרפו אלינו למסע מרתק אל עולם הפיזיקה וההנדסה, ובנו בעצמכם גשר תלוי צעד אחר צעד!

<div id="bridge-builder" dir="rtl">
    <div id="instructions"></div>
    <div id="bridge-area">
        <div id="sky"></div>
        <div id="ground"></div>
        <div id="base1" class="component base"></div>
        <div id="base2" class="component base"></div>
        <div id="tower1" class="component tower"></div>
        <div id="tower2" class="component tower"></div>
        <div id="anchor1" class="component anchor">
            <div class="anchor-text">עוגן איתן</div>
             <div class="anchor-point"></div>
        </div>
        <div id="anchor2" class="component anchor">
             <div class="anchor-text">עוגן איתן</div>
            <div class="anchor-point"></div>
        </div>
        <svg id="cables"></svg>
        <div id="deck" class="component deck"></div>
    </div>
    <button id="next-step">השלב הבא</button>
</div>

<style>
    /* סגנונות בסיסיים לאינטראקציה */
    #bridge-builder {
        width: 100%;
        max-width: 800px;
        margin: 20px auto;
        border: 1px solid #d3d3d3; /* גבול עדין יותר */
        padding: 20px;
        font-family: 'Heebo', sans-serif; /* פונט מודרני יותר */
        background-color: #f4f7f6; /* רקע בהיר ונעים */
        box-shadow: 0 4px 12px rgba(0,0,0,0.1); /* צל עדין ועמוק יותר */
        position: relative;
        border-radius: 8px; /* פינות מעוגלות */
        overflow: hidden; /* לוודא ששום דבר לא גולש החוצה מהקונטיינר */
    }

    #instructions {
        min-height: 60px; /* הגדלת גובה לטקסט ארוך יותר */
        text-align: center;
        margin-bottom: 20px;
        font-size: 1.2em; /* גופן גדול יותר */
        color: #003366; /* כחול כהה יותר */
        font-weight: bold; /* טקסט מודגש */
        display: flex;
        align-items: center; /* למרכז אנכית */
        justify-content: center; /* למרכז אופקית */
        background-color: #eef2f7; /* רקע עדין להוראות */
        padding: 10px;
        border-radius: 4px;
    }

    /* אזור הסימולציה עצמו */
    #bridge-area {
        width: 100%;
        height: 350px; /* הגדלת גובה אזור הסימולציה */
        border: 1px solid #b0bec5; /* גבול מעודן יותר */
        background: linear-gradient(to bottom, #87ceeb, #e0f2f7); /* רקע שמיים */
        position: relative;
        overflow: hidden;
        border-radius: 4px;
    }

     #sky {
         position: absolute;
         top: 0;
         left: 0;
         width: 100%;
         height: 100%; /* השמיים יתפסו את כל השטח העליון */
         background: linear-gradient(to bottom, #87ceeb 0%, #e0f2f7 80%, #b3e5fc 100%); /* גרדיאנט שמיים עדין */
         z-index: 0; /* מתחת לכל המרכיבים */
     }


    #ground {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 70px; /* הגדלת גובה הקרקע */
        background: linear-gradient(to top, #689f38, #8bc34a); /* גרדיאנט דשא/קרקע */
        z-index: 1;
         border-top: 3px solid #558b2f; /* הדגשת גבול עליון של הקרקע */
    }

    /* מרכיבי הגשר */
    .component {
        position: absolute;
        bottom: 70px; /* הצבה מעל הקרקע המוגדלת */
        transition: all 0.8s cubic-bezier(0.25, 0.8, 0.25, 1); /* אנימציית מעבר חלקה יותר */
        z-index: 2; /* מעל הקרקע והשמיים */
        box-sizing: border-box; /* לכלול גבול ופאדינג ברוחב/גובה */
    }

    .base {
        width: 60px; /* בסיסים רחבים יותר */
        height: 30px; /* בסיסים גבוהים יותר */
        background-color: #5d4037; /* חום כהה יותר */
        border-radius: 4px 4px 0 0; /* פינות עליונות מעוגלות */
         box-shadow: 0 -3px 6px rgba(0,0,0,0.2) inset; /* צל פנימי עליון */
         opacity: 0; /* התחלה בלתי נראית */
          transform: translateY(20px); /* התחלה מעט מתחת למקום */
          transition: all 0.6s ease-out;
    }
     .base.visible {
         opacity: 1;
         transform: translateY(0);
     }

    #base1 { left: 10%; } /* הזזה מעט פנימה */
    #base2 { left: 90% - 60px; /* 90% משמאל, פחות רוחב */ } /* הזזה מעט פנימה */

    .tower {
        width: 40px; /* מגדלים רחבים יותר */
        height: 0; /* מתחילים קרוסים */
        background-color: #78909c; /* אפור כחלחל */
        transform-origin: bottom center; /* מרכז האנימציה בתחתית */
        box-shadow: 0 4px 8px rgba(0,0,0,0.3); /* צל למגדלים */
         border-radius: 4px 4px 0 0; /* פינות עליונות מעוגלות */
    }

    #tower1 { left: 10% + 10px; /* ממורכז על הבסיס */ }
    #tower2 { left: 90% - 60px + 10px; /* ממורכז על הבסיס */ }

    .tower.built {
        height: 250px; /* גובה מגדל מוגדל */
         transition: height 1.2s cubic-bezier(0.68, -0.55, 0.27, 1.55); /* אנימציה קפיצית */
    }

    .anchor {
        width: 80px; /* עוגנים רחבים יותר */
        height: 50px; /* עוגנים גבוהים יותר */
        background-color: #757575; /* אפור כהה יותר */
        bottom: 30px; /* חצי שקועים בקרקע המוגדלת */
        z-index: 0; /* מתחת לקרקע בהתחלה */
        opacity: 0; /* מוסתרים בהתחלה */
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
        font-size: 0.9em; /* גודל גופן מעודן */
        border-radius: 6px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2) inset; /* צל פנימי לעוגנים */
         transform: translateY(30px); /* מתחילים מתחת לקרקע */
          transition: all 0.8s cubic-bezier(0.68, -0.55, 0.27, 1.55) 0.5s; /* אנימציה קפיצית והשהייה */
    }

    #anchor1 { left: 2%; } /* הזזה עוד יותר לצדדים */
    #anchor2 { left: 98% - 80px; /* 98% משמאל, פחות רוחב */ }

    .anchor.visible {
        opacity: 1;
        z-index: 2; /* להביא מעל הקרקע כשהם נראים */
         transform: translateY(0);
    }

     .anchor-text {
         position: relative;
         z-index: 1; /* לוודא שהטקסט מעל נקודת העוגן (אם מופיעה) */
     }

    /* SVG לכבלים */
    #cables {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 3; /* מעל המגדלים */
        pointer-events: none; /* לאפשר קליקים לעבור דרך ה-SVG */
    }

    #cables path {
        fill: none;
        stroke: #424242; /* כבלים בצבע כהה יותר */
        stroke-width: 6; /* כבלים עבים יותר */
        stroke-linecap: round; /* קצוות עגולים לכבלים */
        stroke-dasharray: 2000; /* הגדלת דאש כדי לכסות כבל ארוך יותר */
        stroke-dashoffset: 2000; /* התחלה מוסתרת */
        animation: draw-cable 2s cubic-bezier(0.25, 0.8, 0.25, 1) forwards; /* אנימציית ציור משופרת */
         opacity: 0; /* נסתר בהתחלה */
          transition: opacity 0.1s ease-out 0.1s; /* הופעה עדינה לאחר תחילת האנימציה */
    }
     #cables path.visible {
         opacity: 1;
     }

    #cables line {
        stroke: #616161; /* כבלי תליה בצבע בהיר יותר מכבל ראשי */
        stroke-width: 3; /* עובי כבלי תליה */
        stroke-linecap: round;
        stroke-dasharray: 100;
        stroke-dashoffset: 100;
        animation: draw-line 0.5s ease-out forwards;
         opacity: 0;
         transition: opacity 0.1s ease-out 0.05s;
    }
      #cables line.visible {
         opacity: 1;
     }


    @keyframes draw-cable {
        to {
            stroke-dashoffset: 0;
        }
    }
    @keyframes draw-line {
        to {
            stroke-dashoffset: 0;
        }
    }


    #deck {
        width: 0; /* מתחיל קרוס */
        height: 20px; /* סיפון גבוה יותר */
        background-color: #455a64; /* אפור כחלחל כהה לסיפון */
        bottom: 175px; /* מיקום הסיפון מעל הקרקע (70 גובה קרקע + 105 רווח) - יתאים לכבלי התליה */
        left: 15%; /* מיקום התחלה */
        z-index: 4; /* מעל כבלים */
        opacity: 0; /* נסתר בהתחלה */
        box-shadow: 0 4px 8px rgba(0,0,0,0.3); /* צל לסיפון */
         border-radius: 4px;
          transform-origin: left center; /* אנימציית גדילה משמאל לימין */
    }

    #deck.built {
         width: 70%; /* גדילה לרוחב מלא (בין 15% ל 85% משמאל) */
         opacity: 1;
         transition: width 1.8s cubic-bezier(0.4, 0, 0.2, 1), opacity 1.8s ease-out; /* אנימציה חלקה יותר */
         left: 15%; /* ודא שהמיקום נשאר קבוע */
         right: initial; /* למנוע מ right להתנגש */
    }


    /* כפתור השלב הבא */
    #next-step {
        display: block;
        width: 180px; /* כפתור רחב יותר */
        margin: 20px auto;
        padding: 12px 20px; /* פאדינג גדול יותר */
        font-size: 1.2em; /* גופן גדול יותר */
        cursor: pointer;
        background: linear-gradient(to bottom, #66bb6a, #43a047); /* גרדיאנט ירוק */
        color: white;
        border: none;
        border-radius: 6px; /* פינות מעוגלות יותר */
        text-align: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2); /* צל לכפתור */
        transition: all 0.3s ease; /* מעבר חלק בהובר */
        font-weight: bold;
    }

    #next-step:hover {
        background: linear-gradient(to bottom, #81c784, #66bb6a); /* גרדיאנט ירוק בהיר יותר בהובר */
         box-shadow: 0 6px 10px rgba(0,0,0,0.3);
          transform: translateY(-2px); /* אפקט קפיצה עדין */
    }
     #next-step:active {
         background: linear-gradient(to bottom, #43a047, #66bb6a); /* צבע לחיצה */
         box-shadow: 0 2px 4px rgba(0,0,0,0.2);
         transform: translateY(0);
     }


    /* כפתור הצגת/הסתרת הסבר */
    #toggle-explanation {
        display: block;
        width: 220px; /* כפתור רחב יותר */
        margin: 20px auto;
        padding: 12px 20px;
        font-size: 1.2em;
        cursor: pointer;
        background: linear-gradient(to bottom, #42a5f5, #2196f3); /* גרדיאנט כחול */
        color: white;
        border: none;
        border-radius: 6px;
        text-align: center;
         box-shadow: 0 4px 8px rgba(0,0,0,0.2);
         transition: all 0.3s ease;
        font-weight: bold;
    }
     #toggle-explanation:hover {
        background: linear-gradient(to bottom, #64b5f6, #42a5f5); /* גרדיאנט כחול בהיר יותר בהובר */
         box-shadow: 0 6px 10px rgba(0,0,0,0.3);
          transform: translateY(-2px);
    }
     #toggle-explanation:active {
         background: linear-gradient(to bottom, #2196f3, #42a5f5); /* צבע לחיצה */
         box-shadow: 0 2px 4px rgba(0,0,0,0.2);
         transform: translateY(0);
     }


    /* אזור ההסבר המורחב */
    #explanation {
        margin-top: 30px;
        padding: 25px; /* פאדינג גדול יותר */
        border: 1px solid #b0bec5; /* גבול עדין יותר */
        background-color: #e8f5e9; /* רקע ירוק בהיר עדין */
        display: none; /* מוסתר בהתחלה */
        line-height: 1.7; /* רווח שורות גדול יותר לקריאות משופרת */
        border-radius: 8px;
         box-shadow: 0 2px 8px rgba(0,0,0,0.1);
         color: #333; /* צבע טקסט כהה וקריא */
    }
    #explanation h2 {
        margin-top: 0;
        color: #2e7d32; /* ירוק כהה */
        border-bottom: 2px solid #a5d6a7; /* קו תחתון לכותרת */
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
     #explanation h3 { /* סגנון חדש לכותרות משנה בתוך ההסבר */
         color: #388e3c;
         margin-top: 20px;
         margin-bottom: 10px;
     }
    #explanation p, #explanation ul {
        margin-bottom: 18px; /* רווח תחתון גדול יותר */
    }
    #explanation ul {
        padding-right: 25px; /* פאדינג גדול יותר לרשימות */
    }
    #explanation li {
        margin-bottom: 10px; /* רווח גדול יותר בין פריטי רשימה */
    }
     #explanation strong {
         color: #1b5e20; /* הדגשה בצבע ירוק כהה יותר */
     }

    /* אנימציה להופעה */
     .fade-in {
         animation: fadeIn 0.8s ease-out forwards;
     }
     @keyframes fadeIn {
         from { opacity: 0; }
         to { opacity: 1; }
     }


</style>

<button id="toggle-explanation">הצג/הסתר את סודות הגשר התלוי</button>

<div id="explanation">
    <h2>הסבר מורחב: סוד היציבות של גשרים תלויים מודרניים</h2>

    <p><strong>מהו גשר תלוי ומתי הוא הפתרון המנצח?</strong><br>
    דמיינו סיפון כביש או רכבת המרחף מעל תהום או מים עמוקים, ללא עמודים תומכים באמצע... זהו בדיוק הקסם של גשר תלוי! הסיפון אינו נתמך ישירות מלמטה, אלא "נתלה" מלמעלה בעזרת מערכת גאונית של כבלים. גשרים אלו הם הפתרון האולטימטיבי לגישור על מפתחים עצומים, היכן שבניית עמודים במרכז בלתי אפשרית, יקרה או פשוט מפריעה (למשל לתנועת ספינות). מעבר לפונקציונליות, הם גם יצירות אדריכליות מרהיבות!</p>

    <h3>מסע בזמן: מחוטרי במבוק לכבלי פלדה</h3>
    <p>שורשיהם של גשרים תלויים עתיקים כמעט כמו הציוויליזציה, בצורת גשרי חבלים פשוטים מעל נהרות קטנים. הגשרים התלויים המודרניים החלו לצוץ במאה ה-19, אך הם היו מוגבלים בגודלם וחוזקם. הפריצה הגדולה הגיעה עם המהפכה התעשייתית ופיתוח פלדה חזקה במיוחד, שאפשרה לטוות כבלים בעלי כושר נשיאה אדיר. גשר ברוקלין בניו יורק (1883) וגשר הזהב בסן פרנסיסקו (1937) הם דוגמאות מופתיות לאופן שבו פלדה ובטון שינו את כללי המשחק.</p>

    <h3>פיזיקה בפעולה: גיבורי המתיחה והלחיצה</h3>
    <p>הסוד ליציבות גשר תלוי טמון בהבנת כוחות והפעלתם בצורה חכמה:
    <ul>
        <li><strong>כוח מתיחה (Tension):</strong> זהו הכוח השליט בכבלים הראשיים ו"תלי הסיפון" (כבלי התליה האנכיים). דמיינו שאתם מנסים לקרוע חבל - זה כוח מתיחה. הפלדה החזקה מסוגלת לעמוד בכוחות מתיחה עצומים ללא קריסה.</li>
        <li><strong>כוח לחיצה (Compression):</strong> זהו הכוח העיקרי הפועל על המגדלים. משקל הסיפון והכבלים "לוחצים" אותם כלפי מטה. המגדלים, שנבנים בדרך כלל מבטון או פלדה עבים, חייבים להיות בלתי ניתנים לדחיסה.</li>
    </ul>
    בפשטות, הסיפון נתלה על כבלי התליה (מתיחה), אלו מושכים את הכבלים הראשיים (מתיחה), הכבלים הראשיים לוחצים כלפי מטה על המגדלים (לחיצה) ומושכים לצדדים את העוגנים (מתיחה). המערכת כולה מפזרת את העומס האדיר אל נקודות קריטיות: המגדלים (מטה) והעוגנים (הצידה), המעבירים אותו לבסוף בבטחה אל הקרקע המוצקה.</p>

    <h3>שחקני המפתח על בימת הבנייה:</h3>
    <p>כל גשר תלוי מודרני מורכב ממספר אלמנטים חיוניים:
    <ul>
        <li><strong>המגדלים (Towers):</strong> עמודים מונומנטליים שיתמכו בכבלים הראשיים. בלעדיהם, אין לגשר גובה והכבלים לא יוכלו לתלות את הסיפון.</li>
        <li><strong>הכבלים הראשיים (Main Cables):</strong> "עמוד השדרה" של הגשר. הם עוברים מעל המגדלים ומעוגנים בקרקע בקצוות. בנויים מאלפי גידי פלדה דקים שטווים יחד לכדי כבל ענק ונושאים את עיקר משקל הגשר.</li>
        <li><strong>כבלי התליה (Suspenders / Hangers):</strong> הכבלים הקצרים המחברים את הכבלים הראשיים לסיפון. הם נושאים ישירות את משקל הסיפון והתנועה עליו.</li>
        <li><strong>הסיפון (Deck):</strong> המשטח העליון עליו נוסעים. חייב להיות קשיח מספיק כדי לשאת עומסים מקומיים וגמיש מספיק כדי להתמודד עם תנודות ורוח.</li>
        <li><strong>העוגנים (Anchorages):</strong> מבני ענק מאסיביים, לרוב מבטון משוריין או קשורים ישירות לסלע האם, הנמצאים בקצות הגשר ומעגנים את הכבלים הראשיים. הם חייבים לעמוד בכוחות מתיחה עצומים מבלי לזוז מילימטר.</li>
    </ul></p>

    <h3>תזמורת הבנייה: צעד אחר צעד</h3>
    <p>בניית גשר תלוי היא פרויקט הנדסי מורכב ומדויק, המתוכנן עד לפרט האחרון:
    <ol>
        <li><strong>היסודות נבנים:</strong> ראשית, מכינים בסיסים איתנים למגדלים, לעיתים קרובות בעומק רב בקרקע או מתחת למים.</li>
        <li><strong>המגדלים מזנקים:</strong> המגדלים העצומים מוקמים, לעיתים בו זמנית משני צידי המפתח.</li>
        <li><strong>הכבלים הראשיים נמתחים:</strong> זהו שלב מרכזי הכולל מתיחה מדויקת של אלפי גידי הפלדה מעל המגדלים ויצירת הכבל הראשי המעוגן.</li>
        <li><strong>העיגון מתבצע:</strong> קצות הכבלים הראשיים מקובעים לעד בתוך העוגנים המאסיביים, המוכנים לשאת את כל כוח המתיחה.</li>
        <li><strong>כבלי התליה מחוברים:</strong> הכבלים הקצרים המיועדים לתליית הסיפון מותקנים על הכבלים הראשיים במרווחים קבועים.</li>
        <li><strong>הסיפון נבנה:</strong> קטעי הסיפון מורמים בזהירות ומחוברים לכבלי התליה. בדרך כלל מתחילים מהמגדלים ומתקדמים בו-זמנית לעבר המרכז, כדי לשמור על איזון המערכת.</li>
    </ol>
    </p>

    <h3>חומרי גלם מהפכניים ואתגרים הנדסיים:</h3>
    <p><strong>חומרים:</strong> פלדה ובטון מזוין הם החומרים הבלתי מעורערים של גשרים תלויים מודרניים. פלדה מצטיינת במתיחה (לכבלים) ובטון בלחיצה (למגדלים ועוגנים).
    <br>
    <strong>אתגרים:</strong> מהנדסים מתמודדים עם כוחות טבע אדירים:
    <ul>
        <li><strong>רוח:</strong> היא האויב הגדול ביותר. גשרים מודרניים מעוצבים בצורה אווירודינמית וכוללים בולמי זעזועים כדי למנוע תנודות מסוכנות הנגרמות מרוח.</li>
        <li><strong>רעידות אדמה:</strong> באזורים סייסמיים, הגשרים נבנים עם מיסבים מיוחדים ומבנה גמיש מתוכנן לספוג אנרגיה סייסמית.</li>
        <li><strong>עומסים:</strong> מעבר למשקל עצמי ותנועה רגילה, יש לחשב עומסי קיצון כמו שלג כבד, רוחות סערה, ועומסים דינמיים (בלימת משאיות).</li>
    </ul>
    התמודדות עם אתגרים אלו דורשת שימוש במודלים ממוחשבים מתוחכמים, ניסויים מדוקדקים (כמו במנהרות רוח), ותכנון עם שולי בטיחות נדיבים. התוצאה היא גשרים לא רק יציבים וחזקים, אלא גם עמידים בפני איתני הטבע לאורך שנים רבות.</p>
</div>

<script>
    const instructionsDiv = document.getElementById('instructions');
    const bridgeArea = document.getElementById('bridge-area');
    const nextStepButton = document.getElementById('next-step');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const base1 = document.getElementById('base1');
    const base2 = document.getElementById('base2');
    const tower1 = document.getElementById('tower1');
    const tower2 = document.getElementById('tower2');
    const anchor1 = document.getElementById('anchor1');
    const anchor2 = document.getElementById('anchor2');
    const cablesSVG = document.getElementById('cables');
    const deck = document.getElementById('deck');

    let currentStep = 0;
    const groundHeight = 70; // Match CSS ground height

    const steps = [
        { text: "בואו נתחיל! מקמו את הבסיסים האיתנים למגדלים.", action: () => {
            base1.classList.add('visible');
            base2.classList.add('visible');
        }},
        { text: "מרתק! הקימו את המגדלים הגבוהים שישאו את הגשר.", action: () => {
            tower1.classList.add('built');
            tower2.classList.add('built');
        }},
        { text: "כעת, הניחו את הכבלים הראשיים העוברים מעל המגדלים.", action: () => {
            // Use SVG path to draw the main cable
            const svgWidth = cablesSVG.clientWidth;
            const svgHeight = cablesSVG.clientHeight;
            // Get dynamic positions based on CSS
            const tower1X = tower1.offsetLeft + tower1.clientWidth / 2;
            const tower2X = tower2.offsetLeft + tower2.clientWidth / 2;
            const towerTopY_css = bridgeArea.clientHeight - (parseInt(tower1.style.bottom || getComputedStyle(tower1).bottom) + tower1.clientHeight); // Y from top of bridgeArea for tower top
            const towerTopY_svg = towerTopY_css; // SVG Y matches CSS Y from top

            const cableDropY_svg = towerTopY_svg + 80; // עומק נפילה של הכבל באמצע

            const controlX = svgWidth / 2;
            const controlY = cableDropY_svg; // נקודת בקרה לקשת
            const d = `M ${tower1X},${towerTopY_svg} Q ${controlX},${controlY} ${tower2X},${towerTopY_svg}`;

            const mainCablePath = document.createElementNS("http://www.w3.org/2000/svg", "path");
            mainCablePath.setAttribute('d', d);
            mainCablePath.setAttribute('id', 'main-cable');
             mainCablePath.classList.add('visible'); // Make visible for animation
            cablesSVG.appendChild(mainCablePath);

             // Calculate and apply stroke-dashoffset for animation
             const length = mainCablePath.getTotalLength();
             mainCablePath.style.strokeDasharray = length;
             mainCablePath.style.strokeDashoffset = length;
             mainCablePath.style.animation = 'none'; // Reset animation
             // Trigger reflow
             void mainCablePath.offsetWidth;
             // Apply animation
             mainCablePath.style.animation = `draw-cable 2s cubic-bezier(0.25, 0.8, 0.25, 1) forwards`;

        }},
         { text: "חיוני! עגנו את הכבלים הראשיים עמוק בקרקע. כוחות מתיחה אדירים פועלים על העוגנים!", action: () => {
            anchor1.classList.add('visible');
            anchor2.classList.add('visible');

             // Connect main cable to anchors with SVG lines
            const mainCablePath = document.getElementById('main-cable');
            if (!mainCablePath) return; // Should not happen if steps are sequential

            const svgWidth = cablesSVG.clientWidth;
            const svgHeight = cablesSVG.clientHeight;

            // Get the ends of the main cable path (should be above the towers)
             const cableEnd1 = mainCablePath.getPointAtLength(0);
             const cableEnd2 = mainCablePath.getPointAtLength(mainCablePath.getTotalLength());


             // Get anchor connection points (center of anchor's anchor-point div, relative to bridge-area top)
             const anchor1Point = anchor1.querySelector('.anchor-point');
             const anchor2Point = anchor2.querySelector('.anchor-point');

             const anchor1X_svg = anchor1Point.offsetLeft + anchor1Point.clientWidth / 2;
             const anchor1Y_svg = anchor1Point.offsetTop + anchor1Point.clientHeight / 2; // Y relative to bridge-area top

             const anchor2X_svg = anchor2Point.offsetLeft + anchor2Point.clientWidth / 2;
             const anchor2Y_svg = anchor2Point.offsetTop + anchor2Point.clientHeight / 2; // Y relative to bridge-area top


            const cable1 = document.createElementNS("http://www.w3.org/2000/svg", "path");
            // Draw from cable end to anchor point
            const d1 = `M ${cableEnd1.x},${cableEnd1.y} L ${anchor1X_svg},${anchor1Y_svg}`;
            cable1.setAttribute('d', d1);
            cable1.setAttribute('stroke-width', '6');
            cable1.setAttribute('stroke', '#424242');
            cable1.classList.add('anchor-cable', 'visible'); // Add visible class

            const cable2 = document.createElementNS("http://www.w3.org/2000/svg", "path");
            const d2 = `M ${cableEnd2.x},${cableEnd2.y} L ${anchor2X_svg},${anchor2Y_svg}`;
            cable2.setAttribute('d', d2);
             cable2.setAttribute('stroke-width', '6');
             cable2.setAttribute('stroke', '#424242');
            cable2.classList.add('anchor-cable', 'visible'); // Add visible class


            cablesSVG.appendChild(cable1);
            cablesSVG.appendChild(cable2);

             // Animate anchor cables
             cablesSVG.querySelectorAll('.anchor-cable').forEach(cable => {
                 const length = cable.getTotalLength();
                 cable.style.strokeDasharray = length;
                 cable.style.strokeDashoffset = length;
                 cable.style.animation = 'none'; // Reset animation
                 void cable.offsetWidth; // Trigger reflow
                 cable.style.animation = `draw-line 0.8s ease-out forwards`;
             });

        }},
        { text: "חברו את כבלי התליה האנכיים מהכבל הראשי אל המקום בו ימוקם הסיפון.", action: () => {
             const mainCablePath = document.getElementById('main-cable');
             if (!mainCablePath) return;

             const svgHeight = cablesSVG.clientHeight;
             // Deck bottom is 175px from bridgeArea bottom (70px ground + 105px gap)
             // Deck height is 20px
             // So deck top is at 175 + 20 = 195px from bridgeArea bottom
             // Y coordinate from bridgeArea top is svgHeight - 195
             // Let's connect suspenders to the top edge of the future deck position
             const deckTopY_svg = svgHeight - 195;

            // Add suspender cables - distribute evenly along the main cable path length
            const numSuspenders = 12; // Number of pairs of suspenders
            const mainCableLength = mainCablePath.getTotalLength();
            const startPercent = 0.1; // Start slightly after the tower
            const endPercent = 0.9; // End slightly before the tower
            const effectiveLength = mainCableLength * (endPercent - startPercent);

            for (let i = 0; i < numSuspenders; i++) {
                const percent = startPercent + (i / (numSuspenders - 1)) * (endPercent - startPercent);
                const point = mainCablePath.getPointAtLength(mainCableLength * percent);

                const suspender = document.createElementNS("http://www.w3.org/2000/svg", "line");
                suspender.setAttribute('x1', point.x);
                suspender.setAttribute('y1', point.y);
                suspender.setAttribute('x2', point.x);
                suspender.setAttribute('y2', deckTopY_svg); // Connect to the approximate deck level
                suspender.classList.add('suspender-cable', 'visible'); // Add visible class

                 // Animate suspender drawing
                 const length = Math.abs(point.y - deckTopY_svg); // Approximate length
                 suspender.style.strokeDasharray = length;
                 suspender.style.strokeDashoffset = length;
                 suspender.style.animation = 'none'; // Reset animation
                 void suspender.offsetWidth; // Trigger reflow
                 suspender.style.animation = `draw-line 0.4s ease-out forwards ${i * 0.04}s`; // Staggered animation

                cablesSVG.appendChild(suspender);
            }
        }},
        { text: "השלב האחרון: בניית הסיפון! כבלי התליה נושאים כעת את משקלו ומעבירים אותו לכבלים הראשיים.", action: () => {
            deck.classList.add('built');
        }},
        { text: "הגשר התלוי המודרני הושלם! כל הכבוד למהנדסים!", action: () => {
            nextStepButton.style.display = 'none'; // Hide button when finished
            instructionsDiv.textContent = "הגשר התלוי המודרני הושלם! כל הכבוד למהנדסים על יצירת הפלא הזה.";
             // Optional: Add a final flourish animation or state
        }}
    ];

    function updateSimulation() {
        if (currentStep < steps.length) {
            instructionsDiv.textContent = steps[currentStep].text;
            steps[currentStep].action();
            currentStep++;
             if (currentStep === steps.length) {
                 nextStepButton.textContent = "הבנייה הסתיימה"; // Change button text on final step
             }
        }
    }

    nextStepButton.addEventListener('click', updateSimulation);

    // Initial state reset and setup
    function initializeSimulation() {
        currentStep = 0;
        instructionsDiv.textContent = "בואו נתחיל לבנות גשר תלוי מודרני!";
        nextStepButton.style.display = 'block';
         nextStepButton.textContent = "השלב הבא";

        // Reset components
        base1.classList.remove('visible');
        base2.classList.remove('visible');
        tower1.classList.remove('built');
        tower2.classList.remove('built');
        anchor1.classList.remove('visible');
        anchor2.classList.remove('visible');
        deck.classList.remove('built');

        // Clear SVG cables
        cablesSVG.innerHTML = '';

         // Ensure initial CSS states are applied
         base1.style.opacity = 0; base1.style.transform = 'translateY(20px)';
         base2.style.opacity = 0; base2.style.transform = 'translateY(20px)';
         tower1.style.height = '0';
         tower2.style.height = '0';
         anchor1.style.opacity = 0; anchor1.style.transform = 'translateY(30px)';
         anchor2.style.opacity = 0; anchor2.style.transform = 'translateY(30px)';
         deck.style.width = '0'; deck.style.opacity = 0;
         deck.style.transform = 'scaleX(0)'; // Add scale transform for growth effect

         // Small delay to show initial state before first step
         setTimeout(() => {
             // No action needed, just show the initial text and button
         }, 100);
    }

    // Initialize on page load
    initializeSimulation();


    // Toggle explanation visibility
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        if (isHidden) {
             explanationDiv.style.display = 'block';
             // Optional: Scroll to explanation
             explanationDiv.scrollIntoView({ behavior: 'smooth' });
        } else {
             explanationDiv.style.display = 'none';
        }
    });

    // Optional: Restart button functionality (if needed, but wasn't requested)
    // For this task, just hiding the button at the end is sufficient.

</script>
---