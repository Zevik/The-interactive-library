---
title: "דילמת צייד האיילים: סימולטור אינטראקטיבי"
english_slug: stag-hunt-dilemma-interactive-simulator
category: "כלכלה התנהגותית"
tags:
  - תורת המשחקים
  - דילמה חברתית
  - קואופרציה
  - אסטרטגיה
  - אי ודאות
---
# דילמת צייד האיילים: סימולטור אינטראקטיבי

דמיינו: אתם עומדים מול הזדמנות לצוד אייל ענק ומשתלם במיוחד... אבל זה דורש שיתוף פעולה מלא עם צייד אחר. אם שניכם תתמקדו באייל, הרווח יהיה עצום לשניכם!
לחלופין, אתם יכולים להחליט לצוד ארנבת קטנה, שפירה אך בטוחה, לגמרי לבדכם. הארנבת מספקת פחות מזון, אבל אתם יודעים בוודאות שתשיגו אותה.
הדילמה עמוקה: מה תעשו אם אינכם יודעים בוודאות מה מתכנן הצייד השני? האם תסמכו עליו ותסכנו את הכל למען פרס גדול יותר, או שתלכו על הבטוח ותסתפקו במועט?

התנסו בעצמכם בסימולטור ובדקו את האסטרטגיה שלכם!

<div id="stagHuntApp" class="game-container">
    <h2 class="game-title">דילמת צייד האיילים</h2>

    <div class="payoff-matrix-section">
        <h3 class="section-title">מטריצת התשלומים</h3>
        <div class="matrix-wrapper">
            <table>
                <thead>
                    <tr>
                        <th rowspan="2"></th>
                        <th colspan="2">בחירת היריב</th>
                    </tr>
                    <tr>
                        <th><span class="icon">🦌</span> אייל</th>
                        <th><span class="icon">🐇</span> ארנבת</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td rowspan="2"><b>הבחירה שלך</b><br><span class="icon">🦌</span> אייל</td>
                        <td><b>הרווח שלך:</b> <span class="payoff-value">4</span></td>
                        <td><b>הרווח שלך:</b> <span class="payoff-value zero">0</span></td>
                    </tr>
                    <tr>
                        <td><b>רווח היריב:</b> <span class="payoff-value">4</span></td>
                        <td><b>רווח היריב:</b> <span class="payoff-value">1</span></td>
                    </tr>
                    <tr>
                        <td rowspan="2"><b>הבחירה שלך</b><br><span class="icon">🐇</span> ארנבת</td>
                        <td><b>הרווח שלך:</b> <span class="payoff-value">1</span></td>
                        <td><b>הרווח שלך:</b> <span class="payoff-value">1</span></td>
                    </tr>
                    <tr>
                        <td><b>רווח היריב:</b> <span class="payoff-value zero">0</span></td>
                        <td><b>רווח היריב:</b> <span class="payoff-value">1</span></td>
                    </tr>
                </tbody>
            </table>
        </div>
        <p class="matrix-note">הצלחה בציד אייל (<span class="icon">🦌</span>) דורשת שיתוף פעולה מלא משני הצדדים. ציד ארנבת (<span class="icon">🐇</span>) תמיד מצליח ומניב רווח מינימלי.</p>
    </div>

    <div class="choices-section">
        <h3 class="section-title">מה תבחר לצוד בסיבוב הנוכחי?</h3>
        <div class="choice-buttons">
            <button id="chooseStag" class="choice-btn stag-btn" data-choice="stag">
                <span class="icon">🦌</span> לצוד אייל (סיכון גבוה, פוטנציאל רווח גבוה)
            </button>
            <button id="chooseHare" class="choice-btn hare-btn" data-choice="hare">
                <span class="icon">🐇</span> לצוד ארנבת (סיכון נמוך, רווח בטוח)
            </button>
        </div>
         <div class="player-status" id="playerStatus" style="display: none;">
            <p id="yourChoiceDisplay"></p>
            <p id="opponentChoiceDisplay"></p>
        </div>
    </div>

    <div id="roundResult" class="result-area" style="display: none;">
        <h3 class="section-title">תוצאות הסיבוב</h3>
        <div class="outcome-details">
             <p id="outcomeDisplay" class="outcome-text"></p>
             <div class="payoffs-display">
                 <p><b>הרווח שלך:</b> <span id="yourPayoffDisplay"></span></p>
                 <p><b>רווח היריב:</b> <span id="opponentPayoffDisplay"></span></p>
             </div>
        </div>
        <button id="nextRoundBtn" class="action-button" style="display: none;">סיבוב הבא!</button>
    </div>

    <div class="score-area">
        <h3 class="section-title">סיכום כולל</h3>
        <div class="score-details">
            <p>סיבוב: <span id="roundNumber">0</span></p>
            <p>סה"כ רווח שלך: <span id="yourTotalScore">0</span> <span class="icon">💰</span></p>
            <p>סה"כ רווח יריב: <span id="opponentTotalScore">0</span> <span class="icon">💰</span></p>
        </div>
    </div>

</div>

<button id="toggleExplanation" class="toggle-button">מה מסתתר מאחורי דילמת צייד האיילים? (הצג/הסתר הסבר)</button>

<div id="explanation" class="explanation-area" style="display: none;">
    <h2>הסבר מעמיק: דילמת צייד האיילים</h2>

    <h3>מהי דילמת צייד האיילים ולמה היא מרתקת?</h3>
    <p>דילמת צייד האיילים היא אבן יסוד בתורת המשחקים, שמדגימה בצורה אלגנטית את הקונפליקט הנצחי בין השאיפה לרווח אישי מיידי לבין היתרונות האפשריים של שיתוף פעולה הדדי. היא מבוססת על סיפורו של הפילוסוף ז'אן-ז'אק רוסו: שני ציידים יכולים לשתף פעולה ולצוד יחד אייל - משימה שדורשת מחויבות הדדית ומניבה תגמול גדול לשניהם. לחלופין, כל אחד יכול לבחור לצוד לבדו ארנבת - משימה קלה יותר ובטוחה, שמניבה תגמול קטן יותר אך מובטח. הדילמה מתעוררת כאשר הציידים צריכים להחליט בו זמנית, ללא ידיעה ודאית לגבי בחירת הצד השני. האם הסיכון הכרוך בבחירה האופטימלית מבחינה חברתית (ציד אייל) מוצדק, או שעדיף ללכת על הבחירה הבטוחה והפחות משתלמת (ציד ארנבת)?</p>

    <h3>מטריצת התשלומים (Payoff Matrix): מפה של תוצאות אפשריות</h3>
    <p>מטריצת התשלומים היא הכלי שלנו לנתח את המשחק. היא מציגה את התגמול (או 'התועלת') שמקבל כל שחקן עבור כל שילוב אפשרי של בחירות. בסימולטור שראיתם, המספרים מייצגים 'נקודות' או 'רווחים':</p>
    <ul>
        <li><b>אתה בוחר אייל (<span class="icon">🦌</span>), היריב בוחר אייל (<span class="icon">🦌</span>):</b> קואורדינציה מושלמת! שניכם מצליחים לצוד את האייל הענק. רווח גבוה לשניכם (4 לכל אחד). זהו התרחיש האופטימלי מבחינה קולקטיבית.</li>
        <li><b>אתה בוחר אייל (<span class="icon">🦌</span>), היריב בוחר ארנבת (<span class="icon">🐇</span>):</b> אתה מתמקד באייל, אבל היריב "בגד" ופנה לארנבת הבטוחה. אתה נשאר לבד מול האייל ופשוט מפסיד את זמנך ומרצך (רווח 0). היריב הרוויח את הארנבת שלו (רווח 1). זהו תרחיש מסוכן עבור מי שבחר באייל.</li>
        <li><b>אתה בוחר ארנבת (<span class="icon">🐇</span>), היריב בוחר אייל (<span class="icon">🦌</span>):</b> הסיטואציה ההפוכה. אתה בחרת בבטוח, והיריב ניסה לשתף פעולה. אתה קיבלת את הארנבת שלך (רווח 1), בעוד היריב, שנשאר לבד מול האייל, לא הצליח לצוד אותו (רווח 0).</li>
        <li><b>אתה בוחר ארנבת (<span class="icon">🐇</span>), היריב בוחר ארנבת (<span class="icon">🐇</span>):</b> שניכם הלכתם על הבטוח. שניכם השגתם את הארנבת שלכם. רווח נמוך אך מובטח לכל אחד (1 לכל אחד). זוהי ברירת המחדל כאשר אין אמון או קואורדינציה.</li>
    </ul>
    <p>שימו לב: ציד אייל משתלם **רק** אם גם הצד השני בוחר באייל. ציד ארנבת פחות רווחי, אך הוא תמיד אפשרי ללא תלות בשני. זהו לב הדילמה.</p>

    <h3>לא "דילמת האסיר": ההבדל הקריטי</h3>
    <p>למרות הדמיון השטחי, דילמת צייד האיילים שונה מהותית מדילמת האסיר המפורסמת. בדילמת האסיר, הבחירה ה"בוגדנית" (להודות/לבגוד) היא אסטרטגיה דומיננטית – היא תמיד הבחירה הטובה ביותר לשחקן הבוחר בה, ללא תלות במה שיבחר הצד השני. התוצאה היא ששני האסירים "בוגדים" ומגיעים לתוצאה גרועה יותר מזו שהיו מגיעים אליה בשיתוף פעולה. בדילמת צייד האיילים, אין אסטרטגיה דומיננטית כזו. הבחירה המשתלמת עבורך **תלויה** במה שלדעתך יבחר הצד השני. אם אתה מצפה שהיריב יבחר אייל, כדאי לך לבחור אייל. אם אתה מצפה שהיריב יבחר ארנבת, כדאי לך לבחור ארנבת. זהו משחק של תיאום ציפיות ואמון.</p>

    <h3>שיוויי משקל נאש (Nash Equilibrium): איפה המשחק "יכול להיתקע"?</h3>
    <p>שיווי משקל נאש הוא מצב יציב במשחק, בו אף שחקן אינו יכול לשפר את מצבו על ידי שינוי חד-צדדי של בחירתו, בהנחה שהשחקנים האחרים לא משנים את שלהם. בדילמת צייד האיילים ישנם שני שיוויי משקל נאש:</p>
    <ol>
        <li><b>שניהם צדים אייל (<span class="icon">🦌</span>, <span class="icon">🦌</span>):</b> אם אתם נמצאים במצב ששניכם בחרתם אייל, הרווח של כל אחד הוא 4. האם משתלם לך לעבור לצוד ארנבת? לא, כי אז הרווח שלך יירד ל-1 (בעוד היריב יישאר על 4). לכן, אין לך תמריץ לשנות. גם ליריב אין תמריץ לשנות. זהו שיווי משקל "טוב" שדורש אמון ותיאום כדי להגיע אליו.</li>
        <li><b>שניהם צדים ארנבת (<span class="icon">🐇</span>, <span class="icon">🐇</span>):</b> אם אתם נמצאים במצב ששניכם בחרתם ארנבת, הרווח של כל אחד הוא 1. האם משתלם לך לעבור לצוד אייל? לא, כי אז הרווח שלך יירד ל-0 (בעוד היריב יישאר על 1). לכן, אין לך תמריץ לשנות. גם ליריב אין תמריץ לשנות. זהו שיווי משקל "פחות טוב", אך הוא בטוח יותר להשגה אם יש חוסר אמון.</li>
    </ol>
    <p>בעיית ה"קואורדינציה" היא איך להגיע לשיווי המשקל הטוב יותר (אייל, אייל) כאשר שיווי המשקל הבטוח יותר (ארנבת, ארנבת) תמיד זמין ומפתה, במיוחד כשיש אי-ודאות לגבי כוונות הצד השני. הסיכון הגדול ביותר הוא שתבחר אייל, בעוד היריב יבחר ארנבת, ותישאר בלי כלום.</p>

    <h3>מעבר למשחק: השלכות בעולם האמיתי</h3>
    <p>דילמת צייד האיילים היא מודל חזק למצבים רבים בחיינו המצריכים שיתוף פעולה ואמון כדי להגיע לתוצאה הטובה ביותר עבור קבוצה או חברה:</p>
    <ul>
        <li><b>שינויי אקלים ומאגרי משאבים משותפים:</b> התמודדות גלובלית דורשת שיתוף פעולה נרחב (ציד אייל), אך כל מדינה עשויה לחשוש שמדינות אחרות ינצלו את הסיטואציה למען רווח אישי (ציד ארנבת), מה שמוביל לכשל קולקטיבי.</li>
        <li><b>פיתוח טכנולוגיה ותשתיות:</b> פרויקטים גדולים דורשים השקעה מתואמת מאספקטים שונים. חוסר אמון או חוסר תיאום יכולים להוביל לכך שכל צד יבחר בפתרון "בטוח" ופחות יעיל עבורו לבד, במקום לתרום לפרויקט המשותף הגדול יותר.</li>
        <li><b>משא ומתן ודיפלומטיה:</b> הסכמים בינלאומיים או עסקיים גדולים דורשים לקיחת סיכונים מחושבת ואמון הדדי. הפחד מ"בגידה" של הצד השני עלול להוביל להישארות ב"שיווי משקל ארנבת" - הסכם מינימלי ובטוח, במקום שיווי משקל "אייל" - הסכם שאופטימלי לשני הצדדים.</li>
    </ul>
    <p>המשחק מלמד אותנו כמה קריטיים הם אמון, תקשורת, ובניית מוסדות ותמריצים מתאימים כדי להתגבר על הפחד מסיכון ולהגיע לתוצאות הטובות ביותר עבור כולם.</p>
</div>

<style>
    :root {
        --primary-color: #0056b3; /* A rich blue */
        --secondary-color: #f0ad4e; /* Orange */
        --success-color: #5cb85c; /* Green */
        --danger-color: #d9534f; /* Red */
        --info-color: #5bc0de; /* Light Blue */
        --bg-color: #eef2f7; /* Light background */
        --card-bg: #ffffff; /* White */
        --border-color: #ced4da; /* Light grey */
        --text-color: #343a40; /* Dark grey */
        --shadow-light: 0 2px 4px rgba(0, 0, 0, 0.1);
        --shadow-medium: 0 5px 15px rgba(0, 0, 0, 0.15);
    }

    body {
        direction: rtl;
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: var(--text-color);
        background-color: var(--bg-color);
        padding: 20px;
    }

    h1 {
        text-align: center;
        color: var(--primary-color);
        margin-bottom: 30px;
    }

    p {
        margin-bottom: 15px;
    }

    /* --- Game Container --- */
    .game-container {
        background-color: var(--card-bg);
        margin: 20px auto;
        padding: 30px;
        border-radius: 12px;
        max-width: 700px;
        box-shadow: var(--shadow-medium);
        direction: rtl;
        overflow: hidden; /* Clear floats/margins */
    }

    .game-title, .section-title {
        text-align: center;
        color: var(--primary-color);
        margin-bottom: 25px;
        position: relative; /* For underline effect */
    }

     .section-title::after {
        content: '';
        display: block;
        width: 50px;
        height: 3px;
        background: var(--secondary-color);
        margin: 10px auto 0;
        border-radius: 2px;
    }

    /* --- Payoff Matrix --- */
    .payoff-matrix-section {
        margin-bottom: 40px;
    }

    .matrix-wrapper {
        overflow-x: auto; /* Handle small screens */
    }

    .payoff-matrix-section table {
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
        text-align: center;
        background-color: #e9ecef; /* Light grey-blue */
        border-radius: 8px;
        overflow: hidden; /* For border-radius */
    }

    .payoff-matrix-section th, .payoff-matrix-section td {
        border: 1px solid var(--border-color);
        padding: 12px;
        min-width: 80px; /* Prevent squishing */
    }

    .payoff-matrix-section th {
        background-color: #dee2e6; /* Slightly darker grey */
        font-weight: bold;
        color: var(--text-color);
    }

     .payoff-matrix-section td {
         background-color: var(--card-bg);
     }

    .payoff-matrix-section td b {
        display: block;
        margin-bottom: 5px;
    }

    .payoff-value {
        font-weight: bold;
        color: var(--success-color); /* Default payoff color */
    }
    .payoff-value.zero {
        color: var(--danger-color); /* Highlight zero payoff as negative */
    }

    .matrix-note {
        font-size: 0.95em;
        color: #6c757d; /* Muted text */
        text-align: center;
        margin-top: 15px;
        padding: 0 15px;
    }

    .icon {
        margin-left: 5px; /* Space after icon */
    }
    .icon:empty { /* Hide if empty */
        display: none;
    }


    /* --- Choices Section --- */
    .choices-section {
        margin-bottom: 30px;
        text-align: center;
    }

    .choice-buttons {
        display: flex;
        justify-content: center;
        gap: 20px; /* Space between buttons */
        flex-wrap: wrap; /* Wrap on small screens */
    }

    .choice-btn {
        padding: 15px 30px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 30px; /* Pill shape */
        transition: transform 0.2s ease, background-color 0.2s ease, box-shadow 0.2s ease;
        font-weight: bold;
        text-align: center;
        flex-grow: 1; /* Allow buttons to grow */
        max-width: 300px; /* Max width for buttons */
    }

    .choice-btn .icon {
        margin-left: 8px;
        font-size: 1.2em;
        vertical-align: middle;
    }

    .stag-btn {
        background-color: var(--success-color);
        color: white;
        box-shadow: var(--shadow-light);
    }

    .hare-btn {
        background-color: var(--secondary-color);
        color: white;
        box-shadow: var(--shadow-light);
    }

    .choice-btn:hover:not(:disabled) {
        transform: translateY(-3px);
        box-shadow: var(--shadow-medium);
        opacity: 1; /* Ensure full opacity on hover */
    }

     .choice-btn:disabled {
        opacity: 0.6;
        cursor: not-allowed;
        transform: none; /* Remove hover effect when disabled */
        box-shadow: none;
     }

     /* Highlight selected choice */
     .choice-btn.selected {
         outline: 3px solid var(--primary-color);
         outline-offset: 5px;
         box-shadow: var(--shadow-medium);
     }

    .player-status {
        margin-top: 20px;
        padding: 15px;
        background-color: #f8f9fa; /* Lightest grey */
        border: 1px dashed var(--border-color);
        border-radius: 8px;
        text-align: right;
         display: flex;
         justify-content: space-around;
         flex-wrap: wrap;
         gap: 10px;
    }

    .player-status p {
        margin: 0;
        font-size: 1.05em;
        font-weight: bold;
        flex-basis: 48%; /* Allow two paragraphs per row */
        text-align: center;
    }


    /* --- Result Area --- */
    .result-area {
        margin-top: 30px;
        padding: 25px;
        border: 1px solid var(--info-color);
        background-color: #e9f7fd; /* Very light blue */
        border-radius: 8px;
        text-align: center;
        opacity: 0; /* Start hidden for animation */
        transform: translateY(20px);
        transition: opacity 0.5s ease-out, transform 0.5s ease-out;
    }

    .result-area.visible {
        opacity: 1;
        transform: translateY(0);
    }

    .outcome-details {
        margin-bottom: 20px;
    }

    .outcome-text {
        font-size: 1.3em;
        font-weight: bold;
        color: var(--primary-color);
        margin-bottom: 15px;
    }

    .payoffs-display {
        display: flex;
        justify-content: center;
        gap: 30px;
        font-size: 1.1em;
    }

    .payoffs-display p {
        margin: 5px 0;
    }

     .payoffs-display span {
        font-weight: bold;
        color: var(--success-color);
     }

    .action-button {
        display: block;
        margin: 20px auto 0;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 5px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
    }

    .action-button:hover:not(:disabled) {
         background-color: #003f80; /* Darker blue */
         transform: translateY(-1px);
    }

    /* --- Score Area --- */
    .score-area {
        margin-top: 30px;
        padding: 20px;
        border: 1px solid var(--border-color);
        background-color: #f8f9fa; /* Lightest grey */
        border-radius: 8px;
        text-align: center;
    }

    .score-details {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        gap: 10px;
    }

     .score-area p {
        margin: 5px 0;
        font-size: 1.1em;
        font-weight: bold;
         flex-basis: 45%; /* Allow two paragraphs per row */
     }

     .score-area span {
        font-weight: normal;
        color: var(--primary-color);
     }
      .score-area .icon {
        font-size: 1em;
      }


    /* --- Explanation Area --- */
    .toggle-button {
        display: block;
        margin: 30px auto 20px;
        padding: 12px 25px;
        font-size: 1em;
        cursor: pointer;
        background-color: #6c757d; /* Muted grey */
        color: white;
        border: none;
        border-radius: 5px;
        transition: background-color 0.3s ease, transform 0.1s ease;
         font-weight: bold;
    }

    .toggle-button:hover {
        background-color: #5a6268; /* Darker muted grey */
         transform: translateY(-1px);
    }

    .explanation-area {
        direction: rtl;
        font-family: 'Arial', sans-serif;
        margin: 20px auto;
        padding: 30px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        max-width: 700px;
        background-color: var(--card-bg);
        box-shadow: var(--shadow-light);
    }

     .explanation-area h2, .explanation-area h3 {
        color: var(--primary-color);
        text-align: right;
        margin-bottom: 15px;
     }
      .explanation-area h3 {
          margin-top: 25px;
          margin-bottom: 10px;
           color: #5a6268;
      }


     .explanation-area p, .explanation-area ul, .explanation-area ol {
         line-height: 1.7;
         margin-bottom: 18px;
     }

     .explanation-area ul, .explanation-area ol {
         padding-right: 25px;
     }

     .explanation-area li {
         margin-bottom: 10px;
     }

     .explanation-area .icon {
         vertical-align: middle;
     }

     /* Animation for choice selection */
    .choice-btn.selecting {
        animation: pulse 0.5s ease-in-out infinite alternate;
    }

    @keyframes pulse {
        from { transform: scale(1); opacity: 1; }
        to { transform: scale(1.03); opacity: 0.9; }
    }

    /* Responsive adjustments */
    @media (max-width: 600px) {
        .game-container, .explanation-area {
            padding: 20px;
        }

        .choice-buttons {
            flex-direction: column;
            gap: 10px;
        }

        .choice-btn {
            width: 100%; /* Full width on small screens */
            max-width: none;
        }

        .payoffs-display {
            flex-direction: column;
            gap: 10px;
        }

        .player-status p, .score-area p {
             flex-basis: 100%;
             text-align: center;
        }
    }


</style>

<script>
    const payoffMatrix = {
        stag: {
            stag: { user: 4, opponent: 4, outcomeText: 'ניצחון כפול! <span class="icon">🦌</span> <span class="icon">🦌</span> שיתוף פעולה מלא השתלם בגדול!' },
            hare: { user: 0, opponent: 1, outcomeText: 'מלכודת! <span class="icon">🦌</span> <span class="icon">🐇</span> אתה ניסית לצוד אייל, אבל היריב בחר בבטוח. האייל ברח ואתה נשארת בלי כלום...' }
        },
        hare: {
            stag: { user: 1, opponent: 0, outcomeText: 'החמצה הדדית? <span class="icon">🐇</span> <span class="icon">🦌</span> אתה צדת ארנבת בטוחה, והיריב ניסה אייל לבד (ונכשל). אולי פספסתם משהו גדול יותר?' },
            hare: { user: 1, opponent: 1, outcomeText: 'ברירת מחדל. <span class="icon">🐇</span> <span class="icon">🐇</span> שניכם בחרתם בארנבת הקטנה והבטוחה. קיבלתם רווח מינימלי...' }
        }
    };

    let yourTotalScore = 0;
    let opponentTotalScore = 0;
    let roundNumber = 0;
    let isProcessing = false; // Flag to prevent multiple clicks

    const yourTotalScoreEl = document.getElementById('yourTotalScore');
    const opponentTotalScoreEl = document.getElementById('opponentTotalScore');
    const roundNumberEl = document.getElementById('roundNumber');
    const roundResultEl = document.getElementById('roundResult');
    const yourChoiceDisplayEl = document.getElementById('yourChoiceDisplay');
    const opponentChoiceDisplayEl = document.getElementById('opponentChoiceDisplay');
    const outcomeDisplayEl = document.getElementById('outcomeDisplay');
    const yourPayoffDisplayEl = document.getElementById('yourPayoffDisplay');
    const opponentPayoffDisplayEl = document.getElementById('opponentPayoffDisplay');
    const nextRoundBtn = document.getElementById('nextRoundBtn');
    const choiceBtns = document.querySelectorAll('.choice-btn');
    const toggleExplanationBtn = document.getElementById('toggleExplanation');
    const explanationEl = document.getElementById('explanation');
     const playerStatusEl = document.getElementById('playerStatus');


    function updateScoresDisplay() {
        roundNumberEl.textContent = roundNumber;
        yourTotalScoreEl.textContent = yourTotalScore;
        opponentTotalScoreEl.textContent = opponentTotalScore;
    }

    function disableChoices() {
        choiceBtns.forEach(btn => btn.disabled = true);
    }

    function enableChoices() {
        choiceBtns.forEach(btn => {
            btn.disabled = false;
            btn.classList.remove('selected'); // Remove selected highlight
        });
    }

    function showResultArea() {
         roundResultEl.style.display = 'block';
         // Add a slight delay before adding visible class for CSS transition
         setTimeout(() => {
             roundResultEl.classList.add('visible');
         }, 10);
    }

    function hideResultArea() {
        roundResultEl.classList.remove('visible');
        // Hide only after transition might have finished
        setTimeout(() => {
             roundResultEl.style.display = 'none';
        }, 500); // Match CSS transition duration
    }


    function playGame(yourChoice) {
        if (isProcessing) return; // Prevent double clicks
        isProcessing = true;

        disableChoices();
        choiceBtns.forEach(btn => {
            if (btn.dataset.choice === yourChoice) {
                 btn.classList.add('selected'); // Highlight user's choice
                 btn.classList.add('selecting'); // Add animation class
            }
        });

        roundNumber++;
        updateScoresDisplay();

        // Simulate opponent thinking time and choice
        const opponentChoice = Math.random() < 0.5 ? 'stag' : 'hare'; // Simple random AI

        // Show player status area and choices during the "think" phase
        playerStatusEl.style.display = 'flex'; // Use flex for alignment
        yourChoiceDisplayEl.innerHTML = `אתה בחרת: <span class="${yourChoice === 'stag' ? 'text-success' : 'text-warning'}">${yourChoice === 'stag' ? 'אייל <span class="icon">🦌</span>' : 'ארנבת <span class="icon">🐇</span>'}</span>`;
        opponentChoiceDisplayEl.innerHTML = `היריב חושב... <span class="icon">🤔</span>`;


        // Wait a moment before revealing opponent's choice and outcome
        setTimeout(() => {
            choiceBtns.forEach(btn => btn.classList.remove('selecting')); // Stop animation


            const outcome = payoffMatrix[yourChoice][opponentChoice];

            yourTotalScore += outcome.user;
            opponentTotalScore += outcome.opponent;

            // Update opponent's choice display
            opponentChoiceDisplayEl.innerHTML = `היריב בחר: <span class="${opponentChoice === 'stag' ? 'text-success' : 'text-warning'}">${opponentChoice === 'stag' ? 'אייל <span class="icon">🦌</span>' : 'ארנבת <span class="icon">🐇</span>'}</span>`;


            // Display results with animation
            outcomeDisplayEl.innerHTML = outcome.outcomeText;
            yourPayoffDisplayEl.textContent = outcome.user;
            opponentPayoffDisplayEl.textContent = outcome.opponent;
             // Color payoff based on value
            yourPayoffDisplayEl.style.color = outcome.user > 0 ? varFromCSS('--success-color') : varFromCSS('--danger-color');
            opponentPayoffDisplayEl.style.color = outcome.opponent > 0 ? varFromCSS('--success-color') : varFromCSS('--danger-color');


            updateScoresDisplay();
            showResultArea();

            // Show next round button
            nextRoundBtn.style.display = 'block';
            isProcessing = false; // Allow next action
        }, 1500); // Simulate thinking time


    }

    function resetRound() {
        hideResultArea();
        nextRoundBtn.style.display = 'none';
        playerStatusEl.style.display = 'none'; // Hide status display
        enableChoices(); // Re-enable choice buttons
    }

     // Helper to get CSS variable value
    function varFromCSS(varName) {
        return getComputedStyle(document.documentElement).getPropertyValue(varName);
    }

    // Event Listeners for choice buttons
    choiceBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            playGame(btn.dataset.choice);
        });
    });

    // Event Listener for next round button
    nextRoundBtn.addEventListener('click', resetRound);

    // Event Listener for explanation toggle button
    toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationEl.style.display === 'none';
        if (isHidden) {
            explanationEl.style.display = 'block';
            // Optional: Add an animation class if desired
             // explanationEl.classList.add('fade-in'); // Needs corresponding CSS
        } else {
             // Optional: Add an animation class before hiding
             // explanationEl.classList.remove('fade-in'); // Needs corresponding CSS
            explanationEl.style.display = 'none';
        }
        toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר מעמיק' : 'מה מסתתר מאחורי דילמת צייד האיילים? (הצג/הסתר הסבר)';
    });

    // Initial display update
    updateScoresDisplay();

</script>