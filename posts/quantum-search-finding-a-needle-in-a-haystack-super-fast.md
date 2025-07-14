---
title: "חיפוש קוונטי: למצוא מחט בערימת שחת (סופר-מהיר!)"
english_slug: quantum-search-finding-a-needle-in-a-haystack-super-fast
category: "פיזיקה"
tags: ["מחשוב קוונטי", "אלגוריתם גרובר", "חיפוש קוונטי", "אלגוריתמים", "מכניקת הקוונטים"]
---
# חיפוש קוונטי: למצוא מחט בערימת שחת (סופר-מהיר!)
דמיינו שיש לכם ערימת שחת ענקית - מיליוני קשים זהים למראה - ואתם צריכים למצוא בתוכה מחט אחת קטנה. אין דרך לדעת איפה היא, פשוט צריך להתחיל לחפש. בחיפוש רגיל, קלאסי, תצטרכו לבדוק קש-קש, אחד אחרי השני. זה ייקח המון זמן, במיוחד כשהערימה ענקית!

אבל מה אם הייתם יכולים לרתום את כוחותיה המוזרים של מכניקת הקוונטים כדי להאיץ את החיפוש הזה באופן דרמטי? אלגוריתם גרובר עושה בדיוק את זה! הוא לא מוצא את המחט ברגע, אבל הוא יכול למצוא אותה עם הסתברות גבוהה הרבה יותר מהר מכל חיפוש קלאסי - בערך ב-√N צעדים במקום N צעדים (כאשר N הוא גודל ערימת השחת). זהו יתרון קוונטי עוצמתי!

הסימולציה הזו מאפשרת לכם לחוות את פעולת אלגוריתם גרובר צעד אחר צעד. במקום ערימת שחת, יש לנו רשימה לא ממויינת של 'מצבים' אפשריים (קשיות), ואתם בוחרים את 'מצב המטרה' (המחט). אנו נציג את ההסתברות למצוא כל 'קש' ברשימה אם נבצע מדידה קוונטית. בתחילה, כל המצבים שווים בהסתברותם, כמו בסופרפוזיציה אחידה. בכל 'צעד קוונטי' (איטרציה של גרובר), תראו כיצד אלגוריתם גרובר מגביר באופן קסום את ההסתברות למצוא את מצב המטרה, ומוריד את ההסתברות למצוא את שאר המצבים!

<div id="quantumSearchApp">
    <div class="app-header">
        <h2>סימולציית חיפוש קוונטי (גרובר)</h2>
        <p class="subtitle">כיצד מחשב קוונטי יכול להאיץ חיפוש במאגר לא ממויין?</p>
    </div>
    <div class="controls-area">
        <div class="control-group">
            <label for="listSize">גודל הרשימה (N):</label>
            <select id="listSize">
                <option value="8">8</option>
                <option value="16">16</option>
                <option value="32">32</option>
                <option value="64">64</option>
                <option value="128">128</option>
            </select>
        </div>
        <div class="control-group">
            <label for="targetIndex">האיבר המבוקש (אינדקס 0 עד N-1):</label>
            <select id="targetIndex"></select>
        </div>
        <div class="control-group button-group">
            <button id="resetBtn" class="control-button">התחל מחדש</button>
            <button id="stepBtn" class="control-button">צעד גרובר קוונטי</button>
            <button id="autoRunBtn" class="control-button">ריצה אוטומטית</button>
            <button id="measureBtn" class="control-button measure-button">מדידה קוונטית! ⚛️</button>
        </div>
        <div class="steps-info">
            <p>צעדים קוונטיים שבוצעו: <span id="quantumSteps">0</span></p>
            <p>צעדים אופטימליים (כדי למקסם סיכוי): <span id="optimalSteps">-</span></p>
            <p>צעדים קלאסיים (ממוצע צפוי ל-N): <span id="classicalSteps">0</span></p>
        </div>
    </div>
    <div class="visualization-area">
        <h3>התפלגות ההסתברויות (למדידה):</h3>
        <div id="probabilityChart"></div>
        <p class="chart-label">אינדקס האיבר ברשימה</p>
         <div id="measurementResult" class="result-message"></div>
    </div>
</div>

<style>
    #quantumSearchApp {
        font-family: 'Arial', sans-serif;
        direction: rtl;
        display: flex;
        flex-direction: column;
        gap: 25px;
        padding: 25px;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        max-width: 900px;
        margin: 30px auto;
        background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
    }

    #quantumSearchApp .app-header {
        text-align: center;
        margin-bottom: 15px;
    }

    #quantumSearchApp h2 {
        color: #2c3e50;
        margin: 0 0 5px 0;
        font-size: 1.8em;
        font-weight: bold;
    }

    #quantumSearchApp .subtitle {
        color: #5a6a7a;
        font-size: 1em;
        margin-top: 0;
    }

    #quantumSearchApp .controls-area {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        align-items: flex-end;
        padding-bottom: 20px;
        border-bottom: 1px solid #d0d0d0;
    }

    #quantumSearchApp .control-group {
        display: flex;
        flex-direction: column;
        gap: 8px;
    }

     #quantumSearchApp .control-group.button-group {
         flex-direction: row;
         flex-wrap: wrap;
         gap: 10px;
     }

    #quantumSearchApp label {
        font-weight: bold;
        font-size: 0.95em;
        color: #34495e;
    }

    #quantumSearchApp select,
    #quantumSearchApp .control-button {
        padding: 10px 15px;
        border: 1px solid #bdc3c7;
        border-radius: 6px;
        font-size: 1em;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    #quantumSearchApp select {
         background-color: #ecf0f1;
         color: #34495e;
    }

    #quantumSearchApp select:focus {
        border-color: #3498db;
        outline: none;
        box-shadow: 0 2px 6px rgba(52, 152, 219, 0.2);
    }


    #quantumSearchApp .control-button {
        background-color: #3498db;
        color: white;
        border-color: #3498db;
        font-weight: bold;
    }

    #quantumSearchApp .control-button:hover:not(:disabled) {
        background-color: #2980b9;
        border-color: #2980b9;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
     #quantumSearchApp .control-button:active:not(:disabled) {
         background-color: #2471a3;
         border-color: #2471a3;
         box-shadow: inset 0 2px 4px rgba(0,0,0,0.1);
     }

    #quantumSearchApp .control-button:disabled {
        background-color: #cccccc;
        border-color: #cccccc;
        color: #666666;
        cursor: not-allowed;
        box-shadow: none;
    }

    #quantumSearchApp .measure-button {
         background-color: #e67e22; /* Orange */
         border-color: #e67e22;
         display: none; /* Initially hidden */
    }
    #quantumSearchApp .measure-button:hover:not(:disabled) {
         background-color: #d35400;
         border-color: #d35400;
    }

    #quantumSearchApp .steps-info {
        margin-left: auto;
        font-size: 0.95em;
        color: #34495e;
        line-height: 1.6;
        min-width: 180px; /* Ensure it stays on the right */
    }

    #quantumSearchApp .steps-info span {
        font-weight: bold;
        color: #2980b9;
    }
     #quantumSearchApp .steps-info #optimalSteps {
         color: #27ae60; /* Green for optimal */
     }

    #quantumSearchApp .visualization-area {
        text-align: center;
    }

    #quantumSearchApp .visualization-area h3 {
         margin-top: 0;
         margin-bottom: 15px;
         color: #2c3e50;
         font-size: 1.4em;
    }

    #probabilityChart {
        display: flex;
        align-items: flex-end;
        height: 250px; /* Taller chart */
        border-left: 2px solid #bdc3c7;
        border-bottom: 2px solid #bdc3c7;
        padding: 0 2px;
        gap: 1px; /* Very little space between bars for density */
        background-color: #ffffff;
        box-sizing: border-box;
        position: relative; /* For absolute positioning of labels/tooltips */
        overflow: hidden; /* Hide potential overflow from labels */
    }

    .probability-bar {
        flex-grow: 1;
        background-color: #3498db; /* Blue color for bars */
        margin: 0;
        position: relative;
        display: flex;
        justify-content: center;
        align-items: flex-end;
        box-sizing: border-box;
        border: 1px solid rgba(0,0,0,0.05);
        transition: height 0.5s ease-out, background-color 0.3s ease; /* Smooth height and color transitions */
        bottom: -2px; /* Align with bottom border */
    }

    .probability-bar.target {
        background-color: #e74c3c; /* Red color for target */
        border-color: #c0392b;
    }

     .probability-bar:hover {
        opacity: 0.9;
        cursor: help; /* Indicate tooltip/info */
     }

    .bar-label {
        position: absolute;
        bottom: 5px; /* Inside the bar, near the bottom */
        font-size: 0.8em;
        color: white; /* White text for visibility on dark bars */
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        font-weight: bold;
        opacity: 0; /* Initially hidden */
        transition: opacity 0.3s ease;
    }
    .probability-bar:hover .bar-label {
         opacity: 1; /* Show on hover */
    }
     /* Adjust label position if bar is too short */
     .probability-bar.short-bar .bar-label {
          position: relative; /* Reset positioning for very short bars */
          bottom: auto;
          margin-bottom: 3px;
          color: #333; /* Darker text for light background */
          text-shadow: none;
          font-size: 0.7em;
     }


     .chart-index-labels {
         display: flex;
         width: 100%;
         justify-content: space-between;
         padding: 0 5px; /* Align with chart padding */
         box-sizing: border-box;
         font-size: 0.8em;
         color: #555;
         margin-top: 5px;
     }
     .chart-index-label {
          flex-grow: 1;
          text-align: center;
     }
     /* Only show labels for smaller N */
     #probabilityChart[data-size="8"] + .chart-label + .chart-index-labels .chart-index-label { display: block; }
     #probabilityChart[data-size="16"] + .chart-label + .chart-index-labels .chart-index-label:nth-child(odd) { display: block; }
     #probabilityChart[data-size="32"] + .chart-label + .chart-index-labels .chart-index-label:nth-child(4n) { display: block; }
      #probabilityChart[data-size="64"] + .chart-label + .chart-index-labels .chart-index-label:nth-child(8n) { display: block; }
      #probabilityChart[data-size="128"] + .chart-label + .chart-index-labels .chart-index-label:nth-child(16n) { display: block; }
      #probabilityChart[data-size="8"] + .chart-label + .chart-index-labels .chart-index-label:nth-child(n) { text-align: center; }


     .chart-label {
         margin-top: 5px;
         font-size: 0.9em;
         color: #555;
     }
      #measurementResult {
         margin-top: 20px;
         font-size: 1.2em;
         font-weight: bold;
         color: #2c3e50;
         min-height: 1.5em; /* Reserve space */
         text-align: center;
      }
      #measurementResult.success {
          color: #27ae60; /* Green */
          animation: pulse-success 1s ease-in-out infinite;
      }
       #measurementResult.fail {
          color: #c0392b; /* Red */
       }

    @keyframes pulse-success {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.05); opacity: 0.9; }
        100% { transform: scale(1); opacity: 1; }
    }


    #explanationToggle {
        display: block;
        margin: 30px auto 20px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        background-color: #9b59b6; /* Purple */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
    }

    #explanationToggle:hover {
        background-color: #8e44ad;
    }
     #explanationToggle:active {
         transform: scale(0.98);
     }

    #explanationContent {
        display: none;
        margin-top: 20px;
        padding: 25px;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        background-color: #ffffff;
        line-height: 1.7;
        color: #34495e;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
    }

    #explanationContent h3 {
        color: #3498db; /* Blue */
        margin-top: 15px;
        margin-bottom: 10px;
        font-size: 1.3em;
        border-bottom: 1px dashed #bdc3c7;
        padding-bottom: 5px;
    }

    #explanationContent p {
        margin-bottom: 15px;
    }
     #explanationContent ul {
         margin-bottom: 15px;
         padding-right: 20px;
     }
      #explanationContent li {
          margin-bottom: 8px;
      }

</style>
<div class="chart-index-labels" id="chartIndexLabels"></div>

<button id="explanationToggle">הצג הסבר על אלגוריתם גרובר</button>

<div id="explanationContent">
    <h3>האתגר הקלאסי: חיפוש במאגר ענק ולא מסודר</h3>
    <p>דמיינו ספרייה ענקית שבה הספרים זרוקים על הרצפה בלי שום סדר - לא לפי שם, לא לפי נושא, פשוט ערימה כאוטית. אם אתם מחפשים ספר ספציפי, הדרך היחידה שלכם היא פשוט לעבור על כל ספר ולבדוק אם זה הספר שאתם רוצים. במקרה הכי גרוע, הספר שלכם יהיה האחרון שתבדקו, ויקח לכם לבדוק את כל הספרים (N). בממוצע, אם הספר קיים, תצטרכו לבדוק כחצי מהספרים (N/2). זה מה שנקרא "סיבוכיות זמן לינארית" - הזמן שלוקח לפתור את הבעיה גדל באופן לינארי עם גודל הבעיה (N).</p>

    <h3>המפץ הקוונטי: אלגוריתם גרובר נכנס לתמונה</h3>
    <p>בשנת 1996, לוב גרובר הציג אלגוריתם שמנצל את היכולות הייחודיות של מחשב קוונטי כדי לפתור את בעיית החיפוש הלא-ממויין באופן מהיר משמעותית. במקום N/2 צעדים בממוצע, אלגוריתם גרובר יכול למצוא את הפריט המבוקש עם סיכוי גבוה מאוד לאחר כ-π/4 * √N צעדים. שימו לב! לא √N צעדים *בממוצע* למציאה ודאית, אלא √N צעדים *כדי להעלות את ההסתברות למציאה ודאית*. זהו "יתרון קוונטי ריבועי" בזמן הריצה, והוא הופך בעיות חיפוש בלתי אפשריות מבחינה מעשית במחשבים קלאסיים, לאפשריות במחשבים קוונטיים (עתידיים).</p>

    <h3>איך זה עובד קוונטית? ייצוג, אורקל ואמפליפיקציה</h3>
    <p>במחשב קוונטי, במקום לייצג 'קש' בודד בכל פעם, אנו יכולים לייצג את *כל* הקשים האפשריים במקביל בסופרפוזיציה קוונטית. מתחילים את האלגוריתם במצב שבו לכל 'קש' יש אמפליטודת הסתברות זהה (1/√N), כלומר, סיכוי שווה (1/N) להימדד.</p>

    <h4>1. האורקל הקוונטי (מסמן את המטרה)</h4>
    <p>הצעד הראשון בכל איטרציה של גרובר הוא הפעלת "אורקל" (Oracle). דמיינו את האורקל כקופסה שחורה קוונטית שיודעת לזהות את ה'מחט' (האיבר המבוקש). כשאנחנו מפעילים את האורקל על הסופרפוזיציה, הוא מבצע פעולה עדינה: הוא הופך את ה"פאזה" (המקבילה הקוונטית לסימן חיובי/שלילי, אך כללית יותר) של אמפליטודת ההסתברות של 'קש המטרה' מ- + ל- -. שאר האמפליטודות נשארות ללא שינוי. פעולה זו "מסמנת" את המחט באופן קוונטי, מבלי "לגלות" אותה עדיין.</p>

    <h4>2. הגברת אמפליטודה (מנפחים את סיכוי המטרה)</h4>
    <p>זהו הצעד המרכזי והמגניב! לאחר שהאורקל סימן את המטרה בפאזה הפוכה, אנו מפעילים פעולה שנקראת "הגברת אמפליטודה" (Amplitude Amplification). פעולה זו מורכבת משני חלקים וניתן לחשוב עליה כ"היפוך ביחס לממוצע":
    <ul>
        <li>מחשבים את הממוצע של *כל* האמפליטודות הנוכחיות (הממוצע כרגע נמוך בגלל שהאמפליטודה של המטרה הפכה שלילית).</li>
        <li>עבור כל 'קש' (כל מצב), האמפליטודה החדשה שלו מחושבת כך: `2 * ממוצע_נוכחי - אמפליטודה_קודמת`.</li>
    </ul>
    מה קורה פה? האמפליטודה השלילית של המטרה, הנמוכה מהממוצע, הופכת (בפעולה זו) לאמפליטודה חיובית וגבוהה יותר מהממוצע. האמפליטודות החיוביות של שאר המצבים, הגבוהות מהממוצע, הופכות לאמפליטודות חיוביות ונמוכות יותר. התוצאה היא שהאמפליטודה של 'קש המטרה' גדלה משמעותית, בעוד האמפליטודות של שאר הקשים קטנות!</p>

    <h3>הצד הוויזואלי: סיבוב במרחב</h3>
    <p>אפשר לדמיין את פעולת גרובר כסיבוב. מצב המטרה וסופרפוזיציה של כל שאר המצבים מגדירים מישור בתוך המרחב הקוונטי העצום. המצב ההתחלתי (סופרפוזיציה אחידה) הוא וקטור במישור הזה. האורקל מבצע שיקוף במישור זה (היפוך פאזה של המטרה), ופעולת הגברת האמפליטודה מבצעת שיקוף נוסף (ביחס למצב ההתחלתי). רצף שני השיקופים האלו שקול לסיבוב קטן של הווקטור הכולל של המצב הקוונטי *בכיוון* וקטור המטרה. בכל צעד, הווקטור מסתובב עוד קצת ומתקרב יותר למטרה, מה שמגדיל את האמפליטודה שלה.</p>

    <h3>המספר הקסום: √N</h3>
    <p>הסיבוב בכל צעד הוא קטן, אך עקבי. הזווית של הסיבוב תלויה בגודל N. כדי להגיע הכי קרוב שאפשר לווקטור המטרה (שבו האמפליטודה של המטרה כמעט 1), נדרשים כ-π/4 * √N צעדים. אם ממשיכים לבצע צעדים מעבר למספר האופטימלי, הווקטור ממשיך להסתובב ומתחיל להתרחק מווקטור המטרה, וההסתברות למצוא אותה במדידה תתחיל לרדת שוב. הסימולציה מדגימה זאת!</p>

    <h3>מדידה קוונטית: הרגע הדרמטי</h3>
    <p>לאחר ביצוע מספר צעדים (רצוי סביב המספר האופטימלי), מבצעים מדידה קוונטית. המדידה "מכריחה" את המערכת לבחור מצב אחד מתוך הסופרפוזיציה, והסיכוי שייבחר מצב מסוים פרופורציונלי לריבוע האמפליטודה שלו. מכיוון שאלגוריתם גרובר הגביר את האמפליטודה של מצב המטרה, הסיכוי למדוד דווקא אותו הוא גבוה מאוד בנקודה זו (קרוב ל-1).</p>

    <h3>יתרונות ומגבלות</h3>
    <p>אלגוריתם גרובר אינו "בולט" שורשי לכל בעיה. הוא מתאים לבעיות בהן יש לנו "אורקל" - פונקציה שקל לבדוק האם קלט מסוים הוא הפתרון המבוקש, אך קשה למצוא את הפתרון עצמו. הוא לא יעיל לחיפוש ברשימות ממויינות (שם חיפוש בינארי קלאסי מהיר יותר) וגם לא פותר בעיות מורכבות יותר כמו פירוק לגורמים מהר יותר מאלגוריתם שור. אבל עבור סוגי בעיות חיפוש ספציפיים, כמו פתירת בעיות סיפוק (SAT) או חיפוש במסדי נתונים לא מובנים, הוא מציע שיפור משמעותי והוא אחד האלגוריתמים הקוונטיים הבסיסיים והחשובים ביותר.</p>
</div>

<script>
    const app = document.getElementById('quantumSearchApp');
    const listSizeSelect = document.getElementById('listSize');
    const targetIndexSelect = document.getElementById('targetIndex');
    const resetBtn = document.getElementById('resetBtn');
    const stepBtn = document.getElementById('stepBtn');
    const autoRunBtn = document.getElementById('autoRunBtn');
    const measureBtn = document.getElementById('measureBtn');
    const quantumStepsSpan = document.getElementById('quantumSteps');
    const optimalStepsSpan = document.getElementById('optimalSteps');
    const classicalStepsSpan = document.getElementById('classicalSteps');
    const probabilityChart = document.getElementById('probabilityChart');
    const chartIndexLabelsContainer = document.getElementById('chartIndexLabels');
    const measurementResultDiv = document.getElementById('measurementResult');
    const explanationToggleBtn = document.getElementById('explanationToggle');
    const explanationContentDiv = document.getElementById('explanationContent');

    let N;
    let targetIndex;
    let quantumState; // Array of amplitudes (real numbers for this visualization)
    let quantumSteps;
    let autoRunInterval = null;
    let isMeasured = false;

    // --- Helper function to initialize the state (uniform superposition) ---
    function initializeState() {
        stopAutoRun();
        isMeasured = false;
        N = parseInt(listSizeSelect.value, 10);
        targetIndex = parseInt(targetIndexSelect.value, 10);
        // Initial uniform superposition state (real amplitudes)
        // For visualization clarity, we use real amplitudes here.
        // A true quantum state involves complex numbers, but the amplitude amplification
        // principle is well-represented by this real-valued simplification for Grover's.
        quantumState = Array(N).fill(1 / Math.sqrt(N));
        quantumSteps = 0;

        // Classical comparison: Average steps to find in unsorted list is N/2
        const classicalAvgSteps = Math.floor(N / 2);
        classicalStepsSpan.textContent = classicalAvgSteps;

        // Optimal quantum steps: Approx (PI/4) * sqrt(N)
        const optimalSteps = Math.round((Math.PI / 4) * Math.sqrt(N));
        optimalStepsSpan.textContent = optimalSteps;

        measurementResultDiv.textContent = ''; // Clear previous measurement result
        measurementResultDiv.className = 'result-message'; // Reset class

        updateVisualization();
        updateStepCount();
        updateButtonStates();
        populateChartIndexLabels();
    }

    // --- Populate Target Index Select ---
    function populateTargetSelect() {
        N = parseInt(listSizeSelect.value, 10);
        targetIndexSelect.innerHTML = '';
        for (let i = 0; i < N; i++) {
            const option = document.createElement('option');
            option.value = i;
            option.textContent = i;
            targetIndexSelect.appendChild(option);
        }
        // Ensure the selected target is within the new range or default
        const currentTarget = parseInt(targetIndexSelect.value, 10);
         if (isNaN(currentTarget) || currentTarget >= N) {
             targetIndexSelect.value = 0;
         } else {
             targetIndexSelect.value = currentTarget; // Keep previous if valid
         }
         targetIndex = parseInt(targetIndexSelect.value, 10); // Update global targetIndex
    }

    // --- Populate Chart Index Labels ---
    function populateChartIndexLabels() {
        chartIndexLabelsContainer.innerHTML = '';
        chartIndexLabelsContainer.style.justifyContent = N <= 16 ? 'space-between' : 'flex-start'; // Adjust spacing for many bars
        probabilityChart.dataset.size = N; // Use data attribute for CSS visibility control

        const step = N <= 16 ? 1 : (N <= 32 ? 2 : (N <= 64 ? 4 : 8)); // Control density of labels

        for (let i = 0; i < N; i++) {
             const label = document.createElement('div');
             label.classList.add('chart-index-label');
             if (i % step === 0) {
                 label.textContent = i;
             } else {
                 label.textContent = ''; // Hide
             }
             // Adjust flex-basis to distribute labels somewhat evenly, especially for larger N
             label.style.flexBasis = `${100 / N}%`; // Each label takes proportional space
             label.style.textAlign = 'center';
             chartIndexLabelsContainer.appendChild(label);
         }
    }


    // --- Grover's Oracle: Phase flip for the target state (in this real-valued sim, just sign flip) ---
    function applyOracle() {
        quantumState[targetIndex] *= -1;
    }

    // --- Amplitude Amplification: Reflection about the average ---
    function applyAmplification() {
        const average = quantumState.reduce((sum, amp) => sum + amp, 0) / N;
        quantumState = quantumState.map(amp => 2 * average - amp);
    }

    // --- Perform one Grover iteration ---
    function performGroverStep() {
        if (isMeasured) return; // Cannot step after measuring

        const optimalSteps = Math.round((Math.PI / 4) * Math.sqrt(N));
        // Add a small buffer to allow seeing probability decrease past optimum
        const maxStepsBeforeWarning = optimalSteps + Math.max(5, Math.ceil(optimalSteps * 0.2));

        if (quantumSteps >= maxStepsBeforeWarning) {
             console.warn("Reached approximate optimal steps + buffer. Further steps may decrease probability.");
             // Optional: Disable step button or show a message
             // stepBtn.disabled = true; // Might want to let user see what happens
        }

        applyOracle();
        applyAmplification();
        quantumSteps++;
        updateVisualization();
        updateStepCount();
        updateButtonStates();

         // Check if target probability is very high (optional, for auto-stop hint)
         const probabilities = quantumState.map(amp => amp * amp);
         if (probabilities[targetIndex] > 0.98 && autoRunInterval) {
             stopAutoRun();
             // measurementResultDiv.textContent = 'סיכוי גבוה למצוא את המטרה! מומלץ לבצע מדידה.';
         }
    }

    // --- Simulate Measurement ---
    function performMeasurement() {
         if (isMeasured) return; // Already measured
         stopAutoRun(); // Stop auto-run before measurement

         const probabilities = quantumState.map(amp => amp * amp);
         const totalProbability = probabilities.reduce((sum, p) => sum + p, 0); // Should be close to 1

         // Simulate probabilistic outcome based on probabilities
         let cumulativeProbability = 0;
         const rand = Math.random() * totalProbability; // Use random within the total probability range (should be 0-1)
         let measuredIndex = -1;

         for (let i = 0; i < N; i++) {
             cumulativeProbability += probabilities[i];
             if (rand <= cumulativeProbability) {
                 measuredIndex = i;
                 break;
             }
         }

         isMeasured = true;

         // Update visualization to highlight the measured state
         updateVisualization(measuredIndex);

         // Display result message
         if (measuredIndex === targetIndex) {
             measurementResultDiv.textContent = `🥳 מדידה בוצעה! נמצא האיבר המבוקש במיקום ${measuredIndex}!`;
             measurementResultDiv.className = 'result-message success';
         } else {
             measurementResultDiv.textContent = `😞 מדידה בוצעה. נמצא האיבר ${measuredIndex}. נסו שוב או בצעו עוד צעדים.`;
             measurementResultDiv.className = 'result-message fail';
         }

         updateButtonStates(); // Disable step/auto after measurement
    }


    // --- Update Visualization ---
    function updateVisualization(measuredIndex = -1) {
        probabilityChart.innerHTML = '';
        const probabilities = quantumState.map(amp => amp * amp);
        // Find the maximum probability currently displayed for scaling
        const maxDisplayedProb = Math.max(...probabilities);
        // The initial state has max probability 1/N. Scale relative to that if nothing is high.
        const scaleFactor = 1 / (maxDisplayedProb > 1/N ? maxDisplayedProb : (1/N));


        for (let i = 0; i < N; i++) {
            const bar = document.createElement('div');
            bar.classList.add('probability-bar');
            if (i === targetIndex) {
                bar.classList.add('target');
            }
            if (i === measuredIndex) {
                 bar.classList.add('measured'); // Add a class for the measured bar
            }

            // Scale height relative to max probability (or initial uniform max)
             const heightPercent = probabilities[i] * scaleFactor * 100;
             bar.style.height = `${Math.max(0.5, heightPercent)}%`; // Ensure min height for visibility


            const probPercent = (probabilities[i] * 100).toFixed(1);
             if (probPercent > 5 || N <= 16) { // Show percentage inside for high bars or small N
                 const probLabel = document.createElement('span');
                 probLabel.classList.add('bar-label');
                 probLabel.textContent = `${probPercent}%`;
                 bar.appendChild(probLabel);
                 if (heightPercent < 10 && N > 16) { // Adjust label position for very short bars on large N
                     bar.classList.add('short-bar');
                 }
             }

            // Add title for tooltip on hover
             bar.title = `אינדקס ${i}: הסתברות ${(probabilities[i]*100).toFixed(2)}%`;


            probabilityChart.appendChild(bar);
        }
        // Update index labels below chart if they exist
         populateChartIndexLabels();
    }

    // --- Update Step Count Display ---
    function updateStepCount() {
        quantumStepsSpan.textContent = quantumSteps;
    }

     // --- Update Button States ---
     function updateButtonStates() {
         const isAutoRunning = autoRunInterval !== null;
         stepBtn.disabled = isAutoRunning || isMeasured;
         autoRunBtn.disabled = isMeasured;
         measureBtn.style.display = quantumSteps > 0 && !isMeasured ? 'inline-block' : 'none'; // Show measure after first step
         listSizeSelect.disabled = isAutoRunning || isMeasured;
         targetIndexSelect.disabled = isAutoRunning || isMeasured;

         if (isMeasured) {
             stepBtn.textContent = 'צעד גרובר קוונטי'; // Reset text if auto-run was stopped by measure
             autoRunBtn.textContent = 'ריצה אוטומטית'; // Reset text
         } else if (isAutoRunning) {
             autoRunBtn.textContent = 'עצור ריצה אוטומטית';
         } else {
            autoRunBtn.textContent = 'ריצה אוטומטית';
         }

          // Optional: Indicate recommended steps
          const optimal = Math.round((Math.PI / 4) * Math.sqrt(N));
          if (!isMeasured && quantumSteps > 0) {
               if (quantumSteps < optimal) {
                   stepBtn.textContent = `צעד גרובר קוונטי (${optimal - quantumSteps} נותרו)`;
               } else if (quantumSteps === optimal) {
                   stepBtn.textContent = `צעד גרובר קוונטי (אופטימלי!)`;
               } else {
                    stepBtn.textContent = `צעד גרובר קוונטי (${quantumSteps - optimal} צעדים מעבר לאופטימלי)`;
               }
          } else if (!isMeasured && quantumSteps === 0) {
               stepBtn.textContent = 'צעד גרובר קוונטי';
          }

     }


    // --- Auto Run Logic ---
    function startAutoRun() {
         if (isMeasured) return;
        const stepDuration = N <= 16 ? 300 : (N <= 64 ? 200 : 150); // Faster steps for larger N
        autoRunInterval = setInterval(performGroverStep, stepDuration);
        updateButtonStates();
    }

    function stopAutoRun() {
        if (autoRunInterval) {
            clearInterval(autoRunInterval);
            autoRunInterval = null;
            updateButtonStates();
        }
    }


    // --- Event Listeners ---
    listSizeSelect.addEventListener('change', () => {
        populateTargetSelect(); // Repopulate targets for new size
        initializeState(); // Reset state for new size
    });

    targetIndexSelect.addEventListener('change', () => {
        targetIndex = parseInt(targetIndexSelect.value, 10); // Update target index
        initializeState(); // Reset state for new target
    });

    resetBtn.addEventListener('click', () => {
        initializeState(); // Full reset
    });

    stepBtn.addEventListener('click', () => {
        performGroverStep();
    });

    autoRunBtn.addEventListener('click', () => {
        if (autoRunInterval) {
            stopAutoRun();
        } else {
            startAutoRun();
        }
    });

    measureBtn.addEventListener('click', () => {
        performMeasurement();
    });


     explanationToggleBtn.addEventListener('click', () => {
        const isHidden = explanationContentDiv.style.display === 'none' || explanationContentDiv.style.display === '';
        explanationContentDiv.style.display = isHidden ? 'block' : 'none';
        explanationToggleBtn.textContent = isHidden ? 'הסתר הסבר על אלגוריתם גרובר' : 'הצג הסבר על אלגוריתם גרובר';
    });


    // --- Initial setup ---
    populateTargetSelect(); // Populate target select based on initial N
    initializeState(); // Initialize the simulation state

</script>
```