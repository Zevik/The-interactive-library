---
title: "המרחב מתעקם: חוויית כוח המשיכה של איינשטיין"
english_slug: space-bends-einsteins-gravity-experience
category: "מדעים מדויקים / פיזיקה"
tags:
  - תורת היחסות הכללית
  - כוח משיכה
  - מרחב-זמן
  - פיזיקה
  - איינשטיין
  - סימולציה
  - אינטראקטיבי
---
<h1>כוח המשיכה: לא כוח, אלא עיקום של המרחב!</h1>

<p>נשמע מוזר, נכון? אנחנו רגילים לחשוב על כוח המשיכה כמשיכה בלתי נראית בין עצמים בעלי מסה. תפוח נופל ארצה כי כדור הארץ "מושך" אותו. הירח נשאר במסלולו כי כדור הארץ "מושך" אותו. אבל אלברט איינשטיין הציע רעיון מהפכני: מה אם כוח המשיכה הוא לא באמת 'כוח', אלא פשוט התוצאה של שינוי במרקם היסודי ביותר של היקום עצמו - המרחב-זמן?</p>

<p>ברוכים הבאים לסימולציה שמדגימה את הרעיון המרכזי בתורת היחסות הכללית: מסה ואנרגיה מעקמות את המרחב-זמן סביבן, וגופים אחרים נעים במסלולים המתאימים לעיקום הזה, כאילו הם מתגלגלים במורד "שקע" שנוצר. בואו נשחק!</p>

<div class="simulation-container">
    <canvas id="gravityCanvas"></canvas>
    <div class="controls">
        <label for="massSize">גודל והשפעת המסה:</label>
        <input type="range" id="massSize" min="30" max="150" value="70">
        <button id="addMassBtn" class="control-button">הוסף "כוכב" (לחץ בסימולציה)</button>
        <button id="addParticleBtn" class="control-button">שחרר חלקיק בוחן אקראי</button>
         <button id="addOrbitingParticleBtn" class="control-button">שחרר חלקיק במסלול</button>
        <button id="clearBtn" class="control-button">נקה הכל</button>
        <p class="tip">לחץ/גרור בסימולציה כדי להוסיף מסה או לשנות מיקום של "כוכב" קיים.</p>
         <p class="tip">לחץ בסימולציה (לא בזמן הוספת מסה) כדי לשחרר חלקיק בוחן במיקום ספציפי.</p>
    </div>
</div>

<button id="toggleExplanationBtn" class="explanation-button">הצג/הסתר מה באמת קורה כאן (הסבר מעמיק יותר)</button>

<div id="explanation" class="hidden explanation-box">
    <h2>כוח המשיכה: מהתיאוריה הניוטונית ליחסות הכללית</h2>

    <p>עוד מימי אייזק ניוטון, הסבר מקובל לכוח המשיכה היה ככוח משיכה מיידי הפועל בין כל שני גופים בעלי מסה. ככל שהמסות גדולות יותר והמרחק ביניהן קטן יותר, כך כוח המשיכה חזק יותר. מודל זה היה מוצלח להפליא בחיזוי תנועת כוכבי הלכת ותופעות כבידה רבות אחרות. אולם, הרעיון של 'פעולה מרחוק' - השפעה מיידית של גוף אחד על גוף אחר ללא מגע וללא מנגנון ברור - העלה אי-נוחות פילוסופית ומדעית. בנוסף, המודל הניוטוני לא התיישב היטב עם עקרונות תורת היחסות הפרטית של איינשטיין, שהראתה ששום דבר לא יכול לנוע מהר יותר מהאור, ובוודאי שלא השפעה כבידתית.</p>

    <h3>הצגת המרחב-זמן</h3>
    <p>אחת התובנות המרכזיות של איינשטיין בתורת היחסות הכללית היא איחוד המרחב והזמן למקשה אחת הנקראת "מרחב-זמן". במקום להתייחס למרחב ולזמן כאל שתי ישויות נפרדות ובלתי תלויות, היחסות הכללית רואה אותן כארבעה ממדים המשולבים יחדיו (שלושת ממדי המרחב וממד הזמן). איחוד זה חיוני להבנת האופן שבו כוח המשיכה פועל.</p>

    <h3>עקרון השקילות</h3>
    <p>עקרון השקילות, שהיווה נקודת מוצא חשובה לאיינשטיין, קובע שבהינתן סביבה מקומית קטנה מספיק, לא ניתן להבחין בין השפעת כוח משיכה לבין השפעת תאוצה. אדם בתוך מעלית שנופלת נפילה חופשית ירגיש חוסר משקל בדיוק כאילו הוא מרחף בחלל הרחק ממקורות כבידה. ולהפך, אדם בתוך מעלית המואצת כלפי מעלה בחלל ירגיש כוח הדומה לכוח המשיכה. עקרון זה מרמז על קשר עמוק בין כוח המשיכה לבין תנועה ותאוצה.</p>

    <h3>מסות מעקמות את המרחב-זמן</h3>
    <p>ההסבר המרכזי של תורת היחסות הכללית לכוח המשיכה שונה מהותית מהמודל הניוטוני. במקום לראות בכוח המשיכה משיכה ישירה בין מסות, איינשטיין הציע שנוכחות מסה ואנרגיה (שהן שקולות לפי E=mc²) 'מקערת' או מעקמת את המרחב-זמן סביבה. דמיינו בד גומי מתוח: הנחת כדור כבד במרכזו תגרום לשקע. באנלוגיה דו-ממדית זו, המסה היא הכדור, ובד הגומי הוא המרחב-זמן. הסימולציה למעלה מדגימה את זה באופן ויזואלי.</p>

    <h3>תנועה בעקבות העיקום: גיאודטיקות</h3>
    <p>כיצד משפיע עיקום המרחב-זמן על תנועת גופים אחרים? לפי היחסות הכללית, גופים הנעים במרחב-זמן מעוקל אינם נעים בהכרח בקו ישר במובן האוקלידי, אלא לאורך הנתיבים 'הישרים ביותר' האפשריים על פני המשטח המעוקל עצמו. נתיבים אלו נקראים גיאודטיקות. תנועה לאורך גיאודטיקה במרחב-זמן מעוקל היא למעשה מה שאנו חווים ומפרשים כ'נפילה' או 'משיכה כבידתית'. הסימולציה מדגימה אנלוגיה פשטנית לתהליך זה - חלקיקי בוחן נעים לעבר המסה לא בקו ישר על המישור השטוח, אלא "מתגלגלים" אל תוך השקע שיוצרת המסה ברשת המרחב-זמן המדומה, עוקבים אחר ה"מדרון".</p>

    <h3>כוח המשיכה כגאומטריה</h3>
    <p>לסיכום, תורת היחסות הכללית מגדירה מחדש את כוח המשיכה לא ככוח הפועל בין גופים, אלא כביטוי של הגאומטריה של המרחב-זמן עצמו. מסה ואנרגיה מכתיבות למרחב-זמן כיצד להתעקם, והמרחב-זמן המעוקל מכתיב לגופים כיצד לנוע. זוהי תפיסה מהפכנית ששינתה את האופן שבו אנו מבינים את היקום ואת האינטראקציות היסודיות שבו.</p>

    <h3>השלכות ותחזיות</h3>
    <p>תורת היחסות הכללית של איינשטיין לא רק סיפקה הסבר אלגנטי לכוח המשיכה, אלא גם חזתה מגוון תופעות שלא הוסברו במודל הניוטוני, ורבות מהן אושרו מאז בתצפיות וניסויים: עידוש כבידתי (כיצד אור מתכופף סביב מסות גדולות), התקדמות הפריהליון של כוכב חמה (סטייה קטנה במסלולו שלא הוסברה רק על ידי ניוטון), והקיום של גלי כבידה (אדוות במרחב-זמן הנוצרות על ידי אירועים קוסמיים אלימים כמו התנגשות חורים שחורים), שאותרו לראשונה באופן ישיר בשנת 2015.</p>
</div>

<style>
/* כללי */
body {
    font-family: 'Arial', sans-serif; /* פונט קריא ונעים */
    line-height: 1.7; /* מרווח שורות נוח */
    margin: 0; /* הסר מרווחים חיצוניים ברירת מחדל */
    padding: 20px; /* ריפוד פנימי */
    background-color: #f4f7f6; /* רקע בהיר ונעים */
    color: #333; /* צבע טקסט כהה */
    direction: rtl; /* יישור לימין */
    text-align: right; /* יישור טקסט לימין */
}

/* כותרות */
h1, h2, h3 {
    text-align: center; /* מרכז כותרות */
    color: #2c3e50; /* צבע כהה יותר לכותרות */
    margin-bottom: 15px;
}

h1 {
    color: #1a5276; /* גוון כחול עמוק יותר לכותרת ראשית */
    margin-top: 10px;
    margin-bottom: 20px;
}

h2 {
     border-bottom: 2px solid #bdc3c7; /* קו תחתון עדין */
     padding-bottom: 8px;
}

h3 {
    color: #3498db; /* כחול בהיר יותר */
    margin-top: 25px;
    margin-bottom: 10px;
}

p {
    margin-bottom: 15px;
}

/* קונטיינר הסימולציה */
.simulation-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 30px auto; /* מרכוז וריווח */
    padding: 20px;
    border: 1px solid #dcdcdc; /* גבול עדין */
    border-radius: 10px; /* פינות מעוגלות */
    background-color: #ffffff; /* רקע לבן לקונטיינר */
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* צל עדין */
    max-width: 850px; /* רוחב מרבי */
}

/* קנבס */
canvas {
    border: 1px solid #aed6f1; /* גבול בהיר */
    background: linear-gradient(to bottom right, #e0f7fa, #bbdefb); /* רקע גראדיאנט שמימי */
    cursor: pointer; /* סמן עכבר יד */
    margin-bottom: 20px;
    border-radius: 8px; /* פינות מעוגלות */
    box-shadow: inset 0 0 8px rgba(0,0,0,0.1); /* צל פנימי */
}

/* פקדים */
.controls {
    display: flex;
    flex-wrap: wrap; /* עטיפת פקדים לשורה חדשה אם אין מקום */
    justify-content: center; /* מרכוז פקדים */
    align-items: center;
    gap: 15px 20px; /* רווחים בין פקדים */
    width: 100%; /* רוחב מלא */
    padding: 10px 0;
    border-top: 1px solid #eee; /* קו הפרדה עדין */
    margin-top: 10px;
}

.controls label {
    font-weight: bold;
    color: #555;
    white-space: nowrap; /* למנוע שבירת שורה בכותרת של הסליידר */
}

.controls input[type="range"] {
    flex-grow: 1; /* התרחבות למקסימום רוחב אפשרי */
    max-width: 250px; /* הגבלת רוחב לסליידר */
    -webkit-appearance: none; /* הסתרת מראה ברירת מחדל */
    appearance: none;
    height: 8px;
    background: #ddd;
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
    width: 18px;
    height: 18px;
    background: #3498db;
    cursor: pointer;
    border-radius: 50%;
    border: 2px solid #fff;
    box-shadow: 0 1px 3px rgba(0,0,0,0.2);
}

.controls input[type="range"]::-moz-range-thumb {
    width: 18px;
    height: 18px;
    background: #3498db;
    cursor: pointer;
    border-radius: 50%;
    border: 2px solid #fff;
    box-shadow: 0 1px 3px rgba(0,0,0,0.2);
}


.control-button {
    padding: 10px 18px;
    background-color: #5dade2; /* כחול תכלת יפה */
    color: white;
    border: none;
    border-radius: 5px; /* פינות מעוגלות יותר */
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.1s ease;
    font-size: 1em;
    white-space: nowrap; /* למנוע שבירת שורה בכפתור */
}

.control-button:hover {
    background-color: #3498db; /* כחול כהה יותר בהום */
    transform: translateY(-2px); /* אפקט הרמה קל */
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

.control-button:active {
     background-color: #2980b9; /* כחול כהה בלחיצה */
     transform: translateY(0); /* החזרת האפקט */
     box-shadow: none;
}

#addMassBtn {
    background-color: #2ecc71; /* ירוק להוספה */
}

#addMassBtn:hover {
    background-color: #27ae60;
}
#addMassBtn:active {
    background-color: #229954;
}


#addMassBtn.adding {
    background-color: #e74c3c; /* אדום במצב הוספה */
    color: white;
}

#addMassBtn.adding:hover {
     background-color: #c0392b;
}


#clearBtn {
    background-color: #e74c3c; /* אדום לניקוי */
}

#clearBtn:hover {
    background-color: #c0392b;
}
#clearBtn:active {
    background-color: #a93226;
}


.controls .tip {
    width: 100%; /* רוחב מלא לטיפים */
    text-align: center;
    font-size: 0.9em;
    color: #7f8c8d; /* אפור עדין */
    margin-top: 5px;
}

/* כפתור הסבר */
.explanation-button {
    display: block; /* אלמנט בלוק */
    margin: 25px auto; /* מרכוז */
    padding: 12px 25px;
    background-color: #3498db; /* כחול ראשי */
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.1s ease;
    font-size: 1.1em;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

.explanation-button:hover {
    background-color: #2980b9;
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

.explanation-button:active {
    background-color: #2471a3;
    transform: translateY(0);
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}


/* תיבת הסבר */
.explanation-box {
    margin-top: 20px;
    padding: 20px;
    border: 1px solid #dcdcdc;
    border-radius: 10px;
    background-color: #f9f9f9; /* רקע בהיר יותר מהקונטיינר */
    max-width: 850px;
    margin-left: auto;
    margin-right: auto;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.explanation-box.hidden {
    display: none;
}

.explanation-box h2 {
    margin-top: 0;
    color: #2c3e50;
}

.explanation-box h3 {
    color: #3498db;
    margin-top: 20px;
}

.explanation-box p {
    margin-bottom: 15px;
    color: #555;
}

/* סמן עכבר להוספת מסה */
canvas.adding-mass {
    cursor: crosshair;
}

/* סמן עכבר לגרירת מסה */
canvas.dragging-mass {
    cursor: grabbing;
}

/* סמן עכבר לשחרור חלקיק */
canvas.adding-particle {
     cursor: crosshair; /* או סמן אחר */
}


</style>

<script>
const canvas = document.getElementById('gravityCanvas');
const ctx = canvas.getContext('2d');
const massSizeSlider = document.getElementById('massSize');
const addMassBtn = document.getElementById('addMassBtn');
const addParticleBtn = document.getElementById('addParticleBtn');
const addOrbitingParticleBtn = document.getElementById('addOrbitingParticleBtn');
const clearBtn = document.getElementById('clearBtn');
const explanationDiv = document.getElementById('explanation');
const toggleExplanationBtn = document.getElementById('toggleExplanationBtn');

// Define canvas size - make it responsive if needed, but fixed size is simpler for this sim
canvas.width = 700;
canvas.height = 500;

const GRID_SPACING = 25; // Spacing between grid points
const GRID_POINT_RADIUS = 1.8; // Size of grid points
const PARTICLE_RADIUS = 3.5; // Size of test particles
const PARTICLE_COLOR = '#f39c12'; // Orange/Gold
const MASS_COLOR = '#34495e'; // Dark blue/grey
const GRID_COLOR = '#aed6f1'; // Light grid lines/points
const BEND_STRENGTH_FACTOR = 600; // Controls how much the grid visually bends
const GRAVITY_ACCELERATION_FACTOR = 5; // Controls how strongly particles are accelerated by the 'slope'
const DAMPING_FACTOR = 0.995; // Slightly slow down particles each frame
const MIN_DIST_SQ_MASS = 2000; // Minimum distance squared for bend calculation to avoid singularity
const PARTICLE_TRAIL_LENGTH = 30; // How many previous positions to store for the trail

let masses = [];
let particles = [];
let isAddingMass = false;
let isAddingParticle = false;
let draggingMassIndex = -1; // -1 if not dragging, index of mass if dragging

// --- Physics Simulation Functions ---

// Represents a mass object (star/planet)
class Mass {
    constructor(x, y, size) {
        this.x = x;
        this.y = y;
        this.size = size; // Visual size
        this.gravityEffect = size * size * 0.005; // Effect strength based on size squared for more impact
    }

    draw(ctx) {
        // Draw the "dent" effect using a radial gradient
        const gradient = ctx.createRadialGradient(this.x, this.y, 0, this.x, this.y, this.size * 2);
        gradient.addColorStop(0, `rgba(52, 73, 94, 0.8)`); // Darker, more opaque center
        gradient.addColorStop(0.4, `rgba(52, 73, 94, 0.4)`); // Lighter, more transparent mid
        gradient.addColorStop(1, `rgba(52, 73, 94, 0)`); // Fully transparent outer

        ctx.fillStyle = gradient;
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size * 2, 0, Math.PI * 2);
        ctx.fill();

        // Draw the mass itself
        ctx.fillStyle = MASS_COLOR;
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fill();

        // Optional: Add a subtle glow or outline
        // ctx.strokeStyle = MASS_COLOR + 'aa';
        // ctx.lineWidth = 2;
        // ctx.beginPath();
        // ctx.arc(this.x, this.y, this.size + 2, 0, Math.PI * 2);
        // ctx.stroke();
    }
}

// Represents a test particle (like a probe or light ray)
class Particle {
    constructor(x, y, vx = 0, vy = 0) {
        this.x = x;
        this.y = y;
        this.vx = vx;
        this.vy = vy;
        this.trail = []; // Store past positions for trail
    }

    update() {
        // Store current position for the trail
        this.trail.push({ x: this.x, y: this.y });
        if (this.trail.length > PARTICLE_TRAIL_LENGTH) {
            this.trail.shift(); // Remove the oldest position
        }

        let totalAx = 0;
        let totalAy = 0;

        const epsilon = GRID_SPACING * 0.1; // Small offset for gradient calculation

        // Calculate the "bend" function value at a given point (x, y)
        // This function determines the "height" of the simulated curved surface
        const getBendHeight = (px, py) => {
            let height = 0;
            for (const mass of masses) {
                const dx = px - mass.x;
                const dy = py - mass.y;
                const distSq = dx * dx + dy * dy;
                // Use a smooth falloff function for the bend
                height += mass.gravityEffect / (distSq / BEND_STRENGTH_FACTOR + 1);
            }
            return height;
        };


        // Calculate acceleration based on the gradient (slope) of the bend height
        // Particle is accelerated "downhill"
        const bendHere = getBendHeight(this.x, this.y);
        const bendRight = getBendHeight(this.x + epsilon, this.y);
        const bendLeft = getBendHeight(this.x - epsilon, this.y);
        const bendDown = getBendHeight(this.x, this.y + epsilon);
        const bendUp = getBendHeight(this.x, this.y - epsilon);

        // Approximate partial derivatives (slope)
        const dBend_dx = (bendRight - bendLeft) / (2 * epsilon);
        const dBend_dy = (bendDown - bendUp) / (2 * epsilon);

        // Acceleration is proportional to the negative gradient (downhill)
        totalAx = -dBend_dx * GRAVITY_ACCELERATION_FACTOR;
        totalAy = -dBend_dy * GRAVITY_ACCELERATION_FACTOR;


        // Update velocity
        this.vx += totalAx;
        this.vy += totalAy;

        // Apply damping
        this.vx *= DAMPING_FACTOR;
        this.vy *= DAMPING_FACTOR;

        // Update position
        this.x += this.vx;
        this.y += this.vy;

        // Boundary checks: Wrap around the edges for continuous simulation
        if (this.x < 0) this.x = canvas.width;
        if (this.x > canvas.width) this.x = 0;
        if (this.y < 0) this.y = canvas.height;
        if (this.y > canvas.height) this.y = 0;

        return true; // Particle is always alive with wrap-around
    }

    draw(ctx) {
        // Draw the trail
        ctx.strokeStyle = PARTICLE_COLOR + '88'; // Semi-transparent trail
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        if (this.trail.length > 1) {
            ctx.moveTo(this.trail[0].x, this.trail[0].y);
            for (let i = 1; i < this.trail.length; i++) {
                // Gradient opacity for trail fade
                const opacity = i / this.trail.length;
                 ctx.strokeStyle = PARTICLE_COLOR + Math.floor(opacity * 255).toString(16).padStart(2, '0');
                ctx.lineTo(this.trail[i].x, this.trail[i].y);
            }
             ctx.stroke();
        }


        // Draw the particle itself
        ctx.fillStyle = PARTICLE_COLOR;
        ctx.beginPath();
        ctx.arc(this.x, this.y, PARTICLE_RADIUS, 0, Math.PI * 2);
        ctx.fill();
    }
}


// --- Drawing Functions ---

function drawGrid(ctx, masses) {
    ctx.fillStyle = GRID_COLOR; // For points

    // Calculate the bend height for a grid point (px, py)
    const getBendHeight = (px, py) => {
        let height = 0;
        for (const mass of masses) {
            const dx = px - mass.x;
            const dy = py - mass.y;
            const distSq = dx * dx + dy * dy;
            // Use a smooth falloff function for the visual bend depth
            height += mass.gravityEffect / (distSq / BEND_STRENGTH_FACTOR + 1);
        }
        return height;
    };

    // Draw grid points at their displaced position
    for (let x = GRID_SPACING; x < canvas.width; x += GRID_SPACING) {
        for (let y = GRID_SPACING; y < canvas.height; y += GRID_SPACING) {
            // The "displacement" is the simulated bend height
            // We visualize this as a 'downward' shift in the Y direction for simplicity
            const displacementY = getBendHeight(x, y);

            ctx.beginPath();
            // Draw the point at its original X but displaced Y position
            ctx.arc(x, y + displacementY, GRID_POINT_RADIUS, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    // Note: Drawing connecting lines between displaced points (a mesh) is significantly more complex
    // and often requires triangulating the surface, which is beyond a simple canvas example.
    // Drawing displaced points provides a visual analogy of the bending.
}

function draw() {
    // Clear canvas with background gradient
    const bgGradient = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
    bgGradient.addColorStop(0, '#e0f7fa');
    bgGradient.addColorStop(1, '#bbdefb');
    ctx.fillStyle = bgGradient;
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Draw the grid points (simulating the bend visually)
    drawGrid(ctx, masses);

    // Draw the masses and their 'dents'
    for (const mass of masses) {
        mass.draw(ctx);
    }

    // Draw the particles
    for (const particle of particles) {
        particle.draw(ctx);
    }
}

// --- Animation Loop ---

function update() {
    // Update particle positions
    particles = particles.filter(particle => particle.update()); // Particle update returns true/false (though with wrap-around, always true now)

    draw(); // Redraw everything
    requestAnimationFrame(update); // Loop the update and draw function
}

// --- Helper Functions ---

// Get mouse position relative to the canvas
function getMousePos(canvas, event) {
    const rect = canvas.getBoundingClientRect();
    return {
        x: event.clientX - rect.left,
        y: event.clientY - rect.top
    };
}

// --- Event Listeners ---

// Handle click on canvas
canvas.addEventListener('click', (event) => {
    const pos = getMousePos(canvas, event);

    if (isAddingMass) {
        const size = parseInt(massSizeSlider.value);
        masses.push(new Mass(pos.x, pos.y, size));
        isAddingMass = false; // Reset flag
        addMassBtn.textContent = 'הוסף "כוכב" (לחץ בסימולציה)'; // Reset button text
        addMassBtn.classList.remove('adding');
        canvas.classList.remove('adding-mass');
        canvas.style.cursor = 'pointer'; // Reset cursor
    } else if (!isAddingParticle && draggingMassIndex === -1) {
        // If not adding mass and not dragging, add a particle on click
        // Give it a small random initial velocity
        const vx = (Math.random() - 0.5) * 6;
        const vy = (Math.random() - 0.5) * 6;
        particles.push(new Particle(pos.x, pos.y, vx, vy));
         canvas.classList.remove('adding-particle'); // Just in case
         canvas.style.cursor = 'pointer';
    } else if (isAddingParticle) {
         // This state is currently only for the button, not canvas click
         // but keeping this branch allows future expansion if needed.
          canvas.classList.remove('adding-particle');
          canvas.style.cursor = 'pointer';
    }
});

// Handle mouse down for dragging or potentially adding particle via drag/release (future)
canvas.addEventListener('mousedown', (event) => {
     if (isAddingMass) return; // Don't drag if adding new mass

    const pos = getMousePos(canvas, event);

    // Check if clicking on an existing mass
    for(let i = 0; i < masses.length; i++) {
        const mass = masses[i];
        const dx = pos.x - mass.x;
        const dy = pos.y - mass.y;
        const dist = Math.sqrt(dx*dx + dy*dy);

        if (dist < mass.size) { // Clicked inside the mass circle
            draggingMassIndex = i;
            canvas.classList.add('dragging-mass');
            break; // Stop checking after finding the first mass
        }
    }
});

// Handle mouse move for dragging or cursor feedback
canvas.addEventListener('mousemove', (event) => {
    const pos = getMousePos(canvas, event);

    if (draggingMassIndex !== -1) {
        // Update position of the dragged mass
        masses[draggingMassIndex].x = pos.x;
        masses[draggingMassIndex].y = pos.y;
    } else if (isAddingMass) {
         canvas.classList.add('adding-mass');
         canvas.classList.remove('dragging-mass', 'adding-particle');
    } else {
         // Default cursor when not doing anything special
         canvas.classList.remove('adding-mass', 'dragging-mass', 'adding-particle');
         canvas.style.cursor = 'pointer';
    }
});

// Handle mouse up for dragging
canvas.addEventListener('mouseup', (event) => {
    if (draggingMassIndex !== -1) {
        draggingMassIndex = -1; // Stop dragging
        canvas.classList.remove('dragging-mass');
        canvas.style.cursor = 'pointer'; // Reset cursor
    }
     if (isAddingParticle) {
        // This could be used for a "drag to launch particle" feature
        // For now, the button just adds a random particle.
         isAddingParticle = false;
         canvas.classList.remove('adding-particle');
         canvas.style.cursor = 'pointer';
     }
});

// Prevent dragging mass if mouse leaves canvas while dragging
canvas.addEventListener('mouseleave', (event) => {
     if (draggingMassIndex !== -1) {
        draggingMassIndex = -1;
        canvas.classList.remove('dragging-mass');
         canvas.style.cursor = 'pointer';
     }
     if (isAddingMass) {
        // Keep adding mass cursor if mouse leaves and re-enters
     } else {
          canvas.classList.remove('adding-mass', 'dragging-mass', 'adding-particle');
          canvas.style.cursor = 'pointer';
     }
});


addMassBtn.addEventListener('click', () => {
    isAddingMass = !isAddingMass; // Toggle add mass mode
    isAddingParticle = false; // Turn off particle add mode
    if (isAddingMass) {
        addMassBtn.textContent = 'בטל הוספת "כוכב"';
        addMassBtn.classList.add('adding');
        canvas.classList.add('adding-mass');
         canvas.classList.remove('adding-particle');
    } else {
        addMassBtn.textContent = 'הוסף "כוכב" (לחץ בסימולציה)';
        addMassBtn.classList.remove('adding');
         canvas.classList.remove('adding-mass');
    }
    draggingMassIndex = -1; // Ensure dragging is off
     canvas.classList.remove('dragging-mass'); // Visual cue clean up
});

addParticleBtn.addEventListener('click', () => {
    // Add particles from a random point with some random velocity
    const x = Math.random() * canvas.width;
    const y = Math.random() * canvas.height;
    // Give them a small initial velocity
    const vx = (Math.random() - 0.5) * 8; // Increased initial speed
    const vy = (Math.random() - 0.5) * 8; // Increased initial speed
    particles.push(new Particle(x, y, vx, vy));

    // Ensure adding mass/particle mode is off for button click
    isAddingMass = false;
    addMassBtn.textContent = 'הוסף "כוכב" (לחץ בסימולציה)';
    addMassBtn.classList.remove('adding');
    isAddingParticle = false; // Button just adds one particle
    canvas.classList.remove('adding-mass', 'adding-particle');
     canvas.style.cursor = 'pointer';
     draggingMassIndex = -1;

});

addOrbitingParticleBtn.addEventListener('click', () => {
    // Attempt to add a particle in a somewhat stable orbit if a mass exists
    if (masses.length === 0) {
        alert('הוסף "כוכב" קודם!');
        return;
    }

    const mass = masses[0]; // Orbit around the first mass for simplicity
    const radius = mass.size * 3 + Math.random() * mass.size * 2; // Orbit distance relative to mass size
    const angle = Math.random() * Math.PI * 2; // Random starting angle

    const startX = mass.x + radius * Math.cos(angle);
    const startY = mass.y + radius * Math.sin(angle);

    // Calculate initial velocity for a circular orbit analog
    // This is a simplified model, not true orbital mechanics on curved space-time
    // We estimate the required tangential velocity to counteract the "pull"
    const bendHeightAtRadius = (px, py) => {
         let height = 0;
            for (const m of masses) { // Use m to avoid conflict with 'mass' variable
                const dx = px - m.x;
                const dy = py - m.y;
                const distSq = dx * dx + dy * dy;
                height += m.gravityEffect / (distSq / BEND_STRENGTH_FACTOR + 1);
            }
            return height;
    };

    // Estimate the "downhill" acceleration towards the mass at this radius
    const epsilon = GRID_SPACING * 0.1;
    const bendRight = bendHeightAtRadius(startX + epsilon, startY);
    const bendLeft = bendHeightAtRadius(startX - epsilon, startY);
    const bendDown = bendHeightAtRadius(startX, startY + epsilon);
    const bendUp = bendHeightAtRadius(startX, startY - epsilon);

    const estimatedAx = -((bendRight - bendLeft) / (2 * epsilon)) * GRAVITY_ACCELERATION_FACTOR;
    const estimatedAy = -((bendDown - bendUp) / (2 * epsilon)) * GRAVITY_ACCELERATION_FACTOR;

    const gravityMagnitude = Math.sqrt(estimatedAx * estimatedAx + estimatedAy * estimatedAy);

    // In circular motion, a = v^2 / r. So v = sqrt(a * r)
    let orbitalSpeed = 0;
     if (radius > 0) {
          orbitalSpeed = Math.sqrt(gravityMagnitude * radius) * 0.8; // Adjust factor for stability (0.8-1.2 often works)
     }


    // Velocity vector should be tangential to the circle around the mass
    // Tangential vector is perpendicular to the radial vector (startX - mass.x, startY - mass.y)
    const radialX = startX - mass.x;
    const radialY = startY - mass.y;

    // Perpendicular vector options: (-radialY, radialX) or (radialY, -radialX)
    // Choose one based on desired orbit direction (e.g., counter-clockwise)
    const tangentialX = -radialY;
    const tangentialY = radialX;

    // Normalize tangential vector and scale by orbital speed
    const tangentialMag = Math.sqrt(tangentialX * tangentialX + tangentialY * tangentialY);
    let vx = 0, vy = 0;
    if (tangentialMag > 0) {
         vx = (tangentialX / tangentialMag) * orbitalSpeed;
         vy = (tangentialY / tangentialMag) * orbitalSpeed;
    }


    particles.push(new Particle(startX, startY, vx, vy));

     // Ensure adding mass/particle mode is off
    isAddingMass = false;
    addMassBtn.textContent = 'הוסף "כוכב" (לחץ בסימולציה)';
    addMassBtn.classList.remove('adding');
    isAddingParticle = false;
    canvas.classList.remove('adding-mass', 'adding-particle');
     canvas.style.cursor = 'pointer';
     draggingMassIndex = -1;
});


clearBtn.addEventListener('click', () => {
    masses = [];
    particles = [];
    // Reset add mass mode if active
    isAddingMass = false;
    addMassBtn.textContent = 'הוסף "כוכב" (לחץ בסימולציה)';
    addMassBtn.classList.remove('adding');
    isAddingParticle = false;
    canvas.classList.remove('adding-mass', 'adding-particle');
    canvas.style.cursor = 'pointer';
    draggingMassIndex = -1;
    canvas.classList.remove('dragging-mass');
});

toggleExplanationBtn.addEventListener('click', () => {
    explanationDiv.classList.toggle('hidden');
    if (explanationDiv.classList.contains('hidden')) {
        toggleExplanationBtn.textContent = 'הצג מה באמת קורה כאן (הסבר מעמיק יותר)';
    } else {
        toggleExplanationBtn.textContent = 'הסתר הסבר';
    }
});

// Initial state setup
toggleExplanationBtn.textContent = 'הצג מה באמת קורה כאן (הסבר מעמיק יותר)';
explanationDiv.classList.add('hidden'); // Ensure it's hidden by default

// Start the animation loop
update();

</script>
---