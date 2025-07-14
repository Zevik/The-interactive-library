---
title: "מסע בזמן: האבולוציה המרתקת של כלי הניתוח"
english_slug: captivating-journey-the-evolution-of-surgical-tools
category: "רפואה"
tags:
  - היסטוריה
  - רפואה
  - ניתוח
  - טכנולוגיה רפואית
  - כירורגיה
  - סימולציה
---
<h1>מסע בזמן: האבולוציה המרתקת של כלי הניתוח</h1>
<p>הצטרפו אלינו למסע מרתק אל העבר הרפואי! האם דמיינתם פעם עם אילו כלים התמודדו רופאים לפני מאות או אלפי שנים כשהם ניסו להציל חיים? כיצד חפצים יומיומיים הפכו לכלי הצלת חיים מדויקים? בואו לגלות כיצד כלי הניתוח התפתחו מחפצים פרימיטיביים אל הפלא הטכנולוגי של ימינו, וכיצד התפתחות זו שינתה את גבולות הרפואה האפשרית.</p>

<div class="simulation-container">
    <h2>התנסות: סגירת חתך בזמן</h2>
    <p class="sim-intro">בחרו תקופה היסטורית, התנסו בשימוש בכלים האופייניים לה ונסו לתקן חתך בעור. האם תצליחו להתגבר על האתגרים שמציגה כל תקופה?</p>

    <div class="era-selector">
        <label for="era-select">בחרו תקופת זמן למסע:</label>
        <select id="era-select">
            <option value="ancient">העת העתיקה (כלי אבן/ברונזה)</option>
            <option value="medieval">ימי הביניים (ברזל גס)</option>
            <option value="early-modern">תחילת העת החדשה (פלדה פשוטה)</option>
            <option value="19th-century">המאה ה-19 (עידן הסטריליזציה)</option>
            <option value="20th-century">המאה ה-20 (נירוסטה והתמחות)</option>
            <option value="modern">ימינו (טכנולוגיה עלית)</option>
        </select>
    </div>

    <div class="simulation-area">
        <div class="patient-area" id="patient-area">
            <div class="wound">
                 <div class="cut-edge left-edge"></div>
                 <div class="cut-edge right-edge"></div>
            </div>
             <div class="wound-overlay" id="wound-overlay">
                  <!-- Damage/Suture markers go here -->
             </div>
        </div>
        <div class="tools-area" id="tools-area">
            <!-- Tools will be loaded here by JS -->
        </div>
    </div>

    <div class="simulation-feedback" id="simulation-feedback">
        <!-- Feedback will be displayed here -->
    </div>
     <div class="simulation-stats">
         <span id="suture-count">תפרים: 0 / --</span>
         <span id="damage-count">נזק מצטבר: 0</span>
     </div>
    <button id="reset-sim">התחלה מחדש של הסימולציה</button>
</div>

<button id="toggle-explanation">הצג/הסתר את הסיפור המלא מאחורי הכלים</button>

<div id="explanation" style="display: none;">
    <h3>היסטוריה של כלי הניתוח - הסיפור המלא</h3>
    <p>כלי הניתוח הם הגיבורים השקטים בהיסטוריה של הרפואה. התפתחותם אינה רק סיפור טכנולוגי, אלא שיקוף מרתק של האופן בו האנושות הבינה את הגוף, התמודדה עם מחלות ופציעות, ודחפה את גבולות האפשרי.</p>

    <h4>העת העתיקה: כלים מהטבע והתמודדות עם הישרדות</h4>
    <p>בתקופות הקדומות ביותר, כירורגיה הייתה לרוב פרוצדורה של חירום, מוגבלת לטיפול בפציעות גלויות כמו שברי גולגולת (יש עדויות לניתוחי טרפנציה - קדיחת חורים בגולגולת) או קטיעות גפיים בעקבות טראומה. הכלים היו פשוטים: אזמלים, סכינים ומסורים עשויים אבן מחודדת (צור, אובסידיאן) או מתכות פרימיטיביות כמו ברונזה. כלים אלו היו גסים, קשים להחזקה, וגרמו לנזק רב לרקמות הסובבות את אזור הטיפול. היעדר מוחלט של ידע על חיידקים או סטריליזציה הפך כל פתיחת עור לפעולה בעלת סיכון אדיר לזיהום קטלני. מלקחי ברונזה למשל, שימשו בעיקר לשליפת חפצים זרים או שברי עצמות מפצעים.</p>

    <h4>ימי הביניים ותחילת העת החדשה: בין דם לדת</h4>
    <p>תקופת ימי הביניים ראתה שיפור הדרגתי באיכות המתכות (ברזל, פלדה פשוטה), אך הכלים נותרו דומים בעיצובם לבסיס העתיק. בתקופה זו, גילדות הסַפָּּרים-מנתחים היו הכוח העיקרי שעסק בפרוצדורות חיצוניות כמו הקזת דם, קטיעות, וטיפול בפצעים. הידע האנטומי היה חלקי, ומושג הסטריליזציה עדיין לא היה קיים. כלים כמו מלקחי כדורים נהיו רלוונטיים במיוחד בשל פציעות קרב הולכות וגוברות. תקופה זו התאפיינה בשיעורי תמותה גבוהים להחריד לאחר ניתוחים, שהיו לרוב מוצא אחרון נואש.</p>

    <h4>המאה ה-19: מהפכה תעשייתית ומהפכת הסטריליזציה</h4>
    <p>המאה ה-19 היא תקופת מפנה דרמטי. שני גילויים מדעיים שינו את פני הכירורגיה לנצח: פיתוח חומרי הרדמה יעילים (אתר, כלורופורם), שאיפשרו למנתחים לעבוד לאט ומדויק יותר על חולים שקטים וללא כאב, וגילוי עקרונות האנטיספטיקה והסטריליזציה על ידי ג'וזף ליסטר ולואי פסטר. לפתע, ניתן היה להפחית דרמטית את הסיכון לזיהום. במקביל, המהפכה התעשייתית איפשרה ייצור המוני של כלי פלדה איכותיים יותר, חדים יותר, ועמידים יותר. כלים עוצבו מחדש כך שיהיו קלים יותר לניקוי ועיקור. השילוב של הרדמה, סטריליזציה וכלים משופרים פתח את הדלת לפרוצדורות כירורגיות מורכבות הרבה יותר, בתוך חללי הגוף הפנימיים.</p>

    <h4>המאה ה-20: התמחות, נירוסטה ופיתוחים טכנולוגיים</h4>
    <p>עם התקדמות הידע הרפואי, הכירורגיה הפכה למתמחה יותר ויותר (כירורגיית לב-חזה, נוירוכירורגיה, אורתופדיה וכו'). כלים ייעודיים ומורכבים פותחו כדי לענות על צרכי ההתמחויות השונות. המעבר מפלדה לנירוסטה (פלדת אל-חלד) איפשרה כלי ניתוח עמידים יותר בפני קורוזיה וקלים יותר לניקוי ועיקור חוזרים. התפתחות טכניקות הדמיה כמו צילום רנטגן ובהמשך CT ו-MRI, השפיעה גם היא על הצורך בכלים שיכולים לפעול בהנחיית הדמיה. פיתוח האנדוסקופיה הראשונית (כלי המאפשר הצצה לחללי גוף פנימיים) היה צעד ראשון לקראת כירורגיה פולשנית מינימלית.</p>

    <h4>סוף המאה ה-20 ועד היום: המהפכה הזעיר-פולשנית והעידן הדיגיטלי</h4>
    <p>העשורים האחרונים עומדים בסימן מהפכה של ממש: כירורגיה פולשנית מינימלית (Minimal Invasive Surgery - MIS), בעיקר לפרוסקופיה ואנדוסקופיה. במקום פתיחת חתכים גדולים, ניתוחים רבים מבוצעים היום דרך חתכים קטנים ביותר באמצעות כלים ארוכים ודקים המחוברים למצלמה. הדבר דורש סטים חדשים לחלוטין של כלים. בנוסף, טכנולוגיות עילית נכנסו לחדר הניתוח: כירורגיה רובוטית (כמו מערכת דה וינצ'י) המאפשרת למנתח לשלוט בכלים מדויקים ביותר באמצעות קונסולה, לעיתים אף מרחוק; שימוש בלייזר לחיתוך וצריבה מדויקים; מערכות ניווט תוך-ניתוחיות המונחות הדמיה; ושימוש גובר בטכניקות הדמיה מתקדמות תוך כדי הניתוח.</p>

    <h4>מבט לעתיד: חכמים, מחוברים ומותאמים אישית</h4>
    <p>העתיד מבטיח להמשיך את קצב החדשנות המסחרר. אנו צפויים לראות כלים "חכמים" עם חיישנים מובנים המספקים מידע למנתח בזמן אמת, שילוב מציאות רבודה (AR) להקרנת מידע על שדה הניתוח, שימוש בהדפסת תלת-ממד ליצירת כלי ניתוח או שתלים מותאמים אישית לחולה, ושילוב עמוק יותר של בינה מלאכותית בתכנון הניתוח ובהנחיית הרובוטים. כל זאת במטרה להפוך ניתוחים לבטוחים יותר, מדויקים יותר, ולהפחית את זמן ההחלמה של המטופל.</p>
</div>

<style>
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.7;
        direction: rtl;
        text-align: right;
        margin: 0;
        padding: 20px;
        background-color: #f4f7f6; /* Soft background */
        color: #333;
    }

    h1, h2, h3, h4 {
        color: #004085; /* Deep blue */
        margin-bottom: 10px;
    }

    p {
        margin-bottom: 15px;
    }

    .simulation-container {
        border: 1px solid #b8daff; /* Light blue border */
        padding: 25px;
        margin: 25px 0;
        background-color: #e9f5ff; /* Very light blue */
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .sim-intro {
        font-style: italic;
        color: #5a6268; /* Greyish */
        margin-top: -10px;
        margin-bottom: 20px;
    }

    .era-selector {
        margin-bottom: 25px;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .era-selector label {
         font-weight: bold;
         margin-bottom: 8px;
         color: #004085;
    }

    .era-selector select {
        padding: 10px 15px;
        font-size: 1em;
        border: 1px solid #007bff;
        border-radius: 5px;
        background-color: #fff;
        cursor: pointer;
        outline: none;
        transition: border-color 0.3s ease;
        min-width: 200px; /* Ensure dropdown is wide enough */
    }

     .era-selector select:focus {
         border-color: #0056b3;
         box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
     }


    .simulation-area {
        display: flex;
        flex-direction: column; /* Stack on small screens */
        gap: 20px;
        justify-content: center;
        align-items: center; /* Center vertically */
    }

     @media (min-width: 768px) { /* Switch to side-by-side on larger screens */
        .simulation-area {
            flex-direction: row-reverse; /* Tools on left, patient on right */
            align-items: flex-start; /* Align items to the top */
        }
         .tools-area {
             min-width: 180px; /* More space for tools */
             max-width: 250px;
         }
     }


    .patient-area {
        position: relative;
        width: 100%; /* Flexible width */
        max-width: 400px; /* Max width for larger screens */
        height: 200px; /* Fixed height */
        border: 2px solid #8d6e63; /* Skin tone border */
        background-color: #ffe0b2; /* Skin tone color */
        overflow: hidden;
        border-radius: 10px;
        flex-shrink: 0;
        margin-bottom: 20px; /* Space below patient area on small screens */
         cursor: crosshair; /* Indicate clickability */
         box-shadow: inset 0 0 15px rgba(141, 110, 99, 0.3); /* Inner shadow for depth */
    }
     @media (min-width: 768px) {
          .patient-area {
               margin-bottom: 0; /* Remove bottom margin when side-by-side */
          }
     }


    .wound {
         position: absolute;
         top: 50%;
         left: 10%;
         width: 80%;
         height: 10px; /* Height representing the open cut */
         transform: translateY(-50%);
         display: flex;
         justify-content: center;
         align-items: center;
         pointer-events: none; /* Wound itself isn't interactive */
         z-index: 1;
    }

    .cut-edge {
        width: 50%;
        height: 100%;
        background-color: #c62828; /* Dark red representing muscle/blood */
        transition: margin 0.5s ease-out; /* Animation for closing */
    }

    .left-edge {
        margin-right: 5px; /* Initial gap */
        border-top-left-radius: 5px;
        border-bottom-left-radius: 5px;
    }

     .right-edge {
        margin-left: 5px; /* Initial gap */
         border-top-right-radius: 5px;
        border-bottom-right-radius: 5px;
    }

    .wound-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 2; /* Overlay for interaction points */
    }


    .tools-area {
        width: 100%; /* Full width on small screens */
        border-top: 1px solid #eee; /* Separator on small screens */
        padding-top: 10px;
        display: flex;
        flex-direction: column;
        gap: 8px; /* Reduced gap */
        align-items: stretch; /* Stretch items */
    }
     @media (min-width: 768px) {
        .tools-area {
             border-top: none;
             border-right: 1px solid #eee; /* Separator on larger screens */
             padding-top: 0;
             padding-right: 10px;
        }
     }


    .tool {
        padding: 12px 15px; /* More padding */
        border: 1px solid #cce5ff; /* Light blue border */
        background-color: #ffffff; /* White background */
        cursor: pointer;
        border-radius: 6px; /* Slightly more rounded */
        width: 100%; /* Full width */
        text-align: center;
        user-select: none;
        transition: transform 0.1s ease-in-out, background-color 0.2s ease, border-color 0.2s ease;
        font-size: 0.95em;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }

    .tool:hover {
        background-color: #e9f5ff; /* Lighter blue on hover */
        border-color: #a6d1f5;
    }

    .tool.selected {
        border-color: #007bff; /* Primary blue */
        background-color: #cce5ff; /* Lightest blue for selected */
        box-shadow: 0 3px 6px rgba(0, 123, 255, 0.2);
        transform: translateY(-2px); /* Slight lift */
    }

     /* Styles for simulation elements (e.g., sutures, damage) */
     .marker {
         position: absolute;
         transform: translate(-50%, -50%); /* Center point at location */
         z-index: 3;
         pointer-events: none; /* Markers are not interactive */
         opacity: 0; /* Start hidden for animation */
         animation: fade-in 0.5s forwards;
     }

     @keyframes fade-in {
         to { opacity: 1; }
     }


    .suture {
        width: 12px; /* Size of a suture point */
        height: 12px;
        background-color: #007bff; /* Blue */
        border-radius: 50%;
        border: 2px solid #0056b3;
        box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
        animation: pop-in 0.3s ease-out forwards;
     }

      @keyframes pop-in {
          0% { transform: translate(-50%, -50%) scale(0.5); opacity: 0.5; }
          80% { transform: translate(-50%, -50%) scale(1.1); opacity: 1; }
          100% { transform: translate(-50%, -50%) scale(1); opacity: 1; }
      }

     .suture-line { /* Visual line connecting suture points if needed (more complex JS) */
         /* Not implementing line connecting for simplicity now, just points */
     }


    .damage {
        width: 25px; /* Size of a damage point */
        height: 25px;
        background-color: rgba(220, 53, 69, 0.6); /* Semi-transparent red */
        border-radius: 50%;
        border: 2px solid #a71d2a;
        box-shadow: 0 0 8px rgba(220, 53, 69, 0.8);
         animation: pulse 1s infinite alternate, fade-in 0.5s forwards; /* Add pulse effect */
     }

     @keyframes pulse {
         from { transform: translate(-50%, -50%) scale(1); opacity: 0.8; }
         to { transform: translate(-50%, -50%) scale(1.1); opacity: 1; }
     }


    .simulation-feedback {
        margin-top: 20px;
        padding: 15px;
        text-align: center;
        font-weight: bold;
        min-height: 1.5em; /* Reserve space */
        border-radius: 6px;
        background-color: #fff3cd; /* Warning yellow background */
        color: #856404; /* Warning yellow text */
        border: 1px solid #ffeeba;
        transition: all 0.5s ease;
    }

     .simulation-feedback.success {
         background-color: #d4edda; /* Success green */
         color: #155724;
         border-color: #c3e6cb;
     }

      .simulation-feedback.failure {
         background-color: #f8d7da; /* Danger red */
         color: #721c24;
         border-color: #f5c6cb;
     }


     .simulation-stats {
         margin-top: 15px;
         text-align: center;
         font-size: 1em;
         color: #555;
     }

     .simulation-stats span {
         margin: 0 15px;
         font-weight: bold;
     }


    #reset-sim {
        display: block;
        margin: 20px auto 0;
        padding: 12px 25px;
        font-size: 1em;
        cursor: pointer;
        background-color: #ffc107; /* Warning button */
        color: #212529;
        border: none;
        border-radius: 5px;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }
    #reset-sim:hover {
         background-color: #e0a800;
         transform: translateY(-1px);
    }
     #reset-sim:active {
          transform: translateY(0);
     }


    #toggle-explanation {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        font-size: 1em;
        cursor: pointer;
        background-color: #007bff; /* Primary button */
        color: white;
        border: none;
        border-radius: 5px;
         transition: background-color 0.3s ease, transform 0.1s ease;
    }
     #toggle-explanation:hover {
         background-color: #0056b3;
         transform: translateY(-1px);
     }
      #toggle-explanation:active {
           transform: translateY(0);
      }


    #explanation {
        margin-top: 20px;
        padding: 20px;
        border: 1px solid #b8daff;
        background-color: #e9f5ff; /* Same as sim container */
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
         transition: all 0.5s ease; /* Smooth toggle */
    }

    #explanation h3 {
        margin-top: 0;
        border-bottom: 2px solid #007bff; /* Separator */
        padding-bottom: 5px;
        margin-bottom: 15px;
    }

    #explanation h4 {
        margin-bottom: 8px;
        color: #0056b3; /* Slightly darker blue */
        font-weight: bold;
    }
</style>

<script>
    const eras = {
        ancient: {
            name: "העת העתיקה",
            tools: [
                { name: "סכין אבן גסה", type: "damage", precision: 0.1, baseEffect: 30, description: "טובה לחיתוך, גורמת לנזק רב ללא דיוק." },
                { name: "מחט עצם", type: "suture", precision: 0.15, baseEffect: 40, description: "פרימיטיבית ושבירה, קשה לתפור ביעילות." }
            ],
            description: "כלים גסים, דיוק נמוך, סיכון אדיר לזיהום ונזק רקמה.",
            suturePointsNeeded: 5, // Fewer points needed, representing crude closure
            damageTolerance: 80 // Low tolerance before failure
        },
        medieval: {
            name: "ימי הביניים",
            tools: [
                 { name: "אזמל ברזל", type: "damage", precision: 0.2, baseEffect: 25, description: "חד יותר מאבן, עדיין כבד וקשה לשליטה." },
                { name: "מחט ברזל גסה", type: "suture", precision: 0.3, baseEffect: 35, description: "עמידה יותר מעצם, עדיין גסה וקשה לעבודה עדינה." }
            ],
            description: "חומרים טובים יותר, אך טכניקה וכלים עדיין רחוקים מדיוק.",
            suturePointsNeeded: 7,
            damageTolerance: 120
        },
        'early-modern': {
            name: "תחילת העת החדשה",
            tools: [
                 { name: "אזמל פלדה פשוט", type: "damage", precision: 0.3, baseEffect: 20, description: "פלדה משפרת את החדות, אך עדיין חסר דיוק אמיתי." },
                { name: "מחט פלדה", type: "suture", precision: 0.4, baseEffect: 30, description: "מחט חזקה יותר, מאפשרת קצת יותר שליטה." }
            ],
            description: "הפלדה נכנסת לשימוש, הכלים מעודנים יותר, אך הסטריליזציה עדיין חסרה.",
             suturePointsNeeded: 9,
            damageTolerance: 150
        },
        '19th-century': {
            name: "המאה ה-19 (עידן הסטריליזציה)",
            tools: [
                 { name: "אזמל פלדה מעודן", type: "damage", precision: 0.6, baseEffect: 15, description: "פלדה איכותית מאפשרת חיתוך מדויק יותר, אך השימוש הכירורגי בו שונה מתיקון." },
                { name: "מחט פלדה דקה (עקרה)", type: "suture", precision: 0.7, baseEffect: 20, description: "סטריליזציה ודיוק משפרים דרמטית את הסיכוי לתפור בהצלחה." }
            ],
            description: "מהפכת הסטריליזציה והרדמה לצד פלדה איכותית - קפיצת מדרגה אדירה.",
            suturePointsNeeded: 12,
            damageTolerance: 250 // Higher tolerance due to sterility reducing infection damage
        },
        '20th-century': {
            name: "המאה ה-20",
             tools: [
                 { name: "אזמל נירוסטה", type: "damage", precision: 0.8, baseEffect: 10, description: "נירוסטה עמידה בפני חלודה וקלה לעיקור, מדויקת מאד." },
                { name: "מחט נירוסטה עדינה", type: "suture", precision: 0.85, baseEffect: 15, description: "כלים מנירוסטה מאפשרים עבודה עדינה ומדויקת יותר." }
            ],
            description: "נירוסטה הופכת לסטנדרט, התמחות גוברת, וכלים ייעודיים רבים.",
            suturePointsNeeded: 15,
            damageTolerance: 350
        },
        modern: {
            name: "ימינו",
             tools: [
                 { name: "אזמל מיקרו-כירורגי (מייצג)", type: "damage", precision: 0.95, baseEffect: 5, description: "דיוק מירבי, נזק מינימלי, אך לא הכלי לסגירה." },
                { name: "כלי סגירה מדויקים", type: "suture", precision: 0.98, baseEffect: 10, description: "רובוטיקה, לייזר, וכלים מינימליים - דיוק כמעט מושלם." }
            ],
            description: "כירורגיה זעיר-פולשנית, רובוטיקה, דיוק על-אנושי, נזק מזערי ותוצאות טובות.",
            suturePointsNeeded: 20, // More points for fine closure
            damageTolerance: 500 // Very high tolerance due to precision and minimal invasiveness
        }
    };

    let selectedTool = null;
    let currentEra = 'ancient';
    let suturesPlaced = 0;
    let totalDamage = 0;
    let simActive = true;

    const eraSelect = document.getElementById('era-select');
    const toolsArea = document.getElementById('tools-area');
    const woundOverlay = document.getElementById('wound-overlay');
    const patientArea = document.getElementById('patient-area');
    const feedbackArea = document.getElementById('simulation-feedback');
    const resetButton = document.getElementById('reset-sim');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const sutureCountSpan = document.getElementById('suture-count');
    const damageCountSpan = document.getElementById('damage-count');
    const leftCutEdge = document.querySelector('.left-edge');
    const rightCutEdge = document.querySelector('.right-edge');


    // Event Listeners
    eraSelect.addEventListener('change', changeEra);
    woundOverlay.addEventListener('click', handleSimulationClick);
    resetButton.addEventListener('click', resetSimulation);
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר את הסיפור המלא' : 'הצג/הסתר את הסיפור המלא מאחורי הכלים';
    });

    // Initialize simulation
    loadTools(currentEra);
    updateStatsDisplay();
    updateFeedback(`ברוכים הבאים למסע בזמן! בחרו תקופה וכלי ניתוח לתיקון החתך.`);
    setWoundAppearance(eras[currentEra]);


    function loadTools(eraKey) {
        toolsArea.innerHTML = '';
        selectedTool = null; // Deselect tool on era change
        eras[eraKey].tools.forEach(tool => {
            const toolDiv = document.createElement('div');
            toolDiv.classList.add('tool');
            toolDiv.textContent = tool.name;
            toolDiv.title = tool.description; // Add tooltip for description
            toolDiv.dataset.type = tool.type;
            toolDiv.dataset.precision = tool.precision;
            toolDiv.dataset.baseEffect = tool.baseEffect;
            toolDiv.addEventListener('click', selectTool);
            toolsArea.appendChild(toolDiv);
        });
    }

    function selectTool(event) {
        if (!simActive) return;
        // Remove 'selected' class from all tools
        toolsArea.querySelectorAll('.tool').forEach(tool => tool.classList.remove('selected'));

        // Select the clicked tool
        event.target.classList.add('selected');
        selectedTool = {
            name: event.target.textContent,
            type: event.target.dataset.type,
            precision: parseFloat(event.target.dataset.precision),
            baseEffect: parseFloat(event.target.dataset.baseEffect)
        };
         updateFeedback(`כלי נבחר: ${selectedTool.name}. ${selectedTool.description}`);
    }

    function handleSimulationClick(event) {
        if (!simActive) return;
        if (!selectedTool) {
            updateFeedback("אנא בחרו כלי ניתוח תחילה כדי לבצע פעולה.");
            return;
        }

        // Get click position relative to the patient area
        const rect = patientArea.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;

        // Check if click is near the cut line (simplified check)
        // Assuming the cut line is roughly in the middle vertically and spans 80% horizontally
        const cutLineY = patientArea.offsetHeight / 2;
        const cutLineStartX = patientArea.offsetWidth * 0.1;
        const cutLineEndX = patientArea.offsetWidth * 0.9;
        const distanceToCutCenterY = Math.abs(y - cutLineY);
        const clickIsNearCutY = distanceToCutCenterY < 20; // Vertical tolerance
        const clickIsWithinCutX = x >= cutLineStartX && x <= cutLineEndX; // Horizontal range

        const clickIsNearCut = clickIsNearCutY && clickIsWithinCutX;


        let outcomeMessage = "";

        if (selectedTool.type === 'suture') {
            if (clickIsNearCut) {
                 const successProb = selectedTool.precision; // Probability of successful suture placement
                 const potentialDamage = selectedTool.baseEffect * (1 - selectedTool.precision); // Damage related to imprecision

                 if (Math.random() < successProb) {
                     // Successful suture placement
                     addMarker(x, y, 'suture');
                     suturesPlaced++;
                      totalDamage += potentialDamage * 0.5; // Minimal damage even on success
                     outcomeMessage = `תפר הונח בהצלחה! (${(successProb*100).toFixed(0)}% סיכוי עם כלי זה).`;
                 } else {
                     // Failed suture placement (e.g., slipped, broke)
                     totalDamage += selectedTool.baseEffect * (1 + (1-selectedTool.precision)); // More damage on failure
                     addMarker(x, y, 'damage', totalDamage); // Add visual damage marker
                     outcomeMessage = `ניסיון תפירה כושל! (${((1-successProb)*100).toFixed(0)}% סיכוי כשל). נגרם נזק נוסף.`;
                 }
            } else {
                // Clicking with suture tool away from the cut
                 totalDamage += selectedTool.baseEffect * 0.8; // Damage for misapplication
                 addMarker(x, y, 'damage', totalDamage); // Add visual damage marker
                 outcomeMessage = `ניסית לתפור מחוץ לחתך! נגרם נזק לרקמה.`;
            }
        } else if (selectedTool.type === 'damage') { // This tool type is for things that *should* cause damage if misused for repair
             const damageAmount = selectedTool.baseEffect * (1 + (1-selectedTool.precision)); // Damage related to tool nature and imprecision
             totalDamage += damageAmount;
             addMarker(x, y, 'damage', totalDamage); // Add visual damage marker
             outcomeMessage = `זה כלי לחיתוך/גרימה, לא לתיקון! נגרם נזק משמעותי לרקמה.`;
        }

        updateStatsDisplay();
        checkSimulationStatus(outcomeMessage);
    }

    function addMarker(x, y, type, damageValue = 0) {
        const marker = document.createElement('div');
        marker.classList.add('marker', type);
        marker.style.left = `${x}px`;
        marker.style.top = `${y}px`;

        if (type === 'damage') {
             // Optional: Scale damage marker size based on the individual damage caused, not totalDamage
            const size = Math.max(15, Math.min(40, damageValue / 15)); // Scale based on impact
             marker.style.width = `${size}px`;
             marker.style.height = `${size}px`;
        }

        woundOverlay.appendChild(marker);

         // Optional: Remove old markers after a while to avoid clutter
         if (type === 'damage') {
             setTimeout(() => {
                 marker.remove();
             }, 3000); // Remove damage markers after 3 seconds
         }
    }

    function updateStatsDisplay() {
         const currentEraData = eras[currentEra];
        sutureCountSpan.textContent = `תפרים: ${suturesPlaced} / ${currentEraData.suturePointsNeeded}`;
        damageCountSpan.textContent = `נזק מצטבר: ${totalDamage.toFixed(0)} / ${currentEraData.damageTolerance}`;
    }

    function checkSimulationStatus(latestOutcomeMessage) {
        const currentEraData = eras[currentEra];

         // Update wound visual based on sutures placed
         const sutureProgress = suturesPlaced / currentEraData.suturePointsNeeded;
         const gap = Math.max(0, 5 - (sutureProgress * 5)); // Reduce gap from 5px to 0
         leftCutEdge.style.marginRight = `${gap}px`;
         rightCutEdge.style.marginLeft = `${gap}px`;


        if (totalDamage >= currentEraData.damageTolerance) {
            updateFeedback(`הניתוח נכשל! 😢 נגרם נזק רב מדי לרקמה בתנאי תקופת ${currentEraData.name} (${totalDamage.toFixed(0)}/${currentEraData.damageTolerance}). קשה להצליח עם כלים פרימיטיביים/ללא סטריליזציה!`, 'failure');
            simActive = false;
            // Prevent further interaction
            woundOverlay.style.pointerEvents = 'none';
             toolsArea.style.pointerEvents = 'none';
             toolsArea.querySelectorAll('.tool').forEach(tool => tool.classList.remove('selected')); // Deselect
             selectedTool = null;

        } else if (suturesPlaced >= currentEraData.suturePointsNeeded) {
            updateFeedback(`הניתוח הצליח! 🎉 החתך נסגר בהצלחה בתנאי תקופת ${currentEraData.name}. נזק מינימלי נגרם (${totalDamage.toFixed(0)}/${currentEraData.damageTolerance}). היכולת לשלוט בנזק תלויה מאד בכלים!`, 'success');
            simActive = false;
             // Prevent further interaction
            woundOverlay.style.pointerEvents = 'none';
             toolsArea.style.pointerEvents = 'none';
             toolsArea.querySelectorAll('.tool').forEach(tool => tool.classList.remove('selected')); // Deselect
             selectedTool = null;
        } else {
             // Simulation is still active, display the latest outcome message
             updateFeedback(latestOutcomeMessage + ` נותרו לתיקון: ${currentEraData.suturePointsNeeded - suturesPlaced}.`);
        }
    }

     function updateFeedback(message, type = 'info') {
        feedbackArea.textContent = message;
        feedbackArea.className = 'simulation-feedback'; // Reset classes
         if (type === 'success') {
             feedbackArea.classList.add('success');
         } else if (type === 'failure') {
             feedbackArea.classList.add('failure');
         } else {
              feedbackArea.classList.add('info'); // Default class
         }
    }

    function changeEra() {
        currentEra = eraSelect.value;
        resetSimulation(); // Reset simulation state for the new era
        loadTools(currentEra);
        setWoundAppearance(eras[currentEra]);
        updateStatsDisplay();
        updateFeedback(`תקופה נבחרה: ${eras[currentEra].name}. ${eras[currentEra].description} נסו לסגור את החתך באמצעות הכלים הזמינים. נותרו לתיקון: ${eras[currentEra].suturePointsNeeded}`);
    }

    function resetSimulation() {
        suturesPlaced = 0;
        totalDamage = 0;
        simActive = true;
        // Clear all markers
        woundOverlay.innerHTML = '';
        selectedTool = null;
         // Deselect all tools
        toolsArea.querySelectorAll('.tool').forEach(tool => tool.classList.remove('selected'));
        updateStatsDisplay();
         updateFeedback(`הסימולציה אופסה לתקופת ${eras[currentEra].name}. בחרו כלי ניתוח כדי להתחיל.`);
         // Re-enable interaction
         woundOverlay.style.pointerEvents = 'auto';
         toolsArea.style.pointerEvents = 'auto';
         setWoundAppearance(eras[currentEra]); // Reset wound visual
    }

     function setWoundAppearance(eraData) {
          // For now, this just resets the gap. Could potentially add visual changes
          // like more redness/swelling for older eras.
         leftCutEdge.style.marginRight = '5px';
         rightCutEdge.style.marginLeft = '5px';
     }


</script>