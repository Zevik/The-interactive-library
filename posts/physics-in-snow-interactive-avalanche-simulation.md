---
title: "פיזיקה בשלג: סימולציית מפולות אינטראקטיבית"
english_slug: physics-in-snow-interactive-avalanche-simulation
category: "פיזיקה"
tags:
  - מפולת שלג
  - פיזיקה
  - סימולציה
  - כוחות
  - מדרון
  - חיכוך
  - יציבות
---
<h1>פיזיקה בשלג: סימולציית מפולות אינטראקטיבית</h1>

<p>האם אי פעם תהיתם מה גורם למדרונות שלג עצומים להתנתק ולהתדרדר בכוח אדיר? האם מסת השלג לבדה קובעת את גורלו, או שישנם כוחות נסתרים ומשוואות פיזיקליות המשפיעות על רגע האמת? בסימולציה זו, תוכלו לחקור בעצמכם את האיזון העדין בין הכוחות הפועלים על שכבת שלג במדרון ולהבין מתי הוא נשבר.</p>

<div class="simulation-container">
    <div class="controls">
        <div class="control-group">
            <label for="angle-slider">זווית המדרון:</label>
            <input type="range" id="angle-slider" min="15" max="55" value="30">
            <span id="angle-value">30°</span>
        </div>
        <div class="control-group">
            <label for="snow-type-select">סוג השלג:</label>
            <select id="snow-type-select">
                <option value="powder">שלג טרי ואוורירי</option>
                <option value="packed">שלג דחוס וישן</option>
                <option value="wet">שלג רטוב וכבד</option>
            </select>
        </div>
        <button id="run-simulation-button">הפעל סימולציה</button>
    </div>

    <div class="simulation-area">
        <div class="mountain-bg"></div>
        <div class="ground"></div>
        <div class="slope">
            <div class="snow-mass"></div>
        </div>
        <div class="result-display"></div>
    </div>
    <button id="reset-button" class="control-button">אפס סימולציה</button>
</div>

<button id="toggle-explanation" class="control-button toggle-explanation-button">הצג/הסתר הסבר פיזיקלי</button>

<div id="explanation" style="display: none;">
    <h2>מאחורי הקלעים: פיזיקה של מפולות שלג</h2>
    <p>מפולות שלג הן דוגמה מרתקת לכשל מכני בקנה מידה גדול, הנשלט על ידי עקרונות פיזיקליים בסיסיים. בבסיסה, מפולת מתרחשת כאשר הכוחות הדוחפים את השלג למטה גוברים על הכוחות המייצבים המחזיקים אותו במקומו.</p>

    <h3>מאזן הכוחות הקריטי</h3>
    <p>חשבו על גוש השלג בסימולציה. שני כוחות עיקריים נאבקים על גורלו:</p>
    <ul>
        <li><strong>כוח הכבידה (מושך למטה):</strong> כוח הכבידה תמיד מושך את המסה כלפי מרכז כדור הארץ. במדרון, כוח זה מתפרק לשני רכיבים: אחד פועל בניצב למדרון (הנורמל) ואחד פועל במקביל למדרון, מושך את השלג כלפי מטה. ככל שהמדרון תלול יותר (זווית גדולה יותר), רכיב הכוח המושך כלפי מטה גדל משמעותית. בסימולציה, אתם שולטים ישירות על עוצמת הכוח הזה דרך שינוי זווית המדרון.</li>
        <li><strong>כוחות התנגדות (מייצבים):</strong> אלו הכוחות הנלחמים בכוח הכבידה ומנסים לשמור על השלג במקומו. הם כוללים בעיקר:
            <ul>
                <li><strong>חיכוך:</strong> ההתנגדות לתנועה בין שכבות השלג לבין עצמן ובין השלג לקרקע שמתחתיו.</li>
                <li><strong>לכידות (קוהזיה):</strong> המידה שבה גבישי השלג "נדבקים" זה לזה.</li>
            </ul>
            סוג השלג משפיע דרמטית על כוחות ההתנגדות. שלג טרי אוורירי פחות דחוס ובעל לכידות נמוכה יחסית, ולכן פחות יציב. שלג ישן או רטוב יכול להיות בעל לכידות גבוהה יותר, אך מים יכולים גם להקטין חיכוך בתנאים מסוימים (בסימולציה, פישטנו זאת כך שסוג השלג משפיע על "גורם ההתנגדות" הכולל).</li>
        </ul>

    <h3>מתי מתרחשת מפולת?</h3>
    <p>מפולת מתחילה כאשר רכיב כוח הכבידה המושך במורד המדרון גובר על סך כוחות ההתנגדות (חיכוך ולכידות). בנקודה זו, המאזן נשבר, ויציבות השלג קורסת. הסימולציה ממחישה את הרגע הקריטי הזה ואת תפקיד זווית המדרון וסוג השלג בקביעתו.</p>

    <h3>מעבר לסימולציה...</h3>
    <p>במציאות, גורמים נוספים רבים משפיעים על סיכון המפולת: עומס שלג חדש על שכבות קודמות, שינויי טמפרטורה המשפיעים על לכידות השלג, נוכחות שכבות חלשות בתוך עומק השלג, רעידות אדמה, ואפילו עומס קטן נקודתי כמו משקל של אדם או בעל חיים. הבנת הפיזיקה הבסיסית המוצגת כאן היא הצעד הראשון להבנת התופעה המורכבת הזו.</p>
</div>

<style>
/* כללי */
.simulation-container {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    border: 1px solid #d3d3d3; /* גבול עדין */
    padding: 25px;
    margin-bottom: 30px;
    background-color: #f4f7f6; /* רקע בהיר נעים */
    border-radius: 12px; /* פינות מעוגלות יותר */
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08); /* צל עדין */
    max-width: 800px; /* רוחב מקסימלי לנוחות קריאה */
    margin-left: auto;
    margin-right: auto;
    position: relative; /* מאפשר מיקום אבסולוטי בתוכו */
}

.controls {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    margin-bottom: 30px;
    align-items: center;
    justify-content: center; /* ממורכז */
}

.control-group {
    display: flex;
    align-items: center;
    gap: 12px; /* רווח גדול יותר */
    flex-grow: 1;
    min-width: 220px; /* מינימום רוחב */
    background-color: #ffffff; /* רקע לבן לקבוצה */
    padding: 12px 15px;
    border-radius: 8px;
    border: 1px solid #e0e0e0;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

.control-group label {
    font-weight: bold;
    color: #333;
    white-space: nowrap; /* למנוע מעבר שורה בתווית */
}

.control-group input[type="range"] {
    flex-grow: 1;
    /* הסתרת סליידר מקורי ועיצוב מחדש (מורכב, נשאיר כרגע ברירת מחדל מעוצבת) */
    -webkit-appearance: none;
    appearance: none;
    height: 8px;
    background: linear-gradient(to right, #a0c4ff, #4285F4); /* צבעים רעננים */
    outline: none;
    opacity: 0.8;
    transition: opacity .2s;
    border-radius: 4px;
}

.control-group input[type="range"]:hover {
    opacity: 1;
}

.control-group input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 20px;
    height: 20px;
    background: #007bff; /* כחול עז */
    cursor: pointer;
    border-radius: 50%; /* עגול */
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.2);
}

.control-group input[type="range"]::-moz-range-thumb {
    width: 20px;
    height: 20px;
    background: #007bff;
    cursor: pointer;
    border-radius: 50%;
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.2);
}

.control-group select {
     flex-grow: 1;
     padding: 8px;
     border-radius: 4px;
     border: 1px solid #ccc;
     background-color: #f9f9f9;
     cursor: pointer;
     font-size: 1em;
}

.control-group span {
    font-weight: bold;
    color: #007bff; /* כחול כמו הכפתור */
    min-width: 30px; /* לוודא שיש מקום למעל 50 מעלות */
    text-align: right;
}

/* כפתורים כלליים */
.control-button {
    padding: 10px 20px;
    font-size: 1em;
    cursor: pointer;
    border: none;
    border-radius: 5px;
    transition: background-color 0.3s ease, transform 0.1s ease;
    font-weight: bold;
    margin-top: 15px; /* רווח מעל הכפתורים התחתונים */
}

#run-simulation-button {
    background-color: #28a745; /* ירוק */
    color: white;
    flex-shrink: 0;
    min-width: 150px; /* רוחב מינימלי */
}

#run-simulation-button:hover {
    background-color: #218838;
    transform: translateY(-1px); /* אפקט הרמה קל */
}

#run-simulation-button:active {
     transform: translateY(0); /* לחיצה */
}

#reset-button {
    display: block; /* שורה חדשה */
    margin: 15px auto 0; /* ממורכז למטה */
    background-color: #ffc107; /* צהוב/כתום */
    color: #333;
}

#reset-button:hover {
     background-color: #e0a800;
     transform: translateY(-1px);
}
#reset-button:active {
     transform: translateY(0);
}

.toggle-explanation-button {
    display: block;
    margin: 20px auto; /* ממורכז מתחת לקונטיינר */
    background-color: #e9ecef; /* אפור בהיר */
    color: #333;
    border: 1px solid #ced4da;
}

.toggle-explanation-button:hover {
     background-color: #dee2e6;
     transform: translateY(-1px);
}
.toggle-explanation-button:active {
     transform: translateY(0);
}

/* אזור הסימולציה הויזואלי */
.simulation-area {
    position: relative;
    width: 100%;
    height: 300px; /* גובה גדול יותר */
    overflow: hidden;
    margin-top: 20px;
    background: linear-gradient(to bottom, #b0e0e6, #e0f6ff); /* שמיים בהירים */
    border-radius: 8px;
    border: 1px solid #a0c0e0;
    box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.1); /* צל פנימי עדין */
}

.mountain-bg {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: url('https://via.placeholder.com/800x300?text=Mountain+Background') no-repeat center bottom; /* תמונה גנרית של הר */
    background-size: cover;
    z-index: 0; /* מתחת לכל השאר */
    opacity: 0.5; /* שקיפות קלה */
    filter: brightness(1.2) grayscale(0.1); /* בהירות קלה וקצת פחות רוויה */
}

.ground {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 60px; /* גובה קרקע */
    background: linear-gradient(to bottom, #a0522d, #8b4513); /* גווני חום טבעיים */
    z-index: 1;
}

.slope {
    position: absolute;
    bottom: 60px; /* מעל הקרקע */
    left: -50%; /* מתחיל משמאל מחוץ למסך כדי לאפשר סיבוב רחב */
    width: 200%; /* רחב מספיק לסיבוב */
    height: 400px; /* גבוה מספיק */
    background: linear-gradient(to bottom, #f8f8f8, #ffffff); /* גווני שלג בהירים */
    transform-origin: 50% 100%; /* סובב מהנקודה התחתונה המרכזית (היכן שפוגש את הקרקע) */
    transform: rotate(0deg); /* בסיס סיבוב */
    z-index: 2;
    /* border-bottom: 2px solid #ccc; קו מפגש, פחות נחוץ עם רקע הר */
    box-shadow: inset 0 5px 10px rgba(0,0,0,0.1); /* צל פנימי קטן לדגש מדרון */
}

.snow-mass {
    position: absolute;
    top: 50px; /* התחל מעט למטה מהקצה העליון של המדרון הויזואלי */
    left: 80px; /* התחל משמאל */
    width: 100px; /* גודל גוש השלג */
    height: 60px;
    background-color: #ffffff; /* לבן טהור */
    border-radius: 10px; /* פינות מעוגלות למראה רך יותר */
    box-shadow: 0 3px 8px rgba(0,0,0,0.3); /* צל בולט יותר */
    z-index: 3;
    /* תונטרל באמצעות JS */
    transition: transform 0s ease-out; /* ברירת מחדל: ללא אנימציה */
}

/* אנימציית מפולת */
.snow-mass.slide {
     transition: transform 2s ease-in; /* אנימציה מהירה ואגרסיבית יותר */
     /* ה-transform עצמו נקבע ב-JS */
}

/* אנימציית רעידה */
@keyframes shake {
  0%, 100% { transform: translateX(0); }
  10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
  20%, 40%, 60%, 80% { transform: translateX(5px); }
}

.slope.shaking {
    animation: shake 0.5s infinite ease-in-out; /* רעידה מתמשכת קלה */
}

.snow-mass.shaking {
     animation: shake 0.3s infinite ease-in-out; /* רעידה מהירה יותר לגוש השלג */
}


.result-display {
    position: absolute;
    top: 15px;
    right: 15px;
    background-color: rgba(255, 255, 255, 0.95); /* רקע כמעט אטום */
    padding: 12px;
    border-radius: 8px;
    font-weight: bold;
    z-index: 10;
    min-width: 180px; /* רוחב מינימלי */
    text-align: center;
    border: 1px solid #ccc;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    opacity: 0; /* נסתר בהתחלה */
    transition: opacity 0.5s ease-in-out; /* אנימציית הופעה */
}

.result-display.show {
    opacity: 1;
}

.result-display.success {
    color: #28a745; /* ירוק ליציב */
}

.result-display.failure {
    color: #dc3545; /* אדום למפולת */
}


/* הסבר פיזיקלי */
#explanation {
    border: 1px solid #d3d3d3;
    padding: 25px;
    margin-top: 30px;
    background-color: #f9f9f9;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    max-width: 800px; /* רוחב מקסימלי */
    margin-left: auto;
    margin-right: auto;
}

#explanation h2, #explanation h3 {
    color: #333;
    margin-bottom: 15px;
    padding-bottom: 5px;
    border-bottom: 1px solid #eee;
}

#explanation h2 {
    text-align: center;
    border-bottom: 2px solid #ddd;
    padding-bottom: 10px;
}

#explanation p {
    line-height: 1.6;
    color: #555;
    margin-bottom: 15px;
}

#explanation ul {
    margin-top: 15px;
    margin-bottom: 15px;
    padding-left: 20px;
    color: #555;
}

#explanation li {
    margin-bottom: 10px;
    line-height: 1.5;
}

#explanation li strong {
    color: #333;
}


</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const angleSlider = document.getElementById('angle-slider');
    const angleValueSpan = document.getElementById('angle-value');
    const snowTypeSelect = document.getElementById('snow-type-select');
    const runButton = document.getElementById('run-simulation-button');
    const resetButton = document.getElementById('reset-button'); // הוספת כפתור איפוס
    const slopeDiv = document.querySelector('.slope');
    const snowMassDiv = document.querySelector('.snow-mass');
    const resultDisplay = document.querySelector('.result-display');
    const explanationDiv = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggle-explanation');

    // שמירת מיקום התחלתי של גוש השלג (כדי לאפס אליו)
    const initialSnowMassTop = parseFloat(getComputedStyle(snowMassDiv).top);
    const initialSnowMassLeft = parseFloat(getComputedStyle(snowMassDiv).left);


    // עדכון ויזואלי של המדרון וערך הזווית בעת הזזת הסליידר
    angleSlider.addEventListener('input', () => {
        const angle = angleSlider.value;
        angleValueSpan.textContent = `${angle}°`;
        // סובב את אלמנט המדרון נגד כיוון השעון לפי הערך
        // שימו לב: ה-transform-origin ב-CSS הוא בתחתית המרכז, אז זה נראה כמו הטיית הר
        slopeDiv.style.transform = `rotate(-${angle}deg)`;
        resetSimulation(); // אפס מיקום גוש השלג כשזווית משתנה
    });

    // גורמי התנגדות של סוגי שלג (מודל פשוט)
    // ערכים אלו מייצגים את יכולת ההתנגדות היחסית של סוגי השלג להחלקה.
    // ערך גבוה יותר = התנגדות רבה יותר / פחות סיכוי למפולת בזוויות נמוכות.
    // מבוסס על מקדמי חיכוך פנימי ולכידות.
    const snowResistanceFactors = {
        powder: 0.3, // התנגדות נמוכה (מחליק בקלות יחסית)
        packed: 0.7, // התנגדות בינונית
        wet: 1.0     // התנגדות גבוהה (פחות סביר להתחלה, מפשט את הסימולציה)
    };

    // פונקציית הסימולציה
    const runSimulation = () => {
        // איפוס לפני כל הפעלה כדי להתחיל ממצב נקי
        resetSimulation();

        const angle = parseFloat(angleSlider.value); // זווית במעלות
        const snowType = snowTypeSelect.value;
        const resistanceFactor = snowResistanceFactors[snowType];

        // המרת זווית לרדיאנים לצורך פונקציות טריגונומטריות
        const angleRad = angle * Math.PI / 180;

        // מודל כוחות פשוט:
        // כוח מניע (פועל למטה) פרופורציונלי ל-sin(זווית) - מייצג את רכיב כוח הכבידה במורד המדרון
        const drivingForce = Math.sin(angleRad);

        // כוח מתנגד (פועל מעלה) פרופורציונלי ל-(גורם התנגדות * cos(זווית) + התנגדות בסיסית)
        // cos(זווית) קשור לכוח הנורמלי המשפיע על החיכוך
        // התנגדות בסיסית מייצגת חיכוך התחלתי, לכידות מינימלית וכו'.
        const baseResistance = 0.2; // ערך קטן להתנגדות תמיד קיימת
        const resistingForce = resistanceFactor * Math.cos(angleRad) + baseResistance;

        let resultText = '';
        let avalancheOccurred = false;

        // קביעת אם מתרחשת מפולת (כוח מניע > כוח מתנגד)
        // שימוש בסף טולרנטיות קטן למניעת בעיות נקודה צפה וליצירת רגע "קריטי"
        const tolerance = 0.02;
        if (drivingForce > resistingForce + tolerance) {
            resultText = 'תוצאה: מפולת! ההר לא יציב והשלג התדרדר.';
            resultDisplay.className = 'result-display show failure'; // הוספת קלאסים לתוצאה
            avalancheOccurred = true;
        } else {
            resultText = 'תוצאה: יציב. ההר מחזיק את השלג במקומו.';
            resultDisplay.className = 'result-display show success'; // הוספת קלאסים לתוצאה
            avalancheOccurred = false;
        }

        resultDisplay.textContent = resultText;

        // הפעלת אנימציה אם התרחשה מפולת
        if (avalancheOccurred) {
             // הוספת רעידה קלה לפני הנפילה
             slopeDiv.classList.add('shaking');
             snowMassDiv.classList.add('shaking');

             setTimeout(() => {
                slopeDiv.classList.remove('shaking');
                snowMassDiv.classList.remove('shaking');

                // תרגום גוש השלג במורד המדרון הפיזי
                // אנו מתרגמים ביחס למערכת הצירים של ה-slope div המסתובב.
                // תרגום אופקי (translateX) בתוך הדיב המסתובב נראה כמו החלקה במורד המדרון.
                const slideDistanceX = 600; // מרחק גדול יותר להחלקה ויזואלית
                const slideDistanceY = 0; // כרגע אין תרגום אנכי נוסף במערכת הצירים של הסלופ
                const rotationDuringSlide = 10; // סיבוב קל בזמן ההחלקה (מעלות)

                snowMassDiv.style.transition = 'transform 2s ease-in'; // אנימציה
                // שילוב הטרנספורמציות: התרגום (החלקה) והסיבוב (של השלג עצמו בזמן ההחלקה)
                // שים לב: אם היית רוצה תרגום מחושב לפי הזווית הפיזית ביחס למסך,
                // החישוב היה מסובך יותר ומשלב את הזווית.
                //translateX בתוך הסלופ המסתובב כבר מתרגם "לאורך" המדרון הפיזי.
                snowMassDiv.style.transform = `translateX(${slideDistanceX}px) rotate(${rotationDuringSlide}deg)`;

             }, 600); // זמן לרעידה לפני הנפילה (במילישניות)
        }
    };

    // איפוס מיקום גוש השלג ותצוגת התוצאה
    const resetSimulation = () => {
        // השבתת אנימציה באופן זמני לצורך איפוס מיידי
        snowMassDiv.style.transition = 'none';
        // איפוס מיקום (חזרה למקור)
        // מכיוון שהטרנספורמציה היא טרנסלציה ורוטציה, איפוס הוא ל-none או למיקום ההתחלתי
         snowMassDiv.style.transform = 'translateX(0px) rotate(0deg)'; // איפוס לטרנספורמציית בסיס (אין תרגום או סיבוב)

        // הפעלת "ריפלואו" לדפדפן כדי לוודא שהשינוי ללא טרנזישן יוחל לפני הפעלת הטרנזישן מחדש
        snowMassDiv.offsetHeight;

        // הסרת קלאסי רעידה/החלקה אם קיימים
        slopeDiv.classList.remove('shaking');
        snowMassDiv.classList.remove('shaking', 'slide');

        // הסרת קלאסי תוצאה וטקסט
        resultDisplay.textContent = ''; // ניקוי טקסט תוצאה
        resultDisplay.className = 'result-display'; // איפוס קלאסים (יסתיר את התצוגה עקב opacity: 0;)
    };

    // מאזין לאירוע לחיצה על כפתור ההפעלה
    runButton.addEventListener('click', runSimulation);

    // מאזין לאירוע לחיצה על כפתור האיפוס
    resetButton.addEventListener('click', resetSimulation);


    // מאזין לאירוע לחיצה על כפתור הצג/הסתר הסבר
    toggleButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleButton.textContent = isHidden ? 'הסתר הסבר פיזיקלי' : 'הצג/הסתר הסבר פיזיקלי';
    });

    // הגדרה ראשונית בעת טעינת העמוד
    angleValueSpan.textContent = `${angleSlider.value}°`;
    // הגדרת סיבוב המדרון ההתחלתי לפי ערך הסליידר
    slopeDiv.style.transform = `rotate(-${angleSlider.value}deg)`;
    resetSimulation(); // וודא שגוש השלג במיקום התחלתי
});
</script>
```