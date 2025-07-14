---
title: "מנופים: סוד הכוח שמסתתר בכל פינה!"
english_slug: levers-how-little-force-becomes-much
category: "פיזיקה"
tags:
  - מנוף
  - כוח
  - מטען
  - נקודת משען
  - מכונות פשוטות
---
# מנופים: סוד הכוח שמסתתר בכל פינה!

רוצים לגלות איך כלים פשוטים כמו פותחן בקבוקים או מריצה הופכים את החיים לקלים יותר? הסוד נמצא במנופים - מכונות פשוטות אבל גאוניות, שיודעות איך להפוך כוח קטן לעבודה גדולה. בואו נשחק ונראה איך זה עובד!

<div id="app">
  <div class="lever-container">
    <div class="lever-bar"></div>
    <div id="fulcrum" class="lever-element fulcrum">
      <div class="fulcrum-visual"></div> <!-- Visual part of fulcrum -->
      <div class="marker">▼</div>
      <div class="label fulcrum-label">נקודת משען</div>
    </div>
    <div id="load" class="lever-element load">
       <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23ffffff'%3E%3Cpath d='M0 0h24v24H0z' fill='none'/%3E%3Cpath d='M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 16c-3.31 0-6-2.69-6-6s2.69-6 6-6 6 2.69 6 6-2.69 6-6 6z'/%3E%3C/svg%3E" class="icon" alt="Load">
      <div class="label load-label">מטען (100N)</div>
      <div class="distance-label load-distance">d<span class="sub">מטען</span>: 0 ס"מ</div>
      <div class="force-arrow load-arrow down">↓</div>
    </div>
    <div id="effort" class="lever-element effort">
      <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23ffffff'%3E%3Cpath d='M0 0h24v24H0z' fill='none'/%3E%3Cpath d='M12 2c5.52 0 10 4.48 10 10s-4.48 10-10 10S2 17.52 2 12 6.48 2 12 2zm0 16c3.31 0 6-2.69 6-6s-2.69-6-6-6-6 2.69-6 6 2.69 6 6 6zM12 6v6l4 4-1.41 1.41L12 13.83V6z'/%3E%3C/svg%3E" class="icon" alt="Effort">
      <div class="label effort-label">כוח מופעל</div>
      <div class="distance-label effort-distance">d<span class="sub">כוח</span>: 0 ס"מ</div>
      <div class="force-arrow effort-arrow"></div>
    </div>
    <div class="results">
        <div class="calculated-effort">כוח נדרש לשיווי משקל: <span id="effort-value">0.00</span> N</div>
        <div class="mechanical-advantage">יתרון מכני: <span id="ma-value">∞</span></div>
        <div class="lever-type">סוג מנוף: <span id="lever-type">?</span></div>
    </div>
     <div class="bar-endpoints">
        <div class="end-marker left">|</div>
        <div class="end-marker right">|</div>
    </div>
  </div>
  <div class="instructions">
      <p><strong>גררו את העיגולים הצבעוניים (נקודת משען, מטען, כוח) לאורך המוט.</strong> שימו לב איך המרחקים משפיעים על הכוח שתצטרכו להפעיל!</p>
  </div>
</div>

<style>
/* --- גלובלי --- */
#app {
  direction: rtl;
  text-align: center;
  font-family: 'Heebo', sans-serif; /* שימוש בפונט עברי מודרני */
  margin-bottom: 30px;
  background-color: #f4f7f6; /* רקע עדין */
  padding: 20px 0;
  border-radius: 8px;
}

.lever-container {
  position: relative;
  width: 90%; /* ניצול שטח רחב יותר */
  height: 220px; /* גובה גדול יותר */
  margin: 50px auto 80px auto; /* מרווחים מוגדלים */
  border: 1px solid #e0e0e0; /* גבול עדין */
  background-color: #ffffff; /* רקע לבן לחלק האינטראקטיבי */
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.05); /* צל עדין */
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center; /* מרכז את התכולה */
}

/* --- מוט המנוף --- */
.lever-bar {
  position: absolute;
  left: 5%;
  right: 5%;
  top: 50%;
  height: 12px; /* מוט עבה יותר */
  background: linear-gradient(to right, #b0bec5, #78909c); /* גרדיאנט למראה תלת מימדי עדין */
  transform: translateY(-50%);
  border-radius: 6px;
  transition: transform 0.3s ease-out; /* אנימציה לסיבוב */
  box-shadow: 0 2px 4px rgba(0,0,0,0.2);
}

.bar-endpoints {
    position: absolute;
    top: 50%;
    left: 5%;
    right: 5%;
    transform: translateY(-50%);
    display: flex;
    justify-content: space-between;
    pointer-events: none; /* לא להפריע בגרירה */
    z-index: 5; /* מתחת לאלמנטים */
}

.end-marker {
    color: #555;
    font-size: 14px;
    font-weight: bold;
}


/* --- אלמנטים הניתנים לגרירה --- */
.lever-element {
  position: absolute;
  top: 50%;
  transform: translate(-50%, -50%); /* ממקם את האלמנט לפי מרכזו */
  width: 40px; /* אלמנטים גדולים יותר */
  height: 40px;
  border-radius: 50%;
  cursor: grab; /* סמן עכבר לגרירה */
  z-index: 20; /* מעל המוט */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 8px rgba(0,0,0,0.3); /* צל בולט יותר */
  transition: box-shadow 0.1s ease-in-out; /* אנימציה לצל בגרירה */
}

.lever-element:active {
    cursor: grabbing;
    box-shadow: 0 6px 12px rgba(0,0,0,0.4); /* צל מודגש יותר בגרירה */
}

.lever-element .icon {
    width: 60%; /* גודל אייקון יחסי */
    height: 60%;
    fill: #ffffff; /* צבע אייקונים לבן */
}

.fulcrum {
  background-color: #4CAF50; /* ירוק */
  z-index: 30; /* נקודת המשען הכי בולטת */
}

.fulcrum-visual {
    position: absolute;
    bottom: -15px; /* מתחת לעיגול */
    width: 0;
    height: 0;
    border-left: 20px solid transparent; /* בסיס משולש */
    border-right: 20px solid transparent;
    border-top: 20px solid #4CAF50; /* ירוק תואם */
}

.load {
  background-color: #FF9800; /* כתום */
}

.effort {
  background-color: #2196F3; /* כחול */
}

.label {
  position: absolute;
  bottom: -30px; /* מרווח גדול יותר מהעיגול */
  font-size: 12px; /* פונט קצת גדול יותר */
  white-space: nowrap;
  text-align: center;
  color: #333;
  font-weight: bold;
}

.distance-label {
    position: absolute;
    top: -25px; /* מרווח גדול יותר מהעיגול */
    font-size: 11px;
    white-space: nowrap;
    text-align: center;
    color: #555;
}
.distance-label .sub {
    vertical-align: sub;
    font-size: 9px;
}

.force-arrow {
    position: absolute;
    font-size: 28px; /* חץ גדול יותר */
    font-weight: bold;
    color: #f44336; /* אדום לחיזוק ויזואלי */
    bottom: -35px; /* מיקום מתחת לתוויות */
    left: 50%;
    transform: translateX(-50%);
    transition: transform 0.3s ease-out, color 0.3s ease-out; /* אנימציה לכיוון וצבע */
}

.effort-arrow.up {
    transform: translateX(-50%) rotate(180deg); /* סיבוב למעלה */
}

/* הסתרת חץ הכוח המופעל כשהוא על נקודת המשען */
.effort .force-arrow.hidden {
    visibility: hidden;
    opacity: 0;
}


/* --- אזור התוצאות --- */
.results {
    position: absolute;
    bottom: 15px; /* מיקום בתחתית הקונטיינר */
    left: 0;
    right: 0;
    font-size: 16px; /* פונט גדול יותר */
    color: #333;
    display: flex;
    justify-content: space-around; /* פיזור אחיד */
    align-items: center;
    background-color: #e0f2f7; /* רקע בהיר לתוצאות */
    padding: 10px 20px;
    border-radius: 4px;
    margin: 0 20px; /* מרווח מהצדדים */
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.results div {
    margin: 0 5px; /* מרווח קטן יותר בין התוצאות */
    flex-grow: 1; /* גדילה אחידה */
    text-align: center;
}

.results span {
    font-weight: bold;
    color: #0288d1; /* צבע הדגשה כחול */
}

.mechanical-advantage span {
    color: #388e3c; /* ירוק ליתרון */
}


/* --- הוראות --- */
.instructions {
    margin-top: 20px; /* מרווח מתחת לקונטיינר */
    font-size: 15px;
    color: #555;
    font-weight: bold;
}

/* --- הסבר מלא --- */
#toggle-explanation {
  display: block;
  margin: 30px auto 20px auto; /* מרווחים נוחים */
  padding: 12px 25px; /* פדינג גדול יותר */
  font-size: 16px;
  cursor: pointer;
  background-color: #0288d1; /* כחול */
  color: white;
  border: none;
  border-radius: 25px; /* כפתור עגול */
  box-shadow: 0 4px 8px rgba(0,0,0,0.2);
  transition: background-color 0.2s ease-in-out;
}

#toggle-explanation:hover {
    background-color: #0277bd; /* כחול כהה יותר בריחוף */
}

#explanation {
  display: none;
  margin-top: 20px;
  padding: 20px; /* פדינג גדול יותר */
  border: 1px solid #e0e0e0; /* גבול עדין */
  background-color: #ffffff; /* רקע לבן */
  text-align: right;
  line-height: 1.7; /* מרווח שורות נוח */
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.05);
}

#explanation h2, #explanation h3 {
    color: #333;
    border-bottom: 1px solid #eee; /* קו הפרדה עדין */
    padding-bottom: 8px;
    margin-top: 20px;
    margin-bottom: 15px;
}

#explanation p {
    margin-bottom: 12px;
}

#explanation ul {
    margin-bottom: 12px;
    padding-right: 25px; /* הזחה לרשימה */
}

#explanation li {
    margin-bottom: 8px;
}
</style>

<button id="toggle-explanation">הצגת ההסבר המלא</button>

<div id="explanation">
  <h2>מהו מנוף?</h2>
  <p>תארו לעצמכם מוט ארוך ואבן קטנה המשמשת כנקודת משען. אם תלחצו על קצה אחד של המוט, תוכלו להרים אבן כבדה בקצה השני בקלות יחסית! זהו העיקרון הפשוט מאחורי המנוף – מכונה בסיסית המורכבת ממוט קשיח (למשל, עץ, מתכת או עצם) המסתובב סביב נקודה קבועה שנקראת נקודת משען.</p>

  <h2>מרכיבי המנוף</h2>
  <p>לכל מנוף שלושה מרכיבים עיקריים:</p>
  <ul>
    <li>**נקודת משען (Fulcrum):** הנקודה הקבועה שסביבה המוט מסתובב. זה כמו הציר של הנדנדה.</li>
    <li>**כוח מופעל (Effort):** הכוח שאנחנו משקיעים במנוף. זה יכול להיות דחיפה, משיכה או לחיצה.</li>
    <li>**מטען / התנגדות (Load / Resistance):** הכוח שאנחנו מנסים להזיז, להרים או להתגבר עליו באמצעות המנוף. לדוגמה, המשקל של אבן, ההתנגדות של פקק בבקבוק, או משקל הגוף שלנו שאנו מרימים.</li>
  </ul>

  <h2>הסוד: עקרון המומנטים</h2>
  <p>היכולת המדהימה של מנוף להגביר כוח קשורה במושג שנקרא "מומנט". מומנט הוא בעצם השפעת הסיבוב של כוח מסוים סביב נקודת המשען. הוא מחושב פשוט: **מומנט = כוח × מרחק מנקודת המשען (זרוע הכוח)**.</p>
  <p>ככל שאתם מפעילים כוח רחוק יותר מנקודת המשען (זרוע כוח ארוכה יותר), כך אפילו כוח קטן ייצור מומנט גדול יותר. זה כמו לשבת בקצה הרחוק של נדנדה כדי להרים מישהו שיושב קרוב למרכז.</p>

  <h2>מתי המנוף בשיווי משקל?</h2>
  <p>מנוף נמצא בשיווי משקל מושלם כשהשפעת הסיבוב של המטען שווה בדיוק להשפעת הסיבוב של הכוח המופעל, בכיוונים מנוגדים. במילים פשוטות: **מומנט המטען = מומנט הכוח המופעל**.</p>
  <p>או בנוסחה: **כוח המטען × מרחק המטען מנקודת המשען = כוח מופעל × מרחק הכוח המופעל מנקודת המשען**.</p>
  <p>בסימולציה ששיחקתם איתה, המערכת חישבה עבורכם בדיוק איזה כוח נדרש כדי להגיע לשיווי משקל במיקומים שבחרתם.</p>

  <h2>יתרון מכני: כמה המנוף עוזר?</h2>
  <p>ה"יתרון המכני" אומר לנו פי כמה המנוף מקל עלינו את העבודה. זהו היחס בין כוח המטען לכוח המופעל הנדרש כדי להתגבר עליו:</p>
  <p>יתרון מכני = כוח המטען / כוח מופעל. וזה גם שווה ל: **מרחק הכוח המופעל מנקודת המשען / מרחק המטען מנקודת המשען**.</p>
  <p>אם היתרון המכני גדול מ-1, המנוף "מגביר כוח" - אתם צריכים להפעיל פחות כוח מכוח המטען. אם הוא קטן מ-1, אתם צריכים להפעיל יותר כוח (מנופים כאלה שימושיים להגברת מהירות או מרחק תנועה על חשבון כוח). יתרון מכני אינסופי מתקבל כשהכוח המופעל ממוקם רחוק מאוד מנקודת המשען יחסית למטען.</p>


  <h2>משפחות המנופים: 3 סוגים עיקריים</h2>
  <p>המנופים מחולקים לשלוש קבוצות בהתאם למיקום היחסי של נקודת המשען, המטען והכוח המופעל:</p>
  <ul>
    <li>**מנוף סוג 1:** נקודת המשען יושבת *בין* המטען לבין הכוח המופעל. דוגמאות מוכרות: מספריים, נדנדה, מלקחיים (כן, הם בעצם שני מנופים מסוג 1 שמחוברים). במנוף סוג 1 היתרון המכני יכול להיות גדול מ-1, שווה ל-1 או קטן מ-1, הכל תלוי איפה בדיוק ממוקמת נקודת המשען.</li>
    <li>**מנוף סוג 2:** המטען ממוקם *בין* נקודת המשען לבין הכוח המופעל. חשבו על מריצה, פותחן בקבוקים או מפצח אגוזים. במנופים מסוג 2, נקודת המשען היא תמיד בקצה אחד, והכוח המופעל בקצה השני. המטען תמיד קרוב יותר לנקודת המשען מאשר הכוח המופעל, ולכן מנופים אלה *תמיד* מספקים יתרון מכני הגדול מ-1. הם אלופים בהגברת כוח!</li>
    <li>**מנוף סוג 3:** הכוח המופעל נמצא *בין* נקודת המשען לבין המטען. דוגמאות יומיומיות: פינצטה (מלקטת), חכת דיג, מטאטא, ורוב המנופים בגוף האדם (למשל, הזרוע המורמת על ידי שריר הדו-ראשי). במנופים מסוג 3, הכוח המופעל קרוב יותר לנקודת המשען מאשר המטען. לכן, היתרון המכני *תמיד* קטן מ-1. הם לא מגבירים כוח, אבל הם מצוינים להגברת מהירות או מרחק תנועה של המטען ביחס לתנועת הכוח המופעל – שימושי מאוד לזריקת חכה או לטאטוא מהיר!</li>
  </ul>

  <h2>מנופים בכל מקום סביבנו</h2>
  <p>עכשיו כשאתם מכירים את העיקרון, תתחילו לראות מנופים בכל מקום! בכלי עבודה, במבנים (דלתות, שערים), ובגוף שלנו (העצמות הן המוטות, המפרקים הם נקודות המשען, והשרירים מספקים את הכוח). הבנת המנופים פותחת עיניים להבנת העולם הפיזי שמקיף אותנו.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const fulcrum = document.getElementById('fulcrum');
    const load = document.getElementById('load');
    const effort = document.getElementById('effort');
    const leverBar = document.querySelector('.lever-bar');
    const container = document.querySelector('.lever-container');
    const loadDistanceLabel = document.querySelector('.load-distance');
    const effortDistanceLabel = document.querySelector('.effort-distance');
    const effortValueDisplay = document.getElementById('effort-value');
    const maValueDisplay = document.getElementById('ma-value');
    const leverTypeDisplay = document.getElementById('lever-type');
    const effortArrow = document.querySelector('.effort-arrow');

    let activeElement = null;
    let offset = { x: 0, y: 0 };
    const containerRect = container.getBoundingClientRect(); // Initial rect
    const LOAD_FORCE = 100; // Constant load force in Newtons
    const CM_PER_PX = 0.0264583; // Approximation: 1px = 0.0264583cm (based on 96dpi)

    // Get positions relative to the container's left edge (percentage based)
    function getElementPercentage(element) {
        const elementRect = element.getBoundingClientRect();
        const containerRect = container.getBoundingClientRect();
        return ((elementRect.left - containerRect.left + element.offsetWidth / 2) / containerRect.width) * 100;
    }

    function setElementPercentage(element, percentage) {
        const containerRect = container.getBoundingClientRect();
        const barRect = leverBar.getBoundingClientRect();

        // Calculate element's center position in pixels relative to container's left edge
        let newCenterX = (percentage / 100) * containerRect.width;

        // Get bar's pixel positions relative to container's left edge
        const barLeftPx = barRect.left - containerRect.left;
        const barRightPx = barRect.right - containerRect.left;

        // Clamp the element's center position to stay within the bar's pixel bounds
        // Allowing a small buffer on ends for visual clarity
        const bufferPx = element.offsetWidth * 0.3; // Allow 30% of element width outside bar
        const minCenterX = barLeftPx - bufferPx;
        const maxCenterX = barRightPx + bufferPx;

        newCenterX = Math.max(minCenterX, Math.min(newCenterX, maxCenterX));

        // Convert clamped pixel center back to percentage left for the element's style
        const newLeftPercent = ((newCenterX - element.offsetWidth / 2) / containerRect.width) * 100;

        element.style.left = `${newLeftPercent}%`;
    }

    // Set initial positions (percentage of container width)
    setElementPercentage(fulcrum, 50);
    setElementPercentage(load, 30);
    setElementPercentage(effort, 70);


    function calculateLever() {
        const containerRect = container.getBoundingClientRect(); // Update container rect
        const barRect = leverBar.getBoundingClientRect(); // Update bar rect

        // Calculate element center positions in pixels relative to the container's left edge
        const fulcrumPosPx = fulcrum.getBoundingClientRect().left - containerRect.left + fulcrum.offsetWidth / 2;
        const loadPosPx = load.getBoundingClientRect().left - containerRect.left + load.offsetWidth / 2;
        const effortPosPx = effort.getBoundingClientRect().left - containerRect.left + effort.offsetWidth / 2;

        // Distances from the fulcrum (in pixels)
        const loadDistancePx = Math.abs(loadPosPx - fulcrumPosPx);
        const effortDistancePx = Math.abs(effortPosPx - fulcrumPosPx);

        // Convert pixels to cm for display
        const loadDistanceCm = loadDistancePx * CM_PER_PX;
        const effortDistanceCm = effortDistancePx * CM_PER_PX;

        loadDistanceLabel.textContent = `dמטען: ${loadDistanceCm.toFixed(1)} ס"מ`;
        effortDistanceLabel.textContent = `dכוח: ${effortDistanceCm.toFixed(1)} ס"מ`;

        let requiredEffort = 0;
        let mechanicalAdvantage = Infinity; // Default

        const distanceThresholdPx = 5; // Pixels threshold to consider elements "at" the fulcrum

        // --- Calculate Required Effort and MA ---
        if (effortDistancePx > distanceThresholdPx) { // Avoid division by zero/near-zero
             requiredEffort = (LOAD_FORCE * loadDistancePx) / effortDistancePx;
             effortValueDisplay.textContent = requiredEffort.toFixed(2);
             mechanicalAdvantage = effortDistancePx / loadDistancePx; // MA = Effort Arm / Load Arm
             maValueDisplay.textContent = mechanicalAdvantage.toFixed(2);
        } else {
             effortValueDisplay.textContent = '∞'; // Infinite force needed if effort is at fulcrum
             mechanicalAdvantage = 0; // No mechanical advantage possible
             maValueDisplay.textContent = '0.00';
        }

        // --- Determine Lever Type and Effort Arrow Direction ---
        const loadSide = loadPosPx < fulcrumPosPx - distanceThresholdPx ? 'left' : (loadPosPx > fulcrumPosPx + distanceThresholdPx ? 'right' : 'on');
        const effortSide = effortPosPx < fulcrumPosPx - distanceThresholdPx ? 'left' : (effortPosPx > fulcrumPosPx + distanceThresholdPx ? 'right' : 'on');

        let leverType = '?';

        // Hide effort arrow if effort is effectively at fulcrum
         if (effortDistancePx <= distanceThresholdPx) {
             effortArrow.classList.add('hidden');
         } else {
             effortArrow.classList.remove('hidden');
         }

        // Load arrow is always down for the constant load
        load.querySelector('.force-arrow').textContent = '↓';

        if (loadSide !== 'on' && effortSide !== 'on') {
             if (loadSide !== effortSide) {
                 // Type 1: Fulcrum is between load and effort
                 leverType = 'סוג 1';
                 effortArrow.textContent = '↓'; // Effort usually down in Type 1 to lift load
                 effortArrow.classList.remove('up'); // Ensure it's not 'up'
                 effortArrow.style.color = '#f44336'; // Red
             } else {
                 // Type 2 or 3: Fulcrum is at one end, load and effort on same side
                 if (Math.abs(loadPosPx - fulcrumPosPx) > Math.abs(effortPosPx - fulcrumPosPx)) {
                     // Type 3: Effort is between fulcrum and load
                     leverType = 'סוג 3';
                      effortArrow.textContent = '↑'; // Effort usually up in Type 3 to lift load
                     effortArrow.classList.add('up'); // Rotate arrow up
                     effortArrow.style.color = '#f44336'; // Red
                 } else {
                      // Type 2: Load is between fulcrum and effort
                     leverType = 'סוג 2';
                     effortArrow.textContent = '↑'; // Effort usually up in Type 2 to lift load
                     effortArrow.classList.add('up'); // Rotate arrow up
                      effortArrow.style.color = '#f44336'; // Red
                 }
             }
         } else {
             leverType = '?'; // One or more elements on fulcrum or positions are ambiguous
             effortArrow.classList.add('hidden');
         }

        leverTypeDisplay.textContent = leverType;

        // --- Lever Rotation Animation (Visualizing Leverage) ---
        const barLeftPx = barRect.left - containerRect.left;
        const barWidthPx = leverBar.offsetWidth; // Use offsetWidth for current width
        // Calculate fulcrum's position *along the bar* in pixels
        const fulcrumBarPositionPx = fulcrumPosPx - barLeftPx;

        // Set the transform origin of the bar to the fulcrum's position along the bar's width
        const fulcrumBarPercentage = (fulcrumBarPositionPx / barWidthPx) * 100;
        leverBar.style.transformOrigin = `${fulcrumBarPercentage}% 50%`;


        // Calculate tilt angle based on relative distances (visual leverage indicator)
        // Use distance ratio: if effort arm >> load arm, effort side tilts down (negative angle)
        // If load arm >> effort arm, load side tilts down (positive angle)
        let tiltAngle = 0; // degrees
        const maxVisualTilt = 2; // degrees, subtle tilt
        const minDistanceForTilt = 10; // px, minimum distance from fulcrum to consider tilting

        if (loadDistancePx > minDistanceForTilt && effortDistancePx > minDistanceForTilt) {
             // Normalize distances relative to the bar length for a stable visual tilt
             const barLengthConsideration = barWidthPx / 2; // Use half bar length as a reference
             const normalizedLoadDist = loadDistancePx / barLengthConsideration;
             const normalizedEffortDist = effortDistancePx / barLengthConsideration;

             // Tilt based on the difference in normalized distances, scaled by maxVisualTilt
             // Positive tilt means effort side up, load side down (load has more leverage)
             // Negative tilt means effort side down, load side up (effort has more leverage)
             const rawTilt = normalizedLoadDist - normalizedEffortDist;
             tiltAngle = rawTilt * maxVisualTilt; // Scale the difference to the max tilt range

             // Clamp the angle to the max visual tilt
             tiltAngle = Math.max(-maxVisualTilt, Math.min(maxVisualTilt, tiltAngle));

        } else {
             tiltAngle = 0; // No tilt if elements are too close to fulcrum
        }


        // Apply rotation with transition
        // Preserve the vertical translation needed to keep it centered initially
        leverBar.style.transform = `translateY(-50%) rotate(${tiltAngle}deg)`;
    }

    function startDragging(e) {
        // Check if the target or any parent is a draggable element
        activeElement = e.target.closest('.lever-element');
        if (!activeElement) return;

        // Prevent default drag behavior
        e.preventDefault();

        const elementRect = activeElement.getBoundingClientRect();
        const containerRect = container.getBoundingClientRect();

        // Calculate the offset of the mouse click from the element's center
        // We only care about horizontal offset
        offset.x = e.clientX - (elementRect.left + elementRect.width / 2);
        offset.y = 0; // Ensure no vertical drag influence

        activeElement.style.cursor = 'grabbing';
        // Add a class for visual feedback while dragging (e.g., shadow, z-index)
        activeElement.classList.add('dragging');

        document.addEventListener('mousemove', dragElement);
        document.addEventListener('mouseup', stopDragging);
    }

    function dragElement(e) {
        if (!activeElement) return;

        // Prevent default drag behavior
        e.preventDefault();

        const containerRect = container.getBoundingClientRect();

        // Calculate new center position in pixels relative to container's left edge
        let newCenterX = e.clientX - containerRect.left - offset.x;

        // Convert new center pixel position to percentage relative to container width
        let newCenterPercent = (newCenterX / containerRect.width) * 100;

        // Use the setElementPercentage function which handles clamping to bar bounds
        setElementPercentage(activeElement, newCenterPercent);

        // Recalculate lever properties as the element moves
        calculateLever();
    }

    function stopDragging() {
        if (!activeElement) return;
        activeElement.style.cursor = 'grab';
        // Remove the dragging class
        activeElement.classList.remove('dragging');
        activeElement = null;
        document.removeEventListener('mousemove', dragElement);
        document.removeEventListener('mouseup', stopDragging);
         // Optional: Add a slight animation/snap back to level if it wasn't perfectly level
         // calculateLever(); // Recalculate one last time to ensure final position is captured
    }

    // Add event listeners for dragging
    container.addEventListener('mousedown', startDragging);

    // Add dragging class style
     const styleSheet = document.styleSheets[0]; // Get the first stylesheet
     styleSheet.insertRule('.lever-element.dragging { z-index: 100; box-shadow: 0 8px 16px rgba(0,0,0,0.5); }', styleSheet.cssRules.length);


    // Toggle explanation visibility
    const toggleButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    toggleButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleButton.textContent = isHidden ? 'הסתר הסבר' : 'הצגת ההסבר המלא';
        // Scroll to the explanation when shown?
        if (isHidden) {
            explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });

     // Initial calculation after elements are positioned
     calculateLever();

     // Recalculate on window resize to adjust positions and distances
     window.addEventListener('resize', () => {
        // Re-set positions based on current percentages to keep them relative
        setElementPercentage(fulcrum, getElementPercentage(fulcrum));
        setElementPercentage(load, getElementPercentage(load));
        setElementPercentage(effort, getElementPercentage(effort));
        calculateLever();
     });

});
</script>
---
```