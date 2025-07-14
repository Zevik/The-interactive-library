---
title: "סוד ההולוגרמה: כיצד האור בונה מציאות תלת-ממדית?"
english_slug: the-secret-of-the-hologram-how-light-builds-3d-reality
category: "מדעים מדויקים / פיזיקה"
tags:
  - הולוגרפיה
  - אופטיקה
  - עקיפה
  - התאבכות
  - לייזר
---
<h1>סוד ההולוגרמה: ללכוד את המציאות בקרן אור אחת</h1>
<p>דמיינו תמונה שלא סתם נראית אמיתית, אלא ממש *נמצאת* שם. תמונה שממנה אפשר להביט מצד לצד, לראות עומק ופרספקטיבה, כאילו האובייקט עצמו מופיע מול עיניכם. זה לא מדע בדיוני, זו הולוגרפיה – אמנות רישום האור שמפענחת את צפונות המרחב. בניגוד לצילום רגיל שלוכד רק את עוצמת האור, הולוגרמה לוכדת את הסיפור המלא של גל האור, כולל ה'צורה' המרחבית והעומק שלו. בואו נגלה את הקסם הזה.</p>

<div class="hologram-app">
    <h2>שלב ההקלטה: בונים תבנית קסומה</h2>
    <div class="diagram">
        <div id="laser" class="component" data-label="מקור אור קוהרנטי">לייזר</div>
        <div id="beam-splitter" class="component" data-label="מפצל קרן">מפצל</div>
        <div id="object" class="component" data-label="אובייקט תלת-ממדי">אובייקט</div>
        <div id="holographic-film" class="component" data-label="סרט הולוגרפי רגיש">סרט הולוגרפי</div>

        <!-- Beams - will be animated -->
        <div id="beam-to-splitter" class="beam horizontal"></div>
        <div id="ref-beam" class="beam vertical"></div>
        <div id="obj-beam-to-object" class="beam horizontal"></div>
        <div id="obj-beam-from-object" class="beam diagonal"></div>

        <!-- Interference visualization area -->
        <div id="interference-area">
             <div id="interference-pattern" class="interference-pattern hidden"></div>
        </div>


        <!-- Dynamic Labels - maybe appear on hover or animation -->
        <div class="dynamic-label hidden" id="label-laser">מקור אור קוהרנטי (לייזר)</div>
        <div class="dynamic-label hidden" id="label-splitter">מפצל קרן: מפריד את הלייזר לשתי קרניים</div>
        <div class="dynamic-label hidden" id="label-ref">קרן התייחסות: מגיעה ישירות לסרט</div>
        <div class="dynamic-label hidden" id="label-obj-to">קרן אובייקט: מוארת על האובייקט</div>
        <div class="dynamic-label hidden" id="label-object">האובייקט שממנו ניצור הולוגרמה</div>
         <div class="dynamic-label hidden" id="label-obj-from">קרן אובייקט מוחזרת/מפוזרת מהאובייקט (נושאת מידע תלת-ממדי)</div>
        <div class="dynamic-label hidden" id="label-film">סרט הולוגרפי: המקום בו קסם ההתאבכות נרשם</div>
        <div class="dynamic-label hidden" id="label-interference">תבנית התאבכות מיקרוסקופית מורכבת (ההולוגרמה עצמה)</div>

    </div>
    <button id="simulate-button">הפעל את קסם ההקלטה!</button>
</div>

<button id="toggle-explanation" class="explanation-toggle">רוצים לדעת איך זה קורה? לחצו כאן להסבר המלא</button>

<div id="detailed-explanation" class="hidden detailed-explanation">
    <h2>פיענוח הקסם: כך עובדת הולוגרמה</h2>

    <h3>מהי בעצם הולוגרמה? הרבה מעבר לתמונה</h3>
    <p>בצילום רגיל, אנחנו לוכדים רק את עוצמת האור שמגיעה מכל נקודה באובייקט ומטביעים אותה על מישור דו-ממדי. הולוגרמה הולכת צעד ענק קדימה: היא רושמת לא רק את עוצמת האור, אלא גם את ה'פאזה' שלו. דמיינו גל אור כגל ים – הפאזה היא המיקום של הנקודה על הגל (שיא, שפל, או משהו באמצע). המידע על הפאזה הוא שמכיל את כל העומק והפרספקטיבה התלת-ממדית של האובייקט המקורי. לוכדים את חזית הגל המלאה, לא רק 'חתך' שטוח שלה.</p>
    <p><strong>נקודת מפתח:</strong> צילום = בהירות (אמפליטודה בלבד). הולוגרפיה = בהירות + עומק וצורה (אמפליטודה ופאזה).</p>

    <h3>עקרונות קסם בפיזיקה (זה פשוט יותר ממה שזה נשמע)</h3>
    <ul>
        <li><strong>אור קוהרנטי (הכוכב: הלייזר):</strong> כדי לרשום את הפאזה המדויקת של גל אור, צריך שהאור עצמו יהיה סופר-מסודר. כל גלי האור צריכים להיות באותו אורך גל (צבע יחיד), לזוז באותה פאזה, ולהישאר 'מסונכרנים' לאורך זמן ומרחב. רק לייזרים מסוגלים לייצר אור כל כך 'מתואם' – אור קוהרנטי.</li>
        <li><strong>התאבכות: ריקוד הגלים:</strong> כששני גלי אור קוהרנטיים נפגשים, הם 'רוקדים' יחד. אם הם נפגשים ב'צעד' זהה (שיא מול שיא, שפל מול שפל) – האור מתחזק (התאבכות בונה). אם הם נפגשים ב'צעד' הפוך (שיא מול שפל) – הם מבטלים זה את זה (התאבכות הורסת). ריקוד זה יוצר תבנית של פסים בהירים וכהים, המכונה 'תבנית התאבכות'. צורת התבנית מספרת לנו בדיוק על הפרש הדרכים (ובהתאם – הפרש הפאזה) שהגלים עברו.</li>
        <li><strong>עקיפה: האור מתכופף ומספר סיפור:</strong> כשגל אור פוגש במחסום או עובר דרך חריץ צר (או דרך תבנית עדינה ומורכבת כמו תבנית התאבכות רשומה), הוא מתפשט ומתכופף. תבנית ההתאבכות שרשמנו על הסרט ההולוגרפי היא למעשה מבנה מיקרוסקופי מורכב שמאלץ את האור להתכופף בדרכים ספציפיות ביותר כשהוא עובר דרכו.</li>
    </ul>

    <h3>שלב ההקלטה: לבנות את הקוד הסודי</h3>
    <p>התהליך מתחיל במערך מדויק:</p>
    <ol>
        <li><strong>הצורך ב'מאסטרו' קוהרנטי:</strong> משתמשים בלייזר יחיד כמקור אור.</li>
        <li><strong>פיצול הכוח:</strong> קרן הלייזר מפוצלת לשתיים על ידי מפצל קרן (כמו מראה חצי שקופה מתוחכמת).</li>
        <li><strong>שתי קרניים, שתי משימות:</strong> קרן אחת, 'קרן ההתייחסות', נשלחת במסלול ישר ופשוט אל הסרט ההולוגרפי. קרן שנייה, 'קרן האובייקט', מוארת על האובייקט התלת-ממדי.</li>
        <li><strong>קרן האובייקט מתמלאת במידע:</strong> האור שפוגע באובייקט מוחזר או מפוזר ממנו. כל נקודה זעירה על האובייקט שולחת גלים לכל הכיוונים. חזית הגל שמגיעה מהאובייקט אל הסרט ההולוגרפי היא מורכבת להפליא, והיא מכילה את כל המידע המרחבי – העומק, הצורה, הטקסטורה – של האובייקט. היא 'נושאת את הסיפור' של האובייקט.</li>
        <li><strong>המפגש הגורלי על הסרט:</strong> שתי הקרניים – קרן ההתייחסות ה'מסודרת' וקרן האובייקט ה'עמוסה במידע' – נפגשות על פני השטח הרגיש של הסרט ההולוגרפי.</li>
        <li><strong>ריקוד ההתאבכות נרשם:</strong> מכיוון ששתי הקרניים הגיעו מאותו לייזר מקורי, הן קוהרנטיות ויכולות להתאבך. בכל נקודה על הסרט, הפרש הדרכים (ולכן הפרש הפאזה) בין הקרניים קובע אם תהיה שם התאבכות בונה (יותר אור) או הורסת (פחות אור). מכיוון שחזית הגל של קרן האובייקט מורכבת כל כך, גם תבנית ההתאבכות הנוצרת על הסרט היא מורכבת ביותר, עדינה ומיקרוסקופית. זו אינה תמונה של האובייקט, אלא 'קוד מוצפן' – תבנית פסים וצורות שרושמת את הפרש הפאזה בין הקרניים בכל נקודה. זוהי ה'הולוגרמה' הראשונית.</li>
        <li><strong>ללכוד את הקוד:</strong> הסרט ההולוגרפי (מעין סרט צילום ברזולוציה אסטרונומית) רושם את תבנית ההתאבכות הזו כשינויים קבועים בחומר הרגיש לאור. הוא מקבע את ה'קוד' הפיזי הזה.</li>
         <li><strong>הקוד המיקרוסקופי מכיל הכל:</strong> למרות שההולוגרמה עצמה נראית כמו כתם אפור או שקוף עם פסים עדינים בעין בלתי מזוינת, היא מכילה את כל המידע התלת-ממדי על האובייקט, מקודד בתוך המבנה המיקרוסקופי של תבנית ההתאבכות.</li>
    </ol>

    <h3>שלב השחזור: מחזירים את המציאות לחיים</h3>
    <p>כדי 'לפענח' את הקוד ולראות את התמונה התלת-ממדית:</p>
    <ol>
        <li><strong>מאירים את הקוד הסודי:</strong> מאירים את הסרט ההולוגרפי הרשום עם קרן אור דומה מאוד לקרן ההתאבכות המקורית (לרוב שוב לייזר).</li>
        <li><strong>האור פוגש את התבנית ומספר סיפור:</strong> תבנית ההתאבכות המקובעת על הסרט פועלת כמבנה עקיפה מורכב. כשהאור פוגע בה, הוא נשבר ומתפשט בדרכים שנקבעו על ידי הקוד הרשום.</li>
        <li><strong>שחזור מושלם של חזית הגל:</strong> קסם העקיפה גורם לכך שהאור היוצא מההולוגרמה משחזר במדויק את חזית הגל המקורית של קרן האובייקט, כאילו היא עדיין מגיעה מהאובייקט עצמו!</li>
        <li><strong>המוח שלנו מבין את הסיפור התלת-ממדי:</strong> הצופה מביט באור המשוחזר. מכיוון שזהו שחזור של חזית הגל המקורית (שנשאה מידע תלת-ממדי), המוח שלנו מפרש את זה כתמונה תלת-ממדית אמיתית לגמרי. אפשר להזיז את הראש ולראות זוויות שונות של האובייקט, בדיוק כמו שמסתכלים על אובייקט אמיתי. נוצרת תמונה 'וירטואלית' שנראית מרחפת מאחורי הסרט.</li>
    </ol>

    <h3>הולוגרמות סביבנו: איפה הקסם הזה מופיע?</h3>
    <ul>
        <li><strong>הולוגרמות ביטחוניות:</strong> על שטרות, כרטיסי אשראי, רישיונות. אלה הולוגרמות השתקפות שקל לבדוק באור רגיל והן קשות מאוד לזיוף.</li>
        <li><strong>אמנות ותצוגות:</strong> יצירת מיצגים תלת-ממדיים מדהימים במוזיאונים ותערוכות.</li>
        <li><strong>טכנולוגיה:</strong> אחסון נתונים (פוטנציאל לקיבולת ענקית), מיקרוסקופיה, ניתוחים מורכבים (הצגת הדמיות תלת-ממדיות).</li>
        <li><strong>הולוגרמות העברה והשתקפות:</strong> אלה שני הסוגים העיקריים, הנבדלים באופן ההקלטה והשחזור והאם הן נצפות באור לייזר או אור רגיל.</li>
    </ul>
    <p>הולוגרפיה היא דוגמה מרהיבה לאופן שבו הבנה עמוקה של פיזיקת האור יכולה לפתוח דלתות למציאויות ויזואליות חדשות ומרתקות.</p>
</div>

<style>
    /* General Styles */
    .hologram-app, .detailed-explanation {
        direction: rtl;
        font-family: 'Arial', sans-serif;
        max-width: 800px;
        margin: 20px auto;
        padding: 30px; /* More padding */
        border: 1px solid #d3e0ea; /* Softer border */
        border-radius: 12px; /* More rounded corners */
        background-color: #e9f3f8; /* Light blue background */
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    }

    .hologram-app h2 {
        color: #004a7f; /* Dark blue heading */
        margin-bottom: 25px;
        font-size: 1.8em;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.05);
    }

    /* Diagram Styles */
    .diagram {
        position: relative;
        width: 100%;
        height: 350px; /* Slightly taller */
        border: 2px dashed #aaccdd; /* Clearer dashed border */
        margin-bottom: 30px;
        background: linear-gradient(to bottom, #ffffff 0%, #f0f8ff 100%); /* Gentle gradient background */
        overflow: hidden;
        border-radius: 8px;
    }

    .component {
        position: absolute;
        padding: 8px 15px; /* More padding */
        background-color: #ffffff; /* White background */
        border: 1px solid #007bff; /* Blue border */
        border-radius: 6px;
        font-size: 1em;
        white-space: nowrap;
        text-align: center;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease; /* Add subtle hover effect */
        cursor: default; /* Indicate not directly clickable for simulation */
        font-weight: bold;
        color: #333;
    }

     .component:hover {
        transform: translateY(-3px);
        box-shadow: 0 5px 12px rgba(0, 0, 0, 0.15);
     }


    #laser { top: 80px; left: 20px; background-color: #ffdddd; border-color: #ff0000; } /* Reddish for laser */
    #beam-splitter {
        top: 80px; left: 250px; /* Adjusted position */
        width: 25px; height: 80px; /* Larger */
        background: linear-gradient(45deg, #bbddff, #66aaff); /* Blue gradient */
        border: 2px solid #007bff; /* Stronger border */
        border-radius: 6px;
        transform: rotate(45deg);
        display: flex; align-items: center; justify-content: center;
        color: #004a7f;
        font-size: 0.9em;
        font-weight: bold;
     }
    #object { top: 80px; left: 550px; background-color: #ddffdd; border-color: #00aa00; } /* Greenish for object */
    #holographic-film {
        top: 280px; left: 520px; /* Adjusted position */
        width: 150px; height: 25px; /* Larger */
        background-color: #ffcccc; border-color: #ff0000; /* Reddish for film */
        display: flex; align-items: center; justify-content: center;
        color: #a00;
        font-weight: bold;
        font-size: 0.9em;
     }

    .beam {
        position: absolute;
        background: linear-gradient(90deg, #ff0000, #ff6666); /* Red gradient for light */
        height: 4px; /* Thicker beam */
        filter: blur(0.5px); /* Slight glow effect */
        transition: width 1.5s ease-out, height 1.5s ease-out, transform 1.5s ease-out, top 1.5s ease-out, left 1.5s ease-out, opacity 0.5s ease-out;
        transform-origin: left center; /* Default origin for horizontal */
    }

    .beam.horizontal { top: calc(80px + 12.5px); /* Center vertically within component height */ }
    .beam.vertical {
        left: calc(250px + 12.5px); /* Center horizontally within splitter width */
        width: 4px; /* Thicker */
        transform-origin: top center; /* Origin for vertical */
        background: linear-gradient(180deg, #ff0000, #ff6666); /* Gradient top to bottom */
     }
     .beam.diagonal {
        width: 4px; /* Thicker */
        transform-origin: top left; /* Origin for diagonal */
        background: linear-gradient(-45deg, #ff0000, #ff6666); /* Gradient along diagonal */
     }


    #beam-to-splitter { top: 92.5px; left: 55px; width: 0px; opacity: 0; } /* Start from laser edge */
    #ref-beam { top: 92.5px; left: 262.5px; width: 4px; height: 0px; transform: rotate(0deg); opacity: 0; transform-origin: top center; } /* Start below splitter center */
    #obj-beam-to-object { top: 92.5px; left: 262.5px; width: 0px; opacity: 0; } /* Start from splitter center */
    #obj-beam-from-object { top: 92.5px; left: 565px; width: 4px; height: 0px; transform: rotate(0deg); opacity: 0; transform-origin: top left; } /* Start from object edge */


    #interference-area {
        position: absolute;
        top: 280px; left: 520px; /* Match film position */
        width: 150px; height: 25px;
        background-color: rgba(255, 100, 100, 0.1); /* Subtle overlay */
        border: 1px dashed rgba(255, 0, 0, 0.5);
        box-sizing: border-box;
        overflow: hidden; /* Keep pattern inside film */
    }

    .interference-pattern {
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        /* A more complex pattern - example using stripes */
        background-image: repeating-linear-gradient(45deg, rgba(255,0,0,0.8), rgba(255,0,0,0.8) 2px, transparent 2px, transparent 8px);
        background-size: 20px 20px; /* Scale the pattern */
        opacity: 0;
        transition: opacity 1.5s ease-in;
        animation: pulse-interference 2s infinite alternate ease-in-out; /* Subtle pulse animation */
    }

     @keyframes pulse-interference {
        0% { opacity: 0.8; }
        100% { opacity: 1; }
     }

    .dynamic-label {
        position: absolute;
        font-size: 0.9em;
        color: #004a7f; /* Dark blue text */
        white-space: nowrap;
        background-color: #ffffff;
        padding: 4px 8px;
        border: 1px solid #aaccdd;
        border-radius: 4px;
        z-index: 10; /* Above beams */
        pointer-events: none; /* Don't block clicks */
        opacity: 0;
        transition: opacity 0.5s ease-in-out;
    }
    /* Positioning for dynamic labels - place them near their components/beams */
    #label-laser { top: 55px; left: 15px; }
    #label-splitter { top: 160px; left: 210px; }
    #label-ref { top: 170px; left: 270px; }
    #label-obj-to { top: 60px; left: 350px; }
    #label-object { top: 55px; left: 540px; }
    #label-obj-from { top: 140px; left: 620px; transform: rotate(-15deg); } /* Angle slightly */
    #label-film { top: 315px; left: 500px; }
    #label-interference { top: 315px; left: 680px; color: #ff0000; font-weight: bold; } /* Highlight interference label */


    #simulate-button {
        padding: 12px 25px; /* More padding */
        font-size: 1.1em; /* Slightly larger font */
        cursor: pointer;
        background-color: #007bff; /* Primary blue */
        color: white;
        border: none;
        border-radius: 25px; /* Pill shape button */
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        font-weight: bold;
        box-shadow: 0 3px 8px rgba(0, 123, 255, 0.3);
    }

    #simulate-button:hover {
        background-color: #0056b3; /* Darker blue on hover */
        box-shadow: 0 4px 10px rgba(0, 123, 255, 0.4);
    }
     #simulate-button:active {
        transform: translateY(1px); /* Press effect */
        box-shadow: 0 2px 5px rgba(0, 123, 255, 0.2);
     }


    .explanation-toggle {
        display: block;
        width: fit-content;
        margin: 30px auto; /* More space */
        padding: 10px 20px;
        font-size: 1em;
        cursor: pointer;
        background-color: #6c757d; /* Gray */
        color: white;
        border: none;
        border-radius: 20px; /* Rounded button */
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
     .explanation-toggle:hover {
        background-color: #5a6268;
        box-shadow: 0 3px 8px rgba(0, 0, 0, 0.15);
     }
      .explanation-toggle:active {
         transform: translateY(1px);
         box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
      }


    .detailed-explanation {
        text-align: right;
        margin-top: 30px;
    }

    .detailed-explanation h2,
    .detailed-explanation h3 {
        color: #004a7f;
        margin-top: 25px;
        margin-bottom: 12px;
        border-bottom: 1px solid #aaccdd; /* Subtle separator */
        padding-bottom: 5px;
    }

    .detailed-explanation p,
    .detailed-explanation li {
        line-height: 1.7; /* More comfortable reading */
        color: #333;
    }

    .detailed-explanation ul,
    .detailed-explanation ol {
        margin-bottom: 20px;
        padding-right: 20px; /* Indent lists */
    }

     .detailed-explanation li {
         margin-bottom: 8px;
     }

     .detailed-explanation strong {
         color: #0056b3; /* Highlight key terms */
     }

    .hidden {
        display: none;
    }

    /* Animation keyframes for beam travel (example) */
    @keyframes travel-horizontal {
        0% { background-position: 0% center; }
        100% { background-position: 100% center; }
    }
     @keyframes travel-vertical {
        0% { background-position: center 0%; }
        100% { background-position: center 100%; }
    }
    @keyframes travel-diagonal-pos { /* Top-left to bottom-right */
        0% { background-position: 0% 100%; }
        100% { background-position: 100% 0%; }
    }
     @keyframes travel-diagonal-neg { /* Top-right to bottom-left */
        0% { background-position: 100% 100%; }
        100% { background-position: 0% 0%; }
    }


    /* Apply animations */
     #beam-to-splitter, #obj-beam-to-object {
         background-size: 200% 100%; /* Make gradient longer than beam */
         animation: travel-horizontal 1.5s linear infinite; /* Apply animation */
         animation-play-state: paused; /* Pause initially */
     }
     #ref-beam {
         background-size: 100% 200%;
         animation: travel-vertical 1.5s linear infinite;
         animation-play-state: paused;
     }
     #obj-beam-from-object {
          background-size: 200% 200%; /* Adjust size for diagonal */
          animation: travel-diagonal-neg 2s linear infinite; /* Choose appropriate diagonal anim */
          animation-play-state: paused;
     }


</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const simulateButton = document.getElementById('simulate-button');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('detailed-explanation');

        // Diagram elements
        const beamToSplitter = document.getElementById('beam-to-splitter');
        const refBeam = document.getElementById('ref-beam');
        const objBeamToObj = document.getElementById('obj-beam-to-object');
        const objBeamFromObj = document.getElementById('obj-beam-from-object');
        const interferencePattern = document.getElementById('interference-pattern');

         const labels = document.querySelectorAll('.dynamic-label');
         const components = document.querySelectorAll('.component');


         // Function to show a label near a component
         function showLabel(id, delay = 0) {
            const label = document.getElementById('label-' + id);
            if (label) {
                 setTimeout(() => {
                     label.style.opacity = '1';
                 }, delay);
            }
         }

         // Function to hide all labels
         function hideLabels() {
             labels.forEach(label => {
                 label.style.opacity = '0';
             });
         }


         // Reset diagram to initial state
         function resetDiagram() {
            // Stop beam animations
            beamToSplitter.style.animationPlayState = 'paused';
            refBeam.style.animationPlayState = 'paused';
            objBeamToObj.style.animationPlayState = 'paused';
            objBeamFromObj.style.animationPlayState = 'paused';

            // Reset beam sizes and opacity instantly
            beamToSplitter.style.transitionDuration = '0s';
            refBeam.style.transitionDuration = '0s';
            objBeamToObj.style.transitionDuration = '0s';
            objBeamFromObj.style.transitionDuration = '0s';

            beamToSplitter.style.width = '0px'; beamToSplitter.style.opacity = '0';
            refBeam.style.height = '0px'; refBeam.style.opacity = '0';
            objBeamToObj.style.width = '0px'; objBeamToObj.style.opacity = '0';
            objBeamFromObj.style.height = '0px'; objBeamFromObj.style.opacity = '0';

            // Reset interference pattern
            interferencePattern.style.opacity = '0';
            interferencePattern.classList.add('hidden'); // Hide until needed


             // Reset transition duration for next animation
             setTimeout(() => {
                 beamToSplitter.style.transitionDuration = '1.5s';
                 refBeam.style.transitionDuration = '1.5s';
                 objBeamToObj.style.transitionDuration = '1.5s';
                 objBeamFromObj.style.transitionDuration = '1.5s';
             }, 50);

            // Hide labels
            hideLabels();
         }

        // Simulation sequence
        simulateButton.addEventListener('click', () => {
            simulateButton.disabled = true; // Disable button during animation
            resetDiagram(); // Start fresh

            const duration1 = 1500; // Laser to splitter
            const duration2 = 1500; // Splitter to object/film
            const duration3 = 1500; // Object to film
            const duration4 = 1500; // Interference buildup


            // Step 1: Laser to Splitter
            setTimeout(() => {
                 showLabel('laser', 0);
                beamToSplitter.style.width = '205px'; // Distance to splitter center minus half splitter width
                beamToSplitter.style.opacity = '1';
                beamToSplitter.style.animationPlayState = 'running'; // Start animation
                showLabel('splitter', duration1 * 0.8); // Show splitter label near end of travel
            }, 100);

            // Step 2: Beams split and travel
            setTimeout(() => {
                 beamToSplitter.style.animationPlayState = 'paused'; // Pause animation at destination

                // Reference Beam
                refBeam.style.height = '187.5px'; // Distance from splitter center to film center vertically
                 refBeam.style.opacity = '1';
                 refBeam.style.animationPlayState = 'running'; // Start animation
                 showLabel('ref', 0); // Show ref beam label immediately

                // Object Beam
                objBeamToObj.style.width = '272.5px'; // Distance from splitter center to object center
                 objBeamToObj.style.opacity = '1';
                 objBeamToObj.style.animationPlayState = 'running'; // Start animation
                 showLabel('obj-to', 0); // Show obj beam label immediately

                 showLabel('object', duration2 * 0.8); // Show object label near end of travel

            }, 100 + duration1); // After beam reaches splitter

             // Step 3: Object beam reflects/scatters
             setTimeout(() => {
                  refBeam.style.animationPlayState = 'paused'; // Pause animation at film
                  objBeamToObj.style.animationPlayState = 'paused'; // Pause animation at object

                  showLabel('film', 0); // Show film label immediately

                 // Object beam from object to film (Diagonal)
                 // Calculate endpoint relative to diagram, then figure out length and angle
                 const objX = 565; // Object center X
                 const objY = 92.5; // Object center Y
                 const filmX = 595; // Film center X
                 const filmY = 292.5; // Film center Y

                 const dx = filmX - objX;
                 const dy = filmY - objY;
                 const distance = Math.sqrt(dx*dx + dy*dy);
                 const angle = Math.atan2(dy, dx) * 180 / Math.PI;

                 objBeamFromObj.style.left = objX + 'px';
                 objBeamFromObj.style.top = objY + 'px';
                 objBeamFromObj.style.transform = `rotate(${angle}deg)`;
                 objBeamFromObj.style.transformOrigin = 'top left';
                 objBeamFromObj.style.width = distance + 'px'; // Use width for diagonal length
                 objBeamFromObj.style.height = '4px'; // Keep height for thickness
                 objBeamFromObj.style.opacity = '1';
                 // Adjust animation direction based on angle if needed, currently using travel-diagonal-neg
                  objBeamFromObj.style.animationPlayState = 'running'; // Start animation
                  showLabel('obj-from', 0); // Show obj beam from label immediately


             }, 100 + duration1 + duration2); // After obj beam reaches object

             // Step 4: Interference happens on film
             setTimeout(() => {
                 refBeam.style.animationPlayState = 'paused'; // Ensure paused
                 objBeamFromObj.style.animationPlayState = 'paused'; // Ensure paused

                 interferencePattern.classList.remove('hidden');
                 interferencePattern.style.opacity = '1'; // Fade in interference pattern
                 showLabel('interference', duration4 * 0.5); // Show interference label mid-fade
                 simulateButton.disabled = false; // Re-enable button
             }, 100 + duration1 + duration2 + duration3); // After beams meet on film

        });

         // Initial reset
         resetDiagram();


        // Toggle explanation visibility
        toggleExplanationButton.addEventListener('click', () => {
            explanationDiv.classList.toggle('hidden');
            if (explanationDiv.classList.contains('hidden')) {
                toggleExplanationButton.textContent = 'רוצים לדעת איך זה קורה? לחצו כאן להסבר המלא';
            } else {
                toggleExplanationButton.textContent = 'הסתר הסבר מפורט';
            }
        });

         // Optional: Show labels on hover over components (alternative to animation)
         // components.forEach(comp => {
         //     const labelId = comp.id.replace('-', ''); // e.g. laser -> laser
         //      const label = document.getElementById('label-' + labelId);
         //      if (label) {
         //          comp.addEventListener('mouseover', () => { label.style.opacity = '1'; });
         //          comp.addEventListener('mouseout', () => {
         //              // Only hide if simulation is not running
         //              if (!simulateButton.disabled) {
         //                  label.style.opacity = '0';
         //              }
         //          });
         //      }
         // });

    });
</script>
```