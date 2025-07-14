---
title: "סוד הפניות החלקות: איך הדיפרנציאל מאפשר לגלגלים לרקוד במהירויות שונות"
english_slug: what-makes-wheels-spin-at-different-speeds-in-a-turn-meet-the-differential
category: "טכנולוגיה / הנדסת רכב"
tags: ["דיפרנציאל", "סרן", "רכב", "מכניקה", "הנדסה", "איך זה עובד"]
---
# סוד הפניות החלקות: איך הדיפרנציאל מאפשר לגלגלים לרקוד במהירויות שונות

תארו לעצמכם: אתם בפנייה חדה ברכב, והגלגלים שלכם עוברים מרחקים שונים לחלוטין - הגלגל החיצוני חייב להסתובב מהר יותר מהפנימי. איך הרכב מונע מהם להחליק, להתנגד זה לזה, או פשוט להיתקע? סוד הקסם טמון באחד המנגנונים הגאוניים ביותר בהנדסת רכב: הדיפרנציאל! צללו פנימה וגלו איך הרכיב הצנוע הזה מאפשר לרכב שלכם לנוע בצורה חלקה ויעילה.

<div id="differential-app">
    <div class="controls">
        <button id="straight-btn">🚗 נסיעה ישרה</button>
        <button id="turn-left-btn">🔄 פנייה שמאלה</button>
        <button id="turn-right-btn">🔄 פנייה ימינה</button>
    </div>

    <div class="simulation-area">
        <div class="road-stripe left"></div>
        <div class="road-stripe right"></div>

        <div class="axle-assembly">
             <div class="driveshaft"></div>
            <div class="differential-housing">
                <div class="differential-internal">
                    <div class="ring-gear"></div>
                    <div class="carrier">
                        <div class="satellite-pin sat-1"><div class="satellite-gear"></div></div>
                        <div class="satellite-pin sat-2"><div class="satellite-gear"></div></div>
                    </div>
                    <div class="axle-gear left"></div>
                    <div class="axle-gear right"></div>
                     <div class="pinion-gear"></div>
                </div>
            </div>
            <div class="axle left">
                <div class="wheel">
                    <div class="spoke spoke-1"></div>
                    <div class="spoke spoke-2"></div>
                </div>
            </div>
            <div class="axle right">
                <div class="wheel">
                    <div class="spoke spoke-1"></div>
                    <div class="spoke spoke-2"></div>
                </div>
            </div>
        </div>
    </div>
     <div class="indicators">
        <div class="speed-indicator left">גלגל שמאל: 0%</div>
        <div class="speed-indicator right">גלגל ימין: 0%</div>
        <div class="satellite-indicator">סאטליטים (יחסי למארז): 0%</div>
     </div>
</div>

<style>
/* General Styling & Colors */
:root {
    --primary-blue: #3498db;
    --dark-blue: #2980b9;
    --accent-red: #e74c3c;
    --dark-red: #c0392b;
    --gray-light: #ecf0f1;
    --gray-medium: #bdc3c7;
    --gray-dark: #7f8c8d;
    --metal-dark: #444;
    --metal-medium: #666;
    --metal-light: #a0a0a0;
    --shadow-color: rgba(0,0,0,0.3);
    --ground-color: #dfe6e9; /* Soothing light background */
}

#differential-app {
    font-family: 'Heebo', sans-serif; /* Or any other modern sans-serif */
    direction: rtl;
    text-align: center;
    padding: 20px;
    background: linear-gradient(to bottom right, #f0f4f7, #dcdde1); /* Subtle gradient background */
    border-radius: 12px;
    margin-bottom: 30px;
    box-shadow: 0 8px 16px var(--shadow-color);
    overflow: hidden;
    position: relative; /* For absolute positioning of some elements */
}

.controls {
    margin-bottom: 25px;
    display: flex;
    justify-content: center;
    gap: 15px; /* More distinct spacing */
}

.controls button {
    padding: 12px 25px;
    cursor: pointer;
    border: none; /* Remove default border */
    background-color: var(--primary-blue);
    color: white;
    border-radius: 25px; /* Pill shape buttons */
    font-size: 1.1rem;
    font-weight: bold;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

.controls button:hover {
    background-color: var(--dark-blue);
    transform: translateY(-2px);
}
.controls button:active {
    transform: translateY(0);
    box-shadow: 0 2px 4px rgba(0,0,0,0.2);
}

.simulation-area {
    position: relative;
    width: 100%;
    height: 300px; /* Increased height for visual space */
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: var(--ground-color);
    border-radius: 8px;
    box-shadow: inset 0 0 10px rgba(0,0,0,0.1);
    overflow: hidden; /* Keep elements within bounds */
}

/* Animated Road Stripes - Visual cue for movement */
.road-stripe {
    position: absolute;
    width: 80px; /* Width of the stripe */
    height: 100%;
    background-color: rgba(255, 255, 255, 0.4); /* Semi-transparent white */
    z-index: 1; /* Below the axle assembly */
}
.road-stripe.left { left: 10%; }
.road-stripe.right { right: 10%; }


.axle-assembly {
    position: relative;
    width: 95%; /* Wider */
    max-width: 700px; /* Limit max width */
    height: 100px; /* Visual thickness/area */
    display: grid;
    grid-template-columns: 1fr 150px 1fr; /* Left axle, Differential (wider), Right axle */
    align-items: center;
    gap: 10px;
    z-index: 2;
}

.driveshaft {
    position: absolute;
    width: 120px; /* Longer */
    height: 25px; /* Thicker */
    background-color: var(--metal-dark);
    left: 50%;
    top: calc(50% - 45px); /* Position further above diff */
    transform: translateX(-50%);
    transform-origin: right center;
    z-index: 1; /* Below most diff parts */
    border-radius: 0 8px 8px 0;
    box-shadow: inset 2px 2px 5px rgba(0,0,0,0.5);
}

.pinion-gear {
     position: absolute;
     width: 40px; /* Larger */
     height: 40px; /* Larger */
     background-color: var(--metal-dark);
     border-radius: 50%;
     top: calc(50% - 20px);
     /* Position near driveshaft end where it meshes with ring gear */
     right: calc(50% + 50px); /* Adjust based on ring gear size */
     z-index: 4;
     border: 3px solid var(--shadow-color);
     box-sizing: border-box;
}


.differential-housing {
    grid-column: 2;
    position: relative;
    width: 150px; /* Wider */
    height: 150px; /* Taller */
    background-color: var(--metal-light);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 3;
    box-shadow: 0 0 15px var(--shadow-color);
}

.differential-internal {
    position: absolute;
    width: 90%;
    height: 90%;
    border: 3px dashed rgba(0,0,0,0.1); /* Lighter dashed guide */
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    transform-style: preserve-3d; /* Needed for visual depth */
}

.ring-gear {
    position: absolute;
    width: 115%; /* Larger */
    height: 115%; /* Larger */
    border: 8px solid var(--metal-medium); /* Thicker border for teeth effect */
    border-radius: 50%;
    box-sizing: border-box;
    transform: rotateY(90deg); /* Represent ring gear orientation */
    background-color: var(--metal-dark);
    z-index: 2; /* Below carrier */
}

.carrier {
    position: absolute;
    width: 85%; /* Larger */
    height: 85%; /* Larger */
    border: 4px solid var(--gray-light); /* More prominent carrier frame */
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    transform-style: preserve-3d;
    background-color: rgba(var(--gray-medium), 0.3); /* Semi-transparent */
    z-index: 3; /* Between ring and satellites/axle gears */
}

.satellite-pin {
    position: absolute;
    width: 50%; /* Radius from center */
    height: 50%; /* Radius from center */
    transform-origin: 0% 0%; /* Rotate around carrier center */
    display: flex;
    align-items: center;
    justify-content: center;
    /* Add a subtle line for the pin */
    &::before {
        content: '';
        position: absolute;
        width: 4px;
        height: 30px; /* Visual pin length */
        background-color: var(--gray-dark);
        border-radius: 2px;
        transform: translate(calc(50% - 2px), calc(50% - 15px)) rotate(90deg); /* Center and align with satellite gear axis */
        z-index: 6; /* Above other parts */
    }
}
.satellite-pin.sat-1 { transform: rotate(45deg); }
.satellite-pin.sat-2 { transform: rotate(225deg); }

.satellite-gear {
    width: 45px; /* Larger */
    height: 45px; /* Larger */
    background-color: var(--accent-red);
    border-radius: 50%;
    position: absolute;
     /* Center within pin area */
    transform: translate(calc(50% - 22.5px), calc(50% - 22.5px));
    border: 3px solid var(--dark-red);
    box-sizing: border-box;
    z-index: 5; /* Above carrier, below axle gears */
}

.axle-gear {
    position: absolute;
    width: 60px; /* Larger */
    height: 60px; /* Larger */
    background-color: var(--primary-blue);
    border-radius: 50%;
    border: 3px solid var(--dark-blue);
    z-index: 4;
    box-sizing: border-box;
}
.axle-gear.left { left: 0; transform: translateX(-50%); }
.axle-gear.right { right: 0; transform: translateX(50%); }


.axle {
    width: 100%;
    height: 50px; /* Thicker */
    background-color: var(--metal-medium);
    position: relative;
    z-index: 1;
    border-radius: 8px;
    box-shadow: inset 0 0 5px var(--shadow-color);
}

.wheel {
    position: absolute;
    width: 100px; /* Larger wheels */
    height: 100px; /* Larger wheels */
    background-color: var(--metal-dark);
    border-radius: 50%;
    border: 8px solid #222; /* Thicker border */
    box-sizing: border-box;
    top: 50%;
    transform: translateY(-50%);
    z-index: 5;
    color: #eee;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.8rem;
    overflow: hidden;
    box-shadow: 0 4px 10px var(--shadow-color);
}
.axle.left .wheel { left: 0; transform: translate(-50%, -50%); }
.axle.right .wheel { right: 0; transform: translate(50%, -50%); }

/* Wheel Spokes for clearer rotation */
.wheel .spoke {
    position: absolute;
    width: 4px;
    height: 50%;
    background-color: var(--gray-medium);
    transform-origin: bottom center;
    border-radius: 2px;
}
.wheel .spoke-1 { transform: translateY(-50%) rotate(0deg); }
.wheel .spoke-2 { transform: translateY(-50%) rotate(90deg); }


/* Indicators */
.indicators {
    margin-top: 20px;
    display: flex;
    justify-content: center;
    gap: 20px;
    font-weight: bold;
    font-size: 0.95rem;
    color: #333;
}
.speed-indicator { width: 150px; text-align: center; }
.satellite-indicator { width: 200px; text-align: center; }


/* Animation classes will be applied via JS */
/* Example: .rotating { animation: rotate 1s linear infinite; } */
@keyframes rotate {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}
/* Define rotation for elements */
.axle-assembly .rotating { animation: rotate linear infinite; }
.wheel .rotating { animation: rotate linear infinite; }
/* Gears need individual rotation applied via JS for variable speeds */

</style>

<button id="show-explanation-btn" style="margin-top: 30px; padding: 12px 25px; cursor: pointer; border: none; background-color: #2ecc71; color: white; border-radius: 25px; font-size: 1.1rem; font-weight: bold; transition: background-color 0.3s ease, transform 0.1s ease; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">הצג הסבר מורחב</button>

<div id="explanation" style="display: none; margin-top: 30px; padding: 20px; border: 1px solid #dcdde1; background-color: #f8f9fa; border-radius: 10px; text-align: right; line-height: 1.7;">
    <h2>הסבר מורחב: האמנות שבחלוקת כוח</h2>

    <h3>האתגר המכני: למה ציר ישר פשוט לא עובד בפנייה?</h3>
    <p>דמיינו שהגלגלים המונעים ברכב שלכם היו מחוברים לציר ברזל קשיח. בנסיעה ישרה, הכול מושלם – שניהם מסתובבים באותה מהירות ועוברים מרחק זהה. הבעיה מתחילה ברגע שאתם פונים. בפנייה, הגלגל בצד החיצוני של העיקול חייב לגלגל קשת גדולה יותר מאשר הגלגל הפנימי, ובאותו זמן! ציר קשיח היה מכריח את שניהם להסתובב בדיוק באותה מהירות. התוצאה? הגלגל הפנימי היה נגרר או מחליק, הגלגל החיצוני היה נאבק להתקדם מהר מספיק, הצמיגים היו נשחקים במהירות הבזק, וכל פנייה הייתה הופכת לחוויה קופצנית ולא יציבה, עם סיכון אמיתי לאבד שליטה.</p>

    <h3>הפתרון האלגנטי: הצגת הגאון הקטן, הדיפרנציאל</h3>
    <p>כדי לרקוד בין הצורך להניע את שני הגלגלים לבין הצורך לאפשר להם מהירויות סיבוב שונות, נדרש מנגנון מתוחכם שיודע לחלק את הכוח מהמנוע (המומנט), אבל בו זמנית להיות מספיק "גמיש" כדי לאפשר את הפרש המהירויות הזה. בדיוק בשביל זה הומצא הדיפרנציאל – רכיב מכני גאוני הממוקם בדרך כלל בין הגלגלים המונעים (קדמיים או אחוריים, או שניהם ברכב 4X4).</p>

    <h3>צוללים פנימה: מבנה של דיפרנציאל פתוח טיפוסי</h3>
    <p>הדיפרנציאל הנפוץ ביותר ברכבי נוסעים הוא הדיפרנציאל הפתוח. בואו נפשט את החלקים העיקריים שפועלים בו בהרמוניה:</p>
    <ul>
        <li><strong>גלגל הפיניון (Pinion Gear):</strong> מקבל את הכוח המסתובב מציר ההינע הראשי (שמגיע מתיבת ההילוכים). הוא קטן ובעל שיניים קשות.</li>
        <li><strong>גלגל הטבעת (Ring Gear):</strong> גלגל שיניים גדול, המחובר למארז הדיפרנציאל. הפיניון משתלב איתו ומסובב אותו (ולכן את המארז כולו). זהו השער הראשי לכוח מהמנוע אל הדיפרנציאל.</li>
        <li><strong>מארז הדיפרנציאל (Differential Carrier):</strong> מעין "סל" או קופסה חלולה המסתובבת במהירות גלגל הטבעת. בתוך המארז הזה, מותקנים על צירים קטנים...</li>
        <li><strong>גלגלי הסאטליט (Satellite / Pinion Gears):</strong> לרוב זוג או רביעיית גלגלי שיניים קטנים. הם יושבים בתוך המארז וממשקים (מתחברים) עם שני גלגלי השיניים שנמצאים משני צידי המארז...</li>
        <li><strong>גלגלי הציר (Axle / Side Gears):</strong> שני גלגלי שיניים אלו מחוברים ישירות לציריי ההינע המובילים אל הגלגלים המונעים (אחד לגלגל שמאל, אחד לגלגל ימין).</li>
    </ul>

    <h3>המופע המכני: מה קורה בנסיעה ישרה?</h3>
    <p>כאשר הרכב נוסע בקו ישר, שני הגלגלים פוגשים התנגדות דומה והם נדרשים להסתובב באותה מהירות. ציר ההינע מסובב את הפיניון, שמסובב את גלגל הטבעת, שמסובב את מארז הדיפרנציאל. מאחר שגלגלי הציר (המחוברים לגלגלים) מסתובבים באותה מהירות, גלגלי הסאטליט *אינם* מסתובבים על הצירים הקטנים שלהם בתוך המארז. הם נשארים "קפואים" יחסית למארז, ופשוט מסיעים את שני גלגלי הציר (והגלגלים) באותה מהירות סיבוב כמו המארז. הכוח מתחלק שווה בשווה (50/50) בין שני הצירים.</p>

    <h3>האקשן האמיתי: מה קורה בפנייה?</h3>
    <p>זה הרגע שבו הדיפרנציאל באמת זוהר. בפנייה, הגלגל הפנימי "מאט" קלות, מכיוון שהוא עובר מסלול קצר יותר. האטה זו גורמת לגלגל הציר המחובר אליו להסתובב לאט יותר מאשר המארז. ההפרש הזה גורם לגלגלי הסאטליט, שנמצאים בממשק בין המארז לגלגלי הציר, להתחיל להסתובב *על צירם* בתוך המארז. הסיבוב הנוסף הזה של הסאטליטים לא רק מפצה על ההאטה של הגלגל הפנימי, אלא גם מוסיף מהירות סיבוב לגלגל הציר השני – זה המחובר לגלגל החיצוני (שזקוק למהירות גבוהה יותר). למעשה, גלגלי הסאטליט פועלים כמו מתווכים חכמים, "גונבים" את המהירות העודפת מהצד האיטי ומעבירים אותה לצד המהיר, כל זאת תוך שמירה על חלוקת כוח שווה (שוויון המומנט) בין שני הצדדים. מארז הדיפרנציאל עצמו תמיד מסתובב במהירות שהיא הממוצע המדויק של מהירויות שני גלגלי הציר.</p>

    <h3>הצד הפחות זוהר: מה קורה כשאחד הגלגלים מאבד אחיזה?</h3>
    <p>היופי של הדיפרנציאל הפתוח הוא גם נקודת התורפה שלו. הוא תמיד מנסה לשלוח מומנט (כוח) שווה לשני הגלגלים. מומנט נשלח כשיש התנגדות. אם גלגל אחד מאבד אחיזה (על קרח, בוץ, או באוויר), הוא כמעט ולא נתקל בהתנגדות. מאחר שהדיפרנציאל מחלק את המומנט שווה בשווה, הוא שולח לשני הגלגלים רק את מעט המומנט הנדרש כדי לסובב את הגלגל המאבד אחיזה בחופשיות. הגלגל עם האחיזה נותר ללא כוח מספיק כדי להניע את הרכב, והגלגל המאבד אחיזה יסתובב במהירות כפולה ממהירות המארז (ובערך פי שניים ממהירות הגלגל התקוע). זה הרגע המכני שבו רכב עם דיפרנציאל פתוח "נתקע" כשגלגל אחד על משטח חלק – כל הכוח "בורח" לגלגל ללא האחיזה. זהו החיסרון העיקרי של דיפרנציאל פתוח בתנאים קשים, והוא שהוביל לפיתוח דיפרנציאלים מוגבלי החלקה או ננעלים ברכבי שטח ורכבי ביצועים.</p>

    <h3>לסיכום: מהפכה גאונית בפשטותה</h3>
    <p>הדיפרנציאל הפתוח הוא פלא של הנדסה מכנית. הוא מאפשר לרכבים להתנהג בצורה צפויה, חלקה ובטוחה בפניות, תוך שהוא מפשט את מערכת ההינע ומוזיל את הייצור. הבנת פעולתו היא אבן יסוד בהבנת האופן שבו כלי הרכב שאנו לוקחים כמובן מאליו פשוט עובדים.</p>
</div>

<script>
// Get elements
const driveshaft = document.querySelector('.driveshaft');
const ringGear = document.querySelector('.ring-gear');
const carrier = document.querySelector('.carrier');
const satelliteGears = document.querySelectorAll('.satellite-gear');
const axleGearLeft = document.querySelector('.axle-gear.left');
const axleGearRight = document.querySelector('.axle-gear.right');
const wheelLeft = document.querySelector('.axle.left .wheel');
const wheelRight = document.querySelector('.axle.right .wheel');
const speedIndicatorLeft = document.querySelector('.speed-indicator.left');
const speedIndicatorRight = document.querySelector('.speed-indicator.right');
const satelliteIndicator = document.querySelector('.satellite-indicator');
const roadStripes = document.querySelectorAll('.road-stripe');


const straightBtn = document.getElementById('straight-btn');
const turnLeftBtn = document.getElementById('turn-left-btn');
const turnRightBtn = document.getElementById('turn-right-btn');

const showExplanationBtn = document.getElementById('show-explanation-btn');
const explanationDiv = document.getElementById('explanation');

let animationFrameId = null;
let lastTime = performance.now(); // Initialize lastTime
const baseSpeed = 180; // degrees per second for carrier in straight mode
const turnRatio = 1.5; // Outer wheel is 1.5x faster than carrier speed, inner is 0.5x

let carrierAngle = 0;
let wheelLeftAngle = 0;
let wheelRightAngle = 0;
let satelliteRelativeAngle = 0; // Accumulated relative rotation of satellite on its pin

let currentMode = 'straight'; // 'straight', 'turn-left', 'turn-right'
let animationSpeeds = {
    carrier: baseSpeed,
    leftWheel: baseSpeed,
    rightWheel: baseSpeed,
    satelliteRelative: 0
};

// Function to update simulation speeds based on mode
function setModeSpeeds(mode) {
    if (mode === 'straight') {
        animationSpeeds.leftWheel = baseSpeed;
        animationSpeeds.rightWheel = baseSpeed;
        animationSpeeds.carrier = baseSpeed;
        animationSpeeds.satelliteRelative = 0;
    } else if (mode === 'turn-left') {
        // Left wheel inner (slower), Right wheel outer (faster)
        animationSpeeds.carrier = baseSpeed; // Carrier speed can be thought of as average speed
        animationSpeeds.rightWheel = baseSpeed * turnRatio;
        animationSpeeds.leftWheel = baseSpeed * (2 - turnRatio); // Maintain average: (S_L + S_R) / 2 = S_C
        animationSpeeds.satelliteRelative = (animationSpeeds.rightWheel - animationSpeeds.leftWheel) / 2; // Speed difference divided by 2
    } else if (mode === 'turn-right') {
        // Right wheel inner (slower), Left wheel outer (faster)
        animationSpeeds.carrier = baseSpeed;
        animationSpeeds.leftWheel = baseSpeed * turnRatio;
        animationSpeeds.rightWheel = baseSpeed * (2 - turnRatio);
        animationSpeeds.satelliteRelative = (animationSpeeds.rightWheel - animationSpeeds.leftWheel) / 2; // Speed difference divided by 2
    }
    currentMode = mode;
    lastTime = performance.now(); // Reset timer to prevent jump on mode change
}


function updateSimulation(deltaTime) {
    const deltaSeconds = deltaTime / 1000;

    // Update angles based on current animationSpeeds
    carrierAngle = (carrierAngle + animationSpeeds.carrier * deltaSeconds);
    wheelLeftAngle = (wheelLeftAngle + animationSpeeds.leftWheel * deltaSeconds);
    wheelRightAngle = (wheelRightAngle + animationSpeeds.rightWheel * deltaSeconds);
    satelliteRelativeAngle = (satelliteRelativeAngle + animationSpeeds.satelliteRelative * deltaSeconds);

    // Ensure angles stay within a manageable range (e.g., 0-360 or -inf to +inf)
    // Continuous angle accumulation is fine for rotation transforms

    // Apply transforms
    // Carrier rotates around its central axis (perpendicular to screen)
    carrier.style.transform = `rotate(${carrierAngle}deg)`;
    // Ring gear also rotates with the carrier (simplified visual)
    ringGear.style.transform = `rotateY(90deg) rotate(${carrierAngle * 0.5}deg)`; // Ring gear ratio ~2:1 to carrier
     // Driveshaft/Pinion rotate based on carrier speed (simplified 2:1 ratio for visual effect)
    driveshaft.style.transform = `translateX(-50%) translateY(-45px) rotate(${carrierAngle * 2}deg)`;
     // Pinion gear rotates with driveshaft
    document.querySelector('.pinion-gear').style.transform = `rotate(${carrierAngle * 2}deg)`;


    // Wheels and Axle gears rotate around their own axis
    wheelLeft.style.transform = `translate(-50%, -50%) rotate(${wheelLeftAngle}deg)`;
    wheelRight.style.transform = `translate(50%, -50%) rotate(${wheelRightAngle}deg)`;
    axleGearLeft.style.transform = `translateX(-50%) rotate(${wheelLeftAngle}deg)`;
    axleGearRight.style.transform = `translateX(50%) rotate(${wheelRightAngle}deg)`;


    // Satellite gears rotate *relatively* on their pins *within* the carrier's rotation
    // The satellite-pin elements are positioned within the carrier and inherit its rotation implicitly.
    // The satellite gear element needs to rotate *relative* to its pin.
    // We apply the accumulated relative rotation to the satellite gear element itself.
    satelliteGears.forEach(gear => {
         // Apply the accumulated relative rotation on the satellite's local axis
         // Use translate to maintain position within pin area, then rotate
         gear.style.transform = `translate(calc(50% - 22.5px), calc(50% - 22.5px)) rotate(${satelliteRelativeAngle}deg)`;
     });

     // Animate road stripes
     const roadSpeedMultiplier = 0.5; // Road stripes move slower than wheels
     if (currentMode === 'straight') {
         roadStripes.forEach(stripe => stripe.style.transform = `translateY(${(wheelLeftAngle * roadSpeedMultiplier) % 200}px)`); /* Loop effect */
     } else if (currentMode === 'turn-left') {
          roadStripes[0].style.transform = `translateY(${(wheelLeftAngle * roadSpeedMultiplier) % 200}px)`;
          roadStripes[1].style.transform = `translateY(${(wheelRightAngle * roadSpeedMultiplier) % 200}px)`;
     } else if (currentMode === 'turn-right') {
         roadStripes[0].style.transform = `translateY(${(wheelLeftAngle * roadSpeedMultiplier) % 200}px)`;
          roadStripes[1].style.transform = `translateY(${(wheelRightAngle * roadSpeedMultiplier) % 200}px)`;
     }


    // Update speed indicators
    const maxSpeed = Math.max(animationSpeeds.leftWheel, animationSpeeds.rightWheel, animationSpeeds.carrier); // Use max possible speed for percentage base
    const percentageLeft = maxSpeed > 0 ? Math.round((animationSpeeds.leftWheel / maxSpeed) * 100) : 0;
    const percentageRight = maxSpeed > 0 ? Math.round((animationSpeeds.rightWheel / maxSpeed) * 100) : 0;
    // Satellite relative speed percentage: relative speed / (max possible relative speed)
    // Max relative speed occurs during a turn: (Outer - Inner) / 2 = (baseSpeed * 0.5 - baseSpeed * 1.5) / 2 = baseSpeed * (-0.5)
    // Max absolute relative speed is baseSpeed * 0.5
    const maxRelativeSpeed = baseSpeed * (turnRatio - (2 - turnRatio)) / 2 ; // simplified (1.5 - 0.5)/2 * baseSpeed = 0.5 * baseSpeed
    const percentageSatellite = maxRelativeSpeed > 0 ? Math.round((Math.abs(animationSpeeds.satelliteRelative) / maxRelativeSpeed) * 100) : 0;


    speedIndicatorLeft.textContent = `גלגל שמאל: ${percentageLeft}%`;
    speedIndicatorRight.textContent = `גלגל ימין: ${percentageRight}%`;
    satelliteIndicator.textContent = `סאטליטים (יחסי למארז): ${percentageSatellite}%`;

}

function animate(currentTime) {
    const deltaTime = currentTime - lastTime;
    lastTime = currentTime;

    updateSimulation(deltaTime);

    animationFrameId = requestAnimationFrame(animate);
}

// Initial state setup
setModeSpeeds('straight');
animate(performance.now()); // Start the initial animation loop

// Event listeners
straightBtn.addEventListener('click', () => setModeSpeeds('straight'));
turnLeftBtn.addEventListener('click', () => setModeSpeeds('turn-left'));
turnRightBtn.addEventListener('click', () => setModeSpeeds('turn-right'));

showExplanationBtn.addEventListener('click', () => {
    const isHidden = explanationDiv.style.display === 'none';
    explanationDiv.style.display = isHidden ? 'block' : 'none';
    showExplanationBtn.textContent = isHidden ? 'הסתר הסבר' : 'הצג הסבר מורחב';
});

// Optional: Stop animation if element is off-screen for performance
// (requires IntersectionObserver, maybe overkill for this exercise)
</script>