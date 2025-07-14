---
title: "פירוק לגורמים קוונטי: הסוד ששובר את ההצפנה"
english_slug: quantum-factoring-security-threat
category: "טכנולוגיה / מדעי המחשב"
tags:
  - מחשוב קוונטי
  - אלגוריתם שור
  - קריפטוגרפיה
  - מתמטיקה
  - אבטחת מידע
---
<style>
    :root {
        --primary-color: #4A90E2; /* A vibrant blue */
        --secondary-color: #50E3C2; /* A quantum-like green */
        --background-color: #F8F9FA; /* Light grey background */
        --card-background: #FFFFFF; /* White card background */
        --text-color: #333;
        --heading-color: #0F4C81; /* Darker blue for headings */
        --highlight-color: #F5A623; /* Orange for emphasis */
        --border-color: #E0E0E0; /* Light grey border */
        --shadow-color: rgba(0, 0, 0, 0.08);
        --animation-duration: 0.6s;
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.7;
        margin: 0;
        padding: 20px;
        background-color: var(--background-color);
        color: var(--text-color);
        overflow-x: hidden; /* Prevent horizontal scroll */
    }

    h1, h2, h3 {
        color: var(--heading-color);
        text-align: center;
        margin-bottom: 20px;
    }

    h1 {
         font-size: 2.2em;
         margin-top: 0;
    }

    p {
        margin-bottom: 15px;
    }

    #app {
        background-color: var(--card-background);
        padding: 30px;
        margin: 20px auto;
        max-width: 800px;
        border-radius: 12px;
        box-shadow: 0 8px 16px var(--shadow-color);
        overflow: hidden; /* Needed for animations */
    }

    #simulation-area {
        min-height: 400px; /* Give simulation area space */
        border: 1px solid var(--border-color);
        padding: 25px;
        border-radius: 8px;
        background: linear-gradient(135deg, #e0f2f7, #b2ebf2); /* Light gradient background */
        position: relative; /* For absolute positioning of elements */
        overflow: hidden; /* Ensure animations stay within bounds */
    }

    .simulation-step {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        padding: 25px;
        box-sizing: border-box;
        opacity: 0;
        visibility: hidden;
        transition: opacity var(--animation-duration) ease-in-out, visibility var(--animation-duration) ease-in-out;
    }

    .simulation-step.active {
        opacity: 1;
        visibility: visible;
    }

    .hidden {
        display: none; /* Used initially, JS switches to visibility/opacity */
    }

    button {
        display: inline-block;
        padding: 12px 25px;
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        margin-top: 20px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
    }

    button:hover {
        background-color: #3A7ED0;
    }

    button:active {
        transform: scale(0.98);
    }

    #toggle-explanation {
        display: block;
        width: fit-content;
        margin: 20px auto;
        background-color: #6c757d;
    }
     #toggle-explanation:hover {
        background-color: #5a6268;
    }


    .visual-representation {
        margin: 20px 0;
        padding: 20px;
        border: 1px dashed var(--border-color);
        border-radius: 6px;
        background-color: #f0f4f7; /* Lighter background for visuals */
        overflow-x: auto; /* Allow scrolling for wide content */
        position: relative; /* For animations inside */
    }

    .visual-representation p {
        margin: 8px 0;
    }

    .visual-representation .note {
        font-size: 0.9em;
        color: #555;
        margin-top: 15px;
        font-style: italic;
    }

    /* --- Step 1: Superposition Visualization --- */
    .superposition-viz {
        display: flex;
        justify-content: center;
        gap: 10px; /* Space between elements */
        flex-wrap: wrap;
        min-height: 80px;
    }

    .superposition-qubit {
        width: 40px;
        height: 40px;
        background-color: var(--secondary-color);
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        color: var(--heading-color);
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        opacity: 0.8;
        animation: pulse 1.5s infinite ease-in-out alternate;
    }

    @keyframes pulse {
        from { transform: scale(1); opacity: 0.8; }
        to { transform: scale(1.05); opacity: 1; }
    }


    /* --- Step 2: Function Evaluation Visualization --- */
    .function-evaluation-viz {
        display: flex;
        flex-direction: column;
        align-items: center; /* Center the content */
    }

    .input-output-pair {
        display: flex;
        justify-content: space-between;
        width: 100%; /* Takes full width of parent */
        padding: 8px 0;
        border-bottom: 1px dotted #aaa;
        opacity: 0; /* Start hidden */
        transform: translateY(20px); /* Start below */
        animation: slideUpFadeIn var(--animation-duration) ease forwards;
    }

    .input-output-pair:last-child {
        border-bottom: none;
    }

    .input-output-pair span {
        flex: 1; /* Allow spans to grow */
        text-align: center;
    }

    /* Animate pairs sequentially */
    .input-output-pair:nth-child(1) { animation-delay: 0.1s; }
    .input-output-pair:nth-child(2) { animation-delay: 0.2s; }
    .input-output-pair:nth-child(3) { animation-delay: 0.3s; }
    .input-output-pair:nth-child(4) { animation-delay: 0.4s; }
    .input-output-pair:nth-child(5) { animation-delay: 0.5s; }
    .input-output-pair:nth-child(6) { animation-delay: 0.6s; }

    @keyframes slideUpFadeIn {
        to { opacity: 1; transform: translateY(0); }
    }


    /* --- Step 3: Periodicity Visualization --- */
    .periodicity-viz {
         display: flex;
         flex-wrap: wrap;
         justify-content: center; /* Center the sequence */
         gap: 8px; /* Space between numbers */
         min-height: 80px;
    }

    .periodicity-value {
        padding: 8px 12px;
        border: 1px solid var(--primary-color);
        border-radius: 4px;
        background-color: var(--card-background);
        font-weight: bold;
        opacity: 0;
        transform: scale(0.8);
        animation: fadeInScale var(--animation-duration) ease forwards;
    }

     /* Animate values sequentially */
    .periodicity-value:nth-child(1) { animation-delay: 0.1s; }
    .periodicity-value:nth-child(2) { animation-delay: 0.2s; }
    .periodicity-value:nth-child(3) { animation-delay: 0.3s; }
    .periodicity-value:nth-child(4) { animation-delay: 0.4s; }
    .periodicity-value:nth-child(5) { animation-delay: 0.5s; }
    .periodicity-value:nth-child(6) { animation-delay: 0.6s; }
    .periodicity-value:nth-child(7) { animation-delay: 0.7s; }
    .periodicity-value:nth-child(8) { animation-delay: 0.8s; }


    .periodicity-value.highlighted {
        background-color: var(--highlight-color);
        color: white;
        animation: highlightPulse 1s infinite alternate;
    }

    @keyframes fadeInScale {
        to { opacity: 1; transform: scale(1); }
    }

     @keyframes highlightPulse {
        from { background-color: var(--highlight-color); transform: scale(1); }
        to { background-color: darken(var(--highlight-color), 10%); transform: scale(1.05); }
    }

    /* --- Step 4: Classical Processing Visualization --- */
    .classical-processing-viz .calculation-block {
        background-color: #e8f5e9; /* Light green for math */
        padding: 15px;
        border-left: 4px solid #4CAF50; /* Green border */
        border-radius: 4px;
        margin-bottom: 15px;
        white-space: pre-wrap; /* Preserve line breaks */
        font-family: 'Courier New', monospace; /* Monospaced font for calculations */
        opacity: 0;
        transform: translateX(-20px);
        animation: slideRightFadeIn var(--animation-duration) ease forwards;
    }
     .classical-processing-viz .calculation-block:nth-child(1) { animation-delay: 0.2s; }
     .classical-processing-viz .calculation-block:nth-child(2) { animation-delay: 0.5s; }


     @keyframes slideRightFadeIn {
        to { opacity: 1; transform: translateX(0); }
    }


    .classical-processing-viz .factor-result {
        font-size: 1.4em;
        font-weight: bold;
        color: var(--primary-color);
        text-align: center;
        margin-top: 20px;
        opacity: 0;
         animation: fadeInScale 0.8s ease forwards 0.8s; /* Appear after calculations */
    }

     .highlight {
        color: var(--highlight-color);
        font-weight: bold;
    }

     /* --- Step 5: Conclusion --- */
     #step-5 p {
        font-size: 1.1em;
        text-align: center;
        margin-bottom: 30px;
     }


    /* --- Explanation Section --- */
     #explanation {
        background-color: var(--card-background);
        padding: 30px;
        margin: 20px auto;
        max-width: 800px;
        border-radius: 12px;
        box-shadow: 0 8px 16px var(--shadow-color);
        opacity: 0;
        transform: translateY(30px);
        transition: opacity var(--animation-duration) ease, transform var(--animation-duration) ease;
     }

     #explanation.active {
        opacity: 1;
        transform: translateY(0);
     }

    #explanation h2, #explanation h3 {
        color: var(--heading-color);
        text-align: left; /* Align explanation headings left */
        margin-bottom: 15px;
    }

    #explanation ul {
        list-style: disc inside;
        padding-left: 20px;
        margin-bottom: 15px;
    }

    #explanation li {
        margin-bottom: 10px;
    }

    #explanation a {
        color: var(--primary-color);
        text-decoration: none;
        font-weight: bold;
    }

    #explanation a:hover {
        text-decoration: underline;
    }
</style>

<h1>פירוק לגורמים קוונטי: הסוד ששובר את ההצפנה</h1>

<p>דמיינו עולם שבו מנגנוני האבטחה הדיגיטלית החזקים ביותר, אלה שמגנים על הכסף שלכם, על המידע הרפואי שלכם ועל סודות מדינה, יכולים להיפרץ בקלות מפחידה. זה לא סרט מדע בדיוני. זהו פוטנציאל קיים, בזכות אלגוריתם קוונטי אחד ששינה את כללי המשחק.</p>

<div id="app">
    <h2>המסע הקוונטי: פירוק N=15</h2>
    <div id="simulation-area">
        <div id="step-0" class="simulation-step">
            <p>בואו נצא למסע קצר להבנת הליבה של אלגוריתם שור, באמצעות פירוק המספר <strong>N=15</strong> לגורמיו הראשוניים.</p>
            <p>בזמן שמחשב רגיל יצטרך לבדוק מספרים כמו 2, 3, 5... כדי למצוא את הגורמים, אלגוריתם שור משתמש בכוח הקוונטי לגישה מהפכנית.</p>
            <button onclick="nextStep()">התחל את המסע הקוונטי</button>
        </div>
        <div id="step-1" class="simulation-step hidden">
            <h3>שלב 1: הכנה קוונטית - עולם של אפשרויות</h3>
            <p>דמיינו שאתם יכולים לבחון <strong>את כל המספרים האפשריים בו זמנית</strong>. מחשב קוונטי יכול לייצר מצב כזה באמצעות "סופרפוזיציה" של קיוביטים. זה כמו להחזיק ערימת קלפים שבה כל הקלפים הפוכים, אבל אתם יודעים שהם מייצגים את כל המספרים שמעניינים אתכם.</p>
            <div class="visual-representation superposition-viz">
                 <div class="superposition-qubit">|0⟩</div>
                 <div class="superposition-qubit">|1⟩</div>
                 <div class="superposition-qubit">|2⟩</div>
                 <div class="superposition-qubit">|3⟩</div>
                 <div class="superposition-qubit">...</div>
                 <div class="superposition-qubit">|X⟩</div>
            </div>
            <p class="note">זוהי הדמיה מופשטת. במחשב קוונטי אמיתי, מצב זה מקודד בצורה דחוסה בהרבה.</p>
            <button onclick="nextStep()">הבא</button>
        </div>
        <div id="step-2" class="simulation-step hidden">
             <h3>שלב 2: הפעלת הפונקציה - קסם מקבילי</h3>
            <p>עכשיו, ניקח את כל האפשרויות הללו (הערכים X) ונפעיל עליהן <strong>במקביל</strong> פונקציה מתמטית: f(X) = a^X mod N. עבור N=15, נבחר a=7. הפונקציה היא f(X) = 7^X mod 15.</p>
             <p>במחשב קלאסי הייתם מחשבים כל ערך בנפרד. במחשב קוונטי? הפונקציה פועלת על <strong>כל</strong> מצבי הקלט בו זמנית, ומייצרת מצב קוונטי חדש שמקודד את כל זוגות (X, f(X)).</p>
             <div class="visual-representation function-evaluation-viz">
                <div class="input-output-pair"><span>X=0</span> <span>f(0)=7^0 mod 15 = <span class="highlight">1</span></span></div>
                <div class="input-output-pair"><span>X=1</span> <span>f(1)=7^1 mod 15 = <span class="highlight">7</span></span></div>
                <div class="input-output-pair"><span>X=2</span> <span>f(2)=7^2 mod 15 = 49 mod 15 = <span class="highlight">4</span></span></div>
                <div class="input-output-pair"><span>X=3</span> <span>f(3)=7^3 mod 15 = 343 mod 15 = <span class="highlight">13</span></span></div>
                <div class="input-output-pair"><span>X=4</span> <span>f(4)=7^4 mod 15 = 2401 mod 15 = <span class="highlight">1</span></span></div>
                <div class="input-output-pair"><span>X=5</span> <span>f(5)=7^5 mod 15 = 16807 mod 15 = <span class="highlight">7</span></span></div>
                <p class="note">המחשב הקוונטי עושה זאת עבור מגוון רחב של ערכי X בו זמנית, בזמן שבסדרה זו אנו רואים רק דוגמאות.</p>
             </div>
            <button onclick="nextStep()">הבא</button>
        </div>
        <div id="step-3" class="simulation-step hidden">
            <h3>שלב 3: מדידה קוונטית - גילוי הקצב הנסתר</h3>
            <p>כאן מתרחש הקסם הקוונטי העיקרי. באמצעות תהליך מתוחכם שנקרא "טרנספורם פורייה קוונטי" (QFT) וקצת התאבכות קוונטית, אנו מבצעים מדידה. המדידה לא חושפת את כל זוגות (X, f(X)), אלא חושפת מידע על <strong>המחזוריות</strong> של הסדרה f(X).</p>
            <p>המחזוריות (נסמנה כ-'r') היא המרחק בין חזרות בולטות בפונקציה. נסתכל על הסדרה שראינו:</p>
            <div class="visual-representation periodicity-viz">
                <div class="periodicity-value">1</div>
                <div class="periodicity-value">7</div>
                <div class="periodicity-value">4</div>
                <div class="periodicity-value">13</div>
                <div class="periodicity-value">1</div>
                <div class="periodicity-value">7</div>
                <div class="periodicity-value">4</div>
                <div class="periodicity-value">13</div>
                <div class="periodicity-value">...</div>
            </div>
            <p>ניתן לראות שהסדרה <strong>חוזרת על עצמה כל 4 איברים</strong> (1, 7, 4, 13). המדידה הקוונטית מאפשרת לחשוף את הערך r=4 <strong>ביעילות רבה</strong> עבור מספרים גדולים בהרבה!</p>
            <p class="note">התהליך הקוונטי מבוסס על התאבכות שגורמת להסתברויות הקשורות למחזוריות להתחזק.</p>
            <button onclick="nextStep()">הבא</button>
        </div>
         <div id="step-4" class="simulation-step hidden">
            <h3>שלב 4: עיבוד קלאסי - גילוי הגורמים</h3>
            <p>מצאנו את המחזוריות הקוונטית r=4. עכשיו, חוזרים למחשב הקלאסי ולמתמטיקה ידועה כדי לחלץ את הגורמים של N=15. משתמשים בנוסחה מבוססת על אלגוריתם אוקלידס למחלק משותף מרבי (GCD).</p>
            <p>נחשב את GCD(a<sup>r/2</sup> - 1, N) ואת GCD(a<sup>r/2</sup> + 1, N). כאן a=7, r=4, N=15:</p>
            <div class="visual-representation classical-processing-viz">
                <div class="calculation-block">
                    <strong>חישוב הגורם הראשון:</strong><br>
                    GCD(7<sup>4/2</sup> - 1, 15) = GCD(7<sup>2</sup> - 1, 15)<br>
                    = GCD(49 - 1, 15) = GCD(48, 15)<br>
                    אלגוריתם אוקלידס:<br>
                    48 = 3 * 15 + <span class="highlight">3</span><br>
                    15 = 5 * 3 + 0<br>
                    GCD(48, 15) = <span class="highlight">3</span>
                </div>
                <div class="calculation-block">
                    <strong>חישוב הגורם השני:</strong><br>
                    GCD(7<sup>4/2</sup> + 1, 15) = GCD(7<sup>2</sup> + 1, 15)<br>
                    = GCD(49 + 1, 15) = GCD(50, 15)<br>
                    אלגוריתם אוקלידס:<br>
                    50 = 3 * 15 + <span class="highlight">5</span><br>
                    15 = 3 * 5 + 0<br>
                    GCD(50, 15) = <span class="highlight">5</span>
                </div>
                <div class="factor-result">
                    הגורמים של 15 הם: <span class="highlight">3</span> ו- <span class="highlight">5</span>!
                </div>
            </div>
            <p class="note">שימו לב: אם r אי-זוגי, או אם (a<sup>r/2</sup> ± 1) הוא כפולה של N, האלגוריתם עשוי להיכשל ויש לבחור 'a' אחר. אך ההסתברות להצלחה גבוהה.</p>
            <button onclick="nextStep()">סיום המסע</button>
        </div>
        <div id="step-5" class="simulation-step hidden">
            <h3>המשימה הושלמה: פירוק לגורמים!</h3>
            <p>ראינו כיצד אלגוריתם שור משתמש ביכולות הקוונטיות הייחודיות (סופרפוזיציה, התאבכות/QFT) כדי למצוא את המחזוריות ביעילות, ולאחר מכן משתמש במתמטיקה קלאסית כדי לחלץ את הגורמים הראשוניים. זהו כוח חישובי אדיר שמשנה את כללי המשחק!</p>
             <button onclick="resetSimulation()">התחל מסע חדש (מחדש)</button>
        </div>
    </div>
</div>

<button id="toggle-explanation" onclick="toggleExplanation()">הצג הסבר מעמיק</button>

<div id="explanation" class="hidden">
    <h2>הסבר מעמיק: מהפכת שור והאיום על האבטחה</h2>

    <h3>האתגר הקלאסי: מדוע פירוק לגורמים קשה?</h3>
    <p>מציאת הגורמים הראשוניים של מספר גדול היא משימה חישובית קשה <strong>מאוד</strong> למחשבים קלאסיים. האלגוריתמים הקלאסיים היעילים ביותר (כמו אלגוריתם נפת שדה המספרים הכללי - GNFS) לוקחים זמן שגדל באופן <strong>אקספוננציאלי</strong> עם מספר הספרות של המספר. מספר בן מאות ספרות עלול לדרוש יותר זמן מאשר גיל היקום כדי לפרק אותו לגורמים במחשב העל החזק ביותר הקיים כיום.</p>
    <p>קושי זה הוא אבן הפינה של אבטחת המידע המודרנית, ובפרט של הצפנות א-סימטריות (עם מפתח ציבורי) כמו <a href="https://he.wikipedia.org/wiki/RSA" target="_blank">RSA</a>. RSA מאבטח תקשורת יומיומית באינטרנט, עסקאות בנקאיות דיגיטליות, חתימות דיגיטליות ועוד. שבירת RSA דורשת פירוק מכפלת שני מספרים ראשוניים גדולים מאוד לגורמיהם. אם משימה זו הופכת קלה, כל מה שמוצפן בשיטה זו הופך חשוף.</p>

    <h3>אלגוריתם שור: קפיצת המדרגה הקוונטית</h3>
    <p>בשנת 1994, פיטר שור הראה שמחשב קוונטי יכול לבצע פירוק לגורמים בזמן שגדל רק באופן <strong>פולינומי</strong> עם מספר הספרות של המספר - יעילות גבוהה לאין ערוך בהשוואה לאלגוריתמים הקלאסיים עבור מספרים גדולים. אלגוריתם שור לא פותר את בעיית פירוק הגורמים ישירות. במקום זאת, הוא ממיר אותה לבעיית מציאת מחזוריות של פונקציה, אותה הוא פותר ביעילות קוונטית.</p>
    <p>כיצד הוא עושה זאת? הוא ממנף את עקרונות יסוד של מכניקת הקוונטים:</p>
    <ul>
        <li><strong>סופרפוזיציה:</strong> היכולת של קיוביט לייצג 0 ו-1 בו זמנית, ושל מערכת קיוביטים לייצג צירוף של כל המצבים האפשריים (כלומר, כל הקלטים הפוטנציאליים לפונקציה f(X)) - מאפשרת התחלת חישוב על "כל" הקלטים במקביל.</li>
        <li><strong>התאבכות קוונטית:</strong> הפעלת שערים קוונטיים מתאימים (הליבה של אלגוריתם שור הקוונטי היא טרנספורם פורייה קוונטי - QFT) גורמת למצבים קוונטיים שמקודדים מידע הקשור למחזוריות "להתאבך בונה" (להתחזק), בעוד שמצבים לא רלוונטיים "מתאבכים הורס" (נחלשים או מתבטלים). בסיום התהליך הקוונטי, ההסתברות למדוד תוצאה שקשורה למחזוריות גבוהה באופן משמעותי.</li>
        <li><strong>מדידה:</strong> בסיום התהליך הקוונטי, מדידה "מקריסה" את הסופרפוזיציה לתוצאה קלאסית יחידה. למרות שהתוצאה אקראית, אלגוריתם שור מבטיח שהיא תהיה קשורה בסיכוי גבוה למחזוריות המבוקשת. מספר מועט של מדידות קוונטיות ועיבוד קלאסי מאפשרים לחלץ את ערך המחזוריות r בוודאות גבוהה.</li>
    </ul>

    <h3>השלכות מרחיקות לכת: איום קיומי על קריפטוגרפיה</h3>
    <p>אלגוריתם שור אינו רק הישג תיאורטי יפהפה; הוא מהווה איום <strong>אסטרטגי וקיומי</strong> על התשתית הדיגיטלית העולמית. רוב מוחלט של תקשורת מאובטחת, מסחר אלקטרוני, וחתימות דיגיטליות בעולם נשענים על הצפנת RSA ודומותיה (כמו Diffie-Hellman), שייעקפו לחלוטין על ידי מחשב קוונטי גדול מספיק.</p>
    <p>האיום מתממש ברגע שמחשב קוונטי מסוגל להריץ את אלגוריתם שור עבור מספרים בגודל שבו משתמשות שיטות ההצפנה הללו (כיום מדובר על 2048 ביטים ומעלה). היכולת לפרק מפתחות הצפנה אלו תוך שעות או ימים, במקום מיליוני שנים, חושפת מידע רגיש מהעבר, מהווה סיכון למידע עתידי, ומערערת את האמון באבטחת המידע.</p>

    <h3>הפתרון: עידן הקריפטוגרפיה הפוסט-קוונטית (PQC)</h3>
    <p>ההכרה באיום הקוונטי הולידה תחום חדש: "קריפטוגרפיה פוסט-קוונטית" (PQC). מדובר בפיתוח אלגוריתמי הצפנה חדשים שיהיו עמידים בפני התקפות של מחשבים קוונטיים גדולים, תוך שמירה על ביטחונם גם מפני מחשבים קלאסיים. אלגוריתמי PQC מבוססים על בעיות מתמטיות קשות שונות לחלוטין מבעיית פירוק הגורמים או הלוגריתם הדיסקרטי, לדוגמה: בעיות על סריגים (Lattices), קודים (Codes), או פונקציות גיבוב (Hash-based).</p>
    <p>גופים בינלאומיים ובראשם NIST (המכון הלאומי לתקנים וטכנולוגיה בארה"ב) מובילים תהליכים קדחתניים לסטנדרטיזציה ובחירת אלגוריתמי PQC הטובים ביותר. המעבר ל-PQC הוא אתגר גלובלי מורכב, הדורש שדרוג של מערכות תוכנה וחומרה בכל העולם, וצפוי להימשך שנים.</p>

    <h3>היכן אנו עומדים?</h3>
    <p>נכון לכתיבת שורות אלו (אמצע 2024), מחשבים קוונטיים עדיין נמצאים בשלבי פיתוח מוקדמים ("עידן ה-NISQ" - Noisy Intermediate-Scale Quantum). הם קטנים, רגישים לשגיאות ואינם בעלי יכולות תיקון שגיאות מספקות כדי להריץ את אלגוריתם שור על מספרים גדולים המשמשים בהצפנה מודרנית. דרושים מחשבים קוונטיים עם אלפי ואף מיליוני קיוביטים יציבים ויכולות תיקון שגיאות מתקדמות לביצוע משימה זו.</p>
    <p>אף על פי כן, ההתקדמות הטכנולוגית מהירה. קהילת הביטחון והתעשייה כבר החלו בהיערכות למעבר. המידע הרגיש ביותר, שעשוי להידרש להיות סודי למשך עשורים, מצריך כבר היום שיקול של "הצפנה עכשיו, פענוח מאוחר יותר" (Store Now, Decrypt Later) על ידי איסוף נתונים מוצפנים כיום בתקווה לפענחם בעתיד באמצעות מחשב קוונטי. לכן, המעבר ל-PQC הוא הכרחי ודחוף, גם אם ה"שבר הגדול" הקוונטי עדיין לא כאן.</p>
</div>

<script>
    let currentStep = 0;
    const totalSteps = 6; // Steps 0 to 5
    const steps = []; // Array to hold step elements

    function initializeSteps() {
        // Get all step elements and hide them initially via class
        for (let i = 0; i < totalSteps; i++) {
            const stepElement = document.getElementById(`step-${i}`);
            if (stepElement) {
                steps.push(stepElement);
                // Use the hidden class for initial state managed by CSS/JS
                stepElement.classList.add('hidden-initial'); // Use a dedicated class if needed, or just manage via opacity/visibility
                stepElement.classList.remove('active'); // Ensure no step is active initially
            }
        }
    }

    function showStep(stepIndex) {
        if (stepIndex < 0 || stepIndex >= totalSteps) return;

        // Deactivate current step
        if (currentStep >= 0 && currentStep < steps.length) {
             if (steps[currentStep]) {
                 steps[currentStep].classList.remove('active');
             }
        }

        // Activate new step after a short delay to allow for transition
        currentStep = stepIndex;
        if (steps[currentStep]) {
            steps[currentStep].classList.add('active');
            // Ensure hidden-initial is removed if used
             steps[currentStep].classList.remove('hidden-initial');
        }

        // Specific animations per step (optional, can be handled purely by CSS transitions based on .active)
        // For more complex animations, you might need to add/remove specific animation classes here.
        // Example: if (currentStep === 3) animatePeriodicity();
    }

    function nextStep() {
        if (currentStep < totalSteps - 1) {
            showStep(currentStep + 1);
        }
    }

    function resetSimulation() {
        showStep(0);
    }

    function toggleExplanation() {
        const explanationDiv = document.getElementById('explanation');
        const button = document.getElementById('toggle-explanation');

        // Toggle the 'active' class for CSS transitions
        explanationDiv.classList.toggle('active');

        if (explanationDiv.classList.contains('active')) {
             button.textContent = 'הסתר הסבר מעמיק';
             // Ensure visibility is block while transitioning
             explanationDiv.style.display = 'block';
        } else {
             button.textContent = 'הצג הסבר מעמיק';
             // Hide completely after transition if needed, or rely solely on opacity/visibility
             // For this setup, opacity/visibility should be enough.
             // If display:none is crucial, listen for transitionend event.
             // explanationDiv.addEventListener('transitionend', function handler() {
             //     if (!explanationDiv.classList.contains('active')) {
             //          explanationDiv.style.display = 'none';
             //     }
             //     explanationDiv.removeEventListener('transitionend', handler);
             // });
        }
    }

    // Initialize the app when the DOM is ready
    document.addEventListener('DOMContentLoaded', () => {
        initializeSteps(); // Collect step elements
        showStep(0); // Show the first step

        // Set initial text for the toggle button
        const toggleButton = document.getElementById('toggle-explanation');
        toggleButton.textContent = 'הצג הסבר מעמיק';

        // Ensure explanation is hidden on load using styles defined in CSS
        const explanationDiv = document.getElementById('explanation');
        explanationDiv.classList.remove('active'); // Ensure it doesn't start active
        // You might need to explicitly set initial state here if CSS doesn't fully handle it before first toggle
        // explanationDiv.style.opacity = 0;
        // explanationDiv.style.transform = 'translateY(30px)';
        // explanationDiv.style.display = 'none'; // Or rely on visibility: hidden from CSS
    });

</script>