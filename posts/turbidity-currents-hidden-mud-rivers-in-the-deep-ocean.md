---
title: "זרמי עכירות: נהרות בוץ נסתרים במעמקי האוקיינוס"
english_slug: turbidity-currents-hidden-mud-rivers-in-the-deep-ocean
category: "מדעי הסביבה / כדור הארץ"
tags:
  - גיאולוגיה ימית
  - אוקיינוגרפיה
  - משקעים
  - קניונים תת-ימיים
  - טורבידיטים
---
<h1>זרמי עכירות: נהרות בוץ נסתרים במעמקי האוקיינוס</h1>
<p>דמיינו לרגע: מתחת לגלי הים הכחולים, במעמקי האוקיינוס האפלים, שועטים נהרות אדירים של בוץ וסחף. אלה אינם נהרות מים צלולים, אלא זרמים עמוסי משקעים, צפופים וכבדים, הסוחפים טונות של חול וטין במורד מדרונות תת-ימיים עצומים. הכוחות הנסתרים והעצמתיים האלה, המכונים <strong>זרמי עכירות</strong>, חורצים ומרסקים את פני קרקעית הים, בונים מבנים גיאולוגיים ענקיים ומשפיעים עמוקות על הנוף התת-ימי.</p>
<p>בואו נחקור את התופעה המרתקת הזו באמצעות סימולציה אינטראקטיבית.</p>

<div id="app-container">
    <h2>סימולטור זרם עכירות</h2>
    <p>התנסו בהשפעת גורמים שונים על היווצרות והתנהגות זרם עכירות.</p>
    <div class="controls">
        <div class="control-group">
            <label for="sediment">כמות משקעים:</label>
            <input type="range" id="sediment" min="1" max="10" value="5">
            <span id="sediment-value" class="control-value">5 (בינוני)</span>
        </div>

        <div class="control-group">
            <label for="slope">זווית מדרון:</label>
            <input type="range" id="slope" min="5" max="30" value="15">
            <span id="slope-value" class="control-value">15&deg; (מתון)</span>
        </div>

        <div class="control-group">
             <label for="trigger">טריגר (גורם מפעיל):</label>
             <select id="trigger">
                 <option value="small_quake">רעידת אדמה קלה</option>
                 <option value="large_storm">סערה גדולה</option>
                 <option value="river_flood">הצפה מנהר</option>
                 <option value="submarine_slide">מפולת תת-ימית</option>
             </select>
             <span id="trigger-desc" class="control-desc">מפעיל את הזרימה.</span>
         </div>

        <div class="control-group">
            <label for="canyon">תוואי קניון תת-ימי:</label>
            <input type="checkbox" id="canyon">
            <span id="canyon-desc" class="control-desc">מנתב ומאיץ את הזרם.</span>
        </div>

        <div class="button-group">
            <button id="run-sim" class="sim-button">הפעל זרם</button>
            <button id="reset-sim" class="sim-button" disabled>אפס סימולציה</button>
        </div>
    </div>

    <div class="simulation-area">
        <div class="water-surface">פני המים</div>
        <div class="seabed">
            <div class="shelf">מדף יבשתי</div>
            <div class="slope">
                <div class="slope-base">מדרון יבשתי</div>
                <div class="canyon-feature" style="display: none;"></div>
            </div>
            <div class="abyssal-plain">מישור תהומות</div>
        </div>
         <!-- Visual effects and current go above seabed -->
        <div id="erosion-effect" class="erosion-effect"></div>
        <div id="deposition-effect" class="deposition-effect"></div>
        <div id="turbidity-current" class="turbidity-current"></div>
    </div>
     <div class="sim-output" id="sim-output">
         <p>הגדר את הפרמטרים ולחץ "הפעל זרם".</p>
     </div>
</div>

<button id="toggle-explanation" class="toggle-button">הצג הסבר מורחב</button>

<div id="explanation" style="display: none;">
    <h2>הסבר מורחב: זרמי עכירות</h2>

    <h3>מהם זרמי עכירות?</h3>
    <p>זרמי עכירות הם זרמים מהירים, צפופים ועמוסי משקעים (חול, בוץ, סחף) הזורמים במורד מדרונות תת-ימיים תלולים, לרוב באזורים שולי היבשת. הזרמים כבדים מצפיפות המים שמסביב עקב ריכוז המשקעים הגבוה, ולכן הם נעים כ"נהר" נפרד ומוגדר בתוך גוף המים העמוק של האוקיינוס. הם מסוגלים להגיע למהירויות גבוהות ביותר ולהעביר כמויות אדירות של חומר למרחקים עצומים.</p>

    <h3>כיצד נוצרים זרמי עכירות?</h3>
    <p>היווצרות זרם עכירות מחייבת שני תנאים עיקריים:</p>
    <ol>
        <li>**צבירת משקעים:** הצטברות של חומר משקעי לא יציב – לרוב חול וטין המובאים מנהרות או נסחפים לאורך החוף – על מדרון תת-ימי, בדרך כלל על שולי המדף היבשתי.</li>
        <li>**טריגר (גורם מפעיל):** אירוע שמערער את יציבות המשקעים הרכים וגורם להם להתמוטט ולגלוש במהירות במורד המדרון. גורמים אלה יכולים להיות חיצוניים או פנימיים.</li>
    </ol>

    <h3>סוגי טריגרים נפוצים:</h3>
    <p>הטריגרים המפעילים זרמי עכירות יכולים להיות מגוונים ועוצמתיים:</p>
    <ul>
        <li>**רעידות אדמה:** רעידות תת-ימיות או גלי צונאמי הנוצרים בעקבותיהן יכולים לערער בפתאומיות הצטברויות משקעים על המדרונות ולגרום למפולות ענק.</li>
        <li>**סופות גדולות:** גלי סערה עזים המגיעים לעומקים משמעותיים יכולים לערבל משקעים רדודים ולהתחיל גלישה במדרון, במיוחד אם הם מתרחשים בו זמנית עם גלי גאות חזקים.</li>
        <li>**מפולות תת-ימיות:** גושים גדולים של משקעים או סלעים שקורסים במורד המדרון תחת כוח הכבידה יכולים להפעיל זרם עכירות עוקב על ידי ערבול המשקעים בדרכם.</li>
        <li>**הצפות יבשתיות חריגות:** כמויות גדולות במיוחד של מים וסחף המובלות על ידי נהרות גדולים ונשפכות לים יכולות ליצור עומס כבד על שולי המדף ולהפעיל גלישת משקעים.</li>
    </ul>

    <h3>התנהגות הזרם ותנועתו</h3>
    <p>מרגע שהזרם נוצר וצובר משקעים, הוא הופך להיות צפוף וכבד יותר מהמים הסובבים אותו. כוח הכבידה מושך אותו במהירות במורד המדרון התת-ימי. הזרם זורם קרוב לקרקעית, לעיתים קרובות בתוך ערוצים או קניונים תת-ימיים קיימים, מה שמגביר את מהירותו ויכולת הסחיפה שלו. כשהוא מגיע לשטח מישורי יותר, כמו מישור התהומות העמוק, הזרם מאט בהדרגה, מאבד אנרגיה, והמשקעים שהוא נושא מתחילים לשקוע על קרקעית הים.</p>

    <h3>השפעות גיאולוגיות מרכזיות</h3>
    <p>זרמי עכירות אינם רק תופעה חולפת; הם מהווים כוח גיאולוגי מרכזי המעצב באופן דרמטי את נוף קרקעית הים לאורך מיליוני שנים:</p>
    <ul>
        <li>**סחיפה ויצירת קניונים:** במהלך זרימתם המהירה והטורבולנטית במורד המדרונות, זרמי העכירות נושאים עמם כוח סחיפה עצום. הם חורצים, מעמיקים ומרחיבים ערוצים וקניונים תת-ימיים ענקיים – חלקם גדולים יותר מקניונים יבשתיים ידועים.</li>
        <li>**שקיעה ויצירת טורבידיטים:** כשהזרם מאט ומאבד את אנרגייתו, המשקעים שהוא נושא שוקעים על קרקעית הים. תהליך השקיעה מתרחש בסדר אופייני: המשקעים הכבדים והגסים יותר שוקעים ראשונים, ואחריהם העדינים יותר. שקיעה זו יוצרת יחידות סלע שכובות אופייניות הנקראות **טורבידיטים**.</li>
    </ul>

    <h3>מבנה הטורבידיט האופייני (סדרת בּוּמָה - Bouma sequence)</h3>
    <p>טורבידיט קלאסי הוא למעשה תיעוד גיאולוגי של אירוע זרם עכירות יחיד. הוא מציג סדרת שכבות אופיינית המכונה "סדרת בומה", מלמטה (השכבה הראשונה לשקוע) למעלה (האחרונה):</p>
    <ol>
        <li>**Ta:** החלק התחתון והגס ביותר, לרוב חול גס עד בינוני. שוקע מהרגע שהזרם מתחיל לאבד אנרגיה, מייצג את שלב הזרימה הטורבולנטית ביותר.</li>
        <li>**Tb:** חול דק עד בינוני, בעל למינציה (שכוב דק) מקבילה. מייצג האטה מסוימת בזרימה.</li>
        <li>**Tc:** חול דק עד סילט, בעל למינציה אלכסונית או מבנים מעוותים (קונבולוציות) כתוצאה מזרימה ערבולית נוספת בעת האטה.</li>
        <li>**Td:** סילט עדין עד חרסית, בעל למינציה מקבילה עדינה. שקיעה איטית יותר מזרם שכמעט איבד את כל אנרגייתו.</li>
        <li>**Te:** חרסית דקה (פליטי), לעיתים קרובות קשה להבדילה מהמשקעים הרגילים (hemi-pelagic) השוקעים באיטיות בין אירועי זרמי עכירות. מייצגת שקיעה איטית מאוד לאחר שהזרם חלף או כחלק מהשקיעה הרגילה ברקע.</li>
    </ol>
    <p>חשוב לציין שלא כל הטורבידיטים מכילים את כל חמשת השכבות של סדרת בומה. עוצמת הזרם, כמות המשקעים הזמינים והמרחק ממקור הזרם ישפיעו על השכבות שיתפתחו ועל עובין.</p>

    <h3>חשיבותם של זרמי עכירות במחקר הגיאולוגי</h3>
    <p>לימוד זרמי עכירות והטורבידיטים שהם מותירים אחריהם הוא קריטי להבנת תהליכים גיאולוגיים ימיים. הם מספקים מידע על מחזורי השקיעה הימיים, העברת חומרים מיבשה לעומק האוקיינוס, ומשמשים כעדויות לאירועים קטקליזמיים שהתרחשו בעבר (כמו רעידות אדמה וסופות ענק). שכבות טורבידיטים שנחקרות בקידוחים ימיים מאפשרות לתיארוך אירועי עבר ובכך מסייעות בשחזור היסטוריית כדור הארץ, כולל שינויי אקלים קדומים.</p>

    <h3>השפעה על תשתית ימית מעשה ידי אדם</h3>
    <p>למרות שהם תופעה טבעית קדומה, זרמי עכירות מהווים גם סיכון לתשתיות מודרניות המונחות על קרקעית הים, כגון כבלי תקשורת תת-ימיים וצינורות נפט/גז. זרם עכירות חזק יכול לגרום נזק עצום לכבלים על ידי קריעתם או קבורתם תחת שכבות עבות של משקעים, מה שעלול לגרום להפרעות בתקשורת בינלאומית.</p>

</div>

<style>
    :root {
        --shelf-color: #d2b48c;
        --slope-color-base: #8b4513;
        --slope-color-dark: #6b350f;
        --canyon-color: #4a260b;
        --abyssal-color: #3a5a77; /* Deeper blue-grey */
        --water-color: #81d4fa; /* Light bright blue */
        --water-surface-color: rgba(129, 212, 250, 0.7);
        --current-color: rgba(101, 67, 33, 0.8); /* Brown */
        --erosion-color: rgba(239, 83, 80, 0.6); /* Light red */
        --deposition-color-start: #757575; /* Grey */
        --deposition-color-end: #e0e0e0; /* Lighter grey */

        --primary-color: #1a237e; /* Dark blue */
        --secondary-color: #42a5f5; /* Blue */
        --accent-color: #4caf50; /* Green */
        --text-color: #333;
        --bg-color: #f5f5f5; /* Light grey */
        --card-bg-color: #ffffff;
        --border-color: #cfd8dc; /* Light grey-blue */

        --sim-height: 300px;
        --water-surface-height: 25px;
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        margin: 0;
        padding: 20px;
        direction: rtl;
        text-align: right;
        background-color: var(--bg-color);
        color: var(--text-color);
        overflow-x: hidden; /* Prevent horizontal scroll from animations */
    }

    h1, h2, h3 {
        color: var(--primary-color);
        text-align: center;
        margin-bottom: 15px;
        font-weight: bold;
    }
     h1 {
         margin-bottom: 5px;
         font-size: 2em;
     }
     h2 {
         font-size: 1.6em;
         margin-top: 20px;
     }
     h3 {
         font-size: 1.3em;
         margin-top: 25px;
         border-bottom: 1px solid var(--border-color);
         padding-bottom: 5px;
         color: var(--secondary-color);
         text-align: right;
     }

    p {
        margin-bottom: 15px;
    }

    #app-container, #explanation {
        margin-top: 20px;
        padding: 25px;
        border-radius: 12px;
        background-color: var(--card-bg-color);
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border: 1px solid var(--border-color);
    }
     #app-container h2 {
         margin-top: 0;
         margin-bottom: 10px;
     }
     #app-container > p {
         text-align: center;
         color: #555;
         font-style: italic;
         margin-bottom: 25px;
     }


    .controls {
        margin-bottom: 30px;
        padding: 20px;
        background-color: #e3f2fd; /* Very light blue */
        border-radius: 8px;
        text-align: right;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 15px 20px; /* Row and column gap */
        align-items: center;
    }
    .control-group {
        display: flex;
        flex-direction: column;
        align-items: flex-start; /* Align items to the right in RTL */
    }

    .controls label {
        display: block;
        margin-bottom: 5px;
        font-weight: bold;
        color: var(--primary-color);
        font-size: 1em;
    }
     .control-value {
         display: block;
         font-size: 0.9em;
         color: #555;
         margin-top: 3px;
         text-align: center;
         width: 100%;
     }
      .control-desc {
          display: block;
          font-size: 0.85em;
          color: #777;
          margin-top: 5px;
      }

    .controls input[type="range"] {
        width: 100%; /* Make range take full width */
        margin-left: 0;
        direction: ltr;
        accent-color: var(--secondary-color);
        cursor: pointer;
    }
     .controls input[type="range"]::-webkit-slider-thumb {
         -webkit-appearance: none;
         appearance: none;
         width: 18px;
         height: 18px;
         background: var(--secondary-color);
         border: 2px solid var(--primary-color);
         border-radius: 50%;
         cursor: pointer;
         margin-top: -6px; /* Keep thumb centered */
         box-shadow: 0 0 5px rgba(0,0,0,0.2);
     }
     .controls input[type="range"]::-moz-range-thumb {
         width: 18px;
         height: 18px;
         background: var(--secondary-color);
         border: 2px solid var(--primary-color);
         border-radius: 50%;
         cursor: pointer;
         box-shadow: 0 0 5px rgba(0,0,0,0.2);
     }

     .controls select {
        width: 100%; /* Make select take full width */
        padding: 8px;
        border: 1px solid var(--border-color);
        border-radius: 5px;
        background-color: white;
        font-size: 1em;
        color: var(--text-color);
        cursor: pointer;
     }

     .controls input[type="checkbox"] {
        margin-right: 0; /* Adjust for RTL */
        margin-left: 10px; /* Add space to the left */
        vertical-align: middle;
        transform: scale(1.3); /* Make checkbox larger */
        accent-color: var(--accent-color);
        cursor: pointer;
     }
    .control-group label[for="canyon"] {
        display: inline-block; /* Keep label next to checkbox */
         margin-bottom: 0;
         vertical-align: middle;
    }
     .control-group #canyon-desc {
         margin-top: 5px;
     }


    .button-group {
        grid-column: 1 / -1; /* Span across all columns */
        display: flex;
        justify-content: center; /* Center buttons */
        gap: 20px; /* Space between buttons */
        margin-top: 20px;
    }

    .sim-button {
        padding: 10px 20px;
        background-color: var(--secondary-color);
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
    }
    .sim-button:hover:not(:disabled) {
        background-color: #1e88e5; /* Darker blue */
        transform: translateY(-2px);
    }
     .sim-button:active:not(:disabled) {
         transform: translateY(0);
     }
    .sim-button:disabled {
        background-color: var(--border-color);
        cursor: not-allowed;
        box-shadow: none;
    }

    .simulation-area {
        position: relative;
        width: 100%;
        height: var(--sim-height);
        border: 2px solid var(--primary-color);
        background: linear-gradient(to bottom, var(--water-color) 0%, var(--water-color) var(--water-surface-height), #42a5f5 100%); /* Water gradient */
        overflow: hidden;
        direction: ltr; /* Simulation area visually LTR */
        border-radius: 8px;
        box-shadow: inset 0 0 15px rgba(0,0,0,0.3);
        margin-top: 20px;
    }
     .water-surface {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: var(--water-surface-height);
        background: linear-gradient(to bottom, var(--water-surface-color) 0%, rgba(129, 212, 250, 0.4) 100%);
        text-align: center;
        font-size: 0.8em;
        color: var(--primary-color);
        z-index: 5; /* Above everything */
        line-height: var(--water-surface-height);
        box-sizing: border-box;
        text-shadow: 1px 1px 1px rgba(255,255,255,0.5);
        border-bottom: 1px solid rgba(0,0,0,0.1);
     }
    .seabed {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: calc(var(--sim-height) - var(--water-surface-height));
        background-color: var(--abyssal-color); /* Default deep base */
        display: flex;
        z-index: 1;
    }
    .shelf {
        flex-basis: 25%;
        background-color: var(--shelf-color);
        position: relative;
        overflow: hidden;
        border-right: 2px solid var(--slope-color-base);
        box-sizing: border-box;
        text-align: center;
        color: var(--text-color);
        font-size: 0.9em;
        text-shadow: 1px 1px 0 rgba(255,255,255,0.5);
        display: flex;
        align-items: flex-end;
        justify-content: center;
        padding-bottom: 10px;
        font-weight: bold;
        border-bottom: 3px solid var(--slope-color-base); /* Visual break */
    }
    .slope {
        flex-basis: 35%;
        background: linear-gradient(to bottom right, var(--slope-color-base) 0%, var(--slope-color-base) 50%, var(--slope-color-dark) 100%);
        position: relative;
        overflow: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.9em;
        color: #eee;
        text-shadow: 1px 1px 0 rgba(0,0,0,0.5);
        font-weight: bold;
        border-bottom: 3px solid var(--abyssal-color); /* Visual break */
    }
     .canyon-feature {
        position: absolute;
        bottom: 0;
        left: 10%; /* Start the canyon partway down the slope section */
        width: 80%; /* Canyon width */
        height: 100%;
        background-color: var(--canyon-color);
        z-index: 2; /* Above slope base */
        text-align: center;
        color: #ccc;
        font-size: 0.8em;
        padding-top: 50px;
        box-sizing: border-box;
        font-weight: normal;
        /* Canyon shape effect - could use clip-path or just visual color */
     }
    .abyssal-plain {
        flex-basis: 40%;
        background-color: var(--abyssal-color);
        position: relative;
        overflow: hidden;
        text-align: center;
        color: #eee;
        font-size: 0.9em;
        text-shadow: 1px 1px 0 rgba(0,0,0,0.5);
        font-weight: bold;
    }
    .turbidity-current {
        position: absolute;
        bottom: 0;
        left: 25%; /* Start at the end of the shelf */
        width: 50px; /* Initial size */
        height: 30px;
        background: var(--current-color);
        /* Use repeating gradient or texture for flow illusion */
        background: repeating-linear-gradient(
            0deg,
            var(--current-color),
            rgba(120, 80, 40, 0.8) 10px,
            var(--current-color) 20px
        );
        background-size: 100% 20px; /* Control texture size */
        border-radius: 5px;
        z-index: 3;
        display: none;
        transform-origin: bottom left;
        opacity: 1;
        /* Animation for flow texture */
         animation: flow-texture 0.5s linear infinite paused; /* Paused until sim runs */
         box-shadow: 0 0 10px rgba(0,0,0,0.5);
    }

     @keyframes flow-texture {
         from { background-position: 0 0; }
         to { background-position: 0 20px; } /* Move texture down */
     }

     .erosion-effect {
        position: absolute;
        bottom: 0;
        left: 25%; /* Start at slope */
        width: 35%; /* Covers the slope area width */
        height: calc(var(--sim-height) - var(--water-surface-height)); /* Cover the slope area height below water surface */
        background-color: var(--erosion-color);
        z-index: 4; /* Above seabed, below current */
        display: none;
        opacity: 0;
        mix-blend-mode: multiply; /* Blend with background */
     }
    .deposition-effect {
        position: absolute;
        bottom: 0;
        left: 60%; /* Start at abyssal plain */
        width: 40%; /* Covers the abyssal plain area width */
        height: 0;
        background: linear-gradient(to top, var(--deposition-color-start), var(--deposition-color-end)); /* Simple layer gradient */
        z-index: 4; /* Above seabed, below current */
        display: none;
        text-align: center;
        color: var(--primary-color);
        font-weight: bold;
        font-size: 0.9em;
        overflow: hidden;
        box-sizing: border-box;
        padding-top: 10px;
        text-shadow: 1px 1px 0 rgba(255,255,255,0.5);
        opacity: 0.9;
        /* Add hint of layers */
         background-size: 100% 30px; /* Size of a layer block for gradient */
         background-repeat: repeat-y;
    }

     .sim-output {
         margin-top: 20px;
         padding: 15px;
         border: 1px dashed var(--border-color);
         border-radius: 8px;
         background-color: #fff9c4; /* Light yellow */
         text-align: center;
         color: #5d4037; /* Brown */
         font-weight: bold;
     }
      .sim-output p {
          margin: 0;
      }


    .toggle-button {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        background-color: var(--accent-color);
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    .toggle-button:hover {
        background-color: #388e3c; /* Darker green */
        transform: translateY(-2px);
    }
    .toggle-button:active {
        transform: translateY(0);
    }


    #explanation h3 {
        color: var(--secondary-color);
        margin-top: 20px;
        text-align: right;
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 5px;
    }
    #explanation ul, #explanation ol {
        margin-right: 25px;
        padding-right: 0;
        text-align: right;
    }
     #explanation ul li, #explanation ol li {
        margin-bottom: 10px;
        padding-right: 0;
        position: relative;
        list-style: none;
        line-height: 1.5;
     }
      #explanation ul li::before {
         content: "• ";
         position: absolute;
         right: -25px;
         color: var(--secondary-color);
         font-weight: bold;
         font-size: 1.2em;
         top: -2px;
      }
       #explanation ol li {
           counter-increment: list-item;
       }
       #explanation ol li::before {
         content: counter(list-item) ". ";
         position: absolute;
         right: -25px;
         color: var(--secondary-color);
         font-weight: bold;
         font-size: 1.1em;
         top: -2px;
       }

</style>

<script>
    const sedimentRange = document.getElementById('sediment');
    const sedimentValueSpan = document.getElementById('sediment-value');
    const slopeRange = document.getElementById('slope');
    const slopeValueSpan = document.getElementById('slope-value');
    const triggerSelect = document.getElementById('trigger');
    const canyonCheckbox = document.getElementById('canyon');
    const runButton = document.getElementById('run-sim');
    const resetButton = document.getElementById('reset-sim');
    const turbidityCurrentDiv = document.getElementById('turbidity-current');
    const erosionEffectDiv = document.getElementById('erosion-effect');
    const depositionEffectDiv = document.getElementById('deposition-effect');
    const canyonFeatureDiv = document.querySelector('.canyon-feature');
    const simOutputDiv = document.getElementById('sim-output');

    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    // Mapping slider values to descriptions
    const sedimentDescriptions = ["מינימלי", "נמוך מאוד", "נמוך", "בינוני-נמוך", "בינוני", "בינוני-גבוה", "גבוה", "גבוה מאוד", "כמות גדולה", "כמות עצומה"];
    const slopeDescriptions = ["מאוד מתון", "מתון", "מעט תלול", "תלול", "תלול מאוד", "קיצוני"];

    // Update span values and descriptions when range sliders change
    sedimentRange.addEventListener('input', () => {
        const value = parseInt(sedimentRange.value);
        sedimentValueSpan.textContent = `${value} (${sedimentDescriptions[value - 1]})`;
    });
    slopeRange.addEventListener('input', () => {
        const value = parseInt(slopeRange.value);
        let desc = "";
        if (value <= 10) desc = slopeDescriptions[0];
        else if (value <= 15) desc = slopeDescriptions[1];
        else if (value <= 20) desc = slopeDescriptions[2];
        else if (value <= 25) desc = slopeDescriptions[3];
        else if (value <= 28) desc = slopeDescriptions[4];
        else desc = slopeDescriptions[5];
        slopeValueSpan.textContent = `${value}° (${desc})`;
    });

    // Toggle explanation visibility
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מורחב' : 'הצג הסבר מורחב';
         if (isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
         }
    });

    // Show/hide canyon visual based on checkbox
    canyonCheckbox.addEventListener('change', () => {
        canyonFeatureDiv.style.display = canyonCheckbox.checked ? 'block' : 'none';
        // Optional: Add a class to slope for specific canyon styling if needed
        // canyonFeatureDiv.parentElement.classList.toggle('has-canyon', canyonCheckbox.checked);
    });

     // --- Simulation Logic (Enhanced Visuals and Animations) ---

    function runSimulation() {
        // Disable controls during simulation
        runButton.disabled = true;
        resetButton.disabled = false;
        sedimentRange.disabled = true;
        slopeRange.disabled = true;
        triggerSelect.disabled = true;
        canyonCheckbox.disabled = true;

        // Reset previous simulation effects visually *before* starting new one
        resetSimulationVisuals(false);

        simOutputDiv.innerHTML = "<p>מתחיל סימולציה...</p>";


        const sediment = parseInt(sedimentRange.value);
        const slope = parseInt(slopeRange.value);
        const trigger = triggerSelect.value;
        const hasCanyon = canyonCheckbox.checked;

        // --- Calculate simulated parameters ---
        // Base speed affected by slope, sediment, trigger. Canyon increases speed.
        let speedFactor = 0.8 + (slope / 30) * 1.2 + (sediment / 10) * 0.5;
        if (trigger === 'large_storm' || trigger === 'submarine_slide') speedFactor *= 1.4;
        if (trigger === 'small_quake') speedFactor *= 1.1;
        if (trigger === 'river_flood') speedFactor *= 1.05;
        if (hasCanyon) speedFactor *= 1.3; // Canyon effect

        speedFactor = Math.min(3.0, speedFactor); // Cap speed factor

        // Erosion factor: Affected by speed, sediment, slope. Stronger with canyon.
        let erosionFactor = (speedFactor / 3.0) * 0.7 + (sediment / 10) * 0.3;
         if (hasCanyon) erosionFactor = Math.min(1.5, erosionFactor * 1.5); // Canyon enhances erosion significantly, cap at 1.5x visual
        erosionFactor = Math.min(1.0, erosionFactor); // Cap visual erosion width at 100% of slope section

        // Deposition amount: Affected by sediment mainly. Faster current spreads thinner deposit.
        let depositionHeightFactor = (sediment / 10) * 1.8; // More sediment = potentially thicker deposit
         depositionHeightFactor /= Math.max(0.7, speedFactor * 0.6); // Inverse relationship with speed (faster = thinner, spread further)
         depositionHeightFactor = Math.min(1.0, depositionHeightFactor); // Cap visual deposition height (relative to abyssal section height)

        // Current size/visual thickness: Based on sediment and trigger intensity
        let currentHeight = 30 + sediment * 6; // Base 30px + up to 60px
        let currentWidth = 60 + sediment * 10; // Base 60px + up to 100px
         if (trigger === 'submarine_slide') {
             currentHeight *= 1.5; // Larger initial mass
             currentWidth *= 1.2;
         }
        currentHeight = Math.min(100, currentHeight); // Cap visual size
        currentWidth = Math.min(150, currentWidth);

        // Animation durations (inverse of speed)
        const slopeDuration = 5000 / speedFactor; // Time to traverse slope
        const abyssalDuration = 6000 / speedFactor; // Time to traverse abyssal plain and slow down

        // --- Start Simulation Visuals ---

        // Initial state for animation
        turbidityCurrentDiv.style.display = 'block';
        turbidityCurrentDiv.style.width = `${currentWidth * 0.1}px`; // Start small
        turbidityCurrentDiv.style.height = `${currentHeight * 0.1}px`; // Start small
        turbidityCurrentDiv.style.left = '25%'; // Start at shelf edge
        turbidityCurrentDiv.style.bottom = '0';
        turbidityCurrentDiv.style.opacity = 0.5; // Start slightly transparent
        turbidityCurrentDiv.style.transform = 'translateX(0)'; // Reset transform
        turbidityCurrentDiv.style.backgroundPosition = '0 0'; // Reset texture position
        turbidityCurrentDiv.style.animationPlayState = 'running'; // Start flow texture animation

        simOutputDiv.innerHTML = "<p>זרימה מתחילה במדף היבשתי...</p>";


        // Phase 1: Growth and initial movement (quick)
        turbidityCurrentDiv.animate([
            { width: `${currentWidth * 0.1}px`, height: `${currentHeight * 0.1}px`, opacity: 0.5 },
            { width: `${currentWidth}px`, height: `${currentHeight}px`, opacity: 1 }
        ], {
            duration: 600,
            easing: 'ease-out',
            iterations: 1,
            fill: 'forwards'
        }).onfinish = () => {
             simOutputDiv.innerHTML = "<p>הזרם שועט במורד המדרון...</p>";

             // Phase 2: Move down slope (main animation)
             const slopeStartX = 25; // %
             const slopeEndX = 60; // %
             const slopeDistance = slopeEndX - slopeStartX; // % of total width
             const currentMidpoint = (currentWidth / 2) / turbidityCurrentDiv.parentElement.offsetWidth * 100; // Midpoint offset in %

             turbidityCurrentDiv.animate([
                 { left: `${slopeStartX}%` }, // Start at shelf edge
                 { left: `${slopeEndX}%` }   // End at slope end
             ], {
                 duration: slopeDuration,
                 easing: 'linear',
                 iterations: 1,
                 fill: 'forwards'
             }).onfinish = () => {
                  simOutputDiv.innerHTML = "<p>הזרם מגיע למישור התהומות ומתחיל לשקוע...</p>";
                  // Stop flow texture animation after reaching abyssal plain
                  turbidityCurrentDiv.style.animationPlayState = 'paused';


                  // Phase 3: Move across abyssal plain, spread, and thin out
                  const abyssalStartX = 60; // %
                  const abyssalEndX = 95; // %
                  const abyssalSpreadWidth = currentWidth * 1.5; // Spread wider
                  const abyssalThinHeight = currentHeight * 0.3; // Get much thinner


                  turbidityCurrentDiv.animate([
                       { left: `${abyssalStartX}%`, width: `${currentWidth}px`, height: `${currentHeight}px`, opacity: 1 },
                       { left: `${abyssalEndX}%`, width: `${abyssalSpreadWidth}px`, height: `${abyssalThinHeight}px`, opacity: 0.1 }
                  ], {
                      duration: abyssalDuration,
                      easing: 'ease-out', // Slow down significantly
                      iterations: 1,
                      fill: 'forwards'
                  }).onfinish = () => {
                      simOutputDiv.innerHTML = "<p>הסימולציה הסתיימה. נוצרו שכבות טורבידיטים.</p>";

                      // Hide the main current visual after it thins out
                      turbidityCurrentDiv.style.display = 'none';

                      // Re-enable controls after a short delay to appreciate the final state
                      setTimeout(() => {
                          runButton.disabled = false;
                          sedimentRange.disabled = false;
                          slopeRange.disabled = false;
                          triggerSelect.disabled = false;
                          canyonCheckbox.disabled = false;
                      }, 500); // Allow visuals to settle
                  };
              };

              // --- Accompanying Effects (Erosion/Deposition) ---

              // Erosion Effect: Fade in and expand on the slope area during the slope phase
              erosionEffectDiv.style.display = 'block';
              erosionEffectDiv.style.opacity = 0; // Start hidden
              erosionEffectDiv.style.width = '0%'; // Start narrow
              erosionEffectDiv.animate([
                  { opacity: 0, width: '0%' },
                  { opacity: 1, width: `${erosionFactor * 100}%` } // Fade in and expand based on factor
              ], {
                  duration: slopeDuration * 0.8, // Match most of slope phase duration
                  easing: 'ease-in-out',
                  delay: slopeDuration * 0.1, // Start slightly after current begins
                  iterations: 1,
                  fill: 'forwards'
              });


              // Deposition Effect: Appear and grow on the abyssal plain during/after abyssal phase
              depositionEffectDiv.style.display = 'block';
              depositionEffectDiv.style.height = '0'; // Start height animation
               depositionEffectDiv.style.opacity = 0.9; // Keep it visible but slightly transparent
               depositionEffectDiv.innerHTML = "שקיעה<br>(טורבידיטים)"; // Initial text

              depositionEffectDiv.animate([
                  { height: '0px' },
                  { height: `${depositionHeightFactor * (turbidityCurrentDiv.parentElement.offsetHeight - parseInt(getComputedStyle(turbidityCurrentDiv.parentElement).paddingBottom) - parseInt(getComputedStyle(turbidityCurrentDiv.parentElement).borderBottomWidth) - parseInt(getComputedStyle(document.querySelector('.abyssal-plain')).paddingTop))}px` } // Final thickness relative to abyssal height space
              ], {
                  duration: abyssalDuration * 0.8, // Match most of abyssal phase duration
                  easing: 'ease-out',
                  delay: slopeDuration + abyssalDuration * 0.2, // Start after current enters abyssal plain and slows
                  iterations: 1,
                  fill: 'forwards'
              });
         };
    }

    function resetSimulationVisuals(disableReset = true) {
        // Cancel any ongoing animations on the animated elements
        turbidityCurrentDiv.getAnimations().forEach(anim => anim.cancel());
        erosionEffectDiv.getAnimations().forEach(anim => anim.cancel());
        depositionEffectDiv.getAnimations().forEach(anim => anim.cancel());

        // Reset styles to initial hidden/small state
        turbidityCurrentDiv.style.display = 'none';
        turbidityCurrentDiv.style.width = '50px'; // Reset to initial small size for next run
        turbidityCurrentDiv.style.height = '30px';
        turbidityCurrentDiv.style.left = '25%';
        turbidityCurrentDiv.style.bottom = '0';
        turbidityCurrentDiv.style.opacity = 1; // Reset opacity
        turbidityCurrentDiv.style.transform = 'translateX(0)'; // Reset transform
        turbidityCurrentDiv.style.backgroundPosition = '0 0'; // Reset texture
        turbidityCurrentDiv.style.animationPlayState = 'paused'; // Pause flow animation

        erosionEffectDiv.style.display = 'none';
        erosionEffectDiv.style.width = '0%';
        erosionEffectDiv.style.opacity = 0;

        depositionEffectDiv.style.display = 'none';
        depositionEffectDiv.style.height = '0';
        depositionEffectDiv.innerHTML = ""; // Clear text

        // Update output message
        simOutputDiv.innerHTML = "<p>הגדר את הפרמטרים ולחץ \"הפעל זרם\".</p>";


        // Re-enable controls
        runButton.disabled = false;
        resetButton.disabled = disableReset;
        sedimentRange.disabled = false;
        slopeRange.disabled = false;
        triggerSelect.disabled = false;
        canyonCheckbox.disabled = false;

        // Ensure canyon visual is correct on reset based on current checkbox state
        canyonFeatureDiv.style.display = canyonCheckbox.checked ? 'block' : 'none';
    }

    runButton.addEventListener('click', runSimulation);
    resetButton.addEventListener('click', () => resetSimulationVisuals(true)); // Pass true to disable reset button after manual reset

    // Initial state setup
     resetSimulationVisuals(true); // Set initial state correctly (reset button disabled, visuals hidden)
     // Trigger initial updates for input spans and canyon visual display
     sedimentRange.dispatchEvent(new Event('input'));
     slopeRange.dispatchEvent(new Event('input'));
     canyonCheckbox.dispatchEvent(new Event('change'));

</script>
```