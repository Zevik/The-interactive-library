---
title: "סימולציית חברת תרופות: המסע מהמעבדה לשוק"
english_slug: pharma-company-simulation-lab-to-market
category: "ניהול ועסקים / ניהול"
tags:
  - תעשיית התרופות
  - ניהול עסקי
  - מו"פ
  - שיווק תרופות
  - כלכלה עסקית
---
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>סימולציית חברת תרופות</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700&display=swap');

        body {
            font-family: 'Heebo', sans-serif;
            line-height: 1.7;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #e0f7fa 0%, #b3e5fc 100%);
            color: #333;
            display: flex;
            justify-content: center;
            align-items: flex-start;
            min-height: 100vh;
        }
        .container {
            max-width: 900px;
            width: 100%;
            margin: auto;
            background: #ffffff;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }
        h1, h2 {
            color: #0277bd; /* Deep Sky Blue */
            text-align: center;
            margin-bottom: 20px;
            font-weight: 700;
        }
         h1 {
             font-size: 2.2rem;
         }
         h2 {
             font-size: 1.6rem;
             margin-top: 25px;
             border-bottom: 2px solid #e0f7fa;
             padding-bottom: 10px;
         }
        p {
            margin-bottom: 15px;
            font-size: 1.1rem;
        }

        .simulation-area {
            border: 1px solid #b3e5fc; /* Light blue border */
            padding: 25px;
            margin-top: 30px;
            border-radius: 8px;
            background-color: #f1f8e9; /* Light green background */
            box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease-in-out;
        }
         .simulation-area.processing {
             background-color: #fff9c4; /* Light yellow */
             border-color: #fbc02d; /* Yellow */
             animation: pulse 1.5s infinite alternate;
         }

        @keyframes pulse {
            from { box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.05); }
            to { box-shadow: inset 0 0 15px rgba(251, 192, 45, 0.3); }
        }

        .status-panel {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
            margin-bottom: 20px;
            padding: 15px;
            background-color: #e1f5fe; /* Extra light blue */
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }
        .status-item {
            font-weight: 500;
            color: #01579b; /* Darker blue */
            font-size: 1rem;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            padding: 8px;
            border: 1px solid #b3e5fc;
            border-radius: 5px;
            background-color: #ffffff;
        }
        .status-item span {
            font-weight: 700;
            color: #00796b; /* Teal */
            margin-top: 4px;
            font-size: 1.1rem;
             transition: color 0.3s ease;
        }
         .cash-gain span { color: #388e3c !important; } /* Green */
         .cash-loss span { color: #d32f2f !important; } /* Red */
         .reputation-gain span { color: #388e3c !important; } /* Green */
         .reputation-loss span { color: #d32f2f !important; } /* Red */


        .action-panel {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 10px;
            margin-bottom: 20px;
        }
        .action-panel button {
            flex-grow: 1;
            min-width: 150px;
            padding: 12px 20px;
            background-color: #03a9f4; /* Light Blue */
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1.1rem;
            font-weight: 500;
            transition: background-color 0.3s ease, transform 0.1s ease;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .action-panel button:hover:not(:disabled) {
            background-color: #0288d1; /* Darker Light Blue */
            transform: translateY(-2px);
        }
         .action-panel button:active:not(:disabled) {
            transform: translateY(0);
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
         }
         .action-panel button:disabled {
            background-color: #bdbdbd; /* Grey */
            cursor: not-allowed;
            box-shadow: none;
            transform: none;
            opacity: 0.7;
        }

        .output-log {
            margin-top: 20px;
            padding: 15px;
            border: 1px solid #b2dfdb; /* Light teal */
            background-color: #e0f2f7; /* Extra light cyan */
            max-height: 250px;
            overflow-y: auto;
            border-radius: 8px;
            box-shadow: inset 0 0 8px rgba(0,0,0,0.05);
            font-size: 0.95rem;
        }
        .output-log div {
            margin-bottom: 10px;
            padding-bottom: 8px;
            border-bottom: 1px dashed #b2dfdb;
            opacity: 0; /* Start hidden for animation */
            transform: translateY(20px); /* Start below for animation */
            animation: logEntryFadeIn 0.5s ease forwards; /* Animation */
        }
        .output-log div:last-child {
            border-bottom: none;
            animation-delay: 0s !important; /* Ensure the latest is fastest */
        }
         /* Apply animation delay to previous entries */
        .output-log div:not(:last-child) {
             animation-delay: 0.1s; /* Stagger effect */
        }

        @keyframes logEntryFadeIn {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .explanation-toggle {
            display: block;
            width: fit-content;
            margin: 30px auto;
            padding: 12px 25px;
            background-color: #4caf50; /* Green */
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1.1rem;
            font-weight: 500;
            transition: background-color 0.3s ease, transform 0.1s ease;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .explanation-toggle:hover {
            background-color: #388e3c; /* Darker green */
            transform: translateY(-2px);
        }
         .explanation-toggle:active {
             transform: translateY(0);
             box-shadow: 0 1px 3px rgba(0,0,0,0.1);
         }

        .explanation-content {
            display: none;
            margin-top: 20px;
            padding: 20px;
            border: 1px solid #cfd8dc; /* Light grey blue */
            border-radius: 8px;
            background-color: #eceff1; /* Extra light grey blue */
            line-height: 1.8;
            font-size: 1rem;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
             animation: fadeIn 0.5s ease-out;
        }

        @keyframes fadeIn {
             from { opacity: 0; transform: translateY(10px); }
             to { opacity: 1; transform: translateY(0); }
        }

        .explanation-content h2 {
            text-align: right;
            color: #0277bd;
            margin-top: 15px;
            margin-bottom: 10px;
            border-bottom: none;
            padding-bottom: 0;
        }
         .explanation-content h3 {
             color: #00796b;
             margin-top: 15px;
             margin-bottom: 8px;
             font-size: 1.2rem;
             font-weight: 700;
         }
         .explanation-content ul {
            list-style-type: disc;
            padding-right: 20px;
            margin-bottom: 15px;
        }
         .explanation-content li {
            margin-bottom: 10px;
         }
         .explanation-content strong {
             font-weight: 700;
             color: #01579b;
         }

         .game-message {
             text-align: center;
             font-size: 1.5rem;
             font-weight: 700;
             margin-top: 20px;
             padding: 15px;
             border-radius: 8px;
         }
         .game-message.win {
             color: #1b5e20; /* Dark green */
             background-color: #e8f5e9; /* Extra light green */
             border: 2px solid #4caf50;
         }
         .game-message.lose {
             color: #b71c1c; /* Dark red */
             background-color: #ffebee; /* Extra light red */
             border: 2px solid #f44336;
         }

         /* Progress bar for simulation stages */
         .progress-bar-container {
             width: 100%;
             background-color: #e0e0e0;
             border-radius: 5px;
             margin-top: 15px;
             overflow: hidden;
             display: none; /* Hidden by default */
         }
         .progress-bar {
             height: 20px;
             width: 0%;
             background-color: #03a9f4;
             text-align: center;
             line-height: 20px;
             color: white;
             font-size: 0.9rem;
             transition: width 0.4s ease-in-out;
         }
          .simulation-area.processing .progress-bar-container {
              display: block; /* Show when processing */
          }


    </style>
</head>
<body>
    <div class="container">
        <h1>סימולציית חברת תרופות: המסע מהמעבדה לשוק</h1>
        <p>ברוכים הבאים לעולם המאתגר של תעשיית התרופות! אתם עומדים בראש חברת ביוטק חדשה עם הון ראשוני וחלום גדול: לגלות, לפתח ולהשיק תרופה שתשנה חיים. הדרך ארוכה ומפותלת, רצופה בהשקעות ענק, סיכונים מדעיים ורגולטוריים, ותחרות עזה. האם יש לכם את מה שנדרש כדי לנווט את החברה שלכם להצלחה?</p>
        <p>כל החלטה שתקבלו תעלה לכם כסף, תשפיע על המוניטין שלכם ותקדם (או תעצור) את התרופה שלכם בצנרת הפיתוח. הצליחו לאשר מספיק תרופות לפני שהכסף נגמר!</p>

        <div class="simulation-area" id="simulation-area">
            <h2>הסימולציה בפעולה</h2>
            <div class="status-panel">
                <div class="status-item" id="cash-status">מזומנים: <span id="cash">100,000,000</span>₪</div>
                <div class="status-item" id="reputation-status">מוניטין: <span id="reputation">50</span></div>
                <div class="status-item">תרופות מאושרות: <span id="approved-drugs">0</span></div>
                <div class="status-item">תרופה בפיתוח: <span id="drug-in-pipeline">אין</span></div>
                 <div class="status-item">שלב נוכחי: <span id="current-stage">התחלה</span></div>
            </div>

            <div class="progress-bar-container">
                 <div class="progress-bar" id="progress-bar"></div>
            </div>

            <div class="action-panel">
                <button id="start-rnd">התחל מחקר ופיתוח (10M₪)</button>
                 <button id="start-clinical-1" disabled>ניסוי קליני שלב I (20M₪)</button>
                 <button id="start-clinical-2" disabled>ניסוי קליני שלב II (50M₪)</button>
                 <button id="start-clinical-3" disabled>ניסוי קליני שלב III (100M₪)</button>
                 <button id="submit-regulation" disabled>הגש לאישור רגולטורי (5M₪)</button>
                 <button id="launch-marketing" disabled>השק לשוק (שיווק) (30M₪)</button>
            </div>

            <div class="output-log" id="log">
                <div>ברוכים הבאים למסע מרתק בעולם הפארמה! המטרה: לפתח תרופות מצילות חיים ולהצליח כלכלית. יש לכם 100 מיליון ₪ להתחלה. בהצלחה!</div>
            </div>

             <div class="game-message" id="game-message" style="display: none;"></div>
        </div>

        <button class="explanation-toggle" id="toggle-explanation">הצג הסבר על עולם תעשיית התרופות</button>

        <div class="explanation-content" id="explanation">
            <h2>הסבר: עולם תעשיית התרופות - מבט מעמיק</h2>
            <p>תעשיית התרופות היא אחת התעשיות המורכבות, המסוכנות (מבחינה פיננסית) והמשפיעות ביותר בעולם. היא דורשת שילוב נדיר של מדע פורץ דרך, ניהול סיכונים קפדני, הבנה רגולטורית עמוקה ויכולות שיווק אסטרטגיות. הסימולציה שבה שיחקתם היא מודל פשטני מאוד, אך היא נועדה להמחיש את האתגרים וההחלטות המרכזיות לאורך חיי פרויקט פיתוח תרופה.</p>

            <h3>שלבי המסע של תרופה חדשה:</h3>
            <ul>
                <li>
                    <strong>גילוי ומחקר ראשוני (Discovery & Preclinical):</strong> זהו שלב החיפוש אחר מולקולות פוטנציאליות לטיפול במחלה מסוימת. הוא כולל הבנת מנגנוני המחלה, זיהוי מטרות ביולוגיות רלוונטיות, וסינתזה או גילוי של תרכובות כימיות או ביולוגיות שיכולות להשפיע על אותן מטרות. לאחר מכן, מתבצעות בדיקות מעבדה ובדיקות ראשוניות על בעלי חיים (מחקר פרה-קליני) כדי לבחון בטיחות ויעילות ראשונית לפני המעבר לניסויים בבני אדם. זהו שלב יקר מאוד ועם שיעורי הצלחה נמוכים.
                </li>
                <li>
                    <strong>ניסויים קליניים (Clinical Trials) - על בני אדם:</strong> אם התרופה הפוטנציאלית עוברת את השלב הפרה-קליני בהצלחה, היא יכולה להתקדם לניסויים קליניים, המחולקים לשלבים:
                    <ul>
                        <li><strong>שלב I:</strong> מתמקד בעיקר בבטיחות. מעורבים בו קבוצה קטנה של מתנדבים בריאים (או לעיתים חולים במחלה קשה) כדי לבדוק את טווח המינון הבטוח, דרכי הספיגה והפינוי של התרופה בגוף. שיעור הכישלון בשלב זה גבוה יחסית, בעיקר מסיבות בטיחות.</li>
                        <li><strong>שלב II:</strong> בודק יעילות ראשונית ובטיחות בקבוצה גדולה יותר של חולים במחלה המיועדת. מטרתו למצוא את המינון האופטימלי ולהעריך האם יש סימן כלשהו שהתרופה אכן עובדת. זהו שלב קריטי ויקר, ושיעור הכישלון בו גבוה מאוד.</li>
                        <li><strong>שלב III:</strong> השלב הגדול והיקר ביותר. מעורבים בו מאות או אלפי חולים, לעיתים במרכזים רפואיים רבים ברחבי העולם. מטרתו להוכיח באופן חד משמעי את יעילות ובטיחות התרופה בהשוואה לפלצבו (תרופת דמה) או לתרופות קיימות. כישלון בשלב III הוא מכה אנושה לחברה.</li>
                    </ul>
                </li>
                <li>
                    <strong>הגשה לאישור רגולטורי (Regulatory Submission):</strong> אם התרופה צולחת את כל שלבי הניסויים הקליניים, החברה אוספת את כל המידע שנצבר ומגישה אותו לרשויות הרגולציה במדינות השונות (כמו ה-FDA בארה"ב, ה-EMA באירופה, או משרד הבריאות בישראל). הרשויות בוחנות בקפידה את הנתונים כדי לוודא שהתרופה בטוחה ויעילה לשימוש בציבור. תהליך הבדיקה ארוך ויסודי.
                </li>
                <li>
                    <strong>אישור והשקה מסחרית (Approval & Commercialization):</strong> לאחר קבלת האישור הרגולטורי, החברה יכולה להשיק את התרופה לשוק. שלב זה דורש השקעות ענק בשיווק, מכירות, ייצור והפצה. ההצלחה המסחרית תלויה בגורמים רבים, כולל התחרות בשוק, נגישות (הכללה בסל התרופות), ואסטרטגיית המחיר והשיווק.
                </li>
            </ul>

            <h3>האתגרים הגדולים:</h3>
            <ul>
                <li><strong>סיכון וכישלון:</strong> רוב מוחלט של הפרויקטים נכשלים בשלבים שונים, בעיקר בשלבים הקליניים. פיתוח תרופה אחת שלוקח 10-15 שנה עולה בממוצע מעל מיליארד דולר (כולל עלויות הכישלונות).</li>
                <li><strong>רגולציה מחמירה:</strong> דרישות הרשויות גבוהות ומשתנות, ותהליך האישור ארוך ויקר.</li>
                <li><strong>השקעות ענק:</strong> כל שלב דורש מימון משמעותי. חברות נדרשות לגייס הון רב שוב ושוב.</li>
                <li><strong>תחרות:</strong> חברות רבות מתחרות על פיתוח תרופות לאותן מחלות.</li>
                <li><strong>מודלים עסקיים:</strong> ההכנסות מגיעות רק שנים רבות לאחר תחילת ההשקעה, ותקופת הפטנט המגנה על הבלעדיות מוגבלת בזמן.</li>
            </ul>
            <p>כפי שראיתם בסימולציה, ניהול חברת תרופות הוא איזון עדין בין נטילת סיכונים מחושבים, ניהול פיננסי קפדני והתמדה מדעית. הצלחה בשוק זה יכולה להניב רווחים עצומים ולא פחות חשוב - להשפיע לטובה על בריאות מיליוני אנשים ברחבי העולם.</p>
        </div>
    </div>

    <script>
        const cashElement = document.getElementById('cash');
        const reputationElement = document.getElementById('reputation');
        const approvedDrugsElement = document.getElementById('approved-drugs');
        const drugInPipelineElement = document.getElementById('drug-in-pipeline');
        const currentStageElement = document.getElementById('current-stage');
        const logElement = document.getElementById('log');
        const simulationArea = document.getElementById('simulation-area');
        const progressBarContainer = document.getElementById('progress-bar-container');
        const progressBar = document.getElementById('progress-bar');
        const gameMessageElement = document.getElementById('game-message');

        const startRndButton = document.getElementById('start-rnd');
        const startClinical1Button = document.getElementById('start-clinical-1');
        const startClinical2Button = document.getElementById('start-clinical-2');
        const startClinical3Button = document.getElementById('start-clinical-3');
        const submitRegulationButton = document.getElementById('submit-regulation');
        const launchMarketingButton = document.getElementById('launch-marketing');

        const explanationToggle = document.getElementById('toggle-explanation');
        const explanationContent = document.getElementById('explanation');

        let gameState = {
            cash: 100000000, // Start with 100M
            reputation: 50, // 0-100
            approvedDrugs: 0,
            drugInPipeline: null, // null, 'R&D', 'Clinical I', 'Clinical II', 'Clinical III', 'Regulation', 'Approved', 'Failed'
            currentStage: 'התחלה',
            rndCost: 10000000, // 10M
            clinicalCost1: 20000000, // 20M
            clinicalCost2: 50000000, // 50M
            clinicalCost3: 100000000, // 100M
            regulationCost: 5000000, // 5M
            marketingCost: 30000000, // 30M
            rndSuccessRate: 0.3, // 30% chance
            clinicalSuccessRate1: 0.6, // 60% chance
            clinicalSuccessRate2: 0.5, // 50% chance
            clinicalSuccessRate3: 0.7, // 70% chance
            regulationApprovalRate: 0.8, // 80% chance
            revenuePerDrugPerCycle: 50000000, // 50M revenue per approved drug per 'cycle' (simplified)
            isProcessing: false,
            cycles: 0 // Track cycles for revenue
        };

        const stageDurations = {
            'R&D': 2000,
            'Clinical I': 3000,
            'Clinical II': 4000,
            'Clinical III': 5000,
            'Regulation': 4000
        };

        function updateUI() {
            // Animate cash/reputation changes
            animateValueChange(cashElement, gameState.cash);
            animateValueChange(reputationElement, gameState.reputation);

            approvedDrugsElement.textContent = gameState.approvedDrugs;
            drugInPipelineElement.textContent = getPipelineStatusText(gameState.drugInPipeline);
            currentStageElement.textContent = gameState.currentStage;

            // Disable all buttons initially if processing or game over
            const allButtons = [startRndButton, startClinical1Button, startClinical2Button, startClinical3Button, submitRegulationButton, launchMarketingButton];
            allButtons.forEach(button => button.disabled = true);

            if (gameState.isProcessing) {
                simulationArea.classList.add('processing');
                progressBarContainer.style.display = 'block';
            } else {
                simulationArea.classList.remove('processing');
                progressBarContainer.style.display = 'none';
                progressBar.style.width = '0%'; // Reset progress bar
                 progressBar.textContent = '';

                 if (gameState.cash <= 0) {
                     endGame(false); // Lose
                 } else if (gameState.approvedDrugs >= 3) { // Win condition: Approve 3 drugs
                     endGame(true); // Win
                 } else {
                    // Enable buttons based on current stage and funds
                    switch (gameState.drugInPipeline) {
                        case null:
                            startRndButton.disabled = gameState.cash < gameState.rndCost;
                            break;
                        case 'Clinical I':
                            startClinical1Button.disabled = gameState.cash < gameState.clinicalCost1;
                            break;
                        case 'Clinical II':
                            startClinical2Button.disabled = gameState.cash < gameState.clinicalCost2;
                            break;
                        case 'Clinical III':
                            startClinical3Button.disabled = gameState.cash < gameState.clinicalCost3;
                            break;
                         case 'Regulation':
                            submitRegulationButton.disabled = gameState.cash < gameState.regulationCost;
                            break;
                         case 'Approved':
                            launchMarketingButton.disabled = gameState.cash < gameState.marketingCost;
                            break;
                        case 'Failed': // If drug failed, allow starting new R&D
                            gameState.drugInPipeline = null;
                            gameState.currentStage = 'התחלה';
                            startRndButton.disabled = gameState.cash < gameState.rndCost;
                            break;
                    }
                    // Always allow R&D if pipeline is empty and have cash
                     if (gameState.drugInPipeline === null) {
                         startRndButton.disabled = gameState.cash < gameState.rndCost;
                     }
                 }
            }
        }

        function getPipelineStatusText(status) {
            switch (status) {
                case 'R&D': return 'במחקר ופיתוח';
                case 'Clinical I': return 'מוכן לניסוי קליני I';
                case 'Clinical II': return 'מוכן לניסוי קליני II';
                case 'Clinical III': return 'מוכן לניסוי קליני III';
                case 'Regulation': return 'מוכן להגשה רגולטורית';
                case 'Approved': return 'מוכן להשקה מסחרית';
                case 'Failed': return 'התרופה נכשלה';
                default: return 'אין';
            }
        }

        function logEvent(message, isImportant = false) {
            const entry = document.createElement('div');
            entry.textContent = message;
            if (isImportant) {
                entry.style.fontWeight = 'bold';
                 entry.style.color = '#01579b';
            }
            logElement.prepend(entry); // Add to the top

            // Apply animation delay progressively
            const logEntries = logElement.children;
            for(let i = 0; i < logEntries.length; i++) {
                logEntries[i].style.animationDelay = `${i * 0.1}s`;
            }

             // Clean up old entries if log gets too long
             while (logElement.children.length > 50) {
                 logElement.removeChild(logElement.lastChild);
             }
        }

        function handleFailure(stage) {
            const failureMessages = {
                'מחקר ופיתוח': 'פרויקט המחקר והפיתוח נכשל. המולקולה אינה מבטיחה.',
                'ניסוי קליני שלב I': 'ניסוי קליני שלב I נכשל בשל בעיות בטיחות בלתי צפויות.',
                'ניסוי קליני שלב II': 'ניסוי קליני שלב II לא הדגים יעילות מספקת בחולים.',
                'ניסוי קליני שלב III': 'ניסוי קליני שלב III נכשל בהוכחת יעילות ובטיחות מובהקת.',
                'בדיקה רגולטורית': 'הבקשה הרגולטורית נדחתה. נדרשים נתונים נוספים או שהפרויקט נכשל סופית.'
            };
            logEvent(`טרגדיה! ${failureMessages[stage] || `כישלון בשלב ${stage}.`}`, true);
            gameState.drugInPipeline = 'Failed';
            gameState.currentStage = 'כישלון';
            changeReputation(-10); // Lose significant reputation on failure
        }

        function changeCash(amount) {
            const cashStatusElement = document.getElementById('cash-status');
            const oldCash = gameState.cash;
            gameState.cash += amount;
            const newCash = gameState.cash;

            // Add class for visual feedback
            if (amount > 0) {
                cashStatusElement.classList.add('cash-gain');
            } else if (amount < 0) {
                cashStatusElement.classList.add('cash-loss');
            }

            // Remove class after animation (or a short delay)
            setTimeout(() => {
                cashStatusElement.classList.remove('cash-gain', 'cash-loss');
            }, 500); // Adjust delay as needed for CSS transition

            // Animate the number change (handled by updateUI calling animateValueChange)
        }

        function changeReputation(amount) {
             const reputationStatusElement = document.getElementById('reputation-status');
             const oldReputation = gameState.reputation;
             gameState.reputation = Math.max(0, Math.min(100, gameState.reputation + amount)); // Keep reputation between 0-100
             const newReputation = gameState.reputation;

             // Add class for visual feedback
             if (amount > 0) {
                 reputationStatusElement.classList.add('reputation-gain');
             } else if (amount < 0) {
                 reputationStatusElement.classList.add('reputation-loss');
             }

             // Remove class after animation
            setTimeout(() => {
                reputationStatusElement.classList.remove('reputation-gain', 'reputation-loss');
            }, 500); // Adjust delay

             // Animate the number change (handled by updateUI calling animateValueChange)
        }

        function animateValueChange(element, newValue) {
             const span = element.querySelector('span');
             const currentValue = parseFloat(span.textContent.replace(/[^0-9.-]+/g,"")); // Extract number, handle commas/₪
             const diff = newValue - currentValue;
             const duration = 500; // milliseconds
             const start = performance.now();

             function step(timestamp) {
                 const elapsed = timestamp - start;
                 const progress = Math.min(elapsed / duration, 1);
                 const easedProgress = progress < 0.5 ? 2 * progress * progress : -1 + (4 - 2 * progress) * progress; // Ease-in-out

                 const animatedValue = currentValue + diff * easedProgress;

                 if (element === cashElement) {
                      span.textContent = Math.round(animatedValue).toLocaleString() + '₪';
                 } else if (element === reputationElement) {
                      span.textContent = Math.round(animatedValue);
                 }


                 if (progress < 1) {
                     requestAnimationFrame(step);
                 } else {
                     // Ensure final value is exact
                      if (element === cashElement) {
                          span.textContent = Math.round(newValue).toLocaleString() + '₪';
                     } else if (element === reputationElement) {
                          span.textContent = Math.round(newValue);
                     }
                 }
             }

             requestAnimationFrame(step);
        }


        function runSimulationStage(stage, cost, successRate, reputationChangeSuccess, reputationChangeFailure, nextPipelineState, successMessage, failureMessage) {
            if (gameState.isProcessing) return;
            if (gameState.cash < cost) {
                logEvent('אין מספיק מזומנים לפעולה זו.');
                return;
            }

            changeCash(-cost);
            gameState.isProcessing = true;
            gameState.currentStage = `בביצוע: ${stage}`;
            logEvent(`התחלת שלב: ${stage}. עלות: ${cost.toLocaleString()}₪.`);
            updateUI();

            const duration = stageDurations[stage] || 3000; // Default duration
            let progress = 0;
            const interval = setInterval(() => {
                progress += (100 / (duration / 100)); // Increment based on duration
                if (progress > 100) progress = 100;
                progressBar.style.width = progress + '%';
                progressBar.textContent = `${Math.round(progress)}%`;
            }, 100); // Update progress every 100ms


            setTimeout(() => {
                 clearInterval(interval);
                 progressBar.style.width = '100%'; // Ensure it reaches 100%
                 progressBar.textContent = '100%';

                const success = Math.random() < successRate;
                gameState.isProcessing = false;

                if (success) {
                    logEvent(successMessage, true);
                    gameState.drugInPipeline = nextPipelineState;
                    gameState.currentStage = getPipelineStatusText(nextPipelineState);
                    changeReputation(reputationChangeSuccess);
                } else {
                    handleFailure(stage);
                    changeReputation(reputationChangeFailure);
                }

                // Add revenue from approved drugs after each cycle/action completes
                if (gameState.approvedDrugs > 0) {
                     const revenue = gameState.approvedDrugs * gameState.revenuePerDrugPerCycle;
                     changeCash(revenue);
                     logEvent(`הכנסות מחזוריות מתרופות מאושרות: +${revenue.toLocaleString()}₪.`);
                     gameState.cycles++;
                }


                updateUI();
            }, duration);
        }

        function endGame(isWin) {
            gameState.isProcessing = true; // Disable further actions
            const allButtons = [startRndButton, startClinical1Button, startClinical2Button, startClinical3Button, submitRegulationButton, launchMarketingButton];
            allButtons.forEach(button => button.disabled = true);

            gameMessageElement.style.display = 'block';
            if (isWin) {
                gameMessageElement.classList.add('win');
                gameMessageElement.textContent = `ניצחון מוחץ! אישרתם בהצלחה ${gameState.approvedDrugs} תרופות והפכתם לחברת פארמה מובילה! כל הכבוד!`;
                logEvent('🎉🎉🎉 ניצחון! החברה שלכם כבשה את השוק! 🎉🎉🎉', true);
            } else {
                gameMessageElement.classList.add('lose');
                gameMessageElement.textContent = `משחק נגמר! נגמר לכם הכסף לפני שהספקתם לאשר מספיק תרופות. עולם הפארמה אכזרי!`;
                logEvent('💔💔💔 משחק נגמר! אזל המזומנים. נסו שוב! 💔💔💔', true);
            }
             gameState.currentStage = isWin ? 'ניצחון' : 'הפסד';
             updateUI(); // Final UI update
        }


        // Event Listeners
        startRndButton.addEventListener('click', () => {
            runSimulationStage(
                'מחקר ופיתוח',
                gameState.rndCost,
                gameState.rndSuccessRate + (gameState.reputation / 200), // Slight boost from reputation
                5, // Rep gain on success
                -10, // Rep loss on failure
                'Clinical I',
                'פריצת דרך במעבדה! נמצאה מולקולה פוטנציאלית מבטיחה.',
                'פרויקט המחקר נכשל. המולקולה אינה יציבה/יעילה.'
            );
        });

        startClinical1Button.addEventListener('click', () => {
            runSimulationStage(
                'ניסוי קליני שלב I',
                gameState.clinicalCost1,
                gameState.clinicalSuccessRate1 + (gameState.reputation / 400), // Slight boost
                5,
                -10,
                'Clinical II',
                'שלב I הסתיים בהצלחה! התרופה נראית בטוחה לשימוש ראשוני.',
                'שלב I נכשל. התגלו תופעות לוואי חמורות מדי.'
            );
        });

         startClinical2Button.addEventListener('click', () => {
            runSimulationStage(
                'ניסוי קליני שלב II',
                gameState.clinicalCost2,
                gameState.clinicalSuccessRate2 + (gameState.reputation / 400), // Slight boost
                10,
                -10,
                'Clinical III',
                'שלב II הצליח! התרופה הדגימה יעילות משמעותית בקבוצת החולים.',
                'שלב II נכשל. התרופה לא הראתה יתרון מובהק על פני פלצבו/טיפול קיים.'
            );
        });

        startClinical3Button.addEventListener('click', () => {
            runSimulationStage(
                'ניסוי קליני שלב III',
                gameState.clinicalCost3,
                gameState.clinicalSuccessRate3 + (gameState.reputation / 400), // Slight boost
                15,
                -15,
                'Regulation',
                'ניסוי קליני שלב III הושלם בהצלחה! התרופה בטוחה ויעילה בקנה מידה גדול.',
                'שלב III נכשל. התוצאות לא עמדו בציפיות או התגלו סיכונים נוספים.'
            );
        });

        submitRegulationButton.addEventListener('click', () => {
            runSimulationStage(
                'בדיקה רגולטורית',
                gameState.regulationCost,
                gameState.regulationApprovalRate + (gameState.reputation / 400), // Slight boost
                20, // Big rep gain on approval
                -15, // Big rep loss on rejection
                'Approved', // If successful
                'חדשות מעולות! הרשויות הרגולטוריות אישרו את התרופה!',
                'הבקשה הרגולטורית נדחתה. נדרשים נתונים נוספים או שהפרויקט נעצר.' // Failure handled inside runSimulationStage for this step
            );
        });

        launchMarketingButton.addEventListener('click', () => {
             if (gameState.isProcessing) return;
             if (gameState.drugInPipeline !== 'Approved') {
                 logEvent('לא ניתן להשיק לשוק כעת.');
                 return;
             }
             if (gameState.cash < gameState.marketingCost) {
                 logEvent('אין מספיק מזומנים להשקה מסחרית גרנדיוזית!');
                 return;
             }

             changeCash(-gameState.marketingCost);
             gameState.currentStage = 'השקה מסחרית';
             logEvent(`מתחילים בהשקה מסחרית של התרופה! עלות שיווק ראשונית: ${gameState.marketingCost.toLocaleString()}₪.`);
             gameState.isProcessing = true; // Simulate marketing effort time

             const duration = 3000; // Simulate 3 seconds marketing push
             let progress = 0;
             const interval = setInterval(() => {
                 progress += (100 / (duration / 100));
                 if (progress > 100) progress = 100;
                 progressBar.style.width = progress + '%';
                 progressBar.textContent = `${Math.round(progress)}%`;
             }, 100);

             setTimeout(() => {
                 clearInterval(interval);
                 progressBar.style.width = '100%';
                 progressBar.textContent = '100%';

                 gameState.approvedDrugs += 1;
                 logEvent(`🎉🎉🎉 התרופה הושקה בהצלחה לשוק! היא תתחיל להניב הכנסות. 🎉🎉🎉`, true);
                 gameState.drugInPipeline = null; // Pipeline is now free for the next project
                 gameState.currentStage = 'מוכן לפרויקט חדש';
                 changeReputation(10); // Gain reputation from successful launch

                 // Add initial revenue from the first cycle of marketing
                 const initialRevenue = gameState.revenuePerDrugPerCycle;
                 changeCash(initialRevenue);
                 logEvent(`הכנסות ראשוניות מההשקה: +${initialRevenue.toLocaleString()}₪.`);

                 gameState.isProcessing = false;
                 gameState.cycles++; // Count this as a cycle

                 updateUI(); // Update after launch
             }, duration);
        });


        explanationToggle.addEventListener('click', () => {
            const isHidden = explanationContent.style.display === 'none' || explanationContent.style.display === '';
            explanationContent.style.display = isHidden ? 'block' : 'none';
            explanationToggle.textContent = isHidden ? 'הסתר הסבר על תעשיית התרופות' : 'הצג הסבר על עולם תעשיית התרופות';
        });

        // Initial UI update
        updateUI();

    </script>
</body>
</html>
```