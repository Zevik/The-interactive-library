---
title: "מסע החול הגדול: כך נולדות סופות ואבק נדד בעולם"
english_slug: great-sand-journey-how-storms-are-born-dust-travels
category: "מדעי כדור הארץ"
tags: [סופת חול, אקלים, גאוגרפיה, מטאורולוגיה, הדמיה, אינטראקטיבי, דינמיקה אטמוספרית]
---
<h1>מסע החול הגדול: כך נולדות סופות ואבק נדד בעולם</h1>
הצצה מרהיבה אל אחת התופעות האטמוספריות העוצמתיות והמשפיעות ביותר בעולם: סופת החול והאבק. מה מניע מיליארדי חלקיקים זעירים להתרומם מהקרקע ולנדוד אלפי קילומטרים, משנים אקלים, משפיעים על בריאות ואף מדשנים יערות גשם רחוקים? התנסו בעצמכם כדי לגלות!

<div class="app-container">
    <h2>סימולציית דינמיקת חלקיקי קרקע</h2>
    <div class="controls">
        <div class="control-group">
            <label for="windSpeed" class="control-label">עוצמת הרוח:</label>
            <input type="range" id="windSpeed" min="0" max="60" value="0" step="1">
            <span id="windValue" class="wind-value">0</span> קמ"ש
             <div class="wind-bar">
                <div id="windProgress" class="wind-progress"></div>
             </div>
        </div>

        <div class="control-group soil-control">
            <label class="control-label">מצב הקרקע:</label>
            <div class="soil-options">
                <input type="radio" id="soilDry" name="soilType" value="dry" checked>
                <label for="soilDry" class="radio-label">יבשה ופרודה</label>
                <input type="radio" id="soilWet" name="soilType" value="wet">
                <label for="soilWet" class="radio-label">לחה ומלוכדת</label>
            </div>
        </div>

        <div class="threshold-display">
            סף הרוח הקריטי לתנועת חלקיקים ראשונית (קיפוץ): <span id="criticalThreshold">--</span> קמ"ש
        </div>
    </div>
    <div class="simulation-area">
         <div class="ground"></div>
         <div class="particles-container">
            <!-- Sand particles will be added here by JS -->
         </div>
        <div class="wind-indicator">💨</div>
        <div class="wind-lines"></div> <!-- Added for visual effect -->
    </div>
    <div class="key">
        <h3>מנגנוני תנועה עיקריים:</h3>
        <div class="key-item"><span class="particle static-particle stationary"></span> עמידה / זחילה איטית (Creep)</div>
        <div class="key-item"><span class="particle static-particle saltation"></span> קיפוץ דינמי (Saltation)</div>
        <div class="key-item"><span class="particle static-particle suspension"></span> ריחוף למרחקים (Suspension)</div>
    </div>
</div>

<button id="toggleExplanation">קראו על מסע החול: הסבר מפורט</button>

<div id="explanation" style="display: none;">
    <h2>מסע החול הגדול: הבנת התופעה</h2>
    <p>סופות חול ואבק הן אירועים אטמוספריים דרמטיים המתרחשים כאשר רוחות עזות מרימות כמויות אדירות של חלקיקי קרקע - חול, טין ואבק - ונושאות אותם למרחקים. בעוד שסופת חול מתייחסת בדרך כלל לחלקיקים הגדולים יותר (חול, בקוטר עשרות עד מאות מיקרונים) הנעים בעיקר סמוך לקרקע ב'קיפוץ', סופת אבק כוללת חלקיקים קטנים בהרבה (פחות מ-60 מיקרון) היכולים להישאר באוויר שעות וימים ולנדוד אלפי קילומטרים ב'ריחוף'. הסימולציה שלפניכם ממחישה את סקלת התנועה של חלקיקים בגדלים שונים כתלות בעוצמת הרוח ומצב הקרקע.</p>

    <h3>המרכיבים החיוניים להיווצרות סופה:</h3>
    <p>שלושה תנאים מרכזיים חייבים להתקיים:</p>
    <ol>
        <li><strong>משטח יבש ופגיע:</strong> אזורים מדבריים, צחיחים, או שטחים חקלאיים שסבלו מבצורת או עיבוד יתר. הקרקע חשופה, ללא כיסוי צמחי משמעותי וללא לחות מספקת שתאחד את החלקיקים.</li>
        <li><strong>אספקת חלקיקים:</strong> נוכחות של כמויות גדולות של חול ואבק זמינים על פני הקרקע, מוכנים להיסחפות.</li>
        <li><strong>רוח מספיק חזקה:</strong> עוצמת רוח המסוגלת לגבור על כוחות הכבידה והחיכוך האוחזים בחלקיקים. זהו המרכיב הדינמי העיקרי, והסימולציה מתמקדת בהשפעתו.</li>
    </ol>

    <h3>ריקוד החלקיקים: מנגנוני התנועה</h3>
    <p>כשהרוח מתגברת, חלקיקי הקרקע מתחילים לנוע בדרכים שונות, בהתאם לגודלם ולעוצמת הרוח המופעלת עליהם:</p>
    <ul>
        <li><strong>זחילה (Creep):</strong> החלקיקים הכבדים ביותר (חול גס, 500-1000 מיקרון). הם אינם נישאים ברוח ישירות, אלא נדחפים או מתגלגלים לאט על פני הקרקע, לעיתים כתוצאה מפגיעת חלקיקים קטנים יותר המקפצים בהם. מהווה חלק קטן יחסית מסך המסה הנישאת, אך חשוב בתחילת התהליך.</li>
        <li><strong>קיפוץ (Saltation):</strong> המנגנון הדומיננטי עבור חלקיקי חול בגודל בינוני (70-500 מיקרון). זוהי תנועה של קפיצות קצרות: הרוח מרימה את החלקיק לגובה נמוך (סנטימטרים ספורים עד מטר), הוא נע עם הרוח ונוחת חזרה. הפגיעה בקרקע גורמת לניתור נוסף של חלקיק זה או חלקיקים אחרים, ויוצרת אפקט דומינו המגביר את התנועה. סימולציית ה'קיפוץ' ממחישה את האנרגיה המועברת בפגיעות אלו.</li>
        <li><strong>ריחוף (Suspension):</strong> המנגנון המשפיע ביותר על טווח הסופה עבור חלקיקים קטנים מאוד (אבק, פחות מ-60 מיקרון). חלקיקים אלו קלים מספיק כדי להישאר באוויר זמן רב, נישאים על ידי מערבולות הרוח לגבהים רמים (מאות ואף אלפי מטרים). הם יכולים לנסוע מרחקים עצומים, לחצות יבשות ואוקיינוסים, והם הגורם העיקרי להשפעות חוצות גבולות של סופות אבק, כמו ירידת ראות ושינויים אקולוגיים גלובליים.</li>
    </ul>

    <h3>סף הרוח הקריטי: מתי מתחיל הריקוד?</h3>
    <p>נדרשת מהירות רוח מינימלית ("סף התחלה") כדי לגרום לחלקיקים להתחיל לנוע, בעיקר לקיפוץ. סף זה אינו קבוע ותלוי בגורמים רבים:</p>
    <ul>
        <li><strong>גודל חלקיקים:</strong> חלקיקים קטנים מאוד (שנדבקים זה לזה) וגדולים מאוד (כבדים) דורשים רוח חזקה יותר מחלקיקים בגודל בינוני (חול) שהם ה"קופצים" הטבעיים.</li>
        <li><strong>לחות הקרקע:</strong> מים "מדביקים" את החלקיקים. קרקע לחה דורשת רוח חזקה משמעותית לעומת קרקע יבשה. הסימולציה מדגימה בבירור הבדל זה.</li>
        <li><strong>כיסוי צמחי:</strong> צמחייה מגינה על הקרקע ומפחיתה את מהירות הרוח קרוב לפני השטח, מעלה למעשה את סף הרוח האפקטיבי.</li>
        <li><strong>גורמים נוספים:</strong> קרום קרקע (Crust), חומר אורגני, וקשרים כימיים בקרקע יכולים גם הם להשפיע על מידת הלכידות.</li>
    </ul>
    <p>ברגע שמהירות הרוח עוברת את הסף ומתחיל קיפוץ, החלקיקים המקפצים פוגעים בקרקע ומעיפים חלקיקים נוספים, גם כאלה שהיו מלוכדים יותר. תהליך זה יוצר משוב חיובי ויכול לגרום להתפשטות מהירה של תנועת החול והאבק.</p>

    <h3>המסע והשפעותיו: מעבר למדבר</h3>
    <p>עוצמת הסופה, גובה הריחוף וטווח הנשיאה תלויים בגורמים מטאורולוגיים (מהירות וכיוון רוח, יציבות אטמוספרית) ובמאפייני הקרקע (כמות וגודל החלקיקים הזמינים). חלקיקי אבק יכולים להיסחף אלפי קילומטרים ולהשפיע על:</p>
    <ul>
        <li><strong>בריאות:</strong> חלקיקים נשימים חודרים לדרכי הנשימה, מחמירים אסטמה, ברונכיטיס ובעיות לב. סופות גם מעבירות חיידקים, וירוסים וכימיקלים.</li>
        <li><strong>תחבורה:</strong> ירידה חדה בראות מסכנת טיסות, נסיעה בכבישים ושיט ימי.</li>
        <li><strong>תשתיות:</strong> שחיקה ונזק למבנים, כבישים, מסילות רכבת ופנלים סולאריים.</li>
        <li><strong>אקלים:</strong> חלקיקי אבק באטמוספרה משנים את מאזן הקרינה (בולעים/מפזרים אור), משפיעים על היווצרות עננים ומשקעים, ויכולים להשפיע על הטמפרטורה.</li>
        <li><strong>מערכות אקולוגיות:</strong> אבק עשיר במינרלים מדשן אזורים מרוחקים כמו יערות גשם (האמזונס מקבל אבק מהסהרה!) ואוקיינוסים דלי חומרי מזון, אך במקור הוא גורם לאיבוד קרקע פורייה.</li>
    </ul>

    <h3>מוקדי סופות עולמיים:</h3>
    <p>האזורים הפעילים ביותר בעולם מבחינת סופות חול ואבק הם המדבריות הגדולים ואזורים צחיחים למחצה: סהרה (צפון אפריקה), חגורת המדבריות של המזרח התיכון ומרכז אסיה (כולל גובי), חלקים מדרום מערב ארה"ב, אוסטרליה, דרום אמריקה ואף אזורים מסוימים באפריקה שמדרום לסהרה (הסאהל). התחממות גלובלית ושינויים בשימושי קרקע עלולים להרחיב אזורים אלו.</p>
</div>

<style>
    :root {
        --sand-color-light: #f4a460; /* SandyBrown */
        --sand-color-medium: #d2b48c; /* Tan */
        --sand-color-dark: #c0a070; /* Darker Sand */
        --dust-color: #e9967a; /* DarkSalmon */
        --ground-color: #b08b5f; /* Even darker ground */
        --border-color: #ccc;
        --bg-color: #f9f9f9;
        --control-bg-color: #eee;
        --threshold-color: #c0392b; /* Reddish */
        --wind-color: #5a9bd5; /* Blueish for wind lines */
        --transition-speed: 0.3s ease-in-out;
    }

    .app-container {
        font-family: 'Arial', sans-serif;
        direction: rtl;
        text-align: right;
        border: 1px solid var(--border-color);
        padding: 20px;
        margin-bottom: 20px;
        background-color: var(--bg-color);
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        overflow: hidden; /* Ensure elements stay within bounds */
    }

    h1 {
        text-align: center;
        color: #333;
        margin-bottom: 20px;
    }

    .app-container h2 {
        text-align: center;
        color: #555;
        margin-bottom: 20px;
        font-size: 1.5em;
    }

    .controls {
        margin-bottom: 20px;
        padding: 15px;
        background-color: var(--control-bg-color);
        border-radius: 8px;
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        align-items: center;
        justify-content: center;
    }

    .control-group {
         flex: 1 1 250px; /* Allow items to grow/shrink, base width */
         min-width: 200px;
         display: flex;
         flex-direction: column;
         align-items: flex-start;
    }

    .control-label {
        margin-bottom: 8px;
        font-weight: bold;
        color: #333;
    }

    #windSpeed {
        width: 100%;
        height: 8px;
        -webkit-appearance: none;
        appearance: none;
        background: #ddd;
        outline: none;
        opacity: 0.7;
        transition: opacity var(--transition-speed);
        border-radius: 4px;
        margin-bottom: 5px;
    }

    #windSpeed:hover {
        opacity: 1;
    }

    #windSpeed::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 18px;
        height: 18px;
        background: var(--sand-color-light);
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #fff;
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }

    #windSpeed::-moz-range-thumb {
         width: 18px;
         height: 18px;
         background: var(--sand-color-light);
         cursor: pointer;
         border-radius: 50%;
         border: 2px solid #fff;
         box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }

    .wind-value {
        display: inline-block;
        width: 40px;
        text-align: center;
        font-weight: bold;
        color: var(--threshold-color);
        margin-right: 5px;
    }

    .wind-bar {
        width: 100%;
        height: 10px;
        background-color: #ddd;
        border-radius: 5px;
        overflow: hidden;
        margin-top: 5px;
    }

    .wind-progress {
        height: 100%;
        width: 0%; /* Controlled by JS */
        background: linear-gradient(to right, #a0c8f0, var(--wind-color));
        transition: width var(--transition-speed);
    }


    .soil-control {
         align-items: flex-start;
    }

    .soil-options {
        display: flex;
        gap: 15px;
    }

    .soil-options input[type="radio"] {
        margin-left: 5px;
        cursor: pointer;
    }

    .radio-label {
        cursor: pointer;
        color: #555;
    }


    .threshold-display {
        margin-top: 10px;
        font-weight: bold;
        color: #333;
        text-align: center;
        width: 100%; /* Take full width in flex layout */
    }

    #criticalThreshold {
        color: var(--threshold-color);
        font-size: 1.1em;
    }

    .simulation-area {
        position: relative;
        width: 100%;
        height: 300px; /* Increased height for better visualization */
        border: 1px solid var(--border-color);
        background: linear-gradient(to bottom, #87ceeb 0%, #e0c9a7 70%, var(--sand-color-medium) 100%); /* Sky to sand gradient */
        overflow: hidden;
        margin-top: 20px;
        border-radius: 8px;
        box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.1);
    }

    .ground {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 30px; /* Clearer ground line */
        background-color: var(--ground-color);
        z-index: 0; /* Behind particles */
    }

     .particles-container {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
         z-index: 1;
     }


    .particle {
        position: absolute;
        width: 6px; /* Base size */
        height: 6px;
        background-color: var(--sand-color-light);
        border-radius: 50%;
        transform-origin: center; /* Center of particle */
        will-change: transform, left, bottom, opacity; /* Optimize for animation */
         pointer-events: none; /* Don't interfere with mouse */
         z-index: 2;
    }

     .particle.small {
        width: 4px;
        height: 4px;
         background-color: var(--dust-color);
     }

     /* --- Keyframe Animations (managed by JS) --- */

     /* Base movement across the screen - JS updates position, animation adds style */

    @keyframes creep-anim {
        0% { transform: translate(0, 0px) rotate(0deg); }
        50% { transform: translate(5px, -1px) rotate(1deg); } /* Subtle wobble */
        100% { transform: translate(10px, 0px) rotate(0deg); }
    }

    @keyframes saltation-anim {
        0% { transform: translate(0, 0) scale(1); opacity: 1; }
        30% { transform: translate(calc(var(--jump-dist) * 0.3), -40px) scale(1.1) rotate(10deg); opacity: 1; } /* Peak of jump */
        70% { transform: translate(calc(var(--jump-dist) * 0.7), -10px) scale(1.05) rotate(-5deg); opacity: 1; }
        100% { transform: translate(var(--jump-dist), 0) scale(1) rotate(0deg); opacity: 1; } /* Land */
    }

     @keyframes suspension-anim {
        0% { transform: translate(0, 0) scale(1); opacity: 1; }
        20% { transform: translate(50px, -20px) scale(1.05); opacity: 0.9; }
        40% { transform: translate(120px, -50px) scale(1.1); opacity: 0.8; }
        60% { transform: translate(200px, -80px) scale(1.15); opacity: 0.7; }
        80% { transform: translate(280px, -100px) scale(1.2); opacity: 0.6; }
        100% { transform: translate(350px, -110px) scale(1.2); opacity: 0.5; } /* Drift far and fade */
     }


    /* --- Particle State Classes (assigned by JS) --- */
     .particle.stationary {
         animation: none;
         transform: none !important; /* Ensure no animation or transform */
         opacity: 1;
     }

     .particle.creep {
         animation-name: creep-anim;
         animation-timing-function: linear;
         animation-iteration-count: infinite;
     }

    .particle.saltation {
         animation-name: saltation-anim;
         animation-timing-function: cubic-bezier(0.25, 0.46, 0.45, 0.94); /* EaseOutQuad-like for jump */
         animation-iteration-count: 1; /* Single jump */
         animation-fill-mode: forwards; /* Keep final state */
         /* animation-duration is set by JS */
         /* --jump-dist is set by JS */
    }

    .particle.suspension {
        animation-name: suspension-anim;
        animation-timing-function: linear;
        animation-iteration-count: 1; /* Single drift segment */
        animation-fill-mode: forwards; /* Keep final state */
        /* animation-duration is set by JS */
    }

    /* Wind Indicator */
     .wind-indicator {
        position: absolute;
        top: 20px;
        right: 20px; /* Hebrew direction */
        font-size: 3em;
        opacity: 0.6;
        transform: scaleX(-1); /* Point left to show wind from left */
        transition: opacity var(--transition-speed), transform var(--transition-speed);
         filter: drop-shadow(2px 2px 2px rgba(0,0,0,0.2));
         color: rgba(0,0,0,0.6); /* Darker color for visibility */
         z-index: 10;
    }

    .wind-indicator.active {
        opacity: 1;
        /* pulsing effect controlled by JS/CSS class if needed */
    }

     /* Wind lines visual effect */
     .wind-lines {
         position: absolute;
         top: 0;
         left: 0;
         width: 100%;
         height: 100%;
         pointer-events: none;
         overflow: hidden;
         z-index: 5;
     }

     .wind-lines::before {
         content: '';
         position: absolute;
         top: 0;
         left: 0;
         width: 300%; /* Wider to cover animation */
         height: 100%;
         background: repeating-linear-gradient(
            to right,
            transparent,
            transparent 50px, /* Line spacing */
            rgba(255, 255, 255, 0.3) 50px, /* Line start */
            rgba(255, 255, 255, 0.3) 52px, /* Line width */
            transparent 52px /* Line end */
         );
         background-size: 100px 100%; /* Control spacing */
         animation: wind-lines-anim 10s linear infinite;
         opacity: 0; /* Hidden by default */
         transition: opacity var(--transition-speed);
     }

     .wind-lines.active::before {
        opacity: 0.5; /* Visible when active */
        /* animation-duration adjusted by JS */
     }

     @keyframes wind-lines-anim {
         0% { transform: translateX(0); }
         100% { transform: translateX(-200%); } /* Move across */
     }


    .key {
        margin-top: 20px;
        padding: 15px;
        background-color: var(--control-bg-color);
        border-radius: 8px;
        text-align: right;
    }

     .key h3 {
         margin-top: 0;
         margin-bottom: 15px;
         color: #555;
         text-align: center;
     }

    .key-item {
        display: flex;
        align-items: center;
        margin-bottom: 8px;
        color: #333;
        font-size: 0.95em;
    }

    .key-item .static-particle {
        position: static; /* Reset position for key */
        display: inline-block;
        margin-left: 8px; /* Space between dot and text */
        vertical-align: middle;
        animation: none !important; /* No animation in key */
        transform: none !important;
        bottom: auto;
        left: auto;
        width: 10px; /* Larger dots in key */
        height: 10px;
         border: none; /* Remove border if any */
         box-shadow: none; /* Remove shadow if any */
    }

     .key-item .static-particle.creep {
          background-color: var(--sand-color-light); /* Same as main particles */
     }
     .key-item .static-particle.saltation {
          background-color: var(--sand-color-light); /* Same as main particles */
     }
     .key-item .static-particle.suspension {
          background-color: var(--dust-color); /* Same as small particles */
     }


    #toggleExplanation {
        display: block;
        margin: 20px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        background-color: #5a9bd5; /* Blue button */
        color: white;
        border-radius: 6px;
        transition: background-color var(--transition-speed);
        text-align: center;
    }

    #toggleExplanation:hover {
        background-color: #4a8ac2;
    }

    #explanation {
        border: 1px solid var(--border-color);
        padding: 20px;
        margin-top: 20px;
        background-color: var(--bg-color);
        border-radius: 12px;
        direction: rtl;
        text-align: right;
        line-height: 1.7;
        color: #333;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.08);
    }

    #explanation h2, #explanation h3 {
        text-align: center;
        margin-bottom: 15px;
        color: #444;
    }

    #explanation p, #explanation ul, #explanation ol {
        margin-bottom: 18px;
    }

    #explanation ul, #explanation ol {
        padding-right: 25px;
    }

    #explanation li {
        margin-bottom: 8px;
    }

</style>

<script>
    const windSlider = document.getElementById('windSpeed');
    const windValueSpan = document.getElementById('windValue');
    const windProgressBar = document.getElementById('windProgress');
    const soilTypeRadios = document.querySelectorAll('input[name="soilType"]');
    const particlesContainer = document.querySelector('.particles-container'); // Use the new container
    const simulationArea = document.querySelector('.simulation-area');
    const criticalThresholdSpan = document.getElementById('criticalThreshold');
    const explanationDiv = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggleExplanation');
    const windIndicator = document.querySelector('.wind-indicator');
    const windLines = document.querySelector('.wind-lines');


    // Thresholds (mapped from slider value 0-60 km/h)
    // Let's assume slider value is roughly km/h
    const thresholds = {
        dry: { saltation: 15, suspension: 30 }, // Lower thresholds for dry
        wet: { saltation: 30, suspension: 45 }  // Higher thresholds for wet
    };

    // Number of particles
    const numParticles = 80; // Increased number of particles
    const particles = [];

    // Particle properties
    const particleTypes = [
        { class: '', isSmall: false, suspensionBoost: 0 }, // Large (Sand)
        { class: 'small', isSmall: true, suspensionBoost: -10 } // Small (Dust) - easier to suspend
    ];

    // Create particles
    function createParticles() {
        particlesContainer.innerHTML = ''; // Clear existing particles
        particles.length = 0; // Clear particles array

        for (let i = 0; i < numParticles; i++) {
            const particle = document.createElement('div');
            particle.classList.add('particle');

            // Randomly assign particle type (e.g., 70% large, 30% small)
            const type = Math.random() < 0.3 ? particleTypes[1] : particleTypes[0];
            particle.classList.add(type.class);

            // Store particle data
            const particleData = {
                element: particle,
                isSmall: type.isSmall,
                suspensionBoost: type.suspensionBoost,
                state: 'stationary', // Initial state
                left: Math.random() * 100, // Start anywhere horizontally
                bottom: 30 + Math.random() * 10 // Start just above the ground line + some variation
            };
            particles.push(particleData);

            // Set initial position
            particle.style.left = `${particleData.left}%`;
            particle.style.bottom = `${particleData.bottom}px`;
             particle.style.animationDuration = '0s'; // No animation initially

            particlesContainer.appendChild(particle);
        }
    }

    function updateSimulation() {
        const windSpeed = parseInt(windSlider.value, 10);
        windValueSpan.textContent = windSpeed;

        // Update wind progress bar
        const maxWind = parseInt(windSlider.max, 10);
        windProgressBar.style.width = `${(windSpeed / maxWind) * 100}%`;

        const selectedSoilType = document.querySelector('input[name="soilType"]:checked').value;
        const currentThresholds = thresholds[selectedSoilType];

        // Update displayed critical threshold (using saltation threshold)
        criticalThresholdSpan.textContent = currentThresholds.saltation;

        // Wind indicator visibility/opacity
        windIndicator.style.opacity = windSpeed > 5 ? 0.8 + (windSpeed / maxWind) * 0.2 : 0.6;
        windLines.classList.toggle('active', windSpeed > 10); // Show wind lines above a certain speed
        if (windSpeed > 10) {
             // Adjust wind line speed based on wind
             const windLineDuration = Math.max(2, 10 - (windSpeed / 10)); // Faster lines for faster wind
             windLines.style.setProperty('--animation-duration', `${windLineDuration}s`); // CSS variable approach if needed, or set directly
              windLines.style.animationDuration = `${windLineDuration}s`;

        }


        // Update particle states and animations
        particles.forEach(particleData => {
            const particle = particleData.element;
            const isSmall = particleData.isSmall;

            // Calculate individual suspension threshold (smaller particles easier to lift)
            const suspensionThreshold = currentThresholds.suspension + particleData.suspensionBoost;


            let newState = 'stationary';
            let animationDuration = '0s';
            let horizontalSpeed = 0; // % of screen width per second (conceptual)
            let jumpDistance = 0; // px or % horizontal distance for saltation

            if (windSpeed >= suspensionThreshold) {
                newState = 'suspension';
                // Faster, further drift with higher wind
                animationDuration = `${Math.max(2, 8 - (windSpeed - suspensionThreshold) * 0.15)}s`;
                horizontalSpeed = (windSpeed / maxWind) * 100; // Faster drift across
            } else if (windSpeed >= currentThresholds.saltation) {
                newState = 'saltation';
                // Faster, higher jumps with higher wind
                animationDuration = `${Math.max(0.4, 1.5 - (windSpeed - currentThresholds.saltation) * 0.04)}s`;
                 // Adjust jump distance based on wind speed, capping it somewhat
                 jumpDistance = Math.min(100, 10 + (windSpeed - currentThresholds.saltation) * 2); // Jump distance in pixels or relative units

            } else if (windSpeed > currentThresholds.saltation * 0.5) { // Subtle creep just below threshold
                 newState = 'creep';
                 animationDuration = '3s'; // Slow constant movement
                 horizontalSpeed = (windSpeed / maxWind) * 15; // Very slow drift
            } else {
                newState = 'stationary';
                animationDuration = '0s'; // No animation
            }


            // Apply state and animation if changed
            if (particleData.state !== newState) {
                 // Remove old class, force reflow, add new class to restart animation
                 particle.classList.remove(particleData.state);
                 void particle.offsetWidth; // Trigger reflow
                 particle.classList.add(newState);
                 particleData.state = newState;

                 // Reset position and start animation if state implies movement
                 if (newState !== 'stationary') {
                     // Reset particle to a random position on the left side or near current
                      // Let's make them loop across
                      const randomY = 30 + Math.random() * (simulationArea.offsetHeight - 40); // Keep above ground, allow some height
                      particleData.left = -5 - Math.random() * 5; // Start slightly off screen left
                      particleData.bottom = randomY; // Random vertical start
                      particle.style.left = `${particleData.left}%`;
                      particle.style.bottom = `${particleData.bottom}px`;

                       // Set initial transform to reset animation origin
                       particle.style.transform = 'translate(0, 0)';

                       // Add slight random delay to animation start
                        particle.style.animationDelay = `-${Math.random() * (parseFloat(animationDuration) * 0.8)}s`; // Negative delay for staggered start

                 } else {
                      // Snap to ground if stationary
                      particle.style.bottom = `${30 + Math.random() * 5}px`;
                 }

            }

            // Always update animation duration and other variables if the state is active
             if (newState !== 'stationary') {
                 particle.style.animationDuration = animationDuration;

                 // Set custom properties for animations that use them
                 if (newState === 'saltation') {
                      // Saltation animation duration should also affect jump height/distance
                      // This requires custom CSS properties or dynamic keyframes, complex.
                      // Let's simplify: animation duration controls speed, jump distance is handled by the keyframe roughly,
                      // or use a CSS variable if possible to influence keyframe translation amount.
                       // Trying CSS variable for jump distance:
                      const simulationWidth = simulationArea.offsetWidth;
                      const jumpDistancePx = (windSpeed / maxWind) * (simulationWidth * 0.5) + 50; // Jump further with more wind, base 50px
                      particle.style.setProperty('--jump-dist', `${jumpDistancePx}px`);
                 }
             } else {
                 particle.style.animationDuration = '0s'; // Ensure no animation plays
                  // Remove custom properties when not needed
                  particle.style.removeProperty('--jump-dist');
             }


            // Handle particle wrapping for continuous flow in active states
            // Since animations are now 'forwards' or infinite, we need to check position
            if (newState !== 'stationary') {
                 // Check if particle has moved off the right edge
                 // This check is complex with pure CSS transforms and percentages/pixels mixed.
                 // A simpler approach is to listen for 'animationend' for non-infinite animations
                 // and restart them. Infinite ones like creep need a different approach,
                 // e.g., make them cover the full width and restart.

                 // Let's make creep infinite full width, saltation/suspension single full width pass and restart
                 if (newState === 'creep') {
                     // Creep animation needs to be full width and loop infinitely.
                     // Let's adjust the CSS keyframe or rely on JS updating left.
                     // Given the structure, the best is probably JS updating `left` based on speed.
                     // BUT we are trying to keep animation in CSS.
                     // Let's make creep cover 100% width slowly and loop.
                      // Requires changing creep-anim or using JS for position update.
                      // Let's revert creep to a short subtle animation + JS position update for realism.
                      // OR keep the simple CSS animation and only restart saltation/suspension.
                      // Sticking to the plan: all moving animations will cover a distance and JS resets.

                      // Re-evaluating: The easiest way to handle continuous flow with CSS animations
                      // covering a distance is to have the JS update the *base* `left` position
                      // and the animation applies a *relative* transform. When the total position
                      // (base + transform) goes offscreen, reset the base `left` and restart anim.

                       // This requires tracking current animated position, which is tricky.
                       // Let's simplify again: All moving particles loop across the screen
                       // by setting their start position and letting a full-width animation repeat.
                       // This makes the JS simpler.

                       // New Animation Approach: All moving particles animate from 0% to 100% relative transform.
                       // JS sets initial `left`. Animation `translate(0%, 0)` to `translate(100%, Y)`.
                       // This means particles start at `left` and end at `left` + 100% width.
                       // Then, JS detects completion or going offscreen and resets `left`.

                       // Let's refine CSS keyframes for 0% to 100% relative movement.

                 } else if (newState === 'saltation' || newState === 'suspension') {
                     // For non-infinite animations (saltation, suspension segments), listen for end
                      // and restart at a new random position on the left.
                      particle.onanimationend = () => {
                          // Remove state class and animation properties to reset
                          particle.classList.remove(newState);
                          particle.style.animation = 'none';
                          particle.style.transform = 'translate(0,0)'; // Reset transform

                          // Set new random starting position on the left
                           const randomY = 30 + Math.random() * (simulationArea.offsetHeight - 40);
                           particleData.left = -5 - Math.random() * 5; // Start slightly off screen left
                           particleData.bottom = randomY;
                           particle.style.left = `${particleData.left}%`;
                           particle.style.bottom = `${particleData.bottom}px`;

                           // Re-add class to restart animation
                           void particle.offsetWidth; // Trigger reflow
                           particle.classList.add(newState);
                           particle.style.animationDuration = animationDuration; // Re-apply duration
                            particle.style.animationDelay = `-${Math.random() * (parseFloat(animationDuration) * 0.5)}s`; // Stagger restarts
                             if (newState === 'saltation') {
                                 const simulationWidth = simulationArea.offsetWidth;
                                 const jumpDistancePx = (windSpeed / maxWind) * (simulationWidth * 0.5) + 50;
                                 particle.style.setProperty('--jump-dist', `${jumpDistancePx}px`);
                             }
                           // No need to set onanimationend again, it's a property, not event listener
                      };
                 }
            } else {
                 // Ensure no animationend listener is active if stationary
                 particle.onanimationend = null;
            }

            // If state is creep, let's handle its continuous movement via JS position updates
            // This breaks the "animation only in CSS" rule slightly, but is needed for continuous creep
            // Or, define creep animation as infinite 0->100% horizontal movement and loop.
             // Let's stick to the simpler reset-on-end/offscreen approach for all.
             // Creep will also be a single segment animation covering some distance and restarting.
              if (newState === 'creep') {
                 particle.onanimationend = () => {
                      // Same reset logic as saltation/suspension
                      particle.classList.remove(newState);
                      particle.style.animation = 'none';
                      particle.style.transform = 'translate(0,0)';

                       const randomY = 30 + Math.random() * (simulationArea.offsetHeight - 40);
                       particleData.left = -5 - Math.random() * 5; // Start slightly off screen left
                       particleData.bottom = randomY;
                       particle.style.left = `${particleData.left}%`;
                       particle.style.bottom = `${particleData.bottom}px`;

                       void particle.offsetWidth;
                       particle.classList.add(newState);
                       particle.style.animationDuration = animationDuration;
                        particle.style.animationDelay = `-${Math.random() * (parseFloat(animationDuration) * 0.5)}s`;
                 };
              }

        });
    }

    // Update the saltation-anim keyframe to use --jump-dist CSS variable
    // Redefining CSS rules from JS is bad practice. The --jump-dist variable approach is better.
    // Need to make sure the CSS keyframe uses `var(--jump-dist)` correctly.
    // Let's adjust the saltation-anim keyframe above in the <style> block. (Done)

    // Initial setup
    createParticles();
    updateSimulation(); // Set initial state

    // Event listeners
    windSlider.addEventListener('input', updateSimulation);
    soilTypeRadios.forEach(radio => {
        radio.addEventListener('change', updateSimulation);
    });

    // Explanation toggle
    toggleButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleButton.textContent = isHidden ? 'הסתר הסבר' : 'קראו על מסע החול: הסבר מפורט';
    });

     // Initial call to set button text correctly if explanation is initially hidden
    toggleButton.textContent = explanationDiv.style.display === 'none' ? 'קראו על מסע החול: הסבר מפורט' : 'הסתר הסבר';


    // Add resize observer to potentially re-calculate jump distances if simulation area resizes
    const resizeObserver = new ResizeObserver(entries => {
        // Re-calculate jump distances based on new simulation area width
        // and re-apply animation durations/properties?
        // This is complex. For now, let's assume the area doesn't change much after load.
        // Or maybe just call updateSimulation() to re-evaluate?
        // Calling updateSimulation might be too heavy. Let's skip this for simplicity within constraints.
    });

    resizeObserver.observe(simulationArea);

</script>
```