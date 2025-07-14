---
title: "על חודו של קילוואט: לנהל רשת חשמל בשיא הצריכה"
english_slug: peak-power-grid-management-game
category: "טכנולוגיה / הנדסה"
tags: ["רשת חשמל", "ניהול אנרגיה", "שיא צריכה", "תפעול מערכות", "משאבים"]
---
<h1>על חודו של קילוואט: קרב על רשת החשמל</h1>

<p class="game-intro">הקיץ בשיאו, שיא עומס היסטורי לפנינו, והרשת העירונית על סף קריסה. מי תקבל חשמל ומי תישאר בחושך? העיניים נשואות אליך, מנהל/ת הרשת. ההחלטות הקשות בידיים שלך.</p>

<div class="game-container">
    <div class="map">
        <h2>אזורי העיר</h2>
        <!-- ניתן להוסיף עוד אזורים ולמקם אותם באמצעות CSS Grid או Flexbox -->
        <div class="area residential" data-id="res-a" data-type="residential">
             <span class="area-name">מגורים א'</span>
             <span class="area-status"></span>
        </div>
        <div class="area residential" data-id="res-b" data-type="residential">
             <span class="area-name">מגורים ב'</span>
             <span class="area-status"></span>
        </div>
        <div class="area residential" data-id="res-c" data-type="residential">
             <span class="area-name">מגורים ג'</span>
             <span class="area-status"></span>
        </div>
        <div class="area industrial" data-id="ind-a" data-type="industrial">
             <span class="area-name">תעשייה א'</span>
             <span class="area-status"></span>
        </div>
        <div class="area critical" data-id="hosp-a" data-type="critical">
             <span class="area-name">בית חולים</span>
             <span class="area-status"></span>
        </div>
        <div class="area critical" data-id="gov-a" data-type="critical">
             <span class="area-name">מוסדות ציבור</span>
             <span class="area-status"></span>
        </div>
    </div>
    <div class="dashboard">
        <div class="status-panel">
            <h2>מצב הרשת</h2>
            <div class="status-item">זמן: <span id="game-time">00:00</span></div>
            <div class="status-item">
                עומס: <span id="current-load" class="status-value">0</span> MW / קיבולת מקס': <span id="max-capacity" class="status-value">0</span> MW
            </div>
            <div class="meter">
                <div class="load-bar"></div>
            </div>
            <div class="status-item stress-level">לחץ רשת מצטבר: <span id="network-stress" class="status-value">0</span> / סף קריסה: <span id="critical-stress-level" class="status-value">0</span></div>
        </div>
        <div class="controls-panel">
            <h2>פקודות פעולה</h2>
            <button id="ask-public-btn" class="action-btn">קרא לציבור לחסוך (השפעה עדינה)</button>
            <button id="reduce-industrial-btn" class="action-btn">הפחת עומס בתעשייה (השפעה חזקה)</button>
            <p class="control-label">בחר אזור במפה לניתוק יזום:</p>
            <div id="selected-area-info" class="selected-info">בחר אזור במפה</div>
            <button id="cut-power-btn" class="action-btn" disabled>נתק חשמל לאזור הנבחר</button>
        </div>
        <div class="message-panel">
            <h2>עדכוני חמ"ל</h2>
            <div id="game-messages"></div>
        </div>
    </div>
</div>

<button id="toggle-explanation" class="toggle-btn">הצג/הסתר הסבר על רשת החשמל</button>

<div id="explanation" style="display: none;">
    <h2>הסבר: ניהול רשת חשמל בחירום</h2>

    <h3>מבנה בסיסי של רשת חשמל עירונית</h3>
    <p>רשת חשמל מודרנית מורכבת מכמה מרכיבים עיקריים:
    <ul>
        <li><strong>מקורות ייצור:</strong> תחנות כוח שמייצרות חשמל.</li>
        <li><strong>מערכת הולכה וחלוקה:</strong> רשת כבלים ותחנות שנאה המובילות את החשמל לצרכנים.</li>
        <li><strong>צרכנים:</strong> אנחנו, המשתמשים הסופיים (בתים, עסקים, מוסדות).</li>
    </ul>
    מנהל הרשת מפקח על זרימת החשמל, מבטיח איזון בין ייצור לצריכה בכל רגע נתון ושומר על יציבות המערכת.</p>

    <h3>מהו "שיא צריכה" ומדוע הוא מסוכן?</h3>
    <p>שיא צריכה הוא רגע או תקופה בה הביקוש לחשמל מרקיע שחקים (למשל, בימים חמים במיוחד עקב שימוש מסיבי במזגנים). רשת החשמל מוגבלת בקיבולתה. עומס יתר עלול לגרום לחימום יתר של ציוד, תקלות אוטומטיות, ואף לקריסה רחבת היקף (Blackout) שתותיר חלקים גדולים מהעיר או מהמדינה בחושך, עם נזק משמעותי לציוד ותשתיות.</p>

    <h3>כלים לניהול עומסים בזמן משבר (Demand Side Management)</h3>
    <p>כדי למנוע קריסה, מנהל הרשת חייב להפחית את הביקוש באופן יזום:</p>
    <ul>
        <li><strong>קריאה לחיסכון:</strong> בקשה מהציבור או מהעסקים להפחית בצריכה. זו הדרך העדינה ביותר, אך יעילותה תלויה בהיענות ואינה תמיד מספקת מול עומס כבד.</li>
        <li><strong>הפסקות חשמל יזומות (ניתוקי עומס):</strong> ניתוק מבוקר של אזורים מסוימים מהרשת. זהו כלי כואב אך לעיתים הכרחי למניעת קריסה כוללת. יש לתעדף אזורים קריטיים ולהימנע מניתוקם ככל הניתן.</li>
        <li><strong>הפחתת צריכה ממוקדת:</strong> הסכמים עם צרכנים גדולים (כמו מפעלי תעשייה) להפחתת צריכה מיידית בתמורה לתמריץ.</li>
    </ul>
    ניהול משבר אנרגיה דורש שיקול דעת בין הצורך ביציבות הרשת לבין הפגיעה בצרכנים ובכלכלה. אזורים קריטיים (בתי חולים, תשתיות חיוניות) דורשים הגנה מיוחדת.

    <h3>העתיד: רשתות חכמות (Smart Grids)</h3>
    <p>טכנולוגיות מתקדמות כמו מונים חכמים, אוטומציה ותקשורת דו-כיוונית עם הצרכנים מאפשרות ניהול יעיל ומדויק יותר של הרשת, ניטור תקלות בזמן אמת, ניהול ביקוש אוטומטי ושילוב טוב יותר של אנרגיות מתחדשות, במטרה להגביר את אמינות הרשת ולהפחית את הצורך בניתוקים.</p>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@400;700&display=swap');

    body {
        font-family: 'Heebo', sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f4f7f6;
        margin: 0;
        padding: 20px;
        direction: rtl;
    }

    h1, h2, h3 {
        color: #2c3e50;
        text-align: center;
        margin-bottom: 15px;
    }

    h1 {
        color: #e74c3c; /* A more alarming color for the crisis title */
        margin-top: 0;
        font-size: 2.2em;
    }

     .game-intro {
         text-align: center;
         margin-bottom: 30px;
         font-size: 1.1em;
         color: #555;
     }


    .game-container {
        display: flex;
        flex-wrap: wrap; /* Allow wrapping on small screens */
        gap: 25px;
        max-width: 1000px;
        margin: 20px auto;
        border: 1px solid #bdc3c7;
        padding: 25px;
        border-radius: 12px;
        background-color: #ffffff;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    }

    .map {
        flex: 1;
        min-width: 300px; /* Ensure map is not too small */
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
        gap: 15px;
        border: 1px solid #dcdcdc;
        padding: 20px;
        border-radius: 8px;
        background-color: #ecf0f1;
        box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.05);
    }

    .map h2 {
        grid-column: 1 / -1;
        margin-top: 0;
        margin-bottom: 20px;
        color: #34495e;
    }

    .area {
        background-color: #d4efc8; /* Light greenish */
        border: 2px solid #8bc34a; /* Green */
        border-radius: 8px;
        padding: 15px 10px;
        text-align: center;
        cursor: pointer;
        transition: background-color 0.3s ease, border-color 0.3s ease, transform 0.1s ease, opacity 0.3s ease;
        font-size: 0.95em;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 70px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.08);
        font-weight: bold;
    }

    .area:hover:not(.blackout):not(.selected) {
        background-color: #b2e0a6;
        border-color: #7cb342;
        transform: translateY(-3px);
    }

    .area.selected {
        border-color: #3498db; /* Blue */
        box-shadow: 0 0 12px rgba(52, 152, 219, 0.6);
        background-color: #e1f5fe; /* Light blue */
        transform: scale(1.05);
    }

    .area.blackout {
        background-color: #ffcdd2; /* Light red */
        border-color: #e57373; /* Red */
        color: #c0392b; /* Dark red text */
        cursor: not-allowed;
        opacity: 0.7;
        box-shadow: none;
        font-weight: normal;
        text-decoration: none; /* Remove line-through for better look with timer */
    }
    .area.blackout .area-status {
         font-size: 0.8em;
         margin-top: 5px;
         font-weight: bold;
    }

    .area.critical {
        background-color: #fff9c4; /* Light yellow */
        border-color: #fbc02d; /* Yellow */
        font-weight: bold;
    }
    .area.critical.selected {
         border-color: #3498db; /* Blue */
         box-shadow: 0 0 12px rgba(52, 152, 219, 0.6);
         background-color: #e1f5fe; /* Light blue */
         transform: scale(1.05);
    }
    .area.critical.blackout { /* Should not happen based on JS, but for safety */
         background-color: #ef9a9a; /* Medium red */
         border-color: #d32f2f; /* Darker red */
         color: #c0392b;
    }


    .dashboard {
        flex: 1.2;
        min-width: 300px; /* Ensure dashboard is not too small */
        display: flex;
        flex-direction: column;
        gap: 20px;
    }

    .status-panel, .controls-panel, .message-panel {
        border: 1px solid #dcdcdc;
        padding: 20px;
        border-radius: 8px;
        background-color: #ffffff;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.08);
    }

    .status-panel h2, .controls-panel h2, .message-panel h2 {
        margin-top: 0;
        color: #34495e;
        border-bottom: 1px solid #ecf0f1;
        padding-bottom: 10px;
        margin-bottom: 15px;
        text-align: right; /* Align headers to the right in RTL */
    }
     .status-panel h2::after, .controls-panel h2::after, .message-panel h2::after {
         content: '';
         display: block;
         width: 50px; /* Small underline effect */
         height: 3px;
         background-color: #3498db;
         margin-top: 5px;
         margin-right: 0; /* Align underline to the right */
     }


    .status-item {
        margin-bottom: 10px;
        font-size: 1em;
        display: flex;
        justify-content: space-between; /* Space out label and value */
        align-items: center;
    }

    .status-item .status-value {
        font-weight: bold;
        color: #2c3e50;
    }

    .stress-level .status-value {
         color: #e74c3c; /* Red for stress */
    }

    .meter {
        width: 100%;
        height: 30px;
        background-color: #ecf0f1;
        border-radius: 4px;
        overflow: hidden;
        margin-top: 10px;
        border: 1px solid #bdc3c7;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
    }

    .load-bar {
        height: 100%;
        width: 0%;
        background-color: #2ecc71; /* Green */
        transition: width 0.5s ease-in-out, background-color 0.5s ease-in-out;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white; /* Text color for percentage inside bar */
        font-size: 0.9em;
        font-weight: bold;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }

    /* Load bar color changes */
    .load-bar.low { background-color: #2ecc71; } /* Green */
    .load-bar.medium { background-color: #f1c40f; } /* Yellow */
    .load-bar.high { background-color: #e67e22; } /* Orange */
    .load-bar.critical { background-color: #e74c3c; } /* Red */


    .controls-panel .control-label {
        margin-top: 15px;
        margin-bottom: 8px;
        font-size: 1em;
        color: #555;
        font-weight: bold;
    }

    .action-btn {
        display: block;
        width: 100%;
        padding: 12px;
        margin-bottom: 10px;
        background-color: #3498db; /* Blue */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.2s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        font-family: 'Heebo', sans-serif;
    }

    .action-btn:hover:not(:disabled) {
        background-color: #2980b9; /* Darker blue */
        transform: translateY(-2px);
    }
    .action-btn:active:not(:disabled) {
        transform: translateY(0);
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }

    .action-btn:disabled {
        background-color: #bdc3c7; /* Grey */
        cursor: not-allowed;
        box-shadow: none;
    }

     .selected-info {
         font-size: 0.95em;
         color: #2c3e50;
         margin-top: 5px;
         margin-bottom: 10px;
         padding: 8px;
         border: 1px dashed #3498db;
         border-radius: 4px;
         background-color: #ecf0f1;
         text-align: center;
     }

    .message-panel {
        height: 180px; /* Increased height */
        overflow-y: auto;
        background-color: #ecf0f1; /* Light background */
        font-size: 0.9em;
        padding: 15px;
    }

    .message-panel p {
        margin: 8px 0; /* Increased margin */
        padding-bottom: 8px;
        border-bottom: 1px dotted #bdc3c7; /* Softer border */
        color: #34495e;
    }
    .message-panel p:last-child {
        border-bottom: none;
    }
    .message-panel p.warning {
         color: #e67e22; /* Orange for warnings */
         font-weight: bold;
    }
     .message-panel p.error {
         color: #e74c3c; /* Red for errors */
         font-weight: bold;
     }
     .message-panel p.success {
         color: #2ecc71; /* Green for success */
     }


    .toggle-btn {
        display: block;
        width: 220px;
        margin: 30px auto; /* More space */
        padding: 12px;
        text-align: center;
        background-color: #2ecc71; /* Green */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.2s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        font-family: 'Heebo', sans-serif;
    }

    .toggle-btn:hover {
        background-color: #27ae60; /* Darker green */
        transform: translateY(-2px);
    }
     .toggle-btn:active {
         transform: translateY(0);
         box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
     }


    #explanation {
        margin: 20px auto;
        padding: 25px;
        border: 1px solid #bdc3c7;
        border-radius: 8px;
        background-color: #ffffff;
        max-width: 960px;
        direction: rtl;
        line-height: 1.7; /* More comfortable reading */
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
    }

    #explanation h2 {
        color: #34495e;
        margin-top: 0;
        margin-bottom: 20px;
        border-bottom: 1px solid #ecf0f1;
        padding-bottom: 10px;
    }
     #explanation h2::after {
         content: '';
         display: block;
         width: 50px;
         height: 3px;
         background-color: #2ecc71; /* Green underline */
         margin: 5px auto 0 auto; /* Center underline */
     }


    #explanation h3 {
        color: #34495e;
        margin-top: 20px;
        margin-bottom: 10px;
        border-bottom: 1px dotted #ecf0f1;
        padding-bottom: 5px;
    }

    #explanation p {
        margin-bottom: 15px;
        color: #555;
    }

    #explanation ul {
        margin-bottom: 15px;
        padding-right: 25px; /* Increased padding */
        color: #555;
    }

    #explanation li {
        margin-bottom: 8px; /* Increased spacing */
    }

    /* Responsive Adjustments */
    @media (max-width: 768px) {
        .game-container {
            flex-direction: column;
        }
        .map, .dashboard {
            flex: none;
            width: 100%;
        }
        .area {
             min-height: 60px;
             font-size: 0.9em;
        }
         .area-name {
             display: block; /* Ensure name and status are stacked */
         }
    }

     @keyframes pulse-red {
         0% { box-shadow: 0 0 8px rgba(231, 76, 60, 0.4); }
         50% { box-shadow: 0 0 15px rgba(231, 76, 60, 0.8); }
         100% { box-shadow: 0 0 8px rgba(231, 76, 60, 0.4); }
     }
     @keyframes pulse-yellow {
         0% { box-shadow: 0 0 8px rgba(241, 196, 15, 0.4); }
         50% { box-shadow: 0 0 15px rgba(241, 196, 15, 0.8); }
         100% { box-shadow: 0 0 8px rgba(241, 196, 15, 0.4); }
     }
     .stress-level .status-value {
          animation: none; /* Default state */
     }
     .stress-level.pulsing-yellow .status-value {
          animation: pulse-yellow 1.5s infinite ease-in-out;
     }
     .stress-level.pulsing-red .status-value {
          animation: pulse-red 1.5s infinite ease-in-out;
     }

     .game-over-overlay {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(0, 0, 0, 0.7);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000;
     }
     .game-over-modal {
         background-color: #ffffff;
         padding: 40px;
         border-radius: 10px;
         text-align: center;
         box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
         max-width: 400px;
         width: 90%;
     }
     .game-over-modal h2 {
         margin-top: 0;
         color: #e74c3c; /* Red for game over */
     }
     .game-over-modal p {
         font-size: 1.1em;
         margin-bottom: 20px;
         color: #555;
     }
      .game-over-modal .action-btn {
          width: auto;
          padding: 10px 25px;
          background-color: #3498db;
      }

</style>

<script>
    const gameState = {
        time: 0, // minutes
        currentLoad: 0,
        maxCapacity: 900, // MW
        networkStress: 0,
        criticalStressThreshold: 2000, // Adjusted threshold for balance
        areas: {
            'res-a': { name: 'מגורים א׳', type: 'residential', baseLoad: 150, currentLoad: 0, critical: false, blackoutTimer: 0, initialLoadFactor: 1.0 },
            'res-b': { name: 'מגורים ב׳', type: 'residential', baseLoad: 120, currentLoad: 0, critical: false, blackoutTimer: 0, initialLoadFactor: 1.1 }, // Slightly higher initial load
            'res-c': { name: 'מגורים ג׳', type: 'residential', baseLoad: 180, currentLoad: 0, critical: false, blackoutTimer: 0, initialLoadFactor: 0.9 }, // Slightly lower initial load
            'ind-a': { name: 'תעשייה א׳', type: 'industrial', baseLoad: 200, currentLoad: 0, critical: false, reductionActive: false, initialLoadFactor: 1.0 },
            'hosp-a': { name: 'בית חולים', type: 'critical', baseLoad: 80, currentLoad: 0, critical: true, blackoutTimer: 0, initialLoadFactor: 1.0 },
            'gov-a': { name: 'מוסדות ציבור', type: 'critical', baseLoad: 100, currentLoad: 0, critical: true, blackoutTimer: 0, initialLoadFactor: 1.0 },
        },
        gameDuration: 300, // 5 hours in minutes (increased duration)
        timeStep: 10, // minutes simulated per game step
        realTimeStep: 1000, // milliseconds per game step (1 second) - Faster pace
        peakTimeStart: 120, // Peak load phase starts (minutes)
        peakTimeEnd: 240, // Peak load phase ends (minutes)
        peakFactor: 2.0, // Peak load is up to 2.0x base sum
        publicSaveEffect: 0, // Reduction percentage from public saving
        publicSaveDuration: 60, // Duration of public saving effect in minutes
        publicSaveCooldown: 90, // Cooldown for public saving action in minutes (reduced cooldown)
        publicSaveTimer: 0, // Timer for public saving cooldown
        industrialReductionEffect: 0.6, // Percentage reduction for industrial (60%)
        industrialReductionDuration: 90, // Duration of industrial reduction in minutes
        industrialReductionCooldown: 150, // Cooldown for industrial reduction action in minutes (reduced cooldown)
        industrialReductionTimer: 0, // Timer for industrial reduction cooldown
        blackoutDuration: 60, // Duration of a controlled blackout in minutes (increased duration)
        stressDecayPerStep: 5, // Stress reduction per step when load is below capacity
        selectedAreaId: null,
        gameInterval: null, // To hold the interval timer
        gameEnded: false,
    };

    const elements = {
        gameTime: document.getElementById('game-time'),
        currentLoad: document.getElementById('current-load'),
        maxCapacity: document.getElementById('max-capacity'),
        loadBar: document.querySelector('.load-bar'),
        networkStress: document.getElementById('network-stress'),
        criticalStressLevel: document.getElementById('critical-stress-level'),
        askPublicBtn: document.getElementById('ask-public-btn'),
        reduceIndustrialBtn: document.getElementById('reduce-industrial-btn'),
        cutPowerBtn: document.getElementById('cut-power-btn'),
        selectedAreaInfo: document.getElementById('selected-area-info'),
        gameMessages: document.getElementById('game-messages'),
        areas: {}, // To store area elements
        statusPanel: document.querySelector('.status-panel'), // Added for stress animation
    };

    // Store area elements on load and add initial status spans
    document.querySelectorAll('.map .area').forEach(areaElement => {
        elements.areas[areaElement.dataset.id] = areaElement;
    });

    function getLoadMultiplier(time) {
        const t = time;
        const startPeak = gameState.peakTimeStart;
        const endPeak = gameState.peakTimeEnd;
        const totalDuration = gameState.gameDuration;
        const baseMultiplier = 1.0;
        const peakM = gameState.peakFactor;

        if (t < startPeak) {
            // Smooth ease-in to peak start
            const progress = t / startPeak;
            return baseMultiplier + (peakM - baseMultiplier) * Math.sin((progress * Math.PI) / 2);
        } else if (t >= startPeak && t <= endPeak) {
            // Stay at peak or fluctuate slightly (simple peak)
            return peakM; // Could add noise here: peakM + (Math.random() - 0.5) * 0.1;
        } else {
            // Smooth ease-out from peak end
            const timeAfterPeak = t - endPeak;
            const remainingTime = totalDuration - endPeak;
            const progress = timeAfterPeak / remainingTime;
             const endMultiplier = 1.1; // Still 10% above base at the end
            return peakM - (peakM - endMultiplier) * Math.sin((progress * Math.PI) / 2);
        }
    }


    function updateGame() {
        if (gameState.gameEnded) return;

        gameState.time += gameState.timeStep;

        if (gameState.time >= gameState.gameDuration) {
            endGame("win");
            return;
        }

        // Update action cooldown timers
        if (gameState.publicSaveTimer > 0) gameState.publicSaveTimer = Math.max(0, gameState.publicSaveTimer - gameState.timeStep);
        if (gameState.industrialReductionTimer > 0) gameState.industrialReductionTimer = Math.max(0, gameState.industrialReductionTimer - gameState.timeStep);

        // Update blackout timers and reset blackout status if timer runs out
        Object.keys(gameState.areas).forEach(areaId => {
            const area = gameState.areas[areaId];
            if (area.blackoutTimer > 0) {
                 area.blackoutTimer = Math.max(0, area.blackoutTimer - gameState.timeStep);
                 if (area.blackoutTimer === 0) {
                     addMessage(`אספקת החשמל חודשה באזור ${area.name}.`, 'success');
                     // If this was the selected area, deselect it
                     if (gameState.selectedAreaId === areaId) {
                          gameState.selectedAreaId = null;
                     }
                 }
            }
             // Remove industrial reduction effect if timer runs out - handled by setTimeout on button click
        });


        let totalLoad = 0;
        const loadMultiplier = getLoadMultiplier(gameState.time);

        Object.keys(gameState.areas).forEach(areaId => {
            const area = gameState.areas[areaId];

            if (area.blackoutTimer > 0) {
                 area.currentLoad = 0; // No load during blackout
            } else {
                 // Calculate load for areas NOT in blackout
                 let areaLoad = area.baseLoad * area.initialLoadFactor * loadMultiplier; // Apply initial factor and time multiplier

                 // Apply public saving effect (only to residential)
                 if (area.type === 'residential' && gameState.publicSaveEffect > 0) {
                     areaLoad *= (1 - gameState.publicSaveEffect / 100);
                 }

                 // Apply industrial reduction (only to industrial)
                 if (area.type === 'industrial' && area.reductionActive) {
                     areaLoad *= (1 - gameState.industrialReductionEffect);
                 }

                 area.currentLoad = areaLoad;
                 totalLoad += areaLoad;
            }
        });
        gameState.currentLoad = totalLoad;

        // Calculate stress
        if (gameState.currentLoad > gameState.maxCapacity) {
            const overload = gameState.currentLoad - gameState.maxCapacity;
            // Accumulate stress, faster accumulation for higher overload
            gameState.networkStress += overload * (gameState.timeStep / 60) * (1 + overload / gameState.maxCapacity); // Stress grows non-linearly with overload
            // addMessage(`אזהרה: עומס יתר! (${Math.round(gameState.currentLoad)} MW)`, 'warning'); // Only show critical warnings
        } else {
             // Stress decays slowly when load is below capacity
             gameState.networkStress = Math.max(0, gameState.networkStress - gameState.stressDecayPerStep * (gameState.timeStep / 60)); // Decay per minute
        }

         // Cap stress at critical threshold to avoid runaway numbers before game over
         gameState.networkStress = Math.min(gameState.networkStress, gameState.criticalStressThreshold + 100); // Cap slightly above threshold

        // Check for game over
        if (gameState.networkStress >= gameState.criticalStressThreshold) {
            endGame("lose", "הרשת קרסה עקב לחץ קריטי וממושך! נכשלת בניהול המשבר.");
            return;
        }

        // Update UI
        updateUI();

        // Add messages for critical situations
        if (gameState.currentLoad > gameState.maxCapacity * 1.05 && gameState.time % 60 < gameState.timeStep) { // Check every game hour if still overloaded
             addMessage(`עומס הרשת חורג משמעותית מהקיבולת! (${Math.round(gameState.currentLoad)}/${gameState.maxCapacity} MW)`, 'warning');
        }
        if (gameState.networkStress > gameState.criticalStressThreshold * 0.8 && gameState.networkStress < gameState.criticalStressThreshold && gameState.time % 60 < gameState.timeStep) { // Warning when stress is high
             addMessage(`לחץ הרשת מתקרב לסף קריסה! נדרשת פעולה מיידית.`, 'warning');
             elements.statusPanel.querySelector('.stress-level').classList.add('pulsing-yellow');
        } else if (gameState.networkStress >= gameState.criticalStressThreshold * 0.8) {
             elements.statusPanel.querySelector('.stress-level').classList.remove('pulsing-yellow');
             elements.statusPanel.querySelector('.stress-level').classList.add('pulsing-red');
        } else {
             elements.statusPanel.querySelector('.stress-level').classList.remove('pulsing-yellow', 'pulsing-red');
        }

    }

    function updateUI() {
        elements.gameTime.innerText = formatTime(gameState.time);
        elements.currentLoad.innerText = Math.round(gameState.currentLoad);
        elements.maxCapacity.innerText = gameState.maxCapacity;
        elements.networkStress.innerText = Math.round(gameState.networkStress);
        elements.criticalStressLevel.innerText = gameState.criticalStressThreshold;

        const loadPercentage = Math.min(100, (gameState.currentLoad / gameState.maxCapacity) * 100);
        elements.loadBar.style.width = loadPercentage + '%';
        elements.loadBar.innerText = `${Math.round(loadPercentage)}%`; // Display percentage

        // Update load bar color based on percentage
        elements.loadBar.classList.remove('low', 'medium', 'high', 'critical');
        if (loadPercentage > 100) {
             elements.loadBar.classList.add('critical');
        } else if (loadPercentage > 90) {
             elements.loadBar.classList.add('high');
        } else if (loadPercentage > 75) {
             elements.loadBar.classList.add('medium');
        } else {
             elements.loadBar.classList.add('low');
        }


        // Update area styles and status text
        Object.keys(gameState.areas).forEach(areaId => {
            const areaElement = elements.areas[areaId];
            const area = gameState.areas[areaId];
            const statusSpan = areaElement.querySelector('.area-status');
            const nameSpan = areaElement.querySelector('.area-name');


            areaElement.classList.remove('selected', 'blackout');
            areaElement.style.opacity = 1; // Reset opacity

            if (area.blackoutTimer > 0) {
                areaElement.classList.add('blackout');
                const remaining = Math.ceil(area.blackoutTimer / 60); // Minutes remaining
                statusSpan.innerText = `(דק' נותרו: ${remaining})`;
                 nameSpan.style.textDecoration = 'line-through';
            } else {
                 statusSpan.innerText = ''; // Clear status text
                 nameSpan.style.textDecoration = 'none';
                 if (areaId === gameState.selectedAreaId) {
                     areaElement.classList.add('selected');
                 }
            }

             // Optional: Dim industrial area when reduction is active
             if (area.type === 'industrial' && area.reductionActive && area.blackoutTimer === 0) {
                 areaElement.style.opacity = 0.8;
             }

        });

        // Update button states and text
        elements.askPublicBtn.disabled = gameState.publicSaveTimer > 0;
        elements.askPublicBtn.innerText = gameState.publicSaveTimer > 0 ? `קרא לציבור לחסוך (${Math.ceil(gameState.publicSaveTimer / 60)} דק' לקירור...)` : 'קרא לציבור לחסוך (השפעה עדינה)';

        elements.reduceIndustrialBtn.disabled = gameState.industrialReductionTimer > 0;
        elements.reduceIndustrialBtn.innerText = gameState.industrialReductionTimer > 0 ? `הפחת עומס בתעשייה (${Math.ceil(gameState.industrialReductionTimer / 60)} דק' לקירור...)` : 'הפחת עומס בתעשייה (השפעה חזקה)';

        const selectedArea = gameState.selectedAreaId ? gameState.areas[gameState.selectedAreaId] : null;
        elements.cutPowerBtn.disabled = !selectedArea || selectedArea.blackoutTimer > 0 || selectedArea.critical;
        elements.selectedAreaInfo.innerText = selectedArea ? `אזור נבחר לניתוק: ${selectedArea.name}` : 'בחר אזור במפה לניתוק';
        if (selectedArea && selectedArea.critical) {
             elements.selectedAreaInfo.innerText += " (אזור קריטי - לא ניתן לנתק)";
        } else if (selectedArea && selectedArea.blackoutTimer > 0) {
             elements.selectedAreaInfo.innerText += " (כבר מנותק)";
        }
    }

    function formatTime(minutes) {
        const h = Math.floor(minutes / 60);
        const m = minutes % 60;
        return `${String(h).padStart(2, '0')}:${String(m).padStart(2, '0')}`;
    }

    function addMessage(msg, type = 'info') {
        const messageElement = document.createElement('p');
        messageElement.innerText = `[${formatTime(gameState.time)}] ${msg}`;
        messageElement.classList.add(type); // Add class for styling
        // Add animation?
        // messageElement.style.opacity = 0;
        // setTimeout(() => { messageElement.style.opacity = 1; }, 10); // Simple fade in

        elements.gameMessages.appendChild(messageElement);
        elements.gameMessages.scrollTop = elements.gameMessages.scrollHeight; // Auto-scroll
        // Limit number of messages?
        while(elements.gameMessages.children.length > 50) {
             elements.gameMessages.removeChild(elements.gameMessages.children[0]);
        }
    }

     function showGameOverModal(isWin, message) {
         const overlay = document.createElement('div');
         overlay.classList.add('game-over-overlay');

         const modal = document.createElement('div');
         modal.classList.add('game-over-modal');

         const title = document.createElement('h2');
         title.innerText = isWin ? "משימה בוצעה בהצלחה!" : "כישלון במשימה";
         title.style.color = isWin ? '#2ecc71' : '#e74c3c';


         const msgPara = document.createElement('p');
         msgPara.innerText = message;

         const restartBtn = document.createElement('button');
         restartBtn.innerText = 'התחל סימולציה חדשה';
         restartBtn.classList.add('action-btn'); // Use existing button style
         restartBtn.onclick = () => {
             overlay.remove(); // Remove the modal
             initGame(); // Start a new game
         };
         restartBtn.style.width = 'auto'; // Override 100% width
         restartBtn.style.marginTop = '20px';


         modal.appendChild(title);
         modal.appendChild(msgPara);
         modal.appendChild(restartBtn);
         overlay.appendChild(modal);

         document.body.appendChild(overlay);
     }


    function endGame(result, message = "") {
        if (gameState.gameEnded) return; // Prevent multiple end calls
        gameState.gameEnded = true;
        clearInterval(gameState.gameInterval); // Stop the game loop

        const finalMessage = result === "win" ? "ניהלת את רשת החשמל בהצלחה לאורך כל שיא העומס הקריטי! העיר ניצלה מקריסה." : message;
        addMessage(`-- ${result === "win" ? "ניצחון!" : "המשחק הסתיים"} -- ${finalMessage}`, result);

        // Disable all buttons in the controls panel
        document.querySelectorAll('.controls-panel .action-btn').forEach(btn => btn.disabled = true);

        // Show modal after a short delay
        setTimeout(() => {
             showGameOverModal(result === "win", finalMessage);
        }, 500); // Short delay to allow final UI update and message to appear
    }

    // Event Listeners
    elements.askPublicBtn.addEventListener('click', () => {
        if (gameState.publicSaveTimer <= 0) {
            gameState.publicSaveEffect = 8; // Example: 8% reduction
            gameState.publicSaveTimer = gameState.publicSaveCooldown; // Set cooldown
            addMessage("הוצאה קריאה לציבור להפחית שימוש במכשירים עתירי אנרגיה. מקווים להיענות.", 'info');

            // Schedule effect removal
            setTimeout(() => {
                 gameState.publicSaveEffect = 0;
                 addMessage("השפעת הקריאה הציבורית לחיסכון פגה.", 'info');
                 updateUI(); // Update button text
            }, gameState.publicSaveDuration * gameState.realTimeStep / gameState.timeStep); // Convert duration from minutes (game time) to real time

             updateUI(); // Update button text immediately
        }
    });

    elements.reduceIndustrialBtn.addEventListener('click', () => {
        if (gameState.industrialReductionTimer <= 0) {
            Object.values(gameState.areas).forEach(area => {
                if (area.type === 'industrial') {
                    area.reductionActive = true;
                }
            });
            gameState.industrialReductionTimer = gameState.industrialReductionCooldown; // Set cooldown
            addMessage("הופעלו הסכמי הפחתת עומס עם מפעלי תעשייה מרכזיים.", 'info');

            // Schedule effect removal
            setTimeout(() => {
                Object.values(gameState.areas).forEach(area => {
                    if (area.type === 'industrial') {
                        area.reductionActive = false;
                    }
                });
                 addMessage("הגבלת העומס על התעשייה הוסרה.", 'info');
                 updateUI(); // Update button text
            }, gameState.industrialReductionDuration * gameState.realTimeStep / gameState.timeStep); // Convert duration from minutes (game time) to real time

            updateUI(); // Update button text immediately
        }
    });

    document.querySelectorAll('.map .area').forEach(areaElement => {
        areaElement.addEventListener('click', () => {
            const areaId = areaElement.dataset.id;
            const area = gameState.areas[areaId];

             // Cannot select if blacked out or already selected critical area
            if (area.blackoutTimer > 0) {
                 // Clicked a blacked-out area - maybe give info?
                 // addMessage(`אזור ${area.name} מנותק כעת מאספקת חשמל.`, 'info'); // Optional info message
                 gameState.selectedAreaId = null; // Ensure nothing is selected visually if clicking blacked out
            } else {
                 if (gameState.selectedAreaId === areaId) {
                     gameState.selectedAreaId = null; // Deselect if clicking the same area
                 } else {
                      // Check if selecting a critical area
                     if (area.critical) {
                         addMessage(`אזור ${area.name} הוא אזור קריטי. לא ניתן לבצע בו ניתוק יזום.`, 'error');
                         gameState.selectedAreaId = null; // Cannot select critical for cutting
                     } else {
                         gameState.selectedAreaId = areaId; // Select
                     }
                 }
            }
            updateUI(); // Update button state and visual selection
        });
    });

    elements.cutPowerBtn.addEventListener('click', () => {
        const areaId = gameState.selectedAreaId;
        const area = gameState.areas[areaId];
        // Double check conditions before cutting
        if (areaId && area && !area.critical && area.blackoutTimer <= 0) {
            area.blackoutTimer = gameState.blackoutDuration; // Set blackout duration
            // Add stress reduction for this action? Maybe based on the load removed?
            const loadRemoved = area.currentLoad; // Load *at the moment of cutting*
            const stressReduction = Math.min(gameState.networkStress, loadRemoved * (gameState.blackoutDuration / 60) * 0.5); // Example: stress relief based on load removed and blackout duration, capped at current stress
            gameState.networkStress = Math.max(0, gameState.networkStress - stressReduction);

            addMessage(`בוצע ניתוק יזום באזור ${area.name}. צפוי חיסכון בעומס למשך ${gameState.blackoutDuration} דקות.`, 'warning'); // Use warning color as it's a drastic action
            gameState.selectedAreaId = null; // Deselect after action
            updateUI();
        } else if (areaId && area && area.critical) {
            // This case is handled by select logic and button disabled state, but good to have
            addMessage(`פעולה נכשלה: לא ניתן לנתק אזור קריטי (${area.name}).`, 'error');
        } else if (areaId && area && area.blackoutTimer > 0) {
             addMessage(`פעולה נכשלה: אזור ${area.name} כבר מנותק.`, 'warning');
        } else {
            addMessage(`שגיאה: לא נבחר אזור חוקי לניתוק.`, 'error');
        }
    });


    // Explanation toggle
    document.getElementById('toggle-explanation').addEventListener('click', () => {
        const explanationDiv = document.getElementById('explanation');
        const button = document.getElementById('toggle-explanation');
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        button.innerText = isHidden ? 'הסתר הסבר על רשת החשמל' : 'הצג הסבר על רשת החשמל';
    });

    // Initialize game
    function initGame() {
        // Reset state
        gameState.time = 0;
        gameState.currentLoad = 0;
        gameState.networkStress = 0;
        gameState.publicSaveEffect = 0;
        gameState.publicSaveTimer = 0;
        gameState.industrialReductionTimer = 0;
        gameState.selectedAreaId = null;
        gameState.gameEnded = false;

        // Reset area states
        Object.values(gameState.areas).forEach(area => {
            area.currentLoad = 0; // Start with 0, will be calculated in first update
            area.blackoutTimer = 0;
            if (area.type === 'industrial') area.reductionActive = false;
            // No public opinion mechanic implemented yet, so no reset needed
        });

        // Clear messages
        elements.gameMessages.innerHTML = '';

        // Remove any existing game over modal
        const existingModal = document.querySelector('.game-over-overlay');
        if (existingModal) {
             existingModal.remove();
        }


        addMessage("ברוכים הבאים, מנהל רשת. גל החום מתחיל. נהל את העומס ומנע קריסה!", 'info');

        // Enable buttons
        document.querySelectorAll('.controls-panel .action-btn').forEach(btn => btn.disabled = false);
         elements.cutPowerBtn.disabled = true; // Cut button disabled by default until area is selected

        updateUI(); // Initial UI render

        // Clear any existing interval before starting a new one
        if (gameState.gameInterval) {
            clearInterval(gameState.gameInterval);
        }

        // Start game loop
        gameState.gameInterval = setInterval(updateGame, gameState.realTimeStep);
    }

    // Start the game when the script loads
    initGame();

</script>
```