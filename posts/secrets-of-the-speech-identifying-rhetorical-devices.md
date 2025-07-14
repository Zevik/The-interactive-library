---
title: "סודות הנאום: המדריך לזיהוי כלים רטוריים"
english_slug: secrets-of-the-speech-identifying-rhetorical-devices
category: "מדעי הרוח / כללי"
tags: [רטוריקה, נאום, תקשורת, אמנות השכנוע, ניתוח טקסט, כלים רטוריים]
---
# סודות הנאום: המדריך לזיהוי כלים רטוריים

איך נאומים מסוימים מצליחים לגעת בנו עמוק כל כך, לרגש ולסחוף קהל שלם? האם יש נוסחה סודית שמשמשת גדולי הדוברים בהיסטוריה? האמת היא שישנם כלים רבי עוצמה, המכונים כלים רטוריים, שמעצבים את הנאום והופכים אותו ליצירת אמנות של שכנוע והשפעה.

צאו למסע אינטראקטיבי לתוך לב ליבה של הרטוריקה. גלו כיצד לזהות את הכלים שמניעים את אמנות הנאום ולהבין את כוחם האמיתי.

<div id="rhetoric-app-container">
    <h2>משימת ניתוח נאום: מצאו את הכלי הרטורי!</h2>
    <p class="instructions">לחצו על קטע מודגש בטקסט כדי לזהות את הכלי הרטורי החבוי בו.</p>
    <div id="speech-text">
        <p>טוען נאום...</p>
    </div>
    <div id="device-options" class="hidden">
        <p>איזה כלי רטורי מודגם כאן לדעתך?</p>
        <div id="options-list"></div>
    </div>
    <div id="feedback" class="hidden" aria-live="polite"></div>
    <button id="next-snippet-btn" class="hidden">עברו לקטע הנאום הבא</button>
     <div id="progress-indicator" class="hidden">
        <span id="identified-count">0</span> מתוך <span id="total-highlights">0</span> זוהו
    </div>
</div>

<style>
    /* הוספת פונטים מערכתיים נעימים יותר ואסתטיקה מודרנית */
    #rhetoric-app-container {
        font-family: 'Arial', 'Helvetica Neue', 'Helvetica', sans-serif;
        line-height: 1.7;
        margin: 25px auto;
        padding: 30px;
        border: none; /* Remove default border */
        border-radius: 12px;
        max-width: 750px;
        background-color: #ffffff; /* Clean white background */
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        color: #333;
    }

    h2 {
        text-align: center;
        color: #2c3e50; /* Dark blue-gray */
        margin-top: 0;
        margin-bottom: 20px;
    }

    .instructions {
        text-align: center;
        color: #555;
        margin-bottom: 25px;
    }

    #speech-text {
        margin-top: 20px;
        padding: 20px;
        background-color: #ecf0f1; /* Light gray background */
        border-radius: 8px;
        position: relative; /* Needed for potential animations */
        transition: all 0.5s ease;
    }

    .highlight {
        background-color: #fcf3cf; /* Very light yellow */
        cursor: pointer;
        padding: 1px 3px; /* Adjust padding */
        border-bottom: 2px solid #f1c40f; /* Yellow border */
        transition: background-color 0.3s ease, border-bottom-color 0.3s ease;
        display: inline; /* Ensure it wraps naturally */
        line-height: 1.8; /* Improve line spacing with highlights */
    }

    .highlight:hover {
        background-color: #fdebd0; /* Slightly darker yellow on hover */
        border-bottom-color: #e67e22; /* Orange border on hover */
    }

     .highlight.active-highlight {
         background-color: #fdebd0; /* Keep hover color when active */
         border-bottom-color: #e67e22; /* Keep hover color when active */
         box-shadow: 0 0 5px rgba(241, 196, 15, 0.5); /* Add a glow */
     }


    .correctly-identified {
        background-color: #d4efdf; /* Light green */
        color: #186a3b; /* Dark green text */
        cursor: default;
        border-bottom: 2px solid #2ecc71; /* Green border */
        padding: 1px 3px; /* Keep padding consistent */
        transition: background-color 0.5s ease, color 0.5s ease;
        display: inline; /* Ensure it wraps naturally */
         line-height: 1.8; /* Inherit line spacing */
    }

    #device-options {
        margin-top: 20px;
        padding: 20px;
        border: 1px solid #bdc3c7; /* Light gray border */
        background-color: #ecf0f1; /* Match speech-text background */
        border-radius: 8px;
        opacity: 0; /* Start hidden for animation */
        transform: translateY(10px); /* Start slightly lower */
        transition: opacity 0.4s ease-out, transform 0.4s ease-out;
    }

    #device-options.visible {
        opacity: 1;
        transform: translateY(0);
    }


    #options-list {
        display: flex;
        flex-wrap: wrap;
        gap: 10px; /* Increased gap */
        justify-content: center; /* Center the buttons */
        margin-top: 15px;
    }

    #options-list button {
        padding: 10px 15px;
        border: 1px solid #3498db; /* Primary blue */
        border-radius: 5px;
        background-color: #3498db;
        color: white;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.3s ease, transform 0.1s ease, border-color 0.3s ease;
        font-family: inherit; /* Use inherited font */
    }

    #options-list button:hover:not(:disabled) {
        background-color: #2980b9; /* Darker blue */
        border-color: #2980b9;
        transform: translateY(-2px); /* Slight lift on hover */
    }

     #options-list button:active:not(:disabled) {
         transform: translateY(0); /* Press effect */
     }

     #options-list button:disabled {
        background-color: #cccccc;
        border-color: #999999;
        color: #666666;
        cursor: not-allowed;
        opacity: 0.7;
     }


    #feedback {
        margin-top: 20px;
        padding: 18px; /* Increased padding */
        border-radius: 8px;
        font-weight: bold;
        opacity: 0; /* Start hidden for animation */
        transform: translateY(10px); /* Start slightly lower */
        transition: opacity 0.4s ease-out, transform 0.4s ease-out;
    }
     #feedback.visible {
        opacity: 1;
        transform: translateY(0);
     }


    #feedback.correct {
        background-color: #e9f5ee; /* Very light green */
        color: #228b22; /* Forest green */
        border: 1px solid #a9dfbf; /* Medium green border */
    }

    #feedback.incorrect {
        background-color: #faebd7; /* Light peach */
        color: #cd5c5c; /* Indian red */
        border: 1px solid #f5cba7; /* Medium peach border */
    }

    .hidden {
        display: none;
    }

    #next-snippet-btn {
        display: block;
        margin: 30px auto 0; /* More space */
        padding: 12px 25px; /* Larger button */
        font-size: 1.1em;
        cursor: pointer;
        background-color: #2ecc71; /* Emerald green */
        color: white;
        border: none;
        border-radius: 5px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-family: inherit;
    }
     #next-snippet-btn:hover {
        background-color: #27ae60; /* Darker green */
        transform: translateY(-2px);
     }
      #next-snippet-btn:active {
          transform: translateY(0);
      }

    #toggle-explanation {
        display: block;
        margin: 25px auto;
        padding: 10px 20px;
        font-size: 1em;
        cursor: pointer;
        background: none; /* Make it look like a link/secondary button */
        color: #3498db;
        border: 1px solid #3498db;
        border-radius: 5px;
        transition: all 0.3s ease;
        font-family: inherit;
    }

    #toggle-explanation:hover {
        background-color: #eaf2f8; /* Light blue background */
        color: #2980b9;
        border-color: #2980b9;
    }

    #explanation {
        margin-top: 30px;
        padding: 25px;
        background-color: #f8f9f9; /* Very light gray */
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        color: #444;
        line-height: 1.7;
    }

    #explanation h2, #explanation h3 {
        color: #2c3e50;
        margin-bottom: 15px;
        border-bottom: 1px solid #eee;
        padding-bottom: 5px;
    }
    #explanation h3 {
        margin-top: 20px;
    }

    #explanation ul {
        list-style-type: disc;
        margin-left: 20px;
        padding-left: 0;
    }

    #explanation li {
        margin-bottom: 10px;
    }

    #explanation strong {
        color: #555;
    }

    #progress-indicator {
         text-align: center;
         margin-top: 15px;
         font-size: 0.9em;
         color: #555;
    }

     #progress-indicator span {
         font-weight: bold;
         color: #2c3e50;
     }


</style>

<button id="toggle-explanation">הצגת המדריך המלא לכלים רטוריים</button>

<div id="explanation" class="hidden">
    <h2>מדריך: עולם הרטוריקה וכלי השכנוע</h2>
    <h3>מהי רטוריקה ומה תפקידה?</h3>
    <p>רטוריקה היא אמנות השימוש בשפה בצורה יעילה ומשכנעת, בכתב ובעל פה. מטרתה העיקרית היא להשפיע על הקהל – לשכנע, לרתק, להעביר מסר, לעורר רגש או להניע לפעולה. בנאומים, הרטוריקה היא הכוח המניע מאחורי היכולת של דובר לגעת בקהל, לבנות אמון ולהוביל שינוי. זיהוי הכלים הרטוריים מאפשר לנו להבין *איך* נאום עובד ואיך הוא משפיע עלינו.</p>

    <h3>כלים רטוריים נפוצים בניתוח נאומים</h3>
    <p>דוברים וכותבים משתמשים במגוון רחב של טכניקות לשוניות כדי לחזק את המסר שלהם, ליצור קצב, הדגשה או עומק רגשי. הנה כמה מהנפוצים שבהם שתפגשו בנאומים מפורסמים:</p>
    <ul>
        <li>**אנאפורה (Anaphora):** חזרה על מילה או ביטוי **בתחילת** משפטים, פסקאות או יחידות תחביריות עוקבות. יוצרת קצב סוחף, מדגישה רעיון מרכזי ומעצימה את התחושה או המסר החוזר.</li>
        <li>**אפיסטרופה (Epistrophe):** חזרה על מילה או ביטוי **בסוף** משפטים, פסקאות או יחידות תחביריות עוקבות. אפקט דומה לאנאפורה, לרוב עם דגש חזק על המסקנה, התוצאה או הרעיון הסוגר.</li>
        <li>**שאלה רטורית (Rhetorical Question):** שאלה שנשאלת לא כדי לקבל תשובה ישירה, אלא כדי לעורר מחשבה אצל הקהל, להדגיש נקודה כאילו היא ברורה מאליה, או להניע את הקהל להסכים עם הדובר באופן פנימי.</li>
        <li>**ניגוד / אנטיתזה (Antithesis):** הצגת שני רעיונות, מושגים או ביטויים מנוגדים או מנוגדים זה לזה, לרוב במבנה תחבירי מקביל ומאוזן. מדגיש את ההבדלים, יוצר דרמה או בהירות מחשבתית. (למשל: "שאל לא מה ארצך יכולה לעשות למענך, אלא מה אתה יכול לעשות למען ארצך").</li>
        <li>**השוואה (Simile):** השוואה מפורשת בין שני דברים שונים זה מזה אך בעלי נקודת דמיון כלשהי, באמצעות מילות השוואה מפורשות כמו "כמו", "כאילו", "כמו ש...", "דומה ל...".</li>
        <li>**מטפורה (Metaphor):** השוואה מרומזת ועמוקה יותר בין שני דברים שונים, ללא מילות השוואה מפורשות, תוך כדי קביעה שדבר אחד *הוא* דבר אחר, או שדבר אחד פועל כדבר אחר. יוצרת דימוי חי ומעשירה את המשמעות.</li>
        <li>**אוקסימורון (Oxymoron):** צירוף של שתי מילים או ביטויים הסותרים זה את זה לכאורה, אך יחד יוצרים משמעות חדשה, מפתיעה ולעיתים מעוררת מחשבה (למשל: "שתיקה רועמת", "בהלה מבוקרת", "אכזריות רחומה").</li>
        <li>**הדרגתיות / קלימקס (Climax):** סידור מילים, ביטויים, משפטים או רעיונות בסדר עולה של חשיבות, עוצמה, דרמה או היקף. בונה מתח ומגיע לשיא מרשים.</li>
        <li>**אירוניה (Irony):** שימוש בשפה כך שהמשמעות האמיתית המובעת היא ההפוכה מהמשמעות המילולית הנאמרת או הנכתבת. משמשת לרוב לצורך הומור, ביקורת או הדגשה. (האינטראקטיביות הנוכחית מתמקדת בכלים מבניים/פיגורטיביים יותר, אך חשוב להכיר גם את זה).</li>
    </ul>

    <h3>דוגמאות קלאסיות לשימוש בכלים רטוריים בנאומים מפורסמים</h3>
    <ul>
        <li>נאום "יש לי חלום" של מרטין לותר קינג: דוגמה מובהקת וחוזרת לאנאפורה ("I have a dream...").</li>
        <li>נאום ההשבעה של ג'ון פ. קנדי: דוגמה קלאסית לניגוד / אנטיתזה ("Ask not what your country can do for you...").</li>
        <li>נאומי וינסטון צ'רצ'יל בזמן מלחמת העולם השנייה: עשירים במטפורות, אנאפורה ושימוש באפקט הקלימקס ("We shall fight on the beaches...").</li>
    </ul>

    <h3>מדוע זיהוי כלים רטוריים חשוב להבנת נאומים וטקסטים בכלל?</h3>
    <p>זיהוי כלים רטוריים מאפשר לנו לקרוא או להאזין לטקסטים בצורה ביקורתית ומעמיקה יותר:</p>
    <ul>
        <li>**לחשוף את הכוונות האמיתיות:** להבין מה הדובר או הכותב מנסה להשיג מעבר למילים הפשוטות.</li>
        <li>**להבין את השפעה:** לפענח כיצד נוצרת ההשפעה הרגשית והקוגניטיבית החזקה של הטקסט.</li>
        <li>**להעריך טיעונים:** להבחין בין טיעון מבוסס לבין שימוש בכלים רטוריים כדי לחפות על חוסר בתוכן או בהיגיון.</li>
        <li>**להפוך למשתתפים אקטיביים:** לעבור מצריכה פסיבית של מסרים לניתוח אקטיבי ומושכל.</li>
    </ul>

    <h3>כיצד להשתמש בידע זה לניתוח ביקורתי של מסרים?</h3>
    <p>בכל פעם שאתם נתקלים בנאום, מאמר, פרסומת או כל מסר שנועד להשפיע עליכם, עצרו ושאלו את עצמכם:</p>
    <ul>
        <li>אילו כלים רטוריים בולטים בטקסט? האם יש חזרות? ניגודים? דימויים?</li>
        <li>כיצד השימוש בכלים אלו מחזק את המסר המרכזי שהדובר רוצה להעביר?</li>
        <li>על אילו רגשות, ערכים או אמונות שלי הדובר מנסה להשפיע באמצעות הכלים הללו?</li>
        <li>האם הכלים הרטוריים מעשירים את המסר או שמא הם משמשים כעשן כדי להסתיר טיעונים חלשים?</li>
    </ul>
    <p>על ידי פיתוח "עין רטורית", אתם מציידים את עצמכם בכלים קריטיים להתמודדות מושכלת וביקורתית עם שטף המידע והמסרים בעידן המודרני.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const rhetoricAppContainer = document.getElementById('rhetoric-app-container');
    const speechTextDiv = document.getElementById('speech-text');
    const optionsListDiv = document.getElementById('options-list');
    const deviceOptionsDiv = document.getElementById('device-options');
    const feedbackDiv = document.getElementById('feedback');
    const nextSnippetBtn = document.getElementById('next-snippet-btn');
    const toggleExplanationBtn = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const progressIndicator = document.getElementById('progress-indicator');
    const identifiedCountSpan = document.getElementById('identified-count');
    const totalHighlightsSpan = document.getElementById('total-highlights');


    const speechData = [
        {
            text: `I have a dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are created equal." <br><br> <span class='highlight' data-index='0'>I have a dream</span> that one day on the red hills of Georgia, the sons of former slaves and the sons of former slave owners will be able to sit down together at the table of brotherhood.<br><br> <span class='highlight' data-index='1'>I have a dream</span> that one day even the state of Mississippi, a state sweltering with the heat of injustice, sweltering with the heat of oppression, will be transformed into an oasis of freedom and justice.<br><br> <span class='highlight' data-index='2'>I have a dream</span> that my four little children will one day live in a nation where they will not be judged by the color of their skin but by the content of their character.<br><br> <span class='highlight' data-index='3'>I have a dream</span> today!`,
            devices: [
                { index: 0, device: "אנאפורה", feedback: "מצוין! 'I have a dream' חוזר בתחילת מספר פסקאות, וזו דוגמה קלאסית ועוצמתית לאנאפורה. היא יוצרת קצב ומדגישה את החזון המרכזי של הנאום." },
                { index: 1, device: "אנאפורה", feedback: "נכון מאוד! החזרה על 'I have a dream' ממשיכה לבנות את המומנטום הרטורי של הנאום דרך אנאפורה." },
                { index: 2, device: "אנאפורה", feedback: "יוצא מן הכלל! זיהית שוב את האנאפורה הבולטת בנאום זה. זו הטכניקה המרכזית שמקנה לו את עוצמתו." },
                { index: 3, device: "אנאפורה", feedback: "מדויק לחלוטין! הסיום הקצר והקולע 'I have a dream today!' חותם את רצף האנאפורות ומדגיש שהחלום הוא מציאות שפועלים למענה ברגע זה." }
            ],
            all_options: ["אנאפורה", "אפיסטרופה", "שאלה רטורית", "ניגוד", "מטפורה", "הדרגתיות"]
        },
         {
            text: `And so, my fellow Americans: <span class='highlight' data-index='0'>ask not what your country can do for you—ask what you can do for your country</span>.<br><br> My fellow citizens of the world: <span class='highlight' data-index='1'>ask not what America will do for you, but what together we can do for the freedom of man</span>.`,
            devices: [
                { index: 0, device: "ניגוד", feedback: "נכון מאוד! המשפט המפורסם הזה הוא דוגמה קלאסית ויפהפייה לאנטיתזה (ניגוד), שמציגה שני רעיונות מנוגדים במבנה מקביל כדי להדגיש את המעבר מחשיבה אישית לחשיבה קהילתית." },
                { index: 1, device: "ניגוד", feedback: "יוצא מן הכלל! גם כאן ג'ון פ. קנדי משתמש באנטיתזה ('ניגוד') כדי להבליט את ההבדל בין תלות לעשייה משותפת למען מטרה גלובלית גדולה יותר. שימוש אלגנטי בכלי רטורי!" }
            ],
             all_options: ["אנאפורה", "אפיסטroפה", "שאלה רטורית", "ניגוד", "השוואה", "אירוניה"]
        },
        {
             text: `We shall go on to the end, we shall fight in France, <span class='highlight' data-index='0'>we shall fight on the seas and oceans</span>, <span class='highlight' data-index='1'>we shall fight with growing confidence and growing strength in the air</span>, <span class='highlight' data-index='2'>we shall defend our Island, whatever the cost may be</span>, <span class='highlight' data-index='3'>we shall fight on the beaches</span>, <span class='highlight' data-index='4'>we shall fight on the landing grounds</span>, <span class='highlight' data-index='5'>we shall fight in the fields and in the streets</span>, <span class='highlight' data-index='6'>we shall fight in the hills</span>; <span class='highlight' data-index='7'>we shall never surrender</span>.`,
             devices: [
                 { index: 0, device: "אנאפורה", feedback: "נכון! חזרה על 'we shall fight' או 'we shall' בתחילת ביטויים רבים היא אנאפורה שמחזקת את הנחישות וההחלטה להמשיך בלחימה." },
                 { index: 1, device: "אנאפורה", feedback: "מדויק! האנאפורה ממשיכה לבנות את רצף הפעולות ואת התחושה של נחישות בלתי מתפשרת בכל החזיתות." },
                 { index: 2, device: "אנאפורה", feedback: "אומנם הנוסח מעט שונה ('we shall defend'), אך הוא ממשיך את התבנית התחבירית החוזרת ומחזק את רעיון הפעולה הנחרצת, ועדיין נחשב לאנאפורה שמשרתת את ההדרגתיות הכוללת." }, // Adjusted feedback slightly
                 { index: 3, device: "אנאפורה", feedback: "נכון מאוד! שוב אנאפורה, בבנייה לקראת השיא. הדובר סוקר את כל המקומות בהם יתקיים המאבק." },
                 { index: 4, device: "אנאפורה", feedback: "יוצא מן הכלל! האנאפורה חוזרת ומדגישה את הפריסה הרחבה של המאבק בכל מקום אפשרי." },
                 { index: 5, device: "אנאפורה", feedback: "מצוין! האנאפורה ממשיכה, בונה את המומנטום ומעצימה את התחושה של מאבק עיקש ורחב היקף." },
                 { index: 6, device: "אנאפורה", feedback: "כמעט הגענו לשיא! גם כאן האנאפורה תורמת לתחושת המאבק הבלתי פוסק והמקיף בכל שטח אפשרי." },
                 { index: 7, device: "הדרגתיות", feedback: "מבריק! אומנם יש כאן גם אנאפורה סמויה ('we shall'), אבל הנקודה האחרונה 'we shall never surrender' היא שיא עוצמתי שמסכם את כל נקודות המאבק הקודמות בסדר עולה ומגיע למסקנה נחרצת. זו דוגמה קלאסית ומרשימה להדרגתיות (קלימקס)!" } // Enhanced feedback

             ],
              all_options: ["אנאפורה", "אפיסטרופה", "שאלה רטורית", "ניגוד", "הדרגתיות", "מטפורה"]
        },
        {
            text: `Let every nation know, whether it wishes us well or ill, that <span class='highlight' data-index='0'>we shall pay any price, bear any burden, meet any hardship, support any friend, oppose any foe to assure the survival and the success of liberty</span>.`,
             devices: [
                { index: 0, device: "הדרגתיות", feedback: "נכון מאוד! רצף הפעולות וההקרבות ('pay any price', 'bear any burden', 'meet any hardship', 'support any friend', 'oppose any foe') מסודר בסדר עולה של עוצמה ומחויבות, ויוצר אפקט מרשים של הדרגתיות שמחזק את הנחישות וההתחייבות למען החירות." }
            ],
            all_options: ["אנאפורה", "שאלה רטורית", "ניגוד", "הדרגתיות", "מטפורה", "השוואה"]
        },
         {
             text: `And that is how it was that far off in the Pacific, <span class='highlight' data-index='0'>America's golden boys, her fighting sons</span>, died to stop the spread of a cancerous ideology.`,
             devices: [
                 { index: 0, device: "מטפורה", feedback: "מצוין! הדימוי 'America's golden boys' ו'her fighting sons' אינו השוואה מפורשת, אלא שימוש מטפורי לתיאור החיילים כדבר יקר ערך או כחלק מהמשפחה הלאומית. כמו כן, 'a cancerous ideology' היא מטפורה חזקה נוספת המדמה אידיאולוגיה מזיקה למחלה קטלנית." } // Added mention of the second metaphor
             ],
             all_options: ["אנאפורה", "אפיסטרופה", "השוואה", "מטפורה", "אוקסימורון", "אירוניה"]
         },
          {
            text: `Now, I know the plans that I have for you,” declares the Lord, “plans to prosper you and not to harm you, <span class='highlight' data-index='0'>plans to give you hope and a future</span>.”`, // Jeremiah 29:11 - Used structure, not religious context itself
             devices: [
                 { index: 0, device: "אנאפורה", feedback: "נכון! החזרה על המילה 'plans' בתחילת היחידות התחביריות בונה כאן אנאפורה שמדגישה את התכנון והכוונה החיובית." }
             ],
             all_options: ["אנאפורה", "אפיסטרופה", "ניגוד", "השוואה", "מטפורה"]
          },
          {
              text: `Let us not wallow in the valley of despair, I say to you today, my friends. <span class='highlight' data-index='0'>And so let us go back to Mississippi, let us go back to Alabama, let us go back to South Carolina, let us go back to Georgia, let us go back to Louisiana, let us go back to the slums and ghettos of our northern cities</span>, knowing that somehow this situation can and will be changed.`, // From MLK Jr. again
              devices: [
                  { index: 0, device: "אנאפורה", feedback: "מצוין! החזרה הנמרצת על 'let us go back' מהווה אנאפורה שיוצרת קצב ודוחפת את הקהל לדמיין את המסע חזרה ולפעולה." }
              ],
              all_options: ["אנאפורה", "אפיסטרופה", "הדרגתיות", "מטפורה", "השוואה"]
          }

        // Add more snippets here following the structure
    ];

    let currentSnippetIndex = 0;
    let activeHighlightElement = null; // To track the currently selected highlight

    // Function to update the progress indicator
    function updateProgressIndicator() {
         const totalHighlights = speechTextDiv.querySelectorAll('.highlight, .correctly-identified').length;
         const identifiedHighlights = speechTextDiv.querySelectorAll('.correctly-identified').length;

         if (totalHighlights > 0) {
             progressIndicator.classList.remove('hidden');
             identifiedCountSpan.textContent = identifiedHighlights;
             totalHighlightsSpan.textContent = totalHighlights;
         } else {
             progressIndicator.classList.add('hidden');
         }

         // Show next button if all identified
         if (identifiedHighlights === totalHighlights && totalHighlights > 0) {
             nextSnippetBtn.classList.remove('hidden');
         } else {
             nextSnippetBtn.classList.add('hidden');
         }
    }


    // Function to render the current snippet
    function renderSnippet(index) {
        // Hide previous elements with animation
        speechTextDiv.style.opacity = 0;
        deviceOptionsDiv.classList.remove('visible');
        feedbackDiv.classList.remove('visible');
        nextSnippetBtn.classList.add('hidden');
        progressIndicator.classList.add('hidden'); // Hide progress during transition

        setTimeout(() => { // Delay rendering for animation effect
            const snippet = speechData[index];
            speechTextDiv.innerHTML = snippet.text; // Use innerHTML because the highlights are part of the string
             rhetoricAppContainer.scrollTop = 0; // Scroll to top for new snippet


            // Add event listeners to the highlighted parts
            speechTextDiv.querySelectorAll('.highlight').forEach(element => {
                element.addEventListener('click', handleHighlightClick);
            });

            // Reset options and feedback visibility
            deviceOptionsDiv.classList.add('hidden');
            optionsListDiv.innerHTML = ''; // Clear previous options
            feedbackDiv.classList.add('hidden');
            feedbackDiv.textContent = ''; // Clear feedback text

             activeHighlightElement = null; // Reset active highlight

            // Update progress indicator and show speech text
            updateProgressIndicator();
            speechTextDiv.style.opacity = 1; // Fade in speech text


        }, 400); // Match CSS transition duration
    }

    // Function to handle click on a highlighted part
    function handleHighlightClick(event) {
        const target = event.target;

        // If another highlight is active, or this one is already identified, do nothing
        if (activeHighlightElement || target.classList.contains('correctly-identified')) {
             if (target.classList.contains('correctly-identified')) {
                 // If already identified, maybe show feedback again briefly?
                 const index = parseInt(target.dataset.index);
                 const snippet = speechData[currentSnippetIndex];
                 const deviceInfo = snippet.devices.find(d => d.index === index);
                 if (deviceInfo) {
                      displayFeedback(deviceInfo.feedback, true, true); // Show correct feedback briefly
                 }
             }
            return;
        }

        // Set the clicked highlight as active
        activeHighlightElement = target;
        activeHighlightElement.classList.add('active-highlight');


        // Hide previous feedback and options with animation
        feedbackDiv.classList.remove('visible');
        deviceOptionsDiv.classList.remove('visible');


        setTimeout(() => { // Delay showing new options
             optionsListDiv.innerHTML = ''; // Clear previous options
             feedbackDiv.classList.add('hidden'); // Hide feedback entirely after animation

            // Display options for the user to choose
            const snippet = speechData[currentSnippetIndex];
            snippet.all_options.forEach(device => {
                const button = document.createElement('button');
                button.textContent = device;
                button.dataset.device = device;
                // Store index of the clicked highlight directly on the button
                 button.dataset.highlightIndex = target.dataset.index;

                optionsListDiv.appendChild(button);
            });

            deviceOptionsDiv.classList.remove('hidden');
            // Force reflow to restart CSS transition
            void deviceOptionsDiv.offsetWidth;
            deviceOptionsDiv.classList.add('visible');


            // Add event listeners to the device option buttons
            optionsListDiv.querySelectorAll('button').forEach(button => {
                button.addEventListener('click', handleOptionClick);
            });
        }, 300); // Short delay for feedback/options fade out

    }

    // Function to handle clicking a device option
    function handleOptionClick(event) {
        const selectedDevice = event.target.dataset.device;
        const highlightIndex = parseInt(event.target.dataset.highlightIndex); // Get index from button data
        const snippet = speechData[currentSnippetIndex];
        const deviceInfo = snippet.devices.find(d => d.index === highlightIndex);
        const highlightElement = speechTextDiv.querySelector(`.highlight[data-index='${highlightIndex}']`);

        // Disable all option buttons related to this highlight temporarily
         optionsListDiv.querySelectorAll(`button[data-highlight-index='${highlightIndex}']`).forEach(button => {
              button.disabled = true;
         });


        if (deviceInfo && selectedDevice === deviceInfo.device) {
            // Correct answer
            displayFeedback(deviceInfo.feedback, true);
            highlightElement.classList.add('correctly-identified');
            highlightElement.classList.remove('highlight', 'active-highlight'); // Remove original highlight classes
            highlightElement.style.borderBottom = 'none'; // Remove the border dashed line (CSS class handles this now)
            highlightElement.style.cursor = 'default'; // Change cursor (CSS class handles this now)
            highlightElement.removeEventListener('click', handleHighlightClick); // Remove listener


             // Clear active highlight and hide options after a delay
             activeHighlightElement = null;
             setTimeout(() => {
                  deviceOptionsDiv.classList.remove('visible');
                   setTimeout(() => { deviceOptionsDiv.classList.add('hidden'); }, 400); // Hide completely after animation
             }, 1500); // Keep options visible for 1.5s after correct answer

            updateProgressIndicator(); // Update count and check for next snippet

        } else {
            // Incorrect answer
             let incorrectFeedback = `לא בדיוק. '${selectedDevice}' אינו הכלי העיקרי שמודגם בקטע זה. נסה שוב.`;
             // Add a hint
             if (deviceInfo) {
                  switch(deviceInfo.device) {
                       case "אנאפורה": incorrectFeedback += " רמז: האם יש כאן חזרה על מילים או ביטויים בתחילת שורות/משפטים?"; break;
                       case "אפיסטרופה": incorrectFeedback += " רמז: האם יש כאן חזרה על מילים או ביטויים בסוף שורות/משפטים?"; break;
                       case "שאלה רטורית": incorrectFeedback += " רמז: האם זו שאלה שנשאלת כדי לגרום לך לחשוב, ולא כדי לקבל תשובה מילולית?"; break;
                       case "ניגוד": incorrectFeedback += " רמז: האם מוצגים כאן שני רעיונות מנוגדים זה לצד זה, אולי במבנה מאוזן?"; break;
                       case "השוואה": incorrectFeedback += " רמז: חפש מילות השוואה מפורשות כמו 'כמו', 'כאילו'."; break;
                       case "מטפורה": incorrectFeedback += " רמז: חפש דימוי מרומז בין דברים שונים, הצגה של דבר אחד כדבר אחר."; break;
                       case "אוקסימורון": incorrectFeedback += " רמז: חפש צירוף של שתי מילים הסותרות זו את זו לכאורה."; break;
                       case "הדרגתיות": incorrectFeedback += " רמז: האם יש כאן סדרה של פריטים (מילים, ביטויים, רעיונות) המסודרים לפי עוצמה עולה?"; break;
                       case "אירוניה": incorrectFeedback += " רמז: האם נאמר משהו אחד בזמן שהכוונה היא הפוכה?"; break;
                  }
             }

            displayFeedback(incorrectFeedback, false);

             // Re-enable buttons related to this highlight after a short delay
             setTimeout(() => {
                 optionsListDiv.querySelectorAll(`button[data-highlight-index='${highlightIndex}']`).forEach(button => {
                    // Only re-enable if the highlight hasn't been correctly identified by another click (shouldn't happen with activeHighlight logic, but belt and suspenders)
                     if (!highlightElement.classList.contains('correctly-identified')) {
                         button.disabled = false;
                     }
                 });
             }, 500); // Short delay


            // Clear active highlight after feedback is shown
             activeHighlightElement.classList.remove('active-highlight');
             activeHighlightElement = null;

             // Keep options visible for retrying
             // deviceOptionsDiv.classList.remove('hidden'); // Ensure they stay visible

        }
    }

    // Function to display feedback with animation
    function displayFeedback(message, isCorrect, isBrief = false) {
        feedbackDiv.textContent = message;
        feedbackDiv.className = ''; // Reset classes
        feedbackDiv.classList.add('feedback'); // Add base class
        feedbackDiv.classList.add(isCorrect ? 'correct' : 'incorrect');

        feedbackDiv.classList.remove('hidden');
        // Force reflow to restart CSS transition
        void feedbackDiv.offsetWidth;
        feedbackDiv.classList.add('visible');

        if (isBrief) {
             setTimeout(() => {
                 feedbackDiv.classList.remove('visible');
                 setTimeout(() => { feedbackDiv.classList.add('hidden'); }, 400);
             }, 1500); // Show brief feedback for 1.5 seconds
        }
    }

    // Handle Next Snippet button click
    nextSnippetBtn.addEventListener('click', () => {
        currentSnippetIndex++;
        if (currentSnippetIndex < speechData.length) {
            renderSnippet(currentSnippetIndex);
        } else {
            // End of snippets
            speechTextDiv.innerHTML = "<p>🎉 כל הכבוד! סיימת לתרגל את זיהוי הכלים הרטוריים בקטעים אלו. עכשיו תוכל ליישם את הידע הזה על נאומים אחרים שתפגוש! תוכל לרענן את הדף כדי להתחיל מחדש, או לקרוא את המדריך המלא לכלים רטוריים מטה.</p>";
            speechTextDiv.style.opacity = 1; // Ensure final message is visible
            deviceOptionsDiv.classList.add('hidden');
            deviceOptionsDiv.classList.remove('visible');
            feedbackDiv.classList.add('hidden');
            feedbackDiv.classList.remove('visible');
            nextSnippetBtn.classList.add('hidden');
            progressIndicator.classList.add('hidden');
        }
    });

    // Handle Explanation button click
     toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationDiv.classList.contains('hidden');
        if (isHidden) {
            explanationDiv.classList.remove('hidden');
            toggleExplanationBtn.textContent = 'הסתר מדריך';
             toggleExplanationBtn.style.backgroundColor = '#eaf2f8';
             toggleExplanationBtn.style.color = '#2980b9';
             toggleExplanationBtn.style.borderColor = '#2980b9';

        } else {
            explanationDiv.classList.add('hidden');
            toggleExplanationBtn.textContent = 'הצגת המדריך המלא לכלים רטוריים';
             toggleExplanationBtn.style.backgroundColor = ''; /* Reset */
             toggleExplanationBtn.style.color = '#3498db'; /* Reset */
             toggleExplanationBtn.style.borderColor = '#3498db'; /* Reset */

        }
        // Optional: scroll to explanation? No, let's just toggle visibility.
    });


    // Initialize the application
    renderSnippet(currentSnippetIndex);
});
</script>
```