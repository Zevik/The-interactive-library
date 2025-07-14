---
title: "קרב האור והאנרגיה: נורות ליבון מול LED"
english_slug: incandescent-vs-led-light-efficiency-heat-spectrum
category: "פיזיקה"
tags:
  - חשמל
  - אנרגיה
  - אור
  - יעילות אנרגטית
  - פיזיקה
---
# קרב האור והאנרגיה: נורות ליבון מול LED
הייתם מאמינים שכמעט כל האנרגיה שנורת ליבון צורכת הופכת לחום במקום לאור? ואיך נורות ה-LED הקטנות שינו לגמרי את כללי המשחק? בואו נדליק את שתי הנורות ונראה בדיוק איפה האנרגיה הולכת!

<div class="container">
    <div class="bulb-container">
        <h2>נורת ליבון 💡🔥</h2>
        <div class="bulb-visual incandescent-bulb" id="incandescent-bulb">
            <div class="filament"></div>
            <div class="light-glow"></div>
            <div class="heat-waves"></div>
             <div class="energy-in"></div>
             <div class="energy-out light-particles"></div>
             <div class="energy-out heat-particles"></div>
        </div>
        <button class="toggle-button" id="toggle-incandescent">הדלק/י</button>
        <div class="indicators">
             <p>🔌 הספק רגעי: <span id="incandescent-power">0</span> ואט</p>
              <p>💡⚡ אנרגיה נצרכה (סה"כ): <span id="incandescent-total-energy">0</span> ג'אול</p>
            <div class="spectrum-indicator">
                🌈 ספקטרום האור: <div class="spectrum-bar" id="incandescent-spectrum"></div>
            </div>
            <div class="efficiency-indicator">
                📊 חלוקת האנרגיה:
                <div class="efficiency-chart">
                    <div class="efficiency-bar light-bar" id="incandescent-light-efficiency"></div>
                    <div class="efficiency-bar heat-bar" id="incandescent-heat-efficiency"></div>
                </div>
                <p>💡 <span id="incandescent-light-percent">0</span>% אור, 🔥 <span id="incandescent-heat-percent">0</span>% חום</p>
            </div>
        </div>
    </div>

    <div class="bulb-container">
        <h2>נורת LED 💡❄️</h2>
        <div class="bulb-visual led-bulb" id="led-bulb">
             <div class="led-elements"></div>
             <div class="light-glow"></div>
             <div class="heat-waves"></div>
             <div class="energy-in"></div>
             <div class="energy-out light-particles"></div>
             <div class="energy-out heat-particles"></div>
        </div>
        <button class="toggle-button" id="toggle-led">הדלק/י</button>
        <div class="indicators">
             <p>🔌 הספק רגעי: <span id="led-power">0</span> ואט</p>
              <p>💡⚡ אנרגיה נצרכה (סה"כ): <span id="led-total-energy">0</span> ג'אול</p>
             <div class="spectrum-indicator">
                 🌈 ספקטרום האור: <div class="spectrum-bar" id="led-spectrum"></div>
             </div>
             <div class="efficiency-indicator">
                 📊 חלוקת האנרגיה:
                 <div class="efficiency-chart">
                     <div class="efficiency-bar light-bar" id="led-light-efficiency"></div>
                     <div class="efficiency-bar heat-bar" id="led-heat-efficiency"></div>
                 </div>
                 <p>💡 <span id="led-light-percent">0</span>% אור, 🔥 <span id="led-heat-percent">0</span>% חום</p>
             </div>
         </div>
    </div>
</div>

<style>
    :root {
        --incandescent-light-color: #ffda85; /* warmer light */
        --led-light-color: #a1e0ff; /* cooler light */
        --heat-color: #ff6347; /* tomato red */
        --light-efficiency-color: #ffc107; /* amber */
        --heat-efficiency-color: #f44336; /* red */
        --bulb-off-color: #f0f0f0;
        --border-color: #e0e0e0;
        --text-color: #333;
        --background-color: #f8f8f8;
        --card-background: #ffffff;
        --button-on-color: #4CAF50; /* Green */
        --button-off-color: #f44336; /* Red */
    }

    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: var(--text-color);
        background-color: var(--background-color);
        line-height: 1.6;
        padding: 20px;
    }

    h1 {
        text-align: center;
        color: #0056b3;
        margin-bottom: 30px;
    }

    .container {
        display: flex;
        justify-content: center;
        margin-top: 30px;
        flex-wrap: wrap;
        gap: 40px; /* Added gap */
    }

    .bulb-container {
        text-align: center;
        margin: 0; /* Removed margin */
        padding: 30px; /* Increased padding */
        background-color: var(--card-background);
        border: 1px solid var(--border-color);
        border-radius: 12px; /* More rounded corners */
        width: 320px; /* Adjusted width */
        box-shadow: 0 4px 15px rgba(0,0,0,0.1); /* Stronger shadow */
        transition: transform 0.3s ease;
    }

    .bulb-container:hover {
        transform: translateY(-5px);
    }

    .bulb-container h2 {
        color: #007bff;
        margin-top: 0;
        margin-bottom: 25px;
        font-size: 1.4em;
    }

    .bulb-visual {
        width: 120px; /* Larger bulb */
        height: 180px; /* Larger bulb */
        margin: 20px auto 30px auto;
        position: relative;
        border-radius: 50% / 60% 60% 40% 40%;
        background-color: var(--bulb-off-color); /* Off state */
        border: 2px solid var(--border-color);
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        transition: background-color 0.5s ease, box-shadow 0.5s ease;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.1);
    }

     /* Styling for bulb components (filament, LED dots) */
     .filament, .led-elements {
         position: absolute;
         top: 50%;
         left: 50%;
         transform: translate(-50%, -50%);
         z-index: 2; /* Above glow and heat */
     }

     .filament {
         width: 10px;
         height: 30px;
         border-radius: 2px;
         background-color: #ccc; /* Off state */
         transition: background-color 0.3s ease;
     }

     .incandescent-bulb.on .filament {
         background-color: gold; /* On state */
         box-shadow: 0 0 8px gold;
     }

     .led-elements {
         width: 30px;
         height: 15px;
         display: flex;
         justify-content: space-around;
     }

     .led-elements::before, .led-elements::after {
         content: '';
         display: block;
         width: 8px;
         height: 8px;
         border-radius: 50%;
         background-color: #ccc; /* Off state */
         transition: background-color 0.3s ease;
     }

     .led-bulb.on .led-elements::before, .led-bulb.on .led-elements::after {
         background-color: lightblue; /* On state */
         box-shadow: 0 0 6px lightblue;
     }

     /* Light Glow Effect */
     .light-glow {
         position: absolute;
         top: 0;
         left: 0;
         width: 100%;
         height: 100%;
         border-radius: 50% / 60% 60% 40% 40%;
         opacity: 0;
         transition: opacity 0.5s ease-in-out;
         pointer-events: none;
         z-index: 1; /* Below filament/LEDs */
     }

     .incandescent-bulb.on .light-glow {
         opacity: 1;
         box-shadow: 0 0 30px 10px var(--incandescent-light-color), 0 0 60px 20px rgba(255, 140, 0, 0.4); /* Warm glow */
     }

     .led-bulb.on .light-glow {
         opacity: 1;
         box-shadow: 0 0 25px 8px var(--led-light-color), 0 0 50px 15px rgba(0, 191, 255, 0.3); /* Cool glow */
     }


    /* Heat Waves Visualization */
    .heat-waves {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        opacity: 0;
        transition: opacity 0.8s ease-in-out;
        background: radial-gradient(circle at 50% 70%, var(--heat-color) 0%, rgba(255, 165, 0, 0.6) 40%, rgba(255, 255, 0, 0.3) 60%, rgba(255, 255, 255, 0) 80%);
        z-index: 0; /* Farthest back */
    }

    .incandescent-bulb.on .heat-waves {
        opacity: 0.8; /* High heat */
        animation: pulse-heat 2s infinite alternate ease-in-out;
    }

    .led-bulb.on .heat-waves {
        opacity: 0.3; /* Low heat */
    }

    @keyframes pulse-heat {
        0% { transform: scale(0.95); opacity: 0.7; }
        100% { transform: scale(1.05); opacity: 0.9; }
    }


    /* Energy Flow Visualization (Particles) */
    .energy-in {
        position: absolute;
        width: 100%;
        height: 100%;
        overflow: hidden; /* Keep particles inside bulb */
        z-index: 3; /* Above bulb elements */
    }
    .energy-in::before {
        content: '';
        position: absolute;
        bottom: -10px; /* Start from base */
        left: 50%;
        transform: translateX(-50%);
        width: 10px;
        height: 10px;
        background-color: #007bff; /* Blue for incoming energy */
        border-radius: 50%;
        opacity: 0;
    }

     .bulb-visual.on .energy-in::before {
        opacity: 1;
        animation: flow-in 1s linear infinite;
     }

    @keyframes flow-in {
        0% { transform: translate(-50%, 0) scale(0.5); opacity: 0.8; }
        50% { transform: translate(-50%, -100px) scale(1); opacity: 1; }
        100% { transform: translate(-50%, -200px) scale(0.5); opacity: 0.8; }
    }

    .energy-out {
        position: absolute;
        width: 100%;
        height: 100%;
        overflow: hidden;
        z-index: 3; /* Above bulb elements */
    }

    .light-particles::before, .heat-particles::before {
         content: '';
         position: absolute;
         top: 40%; /* Emerge from center */
         left: 50%;
         transform: translateX(-50%);
         width: 6px;
         height: 6px;
         border-radius: 50%;
         opacity: 0;
    }

    .light-particles::before {
        background-color: yellow; /* Light color */
        animation: radiate-light 1.5s ease-out infinite;
    }

    .heat-particles::before {
        background-color: orangered; /* Heat color */
         animation: radiate-heat 2s ease-out infinite;
    }

     .incandescent-bulb.on .light-particles::before { opacity: 0.5; animation-delay: 0.1s; } /* More heat particles */
     .incandescent-bulb.on .heat-particles::before { opacity: 0.8; animation-delay: 0s; }

     .led-bulb.on .light-particles::before { opacity: 0.8; animation-delay: 0s; } /* More light particles */
     .led-bulb.on .heat-particles::before { opacity: 0.3; animation-delay: 0.1s; }

    @keyframes radiate-light {
        0% { transform: translate(-50%, -50%) scale(0.5); opacity: 1; }
        100% { transform: translate(calc(-50% + var(--dx)), calc(-50% + var(--dy))) scale(1.5); opacity: 0; }
    }

     @keyframes radiate-heat {
         0% { transform: translate(-50%, -50%) scale(0.5); opacity: 1; }
         100% { transform: translate(calc(-50% + var(--dx)), calc(-50% + var(--dy))) scale(1.2); opacity: 0; }
     }
     /* Need JS to set --dx, --dy CSS variables for random directions */


    .toggle-button {
        padding: 12px 25px; /* Larger button */
        font-size: 1em; /* Base font size */
        cursor: pointer;
        margin-bottom: 25px;
        border: none;
        border-radius: 6px; /* More rounded */
        background-color: var(--button-on-color); /* Default to On color? Or Off? Let's match state */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        min-width: 100px; /* Fixed width */
    }

     .toggle-button.on {
        background-color: var(--button-off-color);
     }

    .toggle-button:hover {
        opacity: 0.95;
    }
    .toggle-button:active {
        transform: scale(0.98);
    }


    .indicators {
        text-align: left;
        margin-top: 20px;
        font-size: 0.95em;
        width: 100%; /* Ensure indicators take full width */
    }

     .indicators p {
         margin-bottom: 10px; /* More space */
         display: flex; /* Align icon and text */
         align-items: center;
         gap: 5px;
     }

    .spectrum-indicator {
        margin-top: 15px;
        margin-bottom: 20px;
    }

    .spectrum-bar {
        width: 100%;
        height: 25px; /* Taller bar */
        border-radius: 5px;
        margin-top: 8px; /* More space */
        border: 1px solid var(--border-color);
        background: linear-gradient(to right,
             hsl(0, 100%, 60%),    /* Red */
             hsl(60, 100%, 60%),   /* Yellow */
             hsl(120, 100%, 40%),  /* Green */
             hsl(180, 100%, 50%),  /* Cyan */
             hsl(240, 100%, 60%),  /* Blue */
             hsl(300, 100%, 60%)   /* Magenta */
         ); /* Vivid base spectrum */
        opacity: 0.3; /* Off state */
        transition: opacity 0.5s ease;
    }

    /* Enhanced Spectrum Visualization */
    .spectrum-bar.incandescent-spectrum {
        background: linear-gradient(to right, #ff4500, #ffa500, #ffd700, #ffff00, #9acd32, #6495ed, #8a2be2); /* Warm emphasis + smoother */
        opacity: 1;
         box-shadow: 0 0 8px rgba(255, 165, 0, 0.5);
    }

     .spectrum-bar.led-spectrum {
         background: linear-gradient(to right, rgba(0,255,255,0.5), rgba(0,191,255,0.8), rgba(0,0,255,1), rgba(138,43,226,0.7), rgba(255,0,255,0.4), rgba(255,69,0,0.2), rgba(255,215,0,0.1), rgba(144,238,144,0)); /* Example with peaks - visualization */
        opacity: 1;
         box-shadow: 0 0 8px rgba(0, 191, 255, 0.5);
     }


    .efficiency-indicator {
        margin-top: 20px;
    }
     .efficiency-indicator p {
         justify-content: center; /* Center the percentages */
         gap: 15px; /* Space between percents */
     }

    .efficiency-chart {
        width: 100%;
        height: 30px; /* Taller chart */
        display: flex;
        border-radius: 5px; /* Less rounded */
        overflow: hidden;
        border: 1px solid var(--border-color);
        margin-top: 8px; /* Space below label */
    }

    .efficiency-bar {
        height: 100%;
        transition: width 0.8s ease-out; /* Smooth animation */
    }

    .light-bar {
        background-color: var(--light-efficiency-color); /* Yellow/Gold for light */
    }

    .heat-bar {
        background-color: var(--heat-efficiency-color); /* Red for heat */
    }

    #show-explanation-button {
        display: block;
        margin: 50px auto 30px auto; /* More vertical space */
        padding: 12px 25px;
        font-size: 1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: #007bff;
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

     #show-explanation-button:hover {
        background-color: #0056b3;
     }
     #show-explanation-button:active {
         transform: scale(0.98);
     }

    #explanation {
        margin-top: 30px; /* More space */
        padding: 30px; /* More padding */
        border-top: 2px solid #007bff; /* Stronger, colored border */
        background-color: var(--card-background);
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
        display: none; /* Initially hidden */
    }

    #explanation h2 {
         color: #0056b3;
         margin-top: 0;
         margin-bottom: 20px;
         font-size: 1.6em;
    }
    #explanation h3 {
        color: #007bff;
        margin-top: 25px; /* Space above sections */
        margin-bottom: 12px;
        font-size: 1.2em;
    }

    #explanation p {
        margin-bottom: 15px; /* More space between paragraphs */
        line-height: 1.7;
    }
     #explanation ul {
         margin-bottom: 15px;
     }
      #explanation li {
          margin-bottom: 8px;
      }
</style>

<button id="show-explanation-button">הצג/י הסבר מעמיק ומרתק</button>

<div id="explanation">
    <h2>הסבר מעמיק: מאחורי הקלעים של נורות ליבון ו-LED</h2>

    <h3>מסע בזמן קצר: מהפכת התאורה</h3>
    <p>תחשבו על זה - במשך עשורים רבים, הדרך העיקרית שלנו להאיר את החושך בבתים הייתה באמצעות המצאה שהיא בעצם תנור קטן! נורת הליבון, פרי פיתוח של פורצי דרך כמו תומס אדיסון, הייתה פלא טכנולוגי בזמנו, אבל היא בזבזה כמויות עצומות של אנרגיה. המעבר הדרמטי לנורות LED (Light Emitting Diode) הוא לא רק שינוי של נורה, אלא מהפכה של ממש ביעילות, באורך חיים ובהשפעה הסביבתית שלנו.</p>

    <h3>נורת ליבון: פיזיקה של חום זוהר</h3>
    <p>העיקרון של נורת ליבון פשוט להפליא: זרם חשמלי עובר בחוט דקיק מחומר בעל התנגדות גבוהה (בדרך כלל טונגסטן), מה שגורם לו להתחמם בצורה קיצונית (ליבון). כשהחוט מגיע לטמפרטורות של אלפי מעלות, הוא מתחיל לפלוט קרינה - קרינת "גוף שחור". חלק קטן מאוד מהקרינה הזו נמצא בתחום האור הנראה לעינינו, ואילו רובה המכריע נפלט כאנרגיית חום (קרינה אינפרה-אדום). זה כמו לנסות להדליק חדר עם תנור חימום - הוא אמנם פולט קצת אור כשהגוף החימום לוהט, אבל זו ממש לא מטרתו העיקרית. לכן, נורות ליבון הן מבזבזות אנרגיה ענקיות.</p>

    <h3>נורת LED: קסם של אלקטרוניקה מודרנית</h3>
    <p>נורות LED פועלות על עיקרון שונה לחלוטין, מעולם המוליכים למחצה. חשמל עובר דרך רכיב אלקטרוני מיוחד (הדיודה), וגורם לאלקטרונים לנוע בין שכבות שונות. כשהם עוברים ממצב אנרגטי גבוה לנמוך יותר, הם פולטים את האנרגיה העודפת בצורת פוטונים - חלקיקי אור. צבע האור נקבע על ידי החומרים המדויקים מהם עשויה הדיודה. נורות LED "לבנות" מודרניות הן למעשה שילוב מתוחכם - לרוב דיודה כחולה המצופה בחומר שפולט אור צהוב (זרחן), והשילוב של כחול וצהוב יוצר אצלנו במוח תחושה של אור לבן. התהליך הזה יעיל בהרבה בהמרת אנרגיה חשמלית ישירות לאור, עם פליטת חום מינימלית יחסית.</p>

    <h3>יעילות אנרגטית: המספרים מדברים בעד עצמם</h3>
    <p>כאן טמון ההבדל הגדול והמשמעותי ביותר. הסימולציה שלנו מראה זאת בבהירות: נורת ליבון הופכת רק כ-10%-15% מהחשמל לאור, והשאר (85%-90%!) הופך לחום. לעומת זאת, נורת LED מודרנית הופכת 80%-90% מהחשמל לאור, ורק 10%-20% הופכים לחום. דמיינו את החיסכון העצום בחשבון החשמל של מדינה שלמה שעוברת מליבון ל-LED!</p>

    <h3>חום: לגעת או לא לגעת?</h3>
    <p>הבדל היעילות מתבטא ישירות בפליטת החום. נורת ליבון לוהטת! מסוכן לגעת בה לאחר שהייתה דלוקה זמן קצר. היא גם תורמת לחימום הבית בקיץ, מה שמצריך שימוש מוגבר במיזוג. נורת LED כמעט ואינה פולטת חום משמעותי; היא אולי תתחמם מעט למגע, אבל היא בטוחה בהרבה ואינה משפיעה כמעט על טמפרטורת החדר.</p>

    <h3>ספקטרום האור: על איכות הצבעים</h3>
    <p>אור הליבון, כקרינת גוף שחור, פולט ספקטרום "רציף" של אור - כלומר, יש בו ייצוג של כמעט כל צבעי הקשת בצורה חלקה, עם דגש קל על הצד החם (אדומים, כתומים). לכן, צבעים נראים טבעיים ונאמנים מאוד תחת אור ליבון (מדד CRI קרוב ל-100). נורות LED, לעומת זאת, פולטות אור ב"פסים" אנרגטיים מסוימים (התלויים בהרכב המוליכים למחצה והזרחן). למרות שנורות LED לבנות מכוונות לייצר אור שיראה לנו לבן, הספקטרום שלהן שונה. נורות LED איכותיות מגיעות היום למדדי CRI גבוהים מאוד (90+), כך שההבדל ביכולת מסירת הצבע קטן, אך עדיין קיים וחשוב ליישומים כמו תאורת אמנות או צילום.</p>

    <h3>שורה תחתונה: יתרונות, חסרונות וניצחון מוחץ</h3>
    <ul>
        <li>**יעילות אנרגטית:** LED מנצחת בנוק-אאוט (חיסכון של כ-80-90% באנרגיה לתאורה).</li>
        <li>**אורך חיים:** LED מחזיקה פי 25-50 יותר (עשרות אלפי שעות לעומת כ-1000 לליבון). פחות החלפות, פחות פסולת.</li>
        <li>**פליטת חום:** LED פולטת הרבה פחות חום, בטיחותית וחסכונית בקיץ.</li>
        <li>**עמידות:** LED חזקה יותר, אין בה זכוכית שבירה או חוט להט עדין.</li>
        <li>**ספקטרום:** ליבון בעלת ספקטרום טבעי יותר (CRI גבוה), אך LED משפרת זאת כל הזמן.</li>
        <li>**עלות:** LED יקרה יותר ברכישה, אך החיסכון בחשמל ובאורך החיים הופך אותה לזולה לאין ערוך בשימוש ארוך טווח.</li>
        <li>**השפעה סביבתית:** חיסכון החשמל של LED מפחית פליטות מזהמים מתחנות כוח.</li>
    </ul>
    <p>אין ספק שלנורות ליבון היה קסם וספקטרום אור נעים, אך מנקודת מבט אנרגטית וכלכלית, הן שייכות לעבר. נורות LED הן העתיד (וההווה!) של התאורה, וממחישות כיצד חדשנות טכנולוגית יכולה לשנות באופן יסודי את חיינו ואת צריכת האנרגיה שלנו.</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const incandescentBulb = document.getElementById('incandescent-bulb');
        const ledBulb = document.getElementById('led-bulb');
        const toggleIncandescentButton = document.getElementById('toggle-incandescent');
        const toggleLedButton = document.getElementById('toggle-led');

        const incandescentPowerSpan = document.getElementById('incandescent-power');
        const ledPowerSpan = document.getElementById('led-power');
        const incandescentTotalEnergySpan = document.getElementById('incandescent-total-energy');
        const ledTotalEnergySpan = document.getElementById('led-total-energy');

        const incandescentSpectrumDiv = document.getElementById('incandescent-spectrum');
        const ledSpectrumDiv = document.getElementById('led-spectrum');
        const incandescentLightEfficiencyBar = document.getElementById('incandescent-light-efficiency');
        const incandescentHeatEfficiencyBar = document.getElementById('incandescent-heat-efficiency');
        const ledLightEfficiencyBar = document.getElementById('led-light-efficiency');
        const ledHeatEfficiencyBar = document.getElementById('led-heat-efficiency');
        const incandescentLightPercent = document.getElementById('incandescent-light-percent');
        const incandescentHeatPercent = document.getElementById('incandescent-heat-percent');
        const ledLightPercent = document.getElementById('led-light-percent');
        const ledHeatPercent = document.getElementById('led-heat-percent');

        const explanationDiv = document.getElementById('explanation');
        const showExplanationButton = document.getElementById('show-explanation-button');

        let isIncandescentOn = false;
        let isLedOn = false;

        let incandescentTotalEnergy = 0;
        let ledTotalEnergy = 0;
        let energyCounterInterval = null;

        // Configuration (example values for comparison brightness - same lumens)
        // A 60W incandescent bulb produces roughly the same light output (lumens)
        // as a 9-10W LED bulb.
        const INCANDESCENT_POWER_W = 60;
        const LED_POWER_W = 9;
        // Efficiency: approx percentage of energy converted to visible light
        const INCANDESCENT_EFFICIENCY_LIGHT_PERCENT = 12; // Approx 88% heat
        const LED_EFFICIENCY_LIGHT_PERCENT = 85; // Approx 15% heat

        // Particle animation settings
        const PARTICLE_COUNT = 10; // Number of particles for each type
        const PARTICLE_SPEED = 1500; // Animation duration in ms

         function createParticles(bulbElement, particleType, count) {
             const container = bulbElement.querySelector(`.${particleType}`);
             if (!container) return;
             container.innerHTML = ''; // Clear existing particles
             for (let i = 0; i < count; i++) {
                 const particle = document.createElement('div');
                 particle.style.position = 'absolute';
                 particle.style.width = '5px';
                 particle.style.height = '5px';
                 particle.style.borderRadius = '50%';
                 particle.style.backgroundColor = particleType === 'light-particles' ? 'yellow' : 'orangered';
                 particle.style.opacity = '0';
                 particle.style.transition = 'none'; // Reset transition for animation
                 container.appendChild(particle);
             }
         }

        function animateParticles(bulbElement, particleType, isOn) {
             const particles = bulbElement.querySelectorAll(`.${particleType} div`);
             if (!particles.length) return;

             particles.forEach((particle, index) => {
                 particle.style.animation = 'none'; // Reset animation
                 particle.style.opacity = '0';
                 particle.style.transform = 'translate(-50%, -50%)';

                 if (isOn) {
                     const angle = Math.random() * 360;
                     const distance = Math.random() * 80 + 50; // Radiate outwards
                     const dx = Math.cos(angle * Math.PI / 180) * distance;
                     const dy = Math.sin(angle * Math.PI / 180) * distance;

                     // Set CSS variables for keyframes
                     particle.style.setProperty('--dx', `${dx}px`);
                     particle.style.setProperty('--dy', `${dy}px`);

                     setTimeout(() => {
                         particle.style.animation = `${particleType === 'light-particles' ? 'radiate-light' : 'radiate-heat'} ${PARTICLE_SPEED}ms ease-out infinite`;
                         particle.style.animationDelay = `${Math.random() * (PARTICLE_SPEED / particles.length)}ms`; // Stagger start
                          particle.style.opacity = particleType === 'light-particles' ? (bulbElement.classList.contains('led-bulb.on') ? '0.8' : '0.5') : (bulbElement.classList.contains('incandescent-bulb.on') ? '0.8' : '0.3'); // Base opacity based on efficiency
                     }, 10); // Small delay to re-trigger animation
                 }
             });
        }

        function updateBulbState(type) {
            const is diffusing = type === 'incandescent' ? isIncandescentOn : isLedOn;
            const bulbVisual = type === 'incandescent' ? incandescentBulb : ledBulb;
            const toggleButton = type === 'incandescent' ? toggleIncandescentButton : toggleLedButton;
            const powerSpan = type === 'incandescent' ? incandescentPowerSpan : ledPowerSpan;
            const heatWavesDiv = bulbVisual.querySelector('.heat-waves');
            const lightGlowDiv = bulbVisual.querySelector('.light-glow');
            const spectrumDiv = type === 'incandescent' ? incandescentSpectrumDiv : ledSpectrumDiv;
            const lightEffBar = type === 'incandescent' ? incandescentLightEfficiencyBar : ledLightEfficiencyBar;
            const heatEffBar = type === 'incandescent' ? incandescentHeatEfficiencyBar : ledHeatEfficiencyBar;
            const lightPercentSpan = type === 'incandescent' ? incandescentLightPercent : ledLightPercent;
            const heatPercentSpan = type === 'incandescent' ? incandescentHeatPercent : ledHeatPercent;

            if (is diffusing) {
                bulbVisual.classList.add('on');
                lightGlowDiv.style.opacity = 1;
                toggleButton.textContent = 'כיבוי';
                toggleButton.classList.add('on');
                powerSpan.textContent = type === 'incandescent' ? INCANDESCENT_POWER_W : LED_POWER_W;

                if (type === 'incandescent') {
                    heatWavesDiv.style.opacity = 0.8;
                    heatWavesDiv.style.animation = 'pulse-heat 2s infinite alternate ease-in-out';
                    spectrumDiv.classList.add('incandescent-spectrum');
                    spectrumDiv.classList.remove('led-spectrum');
                    lightEffBar.style.width = INCANDESCENT_EFFICIENCY_LIGHT_PERCENT + '%';
                    heatEffBar.style.width = (100 - INCANDESCENT_EFFICIENCY_LIGHT_PERCENT) + '%';
                    lightPercentSpan.textContent = INCANDESCENT_EFFICIENCY_LIGHT_PERCENT;
                    heatPercentSpan.textContent = 100 - INCANDESCENT_EFFICIENCY_LIGHT_PERCENT;
                     animateParticles(bulbVisual, 'light-particles', true);
                     animateParticles(bulbVisual, 'heat-particles', true);
                } else { // LED
                    heatWavesDiv.style.opacity = 0.3;
                     heatWavesDiv.style.animation = 'none'; // No pulsing heat
                    spectrumDiv.classList.remove('incandescent-spectrum');
                    spectrumDiv.classList.add('led-spectrum');
                    lightEffBar.style.width = LED_EFFICIENCY_LIGHT_PERCENT + '%';
                    heatEffBar.style.width = (100 - LED_EFFICIENCY_LIGHT_PERCENT) + '%';
                    lightPercentSpan.textContent = LED_EFFICIENCY_LIGHT_PERCENT;
                    heatPercentSpan.textContent = 100 - LED_EFFICIENCY_LIGHT_PERCENT;
                     animateParticles(bulbVisual, 'light-particles', true);
                     animateParticles(bulbVisual, 'heat-particles', true);
                }
                spectrumDiv.style.opacity = 1;


            } else {
                bulbVisual.classList.remove('on');
                lightGlowDiv.style.opacity = 0;
                toggleButton.textContent = 'הדלק/י';
                toggleButton.classList.remove('on');
                powerSpan.textContent = 0;
                heatWavesDiv.style.opacity = 0;
                 heatWavesDiv.style.animation = 'none';
                spectrumDiv.classList.remove('incandescent-spectrum', 'led-spectrum');
                spectrumDiv.style.opacity = 0.3; /* Off state */
                lightEffBar.style.width = '0%';
                heatEffBar.style.width = '0%';
                lightPercentSpan.textContent = 0;
                heatPercentSpan.textContent = 0;
                 animateParticles(bulbVisual, 'light-particles', false);
                 animateParticles(bulbVisual, 'heat-particles', false);
            }
            updateEnergyCounter(); // Update counter state
        }

        function updateEnergyCounter() {
            if (isIncandescentOn || isLedOn) {
                if (!energyCounterInterval) {
                    let lastTime = performance.now();
                    energyCounterInterval = setInterval(() => {
                        const currentTime = performance.now();
                        const deltaTimeMs = currentTime - lastTime;
                        const deltaTimeSec = deltaTimeMs / 1000; // Time in seconds
                        lastTime = currentTime;

                        if (isIncandescentOn) {
                            incandescentTotalEnergy += INCANDESCENT_POWER_W * deltaTimeSec;
                            incandescentTotalEnergySpan.textContent = incandescentTotalEnergy.toFixed(1);
                        }
                         if (isLedOn) {
                             ledTotalEnergy += LED_POWER_W * deltaTimeSec;
                             ledTotalEnergySpan.textContent = ledTotalEnergy.toFixed(1);
                         }

                    }, 100); // Update every 100ms
                }
            } else {
                clearInterval(energyCounterInterval);
                energyCounterInterval = null;
            }
        }


        toggleIncandescentButton.addEventListener('click', () => {
            isIncandescentOn = !isIncandescentOn;
            updateBulbState('incandescent');
        });

        toggleLedButton.addEventListener('click', () => {
            isLedOn = !isLedOn;
            updateBulbState('led');
        });

        showExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            showExplanationButton.textContent = isHidden ? 'הסתר הסבר מעמיק' : 'הצג/י הסבר מעמיק ומרתק';
        });

         // Initial setup for particles
         createParticles(incandescentBulb, 'light-particles', PARTICLE_COUNT * (INCANDESCENT_EFFICIENCY_LIGHT_PERCENT / 100));
         createParticles(incandescentBulb, 'heat-particles', PARTICLE_COUNT * ((100 - INCANDESCENT_EFFICIENCY_LIGHT_PERCENT) / 100));
         createParticles(ledBulb, 'light-particles', PARTICLE_COUNT * (LED_EFFICIENCY_LIGHT_PERCENT / 100));
         createParticles(ledBulb, 'heat-particles', PARTICLE_COUNT * ((100 - LED_EFFICIENCY_LIGHT_PERCENT) / 100));


    });
</script>
```