---
title: "צבעים מהטבע: סודות הצביעה הקדומה"
english_slug: colors-from-nature-ancient-dyeing-secrets
category: "ארכאולוגיה"
tags:
  - צבעים טבעיים
  - צביעה
  - עת העתיקה
  - כימיה
  - מלאכה קדומה
---
<h1>צבעים מהטבע: מסע אל סודות הצביעה הקדומה</h1>
<p>דמיינו עולם שבו כל צבע בבגד, בשטיח או בציור, מגיע ישירות מהאדמה, מהצומח או מהים. רגע לפני המצאת הצבעים הסינתטיים, האנושות יצרה עולמות ססגוניים להפליא באמצעות אוצרות הטבע בלבד. בואו נצלול יחד למעבדה הקדומה של הצבע ונגלה איך עשו זאת.</p>

<div id="dye-simulator" class="interactive-block">
    <h2>חוויית הצביעה הקדומה: הדמיה אינטראקטיבית</h2>
    <p>בחר/י חומר גלם מהטבע ושיטת מיצוי קדומה, וראה/י איך הצבעים מתגלים לעולם!</p>
    <div class="controls">
        <div class="control-group">
            <label for="material"><i class="icon material-icon"></i> חומר גלם מהטבע:</label>
            <select id="material">
                <option value="">-- בחר חומר --</option>
                <option value="madder">שורש פואת הצבעים (אדום)</option>
                <option value="indigo">עלי אינדיגו (כחול)</option>
                <option value="red-ochre">אבן אוכרה אדומה (פיגמנט)</option>
                <option value="yellow-ochre">אוכרה צהובה (פיגמנט)</option>
                <option value="pomegranate">קליפות רימונים (צהוב-חום)</option>
                <option value="tyrian">חלזונות ארגמן (סגול מלכותי)</option>
            </select>
        </div>

        <div class="control-group" id="method-group" style="display: none;">
            <label for="method" id="method-label"><i class="icon method-icon"></i> שיטת מיצוי עתיקה:</label>
            <select id="method">
                <!-- Options populated by JS based on material -->
            </select>
        </div>

        <button id="simulate-btn" disabled>צא למסע הצביעה!</button>
    </div>

    <div class="simulation-area">
        <div id="animation">
             <div class="icon placeholder-icon">?</div>
            <p>בחר/י חומר גלם ושיטת מיצוי כדי להתחיל את הקסם...</p>
        </div>
        <div id="result">
            <p>דגימת הבד שנצבעה:</p>
            <div id="fabric-sample"></div>
        </div>
    </div>
     <div class="color-info" style="display: none;">
        <p>התקבל הצבע: <span id="color-name"></span></p>
    </div>
</div>

<button id="toggle-explanation" class="explanation-button">רוצה לדעת יותר? הצג/הסתר את הסיפור המלא</button>
<div id="explanation" style="display: none;">
    <h2>צבעים מהטבע בעת העתיקה - הסיפור המלא</h2>
    <p>צבעים טבעיים היו אוצר יקר מפז בעולם העתיק. הם הופקו משלל מקורות מפתיעים: צמחים (שורשים, עלים, פרחים, פירות, קליפות, עצה), מינרלים שמקורם באדמה (עפרות מתכת, אדמות צבעוניות עשירות במינרלים) ואפילו מבעלי חיים ימיים או חרקים ייחודיים.</p>
    <p>חומרי גלם נפוצים ומרתקים לצביעה בעת העתיקה כללו:</p>
    <ul>
        <li><p><b>שורשי פואת הצבעים (Rubia tinctorum):</b> עשב שורשיו מסתירים בתוכם פיגמנטים אדומים חזקים. שימשו ליצירת גווני אדום וורוד עזים, כמו אלה שנמצאו באריגים ארכיאולוגיים ממצדה.</p></li>
        <li><p><b>עלי אינדיגו (Indigofera tinctoria):</b> צמח טרופי שהיה המקור העיקרי לצבע הכחול העמוק (אינדיגו). שלא כמו צבעים רבים אחרים, צבע האינדיגו אינו מסיס במים ודורש תהליך כימי מורכב של תסיסה בחומר בסיסי כדי שיוכל להיקשר לבד. הצבע מתפתח לגוון הכחול העמוק רק בחשיפה לאוויר! שימש לצביעת בגדי עבודה יומיומיים וגם אריגים מפוארים.</p></li>
        <li><p><b>קליפות רימונים (Punica granatum):</b> פסולת אורגנית שהפכה לאוצר! קליפות הרימונים, עשירות בטאנינים, שימשו להפקת צבעים צהובים וחומים-צהבהבים. הטאנינים גם סייעו בקיבוע הצבע לבד.</p></li>
        <li><p><b>אוכרה (Ochre):</b> לא רק לצביעת בדים! אדמות צבעוניות אלו, המכילות תחמוצות ברזל, שימשו בעיקר כפיגמנטים לציור, לקעקועים (קדומים מאוד!), ולצביעה ישירה של עור או חומרים אחרים. הן הניבו מגוון גוונים מרהיבים של אדום, צהוב וחום בהתאם להרכב המינרלי ולטמפרטורת החימום (או חוסר החימום).</p></li>
        <li><p><b>חלזונות ארגמן (Murex/Bolinus brandaris):</b> יוקרה בהתגלמותה! מבלוטה זעירה אצל מספר מיני חלזונות ימיים הפיקו את צבעי הסגול-אדמדם העשירים (ארגמן) והכחול העמוק (תכלת). הפקת כמות קטנה של צבע דרשה אלפי חלזונות ותהליך מסריח ומורכב לאין ערוך. כתוצאה מכך, צבעי הארגמן והתכלת היו יקרים באופן אגדי, שימשו כסמל סטטוס אולטימטיבי, ולעיתים קרובות הוגבלו בחוק רק למלכים, כוהנים, ואישים רמי מעלה ביותר.</p></li>
    </ul>
    <p>תהליכי ההפקה היו ידע סודי שעבר מדור לדור:</p>
    <ul>
        <li><p><b>מיצוי בנוזלים (מים, לעיתים שתן או נוזלים אחרים):</b> שיטה נפוצה לצבעים צמחיים רבים. החומר נטבל או הורתח בנוזל כדי "למשוך" את מולקולות הצבע.</p></li>
        <li><p><b>טחינה:</b> פיגמנטים מינרליים כמו אוכרה פשוט נטחנו לאבקה דקה מאוד, לרוב עורבבו עם חומר מקשר טבעי (כמו שמן, ביצה או שרף) כדי ליצור צבע נוזלי או משחה לשימוש בציור, או שפשפו את האבקה היבשה או הלחה ישירות.</p></li>
        <li><p><b>תסיסה:</b> תהליך מורכב ההופך חומרים בלתי מסיסים (כמו האינדיגו) לחומרים מסיסים. שימש גם להכנת אמבטיות צביעה מסוימות מצמחים אחרים.</p></li>
    </ul>
    <p>אחד הסודות הגדולים של הצביעה הטבעית היה השימוש ב<b>חומרים מקבעים (Mordants)</b>. חומרים אלו, שלרוב היו מלחים מתכתיים (כמו אלום שהופק ממינרלים או צמחים מסוימים, או מלחי ברזל/נחושת), יצרו "גשר" כימי בין מולקולות הצבע לסיבי הבד. בלעדיהם, צבעים רבים היו פשוט נשטפים בכביסה. מעבר לקיבוע, החומר המקבע יכול היה לשנות את הגוון הסופי של הצבע באופן דרמטי! אותו חומר גלם יכול היה להניב גוונים שונים לגמרי עם מקבעים שונים.</p>
    <p>הצביעה הטבעית הייתה אמנות ומדע כאחד, שדרשו מומחיות, סבלנות, וכמויות עצומות של חומר גלם. האתגרים הללו הם שהפכו צבעים מסוימים לסמלי סטטוס כה עוצמתיים. כעת, כשיש לנו את הכל בלחיצת כפתור, קל לשכוח את המסע הארוך והמרתק שעברו הצבעים שלנו.</p>
</div>

<style>
    /* Overall body & layout */
    body {
         font-family: 'Arial Hebrew', Arial, sans-serif; /* Prefer Hebrew font */
         direction: rtl; /* Right-to-left layout */
         text-align: right;
         line-height: 1.6;
         color: #333;
         background-color: #f4f0e6; /* Soft, earthy background */
         margin: 0;
         padding: 20px;
    }

    h1, h2 {
        color: #5a4a3a; /* Muted brown */
        text-align: center;
        margin-bottom: 20px;
    }

    h1 {
        font-size: 2em;
        border-bottom: 2px solid #d4c19e; /* Subtle underline */
        padding-bottom: 10px;
    }

     h2 {
        font-size: 1.5em;
        margin-top: 30px;
     }

    p {
        margin-bottom: 15px;
    }

    ul {
        list-style-type: disc;
        margin-right: 25px;
        margin-bottom: 15px;
    }

    li {
        margin-bottom: 8px;
    }

    b {
        color: #6a5a4a; /* Slightly darker brown for emphasis */
    }


    /* Simulator Styling */
    .interactive-block {
        border: 1px solid #d4c19e; /* Earthy border */
        padding: 30px;
        margin: 30px auto;
        border-radius: 12px;
        background-color: #fff; /* White background for the block */
        box-shadow: 5px 5px 15px rgba(0,0,0,0.1); /* Soft shadow */
        max-width: 700px; /* Limit width */
    }

    .interactive-block h2 {
         color: #4a3a2a;
         margin-top: 0;
         margin-bottom: 15px;
    }

    .interactive-block > p {
        text-align: center;
        font-style: italic;
        color: #555;
        margin-bottom: 25px;
    }

    .controls {
        display: flex;
        flex-direction: column;
        gap: 20px;
        margin-bottom: 30px;
        padding-bottom: 20px;
        border-bottom: 1px dashed #d4c19e;
    }

    .control-group {
        display: flex;
        align-items: center;
        gap: 15px;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
    }

    .controls label {
        font-weight: bold;
        min-width: 120px; /* Align labels better */
        color: #4a3a2a;
        display: flex; /* Align icon and text */
        align-items: center;
        gap: 5px;
    }

     .icon {
        width: 20px;
        height: 20px;
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        display: inline-block;
        vertical-align: middle; /* Align with text baseline */
     }

    .material-icon { background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="%236a5a4a"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm0 18a8 8 0 1 1 8-8A8 8 0 0 1 12 20zM8 13a1 1 0 0 1-1-1 1 1 0 0 1 1-1h8a1 1 0 0 1 1 1 1 1 0 0 1-1 1z"/></svg>'); } /* Generic plant/earth icon */
    .method-icon { background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="%236a5a4a"><path d="M12 22a4 4 0 0 1-4-4V9a4 4 0 0 1 8 0v9a4 4 0 0 1-4 4zm0-14a2 2 0 0 0-2 2v8a2 2 0 0 0 4 0V10a2 2 0 0 0-2-2zM5 9a1 1 0 0 0 0 2h2a1 1 0 0 0 0-2H5zm12 0a1 1 0 0 0 0 2h2a1 1 0 0 0 0-2h-2zM9 4h6v1a1 1 0 0 1-2 0V4H9z"/></svg>'); } /* Beaker/process icon */
     .placeholder-icon {
         background-color: #d4c19e;
         border-radius: 50%;
         color: #fff;
         font-size: 1.2em;
         font-weight: bold;
         width: 40px;
         height: 40px;
         display: flex;
         align-items: center;
         justify-content: center;
         margin-bottom: 10px;
     }


    .controls select {
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 6px;
        font-size: 1rem;
        flex-grow: 1; /* Allow select to take available space */
        min-width: 150px; /* Minimum width for select */
        background-color: #f9f9f9;
        cursor: pointer;
    }

    #simulate-btn {
        background-color: #7b9f35; /* Olive green */
        color: white;
        padding: 12px 25px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1rem;
        transition: background-color 0.3s ease, transform 0.1s ease;
        align-self: center; /* Center the button */
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
        font-weight: bold;
    }

    #simulate-btn:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        box-shadow: none;
    }

    #simulate-btn:hover:not(:disabled) {
        background-color: #6a8b2f;
        transform: translateY(-2px); /* Subtle hover effect */
    }

     #simulate-btn:active:not(:disabled) {
        transform: translateY(0);
     }


    .simulation-area {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 30px;
        padding-top: 30px;
    }

    #animation {
        border: 2px dashed #d4c19e; /* Earthy dashed border */
        padding: 20px;
        min-height: 120px; /* Give it space */
        width: 80%;
        max-width: 400px;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background-color: #fffbf0; /* Light creamy background */
        font-style: italic;
        color: #555;
        border-radius: 8px;
        position: relative; /* Needed for absolute positioning of icons/elements */
        overflow: hidden; /* Hide overflow during animations */
    }

    #animation p {
        margin: 0;
        font-size: 1em;
        color: #4a3a2a;
        font-style: normal;
    }

     /* Animation States & Icons */
     .animation-icon {
        width: 50px;
        height: 50px;
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        display: block;
        margin-bottom: 15px;
        transition: transform 0.5s ease-in-out, opacity 0.5s ease-in-out;
     }

     .icon-boiling { background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="%23e76f51"><path d="M12 2a3 3 0 0 0-3 3v6a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3zM5 15a1 1 0 0 0 0 2h14a1 1 0 0 0 0-2H5zm-1 4a1 1 0 0 0 0 2h16a1 1 0 0 0 0-2H4z"/></svg>'); } /* Pot icon */
     .icon-grinding { background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="%23a0522d"><path d="M18 4h-4V2a2 2 0 0 0-4 0v2H6a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zM6 6h12v12H6zm3 3v2h6V9zm-1 5a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm8 0a1 1 0 1 0 0 2 1 1 0 0 0 0-2z"/></svg>'); } /* Mortar and pestle icon */
     .icon-fermentation { background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="%232a9d8f"><path d="M19 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V5a2 2 0 0 0-2-2zm-1 16H6V6h12zM8 9a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v6a1 1 0 0 1-1 1h-6a1 1 0 0 1-1-1zm2 1v4h4v-4z"/></svg>'); } /* Jar/vat icon */
     .icon-tyrian { background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="%23800080"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>'); } /* Crown/royal icon */
     .icon-grinding-rubbing { background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="%23a0522d"><path d="M13 6.99l1.41 1.41L11 11.83l-2.41-2.41L7.17 10 11 13.83l4.41-4.41L17 10.17l-6 6-4-4 1.41-1.41zM12 2c-5.52 0-10 4.48-10 10s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z"/></svg>');} /* Fingerprint or rubbing icon */
     .icon-finished { background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="%237b9f35"><path d="M12 2c-5.52 0-10 4.48-10 10s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>'); } /* Checkmark icon */

     @keyframes pulse {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.1); opacity: 0.8; }
        100% { transform: scale(1); opacity: 1; }
     }

      @keyframes fade-in {
        0% { opacity: 0; transform: translateY(10px); }
        100% { opacity: 1; transform: translateY(0); }
      }

     .pulsing {
        animation: pulse 1.5s infinite ease-in-out;
     }

     .fade-in {
         animation: fade-in 0.8s ease-out forwards;
     }


    #result {
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    #result p {
        margin-bottom: 15px;
        font-weight: bold;
        color: #4a3a2a;
    }

    #fabric-sample {
        width: 150px; /* Larger sample */
        height: 150px;
        border: 3px dashed #6a5a4a; /* Stronger border */
        margin: 0 auto;
        background-color: #e0d8c0; /* Uncolored fabric look */
        box-shadow: 4px 4px 8px rgba(0,0,0,0.2);
        position: relative; /* For potential future texture/pattern */
        overflow: hidden; /* Hide any overflow */
        transition: background-color 2s ease-in-out; /* Smooth color transition */
        display: flex;
        align-items: center;
        justify-content: center;
        color: #555;
        font-size: 0.9em;
        font-style: italic;
    }

    #fabric-sample::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: repeating-linear-gradient(
            45deg,
            rgba(255,255,255,0.1),
            rgba(255,255,255,0.1) 2px,
            transparent 2px,
            transparent 4px
        ); /* Simple fabric texture */
        pointer-events: none;
    }

    .color-info {
        text-align: center;
        margin-top: 20px;
        font-weight: bold;
        color: #4a3a2a;
    }

    .color-info span {
        color: #000; /* Will be overridden by JS color */
    }


    /* Explanation Styling */
    .explanation-button {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        background-color: #a0522d; /* Sienna/earthy brown */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1rem;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
        font-weight: bold;
    }

    .explanation-button:hover {
        background-color: #8b4513;
        transform: translateY(-2px);
    }

    .explanation-button:active {
        transform: translateY(0);
    }

    #explanation {
        border: 1px solid #d4c19e;
        padding: 30px;
        margin: 20px auto;
        border-radius: 12px;
        background-color: #fffbf0; /* Light creamy background */
        direction: rtl;
        text-align: right;
        max-width: 700px; /* Match simulator width */
        box-shadow: 5px 5px 15px rgba(0,0,0,0.08);
    }

     #explanation h2 {
         color: #4a3a2a;
         margin-top: 0;
         margin-bottom: 20px;
     }


</style>

<script>
    const dyeData = {
        "madder": {
            name: "שורש פואת הצבעים (אדום)",
            methods: {
                "boiling": {
                    name: "הרתחה במים",
                    resultColor: "#A52A2A", // Brownish-red
                    colorName: "אדום-חום (פואה)",
                    animationSteps: [
                        { text: "טוחנים ומכניסים את שורשי הפואה לסיר...", iconClass: "icon-grinding pulsing" },
                        { text: "מוסיפים מים ומרתיחים. הצבע האדום משתחרר לאט לאט...", iconClass: "icon-boiling pulsing" },
                        { text: "טובלים את הבד באמבט הצבע החם...", iconClass: "icon-boiling" } // Keep pot icon but stop pulsing
                    ]
                }
            }
        },
        "indigo": {
            name: "עלי אינדיגו (כחול)",
            methods: {
                "fermentation": {
                    name: "תסיסה (שיטה מסורתית)",
                    resultColor: "#00008B", // Dark Blue
                    colorName: "כחול עמוק (אינדיגו)",
                     animationSteps: [
                        { text: "עלי האינדיגו מושרים במיכל בסיסי ועוברים תהליך תסיסה...", iconClass: "icon-fermentation pulsing" },
                        { text: "הצבע הופך למסיס ומוכן לקליטה בבד...", iconClass: "icon-fermentation" },
                        { text: "הבד נטבל. בחשיפה לאוויר, הצבע הכחול מתפתח ומתקבע!", iconClass: "icon-finished pulsing" } // Use finished icon to show final step/oxidation
                    ]
                },
                "boiling": {
                    name: "הרתחה במים (פחות יעיל לאינדיגו)",
                    resultColor: "#ADD8E6", // Light Blue
                    colorName: "תכלת בהיר (אינדיגו - פחות עמוק)",
                    animationSteps: [
                        { text: "מרתיחים עלי אינדיגו במים...", iconClass: "icon-boiling pulsing" },
                        { text: "שיטה זו פחות יעילה להפקת הצבע הכחול העמוק...", iconClass: "icon-boiling" },
                        { text: "טובלים את הבד...", iconClass: "icon-boiling" }
                    ]
                }
            }
        },
        "red-ochre": {
            name: "אבן אוכרה אדומה (פיגמנט)",
            methods: {
                "grinding": {
                    name: "טחינה לאבקה וערבוב עם נוזל (לציור/צביעה)",
                    resultColor: "#8B0000", // Dark Red
                    colorName: "אדום עמוק (אוכרה)",
                    animationSteps: [
                         { text: "טוחנים את אבן האוכרה האדומה לאבקה דקה...", iconClass: "icon-grinding pulsing" },
                         { text: "מערבבים את האבקה עם מים או שמן ליצירת משחת צבע...", iconClass: "icon-grinding" },
                         { text: "הפיגמנט מוכן לשימוש (לרוב לא לבד בצביעה רגילה). מדגימים את הצבע...", iconClass: "icon-finished pulsing" }
                    ]
                },
                 "rubbing": {
                    name: "שפשוף ישיר על חומר (פחות עמיד בבד)",
                    resultColor: "#CD5C5C", // Indian Red
                    colorName: "אדום בהיר יותר (אוכרה - פחות מקובע)",
                    animationSteps: [
                         { text: "משפשפים את אבן האוכרה ישירות על המשטח...", iconClass: "icon-grinding-rubbing pulsing" },
                         { text: "פיגמנטים עוברים ישירות לחומר. שיטה זו פחות מקבעת...", iconClass: "icon-grinding-rubbing" },
                         { text: "הצבע מתקבל אך עשוי לרדת בקלות...", iconClass: "icon-finished pulsing" }
                    ]
                }
            }
        },
        "yellow-ochre": {
            name: "אוכרה צהובה (פיגמנט)",
            methods: {
                "grinding": {
                    name: "טחינה לאבקה וערבוב עם נוזל (לציור/צביעה)",
                    resultColor: "#DAA520", // Goldenrod
                     colorName: "צהוב זהוב (אוכרה)",
                     animationSteps: [
                         { text: "טוחנים את אבן האוכרה הצהובה לאבקה דקה...", iconClass: "icon-grinding pulsing" },
                         { text: "מערבבים את האבקה עם מים או שמן ליצירת משחת צבע...", iconClass: "icon-grinding" },
                         { text: "הפיגמנט מוכן לשימוש (לרוב לא לבד בצביעה רגילה). מדגימים את הצבע...", iconClass: "icon-finished pulsing" }
                    ]
                },
                 "rubbing": {
                    name: "שפשוף ישיר על חומר (פחות עמיד בבד)",
                    resultColor: "#FFFF00", // Yellow
                    colorName: "צהוב בהיר (אוכרה - פחות מקובע)",
                     animationSteps: [
                         { text: "משפשפים את אבן האוכרה ישירות על המשטח...", iconClass: "icon-grinding-rubbing pulsing" },
                         { text: "פיגמנטים עוברים ישירות לחומר. שיטה זו פחות מקבעת...", iconClass: "icon-grinding-rubbing" },
                         { text: "הצבע מתקבל אך עשוי לרדת בקלות...", iconClass: "icon-finished pulsing" }
                    ]
                }
            }
        },
        "pomegranate": {
            name: "קליפות רימונים (צהוב-חום)",
            methods: {
                "boiling": {
                    name: "הרתחה במים (עם או בלי מקבע)",
                    resultColor: "#B8860B", // Dark Goldenrod (more brown/earthy)
                    colorName: "צהוב-חום (רימונים)",
                     animationSteps: [
                        { text: "מכניסים קליפות רימונים לסיר...", iconClass: "icon-boiling pulsing" },
                        { text: "מרתיחים במים כדי למצות את הצבע והטאנינים...", iconClass: "icon-boiling pulsing" },
                        { text: "טובלים את הבד באמבט הצבע...", iconClass: "icon-boiling" }
                    ]
                }
            }
        },
         "tyrian": {
            name: "חלזונות ארגמן (סגול מלכותי)",
            methods: {
                "complex": {
                    name: "תהליך איסוף ומיצוי מורכב ויקר",
                    resultColor: "#4B0082", // Indigo/dark purple
                    colorName: "ארגמן מלכותי (יוקרתי!)",
                    animationSteps: [
                         { text: "אוספים אלפי חלזונות ארגמן קטנטנים...", iconClass: "icon-tyrian pulsing" },
                         { text: "מפיקים טיפות זעירות של נוזל מבלוטה מיוחדת...", iconClass: "icon-tyrian" },
                         { text: "תהליך מורכב ועתיר זמן חושף את הצבע הסגול המופלא והיקר...", iconClass: "icon-finished pulsing" }
                    ]
                }
            }
        }
    };

    const materialSelect = document.getElementById('material');
    const methodSelect = document.getElementById('method');
    const methodLabel = document.getElementById('method-label');
    const methodGroup = document.getElementById('method-group');
    const simulateButton = document.getElementById('simulate-btn');
    const animationArea = document.getElementById('animation');
    const fabricSample = document.getElementById('fabric-sample');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const colorInfoDiv = document.querySelector('.color-info');
    const colorNameSpan = document.getElementById('color-name');

    // Helper to update animation area content with icon and text
    function updateAnimationArea(text, iconClass = null) {
        animationArea.innerHTML = ''; // Clear current content
        if (iconClass) {
            const iconDiv = document.createElement('div');
            iconDiv.className = 'animation-icon ' + iconClass;
            animationArea.appendChild(iconDiv);
        } else {
             const iconDiv = document.createElement('div');
            iconDiv.className = 'icon placeholder-icon';
            iconDiv.textContent = '?';
            animationArea.appendChild(iconDiv);
        }
        const textP = document.createElement('p');
        textP.textContent = text;
        animationArea.appendChild(textP);
    }


    // Populate method options based on material selection
    materialSelect.addEventListener('change', () => {
        const selectedMaterialKey = materialSelect.value;
        methodSelect.innerHTML = ''; // Clear previous options

        if (selectedMaterialKey && dyeData[selectedMaterialKey]) {
            const methods = dyeData[selectedMaterialKey].methods;
            methodGroup.style.display = 'flex'; // Show method group
            methodSelect.style.display = 'inline-block'; // Ensure select is visible

            const defaultOption = document.createElement('option');
            defaultOption.value = "";
            defaultOption.textContent = "-- בחר שיטה --";
            methodSelect.appendChild(defaultOption);

            for (const methodKey in methods) {
                const option = document.createElement('option');
                option.value = methodKey;
                option.textContent = methods[methodKey].name;
                methodSelect.appendChild(option);
            }
             // Disable button until a method is selected
            simulateButton.disabled = true; // Initially disabled
            simulateButton.textContent = 'בחר שיטה כדי להמשיך';

        } else {
            methodGroup.style.display = 'none'; // Hide method group
            methodSelect.style.display = 'none';
             // Disable button if no material selected
            simulateButton.disabled = true;
            simulateButton.textContent = 'בחר חומר גלם';
        }
         // Reset result area
         updateAnimationArea('בחר חומר גלם ושיטת מיצוי כדי להתחיל את הקסם...');
         fabricSample.style.backgroundColor = '#e0d8c0'; // Reset color
         colorInfoDiv.style.display = 'none'; // Hide color info
         fabricSample.textContent = ''; // Clear sample text
    });

    // Enable simulate button only when a method is selected
    methodSelect.addEventListener('change', () => {
         const selectedMaterialKey = materialSelect.value;
         const selectedMethodKey = methodSelect.value;
         if (selectedMaterialKey && selectedMethodKey) {
             simulateButton.disabled = false;
             simulateButton.textContent = 'צא למסע הצביעה!';
         } else {
             simulateButton.disabled = true;
              simulateButton.textContent = 'בחר שיטה כדי להמשיך';
         }
         // Reset result area if method changes
          updateAnimationArea('מוכן/ה להתחיל את ההדמיה?');
         fabricSample.style.backgroundColor = '#e0d8c0'; // Reset color
         colorInfoDiv.style.display = 'none'; // Hide color info
          fabricSample.textContent = ''; // Clear sample text
    });


    // Handle simulation
    simulateButton.addEventListener('click', () => {
        const selectedMaterialKey = materialSelect.value;
        const selectedMethodKey = methodSelect.value;

        if (selectedMaterialKey && selectedMethodKey && dyeData[selectedMaterialKey] && dyeData[selectedMaterialKey].methods[selectedMethodKey]) {
            const simulationConfig = dyeData[selectedMaterialKey].methods[selectedMethodKey];
            const steps = simulationConfig.animationSteps;
            const finalColor = simulationConfig.resultColor;
            const colorName = simulationConfig.colorName;

            // Disable controls during simulation
            materialSelect.disabled = true;
            methodSelect.disabled = true;
            simulateButton.disabled = true;
            simulateButton.textContent = 'מעבד...';

            // Reset sample text
             fabricSample.textContent = '';
             fabricSample.style.backgroundColor = '#e0d8c0'; // Reset color
             colorInfoDiv.style.display = 'none';

            let currentStep = 0;
            const intervalTime = 1800; // Time between animation steps (milliseconds)

            function runStep() {
                if (currentStep < steps.length) {
                    const step = steps[currentStep];
                    updateAnimationArea(step.text, step.iconClass);
                    currentStep++;
                    setTimeout(runStep, intervalTime);
                } else {
                    // Final step: show colored fabric
                     updateAnimationArea("התהליך הסתיים!", "icon-finished");
                     fabricSample.style.backgroundColor = finalColor; // Animate color change via CSS transition
                     colorNameSpan.textContent = colorName;
                     colorNameSpan.style.color = finalColor; // Set text color to the dye color
                     colorInfoDiv.style.display = 'block'; // Show color info

                    // Re-enable controls after simulation finishes
                    materialSelect.disabled = false;
                    methodSelect.disabled = false;
                    // Re-check if a method is selected to enable button correctly
                    if (methodSelect.value) {
                         simulateButton.disabled = false;
                         simulateButton.textContent = 'צא למסע הצביעה!';
                     } else {
                          simulateButton.disabled = true;
                          simulateButton.textContent = 'בחר שיטה כדי להמשיך';
                     }
                }
            }

            runStep(); // Start the simulation
        } else {
            updateAnimationArea('שגיאה: אנא בחר/י חומר גלם ושיטת מיצוי תקינים.');
            fabricSample.style.backgroundColor = '#e0d8c0'; // Reset color
             colorInfoDiv.style.display = 'none'; // Hide color info
              // Re-enable controls on error
             materialSelect.disabled = false;
             methodSelect.disabled = false;
             simulateButton.disabled = false;
              simulateButton.textContent = 'צא למסע הצביעה!';
        }
    });

    // Toggle explanation visibility
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר את הסיפור המלא' : 'רוצה לדעת יותר? הצג/הסתר את הסיפור המלא';
        // Scroll to explanation if showing it and not already in view
        if (isHidden) {
            explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });

     // Initial state reset
     fabricSample.style.backgroundColor = '#e0d8c0';
     updateAnimationArea('בחר חומר גלם ושיטת מיצוי כדי להתחיל את הקסם...');
     colorInfoDiv.style.display = 'none';
     simulateButton.textContent = 'בחר חומר גלם'; // Initial button text

</script>