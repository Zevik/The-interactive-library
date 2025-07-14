---
title: "פענוח עוררות: משחק הפוליגרף המדעי"
english_slug: detecting-lies-the-polygraph-game
category: "מדעי החברה / פסיכולוגיה"
tags:
  - פוליגרף
  - זיהוי שקרים
  - פסיכולוגיה
  - מגבלות מדעיות
  - פיזיולוגיה
---
# פענוח עוררות: משחק הפוליגרף המדעי

סרטים וסדרות מציגים מכשירי פוליגרף כ"מכונות אמת" קסומות. האם באמת ניתן לגלות שקרים בוודאות רק על סמך שינויים פיזיולוגיים בגוף? בואו ניכנס לנעליו של בודק פוליגרף ונראה כמה מורכבת המשימה של פענוח תגובות הגוף.

<div id="polygraph-app">
    <div id="polygraph-main">
        <div id="scenario-area" class="panel">
            <h2><i class="icon fas fa-clipboard-list"></i> התרחיש:</h2>
            <p id="scenario-text"></p>
            <h3><i class="icon fas fa-user"></i> הנבדק:</h3>
            <p id="subject-text"></p>
        </div>

        <div id="graph-area" class="panel">
            <h3><i class="icon fas fa-chart-line"></i> גרפים פיזיולוגיים בזמן אמת:</h3>
            <div class="graph-container">
                <h4>קצב לב (HR) <span class="unit">(BPM)</span></h4>
                <canvas id="hr-graph" width="600" height="120"></canvas>
            </div>
            <div class="graph-container">
                <h4>נשימה (Resp.) <span class="unit">(CPM)</span></h4>
                <canvas id="resp-graph" width="600" height="120"></canvas>
            </div>
            <div class="graph-container">
                <h4>מוליכות עורית (GSR) <span class="unit">(μS)</span></h4>
                <canvas id="gsr-graph" width="600" height="120"></canvas>
            </div>
             <div class="graph-legend">
                 <span class="legend-item"><span class="legend-color" style="background-color: #e74c3c;"></span> קצב לב</span>
                 <span class="legend-item"><span class="legend-color" style="background-color: #3498db;"></span> נשימה</span>
                 <span class="legend-item"><span class="legend-color" style="background-color: #2ecc71;"></span> מוליכות עורית</span>
             </div>
        </div>

        <div id="questions-area" class="panel">
            <h3><i class="icon fas fa-question-circle"></i> שאלות לבחירה (<span id="question-counter">0</span>/<span id="question-limit">10</span>):</h3>
            <p class="instruction">לחץ על שאלה כדי לשמוע את התגובה הפיזיולוגית של הנבדק.</p>
            <div id="question-buttons">
                <button class="question-button primary-button" data-type="neutral" title="שאלות לבסס קו בסיס לתגובות פיזיולוגיות רגילות.">שאלת ניטרלית</button>
                <button class="question-button primary-button" data-type="control" title="שאלות כלליות על התנהגות לא הוגנת בעבר, נועדו ליצור תגובה פיזיולוגית אצל דובר אמת.">שאלת בקרה</button>
                <button class="question-button primary-button" data-type="relevant" title="שאלות ישירות על האירוע הנחקר. אלו השאלות בהן השקרן צפוי להגיב בעוצמה רבה יותר.">שאלה רלוונטית</button>
            </div>
             <div id="question-feedback" class="feedback hidden">ממתין לשאלה...</div>
        </div>

        <div id="decision-area" class="panel hidden">
            <h3><i class="icon fas fa-balance-scale"></i> הגעת לסוף הסיבוב. מהי מסקנתך?</h3>
            <button id="decide-lie" class="decision-button danger-button"><i class="icon fas fa-times-circle"></i> הנבדק שיקר</button>
            <button id="decide-truth" class="decision-button success-button"><i class="icon fas fa-check-circle"></i> הנבדק אמר אמת</button>
        </div>

        <div id="results-area" class="panel hidden">
            <h3><i class="icon fas fa-poll"></i> תוצאות הסימולציה:</h3>
            <p id="true-state"></p>
            <p id="user-decision"></p>
            <p id="outcome"></p>
            <div id="explanation-points">
                <h4><i class="icon fas fa-lightbulb"></i> תובנות מהסימולציה:</h4>
                <p class="insight"><i class="icon fas fa-flask"></i> <strong>פוליגרף מודד עוררות, לא שקר:</strong> הגרפים הראו תגובות פיזיולוגיות (קצב לב, נשימה, הזעה), שהן סימני עוררות או מתח, לא סימנים ישירים לשקר. התגובות יכולות לנבוע מסיבות רבות.</p>
                <p class="insight"><i class="icon fas fa-puzzle-piece"></i> <strong>הפרשנות מורכבת וסובייקטיבית:</strong> גם בסימולציה פשוטה זו, ראית שאדם דובר אמת יכול להראות תגובות חזקות (למשל, מלחץ או עצבנות), ואדם שקרן יכול להראות תגובות חלשות יחסית (אולי ניסה לשלוט בעצמו). זה מדגים איך אפשר להגיע לתוצאות שגויות (חיוביות כוזבות - אדם ישר מזוהה בטעות כשקרן; שליליות כוזבות - שקרן מזוהה בטעות כדובר אמת).</p>
                <p class="insight"><i class="icon fas fa-question-circle"></i> <strong>חשיבות סוגי השאלות:</strong> השוואת תגובות לשאלות רלוונטיות לעומת שאלות בקרה (Control Question Test) היא ליבת השיטה הנפוצה ביותר, אך גם היא תלויה בהנחות שלא תמיד מתקיימות (למשל, שדובר אמת אכן יגיב חזק יותר לשאלות הבקרה). </p>
                 <p class="insight"><i class="icon fas fa-exclamation-triangle"></i> <strong>מגבלות מדעיות:</strong> בגלל הסיבות הללו ומגבלות נוספות, הקהילה המדעית לא מכירה בפוליגרף ככלי מדויק או אמין לגילוי שקרים, ותוצאותיו לרוב אינן קבילות בבתי משפט בישראל ובעולם.</p>
            </div>
            <button id="restart-simulation" class="primary-button"><i class="icon fas fa-redo"></i> התחל סימולציה חדשה</button>
        </div>
    </div>
</div>

<button id="toggle-explanation" class="secondary-button"><i class="icon fas fa-book-open"></i> הצג/הסתר הסבר מקיף על הפוליגרף</button>

<div id="explanation" class="hidden">
    <h2><i class="icon fas fa-flask"></i> הסבר מורחב: האם הפוליגרף באמת מגלה שקרים?</h2>

    <h3>מה הפוליגרף באמת מודד?</h3>
    הפוליגרף, המכונה לפעמים בטעות "מכונת אמת", אינו מסוגל לזהות שקרים ישירות. במקום זאת, הוא מודד סדרה של שינויים פיזיולוגיים המתרחשים בגוף ונשלטים ברובם על ידי מערכת העצבים האוטונומית, המגיבה באופן בלתי רצוני למצבי עוררות רגשית או מתח. המדדים העיקריים הנמדדים הם:
    <ul>
        <li><i class="icon fas fa-heartbeat"></i> <strong>קצב לב ולחץ דם:</strong> שינויים בדופק ובלחץ הדם (סימן לעוררות של מערכת העצבים הסימפתטית).</li>
        <li><i class="icon fas fa-lungs"></i> <strong>נשימה:</strong> שינויים בדפוס, בקצב ובעומק הנשימה. מתח יכול לגרום לנשימה מהירה ושטוחה יותר.</li>
        <li><i class="icon fas fa-hand-lizard"></i> <strong>מוליכות עורית (GSR - Galvanic Skin Response):</strong> שינויים בהתנגדות החשמלית של העור, המושפעת מכמות הזיעה. הזעה מוגברת, גם אם בלתי מורגשת, מעידה על עוררות פיזיולוגית או מתח נפשי.</li>
    </ul>
    ההנחה המרכזית היא שאמירת שקר גורמת למתח פסיכולוגי פנימי (פחד מהתגלות, אשמה, צורך בדיכוי האמת), ומתח זה מתבטא בעוררות פיזיולוגית חזקה יותר מאשר אמירת אמת.

    <h3>התאוריה מאחורי בדיקת הפוליגרף (CQT - Comparison Question Test)</h3>
    השיטה הנפוצה ביותר לבדיקת פוליגרף נקראת Comparison Question Test (CQT). היא מבוססת על השוואת התגובות הפיזיולוגיות של הנבדק לשלושה סוגי שאלות:
    <ul>
        <li><i class="icon fas fa-comment-alt"></i> <strong>שאלות ניטרליות (Irrelevant Questions):</strong> שאלות פשוטות ומוסכמות שאין להן קשר לאירוע הנחקר (למשל, "האם שמך יוסף?"). הן נועדו לבסס קו בסיס (בייסליין) של התגובה הפיזיולוגית הרגילה של הנבדק במצב נינוח יחסית.</li>
        <li><i class="icon fas fa-question"></i> <strong>שאלות בקרה/השוואה (Control/Comparison Questions):</strong> שאלות רחבות, לרוב על התנהגות לא הוגנת כללית בעבר, שמעט מאוד אנשים יכולים לענות עליהן בוודאות מוחלטת 'לא' (למשל, "האם גנבת אי פעם משהו בחיים?"). שאלות אלו מנוסחות כך שרוב האנשים, גם דוברי אמת בנוגע לאירוע הנחקר, יחושו לגביהן אי-נוחות או חשש קל מעצם השאלה או מהאפשרות להיתפס בשקר קטן או דבר מה מהעבר. הן נועדו ליצור תגובה פיזיולוגית משמעותית אצל דובר אמת, כדי שיהיה למה להשוות את תגובתו לשאלות הרלוונטיות. ההנחה היא שדובר אמת יגיב חזק יותר לשאלות הבקרה (שעשויות לעורר בו חשש או אשמה קלה), בעוד שקרן יגיב חזק יותר לשאלות הרלוונטיות (שעליהן הוא משקר בנוגע לאירוע העיקרי).</li>
        <li><i class="icon fas fa-search"></i> <strong>שאלות רלוונטיות (Relevant Questions):</strong> שאלות ספציפיות וישירות הנוגעות לאירוע הנחקר (למשל, "האם אתה לקחת את החפץ מחדר המשרד?"). אלו השאלות בהן מצפים לראות את התגובה הפיזיולוגית החזקה ביותר אם הנבדק משקר בנוגע לאירוע.</li>
    </ul>

    <h3>כיצד מפרשים את הגרפים וקבלת החלטה</h3>
    בודק הפוליגרף מנתח את הגרפים ומדרג את עוצמת התגובות הפיזיולוגיות לכל שאלה. ההחלטה מתבססת על השוואה:
    <ul>
        <li><i class="icon fas fa-chart-bar"></i> אם התגובות לשאלות הרלוונטיות חזקות באופן עקבי ומשמעותי יותר מאשר התגובות לשאלות הבקרה, הדבר נחשב לאינדיקציה להונאה (Deception Indicated - DI).</li>
        <li><i class="icon fas fa-chart-bar"></i> אם התגובות לשאלות הבקרה חזקות יותר, או שהתגובות לשאלות הרלוונטיות חלשות מהן, הדבר נחשב לאינדיקציה לאמירת אמת (No Deception Indicated - NDI).</li>
        <li><i class="icon fas fa-chart-bar"></i> לעיתים התגובות אינן חד משמעיות, והתוצאה היא מעורפלת (Inconclusive).</li>
    </ul>
     חשוב להדגיש שפרשנות הגרפים אינה אוטומטית ומצריכה שיקול דעת ואף ניסיון של הבודק, מה שמוסיף אלמנט של סובייקטיביות לתהליך.

    <h3>המגבלות והביקורות המרכזיות על הפוליגרף: מדוע הוא אינו "מכונת אמת"?</h3>
    למרות השימוש הנרחב בו בהקשרים מסוימים (בעיקר screening ביטחוני ותעסוקתי), הפוליגרף הוא נושא לוויכוח מדעי ואתי עז, וסופג ביקורת נוקבת מצד הקהילה המדעית והמשפטית:
    <ul>
        <li><i class="icon fas fa-exclamation-circle"></i> <strong>מודד עוררות, לא אמת/שקר:</strong> זוהי המגבלה היסודית ביותר. תגובות פיזיולוגיות המעידות על עוררות או מתח יכולות לנבוע ממגוון עצום של סיבות שאינן קשורות כלל לאמירת שקר בנושא המרכזי. לחץ מהבדיקה עצמה, חרדה כללית, כעס, פחד מתגובה חזקה גם כשדוברים אמת, מחשבות טורדניות, או אפילו מצב פיזיולוגי רגעי - כל אלה יכולים להשפיע על הגרפים ולהתפרש בטעות כסימן להונאה.</li>
        <li><i class="icon fas fa-bug"></i> <strong>תוצאות שגויות:</strong>
            <ul>
                <li><i class="icon fas fa-times"></i> <strong>חיובי כוזב (False Positive):</strong> אדם דובר אמת מזוהה בטעות כשקרן. זה קורה כאשר התגובות לשאלות הרלוונטיות חזקות יותר מהתגובות לשאלות הבקרה, למרות שהנבדק אומר אמת. הסיבות יכולות להיות לחץ גבוה, חרדה ספציפית לשאלה מסוימת, או שהשאלות לא נוסחו/הושוו כראוי. זוהי אחת הבעיות החמורות ביותר, שכן היא עלולה להוביל להאשמת חפים מפשע.</li>
                <li><i class="icon fas fa-check"></i> <strong>שלילי כוזב (False Negative):</strong> שקרן מזוהה בטעות כדובר אמת. זה יכול לקרות אם השקרן אינו חווה מתח מספק בעת אמירת השקר (למשל, פסיכופתים), אם הוא מצליח לשלוט בתגובותיו הפיזיולוגיות (Countermeasures), או אם הוא מגיב בעוצמה חזקה יותר לשאלות הבקרה מסיבות אחרות.</li>
            </ul>
        </li>
        <li><i class="icon fas fa-toolbox"></i> <strong>יכולת הטעיה (Countermeasures):</strong> קיימות שיטות שונות שאנשים יכולים לנקוט כדי לנסות "לעקוף" את הבדיקה ולהטעות את המכונה (למשל, לכווץ שרירים, לנעוץ סיכה באצבע, או לנשוך את הלשון בעת מענה על שאלות הבקרה, כדי להגביר באופן מלאכותי את התגובה הפיזיולוגית עליהן ולהקטין את הפער בינן לבין השאלות הרלוונטיות). בודקי פוליגרף מיומנים אמורים לזהות חלק מהשיטות הללו, אך לא את כולן.</li>
        <li><i class="icon fas fa-gavel"></i> <strong>חוסר קבילות משפטית:</strong> ברוב המוחלט של בתי המשפט בעולם המערבי, כולל ישראל וארה"ב (ברמה הפדרלית ורמת המדינה ברוב המקרים), תוצאות בדיקת פוליגרף אינן קבילות כראיה בגלל חוסר האמינות המוכח שלה.</li>
    </ul>

    <h3>סיכום: כלי לעוררות, לא לאמת</h3>
    הפוליגרף נותר כלי שנוי במחלוקת. הוא אינו יכול לזהות שקרים אלא רק למדוד עוררות פיזיולוגית, שפרשנותה המדויקת בהקשר של גילוי הונאה היא בעייתית ורגישה לטעויות. השימוש בו נשען על הנחות תאורטיות חלשות וקיימות דרכים להטעות אותו. לכן, הוא אינו מהווה "מכונת אמת" ואינו מקובל ככלי אמין מבחינה מדעית או משפטית לגילוי ודאי של שקרים. הסימולציה שלפניכם נועדה להדגים את המורכבות הזו ולהמחיש מדוע פענוח הגרפים אינו תמיד חד משמעי.

</div>

<style>
    /* Enhanced Styling */
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css');

    #polygraph-app {
        font-family: 'Heebo', sans-serif;
        direction: rtl;
        text-align: right;
        background-color: #ecf0f1; /* Light grey background */
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        display: grid;
        grid-template-areas:
            "main";
        grid-template-columns: 1fr;
        gap: 20px;
        max-width: 1000px; /* Limit width for better readability */
        margin: 20px auto; /* Center the app */
    }

    #polygraph-main {
         display: grid;
         grid-template-areas:
             "scenario graph"
             "questions graph"
             "decision graph"
             "results graph";
         grid-template-columns: 1fr 2fr; /* Scenario/Questions on left, Graph on right */
         gap: 20px;
    }

    .panel {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
    }

    #scenario-area { grid-area: scenario; }
    #questions-area { grid-area: questions; }
    #decision-area { grid-area: decision; }
    #results-area { grid-area: results; }
    #graph-area { grid-area: graph; }


    h2, h3 {
        color: #2c3e50; /* Dark blue */
        margin-top: 0;
        margin-bottom: 15px;
        font-weight: 500;
        display: flex;
        align-items: center;
    }
    h3 .icon { margin-left: 10px; color: #3498db; }
    h2 .icon { margin-left: 10px; color: #3498db; }


    #scenario-text, #subject-text {
        font-size: 1.1em;
        line-height: 1.6;
        color: #555;
        margin-bottom: 15px;
    }
     #subject-text { font-weight: bold; color: #333;}

    .graph-container {
        margin-bottom: 20px;
    }

    .graph-container h4 {
        margin-bottom: 5px;
        color: #333;
        font-weight: 400;
        font-size: 1em;
    }
     .graph-container h4 .unit {
         font-size: 0.8em;
         color: #777;
         font-weight: normal;
     }

    canvas {
        border: 1px solid #bdc3c7; /* Light grey border */
        display: block;
        margin-top: 5px;
        background-color: #fdfdfe; /* Off-white background */
        border-radius: 4px;
    }

    #question-buttons {
        display: flex;
        flex-direction: column;
        gap: 12px;
        margin-top: 15px;
    }

    .primary-button, .secondary-button, .decision-button {
        padding: 12px 20px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        font-weight: 500;
        transition: background-color 0.2s ease, transform 0.1s ease, box-shadow 0.2s ease;
        display: flex;
        align-items: center;
        justify-content: center;
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
    }
     .primary-button .icon, .secondary-button .icon, .decision-button .icon { margin-left: 8px; }


    .primary-button {
        background-color: #3498db; /* Peter River blue */
        color: white;
    }

    .primary-button:hover:not(:disabled) {
        background-color: #2980b9; /* Darker blue */
        transform: translateY(-1px);
         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

     .primary-button:active:not(:disabled) {
         transform: translateY(0);
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
     }

    .primary-button:disabled {
        background-color: #bdc3c7; /* Silver */
        cursor: not-allowed;
         box-shadow: none;
    }

     .secondary-button {
        display: block; /* For the toggle button */
        width: fit-content;
        margin: 20px auto;
        background-color: #95a5a6; /* Concrete grey */
        color: white;
     }
     .secondary-button:hover {
         background-color: #7f8c8d; /* Darker concrete */
     }

    .decision-button {
        padding: 12px 25px;
        margin-left: 10px; /* Adjust margin for RTL */
        font-weight: 700;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
    }
     .decision-button:last-child { margin-left: 0; margin-right: 10px; }


    .danger-button { background-color: #e74c3c; color: white; } /* Alizarin red */
    .danger-button:hover { background-color: #c0392b; } /* Darker red */

    .success-button { background-color: #2ecc71; color: white; } /* Emerald green */
    .success-button:hover { background-color: #27ae60; } /* Darker green */

    #restart-simulation { /* Specific styling for restart button */
         margin-top: 20px;
         display: block; /* Make it a block element */
         width: fit-content;
         margin-left: auto; /* Push to the left in RTL */
         margin-right: 0;
    }


    .hidden {
        display: none;
    }

    #explanation {
        border: 1px solid #bdc3c7;
        padding: 30px;
        margin-top: 20px;
        background-color: #ffffff;
        border-radius: 8px;
        direction: rtl;
        text-align: right;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
    }

    #explanation h2, #explanation h3 {
        color: #2c3e50;
        margin-bottom: 15px;
        margin-top: 20px;
        font-weight: 500;
    }
     #explanation h2 .icon, #explanation h3 .icon { margin-left: 10px; color: #2ecc71; }


    #explanation ul {
        margin-bottom: 20px;
        padding-right: 20px; /* Add padding for RTL list items */
        list-style: disc; /* Use disc for list items */
    }

    #explanation li {
        margin-bottom: 10px;
        line-height: 1.6;
        color: #555;
        display: list-item; /* Ensure li behaves as list item */
    }
    #explanation li .icon { margin-left: 8px; color: #3498db; }
    #explanation li ul { margin-top: 10px; margin-bottom: 10px; } /* Nested list spacing */
    #explanation li ul li .icon { color: #e74c3c; } /* Red icon for bullet points */


    .insight {
        margin-bottom: 15px;
        padding: 15px;
        background-color: #ecf0f1; /* Light grey */
        border-right: 4px solid #3498db; /* Blue left border for RTL */
        border-radius: 4px;
        line-height: 1.5;
        color: #333;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    }
     .insight strong { color: #2c3e50; }
     .insight .icon { margin-left: 10px; color: #f39c12; } /* Orange icon */
      .insight:last-child { margin-bottom: 0; }


     .instruction {
         font-size: 0.95em;
         color: #777;
         margin-bottom: 10px;
     }

    .feedback {
         margin-top: 15px;
         padding: 10px;
         background-color: #fff9e6; /* Light yellow */
         border: 1px solid #ffeeba; /* Yellow border */
         color: #856404; /* Dark yellow text */
         border-radius: 4px;
         text-align: center;
         font-weight: bold;
    }

    .graph-legend {
        margin-top: 20px;
        text-align: center;
        font-size: 0.9em;
        color: #555;
    }
    .legend-item {
        display: inline-flex;
        align-items: center;
        margin: 0 10px;
    }
    .legend-color {
        display: inline-block;
        width: 15px;
        height: 15px;
        border-radius: 3px;
        margin-left: 5px; /* Space between color box and text in RTL */
        border: 1px solid #ccc;
    }

    /* Responsive Adjustments */
    @media (max-width: 768px) {
        #polygraph-main {
            grid-template-areas:
                "scenario"
                "graph"
                "questions"
                "decision"
                "results";
            grid-template-columns: 1fr; /* Stack columns on small screens */
        }
        canvas { width: 100%; height: auto; } /* Make canvas responsive */
        .decision-button {
             width: calc(50% - 15px); /* Make decision buttons take half width */
             margin-left: 10px;
             margin-right: 0;
        }
         .decision-button:last-child { margin-left: 0; margin-right: 10px; }
        #decision-area { display: flex; justify-content: center; } /* Center buttons */
    }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const scenarioText = document.getElementById('scenario-text');
        const subjectText = document.getElementById('subject-text');
        const hrCanvas = document.getElementById('hr-graph');
        const respCanvas = document.getElementById('resp-graph');
        const gsrCanvas = document.getElementById('gsr-graph');
        const questionButtons = document.querySelectorAll('.question-button');
        const questionCounterSpan = document.getElementById('question-counter');
        const questionLimitSpan = document.getElementById('question-limit');
        const decisionArea = document.getElementById('decision-area');
        const resultsArea = document.getElementById('results-area');
        const decideLieButton = document.getElementById('decide-lie');
        const decideTruthButton = document.getElementById('decide-truth');
        const trueStatePara = document.getElementById('true-state');
        const userDecisionPara = document.getElementById('user-decision');
        const outcomePara = document.getElementById('outcome');
        const restartButton = document.getElementById('restart-simulation');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');
        const questionFeedback = document.getElementById('question-feedback');

        const ctxHR = hrCanvas.getContext('2d');
        const ctxResp = respCanvas.getContext('2d');
        const ctxGSR = gsrCanvas.getContext('2d');

        // Make canvases responsive while maintaining aspect ratio defined in HTML
         const setCanvasSize = () => {
             const container = hrCanvas.parentElement;
             const width = container.clientWidth; // Get parent width
             const aspectRatio = hrCanvas.height / hrCanvas.width;
             hrCanvas.width = respCanvas.width = gsrCanvas.width = width;
             hrCanvas.height = respCanvas.height = gsrCanvas.height = width * aspectRatio;
             // Redraw graphs if data exists
             if (graphData.hr.length > 0) {
                  drawGraph(ctxHR, graphData.hr, '#e74c3c', hrCanvas.width, hrCanvas.height);
                  drawGraph(ctxResp, graphData.resp, '#3498db', respCanvas.width, respCanvas.height);
                  drawGraph(ctxGSR, graphData.gsr, '#2ecc71', gsrCanvas.width, gsrCanvas.height);
             } else {
                 // Draw only baseline if no data
                  drawBaseline(ctxHR, hrCanvas.width, hrCanvas.height);
                  drawBaseline(ctxResp, respCanvas.width, respCanvas.height);
                  drawBaseline(ctxGSR, gsrCanvas.width, gsrCanvas.height);
             }
         };
        window.addEventListener('resize', setCanvasSize);


        const maxQuestions = 10;
        let currentQuestionCount = 0;
        let currentScenario = null;
        let graphData = { hr: [], resp: [], gsr: [] }; // Array of arrays for each question's data points

        const scenarios = [
            {
                id: 1,
                scenario: "חפץ יקר ערך נעלם מחדר המשרד המשותף. רק אתה והנבדק הייתם שם בשעה שהחפץ נעלם.",
                subject: "הנבדק טוען בתוקף שאינו יודע היכן החפץ.",
                isLying: false // סימולציה: הנבדק אמר אמת
            },
             {
                id: 2,
                scenario: "הייתה תקלה במערכת המחשוב שגרמה נזק. רק למספר מצומצם של עובדים, כולל הנבדק, הייתה גישה למערכת בזמן התקלה.",
                subject: "הנבדק מכחיש שנגע במערכת לפני התקלה.",
                isLying: true // סימולציה: הנבדק שיקר
            },
             {
                id: 3,
                scenario: "נמצא מידע חסוי שהודלף. הנבדק היה אחד מהבודדים שנחשפו למידע זה לפני ההדלפה.",
                subject: "הנבדק נשבע שלא שיתף את המידע עם אף אחד.",
                isLying: true // סימולציה: הנבדק שיקר
            },
             {
                id: 4,
                scenario: "סכום כסף קטן נעלם מהקופה המשותפת בחדר הפסקה. מספר עובדים היו שם, ביניהם הנבדק.",
                subject: "הנבדק אומר שלא ראה את הכסף ולא נגע בו.",
                isLying: false // סימולציה: הנבדק אמר אמת
            }
        ];

        function getRandomScenario() {
            const randomIndex = Math.floor(Math.random() * scenarios.length);
            return scenarios[randomIndex];
        }

        function drawBaseline(ctx, width, height) {
            ctx.clearRect(0, 0, width, height);
            ctx.beginPath();
            ctx.moveTo(0, height / 2);
            ctx.lineTo(width, height / 2);
            ctx.strokeStyle = '#bdc3c7'; // Light grey
            ctx.lineWidth = 1;
            ctx.stroke();
        }

        function clearGraphs() {
            graphData = { hr: [], resp: [], gsr: [] };
            setCanvasSize(); // Redraw baselines
        }

        // Function to draw the graph data with animation
        function drawGraph(ctx, dataSeries, color, width, height) {
             ctx.clearRect(0, 0, width, height);
             drawBaseline(ctx, width, height); // Draw baseline first

             if (dataSeries.length === 0) return;

            const totalPoints = dataSeries.reduce((sum, qData) => sum + qData.length, 0);
            if (totalPoints === 0) return; // Should not happen if dataSeries is not empty, but safety check

             const segmentWidth = width / (maxQuestions * 20); // Assume ~20 points per question simulation

             ctx.beginPath();
             let currentX = 0;
             let currentY = height / 2; // Start at baseline

             ctx.moveTo(currentX, currentY);

             dataSeries.forEach(qData => {
                  qData.forEach((point, pointIndex) => {
                      currentX += width / (maxQuestions * qData.length); // Move X across the question segment
                      const y = height / 2 - (point / 100) * (height * 0.4); // Scale point (0-100) to +/- 40% height
                      ctx.lineTo(currentX, y);
                  });
             });

             ctx.strokeStyle = color;
             ctx.lineWidth = 2.5; // Thicker line
             ctx.lineJoin = 'round'; // Rounded joints
             ctx.lineCap = 'round'; // Rounded caps
             ctx.stroke();
        }


        function generateResponse(type, isLying) {
            const numPoints = 30; // Simulate 30 data points per question
            let hrData = [];
            let respData = [];
            let gsrData = [];

            const baseNeutral = 10; // Baseline noise/response
            const baseControl = 30; // Base response for control questions
            const baseRelevantLie = 70; // Base response for relevant question when lying
            const baseRelevantTruth = 20; // Base response for relevant question when truthful

            let peakValueHR, peakValueResp, peakValueGSR;

            if (type === 'neutral') {
                peakValueHR = baseNeutral;
                peakValueResp = baseNeutral;
                peakValueGSR = baseNeutral;
            } else if (type === 'control') {
                peakValueHR = baseControl + Math.random() * 20; // 30-50
                peakValueResp = baseControl + Math.random() * 20;
                peakValueGSR = baseControl + Math.random() * 20;
            } else if (type === 'relevant') {
                if (isLying) {
                    peakValueHR = baseRelevantLie + Math.random() * 25; // 70-95
                    peakValueResp = baseRelevantLie + Math.random() * 25;
                    peakValueGSR = baseRelevantLie + Math.random() * 25;
                } else {
                    peakValueHR = baseRelevantTruth + Math.random() * 20; // 20-40
                    peakValueResp = baseRelevantTruth + Math.random() * 20;
                    peakValueGSR = baseRelevantTruth + Math.random() * 20;

                    // Introduce variability: Sometimes truthful response is high (anxiety, question wording)
                     if (Math.random() < 0.3) { // 30% chance of higher truthful response
                         const anxietySpike = 30 + Math.random() * 30; // Add 30-60
                          peakValueHR += anxietySpike;
                          peakValueResp += anxietySpike;
                          peakValueGSR += anxietySpike;
                     }
                }
            }

            // Generate smooth-ish data points peaking and returning to baseline
            for (let i = 0; i < numPoints; i++) {
                const progress = i / (numPoints - 1); // 0 to 1
                // Use a function that peaks in the middle, e.g., sine wave or quadratic
                const influence = Math.sin(progress * Math.PI); // Peaks at progress=0.5

                const noise = (Math.random() - 0.5) * 8; // Add +/- 4 noise

                hrData.push(Math.max(0, (baseNeutral + (peakValueHR - baseNeutral) * influence) + noise));
                respData.push(Math.max(0, (baseNeutral + (peakValueResp - baseNeutral) * influence) + noise));
                gsrData.push(Math.max(0, (baseNeutral + (peakValueGSR - baseNeutral) * influence) + noise));
            }

             // Cap values at 100 for scaling
             hrData = hrData.map(v => Math.min(100, v));
             respData = respData.map(v => Math.min(100, v));
             gsrData = gsrData.map(v => Math.min(100, v));


            return { hr: hrData, resp: respData, gsr: gsrData };
        }

        // Function to animate drawing a single question's response
        function animateDraw(ctx, fullData, color, width, height, duration = 1500) { // duration in ms
            const startTime = performance.now();
            const dataPoints = fullData; // The array of points for this question

            const animate = (currentTime) => {
                const elapsedTime = currentTime - startTime;
                const progress = Math.min(elapsedTime / duration, 1); // Progress 0 to 1

                // Determine how many points to draw based on progress
                const pointsToDraw = Math.ceil(progress * dataPoints.length);

                // Draw the baseline and previously drawn question data
                 drawBaseline(ctx, width, height);
                 // Draw previous questions' data first
                 const graphType = (color === '#e74c3c' ? 'hr' : color === '#3498db' ? 'resp' : 'gsr');
                 const previousDataSeries = graphData[graphType].slice(0, graphData[graphType].length - 1);
                 let currentX = 0;
                 let currentY = height / 2;
                 ctx.beginPath();
                 ctx.moveTo(currentX, currentY);
                 previousDataSeries.forEach(qData => {
                      qData.forEach(point => {
                           currentX += width / (maxQuestions * qData.length);
                           const y = height / 2 - (point / 100) * (height * 0.4);
                           ctx.lineTo(currentX, y);
                      });
                 });
                 ctx.strokeStyle = color;
                 ctx.lineWidth = 2.5;
                 ctx.lineJoin = 'round';
                 ctx.lineCap = 'round';
                 ctx.stroke();


                 // Now draw the current question's data based on progress
                 ctx.beginPath();
                 // Start drawing from where the previous data ended
                 const startXCurrentQuestion = width / maxQuestions * (graphData[graphType].length - 1);
                 ctx.moveTo(startXCurrentQuestion, currentY); // Start from the end of the previous segment or baseline


                 for (let i = 0; i < pointsToDraw; i++) {
                     const x = startXCurrentQuestion + (i / (dataPoints.length - 1)) * (width / maxQuestions);
                     const y = height / 2 - (dataPoints[i] / 100) * (height * 0.4);
                     ctx.lineTo(x, y);
                     currentY = y; // Update currentY for the next point
                 }


                 ctx.strokeStyle = color;
                 ctx.lineWidth = 2.5;
                 ctx.lineJoin = 'round';
                 ctx.lineCap = 'round';
                 ctx.stroke();

                if (progress < 1) {
                    requestAnimationFrame(animate);
                } else {
                    // Animation complete, ensure the full line is drawn and re-enable buttons
                     drawGraph(ctx, graphData[graphType], color, width, height);
                     checkAnimationComplete();
                }
            };

             requestAnimationFrame(animate);
        }

        let animationsRunning = 0;

        function startQuestionAnimation(response) {
             animationsRunning = 3; // One for each graph
             questionFeedback.textContent = '...מנתח תגובה';
             questionFeedback.classList.remove('hidden');
             questionButtons.forEach(button => button.disabled = true); // Disable buttons during animation

             const hrData = response.hr;
             const respData = response.resp;
             const gsrData = response.gsr;

             graphData.hr.push(hrData);
             graphData.resp.push(respData);
             graphData.gsr.push(gsrData);

             // Animate each graph
             animateDraw(ctxHR, hrData, '#e74c3c', hrCanvas.width, hrCanvas.height);
             animateDraw(ctxResp, respData, '#3498db', respCanvas.width, respCanvas.height);
             animateDraw(ctxGSR, gsrData, '#2ecc71', gsrCanvas.width, gsrCanvas.height);
        }

        function checkAnimationComplete() {
            animationsRunning--;
            if (animationsRunning <= 0) {
                currentQuestionCount++;
                updateQuestionCounter();
                questionFeedback.classList.add('hidden');
                if (currentQuestionCount < maxQuestions) {
                    questionButtons.forEach(button => button.disabled = false); // Re-enable buttons
                }
            }
        }


        function updateQuestionCounter() {
            questionCounterSpan.textContent = currentQuestionCount;
             if (currentQuestionCount >= maxQuestions) {
                 questionButtons.forEach(button => button.disabled = true);
                 decisionArea.classList.remove('hidden');
             } else {
                 questionButtons.forEach(button => button.disabled = false);
                 decisionArea.classList.add('hidden');
             }
        }

        function showResults(userDecidedLie) {
            const isSubjectLying = currentScenario.isLying;
            let outcomeText = '';

            if (userDecidedLie === isSubjectLying) {
                outcomeText = "<strong class='success-text'><i class='icon fas fa-check-double'></i> המסקנה שלך תואמת את 'האמת' בסימולציה!</strong>";
                if (isSubjectLying) {
                    outcomeText += " (זיהוי נכון של שקרן)";
                } else {
                     outcomeText += " (זיהוי נכון של דובר אמת)";
                }
                 outcomePara.style.color = '#27ae60'; /* Green */
            } else {
                 outcomeText = "<strong class='danger-text'><i class='icon fas fa-exclamation-triangle'></i> המסקנה שלך אינה תואמת את 'האמת' בסימולציה.</strong>";
                 if (userDecidedLie) {
                     outcomeText += " (תוצאה חיובית כוזבת - False Positive)";
                     outcomeText += "<br>זיהית את הנבדק כשקרן, אך בסימולציה הוא אמר אמת. זכור שפוליגרף מודד עוררות, לא שקר! תוצאה זו יכולה לקרות במציאות עקב לחץ גבוה של הנבדק, עצבנות שאינה קשורה לשאלה, או תגובה חזקה לשאלות בקרה שאינן מצביעות בהכרח על שקר בנושא המרכזי.";
                 } else {
                      outcomeText += " (תוצאה שלילית כוזבת - False Negative)";
                      outcomeText += "<br>זיהית את הנבדק כדובר אמת, אך בסימולציה הוא שיקר. גם זה קורה במציאות! זה יכול לקרות אם השקרן מצליח לשלוט בתגובותיו, אינו חווה מספיק מתח, או שהתגובות הפיזיולוגיות שלו היו חלשות או מעורפלות.";
                 }
                 outcomePara.style.color = '#c0392b'; /* Red */
            }

            trueStatePara.innerHTML = `<strong>'האמת' בסימולציה:</strong> הנבדק ${isSubjectLying ? 'שיקר לגבי האירוע המרכזי' : 'אמר אמת לגבי האירוע המרכזי'}.`;
            userDecisionPara.innerHTML = `<strong>ההחלטה שלך:</strong> הנבדק ${userDecidedLie ? 'שיקר' : 'אמר אמת'}.`;
            outcomePara.innerHTML = outcomeText;

            resultsArea.classList.remove('hidden');
        }


        function startNewSimulation() {
            currentScenario = getRandomScenario();
            scenarioText.textContent = currentScenario.scenario;
            subjectText.textContent = currentScenario.subject;
            currentQuestionCount = 0;
            questionLimitSpan.textContent = maxQuestions;
            clearGraphs();
            updateQuestionCounter();
            decisionArea.classList.add('hidden');
            resultsArea.classList.add('hidden');
             questionFeedback.classList.add('hidden');
             // Re-enable buttons
             questionButtons.forEach(button => button.disabled = false);
        }

        // Event Listeners
        questionButtons.forEach(button => {
            button.addEventListener('click', () => {
                if (currentQuestionCount < maxQuestions && animationsRunning === 0) { // Prevent clicks while animating
                    const type = button.getAttribute('data-type');
                    const response = generateResponse(type, currentScenario.isLying);
                    startQuestionAnimation(response);
                }
            });
        });

        decideLieButton.addEventListener('click', () => {
            showResults(true);
            decisionArea.classList.add('hidden');
        });

        decideTruthButton.addEventListener('click', () => {
            showResults(false);
            decisionArea.classList.add('hidden');
        });

        restartButton.addEventListener('click', startNewSimulation);

         toggleExplanationButton.addEventListener('click', () => {
            explanationDiv.classList.toggle('hidden');
            // Scroll to explanation if shown, or back to app if hidden
            if (!explanationDiv.classList.contains('hidden')) {
                 explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
            } else {
                 document.getElementById('polygraph-app').scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
         });


        // Initial setup
        startNewSimulation();
        explanationDiv.classList.add('hidden'); // Ensure explanation is hidden on load
        setCanvasSize(); // Set initial canvas size based on container
    });
</script>
---