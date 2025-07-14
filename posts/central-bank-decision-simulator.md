---
title: "הדירקטוריון המוניטרי: סימולטור קבלת ההחלטות של הבנק המרכזי"
english_slug: central-bank-decision-simulator
category: "מדעי החברה / כלכלה ופיננסים"
tags: ["בנק מרכזי", "מדיניות מוניטרית", "ריבית", "אינפלציה", "מקרו-כלכלה", "סימולציה"]
---
<p>האם אתה מוכן לשבת בכיסא החם ולהשפיע על גורל הכלכלה? דירקטוריון הבנק המרכזי מקבל החלטות קריטיות שמעצבות את יוקר המחיה, שוק העבודה וצמיחת המשק כולו. אילו שיקולים מנחים אותם, ועד כמה קשה לנווט בין יעדים שונים ואף סותרים?</p>
<p>התנסה בסימולטור וגלה את ההשפעה של שינוי בריבית המרכזית.</p>

<div class="simulator-container">
    <h1>לוח המחוונים הכלכלי הנוכחי</h1>
    <div id="dashboard" class="dashboard">
        <div class="indicator" id="indicator-inflation">
            <div class="indicator-title">שיעור אינפלציה (שנתי)</div>
            <div class="indicator-value" id="inflation-current"></div>
            <div class="indicator-trend" id="inflation-trend"></div>
             <div class="indicator-icon"></div> <!-- For potential icon -->
        </div>
        <div class="indicator" id="indicator-unemployment">
             <div class="indicator-title">שיעור אבטלה</div>
            <div class="indicator-value" id="unemployment-current"></div>
            <div class="indicator-trend" id="unemployment-trend"></div>
             <div class="indicator-icon"></div>
        </div>
        <div class="indicator" id="indicator-gdp">
            <div class="indicator-title">צמיחת התוצר (GDP שנתי)</div>
            <div class="indicator-value" id="gdp-current"></div>
            <div class="indicator-trend" id="gdp-trend"></div>
             <div class="indicator-icon"></div>
        </div>
        <div class="indicator" id="indicator-exchange-rate">
             <div class="indicator-title">שער חליפין (מטבע מקומי / $)</div>
            <div class="indicator-value" id="exchange-rate-current"></div>
            <div class="indicator-trend" id="exchange-rate-trend"></div>
             <div class="indicator-icon"></div>
        </div>
        <div class="indicator primary" id="indicator-interest-rate">
             <div class="indicator-title">ריבית בנק מרכזי</div>
            <div class="indicator-value" id="interest-rate-current"></div>
             <div class="indicator-trend">הכלי שלך</div>
             <div class="indicator-icon"></div>
        </div>
    </div>

    <h2>ההחלטה שלך: קביעת הריבית</h2>
    <div class="decision-controls">
        <label for="rate-change">בחר את שינוי הריבית:</label>
        <select id="rate-change">
            <option value="0.75">+0.75% (העלאה אגרסיבית)</option>
             <option value="0.5">+0.50% (העלאה משמעותית)</option>
            <option value="0.25">+0.25% (העלאה מתונה)</option>
            <option value="0" selected>0% (השאר ללא שינוי)</option>
            <option value="-0.25">-0.25% (הורדה מתונה)</option>
            <option value="-0.5">-0.50% (הורדה משמעותית)</option>
            <option value="-0.75">-0.75% (הורדה אגרסיבית)</option>
        </select>
        <!-- placeholder for future controls -->
        <button id="submit-decision">אשר החלטה ובדוק השפעה</button>
    </div>

    <div id="results" class="results">
        <h2>השפעה צפויה (בטווח של כשנה)</h2>
        <div class="indicator" id="result-inflation">
            <div class="indicator-title">שיעור אינפלציה (צפוי)</div>
            <div class="indicator-value" id="inflation-projected"></div>
            <div class="indicator-change" id="inflation-change"></div>
            <div class="indicator-icon"></div>
        </div>
        <div class="indicator" id="result-unemployment">
            <div class="indicator-title">שיעור אבטלה (צפוי)</div>
            <div class="indicator-value" id="unemployment-projected"></div>
            <div class="indicator-change" id="unemployment-change"></div>
            <div class="indicator-icon"></div>
        </div>
        <div class="indicator" id="result-gdp">
            <div class="indicator-title">צמיחת התוצר (GDP צפוי)</div>
            <div class="indicator-value" id="gdp-projected"></div>
            <div class="indicator-change" id="gdp-change"></div>
             <div class="indicator-icon"></div>
        </div>
         <div class="indicator" id="result-exchange-rate">
            <div class="indicator-title">שער חליפין (צפוי)</div>
            <div class="indicator-value" id="exchange-rate-projected"></div>
            <div class="indicator-change" id="exchange-rate-change"></div>
             <div class="indicator-icon"></div>
        </div>
         <div class="indicator outcome" id="result-summary">
            <div class="indicator-title">סיכום ההשפעה</div>
             <div class="indicator-value" id="outcome-message"></div>
             <div class="indicator-change">ראה שינויים לפרטים</div>
             <div class="indicator-icon"></div>
        </div>
    </div>
</div>

<button id="toggle-explanation">מהם הכלים של הבנק המרכזי ואיך הם עובדים? (הצג/הסתר הסבר)</button>

<div id="explanation" style="display: none;">
    <h2>מאחורי הקלעים: הבנק המרכזי והמדיניות המוניטרית</h2>

    <h3>הקוסם של הכלכלה? תפקידי הבנק המרכזי</h3>
    <p>הבנק המרכזי הוא הרבה יותר מבנק רגיל; הוא השומר על יציבות הכלכלה. תפקידיו העיקריים הם לשמור על יציבות מחירים (לרסן אינפלציה ודפלציה), לתמוך בתעסוקה גבוהה ובצמיחה יציבה, ולשמור על חוזקה של המערכת הפיננסית. לעיתים קרובות, כמו במשחק שראית, יש ניגוד אינטרסים בין היעדים - הורדת אינפלציה עלולה לפגוע בצמיחה, למשל. תפקיד הדירקטוריון הוא למצוא את האיזון.</p>

    <h3>הכלי החזק מכולם: הריבית המוניטרית</h3>
    <p>כלי הנשק העיקרי של הבנק המרכזי הוא קביעת הריבית. זו הריבית בה הבנקים המסחריים יכולים ללוות כסף מהבנק המרכזי או להפקיד אצלו. ריבית זו משפיעה כמו גלים על הכלכלה כולה:</p>
    <ul>
        <li>**דלק או בלם לכלכלה:** ריבית נמוכה הופכת הלוואות (למשכנתא, לרכב, לעסק) לזולות יותר, מעודדת אנשים ועסקים להוציא ולהשקיע, ומזניקה את הפעילות. ריבית גבוהה מייקרת הלוואות, מעודדת חיסכון, ומאטה את קצב ההוצאות וההשקעות - בולם לצמיחה.</li>
        <li>**הקרב באינפלציה:** כשהכלכלה "חמה" מדי ויש יותר מדי כסף שרודף אחרי מעט מדי מוצרים, המחירים עולים (אינפלציה). העלאת ריבית מצננת את הביקושים ועוזרת לרסן את עליית המחירים. הורדת ריבית בתקופת מיתון יכולה למנוע דפלציה (ירידת מחירים מסוכנת).</li>
        <li>**השפעה על המטבע:** מדינה עם ריבית גבוהה יותר נהנית מביקוש גדול יותר למטבע שלה מצד משקיעים זרים שמחפשים תשואה גבוהה על כספם. זה יכול לגרום למטבע המקומי להתחזק (שער חליפין נמוך יותר לדולר), מה שמוזיל יבוא ומייקר יצוא.</li>
    </ul>

    <h3>כלים נוספים בארגז הכלים</h3>
    <p>בעיתות משבר או כשהריבית כבר קרובה לאפס, הבנק המרכזי יכול להשתמש בכלים לא שגרתיים כמו "הרחבה כמותית" (QE). זהו מהלך בו הבנק רוכש כמויות גדולות של אגרות חוב בשוק, מזריק כסף למערכת הפיננסית, ומנסה להוריד את הריביות הארוכות טווח ולעודד אשראי. זה כמו "הורדת ריבית ענקית לטווח ארוך".</p>

    <h3>לקרוא את המפה הכלכלית: הנתונים החשובים</h3>
    <p>הבנק המרכזי אינו עובד באפלה. הוא עוקב בדריכות אחר נתונים מרכזיים:</p>
    <ul>
        <li>**אינפלציה:** המדד מספר כמה מהר המחירים עולים. היעד הנפוץ הוא בסביבות 2% בשנה - מספיק כדי "לשמן" את גלגלי הכלכלה, אך לא להזיק לכוח הקנייה.</li>
        <li>**אבטלה:** אחוז האנשים שמחפשים עבודה ואינם מוצאים. אבטלה נמוכה היא בדרך כלל חדשות טובות, אך נמוכה מדי עלולה להצביע על התחממות יתר בשוק העבודה וללחוץ לעליות שכר ואינפלציה (קשר המכונה "עקומת פיליפס").</li>
        <li>**צמיחת GDP:** שינוי התוצר מייצג אם הכלכלה מתרחבת או מתכווצת. צמיחה בריאה היא חיונית לשיפור רמת החיים.</li>
        <li>**שער חליפין:** מחיר המטבע המקומי לעומת מטבעות זרים (בעיקר הדולר). חשוב ליצואנים, יבואנים, תיירות ולהשקעות.</li>
    </ul>
    <p>האתגר הוא להבין את הקשרים המורכבים בין הנתונים הללו ואיך שינוי באחד ישפיע על האחרים.</p>

    <h3>קבלת החלטה תחת לחץ: אתגרים ופשרות</h3>
    <p>החיים של נגיד הבנק המרכזי אינם קלים. מדוע?</p>
    <ul>
        <li>**השפעה מאוחרת:** להחלטת ריבית לוקח זמן להשפיע במלואה - לעיתים מעל שנה! צריך "לירות" מתוך הערכה לאן הכלכלה הולכת, לא היכן היא נמצאת היום.</li>
        <li>**ים של אי-ודאות:** משברים עולמיים, שינויים פוליטיים, התפתחויות טכנולוגיות - הכל משפיע על הכלכלה באופן בלתי צפוי.</li>
        <li>**ציפיות משחקות תפקיד:** אם השווקים מצפים שהריבית תעלה, הם עשויים להתנהג כאילו היא כבר עלתה. תקשורת ברורה של הבנק המרכזי חשובה כדי לנהל את הציפיות.</li>
    </ul>
    <p>כפי שחווית בסימולטור, לכל החלטה יש מחיר ("טרייד-אוף"). העלאת ריבית עשויה להילחם באינפלציה אך לפגוע בצמיחה. הורדת ריבית יכולה לתמוך בצמיחה אך להגביר את הסיכון לאינפלציה. המטרה היא למצוא את שביל הזהב שישרת בצורה הטובה ביותר את מטרות הכלכלה בטווח הארוך.</p>
</div>

<style>
    :root {
        --primary-color: #007bff;
        --primary-color-dark: #0056b3;
        --secondary-color: #6c757d;
        --background-color: #f8f9fa;
        --card-background: #ffffff;
        --border-color: #dee2e6;
        --text-color: #343a40;
        --positive-color: #28a745; /* Green */
        --negative-color: #dc3545; /* Red */
        --neutral-color: #6c757d; /* Gray */
        --positive-bg: #d4edda;
        --negative-bg: #f8d7da;
        --neutral-bg: #e2e6ea;
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.7;
        margin: 0;
        padding: 20px;
        direction: rtl; /* Set text direction to right-to-left */
        text-align: right;
        background-color: var(--background-color);
        color: var(--text-color);
        min-height: 100vh; /* Ensure background covers viewport */
        box-sizing: border-box;
    }

    p {
        margin-bottom: 1em;
    }

    h1, h2, h3 {
        color: var(--primary-color-dark);
        margin-top: 1.5em;
        margin-bottom: 0.8em;
        line-height: 1.3;
    }

    h1 { font-size: 1.8em; }
    h2 { font-size: 1.5em; }
    h3 { font-size: 1.2em; }


    .simulator-container {
        border: 1px solid var(--border-color);
        padding: 25px;
        margin-bottom: 30px;
        background-color: var(--card-background);
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
        transition: box-shadow 0.3s ease;
    }

    .simulator-container:hover {
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.12);
    }

    .dashboard, .results {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 20px;
        margin-bottom: 25px;
    }

    .indicator {
        background-color: #f1f1f1; /* Lighter base */
        padding: 20px 15px;
        border-radius: 8px;
        text-align: center;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
         transition: transform 0.3s ease, background-color 0.3s ease;
         min-height: 120px; /* Ensure uniform height */
    }

    .indicator.primary {
        background-color: var(--primary-color);
        color: white;
    }

    .indicator.primary .indicator-title,
    .indicator.primary .indicator-value,
     .indicator.primary .indicator-trend,
     .indicator.primary .indicator-change {
         color: white;
     }

    .indicator.outcome {
         background-color: var(--secondary-color);
         color: white;
         grid-column: 1 / -1; /* Span across all columns in results */
         align-items: center;
         justify-content: center;
    }

     .indicator.outcome .indicator-title,
     .indicator.outcome .indicator-value,
      .indicator.outcome .indicator-change {
          color: white;
      }


    .indicator:hover {
         transform: translateY(-3px);
    }


    .indicator-title {
        font-size: 0.9em;
        color: var(--text-color);
        margin-bottom: 8px;
        font-weight: bold;
    }

    .indicator.primary .indicator-title { color: white; }
    .indicator.outcome .indicator-title { color: white; }


    .indicator-value {
        margin: 5px 0;
        font-size: 1.8em; /* Larger value font */
        font-weight: bold;
         flex-grow: 1; /* Make value take up space */
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .indicator-trend, .indicator-change {
        font-size: 0.85em;
        font-weight: normal;
        margin-top: 5px;
    }

    .indicator-trend.up, .indicator-change.negative { color: var(--negative-color); font-weight: bold;} /* Red for negative trends/changes (inflation up, unemployment up, GDP down, exchange rate up) */
    .indicator-trend.down, .indicator-change.positive { color: var(--positive-color); font-weight: bold;} /* Green for positive trends/changes (inflation down, unemployment down, GDP up, exchange rate down) */
    .indicator-trend.stable, .indicator-change.neutral { color: var(--neutral-color); } /* Gray for neutral */

     /* Special coloring for indicator backgrounds based on change */
     #result-inflation.negative { background-color: var(--negative-bg); }
     #result-inflation.positive { background-color: var(--positive-bg); }
     #result-inflation.neutral { background-color: var(--neutral-bg); }

     #result-unemployment.negative { background-color: var(--negative-bg); }
     #result-unemployment.positive { background-color: var(--positive-bg); }
     #result-unemployment.neutral { background-color: var(--neutral-bg); }

     #result-gdp.negative { background-color: var(--negative-bg); }
     #result-gdp.positive { background-color: var(--positive-bg); }
     #result-gdp.neutral { background-color: var(--neutral-bg); }

     #result-exchange-rate.negative { background-color: var(--negative-bg); }
     #result-exchange-rate.positive { background-color: var(--positive-bg); }
     #result-exchange-rate.neutral { background-color: var(--neutral-bg); }


    .decision-controls {
        margin-bottom: 30px;
        padding: 20px;
        background-color: #e9ecef; /* Light gray background */
        border-radius: 8px;
        display: flex;
        align-items: center;
        gap: 20px;
        flex-wrap: wrap;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
    }
    .decision-controls label {
        font-weight: bold;
        color: var(--text-color);
        font-size: 1.1em;
    }
    .decision-controls select, .decision-controls button {
        padding: 10px 15px;
        font-size: 1em;
        border: 1px solid var(--border-color);
        border-radius: 6px;
        font-family: 'Arial', sans-serif; /* Ensure consistent font */
    }
     .decision-controls select {
         background-color: white;
         cursor: pointer;
     }

    .decision-controls button {
        background-color: var(--primary-color);
        color: white;
        cursor: pointer;
        border: none;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
        box-shadow: 0 2px 5px rgba(0, 123, 255, 0.3);
    }
    .decision-controls button:hover {
        background-color: var(--primary-color-dark);
    }
     .decision-controls button:active {
         transform: translateY(1px);
         box-shadow: 0 1px 3px rgba(0, 123, 255, 0.5);
     }

    .results {
        /* Initial state before decision */
        display: none; /* Controlled by JS */
        opacity: 0; /* Start hidden for animation */
        transition: opacity 0.5s ease-in-out;
        margin-top: 20px;
        padding-top: 20px;
        border-top: 1px dashed var(--border-color);
    }

     .results.show {
         opacity: 1;
         display: grid; /* Override initial display: none */
     }

    #explanation {
        border: 1px solid var(--border-color);
        padding: 25px;
        background-color: #e9ecef; /* Light gray background */
        border-radius: 12px;
        margin-top: 30px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
    }
    #explanation h2, #explanation h3 {
        color: var(--primary-color-dark);
    }
    #explanation ul {
        list-style: disc;
        margin-right: 25px; /* For RTL list bullets */
        padding-right: 0; /* Reset default padding */
    }
    #explanation li {
        margin-bottom: 10px;
    }

    #toggle-explanation {
        display: block;
        width: auto;
        margin: 30px auto;
        padding: 12px 25px;
        font-size: 1em;
        cursor: pointer;
        border: 1px solid var(--primary-color);
        background-color: white;
        color: var(--primary-color);
        border-radius: 6px;
        transition: background-color 0.3s ease, color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
     #toggle-explanation:hover {
        background-color: var(--primary-color);
        color: white;
        box-shadow: 0 3px 7px rgba(0, 0, 0, 0.15);
     }
     #toggle-explanation:active {
         transform: translateY(1px);
         box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
     }

     /* Add subtle icon/indicator for trends/changes (optional, requires HTML structure or pseudo-elements) */
     /* Example using pseudo-elements */
    .indicator-trend.up::before,
    .indicator-change.negative::before {
        content: "▲ "; /* Up arrow */
        color: var(--negative-color); /* Red */
    }
    .indicator-trend.down::before,
    .indicator-change.positive::before {
        content: "▼ "; /* Down arrow */
        color: var(--positive-color); /* Green */
    }
     .indicator-trend.stable::before,
    .indicator-change.neutral::before {
        content: "▬ "; /* Dash */
        color: var(--neutral-color); /* Gray */
    }

    /* Hide initial results using a class */
    .results:not(.show) {
        display: none;
    }


    /* Media queries for responsiveness */
    @media (max-width: 768px) {
        .dashboard, .results {
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
        }
         .simulator-container, #explanation {
             padding: 20px;
         }
         .decision-controls {
             flex-direction: column;
             align-items: stretch;
             gap: 15px;
         }
         .decision-controls select, .decision-controls button {
             width: 100%; /* Full width on small screens */
             box-sizing: border-box; /* Include padding/border in width */
         }
          .indicator-value {
              font-size: 1.5em;
          }
    }

     @media (max-width: 480px) {
          body {
              padding: 15px;
          }
          .indicator-value {
              font-size: 1.3em;
          }
          h1 { font-size: 1.5em; }
          h2 { font-size: 1.3em; }
          h3 { font-size: 1.1em; }
     }

</style>

<script>
    // Initial Economic State (Example Scenario: High Inflation, Moderate Growth, Low Unemployment)
    // Let's make the initial state slightly more dramatic to show the decision impact
    let economyState = {
        inflation: 6.2, // Annual % - High
        unemployment: 3.5, // % - Very Low
        gdpGrowth: 2.0, // Annual % - Moderate
        exchangeRate: 3.85, // Local currency per USD - Relatively high
        interestRate: 3.50 // % - Moderate
    };

    // Trends (for display purposes - simplified based on state)
    const trends = {
        // Simple logic: inflation > 3% => up, unemployment < 4% => down, gdp > 2% => stable/up, exchange rate > 3.8 => up
        inflation: economyState.inflation > 3.5 ? 'up' : (economyState.inflation < 1.5 ? 'down' : 'stable'),
        unemployment: economyState.unemployment < 4 ? 'down' : (economyState.unemployment > 6 ? 'up' : 'stable'),
        gdpGrowth: economyState.gdpGrowth > 2.5 ? 'up' : (economyState.gdpGrowth < 1 ? 'down' : 'stable'),
        exchangeRate: economyState.exchangeRate > 3.7 ? 'up' : (economyState.exchangeRate < 3.4 ? 'down' : 'stable')
    };

    // Basic Simulation Model Parameters (Simplified multipliers and lags)
    // These are illustrative and do not represent real-world precise relationships.
    // Values adjusted slightly for more noticeable impact in simulation.
    const simulationParams = {
        // Impact of +1% rate change after ~1 year
        inflationImpactPerRate: -1.0, // 1% rate hike reduces inflation by ~1.0%
        unemploymentImpactPerRate: 0.5, // 1% rate hike increases unemployment by ~0.5%
        gdpImpactPerRate: -0.7, // 1% rate hike reduces GDP growth by ~0.7%
        exchangeRateImpactPerRate: -0.12 // 1% rate hike strengthens currency (lower rate per USD) by ~0.12
    };

    // Function to display current state
    function displayCurrentState() {
        document.getElementById('inflation-current').innerText = economyState.inflation.toFixed(1) + '%';
        document.getElementById('unemployment-current').innerText = economyState.unemployment.toFixed(1) + '%';
        document.getElementById('gdp-current').innerText = economyState.gdpGrowth.toFixed(1) + '%';
        document.getElementById('exchange-rate-current').innerText = economyState.exchangeRate.toFixed(2);
        document.getElementById('interest-rate-current').innerText = economyState.interestRate.toFixed(2) + '%';

        document.getElementById('inflation-trend').innerText = `מגמה: ${trends.inflation === 'up' ? 'עולה' : trends.inflation === 'down' ? 'יורדת' : 'יציבה'}`;
        document.getElementById('inflation-trend').className = 'indicator-trend ' + trends.inflation;
        document.getElementById('unemployment-trend').innerText = `מגמה: ${trends.unemployment === 'up' ? 'עולה' : trends.unemployment === 'down' ? 'יורדת' : 'יציבה'}`;
        document.getElementById('unemployment-trend').className = 'indicator-trend ' + trends.unemployment;
        document.getElementById('gdp-trend').innerText = `מגמה: ${trends.gdpGrowth === 'up' ? 'עולה' : trends.gdpGrowth === 'down' ? 'יורדת' : 'יציבה'}`;
        document.getElementById('gdp-trend').className = 'indicator-trend ' + trends.gdpGrowth;
        document.getElementById('exchange-rate-trend').innerText = `מגמה: ${trends.exchangeRate === 'up' ? 'עולה' : trends.exchangeRate === 'down' ? 'יורדת' : 'יציבה'}`;
        document.getElementById('exchange-rate-trend').className = 'indicator-trend ' + trends.exchangeRate;
    }

    // Function to run simulation and display results
    function runSimulation() {
        const rateChange = parseFloat(document.getElementById('rate-change').value);

        // Calculate projected changes based on rate change
        // Note: We calculate change based on the *change* in rate, not the new absolute rate.
        const projectedInflationChange = rateChange * simulationParams.inflationImpactPerRate;
        const projectedUnemploymentChange = rateChange * simulationParams.unemploymentImpactPerRate;
        const projectedGdpChange = rateChange * simulationParams.gdpImpactPerRate;
        const projectedExchangeRateChange = rateChange * simulationParams.exchangeRateImpactPerRate;

        // Calculate projected values
        // Add a small random factor to make it less predictable and more "real-world"-like (within limits)
        const randomFactor = (Math.random() - 0.5) * 0.4; // Random value between -0.2 and +0.2
         const inflationNoise = randomFactor * (rateChange === 0 ? 1 : Math.abs(rateChange) * 2); // More noise if rate changes
         const otherNoise = randomFactor * (rateChange === 0 ? 0.5 : Math.abs(rateChange));

        const projectedInflation = Math.max(-0.5, economyState.inflation + projectedInflationChange + inflationNoise); // Prevent absurd negative inflation
        const projectedUnemployment = Math.max(1.5, economyState.unemployment + projectedUnemploymentChange + otherNoise); // Prevent absurd low unemployment
        const projectedGdp = economyState.gdpGrowth + projectedGdpChange + otherNoise;
        const projectedExchangeRate = economyState.exchangeRate + projectedExchangeRateChange + otherNoise;

        // Determine change classes and text
        const inflationDiff = projectedInflation - economyState.inflation;
        const unemploymentDiff = projectedUnemployment - economyState.unemployment;
        const gdpDiff = projectedGdp - economyState.gdpGrowth;
        const exchangeRateDiff = projectedExchangeRate - economyState.exchangeRate; // Lower number means stronger currency

        const inflationChangeClass = inflationDiff > 0.1 ? 'negative' : (inflationDiff < -0.1 ? 'positive' : 'neutral');
        const unemploymentChangeClass = unemploymentDiff > 0.1 ? 'negative' : (unemploymentDiff < -0.1 ? 'positive' : 'neutral');
        const gdpChangeClass = gdpDiff > 0.1 ? 'positive' : (gdpDiff < -0.1 ? 'negative' : 'neutral');
        // Exchange rate: positive diff means weaker currency (negative outcome)
        const exchangeRateChangeClass = exchangeRateDiff > 0.05 ? 'negative' : (exchangeRateDiff < -0.05 ? 'positive' : 'neutral');


        // Display projected state and changes
        document.getElementById('inflation-projected').innerText = projectedInflation.toFixed(1) + '%';
        document.getElementById('inflation-change').innerText = `שינוי: ${inflationDiff > 0 ? '+' : ''}${inflationDiff.toFixed(1)} נק"א`; // נק"א = נקודות אחוז
        document.getElementById('inflation-change').className = 'indicator-change ' + inflationChangeClass;
         document.getElementById('result-inflation').className = 'indicator ' + inflationChangeClass; // Apply color class to card

        document.getElementById('unemployment-projected').innerText = projectedUnemployment.toFixed(1) + '%';
        document.getElementById('unemployment-change').innerText = `שינוי: ${unemploymentDiff > 0 ? '+' : ''}${unemploymentDiff.toFixed(1)} נק"א`;
        document.getElementById('unemployment-change').className = 'indicator-change ' + unemploymentChangeClass;
        document.getElementById('result-unemployment').className = 'indicator ' + unemploymentChangeClass;

        document.getElementById('gdp-projected').innerText = projectedGdp.toFixed(1) + '%';
        document.getElementById('gdp-change').innerText = `שינוי: ${gdpDiff > 0 ? '+' : ''}${gdpDiff.toFixed(1)} נק"א`;
        document.getElementById('gdp-change').className = 'indicator-change ' + gdpChangeClass;
         document.getElementById('result-gdp').className = 'indicator ' + gdpChangeClass;


        document.getElementById('exchange-rate-projected').innerText = projectedExchangeRate.toFixed(2);
        document.getElementById('exchange-rate-change').innerText = `שינוי: ${exchangeRateDiff > 0 ? '+' : ''}${exchangeRateDiff.toFixed(2)}`;
        document.getElementById('exchange-rate-change').className = 'indicator-change ' + exchangeRateChangeClass;
         document.getElementById('result-exchange-rate').className = 'indicator ' + exchangeRateChangeClass;

        // Add a summary message based on the overall impact
        let outcomeMessage = "ההחלטה שלך בוצעה.";
        let outcomeClass = 'neutral';

        // Simple logic for outcome message - could be more complex
        if (inflationDiff < -0.5 && unemploymentDiff < 0.3 && gdpDiff > 0.3) {
             outcomeMessage = "השפעה חיובית כוללת: שיפור באינפלציה, ללא פגיעה משמעותית באבטלה ובצמיחה!";
             outcomeClass = 'positive';
         } else if (inflationDiff < -0.3 && unemploymentDiff > 0.3 && gdpDiff < -0.3) {
              outcomeMessage = "טרייד-אוף קלאסי: האינפלציה יורדת, אך במחיר עלייה באבטלה והאטה בצמיחה.";
              outcomeClass = 'negative'; // Negative because often fighting inflation harms growth/jobs
         } else if (inflationDiff > 0.3 && unemploymentDiff < -0.3 && gdpDiff > 0.3) {
              outcomeMessage = "התחממות יתר: האינפלציה עלולה לעלות, אך התעסוקה והצמיחה משתפרות.";
              outcomeClass = 'negative'; // Often inflation is the primary concern to fight
         } else if (rateChange === 0) {
              outcomeMessage = "השארת הריבית ללא שינוי. ההשפעה צפויה להיות מתונה.";
              outcomeClass = 'neutral';
         } else if (Math.abs(rateChange) >= 0.5 && (inflationChangeClass === 'neutral' || unemploymentChangeClass === 'neutral' || gdpChangeClass === 'neutral')) {
             outcomeMessage = "השפעה מפתיעה! שינוי גדול בריבית הניב תוצאות מעורבות.";
             outcomeClass = 'neutral';
         }
         // More outcome messages can be added here based on combinations of changes

        document.getElementById('outcome-message').innerText = outcomeMessage;
        document.getElementById('result-summary').className = 'indicator outcome ' + outcomeClass; // Apply color class to summary card


        // Show results with animation
        const resultsDiv = document.getElementById('results');
        resultsDiv.classList.remove('show'); // Reset animation
        // Use a small timeout to allow display: none to apply before adding the class back
        setTimeout(() => {
             resultsDiv.style.display = 'grid'; // Ensure grid display is set before opacity
             resultsDiv.classList.add('show');
        }, 50); // Small delay
    }

    // Event listener for the decision button
    document.getElementById('submit-decision').addEventListener('click', runSimulation);

    // Event listener for the explanation toggle button
    document.getElementById('toggle-explanation').addEventListener('click', function() {
        const explanationDiv = document.getElementById('explanation');
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        if (isHidden) {
            explanationDiv.style.display = 'block';
            this.innerText = 'הסתר הסבר על מדיניות מוניטרית';
        } else {
            explanationDiv.style.display = 'none';
            this.innerText = 'מהם הכלים של הבנק המרכזי ואיך הם עובדים? (הצג/הסתר הסבר)';
        }
    });

    // Initialize the display on page load
    displayCurrentState();

</script>