---
title: "חיים ללא שמש: חשיפת סודות המערכות האקולוגיות הכימוסינתטיות"
english_slug: life-without-sun-exploring-chemosynthetic-ecosystems
category: "מדעי הסביבה / אקולוגיה וקיימות"
tags: ["כימוסינתזה", "מעמקי ים", "פתחי הידרותרמיים", "מערכות אקולוגיות", "ביולוגיה קיצונית", "סימולציה"]
---
<h1>חיים ללא שמש: חשיפת סודות המערכות האקולוגיות הכימוסינתטיות</h1>
<p>דמיינו עולם ללא אור שמש, עמוק במעמקי האוקיינוס הקפואים והחשוכים. ובכל זאת, שם, בטמפרטורות רותחות ובלחץ מוחץ, משגשגים חיים! כיצד זה אפשרי? הצטרפו אלינו למסע אל פלא הכימוסינתזה – הבסיס למערכות אקולוגיות שלמות בסביבות הכי קיצוניות על פני כדור הארץ.</p>

<div id="ecosystem-app">
    <h2>סימולציית מערכת אקולוגית כימוסינתטית</h2>
    <div class="ecosystem-container">
         <div class="deep-sea-background"></div>
        <div class="vent">
            <p>פתח הידרותרמי</p>
            <div class="chemical-output-viz"></div>
        </div>
         <div class="trophic-flow-viz">
             <div class="flow-line bacteria-flow"></div>
             <div class="flow-line primary-flow"></div>
             <div class="flow-line secondary-flow"></div>
         </div>
        <div class="layer bacteria-layer">
            <h3>חיידקים כימוסינתטיים <br>(היצרנים הקדמונים)</h3>
            <div class="population-bar-container">
                 <div class="population-bar" id="bacteria-pop"></div>
                 <div class="population-indicator" id="bacteria-indicator"></div>
            </div>
            <p>אוכלוסייה: <span id="bacteria-count">0</span></p>
        </div>
        <div class="layer primary-consumer-layer">
            <h3>צרכנים ראשוניים <br>(למשל, תולעי צינור, צדפות)</h3>
             <div class="population-bar-container">
                <div class="population-bar" id="primary-pop"></div>
                 <div class="population-indicator" id="primary-indicator"></div>
             </div>
            <p>אוכלוסייה: <span id="primary-count">0</span></p>
        </div>
        <div class="layer secondary-consumer-layer">
            <h3>צרכנים משניים <br>(למשל, סרטנים, דגים עמוקים)</h3>
             <div class="population-bar-container">
                 <div class="population-bar" id="secondary-pop"></div>
                  <div class="population-indicator" id="secondary-indicator"></div>
             </div>
            <p>אוכלוסייה: <span id="secondary-count">0</span></p>
        </div>
         <div class="overlay-message" id="overlay-message"></div>
    </div>

    <div class="controls">
        <h4>שליטה על פרמטר המפתח: זרימת אנרגיה</h4>
        <label for="vent-output">עוצמת פליטת כימיקלים מהפתח:</label>
        <input type="range" id="vent-output" min="0" max="100" value="50">
        <span id="vent-value">50</span>%
        <p class="control-hint">שנו את עוצמת זרימת הכימיקלים כדי לראות איך המערכת האקולוגית מגיבה!</p>
    </div>
    <div class="energy-flow">
        <h4>זרימת אנרגיה במערכת</h4>
        <p>אנרגיה כימית מהפתח <span class="flow-arrow pulsating">&rarr;</span> חיידקים (יצרנים) <span class="flow-arrow pulsating">&rarr;</span> צרכנים ראשוניים <span class="flow-arrow pulsating">&rarr;</span> צרכנים משניים</p>
    </div>
</div>

<button id="toggle-explanation">הצג/הסתר מסע לגילוי עולמות חבויים</button>

<div id="explanation" style="display: none;">
    <h2>מסע לגילוי עולמות חבויים: מעמקי הכימוסינתזה</h2>

    <section>
        <h3>התמרה מופלאה: כימוסינתזה מול פוטוסינתזה</h3>
        <p>בעוד שרוב החיים על פני כדור הארץ תלויים באנרגיית השמש באמצעות <a href="#" class="glossary-link" data-term="פוטוסינתזה">פוטוסינתזה</a>, במעמקים האפלים מתחולל קסם אחר. <a href="#" class="glossary-link" data-term="כימוסינתזה">כימוסינתזה</a> היא התהליך שבו אורגניזמים זעירים, בעיקר חיידקים, לוכדים אנרגיה המשתחררת מריאקציות כימיות (כמו חמצון מימן גופריתי) והופכים אותה לאנרגיה זמינה לבניית תאים. זהו מקור האנרגיה האולטימטיבי לעולמות שאין בהם שמץ של אור.</p>
         <p class="explanation-tip"><strong>טיפ לסימולציה:</strong> זרימת הכימיקלים מהפתח מייצגת את "השמש" של המערכת הזו!</p>
    </section>

    <section>
        <h3>נאות מדבר בלב האפלה: היכן מוצאים אותן?</h3>
        <p>מערכות אקולוגיות אלו אינן שכיחות, אך במקומות בהם תנאי הכימוסינתזה מתקיימים, הן פורחות במגוון חיים מדהים. המפורסמים ביותר הם <a href="#" class="glossary-link" data-term="פתחי הידרותרמיים">פתחי הידרותרמיים</a> – סדקים בקרקעית הים שמהם פורצים מים חמים ועשירים במינרלים געשיים. אך הן קיימות גם בספילות קרות (cold seeps) שם מחלחלים גזים, באגמים תת-קרקעיים חשוכים, ואפילו בסלעים עמוק מתחת לפני הקרקע.</p>
    </section>

    <section>
        <h3>מבנה חיים בשכבות: שרשרת המזון הכימוסינתטית</h3>
        <p>כמו בכל מערכת אקולוגית, גם כאן יש רמות חיים התלויות זו בזו:</p>
        <ul>
            <li><strong>יצרנים (<a href="#" class="glossary-link" data-term="יצרנים">Producers</a>):</strong> גבורי הכימוסינתזה! בדרך כלל חיידקים, החיים חופשי במים ועל משטחים, או בסימביוזה מדהימה בתוך בעלי חיים גדולים יותר. הם הופכים כימיקלים לאנרגיה זמינה לחיים.</li>
            <li><strong>צרכנים ראשוניים (<a href="#" class="glossary-link" data-term="צרכנים ראשוניים">Primary Consumers</a>):</strong> האורגניזמים הראשונים שניזונים ישירות מהיצרנים. הדוגמה המפורסמת ביותר הן תולעי הצינור הענקיות (Riftia pachyptila), שאין להן פה או מערכת עיכול אלא רקמות מלאות בחיידקים כימוסינתטיים המספקים להן מזון ישירות. גם צדפות ושבלולים רבים ניזונים מהחיידקים.</li>
            <li><strong>צרכנים משניים (<a href="#" class="glossary-link" data-term="צרכנים משניים">Secondary Consumers</a>):</strong> טורפי העומק האלו ניזונים מהצרכנים הראשוניים. סרטנים, שרימפס, תמנונים, ודגים שונים משייטים בקרבת הפתחים וניזונים מהמגוון העשיר של הצרכנים הראשוניים.</li>
            <li><strong>מפרקים (<a href="#" class="glossary-link" data-term="מפרקים">Decomposers</a>):</strong> גם כאן, אורגניזמים מיוחדים מפרקים חומר אורגני מת ומחזירים חומרים למערכת.</li>
        </ul>
         <p class="explanation-tip"><strong>טיפ לסימולציה:</strong> הסליידר שאתם מזיזים שולט למעשה בזמינות ה"מזון" עבור שכבת היצרנים (החיידקים), וכל שאר השכבות תלויות בהם!</p>
    </section>

    <section>
        <h3>זרימת חיים ומוות: אנרגיה במעמקים</h3>
        <p>האנרגיה מתחילה כאנרגיה כימית בתרכובות הנפלטות מהפתח. החיידקים קולטים אותה, מקבעים פחמן דו חמצני והופכים אותו לביומסה. ביומסה זו נאכלת על ידי הצרכנים הראשוניים, ומשם עוברת לצרכנים המשניים. זוהי שרשרת מזון ייחודית, המנותקת לחלוטין מהאנרגיה שמקורה בשמש!</p>
    </section>

    <section>
        <h3>לשרוד את הבלתי אפשרי: התאמות מדהימות</h3>
        <p>החיים ליד פתחים הידרותרמיים דורשים הסתגלות יוצאת דופן: טמפרטורות קיצוניות, לחץ אדיר, ריכוזים גבוהים של כימיקלים רעילים כמו מימן גופריתי, וחושך מוחלט. האורגניזמים כאן הם <a href="#" class="glossary-link" data-term="אקסטרמופילים">אקסטרמופילים</a> אמיתיים, עם אנזימים עמידים לחום, מנגנוני ניטרול רעלים, וקשרים סימביוטיים מדהימים עם החיידקים המאפשרים להם לשגשג היכן ששום חיים אחרים לא היו שורדים.</p>
    </section>

    <section>
        <h3>מעבר למעמקים: למה זה חשוב לנו?</h3>
        <p>חקר העולם המרתק הזה מספק תובנות מעמיקות:</p>
        <ul>
            <li><strong>חיים אחרים?</strong>: סביבות אלו דומות לתנאים ששררו על כדור הארץ הקדום. חקרן יכול לשפוך אור על מוצא החיים עצמו – ייתכן שהחיים החלו בפתחים כאלה! הן גם מודל פוטנציאלי לחיים על כוכבים אחרים (כמו הירח אירופה של צדק).</li>
            <li><strong>רפואה וטכנולוגיה</strong>: חלבונים ואנזימים מהאורגניזמים האקסטרמופילים יכולים להיות בעלי יישומים פורצי דרך ברפואה, ביוטכנולוגיה ותעשייה.</li>
            <li><strong>אוצרות נסתרים</strong>: הפתחים עשירים במתכות ומינרלים, מה שמעלה שאלות מורכבות על כריית מעמקי ים עתידית והשפעותיה הסביבתיות.</li>
        </ul>
    </section>
</div>

<div id="glossary-popup" class="glossary-popup" style="display: none;">
    <div class="glossary-content">
        <h4 id="glossary-title"></h4>
        <p id="glossary-definition"></p>
        <button class="close-popup">סגור</button>
    </div>
</div>


<style>
    /* General Enhancements */
    body {
        font-family: 'Arial', sans-serif; /* A slightly more modern sans-serif */
        line-height: 1.7; /* Improved readability */
        margin: 0;
        padding: 20px;
        background-color: #0a0a1a; /* Very dark blue for deep sea feel */
        color: #c0c0e0; /* Soft grey-blue text */
        direction: rtl;
        text-align: right;
        overflow-x: hidden; /* Prevent horizontal scroll */
        position: relative; /* Needed for background effects */
    }

     body::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: radial-gradient(circle at 50% 150%, rgba(10, 10, 26, 0.8) 0%, rgba(10, 10, 26, 1) 60%),
                          url('https://www.transparenttextures.com/patterns/star-konfetti.png'); /* Subtle texture */
        background-size: cover;
        opacity: 0.5;
        z-index: -1;
     }


    h1, h2, h3, h4 {
        color: #4fc3f7; /* Bright blue accent */
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 0 0 5px rgba(79, 195, 247, 0.5); /* Subtle glow */
    }

    h1 { font-size: 2.5em; margin-bottom: 30px; }
    h2 { font-size: 2em; }
    h3 { font-size: 1.5em; margin-top: 20px; }
    h4 { font-size: 1.2em; margin-bottom: 15px; }

    p {
        margin-bottom: 15px;
    }

    a {
        color: #80cbc4; /* Teal accent for links */
        text-decoration: none;
        border-bottom: 1px dotted #80cbc4;
        transition: color 0.3s ease, border-bottom-color 0.3s ease;
    }

    a:hover {
        color: #e0f7fa; /* Lighter teal on hover */
        border-bottom-color: #e0f7fa;
    }

    /* Ecosystem App Styles */
    #ecosystem-app {
        background-color: rgba(18, 18, 36, 0.8); /* Semi-transparent dark blue */
        padding: 30px;
        border-radius: 15px;
        margin: 30px auto; /* Center block */
        max-width: 800px; /* Max width for better readability */
        border: 2px solid #4fc3f7; /* Accent border */
        box-shadow: 0 0 20px rgba(79, 195, 247, 0.3); /* Glow effect */
        position: relative;
        overflow: hidden; /* Hide overflow from animations */
    }

     .deep-sea-background {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(to bottom, rgba(26, 0, 42, 0.8) 0%, rgba(5, 5, 50, 0.9) 50%, rgba(0, 0, 10, 0.95) 100%); /* Deep sea gradient */
        opacity: 0.6;
        z-index: -1;
     }


    .ecosystem-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 30px;
        position: relative;
        min-height: 500px; /* Increased height for better separation */
        padding-bottom: 80px; /* Space for the vent at the bottom */
    }

    .vent {
        background: radial-gradient(circle, rgba(255, 152, 0, 0.8) 0%, rgba(255, 87, 34, 0.9) 50%, rgba(255, 0, 0, 0.8) 100%); /* Fiery gradient */
        width: 120px; /* Slightly larger */
        height: 70px;
        border-radius: 15px 15px 0 0;
        position: absolute;
        bottom: 0; /* Align to bottom */
        left: 50%;
        transform: translateX(-50%);
        text-align: center;
        color: white;
        font-size: 0.9em;
        padding-top: 8px;
        box-shadow: 0 0 20px 8px rgba(255, 87, 34, 0.7); /* More intense glow */
        z-index: 2; /* Bring to front */
        font-weight: bold;
    }

    .chemical-output-viz {
        position: absolute;
        top: -50px; /* Start above the vent */
        left: 10%;
        right: 10%;
        height: 50px;
        background: linear-gradient(to top, rgba(255, 152, 0, 0.5), rgba(255, 87, 34, 0.3), transparent); /* Stream effect */
        opacity: 0; /* Controlled by JS based on vent output */
        transition: opacity 0.5s ease-out;
    }

     .chemical-output-viz::before, .chemical-output-viz::after {
        content: '';
        position: absolute;
        bottom: 0;
        width: 6px; /* Width of individual streams */
        height: 100%;
        background-color: rgba(255, 202, 40, 0.7); /* Yellowish glow for streams */
        animation: chemicalStream 2s infinite linear;
     }
      .chemical-output-viz::before { left: 20%; animation-delay: 0s; }
      .chemical-output-viz::after { right: 20%; animation-delay: 1s; }

      @keyframes chemicalStream {
          0% { transform: translateY(0) scaleY(1); opacity: 1; }
          100% { transform: translateY(-60px) scaleY(0.5); opacity: 0; } /* Streams rise and fade */
      }


    .layer {
        width: 90%; /* Wider layers */
        margin-bottom: 20px; /* More space between layers */
        padding: 15px;
        border-radius: 12px;
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        box-sizing: border-box;
        min-height: 100px; /* Ensure layer height */
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3); /* Add shadow for depth */
        backdrop-filter: blur(3px); /* Subtle blur effect */
        z-index: 1; /* Stack layers */
    }

    .bacteria-layer {
        background-color: rgba(76, 175, 80, 0.2); /* Semi-transparent green */
        border: 1px solid rgba(76, 175, 80, 0.6);
        bottom: 100px; /* Position above vent */
    }

    .primary-consumer-layer {
        background-color: rgba(3, 169, 244, 0.2); /* Semi-transparent blue */
        border: 1px solid rgba(3, 169, 244, 0.6);
        bottom: 220px; /* Position above bacteria */
    }

    .secondary-consumer-layer {
        background-color: rgba(156, 39, 176, 0.2); /* Semi-transparent purple */
        border: 1px solid rgba(156, 39, 176, 0.6);
        bottom: 340px; /* Position above primary */
    }

    .layer h3 {
        margin-top: 0;
        margin-bottom: 10px;
        font-size: 1.1em;
        color: #e0e0e0; /* Light text */
        text-shadow: none; /* Remove glow from layer titles */
    }

    .population-bar-container {
        background-color: rgba(255, 255, 255, 0.15); /* Slightly more visible container */
        border-radius: 5px;
        overflow: hidden;
        height: 20px; /* Taller bars */
        margin-bottom: 8px;
        width: 90%; /* Wider bar container */
        position: relative;
    }

    .population-bar {
        height: 100%;
        background-color: #81c784; /* Softer green */
        width: 0%; /* Initial width */
        transition: width 0.5s ease-out; /* Smooth transition for bar growth */
        position: relative;
    }

     .population-indicator {
        position: absolute;
        top: 0;
        left: 0;
        height: 100%;
        width: 100%;
        background-color: transparent;
        transition: background-color 0.3s ease; /* For status feedback */
        pointer-events: none; /* Allow clicks to pass through */
     }
     .population-indicator.ok { background-color: rgba(0, 255, 0, 0.1); }
     .population-indicator.stressed { background-color: rgba(255, 165, 0, 0.2); animation: pulse-orange 1s infinite alternate; }
     .population-indicator.critical { background-color: rgba(255, 0, 0, 0.2); animation: pulse-red 0.8s infinite alternate; }

     @keyframes pulse-orange {
         0% { background-color: rgba(255, 165, 0, 0.2); }
         100% { background-color: rgba(255, 165, 0, 0.4); }
     }
      @keyframes pulse-red {
         0% { background-color: rgba(255, 0, 0, 0.2); }
         100% { background-color: rgba(255, 0, 0, 0.5); }
     }


    .primary-consumer-layer .population-bar {
         background-color: #64b5f6; /* Softer blue */
    }
     .secondary-consumer-layer .population-bar {
         background-color: #ba68c8; /* Softer purple */
    }


    .layer p {
        margin: 0;
        font-size: 1em; /* Slightly larger font */
        color: #e0e0e0;
        text-align: center; /* Center count */
    }

     .trophic-flow-viz {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        z-index: 0; /* Behind layers */
     }

    .flow-line {
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        width: 2px; /* Thin lines */
        background: linear-gradient(to bottom, transparent 0%, rgba(255, 255, 255, 0.5) 50%, transparent 100%);
        opacity: 0.7;
        animation: flow 1.5s infinite linear;
     }

     .bacteria-flow { bottom: 80px; height: 60px; background-color: rgba(76, 175, 80, 0.5); }
     .primary-flow { bottom: 200px; height: 60px; background-color: rgba(3, 169, 244, 0.5); animation-delay: 0.5s; }
     .secondary-flow { bottom: 320px; height: 60px; background-color: rgba(156, 39, 176, 0.5); animation-delay: 1s; }

     @keyframes flow {
         0% { transform: translateX(-50%) translateY(0); opacity: 0.7; }
         100% { transform: translateX(-50%) translateY(20px); opacity: 0.3; } /* Simulate particles flowing down */
     }


    .controls {
        background-color: rgba(28, 18, 46, 0.8); /* Darker transparent purple */
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
        border: 1px solid #80cbc4; /* Teal border */
        box-shadow: 0 0 15px rgba(128, 203, 196, 0.3);
    }

    .controls label {
        display: block; /* Label on its own line */
        margin-bottom: 12px;
        font-weight: bold;
        color: #e0e0e0;
        font-size: 1.1em;
    }

    .controls input[type="range"] {
        width: calc(100% - 60px); /* Adjust width for span */
        margin-right: 10px;
        vertical-align: middle;
        direction: ltr;
        -webkit-appearance: none;
        appearance: none;
        height: 8px;
        background: #555;
        outline: none;
        opacity: 0.7;
        transition: opacity .2s;
        border-radius: 4px;
     }

    .controls input[type="range"]:hover {
        opacity: 1;
    }

    .controls input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #4fc3f7; /* Blue thumb */
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #e0e0e0;
     }

     .controls input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #4fc3f7;
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #e0e0e0;
     }

    .controls span {
        display: inline-block;
        min-width: 40px; /* Ensure space for value */
        text-align: left;
        font-weight: bold;
        color: #4fc3f7;
    }

     .control-hint {
        font-size: 0.9em;
        color: #a0a0c0;
        text-align: center;
        margin-top: 15px;
     }


    .energy-flow {
        background-color: rgba(28, 18, 46, 0.8);
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
        border: 1px solid #80cbc4;
        box-shadow: 0 0 15px rgba(128, 203, 196, 0.3);
        text-align: center;
    }

    .energy-flow h4 {
        margin-top: 0;
        color: #e0e0e0; /* White text */
        text-shadow: none;
    }

    .flow-arrow {
        color: #81c784; /* Green arrow */
        font-weight: bold;
        margin: 0 5px;
     }
     .flow-arrow.pulsating {
        animation: pulse-arrow 1.5s infinite;
     }

     @keyframes pulse-arrow {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
     }


    button {
        display: block;
        width: auto;
        margin: 20px auto;
        padding: 12px 25px; /* Larger button */
        font-size: 1.1em;
        color: white;
        background-color: #e94560; /* Reddish button */
        border: none;
        border-radius: 6px;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 15px rgba(233, 69, 96, 0.4);
        font-weight: bold;
    }

    button:hover {
        background-color: #ff718c; /* Lighter red on hover */
        transform: translateY(-2px); /* Slight lift effect */
        box-shadow: 0 6px 20px rgba(233, 69, 96, 0.6);
    }
     button:active {
        transform: translateY(0);
        box-shadow: 0 2px 10px rgba(233, 69, 96, 0.4);
     }


    #explanation {
        background-color: rgba(18, 18, 36, 0.8);
        padding: 30px;
        border-radius: 15px;
        border: 2px solid #4fc3f7;
        box-shadow: 0 0 20px rgba(79, 195, 247, 0.3);
        margin-top: 30px;
    }

    #explanation section {
        margin-bottom: 30px;
        padding-bottom: 20px;
        border-bottom: 1px dashed #80cbc4; /* Teal dashed border */
    }

    #explanation section:last-child {
        border-bottom: none;
        margin-bottom: 0;
        padding-bottom: 0;
    }

    #explanation h3 {
         text-align: right;
         color: #b39ddb; /* Light purple for sub-headings */
         margin-bottom: 15px;
         padding-bottom: 8px;
         border-bottom: 1px dotted rgba(179, 157, 219, 0.5);
         font-size: 1.3em;
         text-shadow: none;
    }

    #explanation p.explanation-tip {
        background-color: rgba(128, 203, 196, 0.1);
        border-left: 4px solid #80cbc4;
        padding: 10px 15px;
        margin-top: 15px;
        border-radius: 4px;
        font-style: italic;
        color: #a0a0c0;
    }


    #explanation ul {
        list-style: disc inside;
        padding-right: 20px;
         color: #c0c0e0;
    }

    #explanation li {
        margin-bottom: 10px;
    }

     #explanation strong {
         color: #e94560; /* Reddish accent for strong words */
     }

    /* Glossary Popup */
    .glossary-popup {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.7);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000;
        opacity: 0;
        visibility: hidden;
        transition: opacity 0.3s ease, visibility 0.3s ease;
    }

    .glossary-popup.visible {
         opacity: 1;
         visibility: visible;
    }


    .glossary-content {
        background-color: #1a1a2e;
        padding: 25px;
        border-radius: 10px;
        border: 2px solid #80cbc4;
        max-width: 400px;
        text-align: right;
        box-shadow: 0 0 20px rgba(128, 203, 196, 0.5);
    }

    .glossary-content h4 {
        color: #4fc3f7;
        margin-top: 0;
        text-align: center;
        margin-bottom: 15px;
         text-shadow: none;
    }

    .glossary-content p {
        color: #c0c0e0;
        margin-bottom: 20px;
    }

    .glossary-content button {
        display: block;
        margin: 0 auto;
        background-color: #e94560;
        color: white;
        border: none;
        padding: 8px 15px;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease;
         box-shadow: none;
         font-weight: normal;
    }
     .glossary-content button:hover {
        background-color: #ff718c;
         transform: none;
         box-shadow: none;
     }


     /* Overlay Message */
     .overlay-message {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: rgba(0, 0, 0, 0.8);
        color: white;
        padding: 15px 25px;
        border-radius: 8px;
        font-size: 1.2em;
        font-weight: bold;
        text-align: center;
        z-index: 10;
        opacity: 0;
        visibility: hidden;
        transition: opacity 0.5s ease, visibility 0.5s ease;
     }
     .overlay-message.visible {
         opacity: 1;
         visibility: visible;
     }


    /* Responsive adjustments */
    @media (max-width: 600px) {
        body {
            padding: 10px;
        }
        h1 { font-size: 2em; }
        h2 { font-size: 1.6em; }
        h3 { font-size: 1.2em; }
        .ecosystem-app {
            padding: 15px;
        }
         .layer {
             width: 95%;
             padding: 10px;
             bottom: 80px; /* Adjust positions for smaller screens */
         }
         .bacteria-layer { bottom: 80px; }
         .primary-consumer-layer { bottom: 190px; }
         .secondary-consumer-layer { bottom: 300px; }

         .vent {
             width: 90px;
             height: 50px;
         }
         .controls input[type="range"] {
             width: calc(100% - 50px);
         }
         .glossary-content {
             max-width: 90%;
         }
    }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const ventOutputSlider = document.getElementById('vent-output');
        const ventValueSpan = document.getElementById('vent-value');
        const bacteriaCountSpan = document.getElementById('bacteria-count');
        const primaryCountSpan = document.getElementById('primary-count');
        const secondaryCountSpan = document.getElementById('secondary-count');
        const bacteriaBar = document.getElementById('bacteria-pop');
        const primaryBar = document.getElementById('primary-pop');
        const secondaryBar = document.getElementById('secondary-pop');
        const bacteriaIndicator = document.getElementById('bacteria-indicator');
        const primaryIndicator = document.getElementById('primary-indicator');
        const secondaryIndicator = document.getElementById('secondary-indicator');
        const toggleButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');
        const chemicalOutputViz = document.getElementById('chemical-output-viz');
        const overlayMessage = document.getElementById('overlay-message');

        // Glossary elements
        const glossaryLinks = document.querySelectorAll('.glossary-link');
        const glossaryPopup = document.getElementById('glossary-popup');
        const glossaryTitle = document.getElementById('glossary-title');
        const glossaryDefinition = document.getElementById('glossary-definition');
        const closePopup = document.querySelector('.glossary-popup .close-popup');

        // Simulation Parameters
        let bacteriaPop = 0;
        let primaryPop = 0;
        let secondaryPop = 0;

        // Carrying capacities (approximate maximums for scaling)
        const maxBacteriaCapacity = 50000; // Higher max capacity for more range
        const maxPrimaryCapacity = 15000;
        const maxSecondaryCapacity = 3000;

        // Growth rates (simplified)
        const bacteriaGrowthRate = 0.002; // Growth per step based on vent output
        const primaryGrowthRate = 0.0015; // Growth per step based on bacteria
        const secondaryGrowthRate = 0.001; // Growth per step based on primary

        // Decay/Death rates (simplified, representing natural loss and consumption)
        const bacteriaDecay = 0.0001; // Natural death + eaten by primaries
        const primaryDecay = 0.0002; // Natural death + eaten by secondaries
        const secondaryDecay = 0.0003; // Natural death

        // Simulation interval
        const simulationInterval = 150; // ms between simulation steps

        // --- Simulation Loop ---
        function runSimulationStep() {
            const ventValue = parseInt(ventOutputSlider.value, 10);
            const chemicalInput = ventValue / 100; // Normalize to 0-1

            // Update Bacteria Population
            // Growth is proportional to chemical input
            // Decay is proportional to current population and consumption by primaries
            let bacteriaChange = (chemicalInput * bacteriaGrowthRate * maxBacteriaCapacity) - (bacteriaPop * bacteriaDecay) - (primaryPop * primaryGrowthRate * 0.5); // 0.5 is consumption factor
            bacteriaPop += bacteriaChange;
            bacteriaPop = Math.max(0, Math.min(bacteriaPop, maxBacteriaCapacity)); // Clamp between 0 and max capacity

            // Update Primary Consumer Population
            // Growth is proportional to available bacteria (relative to capacity)
            // Decay is proportional to current population and consumption by secondaries
            let primaryChange = (bacteriaPop / maxBacteriaCapacity * primaryGrowthRate * maxPrimaryCapacity) - (primaryPop * primaryDecay) - (secondaryPop * secondaryGrowthRate * 0.5); // 0.5 is consumption factor
            primaryPop += primaryChange;
            primaryPop = Math.max(0, Math.min(primaryPop, maxPrimaryCapacity)); // Clamp

            // Update Secondary Consumer Population
            // Growth is proportional to available primaries (relative to capacity)
            // Decay is proportional to current population
            let secondaryChange = (primaryPop / maxPrimaryCapacity * secondaryGrowthRate * maxSecondaryCapacity) - (secondaryPop * secondaryDecay);
            secondaryPop += secondaryChange;
            secondaryPop = Math.max(0, Math.min(secondaryPop, maxSecondaryCapacity)); // Clamp

            updateDisplay();
            checkEcosystemStatus();
        }

        // --- Display Update ---
        function updateDisplay() {
            const ventValue = parseInt(ventOutputSlider.value, 10);
            ventValueSpan.textContent = ventValue;

            // Update count text - round for cleaner display
            bacteriaCountSpan.textContent = Math.round(bacteriaPop);
            primaryCountSpan.textContent = Math.round(primaryPop);
            secondaryCountSpan.textContent = Math.round(secondaryPop);

            // Update population bar widths (relative to their OWN max capacity)
            bacteriaBar.style.width = (bacteriaPop / maxBacteriaCapacity) * 100 + '%';
            primaryBar.style.width = (primaryPop / maxPrimaryCapacity) * 100 + '%';
            secondaryBar.style.width = (secondaryPop / maxSecondaryCapacity) * 100 + '%';

            // Update chemical output visualization opacity
            chemicalOutputViz.style.opacity = ventValue / 100;

            // Update flow line heights/visibility based on populations (simplified)
            // Maybe adjust height/opacity based on population size? Or just keep them steady pulses?
             const bacteriaFlowHeight = 60 + (bacteriaPop / maxBacteriaCapacity * 40); // Flow gets stronger with more bacteria
             document.querySelector('.bacteria-flow').style.height = `${bacteriaFlowHeight}px`;

             const primaryFlowHeight = 60 + (primaryPop / maxPrimaryCapacity * 40);
             document.querySelector('.primary-flow').style.height = `${primaryFlowHeight}px`;

             const secondaryFlowHeight = 60 + (secondaryPop / maxSecondaryCapacity * 40);
             document.querySelector('.secondary-flow').style.height = `${secondaryFlowHeight}px`;


        }

        // --- Ecosystem Status Feedback ---
        function checkEcosystemStatus() {
             const thresholdCritical = 0.1; // Below 10% of max capacity
             const thresholdStressed = 0.3; // Below 30% of max capacity

             // Bacteria status
             bacteriaIndicator.className = 'population-indicator'; // Reset
             if (bacteriaPop / maxBacteriaCapacity < thresholdCritical && parseInt(ventOutputSlider.value, 10) > 0) {
                 bacteriaIndicator.classList.add('critical');
             } else if (bacteriaPop / maxBacteriaCapacity < thresholdStressed && parseInt(ventOutputSlider.value, 10) > 0) {
                 bacteriaIndicator.classList.add('stressed');
             } else if (bacteriaPop > 0) {
                  bacteriaIndicator.classList.add('ok');
             }


             // Primary status
             primaryIndicator.className = 'population-indicator'; // Reset
             if (primaryPop / maxPrimaryCapacity < thresholdCritical && bacteriaPop > 0) {
                  primaryIndicator.classList.add('critical');
             } else if (primaryPop / maxPrimaryCapacity < thresholdStressed && bacteriaPop > 0) {
                  primaryIndicator.classList.add('stressed');
             } else if (primaryPop > 0) {
                 primaryIndicator.classList.add('ok');
             }


             // Secondary status
             secondaryIndicator.className = 'population-indicator'; // Reset
             if (secondaryPop / maxSecondaryCapacity < thresholdCritical && primaryPop > 0) {
                  secondaryIndicator.classList.add('critical');
             } else if (secondaryPop / maxSecondaryCapacity < thresholdStressed && primaryPop > 0) {
                  secondaryIndicator.classList.add('stressed');
             } else if (secondaryPop > 0) {
                  secondaryIndicator.classList.add('ok');
             }


             // General message
             if (parseInt(ventOutputSlider.value, 10) === 0 && (bacteriaPop < 100 || primaryPop < 10 || secondaryPop < 5)) { // Low vent AND low populations
                  showMessage("המערכת מתקשה לשרוד ללא אנרגיה מהפתח!");
             } else if (bacteriaPop / maxBacteriaCapacity < thresholdCritical * 2 && parseInt(ventOutputSlider.value, 10) > 0 && (primaryPop/maxPrimaryCapacity < thresholdStressed || secondaryPop/maxSecondaryCapacity < thresholdStressed) ) {
                  showMessage("היצרנים (חיידקים) בלחץ! הגברת זרימת הכימיקלים יכולה לעזור.");
             } else if (secondaryPop / maxSecondaryCapacity > 0.8 && primaryPop / maxPrimaryCapacity > 0.8) {
                   showMessage("המערכת משגשגת! כל רמות החיים נתמכות היטב.");
             } else if (secondaryPop < 50 && primaryPop > maxPrimaryCapacity * 0.5) {
                   showMessage("עודף צרכנים ראשוניים? ייתכן שחסרים טורפים (צרכנים משניים) או שאין מספיק אנרגיה לתמוך בשכבות הגבוהות.");
             }
             else {
                 hideMessage(); // Hide message if status is normal or conditions don't match specific messages
             }

        }

        let messageTimeout;
        function showMessage(message, duration = 3000) {
            overlayMessage.textContent = message;
            overlayMessage.classList.add('visible');
            if (messageTimeout) {
                 clearTimeout(messageTimeout);
            }
            messageTimeout = setTimeout(() => {
                hideMessage();
            }, duration);
        }

        function hideMessage() {
             overlayMessage.classList.remove('visible');
        }


        // --- Explanation Toggle ---
        function toggleExplanation() {
            if (explanationDiv.style.display === 'none' || explanationDiv.style.display === '') {
                explanationDiv.style.display = 'block';
                toggleButton.textContent = 'הסתר מסע לגילוי עולמות חבויים';
            } else {
                explanationDiv.style.display = 'none';
                toggleButton.textContent = 'הצג מסע לגילוי עולמות חבויים';
            }
        }

        // --- Glossary Functionality ---
        const glossaryTerms = {
             "פוטוסינתזה": "תהליך שבו אורגניזמים ממירים אנרגיית אור (בדרך כלל מהשמש), פחמן דו חמצני ומים לאנרגיה כימית בצורת סוכרים.",
             "כימוסינתזה": "תהליך שבו אורגניזמים (בעיקר חיידקים) ממירים אנרגיה המשתחררת מריאקציות כימיות (לרוב חמצון תרכובות אי-אורגניות) לאנרגיה כימית בצורת סוכרים.",
             "פתחי הידרותרמיים": "סדקים בקרקעית הים שמהם פורצים מים חמים ועשירים במינרלים כתוצאה מפעילות געשית תת-ימית.",
             "יצרנים": "אורגניזמים המייצרים את המזון האורגני שלהם בעצמם, בדרך כלל באמצעות פוטוסינתזה או כימוסינתזה. הם הבסיס לשרשרת המזון.",
             "צרכנים ראשוניים": "אורגניזמים הניזונים ישירות מהיצרנים (אוכלי צמחים/חיידקים).",
             "צרכנים משניים": "אורגניזמים הניזונים מצרכנים ראשוניים (טורפים).",
             "מפרקים": "אורגניזמים (חיידקים, פטריות) המפרקים חומר אורגני מת ומחזירים חומרים למערכת האקולוגית.",
             "אקסטרמופילים": "אורגניזמים החיים בסביבות קיצוניות (טמפרטורה, לחץ, מליחות, קרינה וכו') שתהיינה קטלניות לרוב האורגניזמים האחרים."
        };

        glossaryLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const term = link.dataset.term;
                if (glossaryTerms[term]) {
                    glossaryTitle.textContent = term;
                    glossaryDefinition.textContent = glossaryTerms[term];
                    glossaryPopup.classList.add('visible');
                }
            });
        });

        closePopup.addEventListener('click', () => {
            glossaryPopup.classList.remove('visible');
        });

        // Close popup when clicking outside content
        glossaryPopup.addEventListener('click', (e) => {
            if (e.target === glossaryPopup) {
                glossaryPopup.classList.remove('visible');
            }
        });


        // --- Event Listeners ---
        ventOutputSlider.addEventListener('input', () => {
            ventValueSpan.textContent = ventOutputSlider.value; // Instant update of value display
             // The simulation loop will handle the population updates
        });

        toggleButton.addEventListener('click', toggleExplanation);

        // Initial state and start simulation
        updateDisplay(); // Initial display based on default slider value
        setInterval(runSimulationStep, simulationInterval); // Start the simulation loop
    });
</script>
---