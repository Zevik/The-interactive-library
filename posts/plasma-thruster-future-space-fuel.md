---
title: "מנוע פלזמה: הדלק העתידי של חקר החלל?"
english_slug: plasma-thruster-future-space-fuel
category: "מדעים מדויקים / פיזיקה"
tags:
  - פיזיקה
  - הנעה בחלל
  - מנוע פלזמה
  - חלל
  - יונים
  - מנוע_הול
---
<h1>מנוע פלזמה: הדלק העתידי של חקר החלל?</h1>
<p>דמיינו מנוע שמשתמש בכמות זעירה של דלק כדי להאיץ חללית למהירויות אדירות לאורך חודשים ושנים. זה לא מדע בדיוני - זו המציאות של מנועי הפלזמה! במקום לפלוט גז שרוף לוהט כמו רקטות כימיות, הם רותמים את הכוח העוצמתי של חלקיקים טעונים ואת עקרונות החשמל והמגנטיות. בואו לצלול לתוך הליבה של הטכנולוגיה המרתקת הזו בסימולציה אינטראקטיבית.</p>

<div id="app-container">
    <h2>סימולציית מנוע הול: רתמו את הפלזמה!</h2>
    <p>שנו את הפרמטרים וצפו כיצד הם משפיעים על זרימת הפלזמה והדחף שנוצר.</p>
    <div id="thruster-controls">
        <div class="control-group">
            <label for="fuel-flow">זרימת גז קסנון (דלק):</label>
            <input type="range" id="fuel-flow" min="0.5" max="3.0" value="1.5" step="0.1">
            <span id="fuel-flow-value">1.5</span> יחידות
        </div>
        <div class="control-group">
            <label for="electric-field">שדה מאיץ (מתח פריקה):</label>
            <input type="range" id="electric-field" min="150" max="700" value="400" step="20">
            <span id="electric-field-value">400</span> V
        </div>
        <div class="control-group">
            <label for="magnetic-field">שדה מגנטי (לכליאת אלקטרונים):</label>
            <input type="range" id="magnetic-field" min="0.8" max="4.0" value="2.0" step="0.1">
            <span id="magnetic-field-value">2.0</span> יחידות
        </div>
    </div>

    <div id="thruster-visualization">
        <canvas id="thruster-canvas"></canvas>
        <div id="thruster-outputs">
            <p>✨ <strong>דחף (Thrust):</strong> <span id="thrust-output"></span></p>
            <p>🚀 <strong>מומנטום סגולי (יעילות - Isp):</strong> <span id="efficiency-output"></span></p>
            <p>💡 <strong>צריכת הספק:</strong> <span id="power-output"></span></p>
        </div>
         <div id="visualization-legend">
            <span><span class="legend-color" style="background-color: grey;"></span> גז ניטרלי</span>
            <span><span class="legend-color" style="background-color: #00aaff;"></span> יונים (מואצים!)</span>
            <span><span class="legend-color" style="background-color: #ffdd00;"></span> אלקטרונים (כלואים)</span>
        </div>
    </div>
    <p class="output-note">הערכים המוצגים בסימולציה הינם יחסיים ונועדו להמחיש את השפעת הפרמטרים על ביצועי המנוע העקרוניים.</p>
</div>

<button id="toggle-explanation">רוצים לדעת עוד? לחצו להסבר מעמיק!</button>

<div id="explanation" class="hidden">
    <h2>הסבר מעמיק: מנועי פלזמה</h2>

    <h3>מהו מנוע פלזמה ולמה הוא שונה כל כך מרקטות כימיות?</h3>
    <p>תחשבו על רקטה כימית כעל "מפץ" אדיר לזמן קצר - שריפת דלק מהירה ליצירת דחף עצום שמצריך טונות של דלק. מנוע פלזמה הוא יותר כמו "דחיפה" עדינה ואינסופית - הוא מאיץ כמות קטנה של חלקיקים טעונים (פלזמה) למהירויות מטורפות באמצעות שדות חשמליים ומגנטיים. הדחף הרגעי נמוך מאוד (לא מספיק כדי להמריא מכדור הארץ!), אבל הוא יכול לפעול במשך שנים! זה כמו ההבדל בין ספרינט למרתון - רק שבחלל, המרתון הוא המפתח להגיע רחוק באמת וביעילות דלק חסרת תקדים.</p>

    <h3>פלזמה - מצב הצבירה המסתורי הרביעי</h3>
    <p>אם חימום הופך מוצק לנוזל ונוזל לגז, אז מה קורה כשמחממים גז עוד יותר או מפעילים עליו חשמל חזק? האטומים מתפרקים! האלקטרונים ניתקים מהגרעינים, ונוצרת תערובת של יונים טעונים חיובית ואלקטרונים חופשיים טעונים שלילית. זוהי פלזמה - מצב צבירה שמתנהג באופן שונה לחלוטין מגז רגיל, במיוחד כשהוא פוגש שדות חשמליים ומגנטיים. השמש, כוכבים וברקים הם דוגמאות לפלזמה טבעית.</p>

    <h3>עקרון הפעולה הבסיסי: מהדלק לפלזמה, ומהפלזמה לדחף!</h3>
    <p>ההיגיון פשוט: לזרוק משהו אחורה במהירות אדירה כדי להתקדם קדימה. איך מנוע פלזמה עושה את זה?
    <ol>
        <li><strong>כניסת דלק:</strong> בדרך כלל גז אציל כמו קסנון - כבד ויציב כימית. הוא מוזרם לתוך תא מיוחד במנוע.</li>
        <li><strong>יינון (קסם הפלזמה):</strong> אנרגיה (מחשמל, גלי רדיו וכו') ניתנת לגז. האלקטרונים עפים מהאטומים. הופכים את הגז לפלזמה לוהטת של יונים ואלקטרונים.</li>
        <li><strong>האצה (הדחיפה הגדולה):</strong> כאן נכנסים לתמונה השדות החשמליים והמגנטיים. הם מכוונים ומאיצים את החלקיקים הטעונים (בעיקר את היונים החיוביים) החוצה מהמנוע במהירות מסחררת. במנועי הול, שדה מגנטי "לוכד" את האלקטרונים ומאלץ אותם לנוע במסלול מעגלי, מה שיוצר שדה חשמלי חזק שמאיץ את היונים.</li>
        <li><strong>נטרול (פליטה נקייה):</strong> כדי שהחללית לא תיטען שלילית ותמשוך אליה בחזרה את סילון היונים, מוזרמים אלקטרונים גם לחלק החיצוני של הסילון.</li>
    </ol>
    סילון הפלזמה שפורץ החוצה יוצר את הדחף הדרוש לדחיפת החללית קדימה!</p>

    <h3>מנועי פלזמה נפוצים: לא כולם זהים</h3>
    <ul>
        <li><strong>מנועי יונים עם רשתות (Gridded Ion Thrusters):</strong> משתמשים ברשתות מתכת טעונות במתח גבוה כדי למשוך ולהאיץ יונים. יעילים מאוד, אבל הרשתות יכולות להישחק.</li>
        <li><strong>מנועי הול (Hall Thrusters):</strong> הסוג הנפוץ ביותר בלוויינים מסחריים. משתמשים בשילוב גאוני של שדה חשמלי ואלקטרונים הכלואים בשדה מגנטי ליצירת אזור האצה קומפקטי.</li>
        <li><strong>מנועי פלזמה בתדר רדיו/מיקרוגל (RF/Microwave Plasma Thrusters):</strong> משתמשים בגלי רדיו או מיקרוגל ליצירת הפלזמה, ומאיצים אותה בשיטות שונות. פוטנציאל פחות בלאי.</li>
    </ul>

    <h3>הקשר המרתק בין חשמל ומגנטיות</h3>
    <p>שדה חשמלי דוחף חלקיקים טעונים (חיובי בכיוון השדה, שלילי נגד כיוון השדה). שדה מגנטי לא משנה את מהירות החלקיקים, אבל הוא משנה את כיוונם, ומכופף את המסלול שלהם. במנוע הול, השדה המגנטי הרדיאלי מאט דרמטית את האלקטרונים מלהגיע לקצה המנוע. כשהאלקטרונים הלכודים נעים במעגלים, הם יוצרים אזור של מטען שלילי שבתורו יוצר שדה חשמלי חזק מאוד לאורך המנוע. השדה החשמלי הזה הוא זה שדוחף ומאיץ את היונים החיוביים במהירות אדירה החוצה.</p>

    <h3>יתרונות מול אתגרים</h3>
    <ul>
        <li><strong>הכוחות החזקים:</strong>
            <ul>
                <li><strong>יעילות דלק אגדית (Isp גבוה):</strong> מאפשר למשימות חלל להגיע הרבה יותר רחוק עם הרבה פחות דלק. חוסך מיליוני דולרים במסה!</li>
                <li><strong>עבודה לטווח ארוך:</strong> חודשים ושנים של פעולה רציפה, מושלם למסעות ארוכים בחלל העמוק.</li>
            </ul>
        </li>
        <li><strong>הנקודות הפחות זוהרות:</strong>
            <ul>
                <li><strong>דחף נמוך:</strong> לא מתאים לשיגור מכדור הארץ. רק לתמרונים בחלל.</li>
                <li><strong>דורש הרבה חשמל:</strong> צריך מערכות סולאריות גדולות או כוח גרעיני כדי להפעיל אותם בעוצמה.</li>
                <li><strong>מורכבות:</strong> המערכות כוללות אלקטרוניקה עדינה ורכיבי פלזמה.</li>
            </ul>
        </li>
    </ul>

    <h3>איפה פוגשים מנועי פלזמה?</h3>
    <ul>
        <li><strong>לווייני תקשורת:</strong> תיקון מסלול ו"שמירה על תחנה" במסלול גיאוסטציונרי.</li>
        <li><strong>שינוי מסלול והגעה ליעד:</strong> לוויינים רבים עולים למסלול המבצעי שלהם לאט וביעילות באמצעותם.</li>
        <li><strong>גשושיות חלל עמוק:</strong> מסעות לכוכבי לכת רחוקים, אסטרואידים ושביטים (כמו הגשושית Dawn שחקרה וסטה וקרס).</li>
    </ul>

    <h3>לאן הלאה? עתיד ההנעה החשמלית</h3>
    <p>המחקר ממשיך במרץ! המטרה: להגדיל את הדחף (אולי למשימות מאוישות?), לשפר את היעילות אפילו יותר, לפתח מנועים קטנים וחסכוניים ללוויינים זעירים (קיובסאטים), להשתמש בדלקים זולים וזמינים יותר (יוד נשמע מסקרן!), ולהאריך את חיי המנועים עוד ועוד. טכנולוגיות חדשות ומלהיבות נמצאות בפיתוח.</p>
</div>

<style>
    /* כללי */
    #app-container {
        font-family: 'Heebo', sans-serif; /* שימוש בפונט מודרני יותר */
        background: linear-gradient(135deg, #e0eafc, #cfdef3); /* רקע גרדיאנט עדין */
        border: none; /* הסרת גבול ישן */
        padding: 30px;
        margin: 20px auto;
        border-radius: 12px; /* פינות מעוגלות יותר */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* צל עדין */
        max-width: 800px; /* רוחב מקסימלי */
        text-align: center;
    }

     #app-container h2 {
         color: #003366; /* צבע כהה לכותרות */
         margin-bottom: 15px;
         font-size: 1.8em;
         text-shadow: 1px 1px 2px rgba(0,0,0,0.05);
     }

    #app-container p {
        color: #333;
        margin-bottom: 20px;
        line-height: 1.6;
    }


    /* פקדים */
    #thruster-controls {
        margin-top: 20px;
        margin-bottom: 40px;
        display: grid; /* שימוש ב-grid לסידור נוח */
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); /* עמודות שמתאימות את עצמן */
        gap: 25px; /* מרווחים בין הפקדים */
        justify-items: center; /* מרכז את התוכן בכל תא */
    }

    .control-group {
        display: flex;
        flex-direction: column;
        align-items: flex-start; /* יישור לשמאל */
        width: 100%; /* רוחב מקסימלי בתא הגריד */
        max-width: 250px; /* רוחב מוגבל */
        background-color: rgba(255, 255, 255, 0.7); /* רקע שקוף למחצה */
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
        text-align: left;
    }

    .control-group label {
        margin-bottom: 8px;
        font-weight: bold;
        font-size: 1em; /* גודל פונט קצת יותר גדול */
        color: #004080;
    }

    .control-group input[type="range"] {
        width: 100%;
        margin-bottom: 5px;
        -webkit-appearance: none; /* הסתרת סטייל ברירת מחדל */
        appearance: none;
        height: 8px;
        background: #ddd;
        outline: none;
        opacity: 0.9;
        transition: opacity .2s;
        border-radius: 5px;
    }

    .control-group input[type="range"]:hover {
        opacity: 1;
    }

     .control-group input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 18px;
        height: 18px;
        background: #007bff; /* צבע לאגודל */
        cursor: pointer;
        border-radius: 50%; /* אגודל עגול */
        border: 2px solid #fff;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }

    .control-group input[type="range"]::-moz-range-thumb {
        width: 18px;
        height: 18px;
        background: #007bff;
        cursor: pointer;
        border-radius: 50%;
         border: 2px solid #fff;
         box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }


    .control-group span {
        font-weight: bold;
        color: #0056b3; /* צבע לערכים */
        font-size: 1em;
    }


    /* ויזואליזציה */
    #thruster-visualization {
        position: relative;
        width: 100%;
        max-width: 700px; /* הגדלת שטח הויזואליזציה */
        height: 300px; /* הגדלת גובה */
        margin: 20px auto;
        border: 1px solid #b3cde0; /* גבול עדין יותר */
        background-color: #ffffff; /* רקע בהיר */
        overflow: hidden;
        border-radius: 10px;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.1); /* צל פנימי עדין */
    }

    #thruster-canvas {
        display: block;
        width: 100%;
        height: 100%;
    }

    /* פלטים */
    #thruster-outputs {
        margin-top: 30px;
        text-align: left;
        display: inline-block;
        border: 1px dashed #a0c4ff; /* גבול מעוצב */
        padding: 15px 20px;
        border-radius: 8px;
        background-color: rgba(255, 255, 255, 0.8); /* רקע שקוף למחצה */
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }

    #thruster-outputs p {
        margin: 8px 0;
        font-size: 1em;
        color: #003366;
        font-weight: 500;
    }

     #thruster-outputs span {
         font-weight: bold;
         color: #007bff; /* צבע בולט לערכים */
     }

     .output-note {
        font-size: 0.85em;
        color: #555;
        margin-top: 20px;
        font-style: italic;
     }

    #visualization-legend {
        position: absolute;
        bottom: 10px;
        left: 10px;
        background: rgba(255, 255, 255, 0.7);
        padding: 5px 10px;
        border-radius: 5px;
        font-size: 0.8em;
        color: #333;
        display: flex;
        gap: 15px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }

    .legend-color {
        display: inline-block;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        margin-left: 5px; /* Space before color dot */
        vertical-align: middle;
    }


    /* כפתור הסבר */
    #toggle-explanation {
        display: block;
        margin: 30px auto;
        padding: 12px 20px;
        font-size: 1.1em;
        cursor: pointer;
        border: none; /* הסרת גבול ברירת מחדל */
        background: linear-gradient(45deg, #007bff, #0056b3); /* גרדיאנט בכפתור */
        color: white;
        border-radius: 30px; /* כפתור עגול יותר */
        transition: all 0.3s ease; /* אנימציית מעבר */
        box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3); /* צל לכפתור */
        font-weight: bold;
    }

    #toggle-explanation:hover {
        background: linear-gradient(45deg, #0056b3, #003d7a);
        box-shadow: 0 6px 12px rgba(0, 123, 255, 0.4);
        transform: translateY(-2px); /* אפקט הרמה קל */
    }

    /* הסבר */
    #explanation {
        margin-top: 30px;
        padding: 20px;
        border: none;
        border-radius: 12px;
        background-color: #e9ecef; /* רקע בהיר יותר להסבר */
        line-height: 1.7;
        text-align: right; /* יישור לימין לטקסט עברי */
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }

    #explanation.hidden {
        display: none;
    }

    #explanation h2 {
        color: #003366;
        margin-top: 0;
        margin-bottom: 20px;
        font-size: 2em;
        border-bottom: 2px solid #a0c4ff; /* קו תחתון לכותרת ראשית */
        padding-bottom: 10px;
    }

    #explanation h3 {
        color: #004080;
        margin-top: 25px;
        margin-bottom: 15px;
        font-size: 1.5em;
    }

     #explanation p, #explanation ul, #explanation ol {
         color: #333;
         margin-bottom: 15px;
     }

     #explanation ul, #explanation ol {
         padding-right: 20px; /* מרווח לרשימות */
     }

     #explanation li {
         margin-bottom: 8px;
     }
</style>

<script>
    const fuelFlowSlider = document.getElementById('fuel-flow');
    const electricFieldSlider = document.getElementById('electric-field');
    const magneticFieldSlider = document.getElementById('magnetic-field');

    const fuelFlowValueSpan = document.getElementById('fuel-flow-value');
    const electricFieldValueSpan = document.getElementById('electric-field-value');
    const magneticFieldValueSpan = document.getElementById('magnetic-field-value');

    const thrustOutput = document.getElementById('thrust-output');
    const efficiencyOutput = document.getElementById('efficiency-output');
    const powerOutput = document.getElementById('power-output');

    const explanationDiv = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggle-explanation');

    const canvas = document.getElementById('thruster-canvas');
    const ctx = canvas.getContext('2d');

    let particles = [];
    const particleBaseCount = 150; // Base number of particles
    let currentParticleCount = particleBaseCount;

    // Define regions in the canvas (relative width)
    const REGION_ENTRY = 0.1; // Fuel entry
    const REGION_IONIZATION = 0.35; // Ionization chamber
    const REGION_ACCELERATION = 0.75; // Hall channel/Acceleration
    const REGION_EXHAUST = 1.0; // Exhaust plume

    // Particle representation with more states and behavior
    class Particle {
        constructor() {
            this.reset();
        }

        reset() {
             // Start point - slightly before entry to simulate flow in
             this.x = -10 - Math.random() * 20;
             // Y position - within entry port area
             this.y = canvas.height / 2 + (Math.random() - 0.5) * (canvas.height * 0.1);

             this.vx = 0; // velocity x
             this.vy = 0; // velocity y

             this.size = 2;
             this.color = 'grey';
             this.type = 'neutral'; // 'neutral', 'ion', 'electron'
             this.state = 'entering'; // 'entering', 'ionizing', 'accelerating', 'exhaust'

             this.life = 0; // Time in current state/total life
             this.maxIonizeTime = 60 + Math.random() * 60; // How long before ionization attempt
        }

        update(fuelFlow, electricField, magneticField) {
            this.life++;

            if (this.state === 'entering') {
                // Move slowly into the chamber
                this.vx = 0.5 + fuelFlow * 0.2;
                this.x += this.vx;
                this.y += (Math.random() - 0.5) * 0.5; // Slight random drift

                // Transition to ionization state once inside chamber entry
                if (this.x > canvas.width * REGION_ENTRY) {
                    this.state = 'ionizing';
                    this.life = 0; // Reset life for next stage
                     this.vx = 0; // Stop entry velocity
                     this.vy = 0;
                }

            } else if (this.state === 'ionizing') {
                // Drift in ionization chamber, attempt ionization
                this.vx = (Math.random() - 0.5) * 1;
                this.vy = (Math.random() - 0.5) * 1;
                 this.x += this.vx;
                 this.y += this.vy;

                // Clamp position within ionization/acceleration regions
                 this.x = Math.max(canvas.width * REGION_ENTRY * 0.8, Math.min(this.x, canvas.width * REGION_ACCELERATION * 1.1));
                 this.y = Math.max(canvas.height * 0.5 - canvas.height * 0.18, Math.min(this.y, canvas.height * 0.5 + canvas.height * 0.18));


                // Probability of ionization depends on Electric Field (energy) and Magnetic Field (confinement aiding collisions)
                const ionizationChance = (electricField / 700) * (magneticField / 4) * (fuelFlow / 3) * 0.03; // Adjusted probability scale

                if (this.life > this.maxIonizeTime || Math.random() < ionizationChance) {
                    // Success! Ionize. Roughly 50/50 ion/electron split
                    if (Math.random() > 0.55) { // Slightly more ions needed for thrust
                        this.type = 'ion';
                        this.color = '#00aaff'; // Bright blue for ions
                        this.size = 3;
                        this.state = 'accelerating';
                        this.life = 0; // Reset life for next stage
                        this.vx = 0; this.vy = 0; // Will get acceleration next update
                    } else {
                        this.type = 'electron';
                        this.color = '#ffdd00'; // Bright yellow for electrons
                        this.size = 2;
                         // Electrons stay in ionizing/acceleration region longer, crucial for the process
                        this.state = 'ionizing'; // Electrons are 'ionized' but stay 'ionizing' state to show confinement
                         this.life = 0; // Stay in this state longer
                         this.maxIonizeTime = 120 + Math.random() * 80; // Electrons live longer in the channel
                         this.vx = 0; this.vy = 0; // Reset velocity
                    }
                }

            } else if (this.state === 'accelerating' && this.type === 'ion') {
                 // Ions are accelerated through the channel
                 const baseAcceleration = electricField / 100; // Acceleration scales directly with Electric Field
                 this.vx += baseAcceleration * 0.1; // Constant acceleration forward

                 // Magnetic field slightly focuses ions towards center line (simplified)
                 const radialForce = (this.y - canvas.height / 2) * -0.005 * magneticField;
                 this.vy += radialForce;

                 this.x += this.vx;
                 this.y += this.vy;

                 // Transition to exhaust state
                 if (this.x > canvas.width * REGION_ACCELERATION) {
                    this.state = 'exhaust';
                    this.life = 0;
                 }

            } else if (this.type === 'electron' && this.state === 'ionizing') {
                 // Electrons trapped and spiral in the acceleration channel region due to magnetic field
                 // Their movement is key to setting up the Hall field
                 const centerX = canvas.width * (REGION_ENTRY + (REGION_ACCELERATION - REGION_ENTRY) * 0.6); // Center of the channel axially
                 const centerY = canvas.height / 2;

                 // Simulate orbital motion + slow drift + influence by electric field
                 const dx = this.x - centerX;
                 const dy = this.y - centerY;
                 const dist = Math.sqrt(dx*dx + dy*dy);
                 const angle = Math.atan2(dy, dx);

                 const orbitalSpeed = magneticField * 0.8 + electricField * 0.01; // Faster orbit with stronger fields
                 const driftSpeed = electricField * 0.005; // Slow drift towards anode (left)

                 this.vx = -Math.sin(angle) * orbitalSpeed + Math.cos(angle) * driftSpeed * (1 - magneticField/5); // Drift scaled by inverse magnetic field effect
                 this.vy = Math.cos(angle) * orbitalSpeed;

                 this.x += this.vx;
                 this.y += this.vy;

                 // Keep electrons confined to the channel region
                 const channelRadius = canvas.height * 0.18;
                 if (dist > channelRadius) {
                     const ratio = channelRadius / dist;
                     this.x = centerX + dx * ratio;
                     this.y = centerY + dy * ratio;
                 }

                 // Electrons eventually exit or recombine (simplified: just reset if they drift too far right or live too long)
                 if (this.x > canvas.width * REGION_ACCELERATION * 1.1 || this.life > this.maxIonizeTime * (2 + magneticField)) { // Electrons live longer with stronger magnetic field
                    this.reset(); // Electron exits or is lost/recombines
                 }

            } else if (this.state === 'exhaust') {
                // Fly off screen
                this.x += this.vx;
                this.y += this.vy;

                // Reset if off screen
                 if (this.x > canvas.width + 50 || this.x < -50 || this.y > canvas.height + 50 || this.y < -50) {
                     this.reset();
                 }
            }

            // If particle is neutral or ion and drifts off left (shouldn't happen much with good logic but as safeguard)
             if (this.x < -10) {
                 this.reset();
             }
        }


        draw(ctx) {
             ctx.fillStyle = this.color;
             ctx.beginPath();
             ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
             ctx.fill();

            // Optional: Draw tail for accelerated ions
            if (this.state === 'accelerating' && this.type === 'ion' && this.vx > 2) {
                ctx.strokeStyle = this.color + '66'; // Semi-transparent trail
                ctx.lineWidth = this.size / 2;
                ctx.beginPath();
                ctx.moveTo(this.x, this.y);
                ctx.lineTo(this.x - this.vx * 2, this.y - this.vy * 2); // Trail based on velocity
                ctx.stroke();
            }
        }
    }

    // Initialize particles based on current fuel flow
    function initParticles() {
        particles = [];
        currentParticleCount = particleBaseCount + Math.floor(fuelFlowSlider.value * 50); // Adjust count based on fuel flow
        for (let i = 0; i < currentParticleCount; i++) {
             particles.push(new Particle());
             // Stagger initial positions slightly
             particles[i].x = -Math.random() * canvas.width * REGION_ENTRY * 2; // Start before the entry point
        }
    }

    // Animation loop
    function animate() {
        // Clear canvas with a slight fade effect for trails
        ctx.fillStyle = 'rgba(255, 255, 255, 0.3)'; // Semi-transparent white
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        // ctx.clearRect(0, 0, canvas.width, canvas.height); // Use this for sharp clear

        const fuelFlow = parseFloat(fuelFlowSlider.value);
        const electricField = parseFloat(electricFieldSlider.value);
        const magneticField = parseFloat(magneticFieldSlider.value);

        // Adjust particle count dynamically based on fuel flow
        const targetParticleCount = particleBaseCount + Math.floor(fuelFlow * 70);
        while (particles.length < targetParticleCount) {
            particles.push(new Particle());
        }
        while (particles.length > targetParticleCount && particles.length > particleBaseCount / 2) {
             // Remove oldest particles in a 'neutral' or 'entering' state first
            let removed = false;
             for(let i = 0; i < particles.length; i++) {
                 if (particles[i].state === 'entering' || particles[i].state === 'ionizing') {
                     particles.splice(i, 1);
                     removed = true;
                     break;
                 }
             }
             if (!removed) { // If no entering/ionizing, remove oldest in any state
                 particles.shift();
             }
        }


        // Draw Thruster representation (more detailed Hall thruster)
        const thrusterWidth = canvas.width * 0.9;
        const thrusterHeight = canvas.height * 0.5;
        const thrusterY = canvas.height / 2 - thrusterHeight / 2;

        // Base
        ctx.fillStyle = '#556070'; // Dark grey/blue
        ctx.fillRect(0, thrusterY + thrusterHeight * 0.2, thrusterWidth * REGION_ENTRY * 1.2, thrusterHeight * 0.6);

        // Discharge channel (Anode side)
        ctx.fillStyle = '#778899';
        ctx.fillRect(thrusterWidth * REGION_ENTRY * 1.2, thrusterY, thrusterWidth * (REGION_ACCELERATION - REGION_ENTRY * 1.2), thrusterHeight);

        // Magnetic field poles (simplified rectangles)
        ctx.fillStyle = '#445060';
        const poleWidth = thrusterWidth * 0.05;
        const poleHeight = thrusterHeight * 0.3;
        ctx.fillRect(thrusterWidth * (REGION_ENTRY + (REGION_ACCELERATION - REGION_ENTRY) / 3) - poleWidth/2, thrusterY - poleHeight, poleWidth, poleHeight); // Top pole
        ctx.fillRect(thrusterWidth * (REGION_ENTRY + (REGION_ACCELERATION - REGION_ENTRY) / 3) - poleWidth/2, thrusterY + thrusterHeight, poleWidth, poleHeight); // Bottom pole

        // Acceleration channel / Exit (Cathode side)
        ctx.fillStyle = '#99aabb';
        ctx.beginPath();
        ctx.moveTo(thrusterWidth * REGION_ACCELERATION, thrusterY);
        ctx.lineTo(thrusterWidth * REGION_EXHAUST, thrusterY - thrusterHeight * 0.2); // Top exit
        ctx.lineTo(thrusterWidth * REGION_EXHAUST, thrusterY + thrusterHeight * 1.2); // Bottom exit
        ctx.lineTo(thrusterWidth * REGION_ACCELERATION, thrusterY + thrusterHeight);
        ctx.closePath();
        ctx.fill();

         // Exhaust Plume Glow (simplified visual effect)
         const plumeIntensity = Math.min(1, estimatedThrust / 100); // Scales with thrust
         const gradient = ctx.createRadialGradient(
             canvas.width * REGION_EXHAUST, canvas.height / 2, 0,
             canvas.width * REGION_EXHAUST, canvas.height / 2, canvas.width * 0.3 * plumeIntensity + 20
         );
         gradient.addColorStop(0, `rgba(0, 170, 255, ${0.5 * plumeIntensity})`);
         gradient.addColorStop(0.5, `rgba(0, 170, 255, ${0.2 * plumeIntensity})`);
         gradient.addColorStop(1, 'rgba(0, 170, 255, 0)');

         ctx.fillStyle = gradient;
         ctx.beginPath();
         ctx.moveTo(canvas.width * REGION_ACCELERATION, canvas.height / 2 - thrusterHeight * 0.5);
         ctx.lineTo(canvas.width, canvas.height / 2 - thrusterHeight * 0.8); // Wider plume exit
         ctx.lineTo(canvas.width, canvas.height / 2 + thrusterHeight * 0.8);
         ctx.lineTo(canvas.width * REGION_ACCELERATION, canvas.height / 2 + thrusterHeight * 0.5);
         ctx.closePath();
         ctx.fill();


        // Update and draw particles
        let totalIonMomentum = 0; // For thrust calculation
        let totalIonMassFlow = 0; // For Isp calculation
        let totalPowerEstimate = 0; // For power calculation

        particles.forEach(p => {
            p.update(fuelFlow, electricField, magneticField);
            p.draw(ctx);

            // Accumulate data from exiting ions for output calculations
            if (p.state === 'exhaust' && p.type === 'ion') {
                const ionMassUnit = 1; // Simplified mass unit for ions (relative)
                totalIonMomentum += p.vx * ionMassUnit; // Momentum = mass * velocity
                totalIonMassFlow += ionMassUnit; // Total mass exiting in this frame
                totalPowerEstimate += 0.5 * ionMassUnit * p.vx * p.vx; // Kinetic energy (simplified power)
            }
        });

        // Simple output calculations based on aggregated particle data and slider values
        // These are still simplified/relative but linked to simulation velocity
        const averageExitVelocity = totalIonMassFlow > 0 ? totalIonMomentum / totalIonMassFlow : 0;

        // Thrust: Roughly Proportional to Mass Flow Rate * Exhaust Velocity
        // Mass flow rate is represented by fuelFlowSlider.value and particle count.
        // Exhaust velocity is represented by averageExitVelocity (driven by electricField).
        const estimatedThrust = fuelFlow * averageExitVelocity * 0.05; // Scaling factor

        // Efficiency (Isp): Proportional to Exhaust Velocity
        const estimatedEfficiency = averageExitVelocity * 5; // Scaling factor (Isp is velocity / g0)

        // Power: Roughly Proportional to Mass Flow Rate * (Exhaust Velocity)^2 / 2
        // Simplified: roughly Proportional to Fuel Flow * Electric Field (voltage)
        const estimatedPower = fuelFlow * electricField * 0.1; // Scaling factor


        // Update outputs with smoothing (optional, for visual effect)
        thrustOutput.textContent = Math.max(0, estimatedThrust).toFixed(2) + ' יח\'';
        efficiencyOutput.textContent = Math.max(0, estimatedEfficiency).toFixed(1) + ' יח\'';
        powerOutput.textContent = Math.max(0, estimatedPower).toFixed(1) + ' יח\'';


        requestAnimationFrame(animate);
    }

    // Update slider value displays
    fuelFlowSlider.addEventListener('input', () => {
        fuelFlowValueSpan.textContent = fuelFlowSlider.value;
        // Optionally re-initialize particles for immediate count change visual
        // initParticles(); // Can be jarring, dynamic count change in animate loop is better
    });
    electricFieldSlider.addEventListener('input', () => {
        electricFieldValueSpan.textContent = electricFieldSlider.value;
    });
    magneticFieldSlider.addEventListener('input', () => {
        magneticFieldValueSpan.textContent = magneticFieldSlider.value;
    });


    // Toggle explanation visibility
    toggleButton.addEventListener('click', () => {
        explanationDiv.classList.toggle('hidden');
        const isHidden = explanationDiv.classList.contains('hidden');
        toggleButton.textContent = isHidden ? 'רוצים לדעת עוד? לחצו להסבר מעמיק!' : 'הסתר הסבר';
    });

    // Initialize canvas size and start animation
    function resizeCanvas() {
        const container = document.getElementById('thruster-visualization');
        canvas.width = container.offsetWidth;
        canvas.height = container.offsetHeight;
        initParticles(); // Re-initialize particles on resize
    }

    // Load Heebo font
     const link = document.createElement('link');
     link.href = 'https://fonts.googleapis.com/css2?family=Heebo:wght@400;500;700&display=swap';
     link.rel = 'stylesheet';
     document.head.appendChild(link);


    window.addEventListener('resize', resizeCanvas);

    // Initial setup
    resizeCanvas(); // Set initial size and particles
    animate(); // Start animation loop
</script>
```