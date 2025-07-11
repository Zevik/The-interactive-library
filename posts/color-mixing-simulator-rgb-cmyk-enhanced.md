---
title: "קסם הצבעים: אור (RGB) מול דיו (CMYK) - סימולטור אינטראקטיבי"
english_slug: color-mixing-simulator-rgb-cmyk-enhanced
category: "פיזיקה וטכנולוגיה"
tags: [אינטראקטיבי, סימולציה, צבע, RGB, CMYK, הדמיה, למידה חווייתית]
---
# קסם הצבעים: אור (RGB) מול דיו (CMYK)

פעם חשבתם למה הצבעים על מסך המחשב נראים שונה מהצבעים על דף מודפס? הצטרפו אלינו למסע מרתק אל עולם הצבעים, וגלו את ההבדלים המדהימים בין האופן שבו אור יוצר צבע (RGB) לבין האופן שבו דיו בולע אור וחושף צבע (CMYK). התנסו בסימולטור וגלו את הסודות בעצמכם!

<div class="color-simulator-container">
    <div class="color-simulator">
        <div class="color-section rgb-section">
            <h2>צבעי אור (RGB) <br>מודל חיבור (Additive Color)</h2>
             <p class="section-description">שחקו עם עוצמות האור האדום, הירוק והכחול כדי לראות איך אורות משתלבים ויוצרים מגוון צבעים מסנוור.</p>
            <div class="result-area">
                <div class="mixed-color" id="rgb-result"></div>
                <div class="color-label">הצבע שנוצר מערבוב האורות</div>
            </div>
            <div class="sliders-display">
                <div class="slider-row">
                    <label for="r-slider">אדום (R):</label>
                    <input type="range" id="r-slider" min="0" max="255" value="0">
                    <span id="r-value" class="slider-value">0</span>
                    <div class="color-swatch" id="r-swatch"></div>
                </div>
                <div class="slider-row">
                    <label for="g-slider">ירוק (G):</label>
                    <input type="range" id="g-slider" min="0" max="255" value="0">
                    <span id="g-value" class="slider-value">0</span>
                    <div class="color-swatch" id="g-swatch"></div>
                </div>
                <div class="slider-row">
                    <label for="b-slider">כחול (B):</label>
                    <input type="range" id="b-slider" min="0" max="255" value="0">
                    <span id="b-value" class="slider-value">0</span>
                    <div class="color-swatch" id="b-swatch"></div>
                </div>
            </div>
        </div>

        <div class="color-section cmyk-section">
            <h2>צבעי דפוס (CMYK) <br>מודל חיסור (Subtractive Color)</h2>
            <p class="section-description">ערבבו את צבעי הדיו: ציאן, מג'נטה, צהוב ושחור, וגלו איך הם בולעים אור וחושפים צבעים על משטח לבן.</p>
             <div class="result-area">
                <div class="mixed-color" id="cmyk-result"></div>
                 <div class="color-label">הצבע שנוצר מערבוב הדיו<br>(מוצג במונחי מסך - RGB)</div>
            </div>
            <div class="sliders-display">
                 <div class="slider-row">
                    <label for="c-slider">ציאן (C):</label>
                    <input type="range" id="c-slider" min="0" max="255" value="0">
                    <span id="c-value" class="slider-value">0</span>
                     <div class="color-swatch cmyk-swatch" style="background-color: cyan;"></div>
                </div>
                <div class="slider-row">
                    <label for="m-slider">מג'נטה (M):</label>
                    <input type="range" id="m-slider" min="0" max="255" value="0">
                    <span id="m-value" class="slider-value">0</span>
                     <div class="color-swatch cmyk-swatch" style="background-color: magenta;"></div>
                </div>
                <div class="slider-row">
                    <label for="y-slider">צהוב (Y):</label>
                    <input type="range" id="y-slider" min="0" max="255" value="0">
                    <span id="y-value" class="slider-value">0</span>
                     <div class="color-swatch cmyk-swatch" style="background-color: yellow;"></div>
                </div>
                 <div class="slider-row">
                    <label for="k-slider">שחור (K):</label>
                    <input type="range" id="k-slider" min="0" max="255" value="0">
                    <span id="k-value" class="slider-value">0</span>
                     <div class="color-swatch cmyk-swatch" style="background-color: black;"></div>
                </div>
            </div>
        </div>
    </div>
</div>

<button id="reset-simulator" class="action-button reset-button">אפסו את הסימולטור והתחילו מחדש</button>
<button id="toggle-explanation" class="action-button explanation-button">רוצים להבין את הקסם? לחצו כאן להסבר!</button>


<div id="explanation" class="explanation-hidden">
    <h3>הסבר הקסם: למה צבעי אור ודיו מתנהגים שונה?</h3>
    <p>הצבעים שאנו רואים נוצרים באופן בסיסי בשתי דרכים שונות לחלוטין, התלויות במקור הצבע - האם הוא **פולט אור** (כמו מסך) או **מחזיר/בולע אור** (כמו דיו על נייר).</p>

    <h4>מודל RGB (Red, Green, Blue) - חיבורי (Additive)</h4>
    <ul>
        <li>**איפה פוגשים אותו?** מסכים דיגיטליים (טלפונים, טאבלטים, מחשבים, טלוויזיות), מקרנים, תאורת במה צבעונית. כל מה ש**פולט** אור צבעוני.</li>
        <li>**איך זה עובד?** נקודת המוצא היא **חושך מוחלט** (מסך כבוי - שחור). מוסיפים אורות בצבעים אדום, ירוק וכחול (צבעי יסוד באור). ככל שמוסיפים יותר אור (מעלים את ערכי ה-RGB), הצבע הופך **בהיר יותר**.</li>
        <li>**נקודות ציון:**
            <ul>
                <li>0,0,0 (אין אור כלל) = **שחור**.</li>
                <li>255,0,0 = אדום טהור בעוצמה מקסימלית.</li>
                <li>0,255,0 = ירוק טהור בעוצמה מקסימלית.</li>
                <li>0,0,255 = כחול טהור בעוצמה מקסימלית.</li>
                <li>255,255,0 = צהוב זוהר (אדום + ירוק).</li>
                <li>0,255,255 = ציאן (ירוק + כחול).</li>
                <li>255,0,255 = מג'נטה (אדום + כחול).</li>
                <li>255,255,255 (אור מקסימלי מכל הערוצים) = **לבן זוהר**.</li>
            </ul>
        </li>
        <li>**העיקרון:** ערבוב צבעי אור הוא כמו הוספת עוד אור לחדר חשוך - הופך את הכל לבהיר יותר.</li>
    </ul>

    <h4>מודל CMYK (Cyan, Magenta, Yellow, Key/Black) - חיסורי (Subtractive)</h4>
    <ul>
        <li>**איפה פוגשים אותו?** הדפסה על נייר, צבעי ציור, צבעי קיר. כל מה ש**בולע** אור ומחזיר את השאר.</li>
        <li>**איך זה עובד?** נקודת המוצא היא **משטח לבן** (כמו נייר) שמחזיר את כל האור שמגיע אליו. הדיו הצבעוני שאנו מורחים על הנייר **בולע** חלק מהאור ומחזיר רק את השאר. זהו תהליך "חיסור" - הדיו "מחַסֵר" (בולם) אורכי גל מסוימים מהאור הפוגע.</li>
        <li>**צבעי היסוד בדיו:** ציאן (C), מג'נטה (M), וצהוב (Y). תיאורטית, ערבוב מלא של C, M, Y אמור לבלוע את כל האור ולהיראות שחור. בפועל, בגלל אי-טוהר של פיגמנטים בדיו, לרוב מתקבל חום כהה ועכור. לכן מוסיפים דיו שחור (K - Key, שמייצג את הצבע ה"עיקרי" או "מפתח" בדפוס) כדי ליצור שחור עשיר ועמוק יותר וגם לחסוך שימוש יקר בדיו צבעוני ליצירת שחור.</li>
        <li>**נקודות ציון:**
            <ul>
                <li>0,0,0,0 (אין דיו כלל) = **לבן** (צבע המשטח).</li>
                <li>255,0,0,0 (ציאן מקסימלי) = בולע אדום, מחזיר ירוק וכחול => נראה ציאן.</li>
                <li>0,255,0,0 (מג'נטה מקסימלי) = בולע ירוק, מחזיר אדום וכחול => נראה מג'נטה.</li>
                <li>0,0,255,0 (צהוב מקסימלי) = בולע כחול, מחזיר אדום וירוק => נראה צהוב.</li>
                <li>255,255,0,0 (ציאן + מג'נטה) = בולע אדום וירוק, מחזיר כחול => נראה כחול (כחול כהה יותר מכחול ב-RGB).</li>
                <li>0,255,255,0 (מג'נטה + צהוב) = בולע ירוק וכחול, מחזיר אדום => נראה אדום (אדום כהה יותר מאדום ב-RGB).</li>
                <li>255,0,255,0 (ציאן + צהוב) = בולע אדום וכחול, מחזיר ירוק => נראה ירוק (ירוק כהה יותר מירוק ב-RGB).</li>
                <li>255,255,255,0 (C+M+Y ללא K) = בולע כמעט הכל => נראה חום כהה/שחור עכור.</li>
                <li>0,0,0,255 (שחור מקסימלי) = בולע כמעט הכל => נראה שחור.</li>
                <li>255,255,255,255 (C+M+Y+K מקסימליים) = בולע את מירב האור => **שחור הכי עמוק שאפשר להשיג בדפוס**.</li>
            </ul>
        </li>
         <li>**העיקרון:** ערבוב צבעי דיו הוא כמו הוספת עוד שכבות שבולעות אור על דף לבן - הופך את הצבע לכהה יותר.</li>
    </ul>
    <p>הסימולטור הזה מאפשר לכם להתנסות באופן ויזואלי בשני העקרונות הללו. שימו לב איך במודל RGB, הוספת צבעים מבהירה את התוצאה לכיוון הלבן, בעוד שבמודל CMYK, הוספת דיו מכהה את התוצאה לכיוון השחור. זהו ההבדל המהותי בין עבודה עם אור פולט לאור מוחזר!</p>
</div>

<style>
    :root {
        --primary-color: #4a90e2; /* A friendly blue */
        --secondary-color: #50e3c2; /* A complementary turquoise */
        --background-light: #f0f4f8; /* Soft, light background */
        --card-background: #ffffff;
        --text-color: #333; /* Darker text for readability */
        --border-color: #d8dce6; /* Soft border */
        --shadow-light: rgba(0, 0, 0, 0.1);
        --animation-duration: 0.4s; /* Slightly longer for smoother feel */
        --hover-scale: 1.02; /* Slight scale on hover */
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: var(--text-color);
        background-color: var(--background-light);
        margin: 0;
        padding: 20px;
        direction: rtl; /* Right-to-left for Hebrew */
        text-align: right;
        overflow-x: hidden; /* Prevent horizontal scroll */
    }

    h1, h2, h3, h4 {
        color: var(--primary-color);
        text-align: center;
        margin-bottom: 20px;
    }

    h1 {
        font-size: 2.5em;
        margin-top: 10px;
        margin-bottom: 30px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.05);
    }

    h2 {
        font-size: 1.8em;
        margin-top: 0;
        margin-bottom: 15px;
        color: var(--text-color); /* Match text color for section titles */
    }

    h3 {
        font-size: 1.6em;
        margin-top: 20px;
        margin-bottom: 15px;
        text-align: right;
    }

     h4 {
        font-size: 1.3em;
        margin-top: 15px;
        margin-bottom: 10px;
        text-align: right;
        color: var(--secondary-color);
     }

    p {
        margin-bottom: 15px;
        max-width: 900px;
        margin-left: auto;
        margin-right: auto;
        text-align: center;
    }

    p.section-description {
        font-size: 0.95em;
        color: var(--secondary-color);
        margin-top: -10px;
        margin-bottom: 25px;
        text-align: center;
        max-width: none; /* Allow description full width in card */
    }

    .color-simulator-container {
        display: flex;
        justify-content: center;
        margin-bottom: 30px;
        padding: 0 10px; /* Add padding for smaller screens */
    }

    .color-simulator {
        display: flex;
        flex-wrap: wrap;
        gap: 30px;
        width: 100%;
        max-width: 1000px;
    }

    .color-section {
        background-color: var(--card-background);
        border: 1px solid var(--border-color);
        border-radius: 12px; /* More rounded corners */
        padding: 30px 20px; /* More vertical padding */
        box-shadow: 0 8px 16px var(--shadow-light); /* Stronger shadow */
        flex: 1;
        min-width: 320px; /* Slightly increased min width */
        display: flex;
        flex-direction: column;
        align-items: center;
        transition: transform var(--animation-duration) ease; /* Add transform transition */
    }

    .color-section:hover {
         transform: translateY(-5px); /* Subtle lift on hover */
    }


    .result-area {
        margin-bottom: 30px; /* More space below result */
        text-align: center;
    }

    .mixed-color {
        width: 180px; /* Larger circle */
        height: 180px; /* Larger circle */
        border-radius: 50%;
        margin: 0 auto 12px; /* More space below circle */
        border: 4px solid var(--secondary-color); /* More prominent border */
        box-shadow: inset 0 0 15px rgba(0,0,0,0.1); /* Subtle inner shadow */
        transition: background-color var(--animation-duration) ease, transform 0.1s ease; /* Smooth color change & quick pulse */
        cursor: pointer; /* Indicate interactivity */
    }

     .mixed-color:active {
         transform: scale(0.98); /* Quick press effect */
     }


    .color-label {
        font-size: 1em; /* Slightly larger label */
        color: var(--secondary-color);
        font-weight: bold;
    }

    .sliders-display {
        width: 100%;
        max-width: 400px; /* Limit slider area width for better alignment */
    }

    .slider-row {
        display: flex;
        align-items: center;
        margin-bottom: 20px; /* More space between rows */
        gap: 15px; /* Increased space between items */
    }

    .slider-row label {
        flex-basis: 80px;
        text-align: right; /* Align labels to the right */
        font-weight: bold;
        min-width: 60px;
        color: var(--text-color);
    }

     .slider-row input[type="range"] {
        flex-grow: 1;
        -webkit-appearance: none;
        appearance: none;
        height: 10px; /* Thicker slider track */
        background: var(--border-color);
        border-radius: 5px;
        outline: none;
        opacity: 0.9; /* Less opaque */
        transition: opacity var(--animation-duration), transform 0.1s ease;
        cursor: grab;
    }

     .slider-row input[type="range"]:hover {
        opacity: 1;
        transform: scaleY(1.1); /* Subtle scale effect on hover */
    }

     .slider-row input[type="range"]:active {
        cursor: grabbing;
     }


    .slider-row input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 24px; /* Larger thumb */
        height: 24px; /* Larger thumb */
        background: var(--primary-color);
        border-radius: 50%;
        cursor: grab;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2); /* More prominent thumb shadow */
        transition: background-color 0.2s ease, transform 0.1s ease;
    }

    .slider-row input[type="range"]::-webkit-slider-thumb:active {
        transform: scale(1.1); /* Press effect on thumb */
        cursor: grabbing;
    }


    .slider-row input[type="range"]::-moz-range-thumb {
        width: 24px; /* Larger thumb */
        height: 24px; /* Larger thumb */
        background: var(--primary-color);
        border-radius: 50%;
        cursor: grab;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2); /* More prominent thumb shadow */
         transition: background-color 0.2s ease, transform 0.1s ease;
    }
    .slider-row input[type="range"]::-moz-range-thumb:active {
        transform: scale(1.1); /* Press effect on thumb */
         cursor: grabbing;
    }

    /* Specific thumb colors for RGB sliders */
    #r-slider::-webkit-slider-thumb { background: #ff4d4d; } /* Red */
    #g-slider::-webkit-slider-thumb { background: #4dff4d; } /* Green */
    #b-slider::-webkit-slider-thumb { background: #4d4dff; } /* Blue */
    #r-slider::-moz-range-thumb { background: #ff4d4d; } /* Red */
    #g-slider::-moz-range-thumb { background: #4dff4d; } /* Green */
    #b-slider::-moz-range-thumb { background: #4d4dff; } /* Blue */

     /* Specific thumb colors for CMYK sliders */
    #c-slider::-webkit-slider-thumb { background: cyan; }
    #m-slider::-webkit-slider-thumb { background: magenta; }
    #y-slider::-webkit-slider-thumb { background: yellow; }
    #k-slider::-webkit-slider-thumb { background: black; border: 1px solid #fff; } /* White border for black thumb */
    #c-slider::-moz-range-thumb { background: cyan; }
    #m-slider::-moz-range-thumb { background: magenta; }
    #y-slider::-moz-range-thumb { background: yellow; }
    #k-slider::-moz-range-thumb { background: black; border: 1px solid #fff; } /* White border for black thumb */


    .slider-value {
        flex-basis: 40px; /* Wider value span */
        text-align: center;
        font-size: 1em; /* Slightly larger value */
        color: var(--text-color);
        font-weight: bold;
         min-width: 40px;
    }

    .color-swatch {
        width: 30px; /* Larger swatch */
        height: 30px; /* Larger swatch */
        border-radius: 6px; /* More rounded swatch */
        border: 2px solid var(--border-color); /* More prominent border */
         box-sizing: border-box;
         transition: transform 0.1s ease;
         cursor: help; /* Indicate it shows the component color */
    }

    .color-swatch:active {
        transform: scale(0.9); /* Press effect */
    }

    .cmyk-swatch {
         border: 2px solid #333; /* Darker border for CMYK swatches */
    }


    /* Specific swatch colors (dynamic for RGB handled by JS, static for CMYK inline) */
    /* Initial styles are placeholders, JS updates them */
    #r-swatch { background-color: rgb(0, 0, 0); }
    #g-swatch { background-color: rgb(0, 0, 0); }
    #b-swatch { background-color: rgb(0, 0, 0); }


    .action-button {
        display: block;
        margin: 15px auto; /* Center buttons and add space */
        padding: 12px 25px; /* More padding */
        font-size: 1.1em; /* Larger font */
        color: white;
        background-color: var(--primary-color);
        border: none;
        border-radius: 6px; /* More rounded buttons */
        cursor: pointer;
        transition: background-color var(--animation-duration) ease, transform 0.1s ease, box-shadow var(--animation-duration) ease;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        font-weight: bold;
    }

    .action-button:hover {
        background-color: #3a7bcc; /* Darker shade on hover */
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }

     .action-button:active {
         transform: scale(0.98); /* Press effect */
         box-shadow: 0 2px 4px rgba(0,0,0,0.1);
     }

     .reset-button {
         background-color: var(--secondary-color); /* Different color for reset */
     }
    .reset-button:hover {
         background-color: #40c9b0;
    }


    .explanation-hidden {
        display: none;
        background-color: var(--card-background);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 30px 20px;
        box-shadow: 0 8px 16px var(--shadow-light);
        margin-top: 30px;
        max-width: 1000px;
        margin-left: auto;
        margin-right: auto;
        opacity: 0;
        transition: opacity var(--animation-duration) ease;
    }

    .explanation-visible {
        display: block;
        opacity: 1;
    }

     .explanation-hidden ul {
        padding-right: 25px; /* More padding for list */
        margin-bottom: 15px;
     }

     .explanation-hidden li {
         margin-bottom: 10px;
         line-height: 1.5;
         color: var(--text-color);
     }

     .explanation-hidden li ul {
        margin-top: 8px;
        margin-bottom: 8px;
        padding-right: 15px;
        font-size: 0.95em;
        color: #555;
     }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        h1 { font-size: 2em; }
        h2 { font-size: 1.6em; }
        p { text-align: right; } /* Align intro text right on small screens */
        p.section-description { text-align: center;} /* Keep description centered */

        .color-simulator {
            flex-direction: column;
            align-items: center;
            gap: 20px; /* Smaller gap when stacked */
        }

        .color-section {
             width: 100%;
             min-width: auto; /* Remove min-width on small screens */
             padding: 20px 15px;
        }

        .result-area .mixed-color {
             width: 120px; /* Smaller circle on mobile */
             height: 120px; /* Smaller circle on mobile */
             margin-bottom: 8px;
             border-width: 3px;
         }

         .color-label {
             font-size: 0.9em;
         }

         .sliders-display {
             max-width: none; /* Allow full width for sliders on mobile */
         }

         .slider-row {
             flex-direction: column; /* Stack label, slider, value/swatch */
             align-items: flex-start;
             gap: 8px; /* Smaller gap in stacked row */
             margin-bottom: 18px;
         }

         .slider-row label {
             width: 100%; /* Label takes full width */
             text-align: right;
             flex-basis: auto; /* Remove fixed basis */
         }

          .slider-row input[type="range"] {
             width: 100%; /* Slider takes full width */
             flex-grow: 0; /* Don't need flex-grow when width is 100% */
          }

          .slider-value {
              width: auto; /* Value width fits content */
              text-align: right;
              font-size: 0.9em;
              min-width: auto;
              flex-basis: auto;
          }

           .color-swatch {
               width: 25px; /* Smaller swatch */
               height: 25px; /* Smaller swatch */
               border-width: 1px;
               border-radius: 4px;
           }

           /* Arrange value and swatch side-by-side below slider */
           .slider-row::after { /* Use a pseudo-element to create a row */
               content: '';
               display: table;
               clear: both;
           }
            .slider-row > label,
            .slider-row > input[type="range"] {
                float: right; /* Float elements to clear */
                clear: right;
            }

           .slider-row > .slider-value {
               float: right;
               margin-right: 5px; /* Space between value and swatch */
                line-height: 25px; /* Align text vertically with swatch */
           }
            .slider-row > .color-swatch {
                float: right;
            }

        .action-button {
            font-size: 1em;
            padding: 10px 20px;
            margin: 10px auto;
        }

        .explanation-hidden {
            padding: 20px 15px;
        }

        .explanation-hidden ul {
            padding-right: 15px;
        }

        .explanation-hidden li ul {
            padding-right: 10px;
        }

    }


</style>

<script>
    // RGB Elements
    const rSlider = document.getElementById('r-slider');
    const gSlider = document.getElementById('g-slider');
    const bSlider = document.getElementById('b-slider');
    const rValue = document.getElementById('r-value');
    const gValue = document.getElementById('g-value');
    const bValue = document.getElementById('b-value');
    const rSwatch = document.getElementById('r-swatch');
    const gSwatch = document.getElementById('g-swatch');
    const bSwatch = document.getElementById('b-swatch');
    const rgbResult = document.getElementById('rgb-result');

    // CMYK Elements
    const cSlider = document.getElementById('c-slider');
    const mSlider = document.getElementById('m-slider');
    const ySlider = document.getElementById('y-slider');
    const kSlider = document.getElementById('k-slider');
    const cValue = document.getElementById('c-value');
    const mValue = document.getElementById('m-value');
    const yValue = document.getElementById('y-value');
    const kValue = document.getElementById('k-value');
    const cmykResult = document.getElementById('cmyk-result');

    // Control Elements
    const toggleButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const resetButton = document.getElementById('reset-simulator');

    function updateRgbDisplay() {
        const r = parseInt(rSlider.value);
        const g = parseInt(gSlider.value);
        const b = parseInt(bSlider.value);

        rValue.textContent = r;
        gValue.textContent = g;
        bValue.textContent = b;

        // Update individual swatches showing component intensity
        rSwatch.style.backgroundColor = `rgb(${r}, 0, 0)`;
        gSwatch.style.backgroundColor = `rgb(0, ${g}, 0)`;
        bSwatch.style.backgroundColor = `rgb(0, 0, ${b})`;

        // Update mixed result with smooth transition
        rgbResult.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;

         // Add a subtle pulse animation trigger (optional, can be done with CSS classes)
         // rgbResult.classList.remove('pulse'); // Reset animation
         // void rgbResult.offsetWidth; // Trigger reflow
         // rgbResult.classList.add('pulse'); // Re-add animation
    }

    function updateCmykDisplay() {
        const c = parseInt(cSlider.value);
        const m = parseInt(mSlider.value);
        const y = parseInt(ySlider.value);
        const k = parseInt(kSlider.value);

        cValue.textContent = c;
        mValue.textContent = m;
        yValue.textContent = y;
        kValue.textContent = k;

        // CMYK to RGB conversion for display
        // Normalize values from 0-255 to 0-1
        const cNorm = c / 255;
        const mNorm = m / 255;
        const yNorm = y / 255;
        const kNorm = k / 255;

        // Convert CMYK (0-1) to RGB (0-255) using a common formula
        // C = 1 - R/255, M = 1 - G/255, Y = 1 - B/255, K = 1 - max(R/255, G/255, B/255)
        // Reverse: R = 255 * (1-C) * (1-K), G = 255 * (1-M) * (1-K), B = 255 * (1-Y) * (1-K)
        // This is a better approximation than the simple C+K sum for display purposes
        let r = 255 * (1 - cNorm) * (1 - kNorm);
        let g = 255 * (1 - mNorm) * (1 - kNorm);
        let b = 255 * (1 - yNorm) * (1 - kNorm);


        // Ensure values are within 0-255 and round
        r = Math.round(Math.max(0, Math.min(255, r)));
        g = Math.round(Math.max(0, Math.min(255, g)));
        b = Math.round(Math.max(0, Math.min(255, b)));

        // Update mixed result with smooth transition
        cmykResult.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;

         // Add a subtle pulse animation trigger (optional)
         // cmykResult.classList.remove('pulse'); // Reset animation
         // void cmykResult.offsetWidth; // Trigger reflow
         // cmykResult.classList.add('pulse'); // Re-add animation
    }

    function toggleExplanation() {
        // Use classes for smooth transition (CSS handles opacity)
        const isHidden = explanationDiv.classList.contains('explanation-hidden');
        if (isHidden) {
            explanationDiv.classList.remove('explanation-hidden');
            // Force display block immediately so transition works
            explanationDiv.style.display = 'block';
             // Use setTimeout to allow display:block to register before starting opacity transition
             setTimeout(() => {
                explanationDiv.classList.add('explanation-visible');
             }, 10); // Small delay
            toggleButton.textContent = 'הסתירו את ההסבר';
        } else {
            explanationDiv.classList.remove('explanation-visible');
            // Wait for transition to finish before setting display: none
            explanationDiv.addEventListener('transitionend', function handler() {
                explanationDiv.style.display = 'none';
                explanationDiv.classList.add('explanation-hidden');
                explanationDiv.removeEventListener('transitionend', handler);
            });
            toggleButton.textContent = 'רוצים להבין את הקסם? לחצו כאן להסבר!';
        }
    }

    function resetSimulator() {
        // Reset RGB sliders
        rSlider.value = 0;
        gSlider.value = 0;
        bSlider.value = 0;
        updateRgbDisplay();

        // Reset CMYK sliders
        cSlider.value = 0;
        mSlider.value = 0;
        ySlider.value = 0;
        kSlider.value = 0;
        updateCmykDisplay();
    }


    // Add event listeners
    rSlider.addEventListener('input', updateRgbDisplay);
    gSlider.addEventListener('input', updateRgbDisplay);
    bSlider.addEventListener('input', updateRgbDisplay);

    cSlider.addEventListener('input', updateCmykDisplay);
    mSlider.addEventListener('input', updateCmykDisplay);
    ySlider.addEventListener('input', updateCmykDisplay);
    kSlider.addEventListener('input', updateCmykDisplay);

    toggleButton.addEventListener('click', toggleExplanation);
    resetButton.addEventListener('click', resetSimulator);


    // Initial update on page load
    // Set initial state (sliders at 0, results black/white)
    updateRgbDisplay();
    updateCmykDisplay();

    // Optional: Set more interesting initial values on load if desired
    // rSlider.value = 200; gSlider.value = 50; bSlider.value = 150; updateRgbDisplay();
    // cSlider.value = 50; mSlider.value = 150; ySlider.value = 100; kSlider.value = 50; updateCmykDisplay();


</script>