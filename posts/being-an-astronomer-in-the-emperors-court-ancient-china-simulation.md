---
title: "להיות אסטרונום בחצר הקיסר: סימולציה בסין העתיקה"
english_slug: being-an-astronomer-in-the-emperors-court-ancient-china-simulation
category: "אסטרונומיה"
tags: [אסטרונומיה, סין העתיקה, היסטוריה של המדע, ליקויים, לוח שנה, סימולציה]
---
# להיות אסטרונום בחצר הקיסר: סימולציה בסין העתיקה

דמיינו את עצמכם עומדים בפני הדרקון, לחוצים לנבא את גורל האימפריה רק על פי תנועת הכוכבים. האם תחזיקו מעמד בחצר הקיסר, או שליקוי חמה בלתי צפוי ישלח אתכם אל הגרדום? היכנסו לתפקיד האסטרונום הראשי ושחקו על חייכם!

<div class="simulation-container" id="simulation-app">
    <div class="header-area">
        <h2 class="simulation-title">משרד לוח השנה הקיסרי</h2>
        <p class="subtitle">שלטו בכוכבים... או הישלטו על ידם.</p>
    </div>
    <div id="scenario-area" class="game-area">
        <div id="scenario-text" class="text-block">
            <p>שנת XX של השושלת הגדולה. עיני הקיסר וגורלם של מיליונים נשואים אליכם. אתם האסטרונום הראשי, הממונה על קריאת השמיים, ניבוי האותות השמימיים, ושמירה על דיוק הלוח הקיסרי הקדוש. כישלון פירושו תוהו ובוהו... ולרוב, גם עונש מוות.</p>
            <p>נשימה עמוקה. זהו היום הראשון בתפקיד.</p>
            <button class="start-button" onclick="startSimulation()">התחילו את המשחק</button>
        </div>
        <div id="options-container" class="options-block">
            <!-- Options will appear here -->
        </div>
        <div id="result-text" class="result-block">
            <!-- Results will appear here -->
        </div>
    </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Hebrew:wght@400;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&display=swap'); /* Optional: for a slightly more 'epic' feel in titles */


    .simulation-container {
        font-family: 'Noto Sans Hebrew', sans-serif;
        max-width: 700px;
        margin: 40px auto;
        padding: 30px;
        border: 1px solid #a08a73; /* Softer, earthy border */
        border-radius: 12px;
        background: linear-gradient(to bottom, #fefae0, #faedcd); /* Soft, warm background */
        box-shadow: 8px 8px 20px rgba(0, 0, 0, 0.2); /* More pronounced shadow */
        direction: rtl;
        text-align: right;
        position: relative; /* Needed for potential absolute positioning of decorative elements */
        overflow: hidden; /* Hide potential overflow from animations */
    }

     /* Add a subtle pattern or texture */
    .simulation-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHZpZXdCb3g9IjAgMCAyMCAyMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMCAtMC4yVjIwLjJIMjAuMlYwLjhIMFYtMC4yem0uNSAxLjFoMTkuMlYxOS4zSC41VjAuOXoiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlPSIjZGNjMWMxIiBmaWxsPSJub25lIiBvcGFjaXR5PSIwLjMiLz48L3N2Zz4='); /* Subtle grid pattern */
        opacity: 0.1;
        pointer-events: none; /* Ensure pattern doesn't interfere with clicks */
    }


    .header-area {
        text-align: center;
        margin-bottom: 30px;
        position: relative;
        z-index: 1; /* Ensure text is above pseudo-element */
    }

    .simulation-title {
        font-family: 'Cinzel', serif; /* Use Cinzel for titles if desired, or Noto Sans Hebrew Bold */
        font-size: 2em;
        color: #3d2e21; /* Dark brown */
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 1.1em;
        color: #5c4a3b; /* Slightly lighter brown */
        margin-top: 0;
    }

    .game-area {
         position: relative; /* For absolute positioning of animations */
    }

    .text-block {
        margin-bottom: 25px;
        padding: 20px;
        background-color: #fcf6e8; /* Lighter warm color */
        border-radius: 8px;
        line-height: 1.8;
        color: #333;
        border-left: 5px solid #d4a373; /* Decorative border */
        transition: opacity 0.6s ease-out, transform 0.6s ease-out; /* Animation */
    }

    .options-block {
        margin-bottom: 25px;
        display: flex;
        flex-direction: column;
        gap: 12px; /* Slightly more space between options */
        transition: opacity 0.6s ease-out, transform 0.6s ease-out; /* Animation */
    }

    .scenario-option, .start-button {
        display: block; /* Ensure buttons take full width in container */
        width: 100%; /* Full width */
        padding: 14px 20px; /* More padding */
        border: none;
        border-radius: 6px;
        background-color: #4a6c6f; /* Teal/blue-grey color */
        color: white;
        font-size: 1.1em;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        text-align: center; /* Center text in buttons */
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }

    .scenario-option:hover, .start-button:hover {
        background-color: #3d5b5e; /* Darker teal */
        box-shadow: 3px 3px 7px rgba(0,0,0,0.2);
    }

     .scenario-option:active, .start-button:active {
         transform: scale(0.98); /* Press effect */
         box-shadow: 1px 1px 3px rgba(0,0,0,0.2);
     }


    .result-block {
        margin-top: 25px;
        padding: 20px;
        border-radius: 8px;
        line-height: 1.8;
        font-weight: bold;
        text-align: center; /* Center result text */
        opacity: 0; /* Initially hidden for animation */
        transform: translateY(10px); /* Start slightly lower for slide-up */
        transition: opacity 0.6s ease-out, transform 0.6s ease-out; /* Animation */
    }

    /* Result States */
    .result-block.success {
        background-color: #d4edda;
        color: #155724;
        border: 1px solid #c3e6cb;
        box-shadow: 0 0 10px rgba(212, 237, 218, 0.5); /* Glowing effect */
    }

    .result-block.warning {
        background-color: #fff3cd;
        color: #856404;
        border: 1px solid #ffeeba;
         box-shadow: 0 0 10px rgba(255, 243, 205, 0.5);
    }

    .result-block.danger {
        background-color: #f8d7da;
        color: #721c24;
        border: 1px solid #f5c6cb;
         box-shadow: 0 0 10px rgba(248, 215, 218, 0.7); /* Stronger glow for danger */
    }

     .result-block.info { /* For restart message */
        background-color: #e9ecef;
        color: #495057;
        border: 1px solid #dee2e6;
        box-shadow: none;
     }


    /* Animation classes */
    .fade-out {
        opacity: 0;
        transform: translateY(-10px);
    }

    .fade-in {
        opacity: 1;
        transform: translateY(0);
    }


    #toggle-explanation {
        display: block;
        margin: 30px auto; /* More space */
        padding: 12px 25px; /* More padding */
        border: none;
        border-radius: 6px;
        background-color: #a08a73; /* Earthy tone */
        color: white;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        text-align: center;
         box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }

    #toggle-explanation:hover {
        background-color: #8d7a65;
        box-shadow: 3px 3px 7px rgba(0,0,0,0.2);
    }

     #toggle-explanation:active {
         transform: scale(0.98);
         box-shadow: 1px 1px 3px rgba(0,0,0,0.2);
     }


    #explanation {
        margin-top: 30px;
        padding: 25px; /* More padding */
        border: 1px solid #a08a73;
        border-radius: 12px;
        background-color: #fcf6e8; /* Light background */
        direction: rtl;
        text-align: right;
        line-height: 1.7;
        color: #333;
        transition: opacity 0.5s ease; /* Animation for toggle */
    }

    #explanation h3 {
        color: #3d2e21; /* Dark brown */
        margin-top: 20px;
        margin-bottom: 10px;
        border-bottom: 1px dashed #d4a373; /* Subtle separator */
        padding-bottom: 5px;
    }

    #explanation p {
        margin-bottom: 15px;
    }
</style>

<button id="toggle-explanation">הצג/הסתר רקע היסטורי</button>

<div id="explanation" style="display: none;">
    <h2 class="simulation-title">מאחורי הקלעים: אסטרונומיה בחצר הקיסר</h2>
    <h3>השמיים כמראה לממלכה: תפקיד האסטרונומיה בסין העתיקה</h3>
    <p>עבור הסינים הקדמונים, השמיים לא היו רק מרחב של גרמי אור רחוקים, אלא זירת התרחשות אלוהית המשקפת באופן ישיר את הנעשה על הארץ. האסטרונומיה שירתה שלוש מטרות קריטיות: היא הייתה מצפן לחקלאות (קביעת מועדי זריעה וקציר דרך לוח שנה מדויק), עמוד תווך לארגון המדינה והחברה (הלוח קבע חגים, טקסים, ופעילויות ממשל), והכי חשוב – שפה פוליטית ודתית שחיברה את הקיסר ישירות לשמיים.</p>

    <h3>"מנדט השמיים" (天命) והרעד הפוליטי מאירועים שמימיים</h3>
    <p>התפיסה המרכזית שקשרה אסטרונומיה לפוליטיקה הייתה "מנדט השמיים" (טְייֵן מִינְג). לפיה, הקיסר שולט בזכות ברכה שמימית, ואירועים חריגים בשמיים – ליקויים, כוכבי שביט, כוכבים חדשים (סופרנובות) – יכלו להתפרש כסימן שהשמיים אינם שבעי רצון. אי-ניבוי אירועים כאלה, או פרשנות שגויה שלהם, יכלה להיתפס ככישלון של הקיסר עצמו, לערער את סמכותו, ואף לשמש עילה להחלפת שושלת. לכן, האסטרונום המלכותי לא עסק רק במדע, אלא שימש גם יועץ פוליטי, שהיה אחראי לא רק על חישובים אלא גם על נרטיב יציב ומרגיע.</p>

    <h3>המצפים הקיסריים ואנשי הכוכבים: מוסדות ואסטרונומים</h3>
    <p>המדינה הסינית השקיעה הון עתק במוסדות אסטרונומיים רשמיים, שהחשוב בהם היה "משרד לוח השנה" (שמות כמו טָאי שִׁי או צִין טְייֵן גְ'ייֵן). מוסדות אלו העסיקו צוותים גדולים של מומחים – אסטרונומים, מתמטיקאים, סופרים – שתפקידם היה לתצפת, לחשב, ולתעד ללא הרף. אסטרונומים בולטים כמו גָאן דֶּה וְשׁי שֶׁׁן (מחברי קטלוגי כוכבים מהמאה ה-4 לפנה"ס!) וגְווֹ שׁוֹאוּגִ'ין (משושלת יואן) היו דמויות מפתח במדע הסיני.</p>

    <h3>כלים שלובים: תצפיות, חישובים והישגים</h3>
    <p>האסטרונומים הסינים פיתחו שורה של כלים גאוניים: **מצפים** עם מכשירים קבועים לתצפיות מדויקות; **שעוני שמש ולילה** (שעוני מים) למדידת זמן; **גלובוסים שמימיים** מכניים (הון אִי) להדגמה ומדידה של תנועות כוכבים; ו**ספרים אסטרונומיים** שתיעדו שיטות חישוב ותצפיות. הישגיהם כוללים את **התיעוד הארוך והרצוף ביותר בעולם של אירועים שמימיים** (ליקויים, כוכבי שביט, מטאורים, כתמי שמש), **רישום ראשון של סופרנובות** (כמו הסופרנובה של 1054 שהותירה את ערפילית הסרטן), **פיתוח לוחות שנה מהמדויקים בעולם** לתקופתם, ו**מפות שמיים וקטלוגי כוכבים** מפורטים.</p>

    <h3>אסטרונומיה, אסטרולוגיה וראיית עולם</h3>
    <p>קשה להפריד בסין העתיקה בין אסטרונומיה מדעית (תצפית וחישוב), אסטרולוגיה (פרשנות ההשפעה על חיי אדם ומדינה), וקוסמולוגיה (תמונת העולם). כל אלו היו ארוגים יחד. הכוכבים נתפסו לא רק כנקודות אור, אלא כסמלים בעלי משמעות פוליטית ואישית. האסטרונום המלכותי נדרש לשלוט בכל התחומים הללו כדי למלא את תפקידו.</p>

    <h3>מעבר לחומה הגדולה: האסטרונום הסיני בהשוואה לעולם</h3>
    <p>בעוד שתרבויות עתיקות אחרות כמו בבל, מצרים, יוון והמאיה גם הן פיתחו אסטרונומיה מרשימה למטרות דומות (לוחות שנה, פולחן), נראה שבסין הקשר המוסדי הישיר בין האסטרונום המלכותי לשאלת הלגיטימציה השלטונית ("מנדט השמיים") היה הדוק ומכריע במיוחד. בעוד הבבלים הצטיינו בניבוי ליקויים בזכות סדרתיות התצפיות, והיוונים במודלים גיאומטריים, לסינים הייתה מערכת ממשלתית ממוסדת שתמכה באסטרונומיה כמדע מדינה מרכזי.</p>
</div>

<script>
    const simulationApp = document.getElementById('simulation-app');
    const scenarioArea = document.getElementById('scenario-area');
    const scenarioTextElem = document.getElementById('scenario-text');
    const optionsContainerElem = document.getElementById('options-container');
    const resultTextElem = document.getElementById('result-text');
    const explanationElem = document.getElementById('explanation');
    const toggleExplanationBtn = document.getElementById('toggle-explanation');

    let currentScenarioIndex = 0;
    let survived = true;

    const scenarios = [
        {
            text: "השנה היא XXXX, ורוחות רעות מנשבות בחצר. הקיסר זימן אתכם בחופזה. 'השמש נראתה חיוורת באופן מטריד הבוקר,' הוא אומר בקול רועם. 'יועציי לוחשים על ליקוי חמה בלתי צפוי. האם חישוביכם ניבאו זאת?'",
            options: [
                { text: "כן, אדוני הקיסר! אכן צפינו ליקוי חמה חלקי שיגיע מחר בשעה X. אין סיבה לדאגה, הכול תחת שליטתנו.", outcome: { type: 'success', text: "הקיסר מחייך בהקלה. 'מצוין! נאמנותכם ויכולותיכם מוכיחות שהשמיים עמנו.' מעמדכם בחצר מתחזק!" } },
                { text: "לא, אדוני הקיסר. תצפיותינו וחישובינו אינם מראים סימן לליקוי קרוב. ייתכן שזו רק עננות סמיכה או אבק באוויר ממרחקים?", outcome: { type: 'danger', text: "כישלון מחפיר! ליקוי חמה בלתי צפוי הוא אות מבשר רעות, אי-שביעות רצון שמימית! הקיסר זועם על חוסר יכולתכם. 'האם אתם מערערים את מנדט השמיים שלי?' הוא שואל. סופכם נחרץ." } },
                { text: "אדוני הקיסר, עננות כבדה בימים האחרונים הפריעה לתצפיות מדויקות. אנו בודקים בדקדקנות את חישובינו הקודמים ומצפים לשמיים בהירים יותר לאימות...", outcome: { type: 'warning', text: "הקיסר בוחן אתכם בעיניו החודרות. 'אל תאכזבו אותי בשנית,' הוא מזהיר בקור רוח. הלחץ עליכם עצום." } }
            ]
        },
        {
            text: "שרדתם, הפעם. אך השמיים ממשיכים להיות פעילים. מגיעה תצפית יוצאת דופן: כוכב 'אורח' בהיר להפליא הופיע לפתע בשמיים, במקום בו לא היה קודם. היועצים לוחשים על סימני אסון. מה תגידו לקיסר על הכוכב החדש?",
            options: [
                { text: "זהו 'כוכב אורח מבורך'! סימן רב עוצמה להתחלה חדשה וטובה, המבשר על תקופה של שגשוג ושלטון איתן לקיסר!", outcome: { type: 'success', text: "הקיסר ואנשיו נושמים לרווחה. פרשנותכם האופטימית מחזקת את מעמדו. (זהו כנראה רישום של סופרנובה היסטורית!)" } },
                { text: "אדוני, זהו כנראה כוכב שביט - 'כוכב מטאטא' קוסמי, סימן לשינויים גדולים. עלינו לפרש בקפידה את משמעותו האפשרית על ענייני המדינה ולנהוג בזהירות.", outcome: { type: 'warning', text: "הקיסר מודאג מהמושג 'שינויים'. 'האם גורלנו בסכנה?' הוא שואל בחרדה. עליכם להסביר את עצמכם טוב יותר בפני החצר כולה." } },
                { text: "זהו כוכב שביט זועם! הוא מופיע כמבשר רעות, סימן ודאי לאסון קוסמי או ארצי המתקרב!", outcome: { type: 'danger', text: "פסימיות והפצת פחד אינן מתקבלות בחצר הקיסר! אתם מואשמים בניסיון לערער את היציבות ולהחליש את הקיסר. 'הסירו אותו מנגד עיני!' זועק הקיסר. גורלכם נחרץ." } }
            ]
        },
         {
            text: "הלחץ סביבכם מתמיד. כעת, תלונות מגיעות מהשטח: החקלאים מתעקשים שהלוח הקיסרי אינו תואם את עונות השנה כראוי - האביב הגיע מוקדם מדי ביחס לתאריך הרשמי. האם הלוח השתבש? מהי המלצתכם לקיסר?",
            options: [
                { text: "יש הכרח לבצע תיקון בלוח השנה הקיסרי על ידי הוספת חודש מעובר, כפי שמחייבים חישובינו וכדי להתאים לסדר הקוסמי והארצי.", outcome: { type: 'success', text: "הקיסר מקבל את המלצתכם האמיצה. הלוח מתוקן בעזרת חישובים מדויקים, החקלאים רגועים, והסדר הטבעי והמדיני הושב על כנו. הצלחתם לשמור על האיזון!" } },
                { text: "ייתכן שטעויות אנוש בחישובים קודמים הצטברו וגרמו לפער. עלינו לבצע מדידות ותצפיות מדויקות מחדש ולעדכן את הלוח בהתאם.", outcome: { type: 'warning', text: "הקיסר מודאג מהרעיון של טעויות במשרדכם. 'ודאו שדבר כזה לא יקרה שוב, חיי האימפריה תלויים בלוח!' הוא פוקד. האחריות על תיקון הלוח נופלת עליכם." } },
                { text: "אין צורך לשנות דבר. הלוח הקיסרי מדויק ומושלם כפי שנקבע. החקלאים טועים בתחושותיהם, או שזוהי שנה חריגה שאינה דורשת התאמה.", outcome: { type: 'danger', text: "התעלמות מקשיי העם והתעקשות על טעות בחישוב היא מתכון לאסון! המרירות בשטח גוברת, והקיסר רואה בכם סמל לניתוק וחוסר יכולת. 'אתם מביאים אסון על האימפריה!' הוא מאשים. סופכם קרב." } }
            ]
        },
         {
            text: "ניווטתם בהצלחה בין המזימות, הסכנות והאתגרים הקוסמיים! נבואותיכם היו מדויקות, פרשנויותיכם היטיבו עם הקיסר, והלוח הקיסרי נותר סמל לסדר ויציבות. אתם זוכים לכבוד רב, לאוצרות, ולמעמד נכבד בחצר הקיסר. ברכותיכם, שר האסטרונומיה המהולל!",
            options: [
                { text: "שחקו שוב: נסו לשרוד בחצר הקיסר!", outcome: { type: 'info', text: "התחלה מחדש..." } }
            ]
        }
    ];

    function startSimulation() {
        currentScenarioIndex = 0;
        survived = true;
        // Hide start button, clear results, and start game flow
        const startButton = scenarioTextElem.querySelector('.start-button');
        if (startButton) startButton.style.display = 'none'; // Hide the specific button

        resultTextElem.innerHTML = '';
        resultTextElem.className = 'result-block'; // Reset classes

        // Initial display
        displayScenario(currentScenarioIndex);
    }

    function displayScenario(index) {
        if (index >= scenarios.length || !survived && index < scenarios.length -1) {
             endSimulation(!survived);
             return;
        }

        const scenario = scenarios[index];

        // Animate out current content
        scenarioTextElem.classList.add('fade-out');
        optionsContainerElem.classList.add('fade-out');
        resultTextElem.classList.add('fade-out'); // Also fade out previous result if any

        // Wait for animation to complete before changing content
        setTimeout(() => {
            scenarioTextElem.innerHTML = `<p>${scenario.text}</p>`;
            optionsContainerElem.innerHTML = ''; // Clear previous options
            resultTextElem.innerHTML = ''; // Clear result text for the new scenario

            // If it's the final success scenario (index 3)
            if (index === scenarios.length - 1) {
                 const restartButton = document.createElement('button');
                 restartButton.textContent = scenario.options[0].text; // "שחקו שוב..."
                 restartButton.classList.add('scenario-option'); // Use option button style
                 restartButton.onclick = startSimulation;
                 optionsContainerElem.appendChild(restartButton);
                  resultTextElem.className = `result-block ${scenario.options[0].outcome.type}`; // Apply info class
             } else {
                 // Not final scenario, display regular options
                 scenario.options.forEach((option, optionIndex) => {
                     const button = document.createElement('button');
                     button.textContent = option.text;
                     button.classList.add('scenario-option');
                     button.onclick = () => handleChoice(optionIndex);
                     optionsContainerElem.appendChild(button);
                 });
             }


            // Animate in new content
            scenarioTextElem.classList.remove('fade-out');
            scenarioTextElem.classList.add('fade-in');
            optionsContainerElem.classList.remove('fade-out');
            optionsContainerElem.classList.add('fade-in');

            // Fade in result block only when a result is shown after handleChoice
            resultTextElem.classList.remove('fade-in', 'fade-out'); // Ensure no lingering animation classes


             // Reset fade-out after animation completes for next turn
             setTimeout(() => {
                scenarioTextElem.classList.remove('fade-in');
                optionsContainerElem.classList.remove('fade-in');
             }, 600); // Match the transition duration

        }, 600); // Wait duration matches fade-out transition
    }

    function handleChoice(choiceIndex) {
        const scenario = scenarios[currentScenarioIndex];
        const chosenOption = scenario.options[choiceIndex];
        const outcome = chosenOption.outcome;

        // Hide options immediately or fade them out quickly
        optionsContainerElem.classList.add('fade-out');


        // Display result with animation
        resultTextElem.innerHTML = `<p>${outcome.text}</p>`;
        resultTextElem.className = `result-block ${outcome.type}`; // Add outcome class
        // Trigger fade-in animation for result
        requestAnimationFrame(() => { // Use rAF to ensure class removal/addition triggers reflow/repaint
             resultTextElem.classList.remove('fade-out');
             resultTextElem.classList.add('fade-in');
             resultTextElem.style.transform = 'translateY(0)'; // Ensure translateY is reset for fade-in
        });


        if (outcome.type === 'danger') {
            survived = false;
        }

        currentScenarioIndex++;

        // Wait a bit for the user to read the result, then move to the next scenario or end
        setTimeout(() => {
             resultTextElem.classList.remove('fade-in'); // Prepare result for next fade-out/clear
            displayScenario(currentScenarioIndex);
        }, 2500); // Increased delay for reading
    }

    function endSimulation(failed) {
        // Clear options and result area completely
        optionsContainerElem.innerHTML = '';
        optionsContainerElem.className = 'options-block'; // Reset classes
        resultTextElem.innerHTML = '';
        resultTextElem.className = 'result-block'; // Reset classes


        scenarioTextElem.classList.add('fade-out');

        setTimeout(() => {
             if (failed) {
                 scenarioTextElem.innerHTML = "<p>הסימולציה הסתיימה בכישלון... כפי שחששתם, תפקיד האסטרונום המלכותי היה כרוך בסכנות פוליטיות וקוסמיות ממשיות. גורלכם נחרץ על פי הכוכבים (או חוסר היכולת לנבא אותם).</p>";
                  scenarioTextElem.className = 'text-block danger'; // Style failure message as danger

                 const restartButton = document.createElement('button');
                 restartButton.textContent = "נסו שוב להציל את ראשכם!";
                 restartButton.classList.add('scenario-option', 'start-button'); // Use button style
                 restartButton.onclick = startSimulation;
                 optionsContainerElem.appendChild(restartButton); // Add restart button to options area
                 optionsContainerElem.classList.remove('fade-out');
                 optionsContainerElem.classList.add('fade-in'); // Fade in restart button

             } else {
                  // This case should theoretically be handled by displayScenario showing the last index
                  // but add a fallback just in case, though the main flow should not hit this else
                  scenarioTextElem.innerHTML = "<p>סוף הסימולציה.</p>";
                  scenarioTextElem.className = 'text-block info';
             }
             scenarioTextElem.classList.remove('fade-out');
             scenarioTextElem.classList.add('fade-in');

             setTimeout(() => {
                  scenarioTextElem.classList.remove('fade-in');
                  optionsContainerElem.classList.remove('fade-in');
              }, 600); // Clean up classes


        }, 600); // Wait duration
    }

    // Explanation Toggle
    toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationElem.style.display === 'none';
        explanationElem.style.display = isHidden ? 'block' : 'none';
        toggleExplanationBtn.textContent = isHidden ? 'הסתר רקע היסטורי' : 'הצג/הסתר רקע היסטורי';
        // Optional: add a simple fade effect using opacity
        explanationElem.style.opacity = isHidden ? '0' : '1';
         if(isHidden) {
              setTimeout(() => explanationElem.style.opacity = '1', 10); // Small delay to trigger transition
         } else {
              explanationElem.style.opacity = '0';
         }
    });


    // Initial state: Ensure only the intro text and start button are visible
    // All other elements (options, result) are managed by the JS flow
    window.onload = () => {
        optionsContainerElem.innerHTML = ''; // Ensure options are empty initially
        resultTextElem.innerHTML = ''; // Ensure result is empty initially
        resultTextElem.className = 'result-block'; // Reset classes
        scenarioTextElem.classList.remove('fade-out', 'fade-in'); // Clean classes on load
        optionsContainerElem.classList.remove('fade-out', 'fade-in');
         resultTextElem.classList.remove('fade-out', 'fade-in');

         // The start button is in the initial HTML, so no need to add it via JS here.
         // The initial scenario text is also in the HTML.
         // The JS `startSimulation` will manage clearing/adding these.

         // Ensure explanation is hidden initially via JS in case CSS display:none is overridden
         explanationElem.style.display = 'none';
         explanationElem.style.opacity = '0'; // Also set initial opacity for transition
    };


</script>