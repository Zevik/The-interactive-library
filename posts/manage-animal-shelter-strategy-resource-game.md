---
title: "מנהלים מקלט לחיות: מסע הישרדות וניהול משאבים"
english_slug: manage-animal-shelter-strategy-resource-game
category: "ניהול ומלכ\"רים"
tags: [ניהול משאבים, מלכ"רים, רווחת בעלי חיים, קבלת החלטות, סימולציה, משחק לימודי]
---
<!DOCTYPE html>
<html lang="he">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>מנהלים מקלט לחיות: מסע הישרדות וניהול משאבים</title>
    <link href="https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Heebo', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background: linear-gradient(to bottom, #e0f2f7, #b2ebf2); /* Soft blue gradient */
            color: #333;
            direction: rtl; /* Right-to-left for Hebrew */
            text-align: right;
        }
        .container {
            max-width: 960px; /* Slightly wider container */
            margin: 30px auto;
            background: #ffffff;
            padding: 30px 40px; /* More padding */
            border-radius: 12px; /* Softer corners */
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1); /* More prominent shadow */
            position: relative; /* Needed for absolute positioning of messages */
            overflow: hidden; /* Clear floats/margins */
        }
        h1, h2, h3 {
            color: #00796b; /* Teal */
            text-align: center;
            margin-bottom: 20px;
        }
        h1 {
            font-size: 2.5em;
            font-weight: 700;
            border-bottom: 2px solid #b2ebf2;
            padding-bottom: 15px;
        }
         h2 {
             font-size: 1.8em;
             font-weight: 700;
             margin-top: 25px;
             border-bottom: 1px solid #e0f2f7;
             padding-bottom: 10px;
         }
         h3 {
             font-size: 1.4em;
             font-weight: 700;
             margin-top: 20px;
             margin-bottom: 15px;
             color: #004d40; /* Darker teal */
         }

        p {
            font-size: 1.1em;
            margin-bottom: 15px;
        }

        .app-section {
            margin-top: 30px;
            padding: 25px;
            background-color: #e0f2f7; /* Lightest blue */
            border-radius: 10px;
            box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.05);
        }

        .game-state {
            margin-bottom: 30px;
            padding: 20px;
            background-color: #b2ebf2; /* Light blue */
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }

        .game-state p {
            font-size: 1.2em;
            font-weight: 700;
            color: #004d40;
            text-align: center;
            margin-bottom: 15px;
        }

        .stats {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            justify-content: center; /* Center stats */
            margin-bottom: 20px;
        }

        .stat-item {
            background: #00796b; /* Teal */
            color: white;
            padding: 12px 18px; /* More padding */
            border-radius: 25px; /* Pill shape */
            font-weight: 700;
            font-size: 1em;
            min-width: 120px; /* Minimum width */
            text-align: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
            transition: transform 0.3s ease, box-shadow 0.3s ease; /* Animation for updates */
        }

         .stat-item:hover {
             transform: translateY(-3px);
             box-shadow: 0 4px 8px rgba(0,0,0,0.3);
         }

        .stat-value {
             font-weight: bold;
             margin-right: 5px; /* Space between value and label */
        }

        .decisions .controls {
            display: flex;
            flex-wrap: wrap;
            gap: 12px; /* Tighter gap */
            justify-content: center; /* Center buttons */
            margin-bottom: 20px;
        }

        .controls button {
            flex-grow: 1; /* Buttons grow to fill space */
            padding: 12px 20px; /* More padding */
            background-color: #4db6ac; /* Lighter teal */
            color: white;
            border: none;
            border-radius: 8px; /* Softer corners */
            cursor: pointer;
            font-size: 1em;
            font-weight: 700;
            transition: background-color 0.3s ease, transform 0.1s ease;
            min-width: 150px; /* Ensure minimum button width */
            max-width: 200px; /* Max width */
            text-align: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }

        .controls button:hover:not(:disabled) {
            background-color: #26a69a; /* Darker teal on hover */
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        }

         .controls button:disabled {
             background-color: #bdbdbd; /* Grey when disabled */
             cursor: not-allowed;
             opacity: 0.7;
             box-shadow: none;
         }

         .controls button.selected {
             background-color: #004d40; /* Dark teal when selected */
             box-shadow: inset 0 2px 5px rgba(0,0,0,0.3);
             transform: none;
         }

         #nextMonthBtn {
             display: block;
             margin: 25px auto 0; /* Center and add space */
             padding: 15px 30px;
             background-color: #004d40; /* Dark teal */
             color: white;
             border: none;
             border-radius: 8px;
             cursor: pointer;
             font-size: 1.2em;
             font-weight: 700;
             transition: background-color 0.3s ease, transform 0.1s ease;
              box-shadow: 0 3px 8px rgba(0,0,0,0.3);
         }

         #nextMonthBtn:hover:not(:disabled) {
             background-color: #00392e; /* Even darker teal */
             transform: translateY(-2px);
             box-shadow: 0 5px 10px rgba(0,0,0,0.4);
         }

         #nextMonthBtn:disabled {
             background-color: #bdbdbd;
             cursor: not-allowed;
             opacity: 0.7;
             box-shadow: none;
         }

        .messages {
            margin-top: 20px;
            padding: 15px;
            background-color: #fff9c4; /* Light yellow */
            border-radius: 8px;
            border: 1px solid #fbc02d; /* Darker yellow border */
            min-height: 50px; /* Ensure visibility even with short messages */
            position: relative;
            overflow: hidden;
            box-shadow: 0 1px 4px rgba(0,0,0,0.1);
            transition: all 0.5s ease-in-out; /* Smooth appearance */
            text-align: right;
        }

         .messages h3 {
             margin-top: 0;
             color: #fbc02d; /* Match border color */
             text-align: right;
             border: none;
             padding-bottom: 0;
         }

         .messages p {
             font-size: 1em;
             margin-bottom: 5px;
             color: #333;
         }

         .messages p::before {
             content: '• '; /* Bullet point */
             color: #fbc02d;
             font-weight: bold;
         }


        #explanation {
            display: none;
            margin-top: 30px;
            padding-top: 25px;
            border-top: 2px dashed #b2ebf2; /* Dashed border */
        }
        #explanation h2 {
             margin-top: 0;
             text-align: right;
             border: none;
             padding-bottom: 0;
             color: #00796b;
        }
         #explanation ul {
            list-style: none; /* Remove default bullets */
            padding-left: 0;
            margin-top: 15px;
        }
        #explanation li {
            margin-bottom: 12px;
            padding-right: 25px; /* Space for custom bullet */
            position: relative;
            font-size: 1.05em;
            line-height: 1.7;
        }
         #explanation li::before {
             content: '🐾'; /* Paw print bullet */
             position: absolute;
             right: 0;
             color: #00796b;
             font-size: 1.2em;
             top: 0;
         }

        .toggle-explanation-btn {
             padding: 12px 25px;
            background-color: #4caf50; /* Green */
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 1em;
            font-weight: 700;
            transition: background-color 0.3s ease, transform 0.1s ease;
            display: block;
            margin: 25px auto;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }
         .toggle-explanation-btn:hover {
            background-color: #388e3c; /* Darker green */
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        }

        .end-game-message {
            margin-top: 25px;
            padding: 25px;
            border-radius: 8px;
            font-weight: bold;
            text-align: center;
            font-size: 1.3em;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            opacity: 0; /* Start hidden */
            transform: translateY(20px); /* Start below */
            animation: slideUpFadeIn 0.8s forwards; /* Animation */
        }

        .end-game-message.win {
            background-color: #e8f5e9; /* Light green background */
            color: #2e7d32; /* Dark green text */
            border: 2px solid #4caf50;
        }
         .end-game-message.lose {
            background-color: #ffebee; /* Light red background */
            color: #c62828; /* Dark red text */
            border: 2px solid #f44336;
         }

         @keyframes slideUpFadeIn {
             to {
                 opacity: 1;
                 transform: translateY(0);
             }
         }

         .end-game-message button {
             margin-top: 20px;
             padding: 12px 25px;
             background-color: #ff9800; /* Orange */
             color: white;
             border: none;
             border-radius: 8px;
             cursor: pointer;
             font-size: 1em;
             font-weight: 700;
             transition: background-color 0.3s ease, transform 0.1s ease;
             box-shadow: 0 2px 5px rgba(0,0,0,0.2);
         }

          .end-game-message button:hover {
              background-color: #f57c00; /* Darker orange */
               transform: translateY(-2px);
              box-shadow: 0 4px 8px rgba(0,0,0,0.3);
          }

          /* Animation for stat changes */
          .stat-item.changed {
              animation: pulse 0.5s ease-in-out forwards;
          }

          @keyframes pulse {
              0% { transform: scale(1); background-color: #00796b; }
              50% { transform: scale(1.05); background-color: #4db6ac; }
              100% { transform: scale(1); background-color: #00796b; }
          }

          .messages p.new-message {
              opacity: 0;
              transform: translateY(10px);
              animation: fadeInSlideUpMessage 0.5s ease-out forwards;
          }

          @keyframes fadeInSlideUpMessage {
              to {
                  opacity: 1;
                  transform: translateY(0);
              }
          }


    </style>
</head>
<body>

    <div class="container">
        <h1>מנהלים מקלט לחיות: מסע הישרדות וניהול משאבים</h1>

        <p>ברוכים הבאים למקלט לחיות! קיבלתם לידיכם את האחריות על מקום שכולו תקווה וחיים, אבל גם אתגרים וקשיים. בכל חודש תצטרכו לקבל החלטות קריטיות: על מה להוציא את הכסף המוגבל? איך לשמור על בריאות החיות? ואיך למצוא להן בתים אוהבים? המטרה: לשרוד שנה שלמה ולשגשג, תוך שמירה על רווחת בעלי החיים.</p>

        <div class="app-section">
            <h2>הסימולציה שלכם</h2>

            <div class="game-state">
                <p><strong>חודש:</strong> <span id="currentMonth" class="stat-value">1</span> מתוך <span class="stat-value">12</span></p>
                <div class="stats">
                    <div class="stat-item" id="moneyStat">כסף בקופה: <span id="money" class="stat-value">$5,000</span></div>
                    <div class="stat-item" id="animalsStat">בעלי חיים במקלט: <span id="animals" class="stat-value">50</span></div>
                    <div class="stat-item" id="healthyPercentStat">אחוז בריאים: <span id="healthyPercent" class="stat-value">80</span>%</div>
                    <div class="stat-item" id="adoptionsTotalStat">סה"כ אימוצים: <span id="adoptionsTotal" class="stat-value">0</span></div>
                    <div class="stat-item" id="volunteersStat">מתנדבים: <span id="volunteers" class="stat-value">10</span></div>
                </div>
            </div>

            <div class="decisions">
                <h3>החלטות לחודש הקרוב: (בחרו אופציה אחת מכל קטגוריה שרלוונטית עבורכם)</h3>
                <div class="controls">
                    <!-- Vet Care -->
                    <button data-decision-type="vet" data-decision-level="1" data-cost="500" id="vetLow">וטרינר (בסיסי): $500</button>
                    <button data-decision-type="vet" data-decision-level="2" data-cost="1500" id="vetMedium">וטרינר (רגיל): $1,500</button>
                    <button data-decision-type="vet" data-decision-level="3" data-cost="3000" id="vetHigh">וטרינר (מקיף): $3,000</button>

                    <!-- Food -->
                    <button data-decision-type="food" data-decision-level="1" data-cost="800" id="foodStd">מזון (רגיל): $800</button>
                    <button data-decision-type="food" data-decision-level="2" data-cost="1200" id="foodExtra">מזון (איכותי): $1,200</button>
                     <!-- Removed food 0 option as basic care includes minimal food cost now -->

                    <!-- Marketing -->
                     <button data-decision-type="marketing" data-decision-level="1" data-cost="300" id="marketLow">שיווק (מקומי): $300</button>
                     <button data-decision-type="marketing" data-decision-level="2" data-cost="800" id="marketHigh">שיווק (רחב): $800</button>

                    <!-- Operations/Funding -->
                    <button data-decision-type="recruit" data-decision-level="1" data-cost="400" id="recruitVolunteers">גיוס מתנדבים: $400</button>
                    <button data-decision-type="fundraising" data-decision-level="1" data-cost="1000" id="eventFundraising">אירוע התרמה: $1,000</button>
                </div>
            </div>

             <div class="messages" id="monthlyMessages">
                <h3>מה קרה החודש:</h3>
                <!-- Messages will be added here by JS -->
            </div>

            <div class="controls" style="margin-top: 20px;">
                <button id="nextMonthBtn">עבור לחודש הבא ></button>
            </div>

             <div class="end-game-message" id="endGameMessage" style="display: none;">
                <p id="endGameText"></p>
                <!-- Reset button will be added by JS -->
            </div>

        </div>

        <button class="toggle-explanation-btn" id="toggleExplanationBtn">ללמוד על ניהול מלכ"רים וקבלת החלטות ></button>

        <div id="explanation">
            <h2>הסבר: האתגרים בניהול מקלט לחיות ומלכ"רים בכלל</h2>
            <p>ניהול ארגון ללא מטרות רווח (מלכ"ר) הוא משימה מורכבת הדורשת איזון עדין בין מטרת העל החברתית לבין הצורך בשמירה על קיימות כלכלית. במקלט לחיות, זה מתבטא בצורך לספק את הטיפול הטוב ביותר לבעלי החיים, תוך התמודדות עם תקציב מוגבל ותלות בתרומות ומתנדבים.</p>
            <ul>
                <li><strong>האתגרים הייחודיים של מלכ"רים:</strong> המטרה אינה רווח, אלא השפעה. זה מחייב שקיפות, בניית אמון עם הציבור והתורמים, והוכחת יעילות ההשפעה. מקורות הכנסה לרוב פחות יציבים מאשר בעסק.</li>
                <li><strong>ניהול משאבים הוליסטי:</strong> מעבר לכסף, יש לנהל ביעילות זמן (צוות ומתנדבים), תרומות בעין (מזון, ציוד), ומוניטין. הקצאת משאבים כאן שונה - לפעמים נשקיע בגיוס מתנדבים במקום בפרסום, כי ההשפעה לטווח ארוך שונה.</li>
                <li><strong>תכנון פיננסי וגיוס תרומות:</strong> גיוס כספים הוא נשמת אפו של מלכ"ר. זה דורש יצירת קשרים, קמפיינים, הגשת בקשות למענקים, ותקציב מפורט ומאוזן שיבטיח שהארגון לא יקרוס כלכלית. כל שקל נספר.</li>
                <li><strong>קבלת החלטות באילוץ ואי-ודאות:</strong> כמו בסימולציה, יש אירועים בלתי צפויים. צריך לקבל החלטות מהירות ולעיתים קשות (למשל, על איזה טיפול רפואי לוותר כשהתקציב נגמר), תוך שקלול ההשפעה על החיות, הצוות, והמוניטין.</li>
                <li><strong>ניהול כוח אדם - מתנדבים וצוות:</strong> מתנדבים הם כוח עצום, אך דורשים גיוס, הכשרה, ניהול יום-יומי, ושימור. צוות מקצועי (וטרינרים, מטפלים) חיוני, אך עולה כסף. שמירה על מורל ומוטיבציה של כולם היא קריטית להצלחת המקלט.</li>
                <li><strong>הקשר לקהילה:</strong> מקלט אינו אי בודד. הוא תלוי בקהילה לאימוצים, תרומות, ומתנדבים. פעילות חינוכית, אירועים, ושקיפות בונים קשר חזק שתורם לשגשוג המקלט ולהפחתת נטישות בעתיד.</li>
                <li><strong>מדדי הצלחה מורכבים:</strong> מעבר למספר האימוצים, נבחנים מדדים כמו אחוז החיות המבריאות, משך השהייה הממוצע, שביעות רצון מתנדבים, יעילות ההוצאות, גיוון מקורות ההכנסה, וההשפעה הקהילתית הרחבה.</li>
                <li><strong>האספקטים האתיים:</strong> ניהול מקלט כרוך בהתמודדות עם דילמות אתיות כואבות, כמו החלטות על המתת חסד, הקצאת משאבים לטיפולים יקרים (מי מקבל?), והתמודדות עם מקרי התעללות הדורשים גם שיקום וגם משאבים.</li>
            </ul>
             <p>הסימולציה ששיחקתם מדמה חלק מהאתגרים האלו בקנה מידה קטן. כפי שראיתם, כל החלטה משפיעה על המצב הכלכלי, בריאות החיות, ויכולת המקלט להמשיך לפעול.</p>
        </div>
    </div>

    <script>
        const state = {
            month: 1,
            maxMonths: 12,
            money: 5000,
            animals: 50,
            healthyAnimals: 40,
            volunteers: 10,
            adoptionsTotal: 0,
            adoptionsMonth: 0,
            vetBudget: 0,
            foodBudget: 0,
            marketingBudget: 0,
            recruitBudget: 0,
            fundraisingBudget: 0,
            gameEnded: false,
            monthlyMessages: [] // Array to store messages for the month
        };

        const costs = {
            vetLow: 500,
            vetMedium: 1500,
            vetHigh: 3000,
            foodStd: 800,
            foodExtra: 1200,
            marketLow: 300,
            marketHigh: 800,
            recruit: 400,
            fundraising: 1000,
            basicMonthlyCarePerAnimal: 60, // Slightly increased basic cost
        };

        const effects = {
            vet: { // Affects healing sick and preventing new sickness
                0: { healRate: 0.05, newSickRate: 0.15 }, // No vet - bad
                1: { healRate: 0.15, newSickRate: 0.10 }, // Low vet
                2: { healRate: 0.30, newSickRate: 0.06 }, // Medium vet
                3: { healRate: 0.50, newSickRate: 0.03 }  // High vet
            },
            food: { // Affects health recovery rate and new sick rate slightly
                0: { healthMod: -0.1, cost: 0 }, // No food (hypothetical, basic cost covers minimal)
                1: { healthMod: 0, cost: costs.foodStd }, // Standard food
                2: { healthMod: 0.05, cost: costs.foodExtra } // Extra food
            },
            marketing: { // Affects adoption rate (higher marketing + more healthy animals = more adoptions)
                0: { adoptionBase: 0.02 }, // Minimal
                1: { adoptionBase: 0.05 }, // Low effort
                2: { adoptionBase: 0.09 } // High effort
            },
            recruit: { // Adds volunteers
                1: { volunteerGain: 4 }
            },
            fundraising: { // Adds money
                1: { moneyGainBase: 1200, moneyGainVariance: 800 } // Base gain + variance
            },
            eventProbability: 0.4 // Increased chance of random event
        };

        const elements = {
            month: document.getElementById('currentMonth'),
            money: document.getElementById('money'),
            animals: document.getElementById('animals'),
            healthyPercent: document.getElementById('healthyPercent'),
            adoptionsTotal: document.getElementById('adoptionsTotal'),
            volunteers: document.getElementById('volunteers'),
            moneyStat: document.getElementById('moneyStat'), // For animation
            animalsStat: document.getElementById('animalsStat'),
            healthyPercentStat: document.getElementById('healthyPercentStat'),
            adoptionsTotalStat: document.getElementById('adoptionsTotalStat'),
            volunteersStat: document.getElementById('volunteersStat'),

            decisionButtons: document.querySelectorAll('.decisions button'), // All decision buttons
            nextMonthBtn: document.getElementById('nextMonthBtn'),
            monthlyMessagesDiv: document.getElementById('monthlyMessages'),
            endGameMessageDiv: document.getElementById('endGameMessage'),
            endGameText: document.getElementById('endGameText'),
            decisionControls: document.querySelector('.decisions .controls'), // Group for disabling
            explanationDiv: document.getElementById('explanation') // Explanation div
        };

        function updateDisplay() {
            const sickAnimals = state.animals - state.healthyAnimals;
            state.healthyPercent = state.animals === 0 ? 100 : Math.round((state.healthyAnimals / state.animals) * 100);

            // Store old values for animation check
            const oldMoney = parseInt(elements.money.textContent.replace(/[$,]/g, ''));
            const oldAnimals = parseInt(elements.animals.textContent);
            const oldHealthyPercent = parseInt(elements.healthyPercent.textContent);
            const oldAdoptionsTotal = parseInt(elements.adoptionsTotal.textContent);
            const oldVolunteers = parseInt(elements.volunteers.textContent);


            elements.month.textContent = state.month;
            elements.money.textContent = `$${state.money.toLocaleString()}`;
            elements.animals.textContent = state.animals;
            elements.healthyPercent.textContent = state.healthyPercent;
            elements.adoptionsTotal.textContent = state.adoptionsTotal;
            elements.volunteers.textContent = state.volunteers;

            // Animate stats if changed
            if (state.money !== oldMoney) elements.moneyStat.classList.add('changed'); else elements.moneyStat.classList.remove('changed');
            if (state.animals !== oldAnimals) elements.animalsStat.classList.add('changed'); else elements.animalsStat.classList.remove('changed');
            if (state.healthyPercent !== oldHealthyPercent) elements.healthyPercentStat.classList.add('changed'); else elements.healthyPercentStat.classList.remove('changed');
            if (state.adoptionsTotal !== oldAdoptionsTotal) elements.adoptionsTotalStat.classList.add('changed'); else elements.adoptionsTotalStat.classList.remove('changed');
             if (state.volunteers !== oldVolunteers) elements.volunteersStat.classList.add('changed'); else elements.volunteersStat.classList.remove('changed');

             // Remove animation class after animation
             setTimeout(() => {
                 elements.moneyStat.classList.remove('changed');
                 elements.animalsStat.classList.remove('changed');
                 elements.healthyPercentStat.classList.remove('changed');
                 elements.adoptionsTotalStat.classList.remove('changed');
                 elements.volunteersStat.classList.remove('changed');
             }, 600); // Match animation duration

            // Enable/disable buttons based on budget and selection state
            elements.decisionButtons.forEach(button => {
                const cost = parseInt(button.dataset.cost);
                const type = button.dataset.decisionType;
                const level = parseInt(button.dataset.decisionLevel);

                let isDisabled = state.money < cost;
                let isSelected = false;

                if (type === 'vet') {
                    isSelected = state.vetBudget === level;
                     isDisabled = isDisabled || (state.vetBudget > 0 && !isSelected); // Disable others in the category if one is selected
                } else if (type === 'food') {
                    isSelected = state.foodBudget === level;
                     isDisabled = isDisabled || (state.foodBudget > 0 && !isSelected);
                } else if (type === 'marketing') {
                    isSelected = state.marketingBudget === level;
                     isDisabled = isDisabled || (state.marketingBudget > 0 && !isSelected);
                } else if (type === 'recruit') {
                    isSelected = state.recruitBudget === level;
                    isDisabled = isDisabled || state.recruitBudget > 0; // Only allow one recruit action
                } else if (type === 'fundraising') {
                    isSelected = state.fundraisingBudget === level;
                    isDisabled = isDisabled || state.fundraisingBudget > 0; // Only allow one fundraising action
                }


                button.disabled = isDisabled || state.gameEnded; // Also disable if game ended
                button.classList.toggle('selected', isSelected);
                 button.style.backgroundColor = isSelected ? '#004d40' : (isDisabled ? '#bdbdbd' : '#4db6ac');

            });

            // Update messages display
            elements.monthlyMessagesDiv.innerHTML = '<h3>מה קרה החודש:</h3>'; // Clear previous messages
            if (state.monthlyMessages.length > 0) {
                state.monthlyMessages.forEach((msg, index) => {
                    const p = document.createElement('p');
                    p.textContent = msg;
                    p.classList.add('new-message');
                    p.style.animationDelay = `${index * 0.1}s`; // Stagger animation
                    elements.monthlyMessagesDiv.appendChild(p);
                });
                elements.monthlyMessagesDiv.style.display = 'block';
            } else {
                // elements.monthlyMessagesDiv.style.display = 'none'; // Keep the section visible, just clear messages
            }

        }

        function applyDecision(type, level, cost, buttonElement) {
            if (state.gameEnded || buttonElement.disabled) return; // Check disabled state
            if (state.money < cost) {
                alert("אין מספיק כסף להחלטה זו!"); // Use simple alert for now
                return;
            }

            // Prevent selecting more than one per category (except Recruit/Fundraising which are one-offs)
             if (type === 'vet' && state.vetBudget > 0) state.vetBudget = 0; // Deselect previous vet
             if (type === 'food' && state.foodBudget > 0) state.foodBudget = 0; // Deselect previous food
             if (type === 'marketing' && state.marketingBudget > 0) state.marketingBudget = 0; // Deselect previous marketing
             // Recruit and Fundraising are one-off per month, handled by disable

            // Apply decision and subtract cost immediately for feedback
            state.money -= cost;

            if (type === 'vet') state.vetBudget = level;
            else if (type === 'food') state.foodBudget = level;
            else if (type === 'marketing') state.marketingBudget = level;
            else if (type === 'recruit') state.recruitBudget = level;
            else if (type === 'fundraising') state.fundraisingBudget = level;

            updateDisplay(); // Update display immediately to show money change and selection
        }

        function endMonth() {
            if (state.gameEnded) return;

            state.monthlyMessages = []; // Reset monthly messages
            state.adoptionsMonth = 0; // Reset monthly adoptions

            state.monthlyMessages.push(`--- התחלת חודש ${state.month} ---`);

            // --- Apply monthly costs ---
             // Basic care cost (mandatory)
            const basicCareCost = state.animals * costs.basicMonthlyCarePerAnimal;
            state.money -= basicCareCost;
            state.monthlyMessages.push(`עלות טיפול בסיסית ל-${state.animals} חיות: $${basicCareCost}.`);

             // Food cost (mandatory, standard if none selected)
             let foodCostToPay = costs.foodStd; // Default to standard cost
             let actualFoodBudgetLevel = 1; // Default level effect
             if (state.foodBudget === 2) {
                  foodCostToPay = costs.foodExtra;
                  actualFoodBudgetLevel = 2;
             } else if (state.foodBudget === 0 && state.month > 1) { // First month food is included in start money, subsequent months need decision.
                 // If no food decision was made, still pay standard but get no bonus
                 state.monthlyMessages.push('לא בחרת תקציב מזון החודש, סופק מזון בסיסי בעלות רגילה.');
             }
            state.money -= foodCostToPay;
            state.monthlyMessages.push(`הוצאה על מזון: $${foodCostToPay}.`);


            // --- Apply effects based on decisions ---
            const sickAnimalsBefore = state.animals - state.healthyAnimals;
             let healed = 0;
             let newSickFromPoorCare = 0;
             let adopted = 0;
             let newVolunteers = 0;
             let fundraisingGain = 0;

             // Vet care effect
             if (sickAnimalsBefore > 0) {
                healed = Math.min(sickAnimalsBefore, Math.floor(sickAnimalsBefore * effects.vet[state.vetBudget].healRate));
                 state.healthyAnimals += healed;
             }
             if (state.healthyAnimals > 0) {
                newSickFromPoorCare = Math.min(state.healthyAnimals, Math.floor(state.healthyAnimals * effects.vet[state.vetBudget].newSickRate));
                state.healthyAnimals -= newSickFromPoorCare;
             }
             state.healthyAnimals = Math.max(0, Math.min(state.healthyAnimals, state.animals)); // Ensure bounds
             state.monthlyMessages.push(`טיפול וטרינרי (רמה ${state.vetBudget}): החלימו ${healed}, חלו ${newSickFromPoorCare}.`);


             // Food effect (small modification to health change rates based on food quality)
             const foodHealthMod = effects.food[actualFoodBudgetLevel].healthMod;
             // Apply modification to health changes
             const modifiedHealRate = effects.vet[state.vetBudget].healRate * (1 + foodHealthMod);
             const modifiedNewSickRate = effects.vet[state.vetBudget].newSickRate * (1 - foodHealthMod);

              // Re-calculate health effects with food mod (simplification: apply mod directly)
              const sickBeforeFood = state.animals - state.healthyAnimals;
              const healthyBeforeFood = state.healthyAnimals;
              healed = Math.min(sickBeforeFood, Math.floor(sickBeforeFood * modifiedHealRate));
              newSickFromPoorCare = Math.min(healthyBeforeFood, Math.floor(healthyBeforeFood * modifiedNewSickRate));

             state.healthyAnimals = healthyBeforeFood + healed - newSickFromPoorCare;


             state.healthyAnimals = Math.max(0, Math.min(state.healthyAnimals, state.animals)); // Ensure bounds again

             if (foodHealthMod > 0) state.monthlyMessages.push('איכות מזון משופרת תרמה לבריאות החיות והפחיתה תחלואה.');
             if (foodHealthMod < 0) state.monthlyMessages.push('איכות מזון ירודה פגעה בבריאות החיות והגבירה תחלואה.');
             state.monthlyMessages.push(`בריאות החיות לאחר טיפול ומזון: ${state.healthyAnimals} בריאות מתוך ${state.animals}.`);


            // Marketing/Adoption effect (Healthy animals are easier to adopt)
            const baseAdoptionRate = effects.marketing[state.marketingBudget].adoptionBase;
             const potentialAdoptions = Math.floor(state.healthyAnimals * baseAdoptionRate);
             // Volunteers limit how many adoptions can be processed
             const volunteerCapacity = Math.floor(state.volunteers * 0.8); // Each volunteer helps process ~0.8 adoptions?
             adopted = Math.min(potentialAdoptions, volunteerCapacity);
             adopted = Math.max(0, adopted); // Ensure not negative
             state.adoptionsMonth = adopted;
             state.adoptionsTotal += adopted;
             state.animals -= adopted;
             state.healthyAnimals = Math.min(state.healthyAnimals, state.animals); // Ensure healthy count doesn't exceed total
             state.monthlyMessages.push(`שיווק (רמה ${state.marketingBudget}) ומתנדבים סייעו במציאת בתים: ${adopted} חיות אומצו החודש.`);


            // Volunteer recruitment effect
            if (state.recruitBudget > 0) {
                newVolunteers = effects.recruit[state.recruitBudget].volunteerGain;
                state.volunteers += newVolunteers;
                 state.monthlyMessages.push(`השקעה בגיוס מתנדבים השתלמה: ${newVolunteers} מתנדבים חדשים הצטרפו.`);
            } else {
                // Small chance of losing volunteers if conditions are bad (low money, low healthy, low volunteers)
                 if (Math.random() < 0.15 && state.volunteers > 5 && (state.money < 1000 || state.healthyPercent < 50 || state.volunteers < 10)) {
                     const lost = Math.min(state.volunteers - 5, Math.floor(Math.random() * 3) + 1); // Lose 1-3, but not below 5
                     state.volunteers -= lost;
                      state.monthlyMessages.push(`${lost} מתנדבים עזבו החודש עקב תנאי הפעילות הקשים.`);
                 }
            }


            // Fundraising event effect
            if (state.fundraisingBudget > 0) {
                const baseGain = effects.fundraising[state.fundraisingBudget].moneyGainBase;
                const variance = effects.fundraising[state.fundraisingBudget].moneyGainVariance;
                // Success might depend on marketing/volunteers?
                const successModifier = 1 + (state.marketingBudget * 0.1) + (state.volunteers * 0.01); // Better marketing/more volunteers slightly boost fundraising
                fundraisingGain = Math.floor((baseGain + Math.random() * variance) * successModifier);
                state.money += fundraisingGain;
                 state.monthlyMessages.push(`אירוע גיוס התרומות הצליח מעבר למצופה! הקופה גדלה ב-$${fundraisingGain.toLocaleString()}.`);
            } else {
                 // Small base passive income from random small donations
                 const passiveIncome = Math.floor(Math.random() * 200) + 50; // 50 to 250
                 state.money += passiveIncome;
                  state.monthlyMessages.push(`תרומות קטנות ושוטפות נאספו החודש: +$${passiveIncome}.`);
            }


             // --- Simulate natural animal influx/issues ---
             const randomInflux = Math.floor(Math.random() * 6); // 0 to 5 new animals
              if(randomInflux > 0) {
                  state.animals += randomInflux;
                  state.healthyAnimals += randomInflux; // Assume new animals are initially healthy
                  state.monthlyMessages.push(`נאספו חיות נטושות חדשות: ${randomInflux}.`);
              }


            // --- Random Events ---
            if (Math.random() < effects.eventProbability) {
                const events = [
                     { text: "גל נטישות גדול במיוחד מגיע למקלט!", effect: () => {
                          const influx = Math.floor(Math.random() * 15) + 8; // 8 to 22 new animals
                          state.animals += influx;
                          state.healthyAnimals += influx; // Assume initially healthy, but strains resources next month
                          return `אירוע: גל נטישות! נוספו ${influx} חיות למקלט. עלויות וסיכון למחלות יגדלו החודש הבא.`;
                      }},
                     { text: "מחלה מדבקת מתפשטת במהירות במקלט!", effect: () => {
                          const newlySick = Math.min(state.healthyAnimals, Math.floor(state.healthyAnimals * (0.2 + Math.random() * 0.2))); // 20-40% of healthy animals get sick
                          state.healthyAnimals -= newlySick;
                           return `אירוע: התפרצות מחלה! ${newlySick} חיות חלו וזקוקות לטיפול דחוף.`;
                      }},
                     { text: "תרומה גדולה ובלתי צפויה התקבלה!", effect: () => {
                         const donation = Math.floor(Math.random() * 4000) + 2500; // 2500 to 6500
                          state.money += donation;
                           return `אירוע: תרומה מפתיעה! נדיבות הקהילה מילאה את הקופה ב-$${donation.toLocaleString()}.`;
                     }},
                     { text: "תקלה קריטית בתשתיות המקלט דורשת תיקון מיידי ויקר.", effect: () => {
                         const cost = Math.floor(Math.random() * 1500) + 700; // 700 to 2200
                          state.money -= cost;
                           return `אירוע: תקלה! עלות תיקון תשתיות קריטיות: $${cost.toLocaleString()}.`;
                     }},
                      { text: "קמפיין שיווקי מקומי הצליח מעל למצופה!", effect: () => {
                          // Increase adoptions this month retrospectively, or give bonus next month? Let's boost this month.
                           const bonusAdoptions = Math.min(state.healthyAnimals - adopted, Math.floor(state.healthyAnimals * (0.03 + Math.random() * 0.05))); // 3-8% bonus adoptions from healthy pool
                          state.adoptionsMonth += bonusAdoptions;
                          state.adoptionsTotal += bonusAdoptions;
                           state.animals -= bonusAdoptions;
                           state.healthyAnimals = Math.min(state.healthyAnimals, state.animals); // Re-adjust healthy count
                           if (bonusAdoptions > 0) {
                                return `אירוע: הצלחה שיווקית! ${bonusAdoptions} חיות נוספות אומצו בזכות פרסום יוצא דופן.`;
                           } else {
                                return `אירוע: הצלחה שיווקית קטנה! המודעות גדלה אך לא הובילה מיידית לאימוצים נוספים.`;
                           }
                     }},
                      { text: "יום התנדבות גדול משך המון עזרה!", effect: () => {
                         const bonusVolunteers = Math.floor(Math.random() * 5) + 3; // Gain 3-7 volunteers temporarily? Or permanently? Let's make them permanent for simplicity.
                          state.volunteers += bonusVolunteers;
                           return `אירוע: יום התנדבות! ${bonusVolunteers} מתנדבים נלהבים חדשים הצטרפו באופן קבוע.`;
                     }}
                ];
                const randomEvent = events[Math.floor(Math.random() * events.length)];
                 state.monthlyMessages.push(randomEvent.text); // Add event title
                 state.monthlyMessages.push(randomEvent.effect()); // Add effect message
            }

            // Ensure healthy count is not more than total animals
             state.healthyAnimals = Math.min(state.healthyAnimals, state.animals);

            // --- Check Win/Loss Conditions ---
            let endGameReason = '';
            let won = false;

            if (state.money < 0) {
                endGameReason = "נגמר הכסף! המקלט לא יכול לשרוד כלכלית ונאלץ להיסגר.";
                won = false;
            } else if (state.animals <= 0 && state.month <= state.maxMonths) {
                 endGameReason = "כל החיות מצאו בתים! המקלט מילא את ייעודו בהצלחה מדהימה!";
                 won = true; // Winning early condition
            }
            else if (state.healthyAnimals / state.animals < 0.2 && state.animals > 20) { // Less than 20% healthy if more than 20 animals
                 endGameReason = "אחוז החיות הבריאות נמוך מדי! תנאי המחיה ירודים והמקלט לא יכול להמשיך לפעול באופן הומני.";
                 won = false;
            } else if (state.volunteers < 2 && state.animals > 10) { // Not enough help to manage
                 endGameReason = "נותרו מעט מדי מתנדבים וצוות! אין מספיק ידיים לטפל בכל החיות.";
                 won = false;
            }
            else if (state.month >= state.maxMonths) {
                 if (state.money >= 0 && state.healthyAnimals / state.animals >= 0.4 && state.animals > 0) { // Survived, with reasonable health and still animals
                     endGameReason = `הצלחת לנהל את המקלט במשך שנה! ${state.adoptionsTotal} חיות מצאו בתים חדשים, והמקלט ממשיך לפעול בתקווה לעתיד טוב יותר.`;
                     won = true;
                 } else if (state.money >= 0 && state.animals === 0) {
                      endGameReason = `הגעת לסוף השנה וכל החיות אומצו! הצלחה אדירה!`;
                      won = true;
                 }
                 else {
                      endGameReason = `הגעת לסוף השנה, אך מצב המקלט אינו יציב מספיק כדי להבטיח את המשך פעילותו. נדרש שיפור משמעותי.`;
                      won = false;
                 }
            }

            // Prepare for next month
            if (!state.gameEnded) { // Only advance if game isn't over yet
                state.month++;
                state.vetBudget = 0; // Reset decisions for next month
                state.foodBudget = 0;
                state.marketingBudget = 0;
                state.recruitBudget = 0;
                state.fundraisingBudget = 0;
            }


            // Check if game ended
            if (endGameReason !== '') {
                 endGame(won, endGameReason);
            } else {
                state.monthlyMessages.push(`--- סוף חודש ${state.month -1} ---`);
                 updateDisplay(); // Update display only after calculating effects
            }

        }

         function endGame(win, message) {
             state.gameEnded = true;
             elements.nextMonthBtn.disabled = true;
             elements.nextMonthBtn.style.display = 'none'; // Hide next month button
             elements.decisionControls.style.display = 'none'; // Hide decision buttons

             elements.endGameMessageDiv.style.display = 'block';
             elements.endGameText.textContent = message;
             elements.endGameMessageDiv.className = 'end-game-message ' + (win ? 'win' : 'lose'); // Apply win/lose style

             // Add a reset button
             const resetBtn = document.createElement('button');
             resetBtn.textContent = "התחל מסע חדש!";
             resetBtn.onclick = initializeGame;
             // Clear any previous button before adding
             elements.endGameMessageDiv.innerHTML = '<p id="endGameText"></p>';
             elements.endGameMessageDiv.appendChild(document.getElementById('endGameText')); // Re-add the paragraph
             elements.endGameMessageDiv.appendChild(resetBtn);

             // Display final messages
             elements.monthlyMessages.push(message); // Add final message to log
             updateDisplay(); // Final display update
         }


         function initializeGame() {
             state.month = 1;
             state.money = 5000; // Starting money
             state.animals = 50; // Starting animals
             state.healthyAnimals = 45; // Starting healthy animals (adjust slightly)
             state.volunteers = 12; // Starting volunteers (adjust slightly)
             state.adoptionsTotal = 0;
             state.adoptionsMonth = 0;
             state.vetBudget = 0;
             state.foodBudget = 0;
             state.marketingBudget = 0;
             state.recruitBudget = 0;
             state.fundraisingBudget = 0;
             state.gameEnded = false;
             state.monthlyMessages = ['ברוכים הבאים למקלט!']; // Initial message

             elements.nextMonthBtn.disabled = false;
             elements.nextMonthBtn.style.display = 'block';
             elements.decisionControls.style.display = 'flex'; // Show decision buttons again
             elements.endGameMessageDiv.style.display = 'none';
             elements.endGameMessageDiv.className = 'end-game-message'; // Reset class
             elements.endGameMessageDiv.innerHTML = '<p id="endGameText"></p>'; // Clear previous end message and button


             updateDisplay();
         }


        // Event Listeners for decisions - Use data attributes
        elements.decisionButtons.forEach(button => {
            button.addEventListener('click', () => {
                const type = button.dataset.decisionType;
                const level = parseInt(button.dataset.decisionLevel);
                const cost = parseInt(button.dataset.cost);
                applyDecision(type, level, cost, button);
            });
        });


        // Event Listener for Next Month
        elements.nextMonthBtn.addEventListener('click', endMonth);

        // Toggle explanation visibility
        const toggleExplanationBtn = document.getElementById('toggleExplanationBtn');
        const explanationDiv = document.getElementById('explanation');
        toggleExplanationBtn.addEventListener('click', () => {
            const isVisible = explanationDiv.style.display === 'block';
            explanationDiv.style.display = isVisible ? 'none' : 'block';
             toggleExplanationBtn.textContent = isVisible ? 'ללמוד על ניהול מלכ"רים וקבלת החלטות >' : '< הסתר הסבר';
        });


        // Initialize the game on page load
        initializeGame();

    </script>

</body>
</html>