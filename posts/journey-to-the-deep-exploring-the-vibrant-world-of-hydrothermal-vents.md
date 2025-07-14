---
title: "מסע למעמקים: לחקור את העולם התוסס של נביעות הידרותרמיות"
english_slug: journey-to-the-deep-exploring-the-vibrant-world-of-hydrothermal-vents
category: "ביולוגיה"
tags:
  - נביעות הידרותרמיות
  - ים עמוק
  - מערכות אקולוגיות קיצוניות
  - ביולוגיה ימית
  - כלי מחקר תת-ימיים
---
# מסע למעמקים: לחקור את העולם התוסס של נביעות הידרותרמיות

הצטרפו אלינו למסע מרתק אל קרקעית הים העמוק – מקום בו החושך מוחלט, הלחץ עצום, והטמפרטורות מטפסות לרמות רותחות. כאן, סביב נביעות הידרותרמיות מסתוריות, שגשגות מערכות אקולוגיות מהמוזרות והעשירות ביותר על פני כדור הארץ. איך חיים יצורים בסביבה כל כך עוינת? ואיך אנחנו, בני האדם, מצליחים לחשוף את סודותיהם? השתמשו בסימולטור ה-ROV (רכב תת-ימי בשליטה מרחוק) כדי לחקור בעצמכם!

<div class="app-container">
    <div class="rov-view">
        <div class="seabed">
            <div class="vent" id="hydrothermal-vent"></div>
            <div class="bubbles" id="vent-bubbles"></div> <!-- Added for animation -->
            <div class="creatures" id="creatures"></div> <!-- Moved to be child of seabed -->
            <div class="rov" id="rov-model">
                <div class="rov-light"></div> <!-- Added ROV light -->
            </div>
            <div class="sample-area" id="sample-area"></div> <!-- Moved to be child of seabed -->
            <div class="sensor-area" id="sensor-area"></div> <!-- Moved to be child of seabed -->
        </div>
        <div class="overlay-text" id="status-text">מאתרים אתרי מחקר...</div>
         <div class="overlay-feedback" id="feedback-text"></div> <!-- Added for action feedback -->
    </div>
    <div class="controls">
        <h3>בקרות ה-ROV</h3>
        <div class="movement-controls">
             <button id="move-up" aria-label="מעלה">▲</button>
             <div class="horizontal-controls">
                 <button id="move-left" aria-label="שמאלה">◄</button>
                 <button id="move-right" aria-label="ימינה">►</button>
             </div>
             <button id="move-down" aria-label="מטה">▼</button>
        </div>
        <button id="collect-sample" class="action-button">אסוף דגימה</button>
        <button id="deploy-sensor" class="action-button">פרוס חיישנים</button>
    </div>
    <div class="data-display">
        <h3>נתוני חיישנים בזמן אמת</h3>
        <div id="temperature-data">טמפרטורה: --°C</div>
        <div id="h2s-data">מימן גופרתי (H₂S): -- ppm</div>
        <canvas id="temperature-graph" width="280" height="100"></canvas>
         <div id="sample-status"></div> <!-- Used for sample action status -->
         <div id="sensor-status"></div> <!-- Used for sensor action status -->
    </div>
</div>

<button id="toggle-explanation" class="toggle-button">לחשוף את סודות המעמקים (הצג הסבר)</button>

<div id="explanation" class="explanation-section" style="display: none;">
    <h2>הסבר מפורט: חקר נביעות הידרותרמיות</h2>

    <h3>מבוא: מהן נביעות הידרותרמיות ולמה הן כה מיוחדות?</h3>
    <p>נביעות הידרותרמיות אינן סתם חורים בקרקעית האוקיינוס – הן שערים לעולם תת-קרקעי של אנרגיה וכימיה! במקומות אלו, לרוב לאורך רכסים תת-ימיים שבהם לוחות טקטוניים נפרדים, מים חודרים אל תוך סדקים בקרום כדור הארץ. המים מתחממים על ידי המאגמה הלוהטת שמתחת, ממיסים מינרלים מתוך הסלעים, ופורצים חזרה אל הים העמוק כזרם חם (לעיתים רותח!) ועשיר בכימיקלים. זוהי סביבה קיצונית, ללא אור שמש כלל, תחת לחץ עצום, ועם נוכחות גבוהה של חומרים שנחשבים רעילים לרוב היצורים החיים.</p>

    <h3>כימוסינתזה: הבסיס לחיים בעלטה</h3>
    <p>בניגוד לרוב המערכות האקולוגיות על פני כדור הארץ התלויות באנרגיית השמש (פוטוסינתזה), החיים סביב נביעות הידרותרמיות מתבססים על תהליך מדהים הנקרא כימוסינתזה. חיידקים מיוחדים, המכונים חיידקים כימוסינתטיים, מנצלים את האנרגיה הכימית המשתחררת מחימצון תרכובות גופרית (כמו מימן גופרתי - H₂S) או תרכובות ברזל ומנגן הנמצאות במים הפורצים מהנביעה. חיידקים אלו הם ה"יצרנים" של המערכת, והם מהווים את בסיס שרשרת המזון המקומית.</p>

    <h3>מגוון ביולוגי מפתיע ויצורים ייחודיים</h3>
    <p>מי היה מאמין שבסביבה כה קשה יפרחו חיים בשפע כזה? סביב הנביעות שוכנות אוכלוסיות צפופות ומגוונות של יצורים, רבים מהם אנדמיים לחלוטין לאזורים אלו (כלומר, לא נמצאים בשום מקום אחר בעולם). תולעי צינור ענק ללא פה או מערכת עיכול, צדפות ענק, חלזונות, סרטנים בעלי שריון ייחודי, ודגים מסתוריים – כולם מותאמים בצורה מדהימה לתנאים. רבים מהם מקיימים יחסי סימביוזה עם החיידקים הכימוסינתטיים, אוכלים אותם ישירות או מסתמכים על חומר אורגני שהם מייצרים.</p>

    <h3>חקר המעמקים: האתגרים והכלים</h3>
    <p>חקר נביעות הידרותרמיות הוא מבצע לוגיסטי וטכנולוגי מורכב ביותר. ההגעה לעומקים אלו דורשת כלים שיכולים לעמוד בלחצים קיצוניים ובטמפרטורות משתנות. כלי המחקר העיקריים הם:</p>
    <ul>
        <li><strong>ROVs (Remotely Operated Vehicles):</strong> רובוטים תת-ימיים הנשלטים מספינת מחקר על פני המים. הם מצוידים במצלמות וידאו באיכות גבוהה, זרועות רובוטיות לאיסוף דגימות מדויק (מים, סלעים, ויצורים), וחיישנים למדידת טמפרטורה, לחץ, ריכוזי כימיקלים ועוד. ה-ROV מאפשר שהייה ממושכת באתר וחקר בטיחותי.</li>
        <li><strong>צוללות מחקר מאוישות (HOVs):</strong> כמו ה"אלווין" המפורסמת. מאפשרות למדענים לרדת פיזית לאתר ולצפות בו ממקור ראשון, אך הן יקרות יותר להפעלה, מוגבלות בזמן הצלילה ובקיבולת איסוף הדגימות ביחס ל-ROV.</li>
        <li><strong>חיישנים ומכשירי ניטור קבועים:</strong> מוצבים לפרקי זמן ארוכים כדי לעקוב אחר שינויים טמפרטורה, כימיה, או זרמים סביב הנביעות.</li>
    </ul>

    <h3>מדוע המחקר חשוב?</h3>
    <p>המחקר סביב נביעות הידרותרמיות פותח בפנינו צוהר לכמה מהשאלות הגדולות ביותר במדע:</p>
    <ul>
        <li>**גבולות החיים:** אם חיים יכולים לשגשג בתנאים כאלה, היכן עוד ביקום ייתכן שנמצא חיים? (למשל, באוקיינוסים תת-קרקעיים על ירחים של צדק ושבתאי).</li>
        <li>**מקור החיים:** ישנן תיאוריות מרתקות המציעות כי סביבת הנביעות ההידרותרמיות הקדומות, העשירה באנרגיה וכימיקלים, יכלה להיות המקום שבו החלו החיים על פני כדור הארץ.</li>
        <li>**תהליכים פלנטריים:** הנביעות הן חלק אינטגרלי מהתהליכים הגיאולוגיים והגיאוכימיים המעצבים את כדור הארץ והאוקיינוסים שלו.</li>
        <li>**ביוטכנולוגיה ומשאבים:** יצורים המתקיימים בסביבות קיצוניות מספקים מודלים להבנת עמידות קיצונית, ואנזימים מחיידקים טרמופילים (אוהבי חום) משמשים בתעשייה ובמחקר (למשל, בבדיקות PCR). הנביעות גם מרבדות מינרלים בעלי ערך, נושא הנמצא תחת דיון לגבי אפשרויות כרייה עתידיות.</li>
    </ul>
    <p>חקר נביעות הידרותרמיות הוא מסע אל הלא נודע, שממשיך לחשוף בפנינו עולמות נסתרים ולהרחיב את ההבנה שלנו על החיים, כדור הארץ, ואולי אף היקום כולו.</p>
</div>

<style>
    /* כללי */
    .app-container {
        display: flex;
        flex-wrap: wrap;
        gap: 25px; /* Increased gap */
        justify-content: center;
        margin-top: 25px; /* Increased margin */
        font-family: 'Arial', sans-serif; /* More appealing font */
        color: #333; /* Darker text color */
        direction: rtl;
        text-align: right;
    }

    h1, h2, h3 {
         color: #004085; /* Deeper blue for headings */
         margin-top: 0;
    }

    /* אזור ה-ROV והנוף */
    .rov-view {
        position: relative;
        width: 450px; /* Slightly wider view */
        height: 350px; /* Slightly taller view */
        border: 5px solid #001f3f; /* Darker, thicker border */
        background: linear-gradient(to bottom, #000d1a 0%, #001f3f 80%, #003366 100%); /* Gradient for depth effect */
        overflow: hidden;
        border-radius: 10px; /* Rounded corners */
        box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.5); /* Inner shadow for depth */
    }

    .seabed {
        position: absolute;
        bottom: 0;
        left: 0; /* Starts at 0, moves horizontally */
        width: 1500px; /* Much wider seabed */
        height: 150px; /* Deeper seabed visual */
        background: linear-gradient(to bottom, #2c3e50, #0a192a); /* Darker, textured seabed gradient */
        background-size: cover; /* Ensure gradient covers area */
        display: flex;
        align-items: flex-end;
        padding-bottom: 20px; /* More padding */
        box-sizing: border-box;
        transition: left 0.3s ease-out; /* Smooth scroll */
    }

    .vent {
        position: absolute;
        bottom: 0;
        left: 750px; /* Centered in the 1500px seabed */
        transform: translateX(-50%);
        width: 80px; /* Larger vent */
        height: 100px; /* Taller vent */
        background: linear-gradient(to top, #5a3220, #8b4513); /* Brownish/rocky texture */
        border-top-left-radius: 40px 30px;
        border-top-right-radius: 40px 30px;
        box-shadow: 0 -8px 20px rgba(255, 140, 0, 0.9), 0 -15px 30px rgba(255, 69, 0, 0.6); /* Stronger orange/red glow */
        animation: vent-pulse 3s infinite ease-in-out; /* Pulsing glow animation */
    }

    @keyframes vent-pulse {
        0% { box-shadow: 0 -8px 20px rgba(255, 140, 0, 0.9), 0 -15px 30px rgba(255, 69, 0, 0.6); }
        50% { box-shadow: 0 -10px 25px rgba(255, 165, 0, 1), 0 -20px 40px rgba(255, 99, 71, 0.8); }
        100% { box-shadow: 0 -8px 20px rgba(255, 140, 0, 0.9), 0 -15px 30px rgba(255, 69, 0, 0.6); }
    }

    .bubbles {
         position: absolute;
         bottom: 90px; /* Just above the vent opening */
         left: 750px; /* Centered above vent */
         transform: translateX(-50%);
         width: 60px;
         height: 50px; /* Area for bubbles */
         overflow: hidden;
         pointer-events: none;
         z-index: 2; /* Above vent */
     }

    .bubbles::before {
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        width: 10px; /* Initial size of a bubble */
        height: 10px;
        background-color: rgba(255, 255, 255, 0.5);
        border-radius: 50%;
        transform: translateX(-50%);
        animation: bubble-flow 4s infinite linear;
        box-shadow: 0 0 5px rgba(255, 255, 255, 0.8);
    }
    .bubbles::after { /* Second bubble stream */
         content: '';
         position: absolute;
         bottom: -10px; /* Start slightly lower */
         left: 40%;
         width: 8px;
         height: 8px;
         background-color: rgba(255, 255, 255, 0.4);
         border-radius: 50%;
         transform: translateX(-50%);
         animation: bubble-flow 3.5s infinite linear 0.5s; /* Different timing */
         box-shadow: 0 0 4px rgba(255, 255, 255, 0.7);
     }


     @keyframes bubble-flow {
        0% { bottom: 0; opacity: 1; transform: translateX(-50%) scale(1); }
        100% { bottom: 150px; opacity: 0; transform: translateX(-50%) scale(1.5); } /* Bubbles rise faster/higher */
     }


    .creatures {
         position: absolute;
         bottom: 10px; /* On the seabed */
         left: 750px; /* Centered around the vent */
         transform: translateX(-50%);
         width: 250px; /* Wider area for creatures */
         height: 80px; /* Taller area */
         pointer-events: none;
         z-index: 3; /* Above seabed, below ROV */
         /* Use pseudo-elements for multiple creatures */
     }
     .creatures::before, .creatures::after {
        content: '🦑'; /* Squid/octopus emoji */
        position: absolute;
        font-size: 2em; /* Larger emojis */
        opacity: 0.8;
        filter: drop-shadow(0 0 3px rgba(255,255,255,0.3)); /* Subtle glow */
        animation: creature-pulse 3s infinite ease-in-out alternate;
     }
    .creatures::before {
         left: 10%;
         bottom: 20px;
         animation-delay: 0s;
         content: '🦐'; /* Shrimp emoji */
         font-size: 1.5em;
         animation: creature-float 4s infinite ease-in-out alternate;
     }
     .creatures::after {
         right: 10%;
         bottom: 15px;
         animation-delay: 1.5s;
         content: '🦀'; /* Crab emoji */
         font-size: 1.8em;
          animation: creature-pulse 3.5s infinite ease-in-out alternate;
     }
    /* Basic pulsing/floating animation for creatures */
    @keyframes creature-pulse {
         0% { transform: scale(1); opacity: 0.8; }
         50% { transform: scale(1.05); opacity: 1; }
         100% { transform: scale(1); opacity: 0.8; }
    }
     @keyframes creature-float {
         0% { transform: translateY(0); }
         50% { transform: translateY(-5px); }
         100% { transform: translateY(0); }
     }


    .rov {
        position: absolute;
        bottom: 170px; /* Initial Y position relative to view bottom (above seabed visual) */
        left: calc(50% - 30px); /* Centered visually in view */
        width: 60px; /* Slightly larger ROV */
        height: 40px; /* Taller ROV */
        background-color: #607d8b; /* Blue-grey color */
        border-radius: 8px; /* Rounded corners */
        z-index: 10;
        transition: transform 0.2s ease-out; /* Use transform for smoother movement */
        box-shadow: 0 3px 8px rgba(0, 0, 0, 0.5);
    }

     /* Use pseudo-elements for ROV details */
    .rov::before {
         content: '● ●'; /* Lights */
         position: absolute;
         top: 5px;
         left: 50%;
         transform: translateX(-50%);
         color: yellow; /* Light color */
         font-size: 0.8em;
     }
    .rov::after {
         content: '[]'; /* Camera/Arm */
         position: absolute;
         bottom: 5px;
         left: 50%;
         transform: translateX(-50%);
         color: #333;
         font-weight: bold;
         font-size: 1em;
     }

    .rov-light {
         position: absolute;
         bottom: -10px; /* Below the ROV */
         left: 50%;
         transform: translateX(-50%);
         width: 100px; /* Width of light cone base */
         height: 120px; /* Height of light cone */
         background: radial-gradient(circle at 50% 0%, rgba(255, 255, 180, 0.5) 0%, rgba(255, 255, 180, 0.1) 50%, rgba(255, 255, 180, 0) 100%);
         clip-path: polygon(40% 0%, 60% 0%, 100% 100%, 0% 100%); /* Cone shape */
         z-index: 9; /* Below ROV, above seabed */
         pointer-events: none;
    }


     .sample-area, .sensor-area {
        position: absolute;
        bottom: 10px; /* On the seabed */
        width: 60px; /* Larger area */
        height: 60px;
        border: 3px dashed; /* Thicker dashed border */
        border-radius: 8px; /* Rounded corners */
        display: none; /* Hidden by default */
        pointer-events: none;
        box-sizing: border-box;
        z-index: 5;
        background-color: rgba(255, 255, 255, 0.05); /* Subtle fill */
         animation: pulse-border 1.5s infinite ease-in-out alternate; /* Pulsing effect */
     }

     .sample-area {
        left: 750px + 50px; /* Relative to vent center (750) + offset */
        border-color: rgba(100, 149, 237, 0.7); /* Cornflower blue */
        background-color: rgba(100, 149, 237, 0.1);
     }
     .sensor-area {
        left: 750px - 110px; /* Relative to vent center (750) - offset */
         border-color: rgba(60, 179, 113, 0.7); /* Medium sea green */
         background-color: rgba(60, 179, 113, 0.1);
     }
     @keyframes pulse-border {
         0% { border-color: rgba(255, 255, 255, 0.5); }
         100% { border-color: rgba(255, 255, 255, 0.9); }
     }


    .overlay-text {
        position: absolute;
        top: 15px; /* More padding */
        left: 15px;
        color: #fff;
        background-color: rgba(0, 0, 0, 0.6); /* Slightly darker background */
        padding: 8px 12px; /* More padding */
        border-radius: 5px;
        font-size: 1em; /* Slightly larger font */
        z-index: 20;
        text-align: right; /* Ensure text aligns right in RTL */
    }
     .overlay-feedback {
         position: absolute;
         bottom: 15px;
         left: 50%;
         transform: translateX(-50%);
         color: #fff;
         background-color: rgba(0, 0, 0, 0.7);
         padding: 8px 15px;
         border-radius: 5px;
         font-size: 1.1em;
         z-index: 25; /* Above status text */
         opacity: 0; /* Start hidden */
         transition: opacity 0.5s ease-in-out;
     }
     .overlay-feedback.show {
         opacity: 1;
     }
     .overlay-feedback.success {
         background-color: rgba(40, 167, 69, 0.8); /* Green */
     }
     .overlay-feedback.error {
         background-color: rgba(220, 53, 69, 0.8); /* Red */
     }


    /* בקרות ונתונים */
    .controls, .data-display {
        background-color: #e9f1f8; /* Light blue background */
        padding: 20px; /* More padding */
        border-radius: 10px; /* Rounded corners */
        width: 300px; /* Wider panels */
        box-sizing: border-box;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }

    .controls h3, .data-display h3 {
         color: #0056b3; /* Blue headings */
         margin-bottom: 15px; /* More space below heading */
    }

    .movement-controls {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 20px;
    }

    .movement-controls button {
        margin: 4px; /* Less margin for tighter layout */
        padding: 12px 20px; /* Larger buttons */
        cursor: pointer;
        background-color: #007bff; /* Primary blue */
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 1.2em; /* Larger font */
        transition: background-color 0.2s ease;
        min-width: 80px; /* Ensure consistent button size */
        text-align: center;
    }
     .movement-controls button:hover {
         background-color: #0056b3;
     }
     .movement-controls button:active {
         background-color: #003f7f;
     }


    .horizontal-controls {
        display: flex;
        justify-content: center;
        width: 100%;
    }

    .horizontal-controls button {
         margin: 4px;
         padding: 12px 20px;
         cursor: pointer;
         background-color: #007bff;
         color: white;
         border: none;
         border-radius: 5px;
         font-size: 1.2em;
         transition: background-color 0.2s ease;
         min-width: 80px;
          text-align: center;
    }
     .horizontal-controls button:hover {
         background-color: #0056b3;
     }
     .horizontal-controls button:active {
         background-color: #003f7f;
     }


    .action-button {
        display: block;
        width: 100%;
        padding: 12px; /* Larger padding */
        margin-bottom: 12px; /* More margin */
        cursor: pointer;
        background-color: #28a745; /* Green for action */
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 1.1em;
        transition: background-color 0.2s ease;
    }
     .action-button:hover {
         background-color: #218838;
     }
     .action-button:active {
         background-color: #1e7e34;
     }
     .action-button:disabled {
         background-color: #ccc;
         cursor: not-allowed;
     }

    .data-display div {
        margin-bottom: 10px; /* More space */
        font-family: 'Courier New', monospace; /* Different monospace font */
        font-size: 1em; /* Slightly larger */
        color: #003366; /* Dark blue text */
    }

    #temperature-graph {
        display: block;
        margin-top: 15px;
        background-color: #fff;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
     #temperature-graph-container { /* Optional: Wrapper for graph styling */
         position: relative;
     }


    .toggle-button {
        display: block;
        width: 250px; /* Wider button */
        margin: 30px auto; /* More margin */
        padding: 12px 20px;
        font-size: 1.1em;
        cursor: pointer;
        background-color: #17a2b8; /* Teal color */
        color: white;
        border: none;
        border-radius: 5px;
        text-align: center;
        transition: background-color 0.2s ease;
         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
     .toggle-button:hover {
         background-color: #138496;
     }
     .toggle-button:active {
         background-color: #117a8b;
     }


    .explanation-section {
        margin-top: 30px; /* More space */
        padding: 25px; /* More padding */
        background-color: #f0f8ff; /* Light blue background */
        border: 1px solid #b8daff; /* Light blue border */
        border-radius: 10px;
        line-height: 1.7; /* Increased line height */
        color: #333;
         box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }

    .explanation-section h2,
    .explanation-section h3 {
        color: #004085;
        margin-top: 20px; /* More space above headings */
        margin-bottom: 10px;
    }

    .explanation-section p {
        margin-bottom: 15px;
    }

    .explanation-section ul {
        margin-bottom: 15px;
        padding-right: 25px; /* Adjust padding for RTL */
        list-style: disc; /* Ensure bullet points */
    }
    .explanation-section li {
        margin-bottom: 8px; /* More space between list items */
    }
</style>

<script>
    const rov = document.getElementById('rov-model');
    const seabed = document.querySelector('.seabed');
    const vent = document.getElementById('hydrothermal-vent');
    const statusText = document.getElementById('status-text');
    const feedbackText = document.getElementById('feedback-text'); // Added feedback element
    const tempDisplay = document.getElementById('temperature-data');
    const h2sDisplay = document.getElementById('h2s-data');
    const sampleStatus = document.getElementById('sample-status'); // Used only for button status now
    const sensorStatus = document.getElementById('sensor-status'); // Used only for button status now
    const tempGraphCanvas = document.getElementById('temperature-graph');
    const ctx = tempGraphCanvas.getContext('2d');
    const explanationSection = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggle-explanation');
    const sampleArea = document.getElementById('sample-area');
    const sensorArea = document.getElementById('sensor-area');
    const collectButton = document.getElementById('collect-sample');
    const deployButton = document.getElementById('deploy-sensor');

    let rovPosition = { x: 750, y: 170 }; // Initial position within seabed coordinate space (0-1500 for X)
    const seabedWidth = 1500; // Must match CSS .seabed width
    const rovViewWidth = 450; // rov-view width
    const rovViewHeight = 350; // rov-view height
    const rovWidth = 60; // Matches CSS
    const rovHeight = 40; // Matches CSS
    const seabedVisualHeight = 150; // Matches CSS seabed height visual, ROV bottom is relative to view bottom
    const rovMinY = seabedVisualHeight + 20; // Minimum Y (closest to seabed)
    const rovMaxY = rovViewHeight - rovHeight - 20; // Maximum Y (closest to surface/top view edge)

    // Vent position relative to seabed left edge
    const ventPositionX = 750; // Matches CSS left: 750px relative to seabed's width (1500)

    // Target areas centered slightly offset from vent
    const sampleAreaCenterX_seabed = ventPositionX + 50 + (60/2); // Vent center + offset + half area width
    const sensorAreaCenterX_seabed = ventPositionX - 110 + (60/2); // Vent center - offset + half area width
    const areaProximityThreshold = 70; // Distance from ROV center X to area center X to be "in range"

    // Initial ROV visual position (Y relative to view bottom, X is visually centered)
    rov.style.bottom = `${rovPosition.y}px`;
    // X visual position is handled by seabed scrolling

    function updateSeabedPosition() {
        // Calculate how much the seabed should shift horizontally.
        // We want the point 'rovPosition.x' on the seabed (0-1500)
        // to appear aligned with the horizontal center of the rov-view (450/2 = 225).
        // Let seabed_left_offset be the X coordinate on the seabed that aligns with the left edge of the rov-view (0).
        // The point rovPosition.x on the seabed is (rovPosition.x - seabed_left_offset) from the left edge of the view.
        // We want this to be 225. So, 225 = rovPosition.x - seabed_left_offset.
        // seabed_left_offset = rovPosition.x - 225.
        let seabedOffset = rovPosition.x - (rovViewWidth / 2);

        // Clamp the offset so the seabed doesn't move too far.
        // Max negative shift (positive offset applied): (seabedWidth - rovViewWidth) = 1500 - 450 = 1050.
        // The minimum offset is 0.
        seabedOffset = Math.max(0, Math.min(seabedWidth - rovViewWidth, seabedOffset));

        // Apply the negative offset to the seabed's left CSS property
        seabed.style.left = `${-seabedOffset}px`;

        // Update status text and sensor data display based on new position
        updateStatus();
        updateSensorData();
    }

     // Use CSS transform for smoother movement than just updating bottom/left
     // Update logical position and trigger visual updates
    function updateROVPosition(dx, dy) {
        // Update logical position in seabed coordinates for X
        let newX = rovPosition.x + dx;
        // Clamp logical position within seabed bounds for X
        newX = Math.max(rovWidth / 2, Math.min(seabedWidth - rovWidth / 2, newX));

         // Update logical position for Y relative to view bottom
        let newY = rovPosition.y + dy;
         // Clamp logical position within view bounds for Y
        newY = Math.max(rovMinY, Math.min(rovMaxY, newY));

        // Check if position actually changed
        if (newX !== rovPosition.x || newY !== rovPosition.y) {
            rovPosition.x = newX;
            rovPosition.y = newY;

             // Apply visual Y position change directly
            rov.style.bottom = `${rovPosition.y}px`;
             // X visual position is handled by seabed scrolling via updateSeabedPosition
            updateSeabedPosition();

            // Update ROV light position slightly based on movement direction (subtle effect)
             const lightElement = rov.querySelector('.rov-light');
             if (lightElement) {
                 // Simple shift: left/right movement slightly shifts light angle
                 // This is complex with clip-path. A simple approach is just vertical.
                 // Or let's skip dynamic light angle for simplicity while maintaining premium feel via static style.
                 // Keep light centered: lightElement.style.left = '50%';
                 // Keep light bottom: lightElement.style.bottom = '-10px';
             }
        }
    }


    function getDistanceToVent() {
         // ROV center X is rovPosition.x (in seabed coords)
         // Vent center X is ventPositionX (in seabed coords)
         return Math.abs(rovPosition.x - ventPositionX);
     }

    function getTemperatureAtROV() {
        const distance = getDistanceToVent();
        // More refined model: Steep drop-off near vent, stabilizes further away
        const maxTemp = 400; // Example max temp in °C at distance 0
        const baseTemp = 2; // Deep sea base temp in °C far from vent
        // Use an exponential decay model: temp = base + (max - base) * exp(-k * distance)
        const k = 0.015; // Drop-off factor
        const temp = baseTemp + (maxTemp - baseTemp) * Math.exp(-k * distance);
        return Math.max(baseTemp, temp); // Ensure temp doesn't go below base
    }

     function getH2SConcentrationAtROV() {
         const distance = getDistanceToVent();
         // Similar exponential decay model for H2S
         const maxH2S = 200; // Example max ppm at distance 0
         const baseH2S = 0.1; // Background H2S far from vent
         const k = 0.02; // Drop-off factor
         const h2s = baseH2S + (maxH2S - baseH2S) * Math.exp(-k * distance);
         return Math.max(baseH2S, h2s);
     }


    function updateStatus() {
        const distanceToVent = getDistanceToVent();
        let status = `מרחק מהנביעה: כ-${distanceToVent.toFixed(0)} יחידות.`;

        // Check proximity to sample/sensor areas based on ROV X position
        const sampleAreaDistance = Math.abs(rovPosition.x - sampleAreaCenterX_seabed);
        const sensorAreaDistance = Math.abs(rovPosition.x - sensorAreaCenterX_seabed);

        let isInSampleArea = sampleAreaDistance < areaProximityThreshold;
        let isInSensorArea = sensorAreaDistance < areaProximityThreshold;

        if (isInSampleArea) {
             status += " | בטווח איסוף דגימות.";
             sampleArea.style.display = 'block';
             collectButton.disabled = false;
             collectButton.classList.add('ready'); // Optional: Add a visual cue class
             collectButton.innerText = 'אסוף דגימה מהירה'; // More specific text
         } else {
             sampleArea.style.display = 'none';
             collectButton.disabled = true;
             collectButton.classList.remove('ready');
             collectButton.innerText = 'אסוף דגימה';
         }

         if (isInSensorArea) {
             status += " | בטווח פריסת חיישנים.";
             sensorArea.style.display = 'block';
             // Only enable if not already deployed
             if (!deployButton.classList.contains('deployed')) {
                deployButton.disabled = false;
                deployButton.classList.add('ready');
                 deployButton.innerText = 'פרוס מערך חיישנים'; // More specific text
             }
         } else {
             sensorArea.style.display = 'none';
             // Only disable if not already deployed
             if (!deployButton.classList.contains('deployed')) {
                deployButton.disabled = true;
                deployButton.classList.remove('ready');
                deployButton.innerText = 'פרוס חיישנים';
             }
         }

        statusText.innerText = status;
    }

     let temperatureReadings = []; // Store [distance, temp] pairs
     let sensorDeploymentActive = false;

     function updateSensorData() {
        const temp = getTemperatureAtROV();
        const h2s = getH2SConcentrationAtROV();

         // Add some subtle noise to readings for realism (optional)
        const tempNoise = (Math.random() - 0.5) * 0.5; // +/- 0.25°C
        const h2sNoise = (Math.random() - 0.5) * 0.2; // +/- 0.1 ppm
        const displayedTemp = temp + (sensorDeploymentActive ? tempNoise : 0); // Only add noise when sensors "active"
         const displayedH2S = h2s + (sensorDeploymentActive ? h2sNoise : 0);

        tempDisplay.innerText = `טמפרטורה: ${displayedTemp.toFixed(1)}°C`;
        h2sDisplay.innerText = `מימן גופרתי (H₂S): ${displayedH2S.toFixed(2)} ppm`; // More precision for H2S

        // Store reading if sensors are deployed
        if (sensorDeploymentActive) {
             const distance = getDistanceToVent();
             // Record reading only if moved significantly or first reading
             if (temperatureReadings.length === 0 || Math.abs(temperatureReadings[temperatureReadings.length - 1][0] - distance) > 10) { // Record every ~10 units moved
                temperatureReadings.push([distance, temp]); // Store actual temp, not noisy one
                 // Keep readings sorted by distance for graph
                 temperatureReadings.sort((a, b) => a[0] - b[0]);
                 drawTemperatureGraph();
             } else {
                 // If not adding a new point, redraw to update current location dot
                 drawTemperatureGraph();
             }
        } else {
             // If sensors not deployed, only update current values and draw empty graph or graph with current dot
             drawTemperatureGraph(); // Draws axis, labels, and potentially current dot
        }
    }

     function drawTemperatureGraph() {
         ctx.clearRect(0, 0, tempGraphCanvas.width, tempGraphCanvas.height);

         const minDistance = 0; // Graph X axis starts at distance 0 from vent
         const maxDistance = Math.max(500, Math.max(...temperatureReadings.map(r => r[0] || 0))); // Max X is 500 or furthest recorded distance
         const minTemp = 0;
         const maxTemp = 450; // Max temp for graph Y axis (slightly above max possible)

         const xRatio = tempGraphCanvas.width / (maxDistance - minDistance);
         const yRatio = tempGraphCanvas.height / (maxTemp - minTemp);

         // Draw axes
         ctx.strokeStyle = '#888'; // Darker gray axes
         ctx.lineWidth = 1;
         ctx.beginPath();
         // X axis (Distance from vent) - plotted at bottom of graph
         ctx.moveTo(0, tempGraphCanvas.height);
         ctx.lineTo(tempGraphCanvas.width, tempGraphCanvas.height);
         // Y axis (Temperature) - plotted at left (distance 0)
         ctx.moveTo(0, 0);
         ctx.lineTo(0, tempGraphCanvas.height);
         ctx.stroke();

         // Draw vent indicator at Distance 0 (left edge of graph)
         ctx.fillStyle = 'rgba(255, 140, 0, 0.8)'; // Orange
         ctx.font = '10px sans-serif';
         ctx.textAlign = 'left';
         ctx.fillText('נביעה', 5, tempGraphCanvas.height - 5);

         // Draw base temp indicator
         const baseTempY = tempGraphCanvas.height - (getTemperatureAtROV(maxDistance) - minTemp) * yRatio;
         ctx.strokeStyle = '#aaa';
         ctx.beginPath();
         ctx.moveTo(0, baseTempY);
         ctx.lineTo(tempGraphCanvas.width, baseTempY);
         ctx.stroke();
         ctx.fillStyle = '#888';
         ctx.textAlign = 'right';
         ctx.fillText(`${getTemperatureAtROV(maxDistance).toFixed(0)}°C בסיס`, tempGraphCanvas.width - 5, baseTempY - 3);


         if (sensorDeploymentActive && temperatureReadings.length > 0) {
            // Draw data points if sensors are deployed and data exists
             ctx.beginPath();
             ctx.strokeStyle = '#dc3545'; // Red color for temperature line
             ctx.lineWidth = 2;

             temperatureReadings.forEach((reading, index) => {
                 const [distance, temp] = reading;
                 // Clamp distance for drawing if it exceeds maxDistance, but use recorded value
                 const x = (Math.min(distance, maxDistance) - minDistance) * xRatio;
                 const y = tempGraphCanvas.height - (temp - minTemp) * yRatio;

                 if (index === 0) {
                     ctx.moveTo(x, y);
                 } else {
                     ctx.lineTo(x, y);
                 }
             });
             ctx.stroke();
         } else {
              // If sensors not deployed, show message
             ctx.fillStyle = '#666';
             ctx.font = '12px sans-serif';
             ctx.textAlign = 'center';
             ctx.fillText('פרוס חיישנים כדי לאסוף נתוני טמפרטורה', tempGraphCanvas.width / 2, tempGraphCanvas.height / 2);
         }


         // Draw current reading dot (always)
         const currentDistance = getDistanceToVent();
         const currentTemp = getTemperatureAtROV();
          // Clamp current distance for drawing if it exceeds maxDistance
         const currentX = (Math.min(currentDistance, maxDistance) - minDistance) * xRatio;
         const currentY = tempGraphCanvas.height - (currentTemp - minTemp) * yRatio;
         ctx.fillStyle = '#007bff'; // Blue dot for current position
         ctx.beginPath();
         ctx.arc(currentX, currentY, 5, 0, Math.PI * 2); // Slightly larger dot
         ctx.fill();
         ctx.strokeStyle = '#fff'; // White border
         ctx.lineWidth = 1;
         ctx.stroke();

         // Add axis labels
         ctx.fillStyle = '#333';
         ctx.font = '10px sans-serif';
         ctx.textAlign = 'left';
         ctx.fillText('טמפ°C', 5, 10); // Label for Y axis (Temperature)
         ctx.textAlign = 'center';
         ctx.fillText('מרחק מהנביעה (יחידות)', tempGraphCanvas.width / 2, tempGraphCanvas.height - 5); // Label for X axis (Distance)
     }

    function showFeedback(message, isSuccess = true) {
        feedbackText.innerText = message;
        feedbackText.classList.remove('success', 'error');
        feedbackText.classList.add('show', isSuccess ? 'success' : 'error');
        setTimeout(() => {
            feedbackText.classList.remove('show');
        }, 3000); // Hide after 3 seconds
    }


    // Movement controls (using buttons)
    document.getElementById('move-up').addEventListener('click', () => updateROVPosition(0, 20)); // Larger step
    document.getElementById('move-down').addEventListener('click', () => updateROVPosition(0, -20)); // Larger step
    document.getElementById('move-left').addEventListener('click', () => updateROVPosition(-20, 0)); // Larger step
    document.getElementById('move-right').addEventListener('click', () => updateROVPosition(20, 0)); // Larger step


    // Keyboard controls
    document.addEventListener('keydown', (event) => {
        const moveStep = 20; // Match button step
        switch (event.key) {
            case 'ArrowUp':
            case 'w':
            case 'W':
                updateROVPosition(0, moveStep);
                event.preventDefault(); // Prevent scrolling the page
                break;
            case 'ArrowDown':
            case 's':
            case 'S':
                updateROVPosition(0, -moveStep);
                event.preventDefault();
                break;
            case 'ArrowLeft':
            case 'a':
            case 'A':
                updateROVPosition(-moveStep, 0);
                event.preventDefault();
                break;
            case 'ArrowRight':
            case 'd':
            case 'D':
                updateROVPosition(moveStep, 0);
                event.preventDefault();
                break;
        }
    });


    // Sample collection
    collectButton.addEventListener('click', () => {
        const sampleAreaDistance = Math.abs(rovPosition.x - sampleAreaCenterX_seabed);
         if (sampleAreaDistance < areaProximityThreshold) {
            showFeedback('✅ דגימה ביולוגית חשובה נאספה!', true);
            sampleStatus.innerText = 'דגימה נאספה!';
            sampleStatus.style.color = 'green';
             // Optional: Add a temporary visual effect (e.g., flash or particle)
        } else {
            showFeedback('❌ ה-ROV אינו ממוקם מעל אזור הדגימה.', false);
            sampleStatus.innerText = ''; // Clear status if not in range
        }
         // sampleStatus text is less critical now, main feedback is overlay. Clear it later.
         setTimeout(() => sampleStatus.innerText = '', 3000);
    });

    // Sensor deployment
    deployButton.addEventListener('click', (event) => {
         const sensorAreaDistance = Math.abs(rovPosition.x - sensorAreaCenterX_seabed);
         if (sensorAreaDistance < areaProximityThreshold) {
             if (!sensorDeploymentActive) {
                 sensorDeploymentActive = true;
                 event.target.disabled = true;
                 event.target.innerText = 'חיישנים פרוסים ☑️';
                 event.target.classList.add('deployed'); // Mark as deployed
                 showFeedback('📊 חיישנים נפרסו בהצלחה! מתחיל איסוף נתונים.', true);
                 sensorStatus.innerText = 'חיישנים פרוסים';
                 sensorStatus.style.color = 'green';
                 temperatureReadings = []; // Clear previous readings
                 updateSensorData(); // Get initial readings and draw graph
             } else {
                  showFeedback('חיישנים כבר פרוסים באזור זה.', false);
             }
         } else {
             showFeedback('❌ ה-ROV אינו ממוקם מעל אזור פריסת חיישנים.', false);
              sensorStatus.innerText = ''; // Clear status if not in range
         }
         setTimeout(() => sensorStatus.innerText = '', 3000);
    });


    // Toggle explanation visibility
    toggleButton.addEventListener('click', () => {
        if (explanationSection.style.display === 'none') {
            explanationSection.style.display = 'block';
            toggleButton.innerText = 'להסתיר את סודות המעמקים (הסתר הסבר)';
        } else {
            explanationSection.style.display = 'none';
            toggleButton.innerText = 'לחשוף את סודות המעמקים (הצג הסבר)';
        }
    });

    // Initial setup
    updateSeabedPosition(); // Set initial seabed position based on initial ROV position
    // Buttons start disabled in HTML, updateStatus will enable them if in range
    collectButton.disabled = true;
    deployButton.disabled = true;

    // Initial data display and graph
    updateSensorData(); // Get and display initial sensor data (before deployment)
    drawTemperatureGraph(); // Draw initial state of the graph (empty or just current pos)

</script>
```