---
title: "מיהו המחבר הסודי? משחק זיהוי סגנוני"
english_slug: who-is-the-secret-author-stylometry-game
category: "בלשנות"
tags:
  - סטילומטריה
  - ניתוח סגנוני
  - זיהוי מחבר
  - בלשנות משפטית
  - ניתוח טקסט
---
# מיהו המחבר הסודי? הדמיית זיהוי סגנוני

האם מילים יכולות להיות טביעת האצבע הנסתרת שלנו? דמיינו עולם שבו טקסט אנונימי מסגיר את כותבו רק על סמך האופן שבו הוא כתוב. בואו להיות בלשים ספרותיים וגלו כיצד חוקרים מפענחים תעלומות היסטוריות ומשפטיות באמצעות דפוסי שפה סמויים. ההדמיה הזו מזמינה אתכם לצלול לתוך עולם הסטילומטריה ולהתנסות בעקרונותיו בעצמכם.

<div id="app-container" lang="he" dir="rtl">
    <h2 class="section-title">התעלומה: זיהוי הכותב המסתורי</h2>
    <p class="intro-text">לפניכם מקטע טקסט שזהות מחברו נעלמה בערפל, ולצדו שלושה מקטעים ממחברים ידועים. המשימה שלכם: לפצח את התעלומה ולגלות מיהו המחבר האמיתי של הטקסט האנונימי, אך ורק על סמך ניתוח דפוסי הכתיבה.</p>

    <div class="text-section">
        <h3 class="section-subtitle">הממצא: טקסט אנונימי</h3>
        <div id="anonymous-text" class="text-block">
            <!-- טקסט אנונימי יוכנס לכאן -->
        </div>
    </div>

    <div class="text-section">
        <h3 class="section-subtitle">החשודים: מקטעי טקסט ממחברים ידועים</h3>
        <div class="known-authors-container">
            <div class="author-text-block" data-author="authorA">
                <h4>מחבר א'</h4>
                <div id="author-a-text" class="text-block">
                    <!-- טקסט מחבר א' יוכנס לכאן -->
                </div>
            </div>
            <div class="author-text-block" data-author="authorB">
                <h4>מחבר ב'</h4>
                <div id="author-b-text" class="text-block">
                    <!-- טקסט מחבר ב' יוכנס לכאן -->
                </div>
            </div>
            <div class="author-text-block" data-author="authorC">
                <h4>מחבר ג'</h4>
                <div id="author-c-text" class="text-block">
                    <!-- טקסט מחבר ג' יוכנס לכאן -->
                </div>
            </div>
        </div>
    </div>

    <div class="analysis-controls">
        <h3 class="section-subtitle">כלי הניתוח: בחרו מאפיינים לבדיקה</h3>
        <div class="checkbox-group">
             <label class="checkbox-label"><input type="checkbox" class="analysis-feature" data-feature="freqWords"> תדירות מילים נפוצות (כמו: ה, ו, את, של, על, ב, כי, אשר)</label>
             <label class="checkbox-label"><input type="checkbox" class="analysis-feature" data-feature="avgSentenceLength"> אורך משפט ממוצע</label>
             <label class="checkbox-label"><input type="checkbox" class="analysis-feature" data-feature="avgWordLength"> אורך מילה ממוצע</label>
             <label class="checkbox-label"><input type="checkbox" class="analysis-feature" data-feature="punctuation"> שימוש בסימני פיסוק (., ,, !, ?, -, ;)</label>
        </div>
        <button id="analyze-button" class="action-button analyze-button">בצע ניתוח סגנוני</button>
         <div id="analysis-loading" class="loading-indicator hidden"></div>
    </div>

    <div class="analysis-results hidden">
        <h3 class="section-subtitle">תוצאות המעבדה הסטילומטרית:</h3>
        <div class="results-container">
             <table id="results-table">
                <thead>
                    <tr>
                        <th>מאפיין</th>
                        <th>אנונימי</th>
                        <th>מחבר א'</th>
                        <th>מחבר ב'</th>
                        <th>מחבר ג'</th>
                    </tr>
                </thead>
                <tbody>
                    <!-- תוצאות יוכנסו לכאן -->
                </tbody>
            </table>
             <p id="no-features-selected-message" class="info-message">בחר מאפיינים לניתוח ולחץ "בצע ניתוח סגנוני" כדי לראות את התוצאות.</p>
        </div>
    </div>

    <div class="guess-section">
        <h3 class="section-subtitle">הכרעה: נחשו מיהו המחבר הסודי</h3>
        <div class="radio-group">
            <label class="radio-label"><input type="radio" name="author-guess" value="authorA"> מחבר א'</label>
            <label class="radio-label"><input type="radio" name="author-guess" value="authorB"> מחבר ב'</label>
            <label class="radio-label"><input type="radio" name="author-guess" value="authorC"> מחבר ג'</label>
        </div>
        <button id="submit-guess" class="action-button guess-button">האם צדקתי?</button>
    </div>

    <div id="feedback" class="feedback-section hidden">
        <!-- משוב יופיע כאן -->
    </div>

    <button id="toggle-explanation" class="toggle-button">הצג/הסתר את סוד הסטילומטריה</button>

    <div id="explanation" class="hidden">
        <h2>סוד הסטילומטריה נחשף</h2>
        <p>סטילומטריה היא ענף מרתק בבלשנות חישובית המאפשר לנו להשתמש בסטטיסטיקה כדי לזהות "טביעת אצבע" ייחודית של כותבים. השם מגיע מיוונית: 'סטילוס' (עט, סגנון) ו'מטרון' (מדידה).</p>

        <h3>עקרונות הניתוח הסגנוני: כמו טביעת אצבע דיגיטלית של מילים</h3>
        <p>הרעיון הגאוני מאחורי סטילומטריה הוא שכל אדם כותב בצורה מעט שונה, גם אם אינו מודע לכך. זה לא רק אוצר המילים הנדיר בו אנו משתמשים, אלא בעיקר הדפוסים הלא-מודעים שחוזרים על עצמם: תדירות שימוש במילות יחס נפוצות, מבנה המשפטים, הרגלי פיסוק ועוד. אלה יוצרים יחד "פרופיל סגנוני" ייחודי, מעין טביעת אצבע דיגיטלית של הכתיבה.</p>

        <h3>מאפיינים סגנוניים מרכזיים שהופכים אותנו לבלשים סטילומטריים</h3>
        <p>בעת ניתוח סטילומטרי, בודקים מגוון עשיר של מדדים כמותיים:</p>
        <ul>
            <li>**תדירות מילים נפוצות:** אלו המילים הקטנות והנשכחות כמו "ה", "ו", "של". תדירות השימוש בהן משתנה משמעותית בין כותבים ומהווה מדד עוצמתי לזיהוי.</li>
            <li>**אורך משפט ממוצע:** יש כותבים שנוטים למשפטים ארוכים ומפותלים, ואחרים למשפטים קצרים וקולעים.</li>
            <li>**אורך מילה ממוצע:** האם הכותב מעדיף מילים ארוכות ומורכבות או קצרות ופשוטות?</li>
            <li>**שימוש בסימני פיסוק:** כל כותב משתמש בפסיקים, נקודות, סימני קריאה ועוד בתדירות ובהקשרים שונים.</li>
            <li>**עושר אוצר מילים:** עד כמה המחבר חוזר על אותן מילים לעומת שימוש במילים ייחודיות רבות.</li>
            <li>**חלקי דיבר:** היחס בין שמות עצם, פעלים, שמות תואר וכו'.</li>
        </ul>

        <h3>מבלשים ספרותיים לפתרון פשעים: יישומים של סטילומטריה</h3>
        <p>לסטילומטריה יש השפעה רחבה:</p>
        <ul>
            <li>**ספרות:** פתרון ויכוחים היסטוריים על זהות מחברים אנונימיים (כמו במקרה של שייקספיר או כתבים עתיקים).</li>
            <li>**משפט:** זיהוי מחבר של מסמכים חשאיים, מכתבי איום, הודעות כופר, או אפילו פוסטים אנונימיים ברשת במקרים משפטיים.</li>
            <li>**היסטוריה ופוליטיקה:** זיהוי מחברים של מסמכים פוליטיים היסטוריים שפורסמו בעילום שם.</li>
        </ul>

        <h3>המהפכה הדיגיטלית: מחשבים כעוזרי הבלש</h3>
        <p>בעבר, ניתוח כזה היה ידני ומוגבל. כיום, מחשבים ואלגוריתמים מסוגלים לנתח במהירות מיליוני מילים, לזהות דפוסים בלתי נתפסים לעין אנושית, ולהשוות ביניהם בדיוק סטטיסטי מרשים.</p>

        <h3>אבל האם זה תמיד פשוט? מגבלות ואתגרים</h3>
        <p>למרות כוחה, לסטילומטריה יש גם צדדים מורכבים:</p>
        <ul>
            <li>**כמות טקסט:** ניתוח אמין דורש כמות טקסט מספקת.</li>
            <li>**שינויים בסגנון:** כותבים יכולים לשנות סגנון לאורך זמן או בהקשרים שונים.</li>
            <li>**השפעות חיצוניות:** עריכה, שיתופי פעולה או תרגום יכולים לטשטש את טביעת האצבע המקורית.</li>
        </ul>
        <p>למרות האתגרים, סטילומטריה נשארת כלי מרתק ועוצמתי לפענוח סודות הטמונים באופן שבו אנו כותבים.</p>
    </div>

</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    #app-container {
        font-family: 'Heebo', sans-serif;
        max-width: 900px;
        margin: 20px auto;
        padding: 30px; /* Increased padding */
        border: none; /* No border */
        border-radius: 15px; /* More rounded corners */
        background: linear-gradient(to bottom right, #eef2f7, #e0e7ef); /* Subtle gradient background */
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1); /* Softer, larger shadow */
        direction: rtl;
        color: #333;
    }

    h1 {
         text-align: center; /* Center main title */
         color: #1a2e4a; /* Darker blue for main title */
         margin-bottom: 20px;
         font-size: 2em;
         font-weight: 700;
    }

    h2.section-title {
        color: #334e6f; /* Darker blue */
        text-align: right;
        border-bottom: 2px solid #334e6f; /* Add a subtle line */
        padding-bottom: 10px;
        margin-top: 30px;
        margin-bottom: 20px;
        font-size: 1.6em;
         font-weight: 700;
    }

     h3.section-subtitle {
        color: #526c88; /* Medium blue */
        text-align: right;
        margin-bottom: 15px;
        font-size: 1.3em;
        font-weight: 400;
     }

     h4 {
         color: #627d98; /* Lighter blue */
         text-align: center;
         margin-top: 0;
         margin-bottom: 10px;
         font-size: 1.1em;
         font-weight: 700;
     }

    p {
        text-align: right;
        line-height: 1.7; /* Increased line height */
        margin-bottom: 15px;
    }

    .intro-text {
        font-size: 1.1em;
        color: #4a5568;
        margin-bottom: 30px;
    }

    .text-section, .analysis-controls, .analysis-results, .guess-section, .feedback-section {
        margin-bottom: 25px; /* Increased spacing */
        padding: 20px; /* Increased padding */
        border: none;
        border-radius: 10px; /* Slightly more rounded */
        background-color: #ffffff; /* White background for sections */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08); /* Subtle shadow for sections */
    }

    .known-authors-container {
        display: flex;
        flex-wrap: wrap;
        gap: 20px; /* Increased gap */
        justify-content: center;
    }

    .author-text-block {
        flex: 1 1 280px; /* Slightly larger base */
        border: 2px dashed #a0aec0; /* More prominent dashed border */
        padding: 15px; /* Increased padding */
        border-radius: 8px;
        background-color: #edf2f7; /* Light grey-blue background */
        display: flex;
        flex-direction: column;
        transition: transform 0.3s ease, box-shadow 0.3s ease; /* Add transition */
    }

     .author-text-block:hover {
         transform: translateY(-5px); /* Lift effect on hover */
         box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
     }

     .author-text-block.correct-match {
         border-color: #48bb78; /* Green border for correct match */
         box-shadow: 0 0 15px rgba(72, 187, 120, 0.5);
     }

    .text-block {
        min-height: 100px; /* Increased min height */
        padding: 15px; /* Increased padding */
        border: 1px solid #e2e8f0; /* Lighter border */
        border-radius: 6px;
        background-color: #ffffff;
        overflow-y: auto;
        text-align: right;
        direction: rtl;
        flex-grow: 1;
        line-height: 1.6;
        font-size: 0.95em;
        color: #4a5568;
    }

    .checkbox-group, .radio-group {
        margin-bottom: 15px;
    }

    .checkbox-label, .radio-label {
        display: block; /* Make them block for better click area */
        margin-bottom: 10px;
        font-size: 1em;
        cursor: pointer;
        user-select: none; /* Prevent text selection */
        padding: 5px 0; /* Add padding for click area */
    }

    .checkbox-label input, .radio-label input {
        margin-left: 8px; /* Space between checkbox and text */
         /* Hide default checkbox/radio and style with CSS if needed for more custom look */
    }

    button.action-button {
        display: inline-block; /* Allow multiple buttons if needed */
        margin-top: 10px;
        padding: 12px 25px; /* Increased padding */
        border: none;
        border-radius: 8px; /* More rounded */
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease; /* Add transform transition */
        font-weight: 700;
    }

    button.action-button:hover {
        transform: translateY(-2px); /* Lift effect on hover */
    }
     button.action-button:active {
        transform: translateY(0); /* Press effect */
    }

    button.analyze-button {
        background-color: #3182ce; /* Blue */
        color: white;
    }
    button.analyze-button:hover {
        background-color: #2b6cb0; /* Darker blue */
    }

    button.guess-button {
        background-color: #f6ad55; /* Orange */
        color: #4a5568; /* Dark text */
    }
    button.guess-button:hover {
        background-color: #ed8936; /* Darker orange */
    }

     button.toggle-button {
        display: block;
        width: fit-content;
        margin: 30px auto; /* More space, centered */
        padding: 10px 20px;
        background-color: #4fd1c5; /* Teal */
        color: #1a202c; /* Dark text */
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.3s ease;
        font-weight: 700;
    }
    button.toggle-button:hover {
        background-color: #38b2ac; /* Darker teal */
    }


    .analysis-results table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 15px; /* More space */
        text-align: right;
        font-size: 0.95em;
    }

    .analysis-results th, .analysis-results td {
        border: 1px solid #ebf4ff; /* Lighter border */
        padding: 10px; /* More padding */
        text-align: right;
         white-space: nowrap; /* Prevent wrapping in cells */
    }

    .analysis-results th {
        background-color: #e2f0f8; /* Light blue background */
        font-weight: 700;
        color: #2d3748;
    }

    .analysis-results tbody tr:nth-child(even) {
        background-color: #f7fafc; /* Very light grey */
    }
     .analysis-results tbody tr:hover {
        background-color: #ebf8ff; /* Highlight on hover */
     }

     .results-container {
         position: relative; /* Needed for loading indicator */
     }

     #analysis-loading {
        display: inline-block;
        width: 20px;
        height: 20px;
        border: 3px solid rgba(0, 0, 0, .3);
        border-radius: 50%;
        border-top-color: #3182ce;
        animation: spin 0.8s ease-in-out infinite;
        margin-left: 10px; /* Space from button */
         vertical-align: middle;
     }

     @keyframes spin {
        to { -webkit-transform: rotate(360deg); }
     }

     .hidden {
        display: none !important; /* Use !important to ensure hiding */
    }

    .analysis-results.hidden, .feedback-section.hidden {
         /* Use CSS transition for display none/block or opacity/height */
         /* display: none cannot be animated easily, use opacity + visibility or height */
         opacity: 0;
         height: 0;
         overflow: hidden;
         padding: 0;
         margin-bottom: 0;
         transition: opacity 0.4s ease, height 0.4s ease, padding 0.4s ease, margin-bottom 0.4s ease;
    }

     .analysis-results:not(.hidden), .feedback-section:not(.hidden) {
        opacity: 1;
         height: auto; /* Or max-height */
         padding: 20px;
         margin-bottom: 25px;
         transition: opacity 0.4s ease, height 0.4s ease, padding 0.4s ease, margin-bottom 0.4s ease;
     }

     .feedback-section {
        min-height: 60px; /* Increased min height */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
        font-size: 1.1em;
        line-height: 1.6;
     }

    .feedback-section.correct {
        background-color: #f0fff4; /* Very light green */
        border: 2px solid #68d391; /* Green border */
        color: #2f855a; /* Dark green text */
    }

     .feedback-section.incorrect {
        background-color: #fff5f5; /* Very light red */
        border: 2px solid #f56565; /* Red border */
        color: #c53030; /* Dark red text */
    }

     .feedback-section p {
         margin: 8px 0; /* Add margin to paragraphs within feedback */
     }

     .info-message {
         text-align: center;
         font-style: italic;
         color: #718096; /* Grey */
         margin-top: 15px;
         padding: 10px;
         background-color: #ebf8ff;
         border-radius: 5px;
     }


    #explanation {
        margin-top: 25px;
        padding: 25px; /* Increased padding */
        border: none;
        border-radius: 10px;
        background-color: #ffffff;
         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
         line-height: 1.7;
    }

    #explanation h2 {
         border-bottom: 2px solid #4fd1c5; /* Teal line */
         padding-bottom: 8px;
         margin-bottom: 20px;
         color: #007a70; /* Darker teal */
         font-size: 1.5em;
         font-weight: 700;
    }
     #explanation h3 {
         color: #526c88;
         margin-top: 20px;
         margin-bottom: 10px;
         font-size: 1.2em;
          font-weight: 700;
     }

    #explanation ul {
         padding-right: 30px; /* Increased padding */
         list-style-type: disc;
         margin-bottom: 15px;
    }
    #explanation li {
        margin-bottom: 8px;
        line-height: 1.6;
        color: #4a5568;
    }

     /* Responsive adjustments */
     @media (max-width: 768px) {
         #app-container {
             padding: 20px;
         }
         .known-authors-container {
             flex-direction: column;
             gap: 15px;
         }
         .author-text-block {
             flex: none; /* Disable flex grow */
             width: 100%; /* Take full width */
         }
         .analysis-controls label {
             margin-left: 0;
             margin-bottom: 10px;
         }
          button.action-button {
            width: 100%; /* Full width buttons on small screens */
            text-align: center;
            margin-top: 15px;
         }
     }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const texts = {
            anonymous: "השמש זרחה בשמיים הכחולים. ציפורים שרו על העצים. זה היה יום יפה לטייל בפארק. לקחנו סל פיקניק ויצאנו מהבית במהירות. רצינו להגיע לפני שיהיה חם מדי.",
            authorA: "אף שהשמש האירה את כיפת הרקיע בגווני תכלת עזים, הרוח הקרירה ששררה באוויר בבוקר הבטיחה תנאים נוחים יחסית לטיול. השירה העליזה שנשמעה מבין ענפי העצים העבותים הוסיפה נופך פסטורלי לאווירה. אכן, היה זה יום אידיאלי לצאת לסיור בפארק הסמוך, מצוידים בסל פיקניק שהכיל כל טוב.",
            authorB: "השמש זרחה. השמיים היו כחולים. ציפורים שרו. היה יום טוב ללכת לפארק. לקחנו סל ויצאנו. רצינו ללכת עכשיו.",
            authorC: "הו, השמש! היא האירה היום כל כך יפה, בזהב טהור, על שמיים שהיו ממש, אבל ממש כחולים עמוק! והציפורים? הן פשוט שרו את נפשן החוצה, מבין העצים! איזה יום מושלם, פשוט מושלם, לטייל! לקחנו את הסל שלנו, עם כל הדברים הטעימים בו, ויצאנו, במהירות, אל האור!"
        };

        // Define which author the anonymous text matches
        const correctAnswer = 'authorB'; // Anonymous text matches Author B

        // Populate text areas
        document.getElementById('anonymous-text').textContent = texts.anonymous;
        document.getElementById('author-a-text').textContent = texts.authorA;
        document.getElementById('author-b-text').textContent = texts.authorB;
        document.getElementById('author-c-text').textContent = texts.authorC;

        const analyzeButton = document.getElementById('analyze-button');
        const analysisLoading = document.getElementById('analysis-loading');
        const resultsTableBody = document.querySelector('#results-table tbody');
        const analysisResultsDiv = document.querySelector('.analysis-results');
        const noFeaturesMessage = document.getElementById('no-features-selected-message');
        const submitGuessButton = document.getElementById('submit-guess');
        const feedbackDiv = document.getElementById('feedback');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');
         const authorBlocks = document.querySelectorAll('.author-text-block');


        // Feature mapping for feedback text
        const featureMapping = {
             freqWords: 'תדירות מילים נפוצות',
             avgSentenceLength: 'אורך משפט ממוצע',
             avgWordLength: 'אורך מילה ממוצע',
             punctuation: 'שימוש בסימני פיסוק'
        };

        // Analysis Functions
        function cleanText(text) {
            // Remove punctuation that splits words but keep sentence enders (.!?) and hyphens within words potentially
             // Let's refine cleaning: keep hyphens that might be part of words, remove others and symbols.
            let cleaned = text.replace(/[",()':;]/g, '');
             // Remove standalone hyphens or hyphens at start/end of words. Keep hyphen if surrounded by letters.
            cleaned = cleaned.replace(/(?<!\p{L})-|-(?!\p{L})/gu, ''); // Requires Unicode property escapes (u flag)
            cleaned = cleaned.replace(/\s+/g, ' ').trim(); // Normalize spaces
            return cleaned;
        }

         function countWords(text) {
             const cleaned = cleanText(text);
             if (!cleaned) return 0;
             return cleaned.split(/\s+/).filter(word => word.length > 0).length; // Filter out empty strings from split
         }

        function analyzeText(text, features) {
            const results = {};
             // Use original text for punctuation count, cleaned for others
            const cleaned = cleanText(text);
            const sentences = text.split(/[.!?]/).filter(s => s.trim().length > 0);
            const words = cleaned.split(/\s+/).filter(w => w.length > 0);
            const totalWords = words.length;
            const totalSentences = sentences.length;
             // Sum of lengths of cleaned words
            const totalLetters = words.reduce((sum, word) => sum + word.length, 0);

            if (features.includes('freqWords')) {
                const frequentWords = ['ה', 'ו', 'את', 'של', 'על', 'ב', 'כי', 'אשר']; // Keep these based on example
                results.freqWords = {};
                const wordCounts = {};
                 words.forEach(word => {
                     // Lowercase and remove any remaining non-letter chars? Basic cleaning should handle this.
                     wordCounts[word] = (wordCounts[word] || 0) + 1;
                 });

                 frequentWords.forEach(word => {
                      // Calculate frequency as count per 100 words, rounded to 2 decimal places
                     results.freqWords[word] = totalWords > 0 ? ((wordCounts[word] || 0) / totalWords * 100).toFixed(2) : '0.00';
                 });
            }

            if (features.includes('avgSentenceLength')) {
                results.avgSentenceLength = totalSentences > 0 ? (totalWords / totalSentences).toFixed(2) : '0.00';
            }

            if (features.includes('avgWordLength')) {
                 results.avgWordLength = totalWords > 0 ? (totalLetters / totalWords).toFixed(2) : '0.00';
            }

             if (features.includes('punctuation')) {
                 const punctuationMarks = ['.', ',', '!', '?', '-', ';']; // Keep these based on example
                 results.punctuation = {};
                 punctuationMarks.forEach(mark => {
                      // Count punctuation in the original text
                      const count = (text.match(new RegExp('\\' + mark.replace(/[-[\]{}()*+?.,\\^$|#\s]/g, '\\$&'), 'g')) || []).length;
                      results.punctuation[mark] = count;
                 });
             }

            return results;
        }

        function displayResults(analysisResults, features) {
            resultsTableBody.innerHTML = ''; // Clear previous results
            const textsOrder = ['anonymous', 'authorA', 'authorB', 'authorC'];
            const textNames = ['אנונימי', 'מחבר א\'', 'מחבר ב\'', 'מחבר ג\''];

            if (features.length === 0) {
                noFeaturesMessage.classList.remove('hidden');
                analysisResultsDiv.classList.add('hidden'); // Hide the whole results section
                return;
            } else {
                 noFeaturesMessage.classList.add('hidden');
                 analysisResultsDiv.classList.remove('hidden'); // Show the results section
            }

            // Add rows for each selected feature
            features.forEach(feature => {
                if (feature === 'freqWords') {
                     const frequentWords = ['ה', 'ו', 'את', 'של', 'על', 'ב', 'כי', 'אשר'];
                     frequentWords.forEach(word => {
                         const row = resultsTableBody.insertRow();
                         row.insertCell().textContent = `תדירות "${word}" (%)`; // Add unit
                         textsOrder.forEach(key => {
                             row.insertCell().textContent = analysisResults[key].freqWords[word];
                         });
                     });
                } else if (feature === 'avgSentenceLength') {
                    const row = resultsTableBody.insertRow();
                    row.insertCell().textContent = 'אורך משפט ממוצע (מילים)'; // Add unit
                     textsOrder.forEach(key => {
                         row.insertCell().textContent = analysisResults[key].avgSentenceLength;
                     });
                } else if (feature === 'avgWordLength') {
                    const row = resultsTableBody.insertRow();
                    row.insertCell().textContent = 'אורך מילה ממוצע (אותיות)'; // Add unit
                     textsOrder.forEach(key => {
                         row.insertCell().textContent = analysisResults[key].avgWordLength;
                     });
                } else if (feature === 'punctuation') {
                     const punctuationMarks = ['.', ',', '!', '?', '-', ';'];
                     punctuationMarks.forEach(mark => {
                          const row = resultsTableBody.insertRow();
                          row.insertCell().textContent = `שימוש ב-${mark} (מספר מופעים)`; // Add unit/description
                          textsOrder.forEach(key => {
                               row.insertCell().textContent = analysisResults[key].punctuation[mark];
                          });
                     });
                }
            });

             // Force reflow/repaint before applying transition
            void analysisResultsDiv.offsetHeight;
        }


        analyzeButton.addEventListener('click', () => {
            const selectedFeatures = Array.from(document.querySelectorAll('.analysis-feature:checked')).map(cb => cb.dataset.feature);

            if (selectedFeatures.length === 0) {
                alert("אנא בחר לפחות מאפיין אחד לניתוח כדי לראות את התוצאות.");
                displayResults({}, []); // Clear table and show message
                return;
            }

            // Show loading indicator and disable button
            analysisLoading.classList.remove('hidden');
            analyzeButton.disabled = true;

            // Perform analysis (simulate delay for animation)
            setTimeout(() => {
                const analysisResults = {
                    anonymous: analyzeText(texts.anonymous, selectedFeatures),
                    authorA: analyzeText(texts.authorA, selectedFeatures),
                    authorB: analyzeText(texts.authorB, selectedFeatures),
                    authorC: analyzeText(texts.authorC, selectedFeatures)
                };

                displayResults(analysisResults, selectedFeatures);

                // Hide loading indicator and re-enable button
                analysisLoading.classList.add('hidden');
                analyzeButton.disabled = false;
            }, 500); // Simulate a brief processing time
        });

        submitGuessButton.addEventListener('click', () => {
            const selectedAuthorInput = document.querySelector('input[name="author-guess"]:checked');
            const feedbackDiv = document.getElementById('feedback'); // Re-get to ensure correct state
            const authorBlocks = document.querySelectorAll('.author-text-block');

            // Clear previous feedback and highlights
             feedbackDiv.classList.add('hidden');
             feedbackDiv.innerHTML = '';
             authorBlocks.forEach(block => block.classList.remove('correct-match')); // Remove previous correct highlights


            if (!selectedAuthorInput) {
                feedbackDiv.classList.remove('hidden');
                feedbackDiv.className = 'feedback-section incorrect'; // Use incorrect class for this state too
                feedbackDiv.innerHTML = '<p><strong>המממ...</strong> אנא בחר מחבר לפני הבדיקה.</p>';
                 // Add subtle shake animation
                 feedbackDiv.style.animation = 'shake 0.5s';
                 feedbackDiv.addEventListener('animationend', () => feedbackDiv.style.animation = '');

                return;
            }

            const userGuess = selectedAuthorInput.value;
            const isCorrect = userGuess === correctAnswer;
             const selectedAuthorLabel = selectedAuthorInput.labels[0].textContent;
            const correctAuthorLabel = document.querySelector(`input[value="${correctAnswer}"]`).labels[0].textContent;

            feedbackDiv.classList.remove('hidden');
            feedbackDiv.className = 'feedback-section ' + (isCorrect ? 'correct' : 'incorrect');


            if (isCorrect) {
                 feedbackDiv.innerHTML = `<p><strong>בראבו, בלש! נכון מאוד!</strong></p><p> הטקסט האנונימי אכן נכתב על ידי <span style="font-weight: bold; color: #1a202c;">${correctAuthorLabel}</span>.</p>`;
                 // Add highlight to the correct author's block
                document.querySelector(`.author-text-block[data-author="${correctAnswer}"]`).classList.add('correct-match');
                 // Add pulse animation for correct answer
                 feedbackDiv.style.animation = 'pulse 0.8s ease-out';
                 feedbackDiv.addEventListener('animationend', () => feedbackDiv.style.animation = '');

            } else {
                 feedbackDiv.innerHTML = `<p><strong>המממ... לא מדויק הפעם.</strong></p><p> הטקסט האנונימי נכתב על ידי <span style="font-weight: bold; color: #1a202c;">${correctAuthorLabel}</span>, לא על ידי ${selectedAuthorLabel}.</p>`;
                  // Add shake animation for incorrect guess
                 feedbackDiv.style.animation = 'shake 0.5s';
                 feedbackDiv.addEventListener('animationend', () => feedbackDiv.style.animation = '');
                // Optionally highlight the correct author block even on wrong guess
                 document.querySelector(`.author-text-block[data-author="${correctAnswer}"]`).classList.add('correct-match');

            }

             // Provide explanation based on analysis if results are available
            const selectedFeatures = Array.from(document.querySelectorAll('.analysis-feature:checked')).map(cb => cb.dataset.feature);
             const resultsDisplayed = resultsTableBody.innerHTML !== '';


            if (selectedFeatures.length > 0 && resultsDisplayed) {
                const analysisResults = {
                     anonymous: analyzeText(texts.anonymous, selectedFeatures),
                     authorA: analyzeText(texts.authorA, selectedFeatures),
                     authorB: analyzeText(texts.authorB, selectedFeatures),
                     authorC: analyzeText(texts.authorC, selectedFeatures)
                };

                let explanationText = `<p><strong>ניתוח המאפיינים שנבחרו מסביר זאת:</strong></p>`;

                selectedFeatures.forEach(feature => {
                    explanationText += `<p><strong><span style="color: #334e6f;">${featureMapping[feature]}</span>:</strong><br>`;
                    const anonymousValue = analysisResults.anonymous[feature];
                    const correctValue = analysisResults[correctAnswer][feature];
                    const userGuessValue = analysisResults[userGuess][feature];
                    const correctAuthorName = document.querySelector(`input[value="${correctAnswer}"]`).labels[0].textContent;
                     const userGuessAuthorName = selectedAuthorInput.labels[0].textContent;


                    if (feature === 'freqWords' || feature === 'punctuation') {
                        const keys = feature === 'freqWords' ? ['ה', 'ו', 'את', 'של', 'על', 'ב', 'כי', 'אשר'] : ['.', ',', '!', '?', '-', ';'];
                        keys.forEach(key => {
                             const anonVal = typeof anonymousValue[key] !== 'undefined' ? anonymousValue[key] : 'N/A';
                             const correctVal = typeof correctValue[key] !== 'undefined' ? correctValue[key] : 'N/A';
                             const userGuessVal = typeof userGuessValue[key] !== 'undefined' ? userGuessValue[key] : 'N/A';

                             explanationText += `- "${key}": אנונימי = <span style="font-weight: bold;">${anonVal}</span>, ${correctAuthorName} = <span style="font-weight: bold;">${correctVal}</span>`;
                              if (!isCorrect) {
                                  explanationText += `, ${userGuessAuthorName} = <span style="font-weight: bold;">${userGuessVal}</span>`;
                              }

                              // Simple comparison logic for text feedback
                               const isAnonCloseToCorrect = anonVal === correctVal; // Direct match check
                               const isAnonCloseToGuess = !isCorrect && anonVal === userGuessVal; // Direct match check

                               if (isAnonCloseToCorrect && (!isCorrect ? !isAnonCloseToGuess : true)) {
                                   explanationText += ` <span style="color: #2f855a;">(דומה למחבר הנכון!)</span>`;
                               } else if (!isAnonCloseToCorrect && (!isCorrect && isAnonCloseToGuess)) {
                                    explanationText += ` <span style="color: #c53030;">(שונה מהמחבר הנכון, דומה לניחוש שלך)</span>`;
                               } else if (!isAnonCloseToCorrect && (!isCorrect ? !isAnonCloseToGuess : true)) {
                                    explanationText += ` <span style="color: #c53030;">(שונה מהמחבר הנכון)</span>`;
                               } else if (isCorrect && isAnonCloseToCorrect) {
                                    explanationText += ` <span style="color: #2f855a;">(דומה למחבר הנכון)</span>`;
                               }


                               explanationText += "<br>";
                        });
                     } else { // Average values
                        const anonVal = parseFloat(anonymousValue);
                        const correctVal = parseFloat(correctValue);
                        const userGuessVal = parseFloat(userGuessValue);

                         explanationText += `אנונימי = <span style="font-weight: bold;">${anonymousValue}</span>, ${correctAuthorName} = <span style="font-weight: bold;">${correctValue}</span>`;
                         if (!isCorrect) {
                            explanationText += `, ${userGuessAuthorName} = <span style="font-weight: bold;">${userGuessValue}</span>`;
                         }

                         // Simple comparison logic for averages with a tolerance
                         const threshold = 0.6; // Define a small tolerance for averages (adjust as needed)
                         const diffCorrect = !isNaN(anonVal) && !isNaN(correctVal) ? Math.abs(anonVal - correctVal) : Infinity;
                         const diffGuess = !isCorrect && !isNaN(anonVal) && !isNaN(userGuessVal) ? Math.abs(anonVal - userGuessVal) : Infinity;

                         const isAnonCloseToCorrect = diffCorrect <= threshold;
                         const isAnonCloserThanGuess = !isCorrect && diffCorrect < diffGuess;
                         const isGuessCloserThanCorrect = !isCorrect && diffGuess < diffCorrect;
                         const isAnonCloseToGuess = !isCorrect && diffGuess <= threshold;


                         if (isAnonCloseToCorrect && (!isCorrect ? isAnonCloserThanGuess || diffCorrect === diffGuess : true)) {
                              explanationText += ` <span style="color: #2f855a;">(ערכים דומים למחבר הנכון!)</span>`;
                          } else if (!isCorrect && isAnonCloseToGuess && (isGuessCloserThanCorrect || diffCorrect === diffGuess)) {
                               explanationText += ` <span style="color: #c53030;">(ערכים שונים מהמחבר הנכון, דומים לניחוש שלך)</span>`;
                           } else if (!isAnonCloseToCorrect && (!isCorrect ? !isAnonCloseToGuess : true)) {
                                explanationText += ` <span style="color: #c53030;">(ערכים שונים מהמחבר הנכון)</span>`;
                           } else if (isCorrect && isAnonCloseToCorrect) {
                                explanationText += ` <span style="color: #2f855a;">(ערכים דומים למחבר הנכון)</span>`;
                           } else if (!isCorrect && isAnonCloseToCorrect && isAnonCloseToGuess) {
                                explanationText += ` <span style="color: #718096;">(ערכים דומים לשניהם)</span>`;
                           }


                     }

                    explanationText += "</p>"; // Close paragraph for feature explanation
                });
                 feedbackDiv.innerHTML += explanationText;

            } else {
                 feedbackDiv.innerHTML += `<p>בצע ניתוח סגנוני ובחר מאפיינים כדי לראות השוואה מפורטת יותר כאן.</p>`;
            }

            // Force reflow/repaint before applying transition
            void feedbackDiv.offsetHeight;


        });


        toggleExplanationButton.addEventListener('click', () => {
            explanationDiv.classList.toggle('hidden');
            if (explanationDiv.classList.contains('hidden')) {
                toggleExplanationButton.textContent = 'הצג את סוד הסטילומטריה';
            } else {
                 toggleExplanationButton.textContent = 'הסתר את סוד הסטילומטריה';
            }
        });

        // Initial state: explanation hidden, results hidden
        explanationDiv.classList.add('hidden');
         analysisResultsDiv.classList.add('hidden');
         feedbackDiv.classList.add('hidden');
         noFeaturesMessage.classList.remove('hidden'); // Ensure message is visible initially
        toggleExplanationButton.textContent = 'הצג את סוד הסטילומטריה'; // Set initial button text

         // Add basic CSS animations for feedback
         const styleSheet = document.styleSheets[0];
         styleSheet.insertRule(`
            @keyframes shake {
                0%, 100% { transform: translateX(0); }
                10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
                20%, 40%, 60%, 80% { transform: translateX(5px); }
            }
         `, styleSheet.cssRules.length);
          styleSheet.insertRule(`
            @keyframes pulse {
                0% { transform: scale(1); }
                50% { transform: scale(1.01); }
                100% { transform: scale(1); }
            }
         `, styleSheet.cssRules.length);


    });
</script>
```