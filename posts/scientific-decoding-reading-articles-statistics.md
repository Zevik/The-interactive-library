---
title: "פענוח מדעי: קריאת מאמרים וסטטיסטיקות"
english_slug: scientific-decoding-reading-articles-statistics
category: "חשיבה ביקורתית"
tags:
  - מחקרים מדעיים
  - סטטיסטיקה
  - קריאה ביקורתית
  - הבנת נתונים
  - מתודולוגיה
---

# פענוח מדעי: המשימה שלכם

ברוכים הבאים, בלשים מדעיים! בעולם מוצף במידע, היכולת לפענח דיווחי מחקר וסטטיסטיקות היא כוח-על. האם אתם מוכנים לאתגר? צאו למסע שיאפשר לכם לקרוא מעבר לכותרות, לזהות הטיות ולחשוף את האמת שמאחורי הנתונים. המשימה מתחילה עכשיו!

<div class="scientific-detective-app">
  <div id="game-area">
    <div class="game-header">
        <div id="progress"></div>
        <div class="game-title">תיק חקירה מדעי:</div>
    </div>
    <div id="scenario" class="game-card scenario-card"></div>
    <div id="question" class="game-card question-card"></div>
    <div id="options" class="options-list"></div>
    <button id="check-answer" class="game-button primary" disabled>בדוק פענוח</button>
    <div id="feedback" class="feedback-area hidden"></div>
    <button id="next-question" class="game-button secondary hidden">תיק חקירה הבא ></button>
    <div id="game-end" class="game-card success hidden">
      <h2>🕵️‍♂️ משימה הושלמה! 🕵️‍♀️</h2>
      <p>כל הכבוד, בלש מדעי! פענחתם בהצלחה את כל תיקי החקירה. אתם מצוידים כעת בכלים חיוניים לקריאה ביקורתית של מחקרים וסטטיסטיקות.</p>
      <p>המשיכו לחקור ולפענח!</p>
    </div>
  </div>
</div>

<button id="toggle-explanation" class="game-button tertiary">💡 הצג / הסתר את ארגז הכלים לבלש המדעי</button>

<div id="theoretical-explanation" class="explanation-area hidden">
  <h2>ארגז הכלים של הבלש המדעי: מדריך לפענוח</h2>

  <h3>מבנה מאמר מדעי (IMRAD) - המפה שלכם</h3>
  <p>רוב "תיקי החקירה" המדעיים מובנים לפי קוד סודי בן 5 אותיות:</p>
  <ul>
    <li><strong>I - Introduction (מבוא):</strong> מציג את הרקע לפשע המדעי (שאלת המחקר), את המניעים (ההשערות), ואת חשיבות החקירה. שאלו את עצמכם: *מה החוקרים מנסים לגלות ולמה זה חשוב?*</li>
    <li><strong>M - Methods (שיטות):</strong> מפרט את ה"איך" של החקירה - מי נחקר (המדגם), באילו כלים השתמשו, ואיך התנהל התהליך. חפשו כאן ראיות לנקודות תורפה: *האם המדגם מייצג את הזירה המלאה? האם הכלים מדדו בדיוק את מה שרצו לחקור?*</li>
    <li><strong>R - Results (תוצאות):</strong> כאן מוצגות הראיות הגולמיות, לרוב בצורת טבלאות וגרפים. נדרשת עין חדה לפענח את הממצאים המרכזיים ולהבין את ה"סימנים" הסטטיסטיים (כמו מובהקות, גודל אפקט).</li>
    <li><strong>A - And (וּ):</strong> הקשר המחבר בין חלקים.</li>
    <li><strong>D - Discussion (דיון):</strong> החוקרים מציגים את הפרשנות שלהם לראיות, מקשרים לחקירות קודמות, ומודים במגבלות. זה המקום לבדוק האם הפרשנות תואמת את הראיות, או שהחוקרים הלכו רחוק מדי במסקנותיהם.</li>
  </ul>

  <h3>למה לכם להיות בלשים ביקורתיים?</h3>
  <p>כי לא כל "הודעה לעיתונות" או כותרת סנסציונית מבוססת על חקירה מוצקה. קריאה ביקורתית מאפשרת לכם:</p>
  <ul>
    <li>להפריד בין "עובדות" ל"השערות" או "משאלות לב".</li>
    <li>לחשוף הטעיות, ליקויים בחקירה או מסקנות מוגזמות.</li>
    <li>להעריך את מידת האמינות של ה"עדים" (הנתונים).</li>
    <li>להבין את גבולות הגזרה של החקירה ולא להכליל מסקנות לכל העולם.</li>
  </ul>

  <h3>פענוח רמזים סטטיסטיים: מושגי מפתח</h3>
  <ul>
    <li><strong>מובהקות סטטיסטית (p-value):</strong> לא עד כמה הממצא "חשוב", אלא עד כמה סביר שהשגתם אותו במקרה בלבד. p קטן (לרוב מתחת ל-0.05) אומר שהתוצאה כנראה לא מקרית. זכרו: תוצאה מקרית היא לא בהכרח תוצאה חסרת חשיבות, ותוצאה לא מקרית (מובהקת) היא לא בהכרח תוצאה חשובה מבחינה מעשית!</li>
    <li><strong>קורלציה מול סיבתיות:</strong> "חברות" (קורלציה) לא תמיד אומרת שמישהו "גרם" משהו למישהו אחר (סיבתיות). זה שגלידה נמכרת יותר כשיש יותר מקרי טביעה לא אומר שאכילת גלידה גורמת לטביעה (חום הוא הגורם השלישי!). רק תכנון מחקר ספציפי (ניסוי מבוקר) יכול לנסות ולהוכיח סיבתיות. כלל הבלש: קורלציה ≠ סיבתיות!</li>
    <li><strong>גודל אפקט (Effect Size):</strong> זה המדד שנותן לכם את גודל ה"שינוי" או ה"קשר" בפועל. האם הירידה בלחץ הדם הייתה זעירה (2 ממ"כ) או דרמטית (20 ממ"כ)? מדד זה עוזר להבין אם תוצאה מובהקת סטטיסטית היא גם בעלת חשיבות בעולם האמיתי.</li>
  </ul>

  <h3>זיהוי מלכודות והטיות: היזהרו!</h3>
  <ul>
    <li><strong>הטיית דגימה:</strong> האם החוקרים חקרו את האנשים הנכונים? מדגם של "מתנדבים בקמפוס" לא תמיד מייצג את כלל האוכלוסייה שמעניינת אותנו.</li>
    <li><strong>הטיית מדידה:</strong> האם כלי המדידה היו מדויקים? שאלון על הרגלי אכילה עשוי להיות מושפע מרצון המשיבים להיראות בריאים יותר.</li>
    <li><strong>הטיית אישור:</strong> האם החוקרים "רואים" רק את הראיות שתומכות בתיאוריה שלהם, ומתעלמים מאחרות?</li>
    <li><strong>מגבלות מובנות:</strong> כל חקירה מדעית מוגבלת. מדגם קטן, זמן חקירה קצר, או קושי לשלוט בכל המשתנים (במחקרי תצפית) – בלש טוב יחפש את המגבלות הללו, גם אם החוקרים לא הדגישו אותן מספיק.</li>
  </ul>

  <h3>איך לפענח מאמרים מהר ויעיל?</h3>
  <ul>
    <li><strong>התחילו בתקציר (Abstract):</strong> זוהי "תקציר מנהלים" של כל התיק.</li>
    <li><strong>קפצו למבוא (Introduction):</strong> זהו את "מה" ו"למה" של החקירה.</li>
    <li><strong>עברו למסקנות (Discussion/Conclusion):</strong> מה השורה התחתונה מבחינת החוקרים?</li>
    <li><strong>בח</strong></li>
    <li><strong>נו את הראיות הגרפיות (Results):</strong> הסתכלו על טבלאות וגרפים - הם לרוב מציגים את הממצאים העיקריים בצורה ויזואלית. האם הם תואמים את המסקנות?</li>
    <li><strong>צללו פנימה רק אם צריך:</strong> אם משהו נראה חשוד או מעניין במיוחד, חזרו לשיטות ולקריאה מעמיקה יותר של הדיון והמגבלות.</li>
    <li><strong>לא חייבים לקרוא הכל:</strong> התמקדו בחלקים הרלוונטיים לשאלתכם. המשימה היא למצוא את הראיות שחשובות לכם.</li>
  </ul>
</div>

<style>
  :root {
    --primary-color: #007bff;
    --secondary-color: #28a745;
    --tertiary-color: #6c757d;
    --background-color: #e9ecef;
    --card-background: #ffffff;
    --border-color: #dee2e6;
    --correct-color: #28a745;
    --incorrect-color: #dc3545;
    --warning-color: #ffc107;
    --text-color: #343a40;
    --font-family: 'Arial', sans-serif;
  }

  .scientific-detective-app {
    font-family: var(--font-family);
    line-height: 1.6;
    margin: 20px auto;
    padding: 30px;
    max-width: 800px;
    border: 1px solid var(--border-color);
    border-radius: 12px;
    background-color: var(--background-color);
    color: var(--text-color);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    position: relative; /* For animations/transitions */
    overflow: hidden; /* Keep content within bounds */
  }

  .game-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
      padding-bottom: 15px;
      border-bottom: 2px solid var(--border-color);
  }

  .game-title {
      font-size: 1.4em;
      font-weight: bold;
      color: var(--primary-color);
  }

  #progress {
    font-size: 1em;
    color: var(--tertiary-color);
    font-weight: bold;
  }

  .game-card {
    margin-bottom: 20px;
    padding: 20px;
    border-radius: 8px;
    border: 1px solid var(--border-color);
    background-color: var(--card-background);
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
    opacity: 1;
    transform: translateY(0);
    transition: opacity 0.5s ease-out, transform 0.5s ease-out;
  }

  .scenario-card {
      background-color: #eef5ff; /* Light blue */
      border-color: #cce5ff; /* Slightly darker blue */
      font-style: italic;
      white-space: pre-wrap; /* Allow line breaks in scenario */
      animation: fadeIn 0.6s ease-out;
  }

   .question-card {
       font-weight: bold;
       color: var(--text-color);
        animation: fadeIn 0.6s ease-out 0.2s backwards; /* Delayed fade-in */
   }

  .options-list {
    margin-bottom: 20px;
  }

  .options-list label {
    display: block;
    margin-bottom: 12px;
    padding: 15px;
    background-color: var(--card-background);
    border: 1px solid var(--border-color);
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.3s ease, border-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    display: flex;
    align-items: flex-start; /* Align radio and text at the top */
  }

  .options-list label:hover {
    background-color: #f8f9fa;
    border-color: #ced4da;
  }

  .options-list label:active {
      transform: scale(0.98);
  }

  .options-list input[type="radio"] {
    margin-right: 12px;
    flex-shrink: 0; /* Prevent radio button from shrinking */
    margin-top: 3px; /* Optical alignment */
  }

  .options-list label span {
    flex-grow: 1; /* Allow text to take available space */
  }


  .game-button {
    display: inline-block;
    padding: 12px 24px;
    margin-top: 15px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1.1em;
    font-weight: bold;
    transition: background-color 0.3s ease, transform 0.1s ease, opacity 0.3s ease;
    text-align: center;
  }

  .game-button.primary {
    background-color: var(--primary-color);
    color: white;
  }

  .game-button.primary:hover:not(:disabled) {
    background-color: #0056b3;
  }

  .game-button.primary:disabled {
    background-color: #ccc;
    cursor: not-allowed;
    opacity: 0.7;
  }

  .game-button.secondary {
    background-color: var(--secondary-color);
    color: white;
  }

  .game-button.secondary:hover {
    background-color: #218838;
  }

  .game-button.tertiary {
      background-color: var(--tertiary-color);
      color: white;
      display: block; /* Make toggle button block */
      width: 100%;
      margin-top: 30px;
      padding: 15px 24px;
  }

  .game-button.tertiary:hover {
    background-color: #5a6268;
  }


  .feedback-area {
    margin-top: 20px;
    padding: 20px;
    border-radius: 8px;
    font-weight: bold;
    opacity: 0; /* Start hidden for animation */
    transform: translateY(10px); /* Start slightly lower */
    transition: opacity 0.5s ease-out, transform 0.5s ease-out;
  }

  .feedback-area.visible {
      opacity: 1;
      transform: translateY(0);
  }

  .feedback-area.correct {
    background-color: #d4edda; /* light green */
    border: 1px solid #c3e6cb;
    color: var(--correct-color);
  }

  .feedback-area.incorrect {
    background-color: #f8d7da; /* light red */
    border: 1px solid #f5c6cb;
    color: var(--incorrect-color);
  }

  .feedback-area p {
      margin-top: 10px;
      font-weight: normal;
      line-height: 1.5;
  }

  .feedback-area strong {
      display: block;
      margin-bottom: 5px;
      font-size: 1.1em;
  }


  .hidden {
    display: none;
  }

   /* Animation for elements fading/sliding out when new question loads */
  .fade-out {
      opacity: 0;
      transform: translateY(-10px);
  }

  @keyframes fadeIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
  }


  .game-card.success {
    background-color: #d1ecf1; /* light blue-green */
    border: 1px solid #bee5eb;
    color: #0c5460;
    text-align: center;
    animation: fadeIn 0.8s ease-out;
  }

  .game-card.success h2 {
      color: #0c5460;
      margin-bottom: 15px;
  }

  .explanation-area {
    margin-top: 30px;
    padding: 25px;
    border: 1px solid var(--border-color);
    border-radius: 12px;
    background-color: #f8f9fa; /* Lighter background for explanation */
    color: var(--text-color);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    transition: opacity 0.5s ease-out;
  }

  .explanation-area h2, .explanation-area h3 {
    color: var(--primary-color);
    margin-bottom: 15px;
    border-bottom: 1px solid #dee2e6;
    padding-bottom: 5px;
  }

  .explanation-area h3 {
      color: #495057; /* Darker gray for subtitles */
      margin-top: 20px;
      margin-bottom: 10px;
      border-bottom: none;
      padding-bottom: 0;
  }

  .explanation-area p {
    margin-bottom: 15px;
  }

  .explanation-area ul {
    margin-bottom: 15px;
    padding-left: 25px;
  }

  .explanation-area li {
    margin-bottom: 10px;
    line-height: 1.5;
  }

  /* Hide explanation content visually when parent is hidden, but allow smooth transition */
   .explanation-area.hidden {
      opacity: 0;
      max-height: 0; /* Collapse height */
      overflow: hidden;
      padding-top: 0;
      padding-bottom: 0;
      margin-top: 10px; /* Adjust margin during collapse */
      transition: opacity 0.5s ease-out, max-height 0.6s ease-out, padding 0.6s ease-out, margin 0.6s ease-out;
   }

   /* State when explanation is visible */
   .explanation-area:not(.hidden) {
       opacity: 1;
       max-height: 2000px; /* Sufficiently large value to allow full content */
       transition: opacity 0.5s ease-out, max-height 0.6s ease-out, padding 0.6s ease-out, margin 0.6s ease-out;
   }


</style>

<script>
  const gameData = [
    {
      scenario: "תיק חקירה מס' 1: קטע מתוך תקציר מאמר - '\n...מחקר זה בחן את הקשר בין שעות שינה בקרב סטודנטים לבין ביצועיהם במבחנים. השתתפו בו 150 סטודנטים מאוניברסיטה אחת. התוצאות הראו שסטודנטים שישנו בממוצע 7-8 שעות בלילה קיבלו ציונים גבוהים יותר מאלו שישנו פחות מ-6 שעות.'",
      question: "מהי שאלת המחקר המרכזית עליה מנסה לענות תיק חקירה זה?",
      options: [
        "האם אוניברסיטאות צריכות לשנות את לוחות הזמנים כדי לאפשר יותר שינה?",
        "מהו הקשר בין כמות שעות השינה לביצועים אקדמיים בקרב סטודנטים?",
        "כמה שעות שינה דרושות כדי לקבל ציון 100 במבחן?",
        "האם שינה איכותית חשובה יותר מכמות שינה?",
      ],
      correctAnswer: 1,
      feedback: "נכון! ✅ הקטע מציג בבירור את הבחינה של הקשר בין שני משתנים: כמות שעות השינה והביצועים במבחנים. זוהי שאלת המחקר המרכזית.<br/><strong>קשר לארגז הכלים:</strong> שאלת המחקר היא הלב של כל חקירה מדעית ומוצגת לרוב במבוא או בתקציר (I בחוקר IMRAD)."
    },
    {
      scenario: "תיק חקירה מס' 2: מתוך חלק ה'שיטות' (Methods) במאמר - '\nהמדגם כלל 30 משתתפים, 15 בקבוצת הטיפול ו-15 בקבוצת הביקורת. המשתתפים גויסו באמצעות מודעה בקמפוס האוניברסיטה.'",
      question: "איזו מגבלה פוטנציאלית משמעותית ניתן לזהות בשיטה זו?",
      options: [
        "המדגם קטן מדי מכדי להסיק מסקנות כלליות על אוכלוסייה רחבה יותר.",
        "שיטת הגיוס (מודעה בקמפוס) עלולה לגרום להטיית דגימה (המדגם לא מייצג את כלל האוכלוסייה הרלוונטית).",
        "מספר המשתתפים בשתי הקבוצות אינו שווה.",
        "גם א' וגם ב' נכונים ויש להם השפעה על יכולת ההכללה."
      ],
      correctAnswer: 3,
      feedback: "נכון מאוד! ✅ שתי הנקודות הללו מהוות מגבלות חמורות. מדגם של 30 איש הוא קטן מאוד, וגיוס דרך מודעה בקמפוס עלול למשוך רק סוג מסוים של סטודנטים (אלה שמגיעים לקמפוס, שמים לב למודעות ומתעניינים בנושא) ולא לייצג נאמנה את כלל אוכלוסיית הסטודנטים. <br/><strong>קשר לארגז הכלים:</strong> גודל מדגם ושיטת דגימה (חלק ה-Methods) הם קריטיים ליכולת להכליל (Generalize) את ממצאי המחקר מעבר למדגם הספציפי."
    },
    {
      scenario: "תיק חקירה מס' 3: כותרת דיווח חדשותי המבוססת על מחקר - '\n'מחקר חדש מצא: אנשים שאוכלים שוקולד שחור חיים יותר!'",
      question: "בהנחה שהמחקר אכן מצא מתאם (קורלציה) חיובי חזק בין צריכת שוקולד שחור לתוחלת חיים ארוכה יותר, מה הבעיה העיקרית בהסקה שבכותרת?",
      options: [
        "המחקר בוודאי מומן על ידי חברת שוקולד ולכן מוטה.",
        "קורלציה אינה סיבתיות – ייתכן שקיים גורם שלישי המשפיע גם על אכילת שוקולד שחור וגם על תוחלת חיים (למשל, רמת הכנסה גבוהה יותר שמאפשרת רכישת שוקולד יקר יותר וגם גישה טובה יותר לשירותי בריאות).",
        "שוקולד שחור מכיל הרבה סוכר, ולכן לא ייתכן שהוא בריא (זו הנחה לא תמיד נכונה לגבי שוקולד שחור).",
        "הכותרת לא מציינת את גודל המדגם, וזה הליקוי היחיד."
      ],
      correctAnswer: 1,
      feedback: "מדויק! ✅ זוהי הדוגמה הקלאסית לפער בין 'חברות' (קורלציה) ל'גרימה' (סיבתיות). גם אם שני דברים קשורים סטטיסטית, זה לא אומר שאחד הוא הסיבה לשני. בלש טוב תמיד יחשוד בגורמים חיצוניים נסתרים (משתנים מתאמים או מבלבלים) שיכולים להסביר את הקשר שנמצא. <br/><strong>קשר לארגז הכלים:</strong> זכרו תמיד: קורלציה אינה סיבתיות! (Correlation is not causation!) - כלל ברזל בפענוח מדעי."
    },
    {
      scenario: "תיק חקירה מס' 4: מתוך חלק ה'תוצאות' (Results) וה'דיון' (Discussion) של מאמר - '\nניסוי בדק יעילות של תרופה חדשה להורדת לחץ דם. התוצאה המרכזית הראתה ירידה ממוצעת של 2 ממ\"כ (מילימטר כספית) בלחץ הדם הסיסטולי בקבוצת הטיפול לעומת קבוצת הביקורת. הבדל זה נמצא מובהק סטטיסטית (p = 0.04). החוקרים הסיקו בדיון כי התרופה יעילה משמעותית בהורדת לחץ דם.'",
      question: "מהו הניתוח הביקורתי הנכון ביותר של הסקה זו מנקודת מבט של בלש מדעי?",
      options: [
        "ההסקה נכונה לחלוטין, מכיוון שהתוצאה מובהקת סטטיסטית (p < 0.05).",
        "ההסקה עשויה להיות מוגזמת – למרות שההבדל מובהק סטטיסטית, ירידה של 2 ממ\"כ בלבד עשויה להיות קטנה ולא משמעותית מבחינה קלינית או מעשית (גודל אפקט קטן).",
        "המחקר בוודאי לא היה עיוור (Blind), אחרת ההבדל בין הקבוצות היה גדול יותר.",
        "המדגם היה קטן מדי, ולכן התוצאה אינה מהימנה סטטיסטית (סותר את נתון ה-p)."
      ],
      correctAnswer: 1,
      feedback: "פענוח מוצלח! ✅ זוהי מלכודת נפוצה. מובהקות סטטיסטית (p-value) רק אומרת שהתוצאה שהתקבלה כנראה אינה מקרית. היא לא אומרת כלום על גודל ההבדל או על החשיבות המעשית/קלינית שלו. ירידה של 2 ממ\"כ, למרות שהיא מובהקת סטטיסטית (במיוחד במדגם גדול), היא לרוב קטנה מכדי להיחשב משמעותית בפועל לרוב החולים. תמיד בדקו גם את גודל האפקט (גם אם הוא לא מוצג ישירות, ניתן להעריך אותו מהתוצאות).<br/><strong>קשר לארגז הכלים:</strong> הבחינו בין מובהקות סטטיסטית למובהקות מעשית או קלינית – בדקו את גודל האפקט."
    }
  ];

  let currentQuestionIndex = 0;

  const gameArea = document.getElementById('game-area');
  const scenarioElement = document.getElementById('scenario');
  const questionElement = document.getElementById('question');
  const optionsElement = document.getElementById('options');
  const checkAnswerButton = document.getElementById('check-answer');
  const feedbackElement = document.getElementById('feedback');
  const nextQuestionButton = document.getElementById('next-question');
  const gameEndElement = document.getElementById('game-end');
  const toggleExplanationButton = document.getElementById('toggle-explanation');
  const theoreticalExplanationElement = document.getElementById('theoretical-explanation');
  const progressElement = document.getElementById('progress');

  function updateProgress() {
      progressElement.textContent = `תיק ${currentQuestionIndex + 1} מתוך ${gameData.length}`;
  }

  function loadQuestion(index) {
    if (index >= gameData.length) {
      endGame();
      return;
    }

    const data = gameData[index];

    // Add fade-out class to current elements before removing them
    scenarioElement.classList.add('fade-out');
    questionElement.classList.add('fade-out');
    optionsElement.classList.add('fade-out');
    feedbackElement.classList.add('fade-out'); // Hide feedback smoothly

    // Wait for fade-out transition before changing content
    setTimeout(() => {
        scenarioElement.innerHTML = data.scenario;
        questionElement.textContent = data.question;
        optionsElement.innerHTML = '';
        feedbackElement.classList.remove('visible', 'correct', 'incorrect'); // Remove feedback classes
        feedbackElement.classList.add('hidden'); // Ensure display: none after transition
        feedbackElement.style.opacity = ''; // Reset opacity for next show
        feedbackElement.style.transform = ''; // Reset transform for next show

        nextQuestionButton.classList.add('hidden');
        checkAnswerButton.classList.remove('hidden');
        checkAnswerButton.disabled = true;

        data.options.forEach((option, i) => {
          const label = document.createElement('label');
          const input = document.createElement('input');
          input.type = 'radio';
          input.name = 'answer';
          input.value = i;
          input.addEventListener('change', () => {
            checkAnswerButton.disabled = false;
          });
          const span = document.createElement('span');
          span.textContent = option;
          label.appendChild(input);
          label.appendChild(span);
          optionsElement.appendChild(label);
        });

        updateProgress();

        // Remove fade-out and add fade-in for new content
        scenarioElement.classList.remove('fade-out');
        questionElement.classList.remove('fade-out');
        optionsElement.classList.remove('fade-out');
        // Fade-in handled by CSS keyframes on initial load and class removal here
        scenarioElement.style.animation = 'fadeIn 0.6s ease-out';
        questionElement.style.animation = 'fadeIn 0.6s ease-out 0.2s backwards';
        optionsElement.style.animation = 'fadeIn 0.6s ease-out 0.4s backwards';

         // Reset animations after they run
        setTimeout(() => {
             scenarioElement.style.animation = '';
             questionElement.style.animation = '';
             optionsElement.style.animation = '';
        }, 600);


    }, 500); // Match the fade-out transition duration
  }

  function checkAnswer() {
    const selectedOption = optionsElement.querySelector('input[name="answer"]:checked');
    if (!selectedOption) {
      return; // Should not happen due to disabled button
    }

    const selectedAnswerIndex = parseInt(selectedOption.value);
    const data = gameData[currentQuestionIndex];

    // Disable all radio buttons
    optionsElement.querySelectorAll('input[name="answer"]').forEach(input => input.disabled = true);

    // Add classes for visual feedback on selected option (optional but good)
    optionsElement.querySelectorAll('label').forEach((label, index) => {
        if (index === selectedAnswerIndex) {
            label.style.fontWeight = 'bold';
            if (selectedAnswerIndex === data.correctAnswer) {
                label.style.borderColor = varcss('--correct-color');
                label.style.backgroundColor = '#e9f7ef'; /* Light green background */
            } else {
                 label.style.borderColor = varcss('--incorrect-color');
                 label.style.backgroundColor = '#fdeee9'; /* Light red background */
            }
        } else if (index === data.correctAnswer) {
             // Highlight correct answer if incorrect option was chosen
             label.style.borderColor = varcss('--correct-color');
             label.style.backgroundColor = '#e9f7ef';
        }
    });


    feedbackElement.innerHTML = ''; // Clear previous feedback
    feedbackElement.classList.remove('hidden', 'correct', 'incorrect', 'fade-out'); // Clean up classes
    feedbackElement.classList.add('visible'); // Prepare for animation

    if (selectedAnswerIndex === data.correctAnswer) {
      feedbackElement.classList.add('correct');
      feedbackElement.innerHTML = `<strong>נכון! ✅</strong> ${data.feedback}`;
    } else {
      feedbackElement.classList.add('incorrect');
      feedbackElement.innerHTML = `<strong>טעות ❌</strong> התשובה הנכונה היא: ${data.options[data.correctAnswer]}.<br/> ${data.feedback}`;
    }

    checkAnswerButton.classList.add('hidden');
    nextQuestionButton.classList.remove('hidden');

    // Smooth scroll to feedback? Maybe too much animation. Let's skip for now.
    // feedbackElement.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  function nextQuestion() {
    // Reset styles on options from previous question feedback
     optionsElement.querySelectorAll('label').forEach((label) => {
         label.style.fontWeight = '';
         label.style.borderColor = '';
         label.style.backgroundColor = '';
     });

    currentQuestionIndex++;
    loadQuestion(currentQuestionIndex);
  }

  function endGame() {
    gameArea.classList.add('hidden');
    gameEndElement.classList.remove('hidden');
     gameEndElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  function toggleExplanation() {
    theoreticalExplanationElement.classList.toggle('hidden');
    // Optional: Scroll to explanation when revealed
    if (!theoreticalExplanationElement.classList.contains('hidden')) {
       setTimeout(() => { // Wait for display block before scrolling
          theoreticalExplanationElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
       }, 50);
    }
  }

   // Helper to get CSS variable value
   function varcss(name) {
       return getComputedStyle(document.documentElement).getPropertyValue(name).trim();
   }


  checkAnswerButton.addEventListener('click', checkAnswer);
  nextQuestionButton.addEventListener('click', nextQuestion);
  toggleExplanationButton.addEventListener('click', toggleExplanation);

  // Initial load
  loadQuestion(currentQuestionIndex);
</script>
```