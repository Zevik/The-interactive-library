---
title: "לנהל את הזמן כמו נשיא: משחק מטריצת אייזנהאואר"
english_slug: manage-time-like-a-president-eisenhower-matrix-game
category: "פסיכולוגיה"
tags: [ניהול זמן, מטריצת אייזנהאואר, פרודוקטיביות, קבלת החלטות, ארגון אישי]
---
# לשלוט בזמן שלך: משחק מטריצת אייזנהאואר האינטראקטיבי

האם אתם מרגישים כמו כדור פינג-פונג שמוקפץ בין משימות דחופות? שהיום שלכם נשלט על ידי משברים קטנים במקום להתקדם לדברים החשובים באמת? ברוכים הבאים לעולם המטורף של ניהול זמן ללא סדר עדיפויות. אבל אל דאגה, יש דרך טובה יותר – הדרך של הנשיא דווייט ד. אייזנהאואר, שהבין שסדר עדיפויות הוא המפתח לאפקטיביות, לא רק לעבודה קשה.

בואו נשחק קצת. לפניכם רשימה של משימות שגרתיות (או פחות שגרתיות) מחיי היום-יום או העולם העסקי. המשימה שלכם היא לגרור כל משימה לריבוע המתאים לה במטריצת אייזנהאואר, על פי מידת *הדחיפות* ו*החשיבות* שלה. כשתסיימו, נבדוק יחד איך אייזנהאואר היה מסווג אותן, ונראה כמה קרובים הייתם לחשיבה הנשיאותית!

<div id="eisenhower-app">
    <div class="game-area">
        <div id="task-list-container">
             <h2>תיבת המשימות הנכנסות</h2>
             <p>גרור את המשימות למטריצה:</p>
             <div id="task-list">
                 <!-- Tasks will be loaded here by JavaScript -->
             </div>
        </div>

        <div id="matrix-container">
             <h2>מטריצת אייזנהאואר: כאן בונים את סדר העדיפויות</h2>
            <div id="matrix">
                <div class="quadrant" id="q1" data-quadrant-name="דחוף וחשוב">
                    <h3>דחוף וחשוב</h3>
                    <p>עשה! (Do It!)</p>
                    <div class="tasks-in-quadrant"></div>
                </div>
                <div class="quadrant" id="q2" data-quadrant-name="לא דחוף וחשוב">
                    <h3>לא דחוף וחשוב</h3>
                    <p>קבע זמן! (Decide & Schedule!)</p>
                     <div class="tasks-in-quadrant"></div>
                </div>
                <div class="quadrant" id="q3" data-quadrant-name="דחוף ולא חשוב">
                    <h3>דחוף ולא חשוב</h3>
                    <p>האצל! (Delegate!)</p>
                     <div class="tasks-in-quadrant"></div>
                </div>
                <div class="quadrant" id="q4" data-quadrant-name="לא דחוף ולא חשוב">
                    <h3>לא דחוף ולא חשוב</h3>
                    <p>מחק! (Delete!)</p>
                     <div class="tasks-in-quadrant"></div>
                </div>
            </div>
             <button id="process-button" disabled>סיימתי למיין! הראה לי את התוצאות</button>
        </div>
    </div>


    <div id="results-area" class="hidden">
        <h2>ניתוח המיון שלך וסדר העדיפויות הנשיאותי</h2>
        <div id="results-content">
            <!-- Results will be displayed here -->
        </div>
        <div id="score">
            <!-- Score and summary feedback -->
        </div>
         <button id="restart-button">מיין משימות חדשות</button>
    </div>
</div>

<style>
    :root {
        --color-q1: #e74c3c; /* Red - Do */
        --color-q2: #2ecc71; /* Green - Decide */
        --color-q3: #f1c40f; /* Yellow - Delegate */
        --color-q4: #bdc3c7; /* Grey - Delete */
        --color-q1-bg: #fde0dc;
        --color-q2-bg: #d4efdf;
        --color-q3-bg: #fcf3cf;
        --color-q4-bg: #eaeded;
        --color-app-bg: #f4f7f6;
        --color-card-bg: #ffffff;
        --color-text-dark: #333;
        --color-text-medium: #555;
        --color-border: #ccc;
        --color-button-primary: #3498db;
        --color-button-disabled: #ccc;
        --color-button-restart: #9b59b6;
    }

    #eisenhower-app {
        font-family: 'Arial', sans-serif; /* More modern font stack */
        max-width: 1000px; /* Slightly wider */
        margin: 20px auto;
        padding: 30px;
        border: 1px solid var(--color-border);
        border-radius: 12px; /* More rounded corners */
        background-color: var(--color-app-bg);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08); /* Soft shadow */
        color: var(--color-text-dark);
        direction: rtl; /* Ensure right-to-left */
        text-align: right;
    }

    #eisenhower-app h2, #eisenhower-app h3 {
        color: var(--color-text-dark);
        text-align: center;
        margin-bottom: 15px;
    }

    .game-area {
        display: flex;
        flex-wrap: wrap; /* Allow stacking on smaller screens */
        gap: 30px; /* Space between sections */
    }

     #task-list-container, #matrix-container {
         flex: 1; /* Distribute space */
         min-width: 300px; /* Ensure sections don't get too small */
     }

    #task-list-container {
        padding: 15px;
        background-color: #fff; /* White background for the list */
        border-radius: 8px;
        border: 1px solid var(--color-border);
    }
     #task-list-container > p {
         text-align: center;
         color: var(--color-text-medium);
         margin-top: -10px;
         margin-bottom: 20px;
     }

    #task-list {
        min-height: 150px; /* Taller list */
        border: 2px dashed var(--color-border);
        padding: 15px;
        background-color: #fdfdff; /* Very light blueish */
        display: flex;
        flex-wrap: wrap;
        gap: 12px; /* More space between cards */
        border-radius: 8px;
        align-content: flex-start; /* Tasks align to the top */
    }

    .task-card {
        border: 1px solid #ddd;
        padding: 12px;
        background-color: var(--color-card-bg);
        cursor: grab;
        border-radius: 8px; /* Rounded corners */
        width: 100%; /* Take full width in list */
        max-width: 220px; /* Max width for consistency when wrapping */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05); /* Subtle shadow */
        transition: transform 0.2s ease, box-shadow 0.2s ease; /* Smooth transitions */
        display: flex; /* Use flex for internal layout */
        flex-direction: column;
        justify-content: space-between;
    }

     .task-card:active {
         cursor: grabbing;
         transform: scale(1.05); /* Pop out slightly when grabbing */
         box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
     }


     .task-card h4 {
         margin-top: 0;
         margin-bottom: 8px; /* More space */
         font-size: 1.1em;
         color: var(--color-text-dark);
         line-height: 1.4;
     }

     .task-card p {
         margin: 0;
         font-size: 0.9em;
         color: var(--color-text-medium);
         line-height: 1.5;
     }

    #matrix-container {
         padding: 15px;
         background-color: #fff;
         border-radius: 8px;
         border: 1px solid var(--color-border);
    }
     #matrix-container > h2 {
          margin-bottom: 25px;
     }

    #matrix {
        display: grid;
        grid-template-columns: repeat(2, 1fr); /* 2 columns */
        grid-template-rows: repeat(2, 1fr); /* 2 rows */
        gap: 15px; /* Space between quadrants */
        height: 500px; /* Fixed height for matrix area */
    }

    .quadrant {
        border: 2px solid var(--color-border);
        padding: 15px;
        border-radius: 8px;
        background-color: #fff;
        display: flex; /* Use flexbox for quadrant content */
        flex-direction: column;
        align-items: center; /* Center header text */
        overflow: hidden; /* Prevent content overflow */
        transition: background-color 0.3s ease, border-color 0.3s ease;
    }

    .quadrant h3 {
        margin-top: 0;
        font-size: 1.3em;
        margin-bottom: 5px;
    }
     .quadrant p {
        margin-top: 0;
        font-size: 1em;
        color: var(--color-text-medium);
        margin-bottom: 15px;
     }

    /* Specific quadrant colors/borders */
    #q1 { border-color: var(--color-q1); background-color: var(--color-q1-bg); } /* Red - Do */
    #q2 { border-color: var(--color-q2); background-color: var(--color-q2-bg); } /* Green - Decide */
    #q3 { border-color: var(--color-q3); background-color: var(--color-q3-bg); } /* Yellow - Delegate */
    #q4 { border-color: var(--color-q4); background-color: var(--color-q4-bg); } /* Grey - Delete */

    .quadrant.dragover {
        background-color: rgba(0, 0, 0, 0.1); /* Darker overlay */
        border-style: dashed;
        transform: scale(1.02); /* Slight hover effect */
    }

    .tasks-in-quadrant {
        flex-grow: 1; /* Take remaining space */
        min-height: 50px; /* Ensure area is visible */
        border-top: 1px dashed rgba(0,0,0,0.1); /* Separator */
        padding-top: 10px;
        display: flex;
        flex-wrap: wrap;
        gap: 8px; /* Space between cards in quadrant */
        justify-content: center; /* Center cards */
        align-items: flex-start; /* Align cards to the top */
        width: 100%; /* Use full width */
    }
    .tasks-in-quadrant .task-card {
         cursor: default; /* Cannot drag once in quadrant */
         width: 150px; /* Smaller cards inside quadrants */
         margin: 0; /* Remove margin */
         box-shadow: none; /* Remove shadow */
         transition: none; /* Remove transition */
         opacity: 1; /* Ensure visible */
    }

    /* Task card feedback colors after processing */
    .task-card.correct {
        border-color: var(--color-q2); /* Green border */
        background-color: #e8f5e9; /* Lighter green */
    }
     .task-card.incorrect {
        border-color: var(--color-q1); /* Red border */
        background-color: #ffebee; /* Lighter red */
     }

    #process-button {
        display: block;
        width: 100%;
        padding: 18px; /* Larger padding */
        background-color: var(--color-button-primary);
        color: white;
        border: none;
        border-radius: 8px; /* Rounded */
        font-size: 1.3em;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        margin-top: 20px;
    }

    #process-button:hover:not(:disabled) {
        background-color: #2980b9;
        transform: translateY(-2px); /* Lift effect on hover */
    }
     #process-button:active:not(:disabled) {
         transform: translateY(0); /* Press effect */
     }


    #process-button:disabled {
        background-color: var(--color-button-disabled);
        cursor: not-allowed;
    }

    #results-area {
        margin-top: 40px;
        padding-top: 30px;
        border-top: 2px dashed var(--color-border);
        background-color: #fff;
        padding: 20px 30px;
        border-radius: 8px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
    }

    #results-area.hidden {
        display: none;
    }

    #results-content {
        margin-bottom: 30px;
    }

     #results-content div {
         margin-bottom: 15px;
         padding-bottom: 10px;
         border-bottom: 1px solid #eee;
     }

     #results-content div:last-child {
         border-bottom: none;
         padding-bottom: 0;
     }

     #results-content div h4 {
         margin: 0 0 8px 0;
         font-size: 1.2em;
         color: var(--color-text-dark);
     }

     #results-content div p {
         margin: 0;
         font-size: 1em;
         color: var(--color-text-medium);
         line-height: 1.6;
     }
      #results-content div p strong {
          color: var(--color-text-dark);
      }

      .result-feedback {
          font-weight: bold;
          margin-top: 5px;
          display: block;
      }
      .result-feedback.correct { color: var(--color-q2); } /* Green */
      .result-feedback.incorrect { color: var(--color-q1); } /* Red */


    #score {
        font-size: 1.4em;
        font-weight: bold;
        text-align: center;
        color: var(--color-text-dark);
        padding: 15px;
        background-color: #ecf0f1; /* Light background for score */
        border-radius: 8px;
        margin-bottom: 20px;
    }
     #score h4 {
         margin: 0 0 10px 0;
         font-size: 1.5em;
         color: #2c3e50;
     }
      #score p {
          font-size: 1em;
          color: var(--color-text-medium);
          line-height: 1.6;
          margin: 5px 0;
      }
       #score .final-feedback {
           font-size: 1.2em;
           margin-top: 15px;
           color: #27ae60; /* Greenish for positive feedback */
       }
       #score .final-feedback.needs-work {
           color: #e67e22; /* Orangish for improvement */
       }
        #score .final-feedback.warning {
           color: #e74c3c; /* Redish for caution */
       }


    #toggle-explanation {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        background-color: #eee;
        border: 1px solid #ccc;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.2s ease, transform 0.1s ease;
    }
     #toggle-explanation:hover {
         background-color: #ddd;
          transform: translateY(-1px);
     }

    #explanation {
        margin-top: 20px;
        padding: 25px;
        border: 1px solid var(--color-border);
        border-radius: 8px;
        background-color: #fff;
        line-height: 1.7;
        color: var(--color-text-medium);
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    }

    #explanation h2, #explanation h3 {
        color: var(--color-text-dark);
        margin-top: 20px;
        margin-bottom: 10px;
        border-bottom: 1px dashed #eee;
        padding-bottom: 5px;
    }
     #explanation h2 { font-size: 1.8em; }
     #explanation h3 { font-size: 1.4em; }

    #explanation p {
        margin-bottom: 15px;
    }

     #explanation ul, #explanation ol {
         margin-bottom: 15px;
         padding-right: 20px;
     }
      #explanation li {
          margin-bottom: 8px;
      }

     #restart-button {
         display: block;
         width: auto;
         margin: 20px auto 0 auto;
         padding: 10px 20px;
         background-color: var(--color-button-restart);
         color: white;
         border: none;
         border-radius: 4px;
         font-size: 1em;
         cursor: pointer;
         transition: background-color 0.3s ease;
     }
      #restart-button:hover {
          background-color: #8e44ad;
      }


    /* Responsive adjustments */
    @media (max-width: 768px) {
        .game-area {
            flex-direction: column; /* Stack task list and matrix */
            gap: 20px;
        }
         #eisenhower-app {
             padding: 15px;
         }
         #matrix {
             height: auto; /* Auto height when stacked */
             min-height: 400px;
         }
         .task-card {
             max-width: none; /* Allow cards to stretch */
         }
          .tasks-in-quadrant .task-card {
             width: 100px; /* Smaller cards */
          }
    }

</style>

<button id="toggle-explanation">הצג/הסתר הסבר על מטריצת אייזנהאואר</button>

<div id="explanation" style="display: none;">
    <h2>מהי מטריצת אייזנהאואר ומדוע היא כלי חזק לניהול זמן?</h2>
    <p>מטריצת אייזנהאואר, הידועה גם כמטריצת דחוף/חשוב, היא שיטת סיווג משימות פשוטה אך עוצמתית המסייעת לך לארגן את סדר העדיפויות שלך ולנהל את הזמן בצורה אפקטיבית יותר. במקום להגיב באופן רנדומלי למשימות כפי שהן מגיעות, המטריצה מאפשרת לך להחליט מראש היכן כל משימה "שייכת" ומה לעשות איתה בהתאם לחשיבותה ולדחיפותה.</p>

    <h2>ההיסטוריה הקצרה של המטריצה</h2>
    <p>הרעיון הבסיסי מאחורי המטריצה מיוחס לנשיא ארה"ב לשעבר, דווייט ד. אייזנהאואר. אייזנהאואר, שהיה גם גנרל בעל חמש דרגות ופיקד על בעלות הברית במלחמת העולם השנייה, היה ידוע ביכולתו לקבל החלטות קשות ולנהל משאבים מורכבים. הוא אמר: "מה שחשוב רק לעיתים נדירות דחוף, ומה שדחוף רק לעיתים נדירות חשוב." סטיבן קובי, בספרו "שבעת ההרגלים של אנשים אפקטיביים במיוחד", פיתח את הרעיון לכדי מטריצת ארבעת הריבועים המוכרת כיום.</p>

    <h2>פירוט ארבעת הריבועים:</h2>

    <h3>ריבוע 1: דחוף וחשוב (עשה! Do!)</h3>
    <p>זהו ריבוע המשברים והמיידיות. משימות כאן דורשות תשומת לב מיידית והן קריטיות להשגת המטרות שלך. דוגמאות: פרויקט עם דדליין היום, משבר תפעולי פתאומי, בעיה בריאותית דחופה. בילוי מופרז בריבוע זה מעיד על ניהול זמן תגובתי ומוביל לשחיקה. אנשים אפקטיביים שואפים למזער משימות שמגיעות לכאן על ידי תכנון מונע בריבוע 2.</p>

    <h3>ריבוע 2: לא דחוף וחשוב (קבע זמן! Decide!)</h3>
    <p>זהו ריבוע הצמיחה, התכנון והאפקטיביות ארוכת הטווח. משימות כאן חשובות למטרות הגדולות שלך, לפיתוח אישי ומקצועי, ומונעות ממשברים עתידיים להתפתח. דוגמאות: תכנון אסטרטגי, בניית קשרים, למידה והתפתחות, פעילות גופנית סדירה, מניעת בעיות עתידיות, פרויקטים חשובים ללא לחץ זמן מיידי. השקעת זמן יזומה בריבוע זה היא המפתח למניעת שחיקה, להשגת יעדים משמעותיים ולתחושת שליטה.</p>

    <h3>ריבוע 3: דחוף ולא חשוב (האצל! Delegate!)</h3>
    <p>אלו משימות שנראות דחופות (בדרך כלל כי הן דורשות תגובה מיידית), אך אינן קריטיות באמת להשגת המטרות החשובות *לך*. הן לרוב משרתות את המטרות של אחרים. דוגמאות: מענה מיידי למיילים לא חשובים, שיחות טלפון לא מתוכננות, בקשות קטנות ועוצרות עבודה. המפתח כאן הוא לזהות מה ניתן להאציל (למישהו אחר בצוות, לעוזר אישי) או במקרים מסוימים, לסרב בצורה מנומסת אך אסרטיבית.</p>

    <h3>ריבוע 4: לא דחוף ולא חשוב (מחק! Delete!)</h3>
    <p>זהו ריבוע ההסחות דעת ובזבוזי הזמן. משימות כאן אינן חשובות ואינן דחופות. הן פשוט צורכות זמן ואנרגיה מבלי לקדם אותך. דוגמאות: גלילה אינסופית בחדשות או ברשתות חברתיות, משחקי מחשב מוגזמים, צפייה כפייתית בטלוויזיה, שיחות רכילות ארוכות. משימות אלו יש לצמצם, להימנע מהן, או לבטל לחלוטין.</p>

    <h2>איך להשתמש במטריצה בפועל (שלבים למיון משימות)</h2>
    <ol>
        <li>**איסוף:** רשום את כל המשימות שיש לך לבצע.</li>
        <li>**הערכה (לכל משימה):**
            <ul>
                <li>האם המשימה *דחופה*? (דורשת טיפול מיידי? יש דדליין קרוב מאוד?)</li>
                <li>האם המשימה *חשובה*? (האם היא מקדמת אותך לעבר המטרות והערכים החשובים לך? האם יש לה השפעה משמעותית על התוצאות?).</li>
            </ul>
        </li>
        <li>**סיווג:** בהתאם לשתי התשובות, סווג את המשימה לאחד מארבעת הריבועים.</li>
        <li>**פעולה:** פעל בהתאם להמלצת הריבוע: עשה (Do), קבע זמן (Schedule/Decide), האצל (Delegate), או מחק (Delete).</li>
    </ol>

    <h2>היתרונות של שימוש במטריצה</h2>
    <ul>
        <li>**שליטה במקום תגובתיות:** עובר מכיבוי שריפות לתכנון יזום ואקטיבי.</li>
        <li>**מיקוד באמת חשוב:** מבטיח שהזמן והאנרגיה מופנים למשימות שמקדמות אותך משמעותית (בעיקר ריבוע 2).</li>
        <li>**הפחתת לחץ:** כשיודעים מה דחוף ומה חשוב, קל יותר לנהל את העומס.</li>
        <li>**קבלת החלטות מהירה:** כלי ויזואלי שמסייע להכריע לגבי משימות חדשות שמגיעות.</li>
        <li>**זיהוי בזבוזי זמן:** חושף בקלות אילו פעילויות (ריבוע 4) גוזלות את הזמן ללא תמורה.</li>
    </ul>

    <h2>טעויות נפוצות ואיך להימנע מהן</h2>
    <ul>
        <li>**בלבול בין דחוף לחשוב:** הדחיפות לרוב קשורה לגורם חיצוני או לדדליין קרוב. החשיבות קשורה למטרות והערכים הפנימיים שלך. זה ההבדל המרכזי.</li>
        <li>**הזנחת ריבוע 2:** אי השקעה בתכנון ובמניעה (ריבוע 2) מובילה בהכרח להצטברות משברים (ריבוע 1).</li>
        <li>**ביצוע משימות ריבוע 3 בעצמך:** אם אפשר, האצל. אם לא, שאל האם המשימה באמת הכרחית או שניתן לדחות/לבטל.</li>
        <li>**בזבוז זמן בריבוע 4 "כמנוחה":** מנוחה אמיתית מתוכננת (ריבוע 2) אפקטיבית בהרבה מבזבוז זמן פסיבי.</li>
    </ul>

    <h2>טיפים ליישום המטריצה בחיי היום-יום ובעבודה</h2>
    <ul>
        <li>השתמש במטריצה בסוף כל יום עבודה או בתחילת היום למחרת כדי לסווג את המשימות העומדות בפניך.</li>
        <li>הקצה "בלוקי זמן" קבועים ביומן למשימות מריבוע 2.</li>
        <li>התחל את יום העבודה במשימות ריבוע 1 ו-2 (אחרי שמוינו).</li>
        <li>היה מודע להסחות דעת והשתדל לסלק אותן מהסביבה שלך.</li>
        <li>סקירה תקופתית של המטריצה שלך יכולה לעזור לזהות דפוסים (למשל, יותר מדי משימות נופלות לריבוע 1).</li>
        <li>השתמש בכלים דיגיטליים או פיזיים (רשימות, אפליקציות) כדי לעקוב אחר המשימות לאחר הסיווג.</li>
    </ul>
</div>


<script>
    document.addEventListener('DOMContentLoaded', () => {
        const taskList = document.getElementById('task-list');
        const quadrants = document.querySelectorAll('.quadrant');
        const processButton = document.getElementById('process-button');
        const resultsArea = document.getElementById('results-area');
        const resultsContent = document.getElementById('results-content');
        const scoreDisplay = document.getElementById('score');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');
        const restartButton = document.getElementById('restart-button');

        // Define tasks with their correct classifications (for scoring)
        let tasksData = [
            { id: 1, title: 'להכין מצגת לפגישת מועצת המנהלים מחר בבוקר', description: 'נדרשת עבודה רבה על התוכן והעיצוב - דדליין צפוף.', correctQuadrant: 'q1' },
            { id: 2, title: 'לענות על מיילים לא קריטיים מהבוקר', description: 'מעל 50 מיילים שמחכים לתגובה, לא הכל חשוב.', correctQuadrant: 'q3' },
            { id: 3, title: 'לתכנן אסטרטגיה לרבעון הבא', description: 'פגישה עם צוות הפיתוח לתכנון קדימה - חשוב מאוד, לא דחוף מיידית.', correctQuadrant: 'q2' },
            { id: 4, title: 'לנקות את ה"זבל" בתיבת המייל', description: 'הרבה ניוזלטרים ישנים והתראות שכבר לא רלוונטיות - סתם תופס מקום.', correctQuadrant: 'q4' },
            { id: 5, title: 'לתקן באג קריטי שמנע מלקוח להשתמש במוצר', description: 'דווח לפני שעה, משפיע על עבודה שוטפת של לקוח גדול - דחוף וחשוב!', correctQuadrant: 'q1' },
            { id: 6, title: 'לקרוא דוח מחקר חדש על טרנדים בתעשייה', description: 'דוח מקיף שדורש שעה-שעתיים של קריאה מעמיקה - יקדם אותי.', correctQuadrant: 'q2' },
            { id: 7, title: 'להשתתף באירוע חברתי אופציונלי בחברה', description: 'נטוורקינג ושיחות קלות עם עמיתים - נחמד, לא חובה, לא דחוף.', correctQuadrant: 'q4' }, // Changed from Q3 to Q4 as it's optional and social
            { id: 8, title: 'לארגן את שולחן העבודה שלי', description: 'ניירת וכאוס כללי שמצטבר - חשוב לאורך זמן, לא דחוף כרגע.', correctQuadrant: 'q2' }, // Changed from Q4 to Q2 as organisation can be important for productivity
            { id: 9, title: 'להזמין פיצה לארוחת הצהריים', description: 'בטן מקרקרת! - דחוף, אבל לא חשוב לעבודה (אלא אם רעב פוגע בריכוז!)', correctQuadrant: 'q3'}, // New task
            { id: 10, title: 'להתחיל ללמוד שפה חדשה', description: 'תמיד רציתי ללמוד ספרדית - חשוב לצמיחה אישית, לא דחוף בכלל.', correctQuadrant: 'q2'} // New task
        ];

        let currentTasks = [];
        let userClassifications = {}; // { taskId: quadrantId, ... }

        // Function to reset and start a new round
        function initializeGame() {
            // Shuffle tasks and select a subset (e.g., 8 tasks) for variation
             currentTasks = tasksData.sort(() => Math.random() - 0.5).slice(0, 8);

            userClassifications = {};
            taskList.innerHTML = ''; // Clear task list
            quadrants.forEach(quadrant => {
                quadrant.querySelector('.tasks-in-quadrant').innerHTML = ''; // Clear quadrants
            });
            resultsArea.classList.add('hidden');
            processButton.disabled = true;
            processButton.innerText = 'סיימתי למיין! הראה לי את התוצאות';
            processButton.style.backgroundColor = ''; // Reset button color
             restartButton.style.display = 'none'; // Hide restart button initially

            renderTasks();
        }


        // Initial rendering of tasks
        function renderTasks() {
            taskList.innerHTML = ''; // Clear existing tasks
            currentTasks.forEach(task => {
                 // Only render tasks not yet classified (should be all at the start)
                 if (!userClassifications[task.id]) {
                    const taskCard = document.createElement('div');
                    taskCard.classList.add('task-card');
                    taskCard.setAttribute('draggable', true);
                    taskCard.setAttribute('data-task-id', task.id);
                     taskCard.innerHTML = `<h4>${task.title}</h4><p>${task.description}</p>`; // InnerHTML instead of textContent for description italics
                    taskList.appendChild(taskCard);

                    // Add dragstart listener
                    taskCard.addEventListener('dragstart', (event) => {
                        event.dataTransfer.setData('text/plain', event.target.dataset.taskId);
                         // Add a class for visual feedback while dragging
                         event.target.classList.add('dragging');
                        setTimeout(() => {
                             event.target.style.opacity = '0.1'; // Make original element semi-transparent
                         }, 0);
                    });

                    taskCard.addEventListener('dragend', (event) => {
                         // Remove the dragging class and reset opacity
                         event.target.classList.remove('dragging');
                         event.target.style.opacity = '1';

                         // If the task wasn't dropped in a valid zone, it might need to reappear
                         // However, the current drop logic moves it directly, so this might not be necessary if drop is successful.
                         // Let's ensure it reappears if drag was cancelled or invalid drop (though browser default often handles this)
                         const taskId = event.target.dataset.taskId;
                         if (!userClassifications[taskId]) {
                             // If it wasn't classified, put it back in the list (simple append, order might change)
                             // A more complex version would track original position
                             const taskElement = document.querySelector(`.task-card[data-task-id="${taskId}"]`);
                             if (taskElement && !taskElement.parentElement.closest('.quadrant')) {
                                 taskList.appendChild(taskElement); // Append back to list if not in a quadrant
                                 taskElement.style.display = ''; // Ensure visible
                             }
                         }
                    });
                 }
            });
             checkIfAllTasksSorted();
        }

        // Add drag and drop listeners to quadrants
        quadrants.forEach(quadrant => {
            quadrant.addEventListener('dragover', (event) => {
                event.preventDefault(); // Allow drop
                 // Check if the dragged item is a task-card
                const draggedElement = document.querySelector('.task-card.dragging');
                if (draggedElement) {
                    quadrant.classList.add('dragover');
                }
            });

            quadrant.addEventListener('dragleave', () => {
                quadrant.classList.remove('dragover');
            });

            quadrant.addEventListener('drop', (event) => {
                event.preventDefault();
                quadrant.classList.remove('dragover');

                const taskId = event.dataTransfer.getData('text/plain');
                const taskElement = document.querySelector(`.task-card[data-task-id="${taskId}"]`);

                 if (taskElement && !userClassifications[taskId]) { // Ensure it's a valid task and not already classified
                     // Find the task data
                     const taskData = currentTasks.find(task => task.id == taskId);
                     if (!taskData) return; // Should not happen

                     // Move the element visually
                    const tasksInQuadrantDiv = quadrant.querySelector('.tasks-in-quadrant');

                     // Add animation class briefly
                    taskElement.style.opacity = '1'; // Make it visible again
                    taskElement.style.transform = 'scale(0.9)'; // Start slightly smaller
                    taskElement.style.transition = 'transform 0.3s ease, opacity 0.3s ease'; // Add transition
                    tasksInQuadrantDiv.appendChild(taskElement); // Append to the new location

                     // Use a timeout to trigger the transition after appending
                    setTimeout(() => {
                         taskElement.style.transform = 'scale(1)'; // Animate to normal size
                     }, 50); // Small delay

                    taskElement.style.cursor = 'default'; // Make it not draggable after dropping
                    taskElement.setAttribute('draggable', false); // Disable further dragging

                     // Record the classification
                     userClassifications[taskId] = quadrant.id;

                     // Remove task from the source list visually (it's already moved)
                     // If the task was originally in the task list, it's now in the quadrant.
                     // If we implement moving between quadrants later, this would be more complex.
                     // For now, moving from taskList to quadrant is the only supported drag.

                     checkIfAllTasksSorted();
                 }
            });
        });

        function checkIfAllTasksSorted() {
            const sortedCount = Object.keys(userClassifications).length;
            const totalTasks = currentTasks.length;

            if (sortedCount === totalTasks) {
                processButton.disabled = false;
                 processButton.innerText = 'סיימתי למיין! הראה לי את התוצאות';
            } else {
                processButton.disabled = true;
                 processButton.innerText = `נותרו ${totalTasks - sortedCount} משימות למיון...`;
            }
        }


        // Process button logic
        processButton.addEventListener('click', () => {
            resultsArea.classList.remove('hidden');
            resultsContent.innerHTML = ''; // Clear previous results
            scoreDisplay.innerHTML = ''; // Clear previous score
            restartButton.style.display = 'block'; // Show restart button

            let correctCount = 0;
            let userChoicesSummary = { q1: 0, q2: 0, q3: 0, q4: 0 };


            currentTasks.forEach(task => {
                const userQuadrantId = userClassifications[task.id];
                const taskElement = document.querySelector(`.task-card[data-task-id="${task.id}"]`);
                const correctQuadrantId = task.correctQuadrant;
                const isCorrect = (userQuadrantId === correctQuadrantId);

                userChoicesSummary[userQuadrantId]++;

                const userQuadrantName = document.getElementById(userQuadrantId).dataset.quadrantName;
                const correctQuadrantName = document.getElementById(correctQuadrantId).dataset.quadrantName;

                 let feedbackText = "";
                 let feedbackClass = "";
                 if (isCorrect) {
                     feedbackText = "סווג נכון!";
                     feedbackClass = "correct";
                     correctCount++;
                      taskElement.classList.add('correct'); // Add visual feedback to card
                 } else {
                     feedbackText = `כמעט! סווגת ל"${userQuadrantName}", אך סיווג נשיאותי היה "${correctQuadrantName}".`;
                     feedbackClass = "incorrect";
                     taskElement.classList.add('incorrect'); // Add visual feedback to card
                 }

                 resultsContent.innerHTML += `
                     <div>
                         <h4>${task.title}</h4>
                         <p>
                             <strong>הסיווג שלך:</strong> ${userQuadrantName}
                             <br>
                             <strong>הסיווג הנשיאותי:</strong> ${correctQuadrantName}
                         </p>
                         <span class="result-feedback ${feedbackClass}">${feedbackText}</span>
                     </div>
                 `;

                 // Remove any dragover class that might be stuck
                 quadrants.forEach(q => q.classList.remove('dragover'));
            });

            // Calculate and display score
            const totalTasks = currentTasks.length;
            const scorePercentage = Math.round((correctCount / totalTasks) * 100);

            let finalFeedback = "";
            let feedbackColorClass = "";

            if (scorePercentage === 100) {
                finalFeedback = "ציון מושלם! אתה חושב כמו אייזנהאואר!";
                feedbackColorClass = "correct";
            } else if (scorePercentage >= 75) {
                finalFeedback = "מצוין! הבנת את העיקרון וסווגת את רוב המשימות נכון.";
                 feedbackColorClass = "correct";
            } else if (scorePercentage >= 50) {
                finalFeedback = "סביר. יש עוד מקום לשיפור בהבחנה בין דחוף לחשוב.";
                 feedbackColorClass = "needs-work";
            } else {
                finalFeedback = "כדאי לעבור שוב על ההסבר ולתרגל את ההבדל בין דחוף וחשוב.";
                 feedbackColorClass = "warning";
            }


            scoreDisplay.innerHTML = `
                <h4>הציון שלך: ${scorePercentage}% (${correctCount} מתוך ${totalTasks} סווגו נכון)</h4>
                 <p class="final-feedback ${feedbackColorClass}">${finalFeedback}</p>
                 <p><strong>התפלגות הסיווג שלך:</strong></p>
                 <ul>
                     <li>דחוף וחשוב (Q1): ${userChoicesSummary.q1}</li>
                     <li>לא דחוף וחשוב (Q2): ${userChoicesSummary.q2}</li>
                     <li>דחוף ולא חשוב (Q3): ${userChoicesSummary.q3}</li>
                     <li>לא דחוף ולא חשוב (Q4): ${userChoicesSummary.q4}</li>
                 </ul>
                 <p style="font-size:0.9em; color:#666;">זכור, המטרה היא להשקיע את מירב הזמן בריבוע 2 (חשוב, לא דחוף) כדי למנוע משברים בריבוע 1!</p>
            `;

             // Disable processing after showing results
             processButton.disabled = true;
             processButton.innerText = "התוצאות הוצגו";
             processButton.style.backgroundColor = var(--color-button-disabled); // Grey out the button
        });


        // Toggle explanation visibility
        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.innerText = isHidden ? 'הסתר הסבר על מטריצת אייזנהאואר' : 'הצג/הסתר הסבר על מטריצת אייזנהאואר';
        });

         // Restart button logic
         restartButton.addEventListener('click', () => {
             // Remove correctness classes from cards before potentially moving them
             document.querySelectorAll('.task-card').forEach(card => {
                 card.classList.remove('correct', 'incorrect');
                  // Remove any added outcome spans
                  const outcomeSpan = card.querySelector('span');
                  if (outcomeSpan) outcomeSpan.remove();
             });
             initializeGame(); // Start a new game
         });


        // Initial game setup
        initializeGame();

         // Add a class to body/html to indicate JS is active, useful for CSS
         document.body.classList.add('js-active');
    });
</script>