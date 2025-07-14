---
title: "החלטת פרס אבל: סימולטור ועדת הפרס"
english_slug: the-abel-prize-decision-committee-simulator
category: "פילוסופיה של המדע"
tags:
  - מתמטיקה
  - פרס אבל
  - קבלת החלטות
  - ועדות שיפוט
  - אבולואציה אקדמית
---
# החלטת פרס אבל: סימולטור ועדת הפרס

ברוכים הבאים למסדרונות היוקרתיים של האקדמיה הנורווגית למדעים וספרות. לרגע קצר, אתם חלק מוועדת פרס אבל – חמישה מוחות מתמטיים מהשורה הראשונה בעולם, המופקדים על המשימה הכבירה: בחירת זוכה בפרס הנחשק ביותר במתמטיקה. אל מול שולחן הדיונים מונחות תיקיות של שלושה מועמדים יוצאי דופן. כל אחד מהם שינה את פני המתמטיקה בדרכו. איך תשקלו את תרומתם? אילו קריטריונים יכריעו עבורכם? צאו למסע המרתק אל לב תהליך קבלת ההחלטה, והרגישו את הדילמות האמיתיות הניצבות בפני גאוני המתמטיקה הבוחרים את עמיתיהם.

<div id="abel-prize-simulator" class="simulator-container">
    <h2 class="simulator-title">סימולטור ועדת פרס אבל: ההחלטה בידיים שלך</h2>
    <p class="intro-text">כחבר בוועדת פרס אבל, עליך להעריך כל מועמד בקפידה על פי קריטריונים מרכזיים. הזז את המחוונים (1 - ההישג נמוך בקריטריון זה, 10 - ההישג יוצא מן הכלל בקריטריון זה) כדי לשקף את הערכתך.</p>

    <div class="candidates-grid">
        <div class="candidate-card" id="candidate-sharma">
            <h3 class="candidate-name">ד"ר אניה שארמה <span class="candidate-score"></span></h3>
            <p class="candidate-bio">חוקרת צעירה ופורצת דרך בתורת המספרים האנליטית. פתרה השערה ארוכת שנים שנחשבה בלתי חדירה, תוך שימוש בשיטות בנייה חדשות לחלוטין. עבודתה אינה רק פתרון חידה, אלא פותחת שערים לתחומים מחקריים חדשים רבים ובלתי צפויים לעתיד.</p>
            <div class="criteria-list">
                <div class="criterion-item">
                    <label for="sharma-originality">מקוריות וחדשנות:</label>
                    <div class="slider-control">
                        <input type="range" id="sharma-originality" name="sharma-originality" min="1" max="10" value="5">
                        <span class="value-display">5</span>
                    </div>
                </div>
                <div class="criterion-item">
                    <label for="sharma-impact">השפעה עתידית ופוטנציאל פיתוח:</label>
                     <div class="slider-control">
                        <input type="range" id="sharma-impact" name="sharma-impact" min="1" max="10" value="5">
                        <span class="value-display">5</span>
                    </div>
                </div>
                <div class="criterion-item">
                    <label for="sharma-elegance">אלגנטיות הפתרון והשיטות:</label>
                    <div class="slider-control">
                         <input type="range" id="sharma-elegance" name="sharma-elegance" min="1" max="10" value="5">
                        <span class="value-display">5</span>
                    </div>
                </div>
                <div class="criterion-item">
                    <label for="sharma-breakthrough">עומק פריצת הדרך הספציפית:</label>
                    <div class="slider-control">
                        <input type="range" id="sharma-breakthrough" name="sharma-breakthrough" min="1" max="10" value="5">
                        <span class="value-display">5</span>
                    </div>
                </div>
            </div>
        </div>

        <div class="candidate-card" id="candidate-tanaka">
            <h3 class="candidate-name">פרופ' קנג'י טנאקה <span class="candidate-score"></span></h3>
            <p class="candidate-bio">עבודת חיים מונומנטלית ביסודות הגיאומטריה האלגברית הקלאסית. פיתח תיאוריה מאוחדת, רחבה להפליא ואלגנטית, שהפכה לאבן יסוד בתחום. תרומתו נלמדת בכל אוניברסיטה בעולם והשפיעה עמוקות על דורות רבים של מתמטיקאים. השפעתה ארוכת שנים ומבוססת היטב.</p>
             <div class="criteria-list">
                <div class="criterion-item">
                    <label for="tanaka-originality">מקוריות בזמנו והשפעתה ההיסטורית:</label>
                    <div class="slider-control">
                        <input type="range" id="tanaka-originality" name="tanaka-originality" min="1" max="10" value="5">
                        <span class="value-display">5</span>
                    </div>
                </div>
                <div class="criterion-item">
                    <label for="tanaka-impact">השפעה רחבה וארוכת טווח:</label>
                     <div class="slider-control">
                        <input type="range" id="tanaka-impact" name="tanaka-impact" min="1" max="10" value="5">
                        <span class="value-display">5</span>
                    </div>
                </div>
                <div class="criterion-item">
                    <label for="tanaka-elegance">אלגנטיות התיאוריה הכוללת:</label>
                    <div class="slider-control">
                        <input type="range" id="tanaka-elegance" name="tanaka-elegance" min="1" max="10" value="5">
                        <span class="value-display">5</span>
                    </div>
                </div>
                 <div class="criterion-item">
                    <label for="tanaka-breakthrough">עומק פריצת הדרך הכוללת (תיאוריה שלמה):</label>
                    <div class="slider-control">
                        <input type="range" id="tanaka-breakthrough" name="tanaka-breakthrough" min="1" max="10" value="5">
                        <span class="value-display">5</span>
                    </div>
                </div>
            </div>
        </div>

         <div class="candidate-card" id="candidate-petrova">
            <h3 class="candidate-name">ד"ר אלנה פטרובה <span class="candidate-score"></span></h3>
            <p class="candidate-bio">בנתה גשר תיאורטי חזק ומפתיע בין תורת ההסתברות המתקדמת לפיזיקה מתמטית (מכניקה סטטיסטית). עבודתה סיפקה כלים אנליטיים חדשים לחלוטין לשני התחומים במקביל והולידה שדה מחקר אינטרדיסציפלינרי חדש ומלהיב. מייצגת חיבורים לא צפויים.</p>
             <div class="criteria-list">
                <div class="criterion-item">
                    <label for="petrova-originality">מקוריות הקשרים הבין-תחומיים:</label>
                    <div class="slider-control">
                         <input type="range" id="petrova-originality" name="petrova-originality" min="1" max="10" value="5">
                        <span class="value-display">5</span>
                    </div>
                </div>
                <div class="criterion-item">
                    <label for="petrova-impact">השפעה (רוחב על פני תחומים שונים):</label>
                    <div class="slider-control">
                        <input type="range" id="petrova-impact" name="petrova-impact" min="1" max="10" value="5">
                        <span class="value-display">5</span>
                    </div>
                </div>
                <div class="criterion-item">
                    <label for="petrova-elegance">אלגנטיות הסינתזה התיאורטית:</label>
                     <div class="slider-control">
                         <input type="range" id="petrova-elegance" name="petrova-elegance" min="1" max="10" value="5">
                        <span class="value-display">5</span>
                    </div>
                </div>
                 <div class="criterion-item">
                    <label for="petrova-breakthrough">עומק פריצת הדרך בחיבור התחומים:</label>
                     <div class="slider-control">
                        <input type="range" id="petrova-breakthrough" name="petrova-breakthrough" min="1" max="10" value="5">
                        <span class="value-display">5</span>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <button id="submit-decision" class="action-button">קבל את פסק הדין של הוועדה!</button>

    <div id="feedback" class="feedback-area">
        <h3 class="feedback-title">דיון ועדת הפרס: ניתוח ההחלטה שלך</h3>
        <div id="feedback-content"></div>
    </div>
</div>

<style>
:root {
    --primary-color: #0056b3; /* A deep, academic blue */
    --secondary-color: #007bff; /* Lighter blue for highlights/buttons */
    --accent-color: #28a745; /* Green for positive feedback */
    --danger-color: #dc3545; /* Red for contrast/warnings (not heavily used here) */
    --background-color: #f4f7f6; /* Light grey-blue background */
    --card-background: #ffffff; /* White for cards */
    --border-color: #e0e0e0; /* Light grey for borders */
    --text-color: #333; /* Dark grey for text */
    --subtle-text-color: #555; /* Slightly lighter grey */
}

#abel-prize-simulator {
    font-family: 'Arial Hebrew', sans-serif; /* Use a clear Hebrew font */
    line-height: 1.7;
    max-width: 900px; /* Slightly wider container */
    margin: 20px auto;
    padding: 30px; /* More padding */
    background-color: var(--background-color);
    border-radius: 12px; /* More rounded corners */
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* Stronger, softer shadow */
    direction: rtl;
    text-align: right;
    color: var(--text-color);
    overflow: hidden; /* Clean overflow */
}

.simulator-title {
    color: var(--primary-color);
    text-align: center; /* Center title */
    margin-bottom: 20px;
    font-size: 2em; /* Larger title */
}

.intro-text {
    text-align: center;
    margin-bottom: 30px;
    color: var(--subtle-text-color);
    font-size: 1.1em;
}

.candidates-grid {
    display: grid; /* Use grid for more flexible layout */
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); /* Responsive columns */
    gap: 30px; /* Increased gap */
    margin-bottom: 30px;
}

.candidate-card {
    padding: 25px; /* More padding */
    border: 1px solid var(--border-color);
    border-radius: 10px; /* Rounded card corners */
    background-color: var(--card-background);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.07); /* Softer card shadow */
    transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out; /* Smooth hover effect */
    display: flex;
    flex-direction: column; /* Stack content */
}

.candidate-card:hover {
    transform: translateY(-5px); /* Lift effect on hover */
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
}

.candidate-name {
    color: var(--secondary-color);
    margin-top: 0;
    border-bottom: 2px solid var(--border-color); /* Thicker separator */
    padding-bottom: 10px;
    margin-bottom: 15px;
    font-size: 1.5em;
    display: flex; /* Align name and score */
    justify-content: space-between; /* Put score on the left */
    align-items: center;
}

.candidate-score {
    font-size: 0.9em;
    color: var(--primary-color);
    background-color: #eef; /* Light background for score */
    padding: 3px 8px;
    border-radius: 4px;
     direction: ltr; /* Display score left-to-right */
     unicode-bidi: embed; /* Override bidi for score */
     margin-left: 10px; /* Space from name */
     min-width: 30px; /* Ensure space */
     text-align: center;
}


.candidate-bio {
    margin-bottom: 20px;
    font-size: 0.95em;
    color: var(--subtle-text-color);
    flex-grow: 1; /* Allows bio to take up available space */
}

.criteria-list {
    margin-top: auto; /* Pushes criteria to the bottom */
}

.criterion-item {
    margin-bottom: 15px; /* Space between criteria */
}

.criterion-item label {
    display: block;
    margin-bottom: 8px; /* Space below label */
    font-weight: bold;
    color: var(--text-color);
    font-size: 0.9em;
}

.slider-control {
    display: flex;
    align-items: center;
    gap: 10px; /* Space between slider and value */
}

.slider-control input[type="range"] {
    flex-grow: 1; /* Slider takes up remaining space */
    height: 8px; /* Thicker slider track */
    -webkit-appearance: none;
    appearance: none;
    background: linear-gradient(to right, #ccc, var(--secondary-color)); /* Gradient track */
    border-radius: 5px;
    outline: none;
    opacity: 0.9;
    transition: opacity 0.2s ease;
}

.slider-control input[type="range"]:hover {
    opacity: 1;
}

/* Slider thumb styling */
.slider-control input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 20px; /* Thumb size */
    height: 20px; /* Thumb size */
    background: var(--primary-color);
    border: 2px solid var(--card-background); /* White border */
    border-radius: 50%; /* Circular thumb */
    cursor: pointer;
    transition: background 0.3s ease, border-color 0.3s ease;
    box-shadow: 0 2px 4px rgba(0,0,0,0.2);
}

.slider-control input[type="range"]::-moz-range-thumb {
    width: 20px; /* Thumb size */
    height: 20px; /* Thumb size */
    background: var(--primary-color);
     border: 2px solid var(--card-background); /* White border */
    border-radius: 50%; /* Circular thumb */
    cursor: pointer;
     transition: background 0.3s ease, border-color 0.3s ease;
     box-shadow: 0 2px 4px rgba(0,0,0,0.2);
}

.slider-control input[type="range"]::-webkit-slider-thumb:hover,
.slider-control input[type="range"]::-moz-range-thumb:hover {
    background: var(--secondary-color); /* Change color on hover */
}

.value-display {
    display: inline-block;
    min-width: 25px; /* Fixed width for alignment */
    text-align: center;
    font-weight: bold;
    color: var(--primary-color);
    font-size: 1em;
    direction: ltr; /* Ensure number displays correctly */
    unicode-bidi: embed;
}


.action-button {
    display: block;
    width: 100%;
    padding: 12px 20px; /* More padding */
    background-color: var(--secondary-color);
    color: white;
    border: none;
    border-radius: 6px; /* More rounded */
    font-size: 1.2em; /* Larger font */
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.1s ease;
    margin-top: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.action-button:hover {
    background-color: var(--primary-color);
}

.action-button:active {
    transform: scale(0.98); /* Press effect */
}

.feedback-area {
    margin-top: 30px; /* More space */
    padding: 25px; /* More padding */
    border: 1px solid var(--border-color);
    border-radius: 10px;
    background-color: #e9eef2; /* Light blue-grey background */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.07);
    display: none; /* Hidden initially */
    opacity: 0; /* Start transparent for fade-in */
    transition: opacity 0.5s ease-in-out; /* Fade-in transition */
}

.feedback-area.visible {
    display: block;
    opacity: 1;
}

.feedback-title {
    margin-top: 0;
    color: var(--primary-color);
    border-bottom: 1px dashed var(--border-color); /* Dashed separator */
    padding-bottom: 10px;
    margin-bottom: 15px;
}

#feedback-content h4 {
    color: var(--secondary-color);
    margin-top: 20px;
    margin-bottom: 10px;
}

#feedback-content p {
    margin-bottom: 10px;
    color: var(--subtle-text-color);
}

#feedback-content ul {
    margin-bottom: 15px;
    padding-right: 20px; /* Adjust padding for RTL list */
    color: var(--subtle-text-color);
}

#feedback-content li {
    margin-bottom: 8px;
}

#feedback-content strong {
    color: var(--text-color);
}

.explanation-section { /* New class for explanation div */
    margin-top: 30px;
    padding: 25px;
    border-top: 1px solid var(--border-color);
    display: none; /* Hidden initially */
    background-color: var(--card-background);
    border-radius: 10px; /* Match simulator container */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.07);
    opacity: 0; /* Start transparent for fade-in */
    transition: opacity 0.5s ease-in-out; /* Fade-in transition */
}
.explanation-section.visible {
    display: block;
    opacity: 1;
}


.explanation-section h2 {
    color: var(--primary-color);
    margin-top: 0;
    margin-bottom: 15px;
    border-bottom: 1px solid var(--border-color);
    padding-bottom: 10px;
}

.explanation-section ul {
    padding-right: 20px; /* Adjust padding for RTL list */
    list-style: disc; /* Use discs for list items */
    color: var(--subtle-text-color);
}

.explanation-section li {
    margin-bottom: 12px;
}

.explanation-section strong {
    color: var(--text-color);
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .candidates-grid {
        grid-template-columns: 1fr; /* Stack candidates on small screens */
    }

    #abel-prize-simulator {
        padding: 20px;
    }

    .candidate-card {
        padding: 20px;
    }

    .action-button {
        font-size: 1.1em;
    }
}

</style>

<button id="toggle-explanation" class="action-button secondary-button">הצג/הסתר מידע נוסף: מהו פרס אבל ואיך מתבצעת הבחירה?</button>

<div id="explanation" class="explanation-section">
    <h2>הסבר על פרס אבל ותהליך הבחירה: מאחורי הקלעים</h2>
    <ul>
        <li><strong>פסגת המתמטיקה: מה הופך את פרס אבל לכל כך יוקרתי?</strong> פרס אבל (Abel Prize), המוענק מדי שנה על ידי מלך נורווגיה, הוא ההכרה הגבוהה ביותר לה יכול מתמטיקאי לשאוף. הוא נוסד ב-2002 לזכר נילס הנריק אבל, ורבים רואים בו את המקבילה לפרס נובל (שאינו מוענק במתמטיקה באופן רשמי). יוקרתו נובעת מסכום הפרס המשמעותי, מתהליך הבחירה המוקפד והדיסקרטי, ומהכוח לשים זרקור עולמי על תרומות מתמטיות מכוננות.</li>
        <li><strong>מבנה ועדת הפרס: המומחים שמאחורי ההחלטה.</strong> את ההחלטה מקבלת ועדת פרס אבל – פאנל יוקרתי של חמישה מתמטיקאים בעלי שם עולמי, הנבחרים על ידי האקדמיה הנורווגית למדעים וספרות. תהליך המינוי מתחיל בפנייה למוסדות אקדמיים ומדענים בכירים ברחבי הגלובוס.</li>
        <li><strong>המסע אל הזכייה: תהליך הבחירה הרשמי.</strong> לאחר איסוף המועמדויות (הנשמרות בסוד קפדני), הוועדה יוצאת למסע הערכה מעמיק שנמשך חודשים רבים. הוא כולל איסוף חוות דעת מומחים חיצוניות, דיונים פנימיים אינטנסיביים, וצמצום הדרגתי של הרשימה עד להגעה לקונצנזוס על הזוכה הסופי או הזוכים (לפעמים הפרס מתחלק).</li>
        <li><strong>קריטריונים להצלחה: מה מחפשים חברי הוועדה?</strong> הקריטריון העליון הוא תרומה מדעית "בעלת השפעה יוצאת דופן" בתחום המתמטיקה. זהו קריטריון רחב המאפשר לוועדה גמישות, אך הוא מתורגם לרוב להערכת היבטים כמו: <strong>פריצות דרך תיאורטיות עמוקות, פיתוח שיטות חדשניות שמשנות את כללי המשחק, פתרון בעיות יסודיות שפתוחות זמן רב, השפעה רוחבית על תחומי משנה רבים במתמטיקה (או אפילו מחוצה לה), ואלגנטיות ועומק רעיוני של התרומה.</strong> לרוב נבחנת מכלול עבודתו של המועמד לאורך הקריירה.</li>
        <li><strong>אתגרים בוועדה: האמנות של השוואת הבלתי ניתן להשוואה.</strong> הדילמות שראיתם בסימולטור הן אמיתיות. ועדת אבל מתמודדת עם: השוואת הישגים מתחומים מתמטיים רחוקים מאוד (גיאומטריה מול הסתברות, למשל), הערכת הפוטנציאל של עבודה חדשה מול השפעה מוכחת לאורך עשורים של עבודה קלאסית, הצורך להגיע להסכמה בין מומחים בעלי פרספקטיבות שונות, והיבטים סובייקטיביים בהערכת יופי ואלגנטיות מתמטית.</li>
        <li><strong>הד הזכייה: השפעת הפרס על עולם המתמטיקה.</strong> מעבר להכרה אישית, פרס אבל מציב את המחקר המתמטי בסיסי בחזית הבמה העולמית, מעודד השקעה בתחום, ומעורר השראה בקרב דורות חדשים של תלמידים וחוקרים.</li>
        <li><strong>האבל מול נובל: דמיון ושוני.</strong> בדומה לנובל, האבל מוענק על תרומות מכוננות בתחומן, כרוך בתהליך בחירה קפדני ודיסקרטי, ובעל יוקרה עצומה. ההבדלים העיקריים: תחום (אין נובל במתמטיקה), מספר זוכים (אבל יכול להיות אחד או יותר, נובל עד שלושה לתחום), וגוף ההענקה (האקדמיה הנורווגית למדעים וספרות לאבל, מוסדות שונים לנובל).</li>
        <li><strong>מה למדנו מהעבר? דוגמאות לזוכים והסיבות לבחירתם.</strong>
            <ul>
                <li><strong>ז'אן-פייר סר (2003):</strong> זכה על "עיצוב צורתה המודרנית של תחומי מפתח רבים במתמטיקה" (טופולוגיה, גיאומטריה אלגברית, תורת המספרים). דוגמה להכרה בהשפעה רחבה, עמוקה והיסטורית על מספר תחומים.</li>
                <li><strong>אנדרו ויילס (2016 - זכה ב"פרס מיוחד" המקביל לאבל):</strong> על הוכחת המשפט האחרון של פרמה. דוגמה להכרה בפתרון בעיה היסטורית מפורסמת שדרשה פיתוח שיטות מתמטיות חדשות לגמרי.</li>
                  <li><strong>קארן קסקיה קאהן (2019):</strong> על "תרומותיה לטופולוגיה אלגברית ויישומיה בגיאומטריה ובתיאוריה גלובלית של חבורות". דוגמה להכרה בעבודה בחזית המחקר העכשווי שמחברת בין תחומים.</li>
            </ul>
             בחירות אלו מדגימות את הרצון של הוועדה להכיר הן בהישגים שהשפעתם הוכחה לאורך עשורים והן בעבודות עדכניות שמעצבות את עתיד המתמטיקה.
        </li>
    </ul>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const candidateData = [
        { id: 'sharma', name: 'ד"ר אניה שארמה', internalScores: { originality: 9, impact: 7, elegance: 8, breakthrough: 9 } }, // Slightly higher on new breakthrough/originality
        { id: 'tanaka', name: 'פרופ\' קנג\'י טנאקה', internalScores: { originality: 7, impact: 10, elegance: 9, breakthrough: 8 } }, // Highest on impact/elegance of established theory
        { id: 'petrova', name: 'ד"ר אלנה פטרובה', internalScores: { originality: 8, impact: 9, elegance: 8, breakthrough: 9 } } // High on original connections and breadth of impact
    ];

    const sliders = document.querySelectorAll('.candidate-card input[type="range"]');

    // Function to update score display and candidate total score
    const updateScores = () => {
        candidateData.forEach(candidate => {
            let totalScore = 0;
            const candidateElement = document.getElementById(`candidate-${candidate.id}`);
            const scoreSpan = candidateElement.querySelector('.candidate-score');
            const criteriaSliders = candidateElement.querySelectorAll('.criteria-list input[type="range"]');

            criteriaSliders.forEach(slider => {
                const valueSpan = slider.closest('.slider-control').querySelector('.value-display');
                valueSpan.textContent = slider.value;
                totalScore += parseInt(slider.value, 10);
            });

            // Calculate average score
            const averageScore = (totalScore / criteriaSliders.length).toFixed(1);
            scoreSpan.textContent = `ציון ממוצע: ${averageScore}`; // Display average score
        });
    };

    // Add event listeners to sliders for live updates
    sliders.forEach(slider => {
        slider.addEventListener('input', updateScores);
    });

    // Initial score update on load
    updateScores();


    const submitButton = document.getElementById('submit-decision');
    const feedbackArea = document.getElementById('feedback');
    const feedbackContent = document.getElementById('feedback-content');

    submitButton.addEventListener('click', () => {
        const userScores = {};
        let maxUserAvgScore = -1;
        let userChoices = []; // Array to handle ties

        candidateData.forEach(candidate => {
            let totalScore = 0;
            const criteriaScores = {};
            Object.keys(candidate.internalScores).forEach(criterion => {
                const slider = document.getElementById(`${candidate.id}-${criterion}`);
                 if (slider) {
                    const score = parseInt(slider.value, 10);
                    criteriaScores[criterion] = score;
                    totalScore += score;
                 }
            });
             const avgScore = (totalScore / Object.keys(candidate.internalScores).length);
            userScores[candidate.id] = { total: totalScore, average: avgScore, criteria: criteriaScores };

            if (avgScore > maxUserAvgScore) {
                maxUserAvgScore = avgScore;
                userChoices = [candidate.name]; // New highest score, reset choices
            } else if (avgScore === maxUserAvgScore) {
                 userChoices.push(candidate.name); // Tie
            }
        });

        const userChoiceText = userChoices.length === 1 ? userChoices[0] : userChoices.join(' או ');


        // Determine a simplified "ideal" choice based on pre-set internal scores average
        let maxInternalAvgScore = -1;
        let idealChoices = [];
         candidateData.forEach(candidate => {
             let totalInternalScore = 0;
              Object.values(candidate.internalScores).forEach(score => {
                  totalInternalScore += score;
              });
            const avgInternalScore = (totalInternalScore / Object.keys(candidate.internalScores).length);

              if (avgInternalScore > maxInternalAvgScore) {
                  maxInternalAvgScore = avgInternalScore;
                  idealChoices = [candidate.name];
              } else if (avgInternalScore === maxInternalAvgScore) {
                  idealChoices.push(candidate.name);
              }
         });
        const idealChoiceText = idealChoices.length === 1 ? idealChoices[0] : idealChoices.join(' או ');


        let feedbackHTML = `<h4>ניתוח מיידי של הערכתך:</h4>`;
        feedbackHTML += `<p>על פי הניקוד הממוצע שהענקת, המועמד/ים המוביל/ים מבחינתך הוא/הם: <strong>${userChoiceText}</strong> (ממוצע ${maxUserAvgScore.toFixed(1)}).</p>`;

        feedbackHTML += `<h4>השוואה ודילמות אמיתיות:</h4>`;
        feedbackHTML += `<p>תהליך הבחירה בפרס יוקרתי כמו האבל מורכב הרבה יותר מסכום נקודות. חברי ועדת הפרס מביאים איתם פרספקטיבות שונות ונדרשים להתמודד עם דילמות עמוקות. בואו נראה איך ההערכה שלך מתחברת (או שונה) מהאתגרים האופייניים:</p>`;
        feedbackHTML += `<ul>`;

        // Specific comparison points based on candidate types
        feedbackHTML += `<li><strong>צעיר מול ותיק (שארמה מול טנאקה):</strong> הערכתך ל${candidateData[0].name} (ממוצע: ${userScores.sharma.average.toFixed(1)}) ול${candidateData[1].name} (ממוצע: ${userScores.tanaka.average.toFixed(1)}) משקפת את האופן שבו שקלת פוטנציאל עתידי מרגש מול השפעה מוכחת ורחבה לאורך שנים. האם נטית להעניק משקל רב יותר לפריצת דרך טרייה או לבניין תיאורטי קלאסי?</li>`;
        feedbackHTML += `<li><strong>העמקה מול חיבור (פטרובה מול האחרים):</strong> כיצד מיקמת את ${candidateData[2].name} (ממוצע: ${userScores.petrova.average.toFixed(1)}), שתרמה חיבור מהפכני בין תחומים, לעומת המועמדים שתרומתם מעמיקה בעיקר בתוך תחום אחד (גם אם רחב)? הערכתך לקריטריונים כמו 'מקוריות הקשרים' ו'השפעה רוחבית' כאן קריטית.</li>`;
         feedbackHTML += `<li><strong>שקלול קריטריונים:</strong> האם הענקת משקל רב יותר לאלגנטיות הפתרון, לעומת רוחב ההשפעה או עומק פריצת הדרך? ועדת אבל צריכה להגיע לקונצנזוס, ולעיתים הדגשת קריטריון מסוים אצל מועמד אחד, וקריטריון אחר אצל מועמד אחר, מובילה לדיונים מורכבים.</li>`;

        feedbackHTML += `</ul>`;

        feedbackHTML += `<p>הבחירה שלך (${userChoiceText}) משקפת את סולם הערכים המתמטי שאתה הבאת לשולחן הדיונים. </p>`;

        // Add insight based on comparison to "ideal" (internal scores)
         if (userChoices.some(choice => idealChoices.includes(choice))) { // Check if user choice overlaps with ideal choice(s)
             feedbackHTML += `<p class="insight-text"><strong>תובנה:</strong> מעניין! לפחות אחת מהבחירות המובילות שלך (${userChoiceText}) חופפת לבחירה שנחשבת חזקה במיוחד על פי שקלול פנימי של המאפיינים הבולטים ביותר שהוצגו. זה מראה שהערכתך קולטת היטב חלק מהסוגיות המרכזיות בהערכת הישגים ברמה זו.</p>`;
         } else {
              feedbackHTML += `<p class="insight-text"><strong>תובנה:</strong> בחירתך (${userChoiceText}) מייצגת פרספקטיבה שונה מזו שנחשבת לחזקה במיוחד על פי שקלול פנימי של המאפיינים הבולטים שהוצגו. זה בדיוק הקושי האמיתי של ועדת אבל – להגיע להחלטה אחת מוסכמת מבין מועמדים חזקים, כאשר הערכות שונות של היבטים כמו "אלגנטיות", "מקוריות" או "פוטנציאל עתידי" מובילות למסקנות שונות.</p>`;
         }


        feedbackContent.innerHTML = feedbackHTML;
        feedbackArea.classList.add('visible'); // Add class to trigger fade-in
        feedbackArea.scrollIntoView({ behavior: 'smooth', block: 'start' }); // Scroll to feedback
    });

    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');

    toggleExplanationButton.addEventListener('click', () => {
        const isVisible = explanationDiv.classList.contains('visible');
        if (!isVisible) {
            explanationDiv.classList.add('visible');
             toggleExplanationButton.textContent = 'הסתר מידע נוסף על פרס אבל';
             // Scroll after animation starts
             setTimeout(() => explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' }), 100); // Small delay for transition
        } else {
            explanationDiv.classList.remove('visible');
            toggleExplanationButton.textContent = 'הצג/הסתר מידע נוסף על פרס אבל';
             // Scroll back up if needed (optional, could be jarring)
             // setTimeout(() => toggleExplanationButton.scrollIntoView({ behavior: 'smooth', block: 'start' }), 100);
        }
    });

});
</script>
---