---
title: "סוד הכתמים הכהים על סלעי המדבר: מסע אל ורניש מדברי"
english_slug: mystery-of-dark-spots-on-desert-rocks
category: "מדעי הסביבה / כדור הארץ"
tags: ורניש מדברי, גאולוגיה, מדבר, תהליכי בליה, סלעים
---
# סוד הכתמים הכהים על סלעי המדבר

הביטו על סלעי המדבר. האם שמתם לב לשכבה הכהה, הכמעט מבריקה, המכסה אותם לעיתים? זהו לא סתם לכלוך - זוהי תופעה גאולוגית מרתקת הידועה בשם "ורניש מדברי". איך נוצרת השכבה המסתורית הזו, ומדוע דווקא בנופים הצחיחים ביותר? בואו נצלול עמוק לתעלומה!

<div id="desert-varnish-app" style="direction: rtl; font-family: 'Arial', sans-serif; max-width: 900px; margin: 30px auto; background: linear-gradient(to bottom, #f5e7d3, #e0cfa7); border-radius: 12px; box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2); overflow: hidden;">

    <h2 style="text-align: center; color: #5a3e2b; padding: 20px 0 10px 0; margin-bottom: 20px; border-bottom: 1px solid #d3b99d; text-shadow: 1px 1px 2px rgba(255,255,255,0.5);">סימולציה אינטראקטיבית: היווצרות ורניש מדברי</h2>

    <div style="display: flex; justify-content: center; align-items: center; flex-wrap: wrap; padding: 0 20px 20px 20px;">

        <div id="rock-display-area" style="width: 350px; height: 230px; margin: 0 30px 20px 30px; perspective: 1000px;">
             <div id="rock-simulation" style="width: 100%; height: 100%; background-image: url('https://images.unsplash.com/photo-1530090306639-3c99a9348c48?auto=format&fit=crop&w=350&q=80'); background-size: cover; background-position: center; position: relative; border: 3px solid #4a3526; border-radius: 10px; box-shadow: 0 5px 15px rgba(0,0,0,0.3); transform-style: preserve-3d; animation: rockEntrance 1s ease-out;">
                <div id="dust-overlay" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(210, 180, 140, 0.2); opacity: 0; transition: opacity 0.5s ease; border-radius: 7px;"></div>
                <div id="humidity-overlay" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(70, 130, 180, 0.1); opacity: 0; transition: opacity 0.5s ease; border-radius: 7px;"></div>
                <div id="varnish-layer" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: radial-gradient(circle at 50% 50%, rgba(0,0,0,0) 0%, rgba(0,0,0,0.1) 30%, rgba(30,20,10,0.6) 80%, rgba(30,20,10,0.8) 100%); background-size: 200% 200%; opacity: 0; transition: opacity 0.8s ease, transform 0.8s ease, background-color 0.8s ease; border-radius: 7px; transform: scale(0.95);"></div>
                 <div id="gloss-effect" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: radial-gradient(circle at 70% 30%, rgba(255,255,255,0.6) 0%, rgba(255,255,255,0) 50%); opacity: 0; transition: opacity 0.8s ease; border-radius: 7px;"></div>
             </div>
             <div style="text-align: center; margin-top: 10px; color: #5a3e2b; font-weight: bold;">סלע מדברי</div>
        </div>


        <div id="controls" style="width: 450px; padding: 20px; background-color: rgba(255, 255, 255, 0.6); border-radius: 8px; box-shadow: inset 0 0 10px rgba(0,0,0,0.1);">
            <div class="control-group" style="margin-bottom: 20px; padding-bottom: 15px; border-bottom: 1px dashed #d3b99d;">
                <label for="dust-slider" style="display: block; margin-bottom: 8px; font-weight: bold; color: #333;">כמות אבק (מקור למינרלים):</label>
                <input type="range" id="dust-slider" min="0" max="100" value="50" step="1" class="styled-slider">
                <div style="text-align: center; color: #555; font-size: 0.9em;"><span id="dust-value">50</span>%</div>
            </div>

            <div class="control-group" style="margin-bottom: 20px; padding-bottom: 15px; border-bottom: 1px dashed #d3b99d;">
                <label for="humidity-slider" style="display: block; margin-bottom: 8px; font-weight: bold; color: #333;">רמת לחות (הכרחי לתגובה):</label>
                <input type="range" id="humidity-slider" min="0" max="100" value="50" step="1" class="styled-slider">
                 <div style="text-align: center; color: #555; font-size: 0.9em;"><span id="humidity-value">50</span>%</div>
            </div>

            <div class="control-group" style="margin-bottom: 20px; padding-bottom: 15px; border-bottom: 1px dashed #d3b99d;">
                <label for="microbial-slider" style="display: block; margin-bottom: 8px; font-weight: bold; color: #333;">פעילות מיקרוביאלית (מזרז תהליכים):</label>
                <input type="range" id="microbial-slider" min="0" max="100" value="50" step="1" class="styled-slider">
                 <div style="text-align: center; color: #555; font-size: 0.9em;"><span id="microbial-value">50</span>%</div>
            </div>

            <div class="control-group" style="margin-bottom: 25px;">
                <label for="time-slider" style="display: block; margin-bottom: 8px; font-weight: bold; color: #333;">משך זמן (קנה מידה גאולוגי):</label>
                <input type="range" id="time-slider" min="0" max="50" value="0" step="1" class="styled-slider">
                <div style="text-align: center; color: #555; font-size: 0.9em;"><span id="time-value">0</span> אלפי שנים</div>
            </div>

            <div style="text-align: center;">
                <button id="reset-button" style="padding: 12px 25px; font-size: 1em; cursor: pointer; background-color: #a0522d; color: white; border: none; border-radius: 6px; transition: background-color 0.3s ease, transform 0.1s ease;">איפוס תנאים</button>
            </div>
        </div>
    </div>
</div>

<style>
    /* CSS styles within the <style> tag */
    #desert-varnish-app {
        direction: rtl;
        font-family: 'Arial', sans-serif; /* גופן נפוץ וקריא */
        max-width: 900px;
        margin: 30px auto;
        background: linear-gradient(to bottom, #f5e7d3, #e0cfa7); /* רקע מדברי עדין */
        border-radius: 12px;
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
        overflow: hidden;
        color: #333;
    }

    h1 {
        text-align: center;
        color: #4a3526;
        margin-bottom: 20px;
        font-size: 2em;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
    }

    h2 {
         text-align: center;
         color: #5a3e2b;
         padding: 20px 0 10px 0;
         margin-bottom: 20px;
         border-bottom: 1px solid #d3b99d;
         text-shadow: 1px 1px 2px rgba(255,255,255,0.5);
    }

    p {
        text-align: center;
        margin-bottom: 30px;
        font-size: 1.1em;
        color: #555;
        line-height: 1.6;
        padding: 0 20px; /* הוספת ריפוד לפסקאות מחוץ לאפליקציה */
    }


     #rock-simulation {
        background-image: url('https://images.unsplash.com/photo-1530090306639-3c99a9348c48?auto=format&fit=crop&w=350&q=80'); /* תמונה איכותית יותר לסלע */
        background-size: cover;
        background-position: center;
        position: relative;
        border: 3px solid #4a3526;
        border-radius: 10px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        transform-style: preserve-3d; /* לטרנספורמציות תלת ממדיות אם נרצה בעתיד */
        overflow: hidden; /* לוודא שהשכבות בפנים נשארות בגבולות הסלע */
     }

     @keyframes rockEntrance {
        from { transform: scale(0.8); opacity: 0.5; }
        to { transform: scale(1); opacity: 1; }
     }


    #dust-overlay, #humidity-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border-radius: 7px; /* תואם את פינות הסלע הפנימיות */
        pointer-events: none; /* לא להפריע לאינטראקציות */
    }

    #varnish-layer {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: radial-gradient(circle at 50% 50%, rgba(0,0,0,0) 0%, rgba(0,0,0,0.1) 30%, rgba(30,20,10,0.6) 80%, rgba(30,20,10,0.8) 100%); /* גרדיאנט לכהות מרכזית */
        background-size: 200% 200%; /* כדי שהגרדיאנט ימלא הכל */
        opacity: 0; /* התחל שקוף לגמרי */
        transition: opacity 0.8s ease-out, transform 0.8s ease-out; /* אנימציית הופעה וקנה מידה */
        border-radius: 7px;
        transform: scale(0.95); /* התחל קצת קטן יותר */
        pointer-events: none;
    }

    #gloss-effect {
         position: absolute;
         top: 0;
         left: 0;
         width: 100%;
         height: 100%;
         background: radial-gradient(circle at 70% 30%, rgba(255,255,255,0.6) 0%, rgba(255,255,255,0) 50%); /* אפקט ברק */
         opacity: 0; /* התחל שקוף */
         transition: opacity 0.8s ease-out; /* אנימציית הופעת הברק */
         border-radius: 7px;
         pointer-events: none;
    }


    #controls {
        flex-grow: 1;
        padding: 20px;
        background-color: rgba(255, 255, 255, 0.6); /* רקע חצי שקוף לבקרות */
        border-radius: 8px;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.1);
        min-width: 300px; /* לוודא שהבקרות לא הופכות צרות מדי */
    }

     @media (max-width: 768px) {
        #rock-display-area {
             width: 80%; /* רוחב יחסי במסכים קטנים יותר */
             margin: 0 auto 20px auto; /* ממורכז */
        }
         #controls {
            width: 95%; /* רוחב יחסי */
             margin: 0 auto; /* ממורכז */
             padding: 15px;
        }
         #desert-varnish-app {
            padding: 10px;
         }
     }


    .control-group label {
        font-weight: bold;
        color: #333;
        margin-bottom: 8px;
    }

    .styled-slider {
        -webkit-appearance: none;
        appearance: none;
        width: 100%;
        height: 10px; /* עובי הסליידר */
        background: #d3b99d; /* צבע המסלול */
        outline: none;
        opacity: 0.9;
        transition: opacity .2s ease;
        border-radius: 5px;
        margin: 5px 0;
    }

    .styled-slider:hover {
        opacity: 1;
    }

    /* עיצוב הכפתור (thumb) של הסליידר */
    .styled-slider::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 22px; /* גודל הכפתור */
        height: 22px;
        background: #a0522d; /* צבע הכפתור */
        cursor: pointer;
        border-radius: 50%; /* צורה עגולה */
        border: 2px solid #fff; /* מסגרת לבנה */
        transition: background-color 0.2s ease, transform 0.1s ease;
    }

    .styled-slider::-webkit-slider-thumb:hover {
        background-color: #8b4513; /* צבע כהה יותר בריחוף */
        transform: scale(1.1); /* הגדלה קלה בריחוף */
    }

    .styled-slider::-moz-range-thumb {
        width: 22px;
        height: 22px;
        background: #a0522d;
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #fff;
        transition: background-color 0.2s ease, transform 0.1s ease;
    }

    .styled-slider::-moz-range-thumb:hover {
        background-color: #8b4513;
        transform: scale(1.1);
    }


    #reset-button {
        background-color: #a0522d; /* צבע כפתור האיפוס */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        padding: 12px 25px;
        font-size: 1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

    #reset-button:hover {
        background-color: #8b4513; /* צבע כהה יותר בריחוף */
        transform: translateY(-2px); /* אפקט קפיצה קל */
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
     #reset-button:active {
        transform: translateY(0);
         box-shadow: none;
     }


    #explanation {
        margin-top: 40px;
        padding: 20px;
        background-color: rgba(255, 255, 255, 0.7); /* רקע בהיר וחצי שקוף להסבר */
        border-top: 2px solid #d3b99d;
        border-radius: 0 0 12px 12px; /* פינות מעוגלות רק למטה */
    }

    #explanation h3 {
        color: #a0522d; /* צבע כותרות ההסבר */
        margin-top: 20px;
        margin-bottom: 10px;
        font-size: 1.3em;
    }
    #explanation p {
        text-align: right; /* או justify אם רוצים יישור לשוליים */
        margin-bottom: 15px;
        line-height: 1.7;
        color: #555;
        padding: 0; /* הסרת הריפוד שהוספנו קודם לפסקאות הכלליות */
    }
    #explanation ul {
         list-style: disc inside;
         padding-right: 20px;
         color: #555;
         margin-bottom: 15px;
    }
    #explanation li {
         margin-bottom: 8px;
         line-height: 1.6;
    }

    #toggle-explanation {
        display: block;
        margin: 20px auto;
        padding: 12px 25px;
        font-size: 1em;
        cursor: pointer;
        background-color: #5a3e2b; /* צבע כפתור ההסבר */
        color: white;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
     #toggle-explanation:hover {
        background-color: #4a3526;
        transform: translateY(-2px);
         box-shadow: 0 4px 8px rgba(0,0,0,0.3);
     }
     #toggle-explanation:active {
         transform: translateY(0);
          box-shadow: 0 2px 5px rgba(0,0,0,0.2);
     }

</style>

<button id="toggle-explanation">הצגת המסע אל סוד הכתמים / הסתרת ההסבר</button>

<div id="explanation" style="display: none;">
    <h2>מסע אל סוד הכתמים הכהים: כיצד נוצר ורניש מדברי?</h2>

    <p>השכבה הכהה, המבריקה והמסתורית שפוגשת את עינינו על סלעים בנופים צחיחים היא "ורניש מדברי" (Desert Varnish). זהו אינו ציפוי פשוט, אלא סיפור ארוך ומרתק של אלפי ומליוני שנים, שבו חלקיקי אבק קוסמים יחד עם מים ומיקרואורגניזמים ליצירת יצירת אמנות גאולוגית.</p>

    <h3>המרכיבים הסודיים: אבק, מים וחיים זעירים</h3>
    <p>ורניש מדברי נבנה שכבה אחר שכבה, כמו עוגה גאולוגית איטית במיוחד. המרכיבים העיקריים מגיעים אליו בשלוש דרכים:</p>
    <ul>
        <li><strong>אבק נישא ברוח:</strong> רוחות המדבר מעיפות אבק מרוחק, הנוחת על פני הסלעים. אבק זה עשיר בתחמוצות ברזל ומנגן, שהם שנותנים לורניש את צבעו הכהה.</li>
        <li><strong>רסיסי מים:</strong> למרות שהמדבר יבש, טיפות גשם נדירות, ערפל ואפילו טל בבקרים קרירים מספקים את הלחות החיונית. המים ממיסים את המינרלים באבק ובסלע עצמו.</li>
        <li><strong>מיקרואורגניזמים סבלניים:</strong> חיידקים ואצות זעירים שחיים על פני הסלע משחקים תפקיד מפתח! הם "אוכלים" ומעבדים את תחמוצות המנגן והברזל, מזרזים את תהליך החמצון ו"מדביקים" את חלקיקי החרסית והמינרלים יחד. הם כמו "בנאים" זעירים בבניית הורניש.</li>
    </ul>

    <h3>התהליך האיטי: הצטברות לאורך זמן גאולוגי</h3>
    <p>כאשר האבק נוחת על הסלע הלח, המינרלים המומסים באבק ובסלע עצמו מתחילים לנדוד על פני השטח. החיידקים והאצות פועלים את קסמם, מרכזים את הברזל והמנגן. כשהמים מתאדים, המינרלים שוקעים ומתקשים, יוצרים שכבה מיקרוסקופית דקה. התהליך הזה חוזר על עצמו שוב ושוב לאורך אלפי ואף מיליוני שנים, כשהשכבות החדשות מצטברות על גבי הישנות, יוצרות את הורניש הכהה והמבריק שאנו רואים.</p>
    <p>קצב היווצרות הורניש תלוי ישירות בזמינות האבק, תדירות ומשך הרטיבות, וכמות וסוג המיקרואורגניזמים על הסלע. שינויים באחד מהגורמים הללו לאורך הזמן יכולים לשנות את עובי וצבע הורניש.</p>

    <h3>מראה ייחודי ושימושים מדעיים מפתיעים</h3>
    <p>הגוון הכהה של הורניש (מגוונים של חום אדמדם ועד שחור עמוק) תלוי בעיקר ביחס בין תחמוצות הברזל למנגן, ומושפע גם מהמיקרואורגניזמים הספציפיים. ככל שהורניש כהה ועבה יותר, כך לרוב הוא ותיק יותר.</p>
    <p>העובדה שהורניש מצטבר בקצב איטי וקבוע יחסית לאורך תקופות גאולוגיות ארוכות הופכת אותו לכלי רב עוצמה בידי חוקרים. גאולוגים יכולים לנתח את הרכב וקצב היווצרות הורניש על סלעים שונים באזור כדי להבין מתי נחשפו הסלעים הללו (למשל, בעקבות מפולת או שינוי בתוואי נחל) ובכך לתארך אירועים גאולוגיים בנוף. הוא גם יכול לספק רמזים על תנאי אקלים קדומים (פלאו-קלימטולוגיה).</p>
    <p>אז בפעם הבאה שתראו סלע מדברי עם הכתמים הכהים הללו, זכרו שאתם מסתכלים על ארכיון זמן טבעי, שנבנה באיטיות על ידי רוח, מים ויצורים זעירים, ומספר סיפורים בני אלפי שנים על ההיסטוריה של המדבר.</p>
</div>

<script>
    // JavaScript code within the <script> tag
    const dustSlider = document.getElementById('dust-slider');
    const humiditySlider = document.getElementById('humidity-slider');
    const microbialSlider = document.getElementById('microbial-slider');
    const timeSlider = document.getElementById('time-slider');
    const resetButton = document.getElementById('reset-button');
    const dustValueSpan = document.getElementById('dust-value');
    const humidityValueSpan = document.getElementById('humidity-value');
    const microbialValueSpan = document.getElementById('microbial-value');
    const timeValueSpan = document.getElementById('time-value');
    const varnishLayer = document.getElementById('varnish-layer');
    const glossEffect = document.getElementById('gloss-effect'); // קליטת אלמנט הברק
    const dustOverlay = document.getElementById('dust-overlay'); // קליטת שכבת האבק
    const humidityOverlay = document.getElementById('humidity-overlay'); // קליטת שכבת הלחות

    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');

    let varnishLevel = 0; // Represents the accumulated varnish density, 0 to 100

    function updateSimulation() {
        const dust = parseInt(dustSlider.value);
        const humidity = parseInt(humiditySlider.value);
        const microbes = parseInt(microbialSlider.value);
        const time = parseInt(timeSlider.value); // Time in thousands of years

        dustValueSpan.textContent = dust;
        humidityValueSpan.textContent = humidity;
        microbialValueSpan.textContent = microbes;
        timeValueSpan.textContent = time;

        // --- מתמטיקה משופרת לסימולציה ---
        // קצב ההצטברות תלוי בכל הגורמים. כולם חיוניים.
        // נגדיר קצב בסיסי, ונגדיל אותו בהתאם למחוונים.
        // כדי להפוך את כולם לחיוניים, נשתמש במכפלה, אך נדאג שלא יהיה 0 אם אחד מהם 0.
        // נוסיף ערך מינימלי קטן לכל מחוון כדי למנוע כפל באפס שיקפיא את התהליך.
        const minFactor = 0.1; // ערך מינימלי כדי שהקצב לא יהיה אפס מוחלט
        const dustFactor = (dust / 100) + minFactor;
        const humidityFactor = (humidity / 100) + minFactor;
        const microbialFactor = (microbes / 100) + minFactor;

        // קצב ההצטברות הפוטנציאלי (מושפע מהגורמים, אבל עדיין תלוי בזמן לצבירה)
        const accumulationRatePotential = dustFactor * humidityFactor * microbialFactor;

        // רמת הורניש המצטברת תלויה בקצב הפוטנציאלי ובמשך הזמן.
        // TimeSlider הוא 0-50 (אלפי שנים). נמיר אותו לסקאלה של 0-1 לצורך הכפל.
        const timeFactor = (time / 50); // ייתן ערך בין 0 ל-1

        // רמת הורניש הכוללת היא שילוב של הקצב הפוטנציאלי והזמן.
        // נשתמש בפונקציה לא לינארית קלה כדי לשקף שבהתחלה ההצטברות אולי איטית יותר או מהירה יותר תלוי בתנאים
        // נגדיר מקדם כולל שממתן את הקצב ומבטיח 100% מקסימום ב-50k שנים בתנאים אידיאליים (100% בכל הסליידרים).
        // המקדם יהיה כזה ש- 1.1 * 1.1 * 1.1 * 50 * SCALE_FACTOR = 100
        // בערך: 1.33 * 50 * SCALE_FACTOR = 100 => 66.5 * SCALE_FACTOR = 100 => SCALE_FACTOR ~= 1.5
        const scaleFactor = 1.5; // מקדם התאמה לסקאלה 0-100

        varnishLevel = accumulationRatePotential * timeFactor * scaleFactor * 100; // סקאלה ל-0-100

        // לוודא שהרמה נשארת בטווח 0-100
        varnishLevel = Math.max(0, Math.min(100, varnishLevel));

        // --- עדכון ויזואלי ---
        // שקיפות הורניש: 0 (שקוף) עד 0.9 (כהה מאוד)
        const varnishOpacity = varnishLevel / 100 * 0.9;

        // צבע הורניש: מעבר מחום בהיר/אפור לחום כהה/שחור
        // RGBA: (R, G, B, Alpha)
        // צבע בסיס בהיר: [150, 130, 110]
        // צבע יעד כהה: [30, 20, 10]
        const baseColor = [150, 130, 110];
        const targetColor = [30, 20, 10];
        const interpolatedColor = baseColor.map((start, i) =>
             Math.round(start + (targetColor[i] - start) * (varnishLevel / 100))
        );

        // עדכון ה-background באמצעות RGBA כדי לשלוט גם בצבע וגם בשקיפות
        // נשנה את השקיפות הכללית של השכבה במקום רק את ה-rgba ב-background.
        varnishLayer.style.opacity = varnishOpacity;

        // אפקט ברק: הופך בולט יותר כשהורניש כהה יותר (מעל רמה מסוימת)
        if (varnishLevel > 50) {
             const glossOpacity = (varnishLevel - 50) / 50 * 0.5; // עולה מ-0 ל-0.5 כשעוברים מ-50 ל-100
             glossEffect.style.opacity = glossOpacity;
         } else {
             glossEffect.style.opacity = 0;
         }

         // אנימציות עדינות לשינויים בערכי הסליידרים
         // שכבת אבק: שקיפות לפי כמות האבק
         dustOverlay.style.opacity = dust / 100 * 0.3; // מקסימום שקיפות 0.3

         // שכבת לחות: שקיפות לפי רמת הלחות
         humidityOverlay.style.opacity = humidity / 100 * 0.2; // מקסימום שקיפות 0.2

         // אפקט קנה מידה עדין לורניש כשהוא גדל
         const scale = 0.95 + (varnishLevel / 100) * 0.05; // מ-0.95 ל-1
         varnishLayer.style.transform = `scale(${scale})`;
    }

    function resetSimulation() {
        dustSlider.value = 50;
        humiditySlider.value = 50;
        microbialSlider.value = 50;
        timeSlider.value = 0;
        varnishLevel = 0; // Reset internal level
        updateSimulation(); // Update the display to reflect reset
         // לוודא שהברק והאוברליי מתאפסים גם ויזואלית מיד
        glossEffect.style.opacity = 0;
        dustOverlay.style.opacity = 0;
        humidityOverlay.style.opacity = 0;
        varnishLayer.style.opacity = 0; // וגם שכבת הורניש עצמה
         varnishLayer.style.transform = 'scale(0.95)';
    }

    // Add event listeners
    dustSlider.addEventListener('input', updateSimulation);
    humiditySlider.addEventListener('input', updateSimulation);
    microbialSlider.addEventListener('input', updateSimulation);
    timeSlider.addEventListener('input', updateSimulation); // עדכון מיידי בזמן גרירה
    resetButton.addEventListener('click', resetSimulation);

    // Toggle explanation visibility
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        // הוספת גלילה חלקה לאזור ההסבר אם הוא נפתח
        if (isHidden) {
            explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
        // הטקסט על הכפתור נשאר סטטי כפי שהוגדר ב-HTML כדי למנוע שינויים תוך כדי ריצה.
        // toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מורחב' : 'הצגת המסע אל סוד הכתמים / הסתרת ההסבר';
    });

    // Initial update
    updateSimulation();

    // Animate entrance of the simulation container
    const appContainer = document.getElementById('desert-varnish-app');
    appContainer.style.opacity = 0; // Start hidden for animation
    appContainer.style.transform = 'translateY(20px)';
    window.addEventListener('load', () => {
        setTimeout(() => { // Delay slightly to ensure CSS is parsed
            appContainer.style.transition = 'opacity 0.8s ease-out, transform 0.8s ease-out';
            appContainer.style.opacity = 1;
            appContainer.style.transform = 'translateY(0)';
        }, 100); // Short delay
    });


</script>