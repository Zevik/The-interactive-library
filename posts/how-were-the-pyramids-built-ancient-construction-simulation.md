---
title: "תעלומת הפירמידות: נבנה אותן בעצמנו (כמעט!)"
english_slug: how-were-the-pyramids-built-ancient-construction-simulation
category: "ארכאולוגיה"
tags:
  - פירמידות
  - מצרים העתיקה
  - הנדסה עתיקה
  - טכנולוגיה
  - בנייה
---
<div class="interactive-module-container">
    <h1>תעלומת הפירמידות: נבנה אותן בעצמנו (כמעט!)</h1>

    <p>דמיינו אתגר ענק: להרים סלעים במשקל מכוניות ענקיות לגובה בניין של 50 קומות - בלי מנופים או משאיות מודרניות! כך בנו המצרים את הפירמידות העצומות, תעלומה הנדסית שמסקרנת אותנו עד היום. הפירמידה הגדולה בגיזה לבדה מכילה מיליוני אבנים כאלה. איך, למען האלים המצרים, הם עשו את זה? בואו נצלול אל התאוריות המובילות וננסה להרגיש את הקושי בעצמנו.</p>

    <div id="simulation-app" class="simulation-container">
        <h2>המשימה שלכם: העלו אבן ענקית לגובה הפירמידה!</h2>
        <p>בחרו את השיטה העתיקה בה תשתמשו כדי להרים את האבן. כל שיטה מציבה אתגרים שונים...</p>

        <div id="method-selection" class="method-buttons">
            <button data-method="straight_ramp">רמפה ישרה 📏</button>
            <button data-method="spiral_ramp">רמפה לוליינית 🌀</button>
            <button data-method="levers">מנופים/מנופי נדנדה ✨</button>
            <button data-method="rolling_objects">אובייקטים מתגלגלים 🪵</button>
        </div>

        <div id="simulation-output" class="simulation-output">
            <h3>🚧 סימולציית הרמה 🚧</h3>
            <div id="output-text" class="output-text">בחרו שיטה והתחילו את האתגר!</div>
            <div class="progress-area">
                <div class="progress-bar-container">
                    <div id="progress-bar" class="progress-bar">
                        <span id="progress-text">ממתין...</span>
                    </div>
                </div>
                <div id="simulation-status-icon" class="status-icon"></div>
            </div>
            <div id="stats" class="stats-output">
                <h4>📊 הערכת מאמץ ותוצאות (משוער) 📊</h4>
                <p>💪 <strong>כוח אדם נדרש:</strong> <span id="manpower">-</span></p>
                <p>⏱️ <strong>קצב התקדמות:</strong> <span id="speed">-</span></p>
                <p>🧠 <strong>מורכבות השיטה:</strong> <span id="complexity">-</span></p>
                <p>⚖️ <strong>יעילות לאבן גדולה:</strong> <span id="efficiency">-</span></p>
            </div>
        </div>
    </div>

    <button id="toggle-explanation" class="toggle-explanation-button">על הקצה: הצג הסבר מורחב על בניית הפירמידות</button>

    <div id="explanation-content" class="explanation-content">
        <h2>הסבר מורחב: פענוח תעלומת הבנייה העתיקה</h2>

        <h3>מבוא: הפירמידות – מבני נצח של עוצמה וידע</h3>
        <p>הפירמידות המצריות, ובראשן הפירמידה הגדולה בגיזה, הן פלאים אדריכליים שנבנו לפני אלפי שנים, ללא הטכנולוגיה המודרנית שאנו מכירים. הן שימשו כמבני קבורה מלכותיים והעידו על כוחה האדיר, עושרה והארגון המרשים של הממלכה המצרית העתיקה. היקף העבודה והדיוק הנדרשים לבנייתן עצומים, והן עדיין מהוות עדות מדהימה ליכולותיהם של המצרים הקדמונים.</p>

        <h3>האתגרים ההנדסיים האדירים</h3>
        <p>בניית הפירמידה הציבה בפני המצרים אתגרים הנדסיים בקנה מידה שקשה לדמיין:</p>
        <ul>
            <li><strong>משקל עצום:</strong> רבות מהאבנים, במיוחד בבסיס ובליבת המבנה, שקלו עשרות טונות. אבני הגרניט שבתקרות חדרי הקבורה שקלו אף מאות טונות!</li>
            <li><strong>גובה מסחרר:</strong> הפירמידה הגדולה התנשאה לגובה של כ-146 מטרים (שווה ערך לכבניין בן 50 קומות!), מה שהפך את העלאת האבנים לגובה למשימה מורכבת ומסוכנת.</li>
            <li><strong>דיוק מדהים:</strong> האבנים הותאמו זו לזו בדיוק כירורגי כמעט, וכל המבנה כוון בקפידה לעבר הצפון האמיתי – הישג מרשים ללא מכשירי מדידה מודרניים.</li>
        </ul>

        <h3>מסע האבן: ממחצבה אל הפירמידה</h3>
        <p>הובלת האבנים הייתה מבצע לוגיסטי מורכב ביותר:</p>
        <ul>
            <li><strong>הובלה יבשתית:</strong> רוב האבנים היו אבן גיר מקומית. הן נחצבו והונחו על מזחלות עץ שנמשכו על ידי מאות פועלים. עדויות ציוריות מראות שהם שפכו מים או נוזל אחר לפני המזחלות כדי להפחית חיכוך – טכניקה מבריקה! גלגלים לא היו יעילים למשאות כבדים כאלו על הקרקע המדברית.</li>
            <li><strong>הובלה ימית:</strong> אבנים מיוחדות (כמו אבן גיר איכותית לחיפוי וגרניט) הגיעו ממחצבות רחוקות (טורא, אסואן) דרך נהר הנילוס. הן הובלו בסירות משא ענקיות, וייתכן שגם דרך רשת תעלות מיוחדות שנחפרו עד לאתר הבנייה בגיזה.</li>
        </ul>

        <h3>התעלומה הגדולה: איך העלו את האבנים לגובה?</h3>
        <p>זהו אחד המסתורין הגדולים ביותר בארכיאולוגיה, והחוקרים עדיין מתווכחים על הפרטים המדויקים. ההשערות העיקריות הן:</p>
        <ul>
            <li><strong>תאוריות הרמפות:</strong> ההשערה הנפוצה ביותר היא שימוש ברמפות עפר ולבני בוץ שהוקמו סביב הפירמידה. האבנים נמשכו על מזחלות לאורך הרמפות על ידי צוותי פועלים גדולים.
                <ul>
                    <li><strong>רמפה ישרה:</strong> רמפה אחת ארוכה וישרה לצד אחד. <strong>חסרונות:</strong> דורשת כמות אדירה של חומרים ושטח, השיפוע הופך לתלול מאוד בקלות, וקשה לבנותה לגובה רב.</li>
                    <li><strong>רמפה לוליינית (ספירלית):</strong> רמפה שעולה סביב הפירמידה. <strong>יתרונות:</strong> קצרה יותר מרמפה ישרה באותו שיפוע, דורשת פחות חומר. <strong>חסרונות:</strong> מורכבת יותר לבנייה, מסתירה חלק מהפירמידה (מקשה על מדידות), דורשת תמרון קשה בפינות.</li>
                    <li><strong>רמפת זיגזג / פנימית:</strong> ייתכנו גם רמפות קצרות שעולות בזיגזג בצד אחד, או אפילו רמפה פנימית בתוך הפירמידה עצמה (כפי שהוצע במחקרים מסוימים).</li>
                </ul>
            </li>
            <li><strong>תאוריות חלופיות:</strong>
                <ul>
                    <li><strong>מנופים (Levers):</strong> שימוש במנופי עץ פשוטים או מורכבים יותר (כמו ה-Shadoof ששימש להרמת מים), אולי בשילוב עם מבנים או מנופי נדנדה. <strong>היתכנות:</strong> סבירה להרמת אבנים קטנות או יחסית, או לשלבי הגימור העליונים. לא סביר כאמצעי בלעדי לאבנים הגדולות ביותר.</li>
                    <li><strong>אובייקטים מתגלגלים / מסילות:</strong> השערות פחות מקובלות מדברות על שימוש במנגנוני גלילים או מסילות עץ מיוחדות שאפשרו גלגול האבנים. <strong>היתכנות:</strong> פוטנציאל למהירות במישור, אך מאתגר ביותר בשיפועים ולגובה, ודורש מנגנונים עמידים ומדויקים.</li>
                </ul>
            </li>
        </ul>

        <h3>מי עבד ואיך התנהל הפרויקט?</h3>
        <p>הערכות כוח האדם נעות בין עשרות אלפים למאה אלף עובדים. המחקר המודרני מסכים שהם לא היו עבדים, אלא בעיקר איכרים שעבדו בפרויקט בתקופת ההצפה של הנילוס (כאשר לא יכלו לעבד את שדותיהם), לצד צוות קבוע של אנשי מלאכה מקצועיים (סתתים, מודדים, מהנדסים, פקחים). הארגון המצרי המרכזי, היכולת לגייס, להאכיל ולתחזק מספר עצום של אנשים, היה גורם קריטי להצלחה.</p>

        <h3>כלים וטכניקות</h3>
        <p>הבונים השתמשו בכלים פשוטים אך יעילים: אזמלי נחושת (שדרשו חידוד מתמיד) ומאוחר יותר ברזל, פטישי אבן ועץ, מפסלות, פלסים פשוטים (מבוססי מים או שוות משקל), כלי מדידה (חבלים מסומנים, ריבועים), מזחלות, חבלים חזקים (מסיבים צמחיים), ועצים לפיגומים או רמפות.</p>

        <h3>מסתורין מתמשך ומחקר חדשני</h3>
        <p>למרות התקדמות המחקר וההדמיות, עדיין קיימים ויכוחים לגבי שיטות הבנייה המדויקות ביותר. ארכיאולוגים ממשיכים לגלות עדויות חדשות, כמו שרידי רמפות מיוחדות או יומני עבודה עתיקים. ייתכן שהמצרים השתמשו בשילוב של שיטות שונות לגבהים שונים או לסוגי אבנים שונים. המחקר המתמשך ממשיך לשפוך אור על ההיבטים המדהימים של ההנדסה, הפיזיקה והארגון החברתי במצרים העתיקה – ורק מעמיק את ההערכה שלנו להישגיהם.</p>
    </div>
</div>

<style>
    /* גופנים בסיסיים - ניתן לשדרג עם Google Fonts אם מאושר */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f4f4f2; /* רקע בהיר עדין */
        margin: 0;
        padding: 20px;
        direction: rtl; /* תמיכה בעברית */
        text-align: right; /* תמיכה בעברית */
    }

    h1, h2, h3, h4 {
        color: #5d4037; /* חום כהה - צבע אדמה */
        margin-bottom: 15px;
    }

    h1 {
        text-align: center;
        color: #1a237e; /* כחול כהה - מלכותי */
        margin-bottom: 30px;
        font-size: 2.5em;
    }

    h2 {
        font-size: 1.8em;
        border-bottom: 2px solid #ffca28; /* קו צהוב/זהב עדין */
        padding-bottom: 5px;
    }

    h3 {
         font-size: 1.5em;
         color: #4e342e; /* חום בינוני */
    }

     h4 {
         font-size: 1.2em;
         color: #6d4c41; /* חום בהיר יותר */
         margin-bottom: 10px;
     }


    p {
        margin-bottom: 15px;
    }

    ul {
        margin-bottom: 15px;
        padding-right: 20px;
    }

    li {
        margin-bottom: 8px;
    }

    .interactive-module-container {
        max-width: 900px;
        margin: 20px auto;
        background-color: #fff;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        border: 1px solid #e0e0e0;
    }

    .simulation-container {
        border: 2px dashed #ffca28; /* מסגרת מקווקוות בצבע זהב */
        padding: 25px;
        margin-bottom: 30px;
        background-color: #fff9c4; /* רקע בהיר לסימולציה */
        border-radius: 8px;
        text-align: center; /* ליישור כפתורים ומרכיבים */
    }

    .simulation-container h2 {
        color: #c62828; /* אדום כהה - צבע אתגר */
        margin-top: 0;
        border-bottom: none;
    }


    .method-buttons {
        margin: 20px 0;
    }

    .method-buttons button {
        margin: 8px;
        padding: 12px 25px;
        cursor: pointer;
        background: linear-gradient(180deg, #66bb6a 0%, #43a047 100%); /* ירוק עשיר */
        color: white;
        border: none;
        border-radius: 25px; /* כפתורים עגולים יותר */
        font-size: 1em;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 3px 8px rgba(0, 0, 0, 0.2);
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }

    .method-buttons button:hover {
        background: linear-gradient(180deg, #4caf50 0%, #388e3c 100%);
        transform: translateY(-2px);
        box-shadow: 0 5px 12px rgba(0, 0, 0, 0.3);
    }

     .method-buttons button:active {
         transform: translateY(0);
         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
     }


    .simulation-output {
        margin-top: 25px;
        padding: 20px;
        border: 1px solid #ffeb3b; /* מסגרת צהובה בהירה */
        background-color: #fff;
        border-radius: 8px;
        min-height: 250px; /* גובה מינימלי כדי למנוע קפיצות */
        position: relative; /* למיקום האייקון */
        overflow: hidden; /* לוודא שהכל בפנים */
    }

    .simulation-output h3 {
         color: #0288d1; /* כחול בהיר יותר */
         margin-top: 0;
    }

    .output-text {
        font-size: 1.1em;
        color: #555;
        min-height: 50px; /* גובה מינימלי לטקסט */
        display: flex; /* ליישור אנכי */
        align-items: center;
        justify-content: center; /* ליישור אופקי במידת הצורך */
        margin-bottom: 15px;
        text-align: center;
    }

    .progress-area {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 20px;
    }

    .progress-bar-container {
        flex-grow: 1; /* תופס את רוב השטח */
        width: 100%; /* לוודא שמתרחב */
        background-color: #e0e0e0;
        border-radius: 15px;
        height: 35px; /* גובה גבוה יותר */
        overflow: hidden;
        position: relative;
    }

    .progress-bar {
        width: 0%; /* Initial state */
        height: 100%;
        background: linear-gradient(90deg, #0288d1 0%, #03a9f4 100%); /* כחול יפהפה */
        text-align: center;
        line-height: 35px; /* מרכוז טקסט */
        color: white;
        font-weight: bold;
        transition: width 1s ease-in-out; /* Smooth transition */
        display: flex;
        align-items: center;
        justify-content: flex-end; /* יישור הטקסט לימין בתוך הפס */
        padding-left: 10px;
        box-sizing: border-box; /* לוודא פדינג בפנים */
    }

     #progress-text {
         text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
         direction: ltr; /* לוודא שהמספרים נכונים */
         margin-left: 10px; /* רווח מהקצה */
     }


    .status-icon {
        width: 40px;
        height: 40px;
        background-size: cover;
        background-position: center;
        /* אייקונים ייקבעו דרך JS או CSS class */
        /* דוגמא: background-image: url('path/to/hammer-icon.png'); */
        transition: transform 0.5s ease-in-out;
    }

    /* דוגמא לאייקונים - אם רוצים לשלב */
    /* .status-icon.working { background-image: url('hammer.svg'); animation: pulse 1s infinite alternate; } */
    /* .status-icon.difficult { background-image: url('sweat.svg'); } */
    /* .status-icon.complete { background-image: url('check.svg'); } */
    @keyframes pulse {
        from { transform: scale(1); }
        to { transform: scale(1.1); }
    }


    .stats-output {
        margin-top: 20px;
        padding: 15px;
        border-top: 1px dashed #ffeb3b;
        background-color: #fffde7; /* רקע עדין לסטטיסטיקות */
        border-radius: 5px;
        text-align: right;
    }

    .stats-output p {
        margin: 5px 0;
        font-size: 0.95em;
        color: #444;
    }

    .stats-output span {
        font-weight: bold;
        color: #00796b; /* צבע טורקיז/ירוק יפה */
    }

    .toggle-explanation-button {
        display: block; /* כפתור רחב */
        width: fit-content; /* רוחב לפי התוכן */
        margin: 30px auto 20px auto; /* ממורכז */
        padding: 12px 25px;
        cursor: pointer;
        background: linear-gradient(180deg, #ff9800 0%, #f57c00 100%); /* כתום/זהב */
        color: white;
        border: none;
        border-radius: 25px;
        font-size: 1em;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 3px 8px rgba(0, 0, 0, 0.2);
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }

     .toggle-explanation-button:hover {
         background: linear-gradient(180deg, #fb8c00 0%, #ef6c00 100%);
         transform: translateY(-2px);
         box-shadow: 0 5px 12px rgba(0, 0, 0, 0.3);
     }

     .toggle-explanation-button:active {
         transform: translateY(0);
         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
     }


    .explanation-content {
        display: none; /* Hidden by default */
        border-top: 2px solid #1a237e; /* קו כחול כהה */
        margin-top: 30px;
        padding-top: 25px;
        background-color: #e8f5e9; /* רקע ירוק עדין להסבר */
        border-radius: 8px;
        padding: 25px;
    }

    .explanation-content h2 {
        color: #1a237e; /* כחול כהה */
         border-bottom: 2px solid #c5e1a5; /* קו ירוק בהיר */
    }

    .explanation-content h3 {
        color: #388e3c; /* ירוק כהה */
    }

    .explanation-content ul {
        list-style: disc inside; /* תבליטים עגולים */
    }

    .explanation-content ul ul {
        list-style: circle inside; /* תבליטים פנימיים עגולים ריקים */
        margin-top: 5px;
        margin-bottom: 5px;
    }

    /* אנימציות עדינות */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

     .explanation-content.visible {
         display: block;
         animation: fadeIn 0.8s ease-out;
     }

     /* ריספונסיביות בסיסית */
     @media (max-width: 768px) {
         .interactive-module-container {
             padding: 20px;
             margin: 10px auto;
         }

         h1 {
             font-size: 2em;
         }

         h2 {
             font-size: 1.5em;
         }

         .method-buttons button {
             width: 100%; /* כפתורים מלאים ברוחב במסכים קטנים */
             margin-bottom: 10px;
         }

         .progress-area {
            flex-direction: column; /* עמודה במסכים קטנים */
            gap: 10px;
         }

         .status-icon {
             order: -1; /* להעביר את האייקון למעלה */
         }
     }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const explanationButton = document.getElementById('toggle-explanation');
        const explanationContent = document.getElementById('explanation-content');
        const methodButtons = document.querySelectorAll('#method-selection button');
        const outputText = document.getElementById('output-text');
        const progressBar = document.getElementById('progress-bar');
        const progressText = document.getElementById('progress-text');
        const manpowerSpan = document.getElementById('manpower');
        const speedSpan = document.getElementById('speed');
        const complexitySpan = document.getElementById('complexity');
        const efficiencySpan = document.getElementById('efficiency');
        const simulationStatusIcon = document.getElementById('simulation-status-icon');
        const simulationOutput = document.getElementById('simulation-output'); // לשינוי רקע

        let simulationInterval = null; // לניהול האנימציה

        // Toggle explanation visibility with animation
        explanationButton.addEventListener('click', () => {
            const isHidden = explanationContent.style.display === 'none' || explanationContent.style.display === '';
            if (isHidden) {
                explanationContent.style.display = 'block';
                // Add a class to trigger CSS animation
                setTimeout(() => explanationContent.classList.add('visible'), 10); // Small delay for display to register
                explanationButton.textContent = 'חזרה: הסתר הסבר מורחב';
            } else {
                explanationContent.classList.remove('visible');
                 // Wait for animation to finish before hiding
                explanationContent.addEventListener('animationend', function handler() {
                    explanationContent.style.display = 'none';
                    explanationContent.removeEventListener('animationend', handler);
                });
                explanationButton.textContent = 'על הקצה: הצג הסבר מורחב על בניית הפירמידות';
            }
        });

        // Simulation interaction
        methodButtons.forEach(button => {
            button.addEventListener('click', () => {
                const method = button.getAttribute('data-method');
                simulateMethod(method);
            });
        });

        function simulateMethod(method) {
            // Clear previous simulation
            clearInterval(simulationInterval);
            progressBar.style.width = '0%';
            progressText.textContent = 'מתחילים...';
            outputText.textContent = 'מכינים את המשא...';
            manpowerSpan.textContent = '-';
            speedSpan.textContent = '-';
            complexitySpan.textContent = '-';
            efficiencySpan.textContent = '-';
            simulationStatusIcon.style.backgroundImage = ''; // Clear icon
            simulationStatusIcon.classList.remove('working', 'difficult', 'complete');
            simulationOutput.style.backgroundColor = '#fff'; // Reset background


            let methodData = {};
            let stages = []; // Define animation stages

            switch (method) {
                case 'straight_ramp':
                    methodData = {
                        name: "רמפה ישרה",
                        manpower: 'גבוה מאוד',
                        speed: 'איטי (אך יציב)',
                        complexity: 'נמוכה (בנייה)',
                        efficiency: 'נמוכה (לגובה)',
                        stages: [
                            { width: 10, text: "מתחילים למשוך את האבן במעלה הרמפה הארוכה...", icon: 'hammer.svg', status:'working' },
                            { width: 30, text: "השיפוע מתחיל להקשות, נדרשים עוד פועלים...", icon: 'sweat.svg', status:'difficult' },
                            { width: 60, text: "הדרך עוד ארוכה מאוד, המאמץ מצטבר...", icon: 'sweat.svg', status:'difficult' },
                            { width: 85, text: "קרוב למטרה, המשיכה האחרונה קשה במיוחד!", icon: 'hammer.svg', status:'working' },
                            { width: 100, text: "האבן הגיעה ליעדה על הרמפה! (אבל לבנות כזו רמפה לגובה הפירמידה זה סיפור אחר...)", icon: 'check.svg', status:'complete' }
                        ],
                         bgColor: '#ffebee' // רקע עדין לאדום/מאמץ
                    };
                    break;
                case 'spiral_ramp':
                    methodData = {
                        name: "רמפה לוליינית",
                        manpower: 'גבוה',
                        speed: 'בינוני',
                        complexity: 'בינונית (בנייה ותמרון)',
                        efficiency: 'בינונית',
                        stages: [
                            { width: 15, text: "מתחילים לעלות סביב הפירמידה, המשיכה יחסית קלה...", icon: 'hammer.svg', status:'working' },
                            { width: 40, text: "פונים בפינה! נדרש תיאום ותמרון מדויק...", icon: 'sweat.svg', status:'difficult' },
                            { width: 70, text: "ממשיכים לעלות, הדרך מתפתלת...", icon: 'hammer.svg', status:'working' },
                            { width: 90, text: "הקפה אחרונה לפני הגובה הנדרש...", icon: 'hammer.svg', status:'working' },
                            { width: 100, text: "האבן הונחה בהצלחה במיקום על הפירמידה!", icon: 'check.svg', status:'complete' }
                        ],
                         bgColor: '#fff3e0' // רקע עדין לכתום/זהב
                    };
                    break;
                case 'levers':
                    methodData = {
                        name: "מנופים",
                        manpower: 'בינוני (אך נדרשת מיומנות)',
                        speed: 'איטי (לאבנים גדולות)',
                        complexity: 'בינונית (תכנון ותפעול)',
                        efficiency: 'נמוכה (לאבנים הגדולות ביותר)', // יעיל יותר לקטנות
                         stages: [
                            { width: 20, text: "ממקמים את המנופים ומחברים לאבן...", icon: 'hammer.svg', status:'working' },
                            { width: 50, text: "מפעילים את המנופים! הרמה איטית ומבוקרת... דורש כוח רב!", icon: 'sweat.svg', status:'difficult' },
                            { width: 80, text: "כמעט בגובה הרצוי, תיאום קריטי להצלחה...", icon: 'hammer.svg', status:'working' },
                             { width: 100, text: "האבן הועלתה באמצעות מערכת מנופים (סביר יותר לאבן קטנה או למיקום עליון)!", icon: 'check.svg', status:'complete' }
                        ],
                         bgColor: '#e3f2fd' // רקע עדין לכחול/טכניקה
                    };
                    break;
                case 'rolling_objects':
                    methodData = {
                        name: "אובייקטים מתגלגלים",
                        manpower: 'בינוני עד גבוה',
                        speed: 'פוטנציאל למהיר (במישור), איטי (בשיפוע)',
                        complexity: 'גבוהה (מנגנון ומסילות)',
                        efficiency: 'נמוכה (בשיפוע תלול)',
                         stages: [
                            { width: 10, text: "מניחים את האבן על הגלילים/מסילות...", icon: 'hammer.svg', status:'working' },
                            { width: 30, text: "מתחילים לגלגל את האבן קדימה, חלק יחסית על משטח מפולס...", icon: 'hammer.svg', status:'working' },
                             { width: 60, text: "מתמודדים עם שיפוע! הגלגול קשה מאוד ודורש מאמץ ענק!", icon: 'sweat.svg', status:'difficult' },
                            { width: 90, text: "כמעט שם, מקפידים שהאבן לא תחליק אחורה...", icon: 'sweat.svg', status:'difficult' },
                             { width: 100, text: "האבן הגיעה ליעדה בשיטת הגלגול! (יישום מעשי לגובה עדיין נחקר...)", icon: 'check.svg', status:'complete' }
                        ],
                         bgColor: '#fff9c4' // רקע עדין לצהוב/חומר
                    };
                    break;
                default:
                    // Reset to initial state if somehow called with wrong method
                    outputText.textContent = "בחרו שיטה כדי לראות הדגמה ותוצאות משוערות.";
                    progressText.textContent = 'ממתין...';
                    manpowerSpan.textContent = '-';
                    speedSpan.textContent = '-';
                    complexitySpan.textContent = '-';
                    efficiencySpan.textContent = '-';
                    simulationOutput.style.backgroundColor = '#fff';
                    return;
            }

            // Set initial stats
             manpowerSpan.textContent = methodData.manpower;
             speedSpan.textContent = methodData.speed;
             complexitySpan.textContent = methodData.complexity;
             efficiencySpan.textContent = methodData.efficiency;

            // Animate through stages
            let currentStageIndex = 0;
            let currentWidth = 0;
             const durationPerStage = 2000; // מ"ש לכל שלב (ניתן לשנות)

            simulationOutput.style.backgroundColor = methodData.bgColor || '#fff';


            simulationInterval = setInterval(() => {
                 if (currentStageIndex < methodData.stages.length) {
                    const stage = methodData.stages[currentStageIndex];

                    // Animate width
                    progressBar.style.width = stage.width + '%';
                    progressText.textContent = `מתקדם... ${stage.width}%`; // עדכון אחוזים

                    // Update text and icon
                    outputText.textContent = stage.text;

                    // Simple icon update (requires icons to be available or use background position/class)
                    // For this example, we'll use CSS classes to indicate status
                    simulationStatusIcon.classList.remove('working', 'difficult', 'complete');
                    if (stage.status) {
                        simulationStatusIcon.classList.add(stage.status);
                        // Note: Actual background image needs to be defined in CSS or set here if available
                        // Example: simulationStatusIcon.style.backgroundImage = `url('${stage.icon}')`;
                         // Let's use background color instead for simplicity and consistency with CSS only
                         if (stage.status === 'working') simulationStatusIcon.style.backgroundColor = '#4CAF50'; // Green
                         if (stage.status === 'difficult') simulationStatusIcon.style.backgroundColor = '#FF9800'; // Orange
                         if (stage.status === 'complete') simulationStatusIcon.style.backgroundColor = '#2196F3'; // Blue
                         simulationStatusIcon.style.borderRadius = '50%'; // Make it a circle
                         simulationStatusIcon.style.opacity = '1';
                         simulationStatusIcon.style.transform = 'scale(1)';


                    } else {
                         simulationStatusIcon.style.backgroundColor = 'transparent'; // No icon state
                         simulationStatusIcon.style.opacity = '0';
                         simulationStatusIcon.style.transform = 'scale(0)';
                    }


                    currentStageIndex++;
                 } else {
                    // Simulation complete
                    clearInterval(simulationInterval);
                    progressText.textContent = 'הושלם!';
                    simulationStatusIcon.classList.add('complete');
                     simulationStatusIcon.style.backgroundColor = '#2196F3'; // Blue complete
                     simulationStatusIcon.style.borderRadius = '50%';
                     simulationStatusIcon.style.opacity = '1';
                     simulationStatusIcon.style.transform = 'scale(1.2)'; // Pop slightly

                 }
            }, durationPerStage); // Interval time

             // Trigger the first stage immediately
             const initialStage = methodData.stages[0];
             progressBar.style.width = initialStage.width + '%';
             progressText.textContent = `מתקדם... ${initialStage.width}%`;
             outputText.textContent = initialStage.text;
             simulationStatusIcon.classList.remove('working', 'difficult', 'complete');
             if (initialStage.status) {
                 simulationStatusIcon.classList.add(initialStage.status);
                 if (initialStage.status === 'working') simulationStatusIcon.style.backgroundColor = '#4CAF50';
                 if (initialStage.status === 'difficult') simulationStatusIcon.style.backgroundColor = '#FF9800';
                 simulationStatusIcon.style.borderRadius = '50%';
                 simulationStatusIcon.style.opacity = '1';
                 simulationStatusIcon.style.transform = 'scale(1)';
             } else {
                 simulationStatusIcon.style.backgroundColor = 'transparent';
                 simulationStatusIcon.style.opacity = '0';
                 simulationStatusIcon.style.transform = 'scale(0)';
             }

             currentStageIndex = 1; // Move to the next stage for the interval
        }


        // Initial state
        explanationContent.style.display = 'none';
        explanationContent.classList.remove('visible'); // Ensure animation class is off initially
         simulationStatusIcon.style.opacity = '0'; // Hide icon initially
         simulationStatusIcon.style.transform = 'scale(0)';

    });
</script>