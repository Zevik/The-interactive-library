---
title: "מי אני? אתגר זיהוי שלדי דינוזאורים"
english_slug: who-am-i-dinosaur-skeleton-identification
category: "פלאונטולוגיה"
tags: [דינוזאורים, שלדים, פלאונטולוגיה, מאובנים, זיהוי, משחק]
---
# מי אני? אתגר זיהוי שלדי דינוזאורים

היי, חוקר דינוזאורים צעיר! האם אתה מוכן למסע בזמן לעולם ששלטו בו יצורים ענקיים? שלדי הדינוזאורים הם כמו חתימות קדומות - לכל אחד מבנה ייחודי שסיפר סיפור על חייו. עכשיו תורך להיות הפלאונטולוג! האם תצליח לזהות את הדינוזאורים האגדיים רק על פי השלד המאובן שלהם? בוא נשחק ונראה!

<div id="quiz-container" class="quiz-container">
    <div id="quiz-header" class="quiz-header">
        <span id="progress"></span>
        <span id="score">ניקוד: 0</span>
    </div>
    <div id="skeleton-area" class="skeleton-area">
        <img id="dinosaur-skeleton" src="" alt="שלד דינוזאור" class="skeleton-image">
    </div>
    <div id="options-container" class="options-container">
        <!-- Buttons will be added here by JS -->
    </div>
    <div id="feedback" class="feedback">
        <!-- Feedback message here -->
    </div>
    <button id="next-button" class="control-button next-button" style="display:none;">השאלה הבאה</button>
    <div id="completion-message" class="completion-message" style="display:none;">
        כל הכבוד! סיימת את האתגר בהצלחה! <br> האם למדת לזהות את ענקי העבר?
    </div>
</div>

<style>
/* General styles for the container */
.quiz-container {
    font-family: 'Arial', sans-serif; /* Using a common sans-serif font */
    direction: rtl;
    text-align: right;
    padding: 30px;
    border: 1px solid #dcdcdc; /* Softer border */
    border-radius: 12px; /* More rounded corners */
    max-width: 650px; /* Slightly wider */
    margin: 30px auto; /* More margin */
    background-color: #ffffff; /* White background */
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); /* Soft shadow */
    position: relative; /* Needed for potential absolute positioning */
}

/* Header with score and progress */
.quiz-header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
    font-size: 1em;
    color: #555;
}

#progress {
    font-weight: bold;
    color: #007bff; /* Blue color for progress */
}

#score {
    font-weight: bold;
    color: #28a745; /* Green color for score */
}


/* Skeleton image area */
.skeleton-area {
    text-align: center; /* Center the image */
    margin-bottom: 25px;
    min-height: 300px; /* Ensure space even before image loads */
    display: flex;
    align-items: center;
    justify-content: center;
}

.skeleton-image {
    max-width: 100%;
    max-height: 380px; /* Slightly increased max height */
    display: block;
    /* Added transition for smoother image loading/changing */
    opacity: 1;
    transition: opacity 0.5s ease-in-out;
}

.skeleton-image.loading {
    opacity: 0.5; /* Indicate loading state */
}


/* Options buttons container */
.options-container {
    text-align: center;
    margin-top: 20px;
}

.options-container button {
    display: block;
    width: 90%; /* Make buttons wider */
    margin: 12px auto; /* More vertical space */
    padding: 14px 25px; /* Larger padding */
    font-size: 1.1em; /* Slightly larger font */
    cursor: pointer;
    border: none; /* No default border */
    border-radius: 8px; /* More rounded */
    background-color: #007bff; /* Primary blue */
    color: white;
    transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease; /* Smooth transitions */
    box-shadow: 0 2px 5px rgba(0, 123, 255, 0.2); /* Subtle shadow */
}

.options-container button:hover:not(:disabled) {
    background-color: #0056b3; /* Darker blue on hover */
    transform: translateY(-2px); /* Lift effect on hover */
    box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3);
}

.options-container button:active:not(:disabled) {
    transform: translateY(0); /* Press effect */
    box-shadow: 0 2px 5px rgba(0, 123, 255, 0.2);
}

.options-container button:disabled {
    cursor: not-allowed;
    opacity: 0.6;
    background-color: #cccccc; /* Grey out disabled buttons */
    color: #666666;
    box-shadow: none;
    transform: none;
}

/* Styling for correct/incorrect buttons after selection */
.options-container button.correct {
    background-color: #28a745; /* Green */
    border-color: #218838;
    color: white;
    box-shadow: 0 2px 5px rgba(40, 167, 69, 0.3);
}

.options-container button.incorrect {
    background-color: #dc3545; /* Red */
    border-color: #c82333;
    color: white;
    box-shadow: 0 2px 5px rgba(220, 53, 69, 0.3);
}


/* Feedback area */
.feedback {
    text-align: center;
    margin-top: 20px; /* More space above feedback */
    min-height: 2em; /* Ensure space even when empty */
    font-size: 1.1em;
    font-weight: bold;
    transition: color 0.5s ease, opacity 0.5s ease; /* Smooth transitions */
    opacity: 0; /* Start hidden */
}

.feedback.visible {
    opacity: 1; /* Fade in */
}

.feedback-correct {
    color: #28a745; /* Green */
}

.feedback-incorrect {
    color: #dc3545; /* Red */
    /* Added a slight shake animation for incorrect */
    animation: shake 0.5s;
}

@keyframes shake {
  0%, 100% { transform: translateX(0); }
  10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
  20%, 40%, 60%, 80% { transform: translateX(5px); }
}

/* Control buttons (Next, Toggle Explanation) */
.control-button {
    display: block;
    width: fit-content;
    margin: 25px auto 10px auto; /* Adjusted margin */
    padding: 12px 25px; /* Larger padding */
    font-size: 1.1em; /* Larger font */
    cursor: pointer;
    border: none; /* No default border */
    border-radius: 8px; /* More rounded */
    background-color: #17a2b8; /* Info blue/teal */
    color: white;
    transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease; /* Smooth transitions */
    box-shadow: 0 2px 5px rgba(23, 162, 184, 0.2); /* Subtle shadow */
}

.control-button:hover {
    background-color: #138496; /* Darker teal on hover */
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(23, 162, 184, 0.3);
}
.control-button:active {
     transform: translateY(0);
     box-shadow: 0 2px 5px rgba(23, 162, 184, 0.2);
}

/* Specific style for Next button if needed (optional) */
.next-button {
    background-color: #28a745; /* Green */
    box-shadow: 0 2px 5px rgba(40, 167, 69, 0.2);
}
.next-button:hover {
    background-color: #218838; /* Darker green */
    box-shadow: 0 4px 8px rgba(40, 167, 69, 0.3);
}
.next-button:active {
     box-shadow: 0 2px 5px rgba(40, 167, 69, 0.2);
}


/* Completion Message */
.completion-message {
    display: none;
    text-align: center;
    font-size: 1.5em; /* Larger font */
    color: #28a745; /* Green */
    margin-top: 30px; /* More space */
    font-weight: bold;
    padding: 20px;
    border: 2px dashed #28a745; /* Dashed border */
    border-radius: 10px;
    background-color: #e9f7ef; /* Light green background */
}

/* Explanation section */
#explanation {
    margin-top: 40px; /* More space above */
    padding: 25px; /* More padding */
    border: 1px solid #ddd;
    border-radius: 10px; /* More rounded */
    background-color: #f8f9fa; /* Light grey background */
    direction: rtl;
    text-align: right;
}

#explanation h2, #explanation h3 {
    color: #343a40; /* Darker headings */
    margin-bottom: 18px; /* More space below headings */
    border-bottom: 2px solid #007bff; /* Blue underline */
    padding-bottom: 8px;
}

#explanation p {
    margin-bottom: 18px; /* More space between paragraphs */
    line-height: 1.7; /* Increased line height for readability */
    color: #495057; /* Slightly darker text */
}

#explanation ul {
    margin-bottom: 18px;
    padding-right: 20px; /* Indent list */
}

#explanation li {
    margin-bottom: 8px;
    line-height: 1.6;
    color: #495057;
}

#explanation ul ul {
    margin-bottom: 8px;
}

</style>

<button id="toggle-explanation" class="control-button">הצג הסבר על זיהוי שלדי דינוזאורים</button>

<div id="explanation" style="display:none;">
    <h2>כיצד שלדי דינוזאורים מספרים לנו סיפור? מבט פלאונטולוגי</h2>
    <p>שלדי הדינוזאורים הם לא רק עצמות עתיקות - הם חלונות נדירים אל עולם נכחד, ספרים כתובים באבן המגלים לנו סודות על ענקי העבר ששלטו בכדור הארץ לפני עשרות ומאות מיליוני שנים. כל פרט בשלד, מצורת הגולגולת ועד קצה הזנב, מהווה רמז קריטי לאורח חייו, סביבתו ואף התנהגותו של היצור הקדום. בואו נצלול עמוק יותר!</p>

    <h3>מסע האבן: כיצד שלד הופך למאובן ומה הוא חושף</h3>
    <p>רוב היצורים שנכחדו לא השאירו זכר. רק בתנאים יוצאי דופן - כמו קבורה מהירה במשקעים (בוץ, חול, אפר וולקני) המונעת חמצון והתפרקות - יכול שלד להתאבן. בתהליך איטי ומדהים, מים מחלחלים דרך העצמות ומחליפים בהדרגה את החומר האורגני המקורי במינרלים קשיחים. התוצאה היא מאובן: העתק מדויק מאבן של העצם המקורית. מאובנים אלו הם עדות כמעט יחידה לדינוזאורים. הם מאפשרים לנו לשחזר את צורתם החיצונית, לאמוד את גודלם ומשקלם, לשער את תנועתם, להבין את תזונתם (אילו שיניים היו להם? מבנה הלסת?), ואפילו לשפוך אור על התנהגויות כמו חיים בעדרים או דאגה לצאצאים, אם מוצאים מספר שלדים יחד או עדויות לקינים וביצים.</p>

    <h3>המפתח לזיהוי: מאפייני שלד בסיסיים</h3>
    <p>שלד הדינוזאור הוא המדריך הראשי לזיהויו:</p>
    <ul>
        <li>**גודל ופרופורציות:** האם ענק או קטן? צוואר ארוך או קצר? זנב ארוך וקשיח או קצר וגמיש? רגליים קדמיות ארוכות יותר מהאחוריות או להפך?</li>
        <li>**הגולגולת:** אולי החלק המרכזי בזיהוי. צורתה (ארוכה/קצרה, כבדה/קלה), גודלה ביחס לגוף, מבנה הלסתות (עדינות/חזקות), וחשוב מכל - השיניים (חדות ומעוקלות לטורפים, שטוחות או דמויות עלה לצמחוניים), ומאפיינים ייחודיים כמו קרניים, בליטות, או מניפות גרמיות.</li>
        <li>**מבנה האגן והגפיים:** מבנה האגן קובע האם הדינוזאור היה הולך על שתיים (דו-רגלי) או ארבע (ארבע-רגלי). מבנה כפות הרגליים והידיים, נוכחות טפרים (חדים לטורפים, רחבים או דמויי פרסה לצמחוניים) ואורך האצבעות מספקים רמזים על תנועה, ציד, אחיזה או הגנה.</li>
        <li>**שריון ומבנים מיוחדים:** לוחות גרמיות על הגב, קוצים, שריון כבד, מניפות עצם על הראש או הגב - כל אלו התפתחו כהגנה מפני טורפים והם סימני זיהוי מובהקים.</li>
    </ul>

    <h3>מי אכל מה? הבדלים מבניים בין טורפים לצמחוניים</h3>
    <p>השלד מגלה רבות על התפריט:</p>
    <ul>
        <li><strong>טורפים (תרפודים):</strong> שלדים אלו מעוצבים לצוד ולהרוג. גולגולת גדולה וחזקה, לסתות עם שיניים חדות, משוננות ומעוקלות לקריעת בשר, וטפרים חדים בכפות הרגליים והידיים. לרוב היו דו-רגליים עם זנב ארוך לאיזון בזמן ריצה ורדיפה. דוגמאות: טירנוזאורוס רקס, ולוצירפטור.</li>
        <li><strong>צמחוניים:</strong> מגוונים מאוד במבנה השלד, בהתאם לאסטרטגיות הגנה ואכילה.
            <ul>
                <li><strong>אורניתיסקיה:</strong> לרוב בעלי מבנה דמוי מקור בחזית הפה לקטיפת צמחייה. רבים פיתחו שריון, קרניים או מבנים גרמיים מרשימים אחרים להגנה. רובם ארבע-רגליים, אם כי חלקם (כמו האיגואנודון) יכלו לעמוד על שתיים. דוגמאות: טריצרטופס, סטגוזאורוס, אנקילוזאורוס.</li>
                <li><strong>סאורופודים:</strong> הענקים האמיתיים. צמחוניים ארבע-רגליים עם גוף מסיבי, צוואר וזנב ארוכים במיוחד (כדי להגיע לצמחייה גבוהה או להשתמש בזנב כשוט הגנה/איזון), וגולגולת קטנה יחסית עם שיניים מותאמות יותר לתלישה מאשר ללעיסה. דוגמאות: ברכיוזאורוס, אפטוזאורוס.</li>
            </ul>
        </li>
    </ul>

     <h3>מעבר לדינוזאורים: זוחלים קדומים מעופפים וימיים</h3>
    <p>חשוב לזכור שלא כל זוחל קדום הוא דינוזאור! זוחלים מעופפים כמו פטרוזאורים (דוגמת פטרודקטיל או פטרנודון) וזוחלים ימיים גדולים (איכטיוזאורים, פלסיוזאורים, מוזאזאורים) חיו באותה תקופה אך שייכים לקבוצות זוחלים אחרות. השלדים שלהם מותאמים באופן קיצוני לתנועה באוויר או במים (למשל, כנפיים נתמכות על ידי אצבע אחת ארוכה במיוחד אצל פטרוזאורים, או גפיים דמויות סנפירים אצל זוחלים ימיים) והם שונים מאוד משלדי הדינוזאורים.</p>

    <h3>השלדים ככרוניקה של האבולוציה</h3>
    <p>השוואת שלדי דינוזאורים מתקופות גיאולוגיות שונות ובמקומות שונים בעולם היא לב עבודת הפלאונטולוגים. זה מאפשר למפות את "עץ המשפחה" של הדינוזאורים, להבין כיצד קבוצות התפתחו והתפצלו, כיצד התפשטו ברחבי היבשות, וכיצד שינו את צורתם ומאפייניהם בתגובה לשינויים סביבתיים ולאבולוציה של צמחים ובעלי חיים אחרים. השלדים הם העדות המוחשית היחידה שלנו לתור הזהב של הדינוזאורים, שהגיע לסופו עם הכחדה המונית דרמטית לפני כ-66 מיליון שנה. לימודם הוא מסע בלשי מרתק אל העבר הרחוק.</p>
</div>

<script>
const dinosaurs = [
    {
        name: "טירנוזאורוס רקס (T-Rex)",
        image: "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Tyrannosaurus_rex_silhouette.svg/langhe-280px-Tyrannosaurus_rex_silhouette.svg.png",
        correctAnswer: "טירנוזאורוס רקס (T-Rex)",
        options: ["טירנוזאורוס רקס (T-Rex)", "טריצרטופס", "ברכיוזאורוס", "סטגוזאורוס"],
        feedback_correct: "מעולה! זיהוי מושלם! אין לטעות בגולגולת הענקית והעצמות החזקות של מלך הטורפים.",
        feedback_incorrect: "קרוב, אבל לא מדויק. שימו לב למבנה הגולגולת הענקית והשיניים החדות - זה סימן מובהק לטורף-על כמו הטי-רקס. צמחונים כמו טריצרטופס או ברכיוזאורוס נראים שונה לגמרי."
    },
    {
        name: "טריצרטופס",
        image: "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Triceratops_Prorsus_restoration.svg/langhe-280px-Triceratops_Prorsus_restoration.svg.png",
        correctAnswer: "טריצרטופס",
        options: ["סטגוזאורוס", "טריצרטופס", "ולוצירפטור", "אנקילוזאורוס"],
        feedback_correct: "יפה מאוד! הקרניים המאיימות והמניפה הגרמית הגדולה (פריל) הן כרטיס הביקור הבלעדי של הטריצרטופס הצמחוני.",
        feedback_incorrect: "נסו שוב להסתכל על הראש. הקרניים והמניפה הגרמית הן מאפיין ייחודי של הטריצרטופס, ששימשו כנראה להגנה או לתצוגה. סטגוזאורוס מזוהה על פי לוחות הגב, וולוצירפטור קטן בהרבה."
    },
    {
        name: "סטגוזאורוס",
        image: "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Stegosaurus_stenops_dorsal.svg/langhe-280px-Stegosaurus_stenops_dorsal.svg.png",
        correctAnswer: "סטגוזאורוס",
        options: ["ברכיוזאורוס", "טירנוזאורוס רקס (T-Rex)", "סטגוזאורוס", "טריצרטופס"],
        feedback_correct: "מצוין! אלו הלוחות הגרמיות הייחודיות על הגב והקוצים בזנב (טאג'ומיזר) שמגלים מיד שמדובר בסטגוזאורוס המרשים.",
        feedback_incorrect: "כמעט, אבל לא נכון. הלוחות והקוצים על הגב והזנב הם סימן היכר מובהק של הסטגוזאורוס הצמחוני. ברכיוזאורוס הוא ענק בעל צוואר ארוך, וטי-רקס הוא טורף איום."
    },
     {
        name: "ברכיוזאורוס",
        image: "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Brachiosaurus_altithorax_outline.svg/langhe-280px-Brachiosaurus_altithorax_outline.svg.png",
        correctAnswer: "ברכיוזאורוס",
        options: ["סטגוזאורוס", "ברכיוזאורוס", "ולוצירפטור", "אפטוזאורוס"],
        feedback_correct: "בדיוק! רק הברכיוזאורוס מתהדר בצוואר ארוך כל כך וברגליים קדמיות הגבוהות מהאחוריות, מה שנתן לו מראה של ג'ירף ענקי מהעבר.",
        feedback_incorrect: "זוהי טעות נפוצה! שימו לב לצוואר הארוך במיוחד ולרגליים הקדמיות שהן ארוכות יותר מהאחוריות. זהו הברכיוזאורוס הענק, צמחוני שהגיע לצמרות העצים. סטגוזאורוס וולוצירפטור שונים ממנו באופן מהותי."
    },
    {
        name: "ולוצירפטור",
        image: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Velociraptor_mongoliensis_dorsal.svg/langhe-280px-Velociraptor_mongoliensis_dorsal.svg.png",
        correctAnswer: "ולוצירפטור",
        options: ["טריצרטופס", "ברכיוזאורוס", "ולוצירפטור", "טירנוזאורוס רקס (T-Rex)"],
        feedback_correct: "מעולה! זיהוי מדויק! השלד הקטן והזריז עם הטופר הגדול והמעוקל ברגל (sickle claw) שייך לולוצירפטור המהיר.",
        feedback_incorrect: "נסו שוב. שלד זה קטן בהרבה מהאחרים והוא כולל טופר גדול ומעוקל על אצבע אחת ברגל, המעיד על טורף זריז ממשפחת הדרומאוזאוריים, כמו הולוצירפטור. טריצרטופס וברכיוזאורוס ענקיים וצמחוניים."
    },
     {
        name: "פטרודקטיל (לא דינוזאור!)",
        image: "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Pterodactylus_antiquus_outline.svg/langhe-280px-Pterodactylus_antiquus_outline.svg.png",
        correctAnswer: "פטרודקטיל (לא דינוזאור!)",
        options: ["ולוצירפטור", "סטגוזאורוס", "פטרודקטיל (לא דינוזאור!)", "ברכיוזאורוס"],
        feedback_correct: "נכון מאוד! הפתעת המערכת! זוהי לא דינוזאור כלל, אלא פטרוזאור, זוחל מעופף קדום. מבנה הכנף הנתמכת על ידי אצבע אחת ארוכה במיוחד הוא סימן הזיהוי שלו.",
        feedback_incorrect: "שימו לב למבנה המיוחד של הגפיים הקדמיות. זהו לא דינוזאור יבשתי כמו ולוצירפטור או סטגוזאורוס, אלא פטרוזאור מעופף! הכנפיים שלו נתמכו על ידי אצבע רביעית ארוכה במיוחד."
    }
];

let currentQuestionIndex = 0;
let score = 0;
const totalQuestions = dinosaurs.length;

const skeletonImg = document.getElementById('dinosaur-skeleton');
const optionsContainer = document.getElementById('options-container');
const feedbackDiv = document.getElementById('feedback');
const nextButton = document.getElementById('next-button');
const completionMessageDiv = document.getElementById('completion-message');
const toggleExplanationButton = document.getElementById('toggle-explanation');
const explanationDiv = document.getElementById('explanation');
const scoreSpan = document.getElementById('score');
const progressSpan = document.getElementById('progress');


function loadQuestion(index) {
    if (index >= totalQuestions) {
        endQuiz();
        return;
    }

    const dinosaur = dinosaurs[index];

    // Hide previous feedback and next button immediately
    feedbackDiv.classList.remove('visible', 'feedback-correct', 'feedback-incorrect');
    feedbackDiv.textContent = ''; // Clear text content
    nextButton.style.display = 'none';

    // Add loading class for image transition
    skeletonImg.classList.add('loading');

    // Set image source and remove loading class when loaded
    skeletonImg.onload = () => {
        skeletonImg.classList.remove('loading');
    };
    skeletonImg.src = dinosaur.image;

    optionsContainer.innerHTML = '';
    completionMessageDiv.style.display = 'none';

    // Update progress indicator
    progressSpan.textContent = `שאלה ${index + 1} מתוך ${totalQuestions}`;

    // Shuffle options
    const shuffledOptions = shuffleArray([...dinosaur.options]);

    shuffledOptions.forEach(option => {
        const button = document.createElement('button');
        button.textContent = option;
        button.addEventListener('click', () => handleAnswer(button, option, dinosaur.correctAnswer, dinosaur.feedback_correct, dinosaur.feedback_incorrect));
        optionsContainer.appendChild(button);
    });
}

function handleAnswer(clickedButton, selectedAnswer, correctAnswer, feedbackCorrect, feedbackIncorrect) {
    disableOptions(); // Disable all options after first click

    if (selectedAnswer === correctAnswer) {
        score++; // Increase score for correct answer
        scoreSpan.textContent = `ניקוד: ${score}`; // Update score display
        feedbackDiv.textContent = feedbackCorrect;
        feedbackDiv.className = 'feedback visible feedback-correct'; // Add correct classes
        clickedButton.classList.add('correct'); // Highlight correct button
    } else {
        feedbackDiv.textContent = feedbackIncorrect;
        feedbackDiv.className = 'feedback visible feedback-incorrect'; // Add incorrect classes
        clickedButton.classList.add('incorrect'); // Highlight incorrect button
        // Also highlight the correct answer
        optionsContainer.querySelectorAll('button').forEach(button => {
            if (button.textContent === correctAnswer) {
                 button.classList.add('correct');
            }
        });
    }

    nextButton.style.display = 'block'; // Show next button
}

function disableOptions() {
    optionsContainer.querySelectorAll('button').forEach(button => {
        button.disabled = true;
    });
}

function nextQuestion() {
    currentQuestionIndex++;
    loadQuestion(currentQuestionIndex);
}

function endQuiz() {
    skeletonImg.style.display = 'none';
    optionsContainer.style.display = 'none';
    feedbackDiv.style.display = 'none'; // Hide feedback
    nextButton.style.display = 'none'; // Hide next button
    progressSpan.style.display = 'none'; // Hide progress

    completionMessageDiv.style.display = 'block'; // Show completion message
    completionMessageDiv.innerHTML = `כל הכבוד! סיימת את האתגר בהצלחה!<br>הניקוד הסופי שלך: <strong>${score} מתוך ${totalQuestions}</strong><br>האם למדת לזהות את ענקי העבר?`;

     // Optional: Reset button to start over? (Not requested, but good for game-like feel)
     // Add a reset button dynamically
}

// Fisher-Yates (aka Knuth) Shuffle
function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]]; // Swap elements
    }
    return array;
}

// Event listeners
nextButton.addEventListener('click', nextQuestion);

toggleExplanationButton.addEventListener('click', () => {
    const isHidden = explanationDiv.style.display === 'none';
    explanationDiv.style.display = isHidden ? 'block' : 'none';
    toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר על זיהוי שלדי דינוזאורים' : 'הצג הסבר על זיהוי שלדי דינוזאורים';
});

// Initial load
loadQuestion(currentQuestionIndex);
</script>