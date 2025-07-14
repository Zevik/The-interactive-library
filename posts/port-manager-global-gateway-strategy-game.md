---
title: "מנהל נמל: משחק אסטרטגיה לשער הסחר העולמי"
english_slug: port-manager-global-gateway-strategy-game
category: "מדעי החברה / כלכלה ופיננסים"
tags: ["ניהול", "לוגיסטיקה", "סחר בינלאומי", "שרשרת אספקה", "תשתיות"]
---
<h1>מנהל נמל: משחק אסטרטגיה לשער הסחר העולמי</h1>

<p>האם תהיתם פעם מה קורה מאחורי הקלעים של זרימת הסחורות העולמית? נמלים ימיים הם הלב הפועם של הכלכלה הגלובלית, נקודות מפגש קריטיות בין יבשה לים. ניהול נמל תקין הוא אמנות הדורשת חשיבה אסטרטגית, ניהול משאבים יעיל וקבלת החלטות מהירות. בואו לצלול פנימה, קבלו לידיכם את ההגה, וגלו בעצמכם מה נדרש כדי להפוך נמל לפעיל ויעיל לשער סחר מצליח בקנה מידה עולמי.</p>

<div id="port-simulation">
    <div id="simulation-area">
        <div id="port-map">
            <h2><i class="icon icon-map"></i> מפת הנמל</h2>
            <div class="berth-container">
                <div class="berth" data-berth-id="1">
                    <h3>רציף 1</h3>
                    <div class="berth-status">פנוי</div>
                    <div class="ship-at-berth"></div>
                </div>
                <div class="berth" data-berth-id="2">
                    <h3>רציף 2</h3>
                    <div class="berth-status">פנוי</div>
                    <div class="ship-at-berth"></div>
                </div>
                <div class="berth" data-berth-id="3">
                    <h3>רציף 3</h3>
                    <div class="berth-status">פנוי</div>
                    <div class="ship-at-berth"></div>
                </div>
                <div class="berth" data-berth-id="4">
                    <h3>רציף 4</h3>
                    <div class="berth-status">פנוי</div>
                    <div class="ship-at-berth"></div>
                </div>
            </div>
            <div id="waiting-area">
                <h3><i class="icon icon-ship"></i> אזור עגינה (אוניות ממתינות)</h3>
                <ul id="waiting-ships-list">
                    <!-- Waiting ships will be listed here -->
                    <li class="placeholder">אין אוניות ממתינות כרגע.</li>
                </ul>
            </div>
        </div>
        <div id="controls">
            <h2><i class="icon icon-controls"></i> פאנל ניהול</h2>
            <div id="kpis">
                <h3><i class="icon icon-kpi"></i> מדדי ביצוע (KPIs)</h3>
                <p>שעת סימולציה: <span id="simulation-time">0</span></p>
                <p>תפוקה מצטברת: <span id="throughput">0</span> טון מטען</p>
                <p>ממוצע זמן שהייה אונייה בנמל: <span id="avg-turnaround">N/A</span> שעות</p>
                <p>ממוצע זמן המתנה לרציף: <span id="avg-wait">N/A</span> שעות</p>
                <p>ניצולת רציפים (ממוצע): <span id="berth-utilization">0.0%</span></p>
            </div>
            <div id="assignment-controls">
                <h3><i class="icon icon-assign"></i> הקצאת אונייה לרציף</h3>
                <p>בחר אונייה ממתינה ורציף פנוי להקצאה:</p>
                <div class="control-group">
                    <label for="select-ship">אונייה:</label>
                    <select id="select-ship">
                        <option value="">-- בחר אונייה --</option>
                    </select>
                </div>
                 <div class="control-group">
                    <label for="select-berth">רציף:</label>
                    <select id="select-berth">
                        <option value="">-- בחר רציף --</option>
                    </select>
                </div>
                <button id="assign-button" disabled><i class="icon icon-confirm"></i> בצע הקצאה</button>
            </div>
            <div id="game-actions">
                 <h3><i class="icon icon-actions"></i> פעולות זמן</h3>
                 <button id="next-turn-button"><i class="icon icon-clock"></i> התקדם לשעה הבאה</button>
            </div>
            <div id="messages">
                <h3><i class="icon icon-messages"></i> יומן תפעול</h3>
                <ul id="message-list">
                     <li class="placeholder">הודעות המערכת יופיעו כאן.</li>
                </ul>
            </div>
        </div>
    </div>
</div>

<button id="toggleExplanationButton"><i class="icon icon-info"></i> הצג/הסתר הסבר תיאורטי: נמלים ימיים וניהולם</button>

<div id="explanation" style="display: none;">
    <h2><i class="icon icon-book"></i> הסבר תיאורטי: נמלים ימיים וניהולם</h2>

    <p>נמלים ימיים הם עורקי החיים של הסחר העולמי. למעלה מ-80% מהסחר הבינלאומי במוצרים מתבצע דרך הים, ונמלים משמשים כצמתים קריטיים בשרשרת האספקה הגלובלית, מחברים בין נתיבי שיט ימיים לבין מערכות שינוע יבשתיות (רכבות, משאיות).</p>

    <h3><i class="icon icon-structure"></i> רכיבים מרכזיים של נמל</h3>
    <ul>
        <li>**רציפים (Berths):** המקום שבו אוניות עוגנות לצורך פריקה וטעינה של מטען. מספר הרציפים, סוגם, ועומק המים לידם מגבילים את כמות וסוג האוניות שהנמל יכול לטפל בהן בו זמנית.</li>
        <li>**עגורנים (Cranes):** ציוד מכני המשמש להרמה והזזת מטענים כבדים בין האונייה לרציף או לשטח האחסון. סוגי עגורנים שונים מותאמים לסוגי מטען שונים (עגורני מכולות, עגורנים לתפזורת). זמינות העגורנים משפיעה ישירות על קצב הפריקה/טעינה.</li>
        <li>**שטחי אחסון (Storage Areas):** שטחים ייעודיים לאחסון מטען זמני לפני שינועו ליעד הסופי או העמסתו על אונייה אחרת. כוללים מסופי מכולות (Container Terminals), מחסנים, ומגרשי אחסון למטענים בתפזורת או רכבים. ניהול יעיל של שטחי אחסון חיוני למניעת עומס.</li>
        <li>**שערים (Gates):** נקודות הכניסה והיציאה היבשתיות של מטענים מהנמל (עבור משאיות, רכבות). יעילות תהליך הכניסה/יציאה בשער משפיעה על העומס מחוץ לנמל.</li>
        <li>**תשתיות יבשתיות:** חיבורים מסילתיים וכבישים מהירים המובילים אל הנמל וממנו, ומאפשרים שינוע מהיר ויעיל של מטען פנים הארץ.</li>
    </ul>

    <h3><i class="icon icon-process"></i> תהליכים תפעוליים בנמל</h3>
    <p>הפעילות השוטפת בנמל כוללת:</p>
    <ul>
        <li>**עגינת אוניות:** ניהול התנועה הימית, הכוונה של אוניות לאזור עגינה (במידה והרציפים תפוסים) ולאחר מכן הקצאת רציף פנוי.</li>
        <li>**פריקה וטעינה (Loading/Unloading):** שימוש בעגורנים וציוד נוסף להעברת מטען בין האונייה לרציף. זהו בדרך כלל השלב שלוקח את מרבית הזמן בשהיית האונייה ברציף.</li>
        <li>**אחסון מטען:** העברת המטען משטח הרציף לשטחי האחסון בנמל.</li>
        <li>**שחרור מטען (Clearance):** תהליכים בירוקרטיים ורגולטוריים, בעיקר מול המכס, לשחרור המטען מהנמל.</li>
        <li>**שינוע יבשתי (Inland Transport):** העמסת המטען על משאיות או רכבות לשינוע ליעדו הסופי, או קבלת מטען מהיבשה להעמסה על אוניות.</li>
    </ul>

    <h3><i class="icon icon-challenge"></i> אתגרים בניהול נמל</h3>
    <p>מנהל נמל חייב להתמודד עם מגוון אתגרים:</p>
    <ul>
        <li>**עומס (Congestion):** עומס ימי (אוניות ממתינות מחוץ לנמל) ועומס יבשתי (פקקי משאיות, עומס בשערי הנמל). נגרם לרוב מחוסר התאמה בין קצב הגעת האוניות/מטענים לבין קיבולת הטיפול של הנמל.</li>
        <li>**ניהול משאבים:** הקצאה אופטימלית של רציפים, עגורנים, ציוד פריקה/טעינה וכוח אדם, כדי למקסם את התפוקה ולמזער זמני המתנה.</li>
        <li>**תחזוקה והשקעות:** שמירה על תקינות הציוד והתשתיות הקיימות, ותכנון השקעות עתידיות להגדלת הקיבולת או שדרוג טכנולוגי.</li>
        <li>**טכנולוגיה:** אימוץ טכנולוגיות חדשות לשיפור היעילות (מערכות ניהול נמל, אוטומציה, מעקב אחרי מטען).</li>
        <li>**בטיחות וסביבה:** הבטחת תהליכי עבודה בטוחים לעובדים ולסביבה, וציות לתקנות מחמירות.</li>
        <li>**גורמים חיצוניים:** התמודדות עם השפעות של גורמים בלתי צפויים כמו מזג אוויר קיצוני, תקלות טכניות, שביתות, או שינויים פתאומיים בנפחי הסחר.</li>
    </ul>

    <h3><i class="icon icon-analytics"></i> מדדי ביצוע עיקריים (KPIs)</h3>
    <p>כדי למדוד את יעילות הנמל משתמשים במדדים שונים:</p>
    <ul>
        <li>**תפוקה (Throughput):** כמות המטען (מכולות, טון) שעוברת דרך הנמל ביחידת זמן נתונה (למשל, לשעה, ליום, לשנה). מדד כמותי מרכזי.</li>
        <li>**זמן שהייה של אונייה (Turnaround Time):** הזמן הכולל שבו אונייה נמצאת בנמל, החל מכניסתה לאזור העגינה ועד עזיבתה לאחר השלמת הטיפול. כולל זמן המתנה וזמן טיפול ברציף. שאיפה לצמצם זמן זה ככל האפשר.</li>
        <li>**ניצולת רציפים (Berth Utilization):** אחוז הזמן שבו רציף תפוס על ידי אונייה מתוך סך הזמן הזמין. ניצולת גבוהה מדי (למשל, מעל 70-80%) עלולה להעיד על עומס וחוסר קיבולת, ואף לגרום לעיכובים. ניצולת נמוכה מדי עלולה להעיד על תשתית עודפת או חוסר ביקוש.</li>
        <li>**זמן שהייה של מטען (Dwell Time):** הזמן שלוקח למטען מרגע פריקתו מהאונייה ועד יציאתו מהנמל. מדד ליעילות התהליכים היבשתיים ושחרור המכס.</li>
    </ul>

    <h3><i class="icon icon-supplychain"></i> הנמל כחוליה בשרשרת האספקה</h3>
    <p>יעילות הנמל משפיעה ישירות על כל שרשרת האספקה הגלובלית. עיכובים בנמל יכולים לגרום לעלייה בעלויות (דמי המתנה לאוניות, עלויות אחסון, קנסות), לשבש לוחות זמנים (זמן הגעה לשוק של מוצרים), ולהשפיע על המלאי ביבשה. נמל יעיל, לעומת זאת, מקטין עלויות, משפר את אמינות שרשרת האספקה, ותורם לתחרותיות של המשק.</p>
</div>

<style>
    body {
        font-family: 'Heebo', sans-serif; /* Use a more modern Hebrew-friendly font */
        direction: rtl;
        line-height: 1.6;
        margin: 0;
        padding: 0; /* Remove body padding, let the container manage it */
        background: linear-gradient(to bottom right, #e0f2f7, #b3e5fc); /* Subtle gradient background */
        color: #333;
        overflow-x: hidden; /* Prevent horizontal scroll */
    }

    h1, h2, h3 {
        color: #0056b3; /* Darker blue for headings */
        margin-bottom: 10px;
    }

     h1 {
         text-align: center;
         margin-top: 20px;
         margin-bottom: 10px;
         font-size: 2em;
         color: #003f8c;
     }

    #port-simulation {
        display: flex;
        flex-wrap: wrap;
        gap: 25px; /* Slightly larger gap */
        margin: 20px auto; /* Center the simulation block */
        max-width: 1200px; /* Limit max width */
        background-color: #ffffff;
        padding: 30px; /* More padding */
        border-radius: 12px; /* More rounded corners */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* Stronger, softer shadow */
    }

    #simulation-area {
        flex: 2;
        min-width: 450px; /* Increased min-width */
        display: flex;
        flex-direction: column;
        gap: 25px;
    }

    #port-map {
        background: linear-gradient(to bottom, #e3f2fd, #bbdefb); /* Lighter blue gradient */
        padding: 20px;
        border-radius: 8px;
        text-align: center;
        border: 1px solid #90caf9;
        position: relative; /* For potential future animations */
    }

     #port-map h2 {
         margin-top: 0;
         color: #0d47a1;
     }

    .berth-container {
        display: flex;
        justify-content: space-around;
        gap: 15px; /* Increased gap */
        margin-bottom: 25px;
    }

    .berth {
        background-color: #e1f5fe; /* Very light blue */
        border: 1px solid #b3e5fc;
        padding: 15px; /* More padding */
        border-radius: 8px;
        text-align: center;
        width: 22%; /* Slightly adjusted width */
        min-height: 120px; /* Increased height */
        display: flex;
        flex-direction: column;
        justify-content: center; /* Center content vertically */
        transition: transform 0.3s ease, box-shadow 0.3s ease; /* Add transitions */
        cursor: pointer; /* Indicate clickability (even if not interactive yet) */
         position: relative; /* For animations */
         overflow: hidden; /* Hide overflow for animations */
    }

     .berth:hover:not(.occupied) {
         transform: translateY(-5px); /* Lift effect on hover */
         box-shadow: 0 4px 8px rgba(0,0,0,0.1);
     }

    .berth.occupied {
        background-color: #e8f5e9; /* Very light green */
        border-color: #c8e6c9;
        color: #1b5e20; /* Dark green text */
    }

     .berth.occupied .berth-status {
         color: #2e7d32; /* Darker green status */
     }


    .berth-status {
        font-weight: bold;
        margin-bottom: 8px;
        color: #01579b; /* Dark blue status */
        font-size: 1.1em;
         transition: color 0.3s ease;
    }


    .ship-at-berth {
        font-size: 0.95em;
        color: #455a64; /* Muted gray */
         min-height: 1.2em; /* Reserve space */
    }

    #waiting-area {
         background-color: #fff9c4; /* Very light yellow */
         border: 1px solid #fff176;
         padding: 15px;
         border-radius: 8px;
         text-align: right;
         min-height: 80px; /* Ensure minimum height */
    }

     #waiting-area h3 {
         margin-top: 0;
         color: #f57f17; /* Dark yellow */
     }

    #waiting-ships-list {
        list-style: none;
        padding: 0;
        margin: 10px 0 0 0;
        min-height: 20px; /* Reserve space */
    }

    #waiting-ships-list li {
        background-color: #fff;
        border: 1px solid #ffee58; /* Medium yellow */
        padding: 10px; /* More padding */
        margin-bottom: 8px; /* More margin */
        border-radius: 5px; /* Slightly more rounded */
        font-size: 0.9em;
        color: #333;
         transition: transform 0.3s ease, opacity 0.3s ease; /* Animation for list items */
    }

    #waiting-ships-list li.placeholder {
        text-align: center;
        font-style: italic;
        color: #777;
        border: none;
        background: none;
    }

     #waiting-ships-list li.ship-entering {
         transform: translateX(-100%);
         opacity: 0;
     }

     #waiting-ships-list li.ship-present {
         transform: translateX(0);
         opacity: 1;
     }


    #controls {
        flex: 1;
        min-width: 300px;
        display: flex;
        flex-direction: column;
        gap: 25px;
    }

    #kpis, #assignment-controls, #game-actions, #messages {
        background-color: #eef2f7; /* Light gray-blue */
        padding: 20px;
        border-radius: 8px;
        border: 1px solid #d5e0ed;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.05); /* Subtle inner shadow */
    }
     #kpis h3, #assignment-controls h3, #game-actions h3, #messages h3 {
         margin-top: 0;
     }

    #kpis p {
        font-size: 1em;
        margin-bottom: 8px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-bottom: 5px;
        border-bottom: 1px dotted #ccc;
    }
     #kpis p:last-child {
         border-bottom: none;
         margin-bottom: 0;
     }

    #kpis span {
         font-weight: bold;
         color: #0056b3;
         font-size: 1.1em;
          min-width: 50px; /* Align values */
          text-align: left;
    }


    .control-group {
        margin-bottom: 15px;
    }

    #assignment-controls label {
        display: block; /* Labels on their own line */
        margin-bottom: 5px;
        font-weight: bold;
        color: #0056b3;
    }

    #assignment-controls select {
        width: 100%;
        padding: 10px; /* More padding */
        border-radius: 5px;
        border: 1px solid #ccc;
        font-size: 1em;
        background-color: #fff;
        cursor: pointer;
        -webkit-appearance: none; /* Remove default dropdown arrow */
        -moz-appearance: none;
        appearance: none;
        background-image: url('data:image/svg+xml;utf8,<svg fill="%23333" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M7 10l5 5 5-5z"/><path d="M0 0h24v24H0z" fill="none"/></svg>'); /* Custom arrow */
        background-repeat: no-repeat;
        background-position: left 10px center; /* Adjust arrow position for RTL */
        padding-left: 40px; /* Make space for arrow */
        transition: border-color 0.3s ease;
    }

    #assignment-controls select:focus {
        outline: none;
        border-color: #007bff;
        box-shadow: 0 0 5px rgba(0, 123, 255, 0.25);
    }


    #assignment-controls button {
         background-color: #007bff;
         color: white;
         border: none;
         cursor: pointer;
         padding: 10px 20px; /* More padding */
         border-radius: 5px;
         font-size: 1.1em;
         transition: background-color 0.3s ease, opacity 0.3s ease;
         width: 100%;
         display: flex;
         align-items: center;
         justify-content: center;
         gap: 8px;
    }

    #assignment-controls button:hover:not(:disabled) {
        background-color: #0056b3;
    }

    #assignment-controls button:disabled {
         background-color: #cccccc;
         cursor: not-allowed;
         opacity: 0.6;
    }

     #game-actions button {
        background-color: #28a745; /* Green */
        color: white;
        border: none;
        cursor: pointer;
        padding: 12px 20px;
        border-radius: 5px;
        font-size: 1.1em;
        width: 100%;
        transition: background-color 0.3s ease;
        display: flex;
         align-items: center;
         justify-content: center;
         gap: 8px;
     }
     #game-actions button:hover {
        background-color: #218838;
     }

    #messages ul {
        list-style: none;
        padding: 0;
        max-height: 200px; /* Increased height */
        overflow-y: auto;
        border-top: 1px solid #d5e0ed;
        padding-top: 10px;
    }

    #messages li {
        background-color: #ffffff;
        border: 1px solid #eee;
        padding: 10px; /* More padding */
        margin-bottom: 8px; /* More margin */
        border-radius: 5px;
        font-size: 0.9em;
        color: #555;
        word-break: break-word; /* Prevent long words from breaking layout */
        opacity: 0; /* Start invisible for animation */
        transform: translateY(10px); /* Start slightly down for animation */
        animation: message-fade-in 0.5s ease forwards; /* Animation */
    }

     #messages li.placeholder {
        text-align: center;
        font-style: italic;
        color: #777;
        border: none;
        background: none;
     }

     #messages li:nth-child(1) { animation-delay: 0.1s; }
     #messages li:nth-child(2) { animation-delay: 0.2s; }
     #messages li:nth-child(3) { animation-delay: 0.3s; }
     #messages li:nth-child(4) { animation-delay: 0.4s; }
     #messages li:nth-child(5) { animation-delay: 0.5s; }


     @keyframes message-fade-in {
         to {
             opacity: 1;
             transform: translateY(0);
         }
     }


    #toggleExplanationButton {
        display: block;
        margin: 30px auto; /* More margin */
        padding: 12px 25px; /* More padding */
        background-color: #6c757d; /* Gray */
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.3s ease;
        display: flex;
         align-items: center;
         justify-content: center;
         gap: 8px;
    }
     #toggleExplanationButton:hover {
        background-color: #5a6268;
     }


    #explanation {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        margin: 20px auto;
        max-width: 1200px;
        border-top: 5px solid #0056b3; /* Accent color top border */
    }

    #explanation h2, #explanation h3 {
        margin-top: 20px; /* More space above headings */
        margin-bottom: 15px;
         color: #003f8c;
    }

    #explanation ul {
        margin-top: 15px;
        margin-bottom: 20px;
        padding-right: 20px; /* Adjust for RTL */
         list-style: disc; /* Use default disc style */
         line-height: 1.8;
    }

     #explanation ul li {
         margin-bottom: 10px;
     }

     /* Icons (Simple unicode or inline SVG) */
     .icon {
         display: inline-block;
         margin-left: 5px; /* Space after icon in RTL */
     }

     .icon-map::before { content: "📍"; } /* Unicode for map */
     .icon-ship::before { content: "🚢"; } /* Unicode for ship */
     .icon-controls::before { content: "🎛️"; } /* Unicode for controls */
     .icon-kpi::before { content: "📊"; } /* Unicode for chart */
     .icon-assign::before { content: "⚓"; } /* Unicode for anchor */
     .icon-confirm::before { content: "✅"; } /* Unicode for check */
     .icon-actions::before { content: "⏳"; } /* Unicode for hourglass */
     .icon-clock::before { content: "⏱️"; } /* Unicode for stopwatch */
     .icon-messages::before { content: "💬"; } /* Unicode for speech bubble */
     .icon-info::before { content: "ℹ️"; } /* Unicode for info */
     .icon-book::before { content: "📚"; } /* Unicode for books */
     .icon-structure::before { content: "🏗️"; } /* Unicode for building */
     .icon-process::before { content: "🔄"; } /* Unicode for refresh */
     .icon-challenge::before { content: "⚠️"; } /* Unicode for warning */
     .icon-analytics::before { content: "📈"; } /* Unicode for graph */
     .icon-supplychain::before { content: "🔗"; } /* Unicode for link */


     /* Add some visual distinction for selected items in dropdowns */
     #select-ship option:checked {
        background-color: #b3e5fc;
        font-weight: bold;
     }
      #select-berth option:checked {
        background-color: #c8e6c9;
        font-weight: bold;
     }


     /* Add animation to berth when status changes */
     .berth .berth-status {
         transition: color 0.5s ease, transform 0.5s ease;
     }
      .berth.occupied .berth-status {
         color: green; /* Change color on occupied */
         transform: scale(1.1); /* Slightly larger text */
      }

     /* Basic "ship" animation cue in berth */
     @keyframes pulse-ship {
         0% { transform: scale(1); opacity: 0.8; }
         50% { transform: scale(1.05); opacity: 1; }
         100% { transform: scale(1); opacity: 0.8; }
     }

     .berth.occupied .ship-at-berth {
         animation: pulse-ship 2s infinite ease-in-out;
         color: #1b5e20;
     }


</style>

<script>
    const berths = [
        { id: 1, occupiedBy: null, timeRemaining: 0, totalOccupiedTime: 0 },
        { id: 2, occupiedBy: null, timeRemaining: 0, totalOccupiedTime: 0 },
        { id: 3, occupiedBy: null, timeRemaining: 0, totalOccupiedTime: 0 },
        { id: 4, occupiedBy: null, timeRemaining: 0, totalOccupiedTime: 0 }
    ];

    let waitingShips = [];
    let shipsInPort = []; // Ships currently at berths
    let completedShips = []; // Ships that have finished processing
    let simulationTime = 0;
    let totalProcessedCargo = 0;
    let nextShipId = 1;
    let shipArrivalTimer = 0; // Initial arrival happens quickly
    let eventTimer = 0; // Initial event happens quickly

    const baseShipArrivalRate = 0.25; // Average ships per hour (1 ship every 4 hours)
    const baseEventRate = 0.1; // Average event per hour (1 event every 10 hours)
    const timeUnit = 1000; // Simulation speed in milliseconds per hour (adjust for faster/slower game)
    let gameInterval = null;

    // DOM Elements
    const simulationTimeEl = document.getElementById('simulation-time');
    const throughputEl = document.getElementById('throughput');
    const avgTurnaroundEl = document.getElementById('avg-turnaround');
    const avgWaitEl = document.getElementById('avg-wait');
    const berthUtilizationEl = document.getElementById('berth-utilization');
    const waitingShipsListEl = document.getElementById('waiting-ships-list');
    const selectShipEl = document.getElementById('select-ship');
    const selectBerthEl = document.getElementById('select-berth');
    const assignButtonEl = document.getElementById('assign-button');
    const nextTurnButtonEl = document.getElementById('next-turn-button');
    const messageListEl = document.getElementById('message-list');
    const toggleExplanationButton = document.getElementById('toggleExplanationButton');
    const explanationDiv = document.getElementById('explanation');
    const berthElements = document.querySelectorAll('.berth');


    // --- Simulation Logic ---

    function generateShip(isLarge = false) {
        const cargoAmount = isLarge ? Math.floor(Math.random() * 8000) + 6000 : Math.floor(Math.random() * 5000) + 1000; // 1000-6000, or 6000-14000 for large
        const processingTimeNeeded = isLarge ? Math.max(10, Math.floor(cargoAmount / 500)) : Math.max(3, Math.floor(cargoAmount / 500)); // 3-12, or 10-28 hours approx
        const ship = {
            id: nextShipId++,
            cargoAmount: cargoAmount,
            arrivalTime: simulationTime,
            processingTimeNeeded: processingTimeNeeded,
            timeRemaining: processingTimeNeeded, // Time left at berth
            waitTime: 0, // Time spent waiting for a berth
            turnaroundTime: 0, // Total time in port
            assignedBerthId: null,
            assignmentTime: null, // Time assigned to berth
            isLarge: isLarge
        };
        waitingShips.push(ship);
        addMessage(`אונייה ${isLarge ? 'ענק' : ''} חדשה הגיעה (ID: ${ship.id}, מטען: ${ship.cargoAmount.toLocaleString()} טון) וממתינה לרציף.`);

        // Add animation class to the new ship list item (handled in updateUI)
    }

    function assignShipToBerth(shipId, berthId) {
        const shipIndex = waitingShips.findIndex(ship => ship.id === shipId);
        const berthIndex = berths.findIndex(berth => berth.id === berthId);

        if (shipIndex === -1) {
            addMessage('שגיאה בהקצאה: האונייה אינה ברשימת ההמתנה.', 'error');
            return false;
        }
         if (berthIndex === -1 || berths[berthIndex].occupiedBy !== null) {
             addMessage('שגיאה בהקצאה: הרציף אינו פנוי או לא קיים.', 'error');
             return false;
         }

        const ship = waitingShips.splice(shipIndex, 1)[0];
        ship.assignedBerthId = berthId;
        ship.assignmentTime = simulationTime;
        ship.waitTime = simulationTime - ship.arrivalTime; // Calculate wait time
        berths[berthIndex].occupiedBy = ship.id;
        berths[berthIndex].timeRemaining = ship.processingTimeNeeded;
        shipsInPort.push(ship);

        addMessage(`הוקצתה אונייה ID:${ship.id} לרציף ${berthId}. זמן טיפול משוער: ${ship.processingTimeNeeded} שעות.`, 'success');

        // Visual feedback: highlight berth temporarily?
        const berthEl = document.querySelector(`.berth[data-berth-id="${berthId}"]`);
        if (berthEl) {
             berthEl.classList.add('assign-animation');
             setTimeout(() => berthEl.classList.remove('assign-animation'), 1000);
        }

        return true;
    }

    function processTurn() {
        simulationTime++;
        shipArrivalTimer--;
        eventTimer--;

        // Handle ship arrivals
        if (shipArrivalTimer <= 0) {
             generateShip(Math.random() < 0.1); // 10% chance of large ship
             // Reset timer with some randomness
             shipArrivalTimer = Math.max(2, Math.floor(Math.random() * (1 / baseShipArrivalRate) * 2.5)); // Next ship arrives in 2-10 hours approx
        }

         // Handle random events
         if (eventTimer <= 0) {
             triggerRandomEvent();
             eventTimer = Math.max(5, Math.floor(Math.random() * (1 / baseEventRate) * 2.5)); // Next event in 5-25 hours approx
         }


        // Process ships at berths
        const shipsCompletedThisTurn = [];
        shipsInPort.forEach(ship => {
            const berth = berths.find(b => b.occupiedBy === ship.id);
            if (berth) {
                 berth.totalOccupiedTime++; // Track berth utilization
                 berth.timeRemaining--;
                 ship.timeRemaining--; // Also track on ship object for display/calc

                 // Visual cue for processing progress? Could update shipEl text color or add a bar

                 if (berth.timeRemaining <= 0) {
                    // Ship processing complete
                    shipsCompletedThisTurn.push(ship.id);
                    berth.occupiedBy = null;
                    berth.timeRemaining = 0;
                    ship.turnaroundTime = simulationTime - ship.arrivalTime; // Calculate total time
                    completedShips.push(ship);
                    totalProcessedCargo += ship.cargoAmount;
                    addMessage(`אונייה ID:${ship.id} סיימה טיפול ברציף ${berth.id} ועזבה את הנמל. מטען: ${ship.cargoAmount.toLocaleString()} טון.`, 'success');

                    // Visual feedback: remove occupied class immediately for next update cycle
                    const berthEl = document.querySelector(`.berth[data-berth-id="${berth.id}"]`);
                    if (berthEl) {
                         berthEl.classList.remove('occupied');
                         // Could add a "departure" animation class here
                    }
                 }
            }
        });

        // Remove completed ships from shipsInPort
        shipsInPort = shipsInPort.filter(ship => !shipsCompletedThisTurn.includes(ship.id));

        // Update wait time for waiting ships
        waitingShips.forEach(ship => {
            ship.waitTime++;
        });

        updateUI();
        calculateKPIs();
    }

    function triggerRandomEvent() {
        const events = [
            { text: "סערה בים: קצב הפריקה הואט בכל הרציפים הפעילים לשעתיים.", effect: 'slowdown', duration: 2 },
            { text: "תקלה קלה בעגורן ברציף: הטיפול באונייה מתעכב בשעתיים.", effect: 'delay', target: 'berth', duration: 2 },
            { text: "תקלה חמורה בעגורן ברציף: הטיפול באונייה מתעכב בחמש שעות.", effect: 'delay', target: 'berth', duration: 5, type: 'warning' },
            { text: "אוניית ענק בלתי צפויה הגיעה! דורשת רציף וזמן טיפול ארוכים מהרגיל.", effect: 'new_large_ship' },
            { text: "עומס בשערי היציאה: קצב שחרור מטענים מהנמל ליבשה הואט.", effect: 'outbound_delay', type: 'info' }, // Abstract effect for now
            { text: "התייעלות תפעולית רגעית: קצב הפריקה/טעינה ברציפים השתפר לשעתיים.", effect: 'speedup', duration: 2, type: 'success' }
        ];

        // Filter events that require ships at berth if none are present
        const possibleEvents = events.filter(event =>
            !(event.effect === 'slowdown' || event.effect === 'delay' || event.effect === 'speedup') || shipsInPort.length > 0
        );

        if (possibleEvents.length === 0) {
            // No events can trigger if no ships are being processed
             addMessage(`[שעה ${simulationTime}] אין אירועים מיוחדים כרגע.`, 'info');
             return;
        }

        const event = possibleEvents[Math.floor(Math.random() * possibleEvents.length)];
        let message = event.text;
        let messageType = event.type || 'info';

        if (event.effect === 'delay' && event.target === 'berth') {
            const targetShip = shipsInPort[Math.floor(Math.random() * shipsInPort.length)];
            const berth = berths.find(b => b.occupiedBy === targetShip.id);
            if (berth) {
                 berth.timeRemaining += event.duration;
                 targetShip.timeRemaining += event.duration;
                 message = `🚩 תקלה בעגורן ברציף ${berth.id}: הטיפול באונייה ID:${targetShip.id} מתעכב ב-${event.duration} שעות.`;
                 messageType = event.type || 'warning';
            } else {
                 // This should not happen with the filter, but as a fallback
                 addMessage(`[שעה ${simulationTime}] ניסיון לאירוע תקלה - לא התרחש כי אין אוניות ברציפים.`, 'info');
                 return;
            }
        } else if (event.effect === 'slowdown') {
             message = `⛈️ סערה בים: קצב הפריקה הואט בכל הרציפים הפעילים ל-${event.duration} שעות. זמן הטיפול מתארך.`;
             messageType = event.type || 'warning';
             shipsInPort.forEach(ship => {
                const berth = berths.find(b => b.occupiedBy === ship.id);
                if (berth) {
                    // Add extra time proportional to remaining time, or a fixed small amount
                    const delay = Math.max(1, Math.ceil(ship.timeRemaining * 0.15)); // 15% delay, min 1 hour
                    ship.timeRemaining += delay;
                    berth.timeRemaining += delay;
                }
             });

        } else if (event.effect === 'speedup') {
             message = `✨ התייעלות תפעולית: קצב הפריקה/טעינה השתפר ל-${event.duration} שעות! זמן הטיפול מתקצר.`;
             messageType = event.type || 'success';
             shipsInPort.forEach(ship => {
                const berth = berths.find(b => b.occupiedBy === ship.id);
                if (berth) {
                    // Reduce time proportional to remaining time, or a fixed small amount
                    const speedup = Math.max(1, Math.ceil(ship.timeRemaining * 0.1)); // 10% speedup, min 1 hour
                    ship.timeRemaining = Math.max(1, ship.timeRemaining - speedup); // Ensure time doesn't go below 1
                    berth.timeRemaining = Math.max(1, berth.timeRemaining - speedup);
                }
             });
        }
        else if (event.effect === 'new_large_ship') {
             generateShip(true); // Already generates and adds message
             return; // Skip adding message again
        } else if (event.effect === 'outbound_delay') {
             message = `🚚 עומס בשערי היציאה: תהליך שחרור המטענים מהנמל מתעכב.`;
             messageType = event.type || 'warning';
             // Abstract effect, no direct simulation impact in this version, but informs the player
        }

        addMessage(message, messageType);
    }


    function addMessage(text, type = 'info') {
        const li = document.createElement('li');
        li.textContent = `[שעה ${simulationTime.toString().padStart(3, '0')}] ${text}`; // Pad time for alignment
        li.classList.add('message', type); // Add classes for styling

        // Add classes for animation
        li.style.opacity = 0;
        li.style.transform = 'translateY(10px)';

        // Remove placeholder if present
        const placeholder = messageListEl.querySelector('.placeholder');
        if (placeholder) {
            placeholder.remove();
        }

        messageListEl.prepend(li); // Add to the top

        // Trigger the animation
        setTimeout(() => {
            li.style.opacity = 1;
            li.style.transform = 'translateY(0)';
        }, 50); // Small delay for animation to work


        // Limit messages (optional, but good practice)
        while (messageListEl.children.length > 20) { // Keep slightly more messages
            messageListEl.removeChild(messageListEl.lastChild);
        }
    }


    // --- UI Update ---

    function updateUI() {
        // Update Time
        simulationTimeEl.textContent = simulationTime.toString().padStart(3, '0');

        // Update Berths
        berthElements.forEach(berthEl => {
            const berthId = parseInt(berthEl.dataset.berthId);
            const berth = berths.find(b => b.id === berthId);
            const statusEl = berthEl.querySelector('.berth-status');
            const shipEl = berthEl.querySelector('.ship-at-berth');

            if (berth.occupiedBy !== null) {
                const ship = shipsInPort.find(s => s.id === berth.occupiedBy);
                 berthEl.classList.add('occupied');
                statusEl.textContent = `תפוס`;
                shipEl.innerHTML = `אונייה ID:${ship.id}<br/>(${ship.timeRemaining} שע' נותרו)`; // Use innerHTML for line break
            } else {
                berthEl.classList.remove('occupied');
                statusEl.textContent = `פנוי`;
                shipEl.textContent = '';
            }
        });

        // Update Waiting Ships List
        const currentShipIdsInList = Array.from(waitingShipsListEl.children).map(li => li.dataset.shipId).filter(id => id);

        // Remove ships that are no longer waiting
         currentShipIdsInList.forEach(shipId => {
            if (!waitingShips.find(ship => ship.id === parseInt(shipId))) {
                const liToRemove = waitingShipsListEl.querySelector(`li[data-ship-id="${shipId}"]`);
                if (liToRemove) {
                    // Optional: Add removal animation class
                    liToRemove.style.opacity = 0;
                    liToRemove.style.transform = 'translateX(-100%)';
                    setTimeout(() => liToRemove.remove(), 500); // Remove after animation
                }
            }
         });


        // Add/Update ships still waiting
        waitingShips.forEach(ship => {
            let li = waitingShipsListEl.querySelector(`li[data-ship-id="${ship.id}"]`);

            if (!li) {
                // New ship - create element and add animation class
                li = document.createElement('li');
                li.dataset.shipId = ship.id; // Store ship ID
                li.classList.add('ship-entering'); // Add initial animation class
                waitingShipsListEl.appendChild(li); // Add to DOM

                 // Trigger the entry animation
                setTimeout(() => {
                    li.classList.remove('ship-entering');
                    li.classList.add('ship-present'); // Final state class
                }, 50); // Small delay
            }

             // Update content
             li.textContent = `ID:${ship.id}${ship.isLarge ? ' (ענק)' : ''} | מטען: ${ship.cargoAmount.toLocaleString()} טון | נדרש: ${ship.processingTimeNeeded} שעות | ממתינה: ${ship.waitTime} שעות`;
             li.style.borderColor = ship.waitTime > 10 ? '#ff9800' : '#ffee58'; // Highlight ships waiting too long
             li.style.backgroundColor = ship.waitTime > 10 ? '#fff3e0' : '#fff';
        });

        // Add placeholder if no ships are waiting and no ships are animating out
        if (waitingShips.length === 0 && waitingShipsListEl.querySelectorAll('li:not(.ship-entering)').length === 0) {
             if (!waitingShipsListEl.querySelector('.placeholder')) {
                const placeholder = document.createElement('li');
                placeholder.classList.add('placeholder');
                placeholder.textContent = 'אין אוניות ממתינות כרגע.';
                waitingShipsListEl.appendChild(placeholder);
             }
        } else {
             // Remove placeholder if ships are present or animating
             const placeholder = waitingShipsListEl.querySelector('.placeholder');
             if (placeholder) placeholder.remove();
        }


        // Update Assignment Selects
        selectShipEl.innerHTML = '<option value="">-- בחר אונייה --</option>';
        waitingShips.sort((a, b) => b.waitTime - a.waitTime).forEach(ship => { // Sort by wait time (longest first)
            const option = document.createElement('option');
            option.value = ship.id;
            option.textContent = `ID:${ship.id}${ship.isLarge ? ' (ענק)' : ''} (ממתינה ${ship.waitTime} שע')`;
            selectShipEl.appendChild(option);
        });

        selectBerthEl.innerHTML = '<option value="">-- בחר רציף --</option>';
        berths.filter(berth => berth.occupiedBy === null).forEach(berth => {
            const option = document.createElement('option');
            option.value = berth.id;
            option.textContent = `רציף ${berth.id} (פנוי)`;
            selectBerthEl.appendChild(option);
        });

         // Enable/Disable Assign button
         assignButtonEl.disabled = !(selectShipEl.value && selectBerthEl.value);
    }

    // --- KPI Calculation ---

    function calculateKPIs() {
        throughputEl.textContent = totalProcessedCargo.toLocaleString(); // Format number

        // Avg Turnaround Time
        if (completedShips.length > 0) {
            const totalTurnaround = completedShips.reduce((sum, ship) => sum + ship.turnaroundTime, 0);
            avgTurnaroundEl.textContent = (totalTurnaround / completedShips.length).toFixed(1);
        } else {
            avgTurnaroundEl.textContent = 'N/A';
        }

        // Avg Wait Time (only for ships that were actually assigned and completed)
        const completedAssignedShips = completedShips.filter(ship => ship.assignmentTime !== null);
        // Also include the current wait time of waiting ships for a more dynamic KPI
        const currentWaitingTimes = waitingShips.map(ship => ship.waitTime);
        const allWaitTimes = completedAssignedShips.map(ship => ship.waitTime).concat(currentWaitingTimes);

        if (allWaitTimes.length > 0) {
             const totalWait = allWaitTimes.reduce((sum, time) => sum + time, 0);
             avgWaitEl.textContent = (totalWait / allWaitTimes.length).toFixed(1);
        }
         else {
             avgWaitEl.textContent = 'N/A';
         }


        // Berth Utilization
        if (simulationTime > 0) {
             const totalPossibleBerthTime = simulationTime * berths.length;
             const totalActualOccupiedTime = berths.reduce((sum, berth) => sum + berth.totalOccupiedTime, 0);
             berthUtilizationEl.textContent = ((totalActualOccupiedTime / totalPossibleBerthTime) * 100 || 0).toFixed(1) + '%'; // Handle division by zero
        } else {
            berthUtilizationEl.textContent = '0.0%';
        }

         // Add visual feedback for KPIs
         throughputEl.style.color = totalProcessedCargo > 0 ? '#28a745' : '#555'; // Green if > 0
         avgWaitEl.style.color = parseFloat(avgWaitEl.textContent) > 5 ? '#dc3545' : (parseFloat(avgWaitEl.textContent) > 2 ? '#ffc107' : '#28a745'); // Red/Orange/Green based on value
         avgTurnaroundEl.style.color = parseFloat(avgTurnaroundEl.textContent) > 15 ? '#dc3545' : (parseFloat(avgTurnaroundEl.textContent) > 8 ? '#ffc107' : '#28a745');
         berthUtilizationEl.style.color = parseFloat(berthUtilizationEl.textContent) > 75 ? '#ffc107' : (parseFloat(berthUtilizationEl.textContent) < 25 ? '#dc3545' : '#28a745'); // Orange if high, Red if low, Green if medium
    }

    // --- Game Loop Control ---
     function startGameLoop() {
         if (gameInterval === null) {
            gameInterval = setInterval(processTurn, timeUnit);
            nextTurnButtonEl.textContent = 'עצור סימולציה';
            nextTurnButtonEl.style.backgroundColor = '#dc3545'; // Red color for stop
            nextTurnButtonEl.prepend(createIconSpan('⛔')); // Stop icon
         } else {
            clearInterval(gameInterval);
            gameInterval = null;
            nextTurnButtonEl.textContent = 'התקדם לשעה הבאה (המשך סימולציה)';
            nextTurnButtonEl.style.backgroundColor = '#28a745'; // Green color for play
            nextTurnButtonEl.prepend(createIconSpan('⏱️')); // Clock icon
         }
     }

     function createIconSpan(icon) {
         const span = document.createElement('span');
         span.textContent = icon;
         span.classList.add('icon'); // Use the existing icon style
         return span;
     }


    // --- Event Listeners ---

    nextTurnButtonEl.addEventListener('click', startGameLoop);

    assignButtonEl.addEventListener('click', () => {
        const selectedShipId = parseInt(selectShipEl.value);
        const selectedBerthId = parseInt(selectBerthEl.value);
        if (selectedShipId && selectedBerthId) {
            assignShipToBerth(selectedShipId, selectedBerthId);
            // Reset selects after assignment
            selectShipEl.value = "";
            selectBerthEl.value = "";
            assignButtonEl.disabled = true;
             // Clear select styling
             selectShipEl.classList.remove('selected');
             selectBerthEl.classList.remove('selected');
        }
    });

    // Enable/disable assign button when selections change
    selectShipEl.addEventListener('change', () => {
        assignButtonEl.disabled = !(selectShipEl.value && selectBerthEl.value);
         // Add visual feedback
         if (selectShipEl.value) { selectShipEl.classList.add('selected'); } else { selectShipEl.classList.remove('selected'); }
    });
     selectBerthEl.addEventListener('change', () => {
        assignButtonEl.disabled = !(selectShipEl.value && selectBerthEl.value);
         // Add visual feedback
         if (selectBerthEl.value) { selectBerthEl.classList.add('selected'); } else { selectBerthEl.classList.remove('selected'); }

     });


    toggleExplanationButton.addEventListener('click', () => {
        if (explanationDiv.style.display === 'none') {
            explanationDiv.style.display = 'block';
            toggleExplanationButton.innerHTML = '<i class="icon icon-info"></i> הסתר הסבר תיאורטי';
        } else {
            explanationDiv.style.display = 'none';
            toggleExplanationButton.innerHTML = '<i class="icon icon-info"></i> הצג/הסתר הסבר תיאורטי: נמלים ימיים וניהולם';
        }
    });


    // --- Initialization ---

    function initializeSimulation() {
        // Generate initial ships arriving quickly
        for(let i = 0; i < 2; i++) {
            generateShip();
        }
        // Trigger first arrival and event soon after start
        shipArrivalTimer = Math.max(1, Math.floor(Math.random() * (1 / baseShipArrivalRate) * 1.5));
        eventTimer = Math.max(3, Math.floor(Math.random() * (1 / baseEventRate) * 1.5));


        updateUI();
        calculateKPIs();
        addMessage('ברוכים הבאים למשחק מנהל הנמל! אוניות ראשונות בדרך.', 'info');

        // Start the simulation automatically (optional, can be manual)
        // startGameLoop(); // Let's keep it manual for the first turn
        nextTurnButtonEl.prepend(createIconSpan('⏱️')); // Add icon initially
    }

    initializeSimulation(); // Start the simulation on page load

</script>
---