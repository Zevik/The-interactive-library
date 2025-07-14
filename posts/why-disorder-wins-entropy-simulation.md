---
title: "למה הבלגן מנצח? סימולציה של אנטרופיה"
english_slug: why-disorder-wins-entropy-simulation
category: "מדעים מדויקים / פיזיקה"
tags:
  - אנטרופיה
  - תרמודינמיקה
  - פיזיקה סטטיסטית
  - סדר ואי-סדר
  - החוק השני של התרמודינמיקה
---
# למה הבלגן מנצח? סימולציה של אנטרופיה

האם שמתם לב שבלגן נוצר 'מעצמו' בקלות, בעוד שסדר דורש מאמץ אדיר? מדוע כוס קפה חמה מתקררת תמיד, ולעולם לא מתחממת מעצמה בחדר קר? נראה שיש "כוח" נסתר בטבע שדוחף את הדברים לכיוון מסוים... בואו נחקור את התעלומה הזו בעזרת סימולציה פשוטה של חלקיקים בכלי.

<div class="simulation-area">
    <div class="simulation-container">
        <div id="vessel" class="vessel">
            <div id="partition" class="partition"></div>
            <div id="particles" class="particles-container">
                <!-- Particles will be added here by JavaScript -->
            </div>
        </div>
        <div class="simulation-controls">
            <button id="removePartitionButton" class="control-button primary-button">הסר את המחיצה וצפה מה קורה!</button>
            <button id="restartSimulationButton" class="control-button secondary-button">התחל מחדש</button>
        </div>
        <div id="distribution-status" class="distribution-status">
            <span id="leftCount"></span>
            <span id="statusText"></span>
            <span id="rightCount"></span>
        </div>
    </div>

    <button id="toggleExplanationButton" class="explanation-toggle-button">🤔 מה בדיוק ראיתי? הצג הסבר על אנטרופיה 🤔</button>

    <div id="explanation" class="explanation-content explanation-hidden">
        <h2>הסבר: אנטרופיה, אי-סדר והסתברות</h2>
        <p>התופעה שצפיתם בה בסימולציה היא המחשה ויזואלית לאחד המושגים הבסיסיים והחזקים ביותר בפיזיקה – **אנטרופיה**.</p>

        <h3>אנטרופיה: מדד לאי-סדר או למגוון?</h3>
        <p>אנטרופיה היא מדד לכמה "דרכים" יש למערכת להיות במצב מסוים. היא לא רק "בלגן", אלא מספר הדרכים האפשריות לסדר את החלקיקים המיקרוסקופיים במערכת כדי לקבל את התמונה המאקרוסקופית שאנו רואים.</p>

        <h3>מדוע 'אי-סדר' בעצם 'מנצח'? עניין של סטטיסטיקה גרידא!</h3>
        <p>דמיינו שיש לכם מטבע אחד. יש 2 מצבים אפשריים (עץ/פלי). דמיינו שני מטבעות. יש 4 מצבים (עץ-עץ, עץ-פלי, פלי-עץ, פלי-פלי). דמיינו 100 מטבעות! יש מספר אסטרונומי של מצבים אפשריים. מה המצב הכי סביר? לא שכולם יהיו 'עץ' (יש רק דרך אחת כזו). המצב הכי סביר הוא שיהיו בערך 50 'עץ' ו-50 'פלי' – כי יש **הרבה יותר** דרכים לקבל את המצב הזה (הבלתי מסודר והמעורב) מאשר את המצב שבו כולם אותו דבר (המסודר).</p>
        <p>זה בדיוק מה שקורה עם החלקיקים בסימולציה: מצב שבו כל החלקיקים נמצאים בצד אחד הוא מצב מאוד "מיוחד" ובעל מעט סידורים אפשריים ברמה המיקרוסקופית (אנטרופיה נמוכה). מצב שבו החלקיקים מפוזרים באופן אחיד בכל הכלי הוא מצב "רגיל" וניתן להשיגו בהמון המון דרכים שונות (אנטרופיה גבוהה). כשהסרתם את המחיצה, החלקיקים פשוט הסתובבו באקראי, וכמו שהמטבעות "שואפים" להגיע למצב הכי סביר סטטיסטית (בערך 50/50), כך החלקיקים התפזרו לכיוון המצב הסביר ביותר – הפיזור האחיד והבלתי סדור.</p>

        <h3>הקשר לחוק השני של התרמודינמיקה</h3>
        <p>עקרון האנטרופיה מנוסח בחוק השני של התרמודינמיקה, שאומר שבמערכת סגורה (שאינה מחליפה חומר או אנרגיה עם הסביבה), האנטרופיה תמיד שואפת לגדול או להישאר קבועה. היא לעולם לא תקטן מעצמה. זהו אחד החוקים היסודיים והמשמעותיים ביותר בטבע, שמסביר מדוע תהליכים רבים הם בלתי הפיכים בזמן.</p>

        <h3>אנטרופיה בחיי היום-יום: דוגמאות</h3>
        <ul>
            <li>**התקררות וחימום:** חום עובר מגוף חם לקר, כי פיזור שווה יותר של אנרגיה קינטית בין כל החלקיקים במערכת הוא מצב סביר יותר (אנטרופיה גבוהה) מאשר ריכוז האנרגיה במקום אחד (אנטרופיה נמוכה).</li>
            <li>**התמוססות סוכר בתה:** מולקולות הסוכר והתה מתערבבות כי יש אינסוף כמעט דרכים למקם אותן מעורבבות, לעומת מעט דרכים למקם אותן נפרדות (הסוכר בתחתית הכוס).</li>
            <li>**החדר שלכם:** הרבה יותר דרכים "לבנות" חדר מבולגן מאשר חדר מסודר. כל פעולה אקראית (כמו הנחת ספר בכל מקום) מגדילה את האנטרויות האפשריות של המערכת, דוחפת אותה לכיוון הבלגן.</li>
        </ul>
        <p>אז בפעם הבאה שהחדר יתלכלך מעצמו, זכרו: זה לא אתם עצלנים, זו פשוט האנטרופיה עושה את שלה – דוחפת את העולם לכיוון המצב הסביר ביותר מבחינה סטטיסטית!</p>
    </div>
</div>


<style>
/* גופנים בסיסיים ותיקונים כלליים */
body {
    font-family: 'Arial', sans-serif; /* גופן נקי ומודרני */
    line-height: 1.6;
    color: #333; /* צבע טקסט כללי כהה אך לא שחור מוחלט */
    background-color: #f4f7f6; /* רקע בהיר ונעים */
    padding: 20px;
}

h1, h2, h3 {
    color: #004085; /* כותרות בצבע כחול עמוק */
    margin-bottom: 15px;
    font-weight: bold;
}

h1 { font-size: 2em; }
h2 { font-size: 1.5em; }
h3 { font-size: 1.2em; }

p {
    margin-bottom: 15px;
    font-size: 1.1em;
}

ul {
    margin-bottom: 15px;
    padding-left: 20px;
    list-style: disc outside; /* נקודות ברורות */
}

li {
    margin-bottom: 8px;
}

/* סגנון איזור הסימולציה */
.simulation-area {
    background-color: #ffffff; /* רקע לבן לאיזור הסימולציה */
    border: 1px solid #b8daff; /* גבול עדין בצבע בהיר */
    border-radius: 12px; /* פינות מעוגלות יותר */
    padding: 25px;
    margin: 20px auto; /* מרכוז עם שוליים */
    max-width: 600px; /* רוחב מירבי */
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); /* צל עדין להדגשה */
    text-align: center; /* מרכז את התוכן הפנימי */
}

.simulation-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 20px;
}

.vessel {
    width: 100%; /* התאמה לרוחב המקסימלי של ההורה */
    max-width: 500px; /* רוחב מירבי לכלי עצמו */
    aspect-ratio: 2.5 / 1; /* יחס גובה-רוחב */
    border: 3px solid #004085; /* גבול כהה יותר לכלי */
    position: relative;
    overflow: hidden; /* Hide particles outside */
    background-color: #e9ecef; /* רקע מעט אפור לכלי */
    margin-bottom: 15px;
    border-radius: 8px; /* פינות מעוגלות לכלי */
}

.partition {
    position: absolute;
    left: 50%; /* Start in the middle */
    top: 0;
    bottom: 0;
    width: 3px; /* עובי מחיצה */
    background-color: #dc3545; /* צבע אדום למחיצה */
    z-index: 2; /* Make sure partition is above particles initially */
    transition: all 0.5s ease-out; /* אנימציה להסרת המחיצה */
}

.partition.removed {
    left: -10px; /* הזז מחוץ למסך */
    opacity: 0; /* טשטש */
}

.particles-container {
    width: 100%;
    height: 100%;
    position: relative;
    /* לא להגדיר overflow: hidden כאן אלא על vessel */
}

.particle {
    position: absolute;
    width: 6px; /* גודל חלקיק מעט גדול יותר */
    height: 6px;
    background-color: #007bff; /* צבע כחול בולט לחלקיקים */
    border-radius: 50%;
    box-shadow: 0 0 3px rgba(0, 123, 255, 0.5); /* צל קטן לחלקיק */
    transition: background-color 0.1s ease; /* מעבר צבע קצר במקרה של התנגשות עתידית */
    /* הסרת ה-transition על all לטובת ביצועים */
}


/* סגנון כפתורים */
.control-button {
    padding: 12px 25px;
    font-size: 1.1em;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.1s ease;
    margin: 0 5px;
}

.primary-button {
    color: #fff;
    background-color: #28a745; /* כפתור ירוק ראשי */
}

.primary-button:hover {
    background-color: #218838;
    transform: translateY(-1px); /* אפקט ריחוף קל */
}

.primary-button:active {
     transform: translateY(0);
     background-color: #1e7e34;
}

.primary-button:disabled {
    background-color: #6c757d; /* אפור כאשר לא פעיל */
    cursor: default;
    transform: none;
}

.secondary-button {
    color: #004085; /* צבע כחול כהה לטקסט */
    background-color: #e9ecef; /* רקע אפור בהיר */
    border: 1px solid #004085; /* גבול תואם */
}

.secondary-button:hover {
    background-color: #d3d9df;
     transform: translateY(-1px); /* אפקט ריחוף קל */
}
.secondary-button:active {
     transform: translateY(0);
     background-color: #c8ced3;
}


/* סטטוס פיזור חלקיקים */
.distribution-status {
    margin-top: 15px;
    font-size: 1.1em;
    color: #555;
    min-height: 1.5em; /* שמור מקום לטקסט גם אם ריק */
}

#leftCount, #rightCount {
    font-weight: bold;
    color: #007bff; /* צבע החלקיקים */
}

#statusText {
    margin: 0 10px;
}


/* סגנון כפתור ההסבר */
.explanation-toggle-button {
     display: block; /* כפתור ברוחב מלא יחסית להורה */
     width: auto; /* רוחב אוטומטי בהתאם לתוכן, מרכוז על ידי margin auto בהורה */
     margin: 20px auto;
     padding: 12px 25px;
     font-size: 1.1em;
     color: #fff;
     background-color: #17a2b8; /* כפתור בצבע טורקיז */
     border: none;
     border-radius: 6px;
     cursor: pointer;
     transition: background-color 0.3s ease, transform 0.1s ease;
     text-align: center;
}

.explanation-toggle-button:hover {
    background-color: #138496;
    transform: translateY(-1px);
}
.explanation-toggle-button:active {
     transform: translateY(0);
     background-color: #117a8b;
}


/* סגנון איזור ההסבר */
.explanation-content {
    margin-top: 20px;
    padding: 25px;
    border: 1px solid #bee5eb; /* גבול עדין */
    border-radius: 12px;
    background-color: #e2f0fb; /* רקע כחול בהיר */
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    transition: all 0.4s ease-in-out; /* אנימציית מעבר להסבר */
}

.explanation-hidden {
    display: none;
    opacity: 0; /* התחל שקוף */
    transform: translateY(10px); /* התחל קצת למטה */
}

.explanation-content:not(.explanation-hidden) {
    display: block;
    opacity: 1; /* הופך שקוף לחלוטין */
    transform: translateY(0); /* עולה למקום */
}

/* אנימציה עדינה לכניסת חלקיקים? (אופציונלי ומורכב) */
/* במקום אנימציה מורכבת, נסתפק בתנועה רגילה */


/* רספונסיביות בסיסית */
@media (max-width: 600px) {
    .simulation-area {
        padding: 15px;
    }
    .vessel {
        width: 95%; /* יותר שוליים במסכים קטנים */
    }
    .control-button, .explanation-toggle-button {
        width: auto; /* יכולים להישאר inline-block */
        margin: 5px; /* מרווחים קטנים יותר בין כפתורים */
        padding: 10px 20px;
        font-size: 1em;
    }
    .simulation-controls {
        flex-direction: column; /* כפתורים אחד מתחת לשני */
        align-items: stretch;
    }
     .control-button {
         margin: 5px 0;
     }
}

</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const vessel = document.getElementById('vessel');
    const partition = document.getElementById('partition');
    const particlesContainer = document.getElementById('particles');
    const removePartitionButton = document.getElementById('removePartitionButton');
    const restartSimulationButton = document.getElementById('restartSimulationButton');
    const toggleExplanationButton = document.getElementById('toggleExplanationButton');
    const explanationDiv = document.getElementById('explanation');
    const leftCountSpan = document.getElementById('leftCount');
    const rightCountSpan = document.getElementById('rightCount');
    const statusTextSpan = document.getElementById('statusText');

    const numParticles = 200; // הגדלת מספר החלקיקים לאפקט ויזואלי טוב יותר
    const particleSize = 4; // גודל חלקיק מעט קטן יותר
    const maxSpeed = 2; // מהירות מירבית גבוהה יותר
    const boundaryMargin = particleSize / 2; // שוליים קטנים מגבול הכלי

    let particles = [];
    let animationFrameId;
    let partitionRemoved = false;
    let vesselWidth = vessel.clientWidth; // יקבע בהתחלה ובעת שינוי גודל
    let vesselHeight = vessel.clientHeight;
    let initialPartitionX = vesselWidth / 2;

    // פונקציה לעדכון מימדי הכלי (למקרה של שינוי גודל חלון)
    function updateVesselDimensions() {
         vesselWidth = vessel.clientWidth;
         vesselHeight = vessel.clientHeight;
         initialPartitionX = vesselWidth / 2;
          // עדכן גבולות התנגשות במידת הצורך (לא הכרחי כרגע כי הם דינמיים)
    }

    // פונקציה ליצירת חלקיק בודד
    function createParticle(x, y) {
        const particle = document.createElement('div');
        particle.classList.add('particle');
        particle.style.width = `${particleSize}px`;
        particle.style.height = `${particleSize}px`;
        particlesContainer.appendChild(particle);

        // מהירות התחלתית אקראית
        const angle = Math.random() * 2 * Math.PI;
        const speed = Math.random() * maxSpeed * 0.5 + maxSpeed * 0.5; // מהירות בין מחצית המהירות המירבית למירבית עצמה

        return {
            element: particle,
            x: x,
            y: y,
            vx: Math.cos(angle) * speed,
            vy: Math.sin(angle) * speed
        };
    }

    // אתחול חלקיקים בצד שמאל בלבד
    function initializeParticles() {
        // עצור אנימציה אם רצה
        if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
        }

        particlesContainer.innerHTML = ''; // נקה חלקיקים קיימים
        particles = [];
        partitionRemoved = false;

        // ודא שהמחיצה גלויה ובמקום
        partition.style.display = 'block';
        partition.classList.remove('removed'); // הסר קלאס אנימציה אם היה
        partition.style.left = '50%'; // ודא שהמחיצה בדיוק באמצע

        // ודא שהכפתור פעיל ועם הטקסט הנכון
        removePartitionButton.disabled = false;
        removePartitionButton.textContent = "הסר את המחיצה וצפה מה קורה!";
        removePartitionButton.style.backgroundColor = ''; // הסר צבע אפור

        // אתחל מוני חלקיקים
        updateCounts();


        updateVesselDimensions(); // עדכן מימדים לפני אתחול מיקום חלקיקים

        for (let i = 0; i < numParticles; i++) {
            // מקם באקראי בחצי השמאלי של הכלי, עם שוליים קטנים מהקירות והמחיצה
            const x = Math.random() * (initialPartitionX - particleSize * 2 - boundaryMargin * 2) + boundaryMargin;
            const y = Math.random() * (vesselHeight - particleSize * 2 - boundaryMargin * 2) + boundaryMargin;
            particles.push(createParticle(x, y));
        }
        renderParticles(); // הצגה ראשונית
        animate(); // התחל אנימציה מיד כדי להראות את התנועה בתוך הצד השמאלי
    }

    // רינדור מיקומי חלקיקים על המסך
    function renderParticles() {
        particles.forEach(p => {
            p.element.style.left = `${p.x}px`;
            p.element.style.top = `${p.y}px`;
        });
    }

    // פונקציה לעדכון מוני חלקיקים וסטטוס
    function updateCounts() {
        let leftCount = 0;
        let rightCount = 0;

        particles.forEach(p => {
             // חשב לפי מרכז החלקיק לעומת מרכז הכלי/מחיצה
             if (p.x + particleSize / 2 < vesselWidth / 2) {
                 leftCount++;
             } else {
                 rightCount++;
             }
        });

        leftCountSpan.textContent = `חלקיקים בשמאל: ${leftCount}`;
        rightCountSpan.textContent = `חלקיקים בימין: ${rightCount}`;

        // עדכן סטטוס טקסטואלי
        if (!partitionRemoved) {
             statusTextSpan.textContent = ' | ';
        } else {
             // חשב יחס
             const total = leftCount + rightCount;
             if (total === 0) {
                  statusTextSpan.textContent = ' | ';
                  return;
             }
             const leftRatio = leftCount / total;
             const rightRatio = rightCount / total;

             if (leftCount === total || rightCount === total) {
                  statusTextSpan.textContent = ' | מצב התחלתי/מאוד מסודר | ';
             } else if (leftRatio > 0.45 && leftRatio < 0.55) { // בערך 50/50
                  statusTextSpan.textContent = ' | מצב קרוב לשיווי משקל (בלגן מרבי) | ';
             } else if (leftRatio > 0.2 && leftRatio < 0.8) { // פיזור סביר
                 statusTextSpan.textContent = ' | מתפזרים... | ';
             } else { // עדיין מרוכזים יחסית
                 statusTextSpan.textContent = ' | פיזור התחלתי... | ';
             }
        }
    }


    // לולאת אנימציה
    function animate() {
        updateVesselDimensions(); // ודא מימדים מעודכנים לחישובי התנגשות

        particles.forEach(p => {
            // עדכון מיקום
            p.x += p.vx;
            p.y += p.vy;

            // טיפול בהתנגשויות עם הקירות (הקפצה)
            // קיר שמאל
            if (p.x < boundaryMargin) {
                p.x = boundaryMargin + (boundaryMargin - p.x); // תקן מיקום
                p.vx *= -1; // הפוך כיוון
            }
             // קיר ימין
            if (p.x > vesselWidth - particleSize - boundaryMargin) {
                p.x = vesselWidth - particleSize - boundaryMargin - (p.x - (vesselWidth - particleSize - boundaryMargin)); // תקן מיקום
                p.vx *= -1; // הפוך כיוון
            }
            // קיר עליון
            if (p.y < boundaryMargin) {
                p.y = boundaryMargin + (boundaryMargin - p.y); // תקן מיקום
                p.vy *= -1; // הפוך כיוון
            }
             // קיר תחתון
            if (p.y > vesselHeight - particleSize - boundaryMargin) {
                p.y = vesselHeight - particleSize - boundaryMargin - (p.y - (vesselHeight - particleSize - boundaryMargin)); // תקן מיקום
                p.vy *= -1; // הפוך כיוון
            }


            // טיפול בהתנגשות עם המחיצה אם היא קיימת
            if (!partitionRemoved) {
                // נבדוק התנגשות רק אם החלקיק קרוב לאיזור המחיצה
                 const partitionThreshold = initialPartitionX; // קו המחיצה האמצעי
                 const particleCenter = p.x + particleSize / 2;
                 const prevParticleCenter = (p.x - p.vx) + particleSize / 2;


                // התנגשות כשהחלקיק עובר מצד לצד את קו האמצע
                if (
                    // זז ימינה וחוצה את קו האמצע
                    p.vx > 0 && prevParticleCenter <= partitionThreshold && particleCenter > partitionThreshold
                    ||
                    // זז שמאלה וחוצה את קו האמצע
                    p.vx < 0 && prevParticleCenter >= partitionThreshold && particleCenter < partitionThreshold
                ) {
                     p.vx *= -1; // הפוך מהירות אופקית
                     // תקן מיקום כדי שלא יתקע במחיצה או יעבור אותה
                     if (p.vx > 0) { // החלקיק התקדם שמאלה והוקפץ ימינה
                          p.x = partitionThreshold + (partitionThreshold - particleCenter) - particleSize/2; // מיקום אחרי ההקפצה, מימין למחיצה
                     } else { // החלקיק התקדם ימינה והוקפץ שמאלה
                          p.x = partitionThreshold - (particleCenter - partitionThreshold) - particleSize/2; // מיקום אחרי ההקפצה, משמאל למחיצה
                     }
                }
            }
        });

        renderParticles(); // עדכן DOM
        updateCounts(); // עדכן מוני חלקיקים
        animationFrameId = requestAnimationFrame(animate); // המשך אנימציה
    }

    // אירוע לחיצה על כפתור הסרת המחיצה
    removePartitionButton.addEventListener('click', () => {
        if (!partitionRemoved) {
            partition.classList.add('removed'); // הפעל אנימציית הסרה
            // המחיצה תיעלם פיזית לאחר האנימציה (או מיידית, תלוי ב-CSS display)
            // כדי שההתנגשות תפסיק מיד:
            partitionRemoved = true;
            removePartitionButton.disabled = true;
            removePartitionButton.textContent = "המחיצה הוסרה";
            removePartitionButton.style.backgroundColor = "#6c757d";
            removePartitionButton.style.cursor = "default";

            // אם אנימציה עדיין לא רצה (לא אמור לקרות כי היא רצה מההתחלה), התחל אותה.
            if (!animationFrameId) {
                animate();
            }
        }
    });

     // אירוע לחיצה על כפתור התחלה מחדש
     restartSimulationButton.addEventListener('click', () => {
         initializeParticles(); // אתחל הכל מחדש
     });


    // אירוע לחיצה על כפתור הצגת/הסתרת הסבר
    toggleExplanationButton.addEventListener('click', () => {
        if (explanationDiv.classList.contains('explanation-hidden')) {
            explanationDiv.classList.remove('explanation-hidden');
            // הוספת דיליי קצר כדי שהאנימציה תיראה טוב יותר אחרי שה-display השתנה
            setTimeout(() => {
                 explanationDiv.style.opacity = '1';
                 explanationDiv.style.transform = 'translateY(0)';
            }, 10); // דיליי קצר ביותר
            toggleExplanationButton.textContent = 'בטל הסבר על אנטרופיה 👆'; // שינוי טקסט
            toggleExplanationButton.style.backgroundColor = '#dc3545'; // שינוי צבע לכפתור 'בטל'
        } else {
            explanationDiv.style.opacity = '0'; // התחל טשטוש
            explanationDiv.style.transform = 'translateY(10px)'; // התחל תנועה למטה
            // הסתר פיזית לאחר סיום האנימציה
            explanationDiv.addEventListener('transitionend', function handleTransitionEnd() {
                 explanationDiv.classList.add('explanation-hidden');
                 explanationDiv.removeEventListener('transitionend', handleTransitionEnd); // הסר את המאזין לאחר השימוש
            }, { once: true }); // ודא שהמאזין יופעל פעם אחת בלבד
            toggleExplanationButton.textContent = '🤔 מה בדיוק ראיתי? הצג הסבר על אנטרופיה 🤔'; // שינוי טקסט בחזרה
             toggleExplanationButton.style.backgroundColor = ''; // החזר צבע רגיל

        }
    });

    // אתחול ראשוני של הסימולציה
    initializeParticles();

    // הוספת מאזין לאירוע שינוי גודל חלון כדי לעדכן מימדים
    // window.addEventListener('resize', updateVesselDimensions); // זה יכול להיות יקר מבחינת ביצועים, נעדכן רק ב-animate loop.


});
</script>
```