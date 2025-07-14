---
title: "צוללים למסתורי המערה: חוקרים מערכות אקולוגיות תת-קרקעיות"
english_slug: diving-into-the-cave-depths-new-tool-for-ecosystem-research
category: "מדעי הסביבה / אקולוגיה וקיימות"
tags: [מערות, אקולוגיה, בתי חיים, כלי מחקר, מגוון ביולוגי, סביבות קיצון]
---
# צוללים למסתורי המערה: חוקרים מערכות אקולוגיות תת-קרקעיות
מערות נראות לנו לרוב כחללים אפלים ושוממים, אך למעשה הן בתי גידול תוססים המכילים חיים יחידים במינם, שהתפתחו בתנאים קיצוניים. איך מגלים את הסודות האקולוגיים החבויים מתחת לפני הקרקע, במקום שבו אין אור שמש והכללים שונים? בואו נצא למסע ונגלה בעזרת כלי המחקר שלנו!

<div class="cave-explorer-app">
    <div class="cave-representation">
        <div class="zone entrance" data-zone="entrance">אזור הכניסה</div>
        <div class="zone twilight" data-zone="twilight">אזור המעבר</div>
        <div class="zone dark" data-zone="dark">האזור העמוק</div>
        <div class="selected-zone-indicator">🌍 לחצו על אזור במערה כדי להתחיל</div>
        <div class="cave-background-animation"></div>
    </div>
    <div class="controls">
        <h2>🔬 בחרו כלי חקר</h2>
        <p class="controls-instruction">בחרו אזור במערה, ואז בחרו כלי כדי לבצע מדידה או סקר.</p>
        <button class="tool-button" data-tool="temperature_humidity" disabled>🌡️ טמפרטורה ולחות</button>
        <button class="tool-button" data-tool="light" disabled>☀️ עוצמת אור</button>
        <button class="tool-button" data-tool="co2" disabled>☁️ רמת פחמן דו-חמצני</button>
        <button class="tool-button" data-tool="organic_matter" disabled>🍂 חומר אורגני</button>
        <button class="tool-button" data-tool="organisms" disabled>🐜 סקר אורגניזמים</button>
    </div>
    <div class="results">
        <h2>📊 ממצאי המחקר</h2>
        <div id="results-display">
            <div class="initial-message">בחרו אזור וכלי מחקר כדי לראות ממצאים.</div>
        </div>
    </div>
</div>

<button id="toggle-explanation" class="explanation-toggle-button">💡 הצגת הסבר על אקולוגיה של מערות</button>

<div id="explanation" style="display: none;">
    <h2>הסבר: חקר מערכות אקולוגיות תת-קרקעיות</h2>

    <h3>מה הופך מערכת אקולוגית במערה למיוחדת?</h3>
    מערות הן סביבות קיצון שנבדלות מהותית מבתי גידול מעל פני השטח. הן מציעות תנאים יציבים יחסית (טמפרטורה ולחות כמעט קבועות באזורים הפנימיים), חושך מוחלט (בעומק), אוורור מוגבל, ולרוב מחסור במזון המיוצר במקום (תלות במקורות חיצוניים). תנאים אלו אילצו את החיים במערות לפתח התאמות יוצאות דופן.

    <h3>האזורים השונים במערה (Zonação):</h3>
    חלוקה מקובלת של המערה לאזורים לפי תנאי הסביבה, בעיקר אור:
    <ul>
        <li>**אזור הכניסה (Entrance Zone):** החלק הקרוב לפתח, מושפע ישירות מהסביבה החיצונית (אור, טמפרטורה, רוח, גשם). תמצאו בו אורגניזמים שחיים גם בחוץ (Trogloxenes) ואחרים שיכולים לחיות בשני המקומות (Troglophiles).</li>
        <li>**אזור המעבר (Twilight Zone):** אזור דמדומים, בו האור הטבעי נחלש אך עדיין קיים. השפעת תנאי החוץ פוחתת, והתנאים הופכים יציבים יותר. מאוכלס בעיקר ב-Troglophiles.</li>
        <li>**האזור העמוק (Dark Zone):** ליבת המערה, שרויה בחושך מוחלט. התנאים הסביבתיים (טמפרטורה, לחות) יציבים כמעט לחלוטין. זהו ביתם של ה-Troglobites - מינים שמותאמים רק לחיים במערות.</li>
    </ul>

    <h3>מאפיינים סביבתיים בכל אזור:</h3>
    <ul>
        <li>**תנאי אור:** ירידה חדה בכמות האור מכניסת המערה ופנימה, עד לאפס אור באזור העמוק.</li>
        <li>**טמפרטורה ולחות:** תנודתיות גבוהה באזור הכניסה, ויציבות גוברת ככל שמעמיקים. באזור העמוק, הטמפרטורה קבועה (שווה לטמפרטורת הסלע הממוצעת השנתית באזור) והלחות קרובה ל-100%.</li>
        <li>**אוורור:** זרימת אוויר חופשית בכניסה, אוורור מוגבל בעומק, מה שעלול לגרום להצטברות גזים כמו פחמן דו-חמצני.</li>
        <li>**זמינות מזון:** מקורות המזון מגיעים בעיקר מבחוץ. בכניסה יש יותר חומר אורגני נסחף; בעומק המזון מוגבל, מבוסס על גואנו (צואת עטלפים), שורשים שחודרים, או ייצור ראשוני כימוסינתטי נדיר.</li>
    </ul>

    <h3>קבוצות אורגניזמים והתאמות לחיים במערות:</h3>
    <ul>
        <li>**טרוגלוקסנים (Trogloxenes):** "אורחים" במערה. משתמשים בה למחסה, לינה או רבייה (כמו עטלפים), אך יוצאים ממנה כדי למצוא מזון ולמעשה חיים את רוב חייהם בחוץ.</li>
        <li>**טרוגלופילים (Troglophiles):** "אוהבי מערות". יכולים לחיות ולהתרבות הן בתוך המערה והן מחוצה לה, אך מעדיפים את התנאים היציבים יותר בפנים. דוגמה: חרקים מסוימים, עכבישים.</li>
        <li>**טרוגלובייטים (Troglobites):** "שומיני מערות" אמיתיים. מותאמים באופן ייחודי לחיים אך ורק בסביבת המערה ואינם מסוגלים לשרוד מחוצה לה. בעלי התאמות כמו איבוד פיגמנטציה (הם לרוב לבנים), ניוון או היעדר עיניים (הם עיוורים), הגברת חוש המישוש והריח, קצב מטבולי איטי. מדובר לרוב בחסרי חוליות כמו סרטנאים, דגים חסרי עיניים, או חרקים.</li>
    </ul>

    <h3>דפוסי שינוי והמגוון לאורך המערה:</h3>
    ככל שמתקדמים לתוך המערה, התנאים הסביבתיים משתנים באופן הדרגתי (גרדיאנט). שינויים אלו משפיעים על סוגי וצפיפות האורגניזמים. אזור הכניסה עשוי להיות עשיר במינים רבים, אזור המעבר בעל מגוון מופחת יותר, והאזור העמוק מכיל אולי פחות מינים בסך הכל, אך הם יהיו ייחודיים, נדירים ולעיתים אנדמיים (נמצאים רק שם).

    <h3>חשיבות חקר מערות:</h3>
    מערות הן כמו "איים אקולוגיים" תת-קרקעיים, עם מגוון ביולוגי נדיר ובסיכון. חקרן עוזר לנו להבין עקרונות יסוד באקולוגיה בתנאים קיצוניים, לשמש כאינדיקטור לזיהום או שינויים סביבתיים, והוא קריטי למאמצי שימור של בתי גידול ייחודיים אלו.

    <h3>טכניקות וכלים מודרניים לחקר מערות:</h3>
    כיום משתמשים בטכנולוגיות כמו חיישנים מתוחכמים לניטור סביבתי לטווח ארוך, כלים לדיגום עדין שאינו פוגע בסביבה הרגישה, ניתוח DNA סביבתי (eDNA) מטיפות מים או אדמה כדי לזהות מינים, וסימולציות אינטראקטיביות כמו זו שבניתם, כדי לאסוף מידע מדויק ולהבין טוב יותר את הקשרים המורכבים במערכות אקולוגיות מרתקות אלו.
</div>

<script>
    const zones = document.querySelectorAll('.zone');
    const toolButtons = document.querySelectorAll('.tool-button');
    const resultsDisplay = document.getElementById('results-display');
    const selectedZoneIndicator = document.querySelector('.selected-zone-indicator');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const initialMessage = resultsDisplay.querySelector('.initial-message');

    let selectedZone = null;

    // Enhanced Data Structure with Icons and better phrasing
    const data = {
        entrance: {
            temperature_humidity: { icon: '🌡️', title: 'טמפרטורה ולחות', results: { temp: 'משתנה מאוד (מושפע מתנאי חוץ)', humidity: 'משתנה מאוד (מושפע מתנאי חוץ)' } },
            light: { icon: '☀️', title: 'עוצמת אור', results: { level: 'גבוהה (אור שמש ישיר / חלקי)' } },
            co2: { icon: '☁️', title: 'רמת פחמן דו-חמצני', results: { level: 'נמוכה (אוורור טבעי טוב)' } },
            organic_matter: { icon: '🍂', title: 'חומר אורגני', results: { presence: 'גבוהה (שיירים צמחיים, עלים, נסחף פנימה)', source: 'מקור עיקרי: פני השטח' } },
            organisms: { icon: '🐜', title: 'סקר אורגניזמים', results: { list: ['עטלפים (לינה זמנית)', 'עכבישים נפוצים', 'חרקים (חיפוש מזון)', 'חולייתנים קטנים (עכברים, זוחלים)', 'צמחים (קרוב לפתח)', 'פרוקי רגליים Troglophiles'] } }
        },
        twilight: {
            temperature_humidity: { icon: '🌡️', title: 'טמפרטורה ולחות', results: { temp: 'יציבה יחסית (פחות תלות בחוץ)', humidity: 'גבוהה ויציבה יחסית' } },
            light: { icon: '☀️', title: 'עוצמת אור', results: { level: 'נמוכה מאוד (אור מעומעם)' } },
            co2: { icon: '☁️', title: 'רמת פחמן דו-חמצני', results: { level: 'בינונית (אוורור מוגבל יותר)' } },
            organic_matter: { icon: '🍂', title: 'חומר אורגני', results: { presence: 'בינונית (גואנו עטלפים, חומר נסחף)', source: 'מקורות: עטלפים, נסחפים מבחוץ' } },
            organisms: { icon: '🐜', title: 'סקר אורגניזמים', results: { list: ['Troglophiles (עכבישים, חרקים)', 'דו-חיים מסוימים', 'עטלפים (מעבר / לינה)', 'חסרי חוליות קטנים'] } }
        },
        dark: {
            temperature_humidity: { icon: '🌡️', title: 'טמפרטורה ולחות', results: { temp: 'יציבה מאוד (קרובה לטמפ\' הסלע)', humidity: 'קרובה ל-100% ויציבה מאוד' } },
            light: { icon: '☀️', title: 'עוצמת אור', results: { level: 'אפסית (חושך מוחלט)' } },
            co2: { icon: '☁️', title: 'רמת פחמן דו-חמצני', results: { level: 'גבוהה יחסית (אוורור ירוד)' } },
            organic_matter: { icon: '🍂', title: 'חומר אורגני', results: { presence: 'נמוכה (גואנו, בקטריות כימוסינתטיות נדירות)', source: 'מקורות: גואנו עטלפים, יצרנים כימוסינתטיים (נדיר)' } },
            organisms: { list: ['Troglobites (חסרי חוליות עיוורים ולבנים: סרטנאים, חרקים)', 'בקטריות ופטריות', 'עכבישים Troglophile (מעטים)', 'מגוון מינים נמוך אך ייחודי ביותר.'], icon: '🐜', title: 'סקר אורגניזמים' }
        }
    };

    // Add event listeners to zones
    zones.forEach(zone => {
        zone.addEventListener('click', () => {
            // Deselect previously selected zone
            if (selectedZone) {
                document.querySelector(`.zone.${selectedZone}`).classList.remove('selected');
            }

            // Select new zone and update indicator
            selectedZone = zone.dataset.zone;
            zone.classList.add('selected');
            selectedZoneIndicator.textContent = `🗺️ נבחר אזור: ${zone.textContent}`;
            selectedZoneIndicator.classList.add('pulsing'); // Add pulse animation
             setTimeout(() => selectedZoneIndicator.classList.remove('pulsing'), 1000); // Remove pulse after 1s

            // Enable tool buttons with a slight delay and animation
            toolButtons.forEach(button => {
                 button.classList.remove('tool-enabled-animation'); // Reset animation
                 button.disabled = true; // Disable temporarily
            });
            setTimeout(() => {
                 toolButtons.forEach(button => {
                     button.disabled = false;
                     button.classList.add('tool-enabled-animation');
                 });
            }, 300); // Delay enables after zone selection highlight

            // Clear results area and show instruction
            resultsDisplay.innerHTML = '<div class="instruction-message">✅ בחרו כלי חקר לבדיקת אזור זה.</div>';
        });
    });

    // Add event listeners to tool buttons
    toolButtons.forEach(button => {
        button.addEventListener('click', () => {
            if (!selectedZone) {
                resultsDisplay.innerHTML = '<div class="error-message">🚨 אנא בחר תחילה אזור במערה!</div>';
                return;
            }

            // Disable tools during "scan"
            toolButtons.forEach(btn => btn.disabled = true);

            const tool = button.dataset.tool;
            const zoneData = data[selectedZone][tool];
            const zoneName = document.querySelector(`.zone.${selectedZone}`).textContent;

            // Simulate scanning/measuring process
            resultsDisplay.innerHTML = `<div class="scanning-message">📡 מפעיל ${button.textContent} באזור ${zoneName}... אנא המתן...</div>`;
            resultsDisplay.classList.add('scanning'); // Add scanning visual effect

            setTimeout(() => {
                resultsDisplay.classList.remove('scanning');

                let resultHtml = `<h3>${zoneData.icon} ממצאי ${zoneData.title} ב${zoneName}:</h3>`;

                if (tool === 'temperature_humidity') {
                    resultHtml += `<p><strong>טמפרטורה:</strong> ${zoneData.results.temp}</p>`;
                    resultHtml += `<p><strong>לחות:</strong> ${zoneData.results.humidity}</p>`;
                } else if (tool === 'light') {
                    resultHtml += `<p><strong>עוצמת אור:</strong> ${zoneData.results.level}</p>`;
                } else if (tool === 'co2') {
                    resultHtml += `<p><strong>רמת CO2:</strong> ${zoneData.results.level}</p>`;
                } else if (tool === 'organic_matter') {
                    resultHtml += `<p><strong>נוכחות חומר אורגני:</strong> ${zoneData.results.presence}</p>`;
                    resultHtml += `<p><strong>מקור עיקרי:</strong> ${zoneData.results.source}</p>`;
                } else if (tool === 'organisms') {
                    resultHtml += `<p><strong>אורגניזמים אופייניים שנצפו:</strong></p><ul>`;
                    zoneData.results.list.forEach(org => {
                         resultHtml += `<li>${org}</li>`;
                    });
                    resultHtml += `</ul>`;
                }

                // Display results with fade-in animation
                resultsDisplay.innerHTML = `<div class="results-content">${resultHtml}</div>`;
                resultsDisplay.querySelector('.results-content').style.animation = 'fadeIn 0.5s ease-out';

                // Re-enable tools
                toolButtons.forEach(btn => btn.disabled = false);

            }, 1500); // Simulate 1.5 seconds of scanning
        });
    });

    // Toggle explanation visibility
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'סגירת הסבר' : '💡 הצגת הסבר על אקולוגיה של מערות';
         toggleExplanationButton.classList.toggle('active', isHidden);
    });

    // Initial state setup
    resultsDisplay.innerHTML = '<div class="initial-message">בחרו אזור וכלי מחקר כדי לראות ממצאים.</div>';

</script>

<style>
    /* General container styling */
    .cave-explorer-app {
        font-family: 'Arial', sans-serif;
        direction: rtl;
        display: flex;
        flex-wrap: wrap;
        gap: 25px; /* Increased gap */
        max-width: 1000px; /* Increased max width */
        margin: 30px auto; /* Increased margin */
        padding: 25px; /* Increased padding */
        border: 1px solid #444; /* Darker border */
        border-radius: 12px; /* More rounded corners */
        background: linear-gradient(to bottom right, #1c1c1c, #333333); /* Darker, richer background */
        color: #e0e0e0; /* Light gray text */
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3); /* More prominent shadow */
    }

    /* Cave representation styling */
    .cave-representation {
        flex: 2;
        min-width: 320px; /* Increased min width */
        background: radial-gradient(ellipse at bottom, #2e1b0f 0%, #1a0f07 60%, #0f0704 100%); /* More realistic cave gradient */
        border-radius: 12px; /* Consistent rounded corners */
        padding: 25px; /* Increased padding */
        display: flex;
        flex-direction: column;
        gap: 15px; /* Increased gap between zones */
        position: relative;
        min-height: 300px; /* Increased min height */
        justify-content: space-around;
        overflow: hidden; /* Hide pseudo-element overflow */
        border: 1px solid #5a3a22; /* Border to match cave colors */
        box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.5); /* Inner shadow for depth */
    }

     /* Subtle background animation for the cave */
    .cave-representation::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle, rgba(46, 27, 15, 0.1) 0%, rgba(26, 15, 7, 0.2) 50%, rgba(15, 7, 4, 0.3) 100%);
        animation: cavePulse 15s infinite alternate ease-in-out;
        pointer-events: none; /* Allow clicks on zones */
    }

     @keyframes cavePulse {
        0% { opacity: 0.8; }
        100% { opacity: 1; }
    }


    /* Zone styling */
    .zone {
        background-color: rgba(255, 255, 255, 0.08); /* More subtle initial background */
        border: 2px solid rgba(255, 255, 255, 0.1); /* Subtle border */
        padding: 12px; /* Increased padding */
        text-align: center;
        cursor: pointer;
        border-radius: 8px; /* Slightly more rounded */
        color: #ffffff; /* White text for contrast */
        font-weight: bold;
        transition: background-color 0.3s ease-in-out, border-color 0.3s ease-in-out, transform 0.2s ease-out;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.3); /* Text shadow for readability */
        position: relative; /* Needed for potential future effects */
    }

    .zone:hover {
        background-color: rgba(255, 255, 255, 0.15); /* More prominent hover */
        border-color: rgba(255, 255, 255, 0.3);
        transform: translateY(-3px); /* Slight lift effect */
    }

    .zone.selected {
        border-color: #4CAF50; /* Green highlight for selected */
        background-color: rgba(76, 175, 80, 0.3); /* Greenish background */
        box-shadow: 0 0 10px rgba(76, 175, 80, 0.5); /* Glow effect */
        transform: scale(1.03); /* Slight scale up */
    }

    /* Specific zone colors (subtle difference) */
    .zone.entrance { background-color: rgba(255, 255, 255, 0.1); }
    .zone.twilight { background-color: rgba(255, 255, 255, 0.08); }
    .zone.dark { background-color: rgba(255, 255, 255, 0.05); }

    /* Selected zone indicator */
    .selected-zone-indicator {
        position: absolute;
        top: 15px; /* Adjusted */
        left: 15px; /* Adjusted for RTL */
        right: auto;
        background-color: rgba(76, 175, 80, 0.9); /* Darker green, more opaque */
        color: white;
        padding: 6px 12px; /* Increased padding */
        border-radius: 6px; /* Slightly more rounded */
        font-size: 0.95em; /* Slightly larger font */
        font-weight: normal;
        z-index: 10; /* Ensure it's on top */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }

     /* Pulse animation for indicator */
    .selected-zone-indicator.pulsing {
        animation: pulse 1s ease-out;
    }

    @keyframes pulse {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.05); opacity: 0.9; }
        100% { transform: scale(1); opacity: 1; }
    }


    /* Controls and Results panels */
    .controls, .results {
        flex: 1;
        min-width: 280px; /* Adjusted min width */
        padding: 20px; /* Increased padding */
        border: 1px solid #444; /* Darker border */
        border-radius: 12px; /* Consistent rounded corners */
        background-color: #2a2a2a; /* Darker background */
        color: #e0e0e0; /* Light gray text */
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2); /* Subtle shadow */
    }

    .results {
        flex: 2; /* Results panel can be wider */
        min-width: 320px; /* Increased min width */
    }

    .controls h2, .results h2 {
        margin-top: 0;
        color: #66bb6a; /* Greenish title color */
        font-size: 1.3em; /* Slightly larger font */
        border-bottom: 1px solid #444; /* Separator line */
        padding-bottom: 8px;
        margin-bottom: 15px;
    }

     .controls-instruction {
         font-size: 0.9em;
         color: #bbbbbb; /* Lighter gray for instructions */
         margin-bottom: 20px; /* More space */
     }


    /* Tool button styling */
    .tool-button {
        display: flex; /* Use flex for icon and text */
        align-items: center; /* Vertically align */
        justify-content: center; /* Center content */
        width: 100%;
        padding: 12px; /* Increased padding */
        margin-bottom: 10px;
        background-color: #555; /* Darker grey */
        color: white;
        border: none;
        border-radius: 8px; /* Consistent rounded corners */
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.3s ease-in-out, transform 0.2s ease-out, box-shadow 0.2s ease-out;
        gap: 8px; /* Space between icon and text */
    }

     .tool-button span {
         font-size: 1.2em; /* Make icon slightly larger */
     }

    .tool-button:hover:not(:disabled) {
        background-color: #666; /* Lighter hover */
        transform: translateY(-2px); /* Lift effect on hover */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    }

    .tool-button:disabled {
        background-color: #444; /* Darker disabled */
        color: #888; /* Grayed out text */
        cursor: not-allowed;
        transform: none;
        box-shadow: none;
    }

    /* Animation for tool buttons when enabled */
     .tool-enabled-animation {
        animation: popIn 0.3s ease-out forwards;
     }

     @keyframes popIn {
        0% { transform: scale(0.8); opacity: 0; }
        100% { transform: scale(1); opacity: 1; }
     }


    /* Results display area */
    #results-display {
        margin-top: 15px;
        padding: 15px; /* Increased padding */
        border: 1px dashed #66bb6a; /* Dashed border matching highlight */
        min-height: 150px; /* Increased min height */
        background-color: #3a3a3a; /* Slightly lighter dark background */
        border-radius: 8px; /* Consistent rounded corners */
        font-size: 0.95em; /* Slightly larger text */
        color: #e0e0e0; /* Light gray text */
        position: relative; /* Needed for absolute positioning inside */
        overflow: hidden; /* For scanning effect */
    }

     /* Initial message styling */
     #results-display .initial-message,
     #results-display .instruction-message,
     #results-display .error-message,
     #results-display .scanning-message {
         text-align: center;
         color: #bbbbbb; /* Lighter gray */
         padding: 20px;
         font-style: italic;
     }

     #results-display .error-message {
         color: #ff6b6b; /* Red for error */
     }

    /* Scanning animation effect */
    #results-display.scanning {
        opacity: 0.8;
        background: linear-gradient(45deg, #3a3a3a 25%, #4a4a4a 50%, #3a3a3a 75%);
        background-size: 200% 200%;
        animation: scanning 1.5s linear infinite;
    }

    @keyframes scanning {
        0% { background-position: 100% 0; }
        100% { background-position: -100% 0; }
    }


    #results-display h3 {
        margin-top: 0;
        color: #9ccc65; /* Lighter green for result titles */
        font-size: 1.15em; /* Slightly larger */
        margin-bottom: 10px;
         display: flex;
         align-items: center;
         gap: 8px;
    }

    #results-display p {
        margin-bottom: 8px;
        line-height: 1.5;
         color: #d0d0d0; /* Slightly darker than main text */
    }

    #results-display strong {
        color: #e0e0e0; /* Whiteish for emphasis */
    }

    #results-display ul {
        padding-right: 25px; /* Adjust padding for RTL list */
        margin-top: 10px;
        list-style: disc;
        color: #d0d0d0;
    }

     #results-display li {
        margin-bottom: 6px;
         line-height: 1.5;
     }

     /* Results content fade-in animation */
     @keyframes fadeIn {
         from { opacity: 0; }
         to { opacity: 1; }
     }

    /* Explanation toggle button */
    .explanation-toggle-button {
        display: block;
        width: fit-content;
        margin: 30px auto; /* Centered, increased margin */
        padding: 12px 25px; /* Increased padding */
        background-color: #0288d1; /* Blue color */
        color: white;
        border: none;
        border-radius: 8px; /* Consistent rounded corners */
        cursor: pointer;
        font-size: 1.1em; /* Larger font */
        transition: background-color 0.3s ease-in-out, transform 0.2s ease-out;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    .explanation-toggle-button:hover {
         background-color: #0277bd; /* Darker blue on hover */
         transform: translateY(-2px); /* Lift effect */
    }

     .explanation-toggle-button.active {
         background-color: #d32f2f; /* Red when active (showing explanation) */
     }
      .explanation-toggle-button.active:hover {
         background-color: #c62828; /* Darker red */
      }


    /* Explanation section styling */
    #explanation {
        margin: 30px auto;
        max-width: 1000px; /* Consistent with app width */
        padding: 25px;
        border: 1px solid #444;
        border-radius: 12px;
        background-color: #2a2a2a; /* Consistent dark background */
        color: #e0e0e0; /* Consistent text color */
        direction: rtl;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        line-height: 1.7; /* Improved readability */
    }

    #explanation h2, #explanation h3 {
        color: #66bb6a; /* Consistent title color */
        margin-bottom: 12px;
         line-height: 1.4;
    }

    #explanation h2 {
        border-bottom: 1px solid #444; /* Consistent separator */
        padding-bottom: 10px;
        margin-bottom: 20px;
        font-size: 1.4em;
    }

    #explanation h3 {
         margin-top: 25px; /* More space above subheadings */
         color: #9ccc65; /* Lighter green */
         font-size: 1.2em;
    }

    #explanation p, #explanation ul {
        margin-bottom: 15px;
        color: #d0d0d0;
    }

    #explanation ul {
        padding-right: 30px; /* Adjust padding for RTL lists */
        list-style: disc;
    }

     #explanation li {
        margin-bottom: 8px;
     }

     #explanation strong {
         color: #e0e0e0;
     }


     /* Responsive adjustments */
    @media (max-width: 768px) {
        .cave-explorer-app {
            flex-direction: column;
            gap: 20px;
            padding: 20px;
            margin: 20px auto;
        }

        .cave-representation, .controls, .results {
            flex: none;
            width: 100%;
            min-width: auto;
             padding: 20px;
             min-height: auto; /* Allow height to be determined by content */
        }
         .cave-representation {
             height: 250px; /* Fixed height still good for visual */
             justify-content: space-between; /* Spread out zones */
         }
         .zone {
             padding: 10px;
             font-size: 0.9em;
         }
         .selected-zone-indicator {
            font-size: 0.85em;
            top: 10px;
            left: 10px; /* Adjusted for RTL */
         }
        .controls h2, .results h2 {
            font-size: 1.2em;
            margin-bottom: 10px;
        }
        .controls-instruction {
            margin-bottom: 15px;
        }
         .tool-button {
             font-size: 0.95em;
             padding: 10px;
         }
        #results-display {
            min-height: 120px;
            padding: 12px;
        }
         #results-display h3 {
             font-size: 1.1em;
             margin-bottom: 8px;
         }
        .explanation-toggle-button {
             font-size: 1em;
             padding: 10px 20px;
             margin: 20px auto;
         }
         #explanation {
             padding: 20px;
             margin: 20px auto;
         }
         #explanation h2 {
            font-size: 1.3em;
             margin-bottom: 15px;
         }
         #explanation h3 {
            font-size: 1.1em;
             margin-top: 20px;
         }
         #explanation p, #explanation li {
             font-size: 0.95em;
         }
    }
</style>