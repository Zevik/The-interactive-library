---
title: "כלים שלובים בהיסטוריה: מסע מרתק בעקבות כלי החקלאות"
english_slug: tools-of-history-journey-through-agricultural-tools
category: "ארכאולוגיה"
tags: [כלי חקלאות היסטוריים, ארכיאולוגיה, היסטוריה של הטכנולוגיה, התפתחות החקלאות, עבודה חקלאית, חידון]
---
<div class="container">
    <h1>כלים שלובים בהיסטוריה: מסע מרתק בעקבות כלי החקלאות</h1>
    <p class="intro-text">צאו למסע בזמן וגלו את כלי העבודה שעיצבו את חיי אבות אבותינו והיו המפתח להתפתחות הציוויליזציה. האם תצליחו לזהות אותם ולגלות כיצד שינו את פני האדמה? בואו נראה כמה אתם מכירים את המהפכות הטכנולוגיות של העבר!</p>

    <div id="interactive-app" class="game-container">
        <div id="tool-display" class="tool-section">
            <img id="tool-image" src="" alt="כלי חקלאי היסטורי">
             <div id="tool-counter"></div> <!-- Added for progress -->
            <div id="score" class="score-display">ניקוד: 0</div>
        </div>

        <div id="question-area" class="questions-section">
            <div class="question-block">
                <p class="question-title">1. מהו שם הכלי?</p>
                <div id="name-options" class="options-container"></div>
            </div>
            <div class="question-block">
                <p class="question-title">2. באיזו תקופה היסטורית הכלי היה בשימוש עיקרי?</p>
                <div id="period-options" class="options-container"></div>
            </div>
            <div class="question-block">
                <p class="question-title">3. מהי הפונקציה העיקרית של הכלי?</p>
                <div id="function-options" class="options-container"></div>
            </div>
        </div>

        <div class="button-area">
            <button id="submit-answer" class="game-button">בדיקה</button>
            <button id="next-tool" class="game-button primary" style="display: none;">כלי הבא >></button>
        </div>

        <div id="feedback" class="feedback-area"></div>
        <div id="tool-explanation" class="tool-explanation"></div>

        <div id="game-over" class="game-over" style="display: none;">
            <h2>סוף המשחק! 🎉</h2>
            <p>סיימת את כל הכלים. הניקוד הסופי שלך: <span id="final-score"></span></p>
            <button id="restart-game" class="game-button primary">התחל משחק חדש</button>
        </div>
    </div>

     <div class="explanation-toggle-area">
        <button id="toggle-explanation" class="game-button secondary">הצג הסבר מורחב על התפתחות החקלאות</button>
     </div>

    <div id="full-explanation" class="full-explanation" style="display: none;">
        <h2>הסבר מורחב: כלים שלובים בהיסטוריה של החקלאות</h2>
        <p>החקלאות אינה רק שיטה להפקת מזון; היא מהפכה שעיצבה מחדש את חיי האדם, את החברה ואת הסביבה. המעבר מליקוט וציד לחקלאות יושבת אפשר גידול אוכלוסין, הקמת יישובי קבע, התפתחות של מבנים חברתיים מורכבים יותר וצמיחתן של תרבויות עשירות.</p>
        <p>התפתחות זו הייתה בלתי אפשרית ללא התפתחות מקבילה בכלי החקלאות. כלי העבודה שימשו כמרחיבי יכולת האדם, אפשרו לו להתמודד עם אתגרים פיזיים כמו עיבוד אדמה קשה, קציר יבולים ביעילות וטיפול בתוצרת. ההיסטוריה של כלי החקלאות היא למעשה היסטוריה של התפתחות טכנולוגית ושל הסתגלות אנושית.</p>

        <h3>סקירה כללית של התפתחות כלי החקלאות בתקופות שונות:</h3>
        <ul>
            <li><strong>תקופת האבן (הפלאוליתית, הנאוליתית):</strong> בתקופות הקדומות ביותר, כלי החקלאות היו פשוטים ועשויים מחומרים זמינים: אבן, עץ ועצם. דוגמאות כוללות מקלות חפירה פשוטים לרכך אדמה או לזרוע, ומגלי אבן או עצם עם להבי צור או אובסידיאן לקציר דגנים פראיים או מבויתים מוקדמים. הכלים הללו דרשו עבודה פיזית רבה והיו מוגבלים ביעילותם.</li>
            <li><strong>תקופת הברונזה והברזל:</strong> גילוי ושימוש במתכות הביאו למהפכה של ממש. הכלים הפכו חזקים יותר, עמידים יותר וניתנים לעיצוב מדויק יותר. הופיעו מגלי מתכת (ברונזה ואחר כך ברזל) יעילים יותר, ומחרשות פשוטות שנגררו תחילה על ידי בני אדם ואחר כך על ידי בהמות משא (שוורים). כלים אלו אפשרו לעבד שטחים גדולים יותר ולהגדיל את התפוקה.</li>
            <li><strong>העת העתיקה וימי הביניים:</strong> בתקופות אלו נמשכו השיפורים. הרומאים פיתחו סוגים שונים של מחרשות, ובצפון אירופה בימי הביניים הופיעה מחרשת הגלגלים הכבדה, עם להב מתכת הפוך (moldboard) שיכול היה להפוך את האדמה ביעילות בקרקעות הכבדות והפוריות של צפון אירופה. כלים נוספים כמו מעדרים משופרים, קלשונים ומגרפות עץ או מתכת נכנסו לשימוש נרחב.</li>
            <li><strong>העידן המודרני המוקדם (מהרנסנס ועד המהפכה התעשייתית):</strong> תקופה זו ראתה שיפורים הדרגתיים בכלים קיימים, כמו גם תחילת הפיתוח של מכונות חקלאיות מורכבות יותר, כמו זורעים (seed drills) מכניים ראשונים וקציר מכני ניסיוני. התפתחות המטלורגיה וההנדסה הניחה את היסודות למהפכה התעשייתית בחקלאות.</li>
        </ul>

        <h3>הקשר בין כלי החקלאות לשיטות העיבוד והשפעתם על התפוקה החקלאית:</h3>
        <p>כלי העבודה לא רק שינו את אופן העבודה, אלא גם אפשרו שיטות עיבוד חדשות. המחרשה אפשרה חריש עמוק יותר שהגדיל את פוריות הקרקע ודיכא עשבים. מגלי המתכת אפשרו קציר מהיר ויעיל יותר, והקלשון והמגרפה סייעו באיסוף התוצרת והכנת הקרקע. כל שיפור בכלי הביא בדרך כלל לגידול ביעילות העבודה ובתפוקת היבול ליחידת שטח, מה שאיפשר לקיים אוכלוסיות גדולות יותר.</p>

        <h3>השפעת התפתחות כלי החקלאות על מבנה החברה והכלכלה:</h3>
        <p>גידול התפוקה החקלאית שנגרם משיפור הכלים היה בעל השפעה עמוקה על החברה והכלכלה. עודף מזון איפשר לחלק מהאוכלוסייה לעסוק במקצועות שאינם חקלאות (סוחרים, בעלי מלאכה, כהני דת, פקידים), מה שהוביל להתפתחות ערים וריבוד חברתי. התפתחות כלים כמו מחרשת הגלגלים הכבדה, שדרשה מספר בהמות וצוות עובדים, עודדה שיתוף פעולה קהילתי או התפתחות חקלאות בקנה מידה גדול יותר (כמו אחוזות פיאודליות). כך, ההתפתחות הטכנולוגית בחקלאות הייתה קשורה קשר בל יינתק לשינויים חברתיים, כלכליים ופוליטיים.</p>

        <h3>דוגמאות לכלים איקוניים וסיפורם ההיסטורי:</h3>
        <ul>
            <li><strong>המחרשה:</strong> אולי הכלי החקלאי המשפיע ביותר בהיסטוריה. מהמקל הפשוט ועד למחרשת המתכת המורכבת, המחרשה אפשרה להפוך את האדמה, להכין אותה לזריעה, ולהילחם בעשבים. היא הייתה הבסיס לחקלאות אינטנסיבית ואיפשרה יישוב קבע רחב היקף.</li>
            <li><strong>המגל והמחרשה:</strong> יחד, המגל (לקציר) והמחרשה (לחריש) הם סמלים מובהקים של החקלאות הקלאסית והמסורתית. הם אפשרו את מחזור הגידול השנתי והיו בשימוש יומיומי על ידי חקלאים במשך אלפי שנים.</li>
            <li><strong>הקלשון:</strong> כלי פשוט אך רב-תכליתי, ששימש להרים, להעביר ולפזר חומרים כמו חציר, קש וזבל. שיפורים בחומרי הגלם אפשרו יצירת קלשונים קלים וחזקים יותר שייעלו עבודות רבות במשק החקלאי.</li>
        </ul>
        <p>הכלים הללו, שנראים לנו היום פשוטים, היו שיאי טכנולוגיה בתקופתם ושינו את יכולת האדם לעבוד את האדמה בצורה דרמטית, והניחו את היסודות לעולם המודרני שאנו מכירים.</p>
    </div>
</div>


<style>
    /* General Styles */
    .container {
        font-family: 'Arial', sans-serif;
        max-width: 800px;
        margin: 20px auto;
        padding: 0 20px; /* Add horizontal padding */
        direction: rtl;
        text-align: right;
        color: #333;
    }

    h1 {
        color: #2c3e50; /* Dark blue/grey */
        text-align: center;
        margin-bottom: 20px;
    }

    .intro-text {
        text-align: center;
        margin-bottom: 30px;
        font-size: 1.1em;
        color: #555;
    }

    /* Game Container */
    .game-container {
        background-color: #ecf0f1; /* Light grey */
        border: 1px solid #bdc3c7; /* Grey border */
        border-radius: 12px; /* More rounded corners */
        padding: 25px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        margin-bottom: 20px;
    }

    /* Tool Display Section */
    .tool-section {
        text-align: center;
        margin-bottom: 30px;
        position: relative; /* Needed for absolute positioning of counter */
    }

    #tool-image {
        max-width: 100%;
        height: auto;
        min-height: 150px; /* Ensure some space even before image loads */
        border: 1px solid #bdc3c7;
        border-radius: 8px;
        background-color: #ffffff; /* White background */
        padding: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
        transition: opacity 0.5s ease-in-out; /* Fade animation */
    }

     #tool-image.fade-in {
         opacity: 1;
     }

    #tool-counter {
        position: absolute;
        top: 15px; /* Position at top-right */
        left: 15px;
        background-color: rgba(44, 62, 80, 0.8); /* Dark background with transparency */
        color: white;
        padding: 5px 10px;
        border-radius: 20px;
        font-size: 0.9em;
        font-weight: bold;
        z-index: 10; /* Ensure it's above the image */
    }

    .score-display {
        margin-top: 15px;
        font-size: 1.3em;
        font-weight: bold;
        color: #27ae60; /* Green for score */
        transition: color 0.3s ease; /* Smooth color transition */
    }

    /* Questions Section */
    .questions-section {
        margin-bottom: 20px;
    }

    .question-block {
        margin-bottom: 20px; /* More space between questions */
        padding: 15px;
        background-color: #ffffff; /* White background */
        border: 1px solid #dcdcdc; /* Lighter border */
        border-radius: 8px;
    }

    .question-title {
        margin-top: 0;
        margin-bottom: 12px; /* Space below title */
        font-size: 1.1em;
        font-weight: bold;
        color: #34495e; /* Darker grey/blue */
    }

    .options-container {
        display: flex;
        flex-wrap: wrap;
        gap: 10px; /* Space between option buttons */
    }

    /* Style for Radio Button Labels (as buttons) */
    .options-container label {
        background-color: #e0e0e0; /* Light grey */
        padding: 10px 15px;
        border-radius: 25px; /* Pill shape */
        cursor: pointer;
        transition: background-color 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
        border: 1px solid #ccc;
        font-size: 1em;
        user-select: none; /* Prevent text selection */
    }

    .options-container input[type="radio"] {
        display: none; /* Hide default radio button */
    }

    .options-container input[type="radio"]:checked + label {
        background-color: #a0d468; /* Greenish */
        border-color: #8dc253; /* Darker green */
        color: #333;
        box-shadow: 0 1px 4px rgba(0, 0, 0, 0.2);
    }

    .options-container label:hover {
        background-color: #d5d5d5; /* Darker grey on hover */
    }

    /* Styles for feedback on options AFTER check */
    .options-container label.correct {
        background-color: #2ecc71; /* Emerald green */
        color: white;
        border-color: #27ae60;
        font-weight: bold;
    }

     /* Apply correct style to checked AND correct label after submit */
     .options-container input[type="radio"]:checked + label.correct {
         background-color: #2ecc71; /* Ensure correct green for checked correct */
         color: white;
         border-color: #27ae60;
         font-weight: bold;
     }

    .options-container label.incorrect {
        background-color: #e74c3c; /* Alizarin red */
        color: white;
        border-color: #c0392b;
        font-weight: bold;
    }

     /* Apply incorrect style to checked AND incorrect label after submit */
      .options-container input[type="radio"]:checked + label.incorrect {
        background-color: #e74c3c; /* Ensure incorrect red for checked incorrect */
        color: white;
        border-color: #c0392b;
        font-weight: bold;
    }


    /* Button Area */
    .button-area {
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    /* Game Buttons */
    .game-button {
        display: inline-block; /* Align buttons */
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 25px; /* More rounded */
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
        text-decoration: none; /* For potential link-like buttons */
    }

    .game-button:hover {
        transform: translateY(-2px); /* Slight lift effect */
    }

    .game-button:active {
         transform: translateY(0); /* Press effect */
    }


    #submit-answer {
        background-color: #3498db; /* Peter river blue */
        color: white;
    }

    #submit-answer:hover {
        background-color: #2980b9; /* Darker blue */
    }

    .game-button.primary {
        background-color: #2ecc71; /* Emerald green */
        color: white;
        margin-right: 10px; /* Space between buttons if multiple */
    }

    .game-button.primary:hover {
         background-color: #27ae60; /* Darker green */
    }

     .game-button.secondary {
        background-color: #f39c12; /* Orange */
        color: white;
        margin-right: 0; /* No right margin for this button */
     }
     .game-button.secondary:hover {
        background-color: #e67e22; /* Darker orange */
     }

     .explanation-toggle-area {
         text-align: center;
         margin-top: 30px;
         margin-bottom: 30px;
     }


    /* Feedback Area */
    .feedback-area {
        margin-top: 15px;
        padding: 15px;
        border-radius: 8px;
        min-height: 1.5em; /* Reserve space */
        font-size: 1.1em;
        font-weight: bold;
        text-align: center; /* Center feedback text */
         opacity: 0; /* Start hidden */
         transition: opacity 0.5s ease-in-out; /* Fade in */
    }
     .feedback-area.visible {
         opacity: 1;
     }

    .feedback-correct {
        background-color: #d4edda; /* Light green */
        color: #155724; /* Dark green */
        border: 1px solid #c3e6cb;
    }

    .feedback-incorrect {
        background-color: #f8d7da; /* Light red */
        color: #721c24; /* Dark red */
        border: 1px solid #f5c6cb;
    }

    /* Tool Explanation */
    .tool-explanation {
        margin-top: 20px;
        padding: 15px;
        background-color: #ecf0f1; /* Light grey */
        border: 1px solid #bdc3c7;
        border-radius: 8px;
        display: none; /* Hidden initially */
        opacity: 0; /* Start hidden for animation */
        transform: translateY(10px); /* Start slightly below */
        transition: opacity 0.5s ease-out, transform 0.5s ease-out; /* Slide up and fade in */
    }

    .tool-explanation.visible {
        display: block; /* Show to apply transitions */
        opacity: 1;
        transform: translateY(0);
    }

     .tool-explanation h3 {
         margin-top: 0;
         color: #34495e;
         border-bottom: 1px solid #dcdcdc;
         padding-bottom: 5px;
         margin-bottom: 10px;
     }

    /* Game Over Screen */
    .game-over {
        text-align: center;
        margin-top: 30px;
        padding: 30px;
        background-color: #dcf0fa; /* Light blue */
        border: 1px solid #aed6f1;
        border-radius: 12px;
         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .game-over h2 {
        color: #2e86c1; /* Blue */
        margin-top: 0;
        margin-bottom: 15px;
    }

    .game-over p {
        font-size: 1.2em;
        margin-bottom: 20px;
    }

    #final-score {
        font-size: 1.5em;
        font-weight: bold;
        color: #27ae60; /* Green */
    }

    /* Full Explanation Section */
    .full-explanation {
        margin-top: 20px;
        padding: 25px;
        border: 1px solid #bdc3c7;
        border-radius: 12px;
        background-color: #ecf0f1;
        direction: rtl;
        text-align: right;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
        display: none; /* Hidden initially */
        opacity: 0; /* Start hidden for animation */
        transform: translateY(10px); /* Start slightly below */
        transition: opacity 0.5s ease-out, transform 0.5s ease-out; /* Slide up and fade in */
    }

     .full-explanation.visible {
        display: block; /* Show to apply transitions */
        opacity: 1;
        transform: translateY(0);
    }

    .full-explanation h2, .full-explanation h3 {
        color: #2c3e50;
        border-bottom: 1px solid #dcdcdc;
        padding-bottom: 5px;
        margin-top: 20px;
        margin-bottom: 15px;
    }

    .full-explanation ul {
        list-style-type: disc;
        margin-right: 20px;
        padding-right: 0;
        line-height: 1.6;
    }
     .full-explanation li {
        margin-bottom: 10px;
     }

    /* Responsive adjustments */
    @media (max-width: 600px) {
        .container {
            padding: 0 10px;
        }

        .game-container, .full-explanation {
            padding: 15px;
        }

        .options-container {
            flex-direction: column; /* Stack options vertically on small screens */
        }

        .options-container label {
             width: 100%; /* Make labels take full width */
             box-sizing: border-box; /* Include padding and border in width */
             text-align: center;
        }

        .game-button {
            width: 100%;
            margin-bottom: 10px;
        }

         .game-button.primary {
             margin-right: 0; /* Remove margin on small screens */
         }
         .button-area button {
             display: block; /* Stack buttons */
         }
    }
</style>

<script>
    const tools = [
        {
            image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Flint_sickle.jpg/1200px-Flint_sickle.jpg', // Example image, replace with actual tool images
            name: 'מגל אבן',
            period: 'תקופת האבן הנאוליתית',
            function: ['קציר', 'עיבוד צמחים'],
            options: {
                name: ['מגל אבן', 'מחרשת עץ', 'מעדר ברונזה', 'קלשון מתכת'],
                period: ['תקופת הברונזה', 'תקופת האבן הנאוליתית', 'ימי הביניים', 'העידן המודרני'],
                function: ['חרישה', 'זריעה', 'קציר', 'עיבוד צמחים', 'דיש']
            },
            explanation: 'מגל אבן היה אחד מכלי הקציר הראשונים, ששימש לקצירת דגנים בתקופה הנאוליתית, כאשר החקלאות החלה להתפתח. הוא כלל להב עשוי אבן צור או אובסידיאן שהוכנס לתוך ידית עץ או עצם. השימוש בו היה איטי ודרש מאמץ רב, אך הוא איפשר את המעבר מליקוט שיבולים לקציר שיטתי.'
        },
        {
            image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Reconstructed_Bronze_Age_Plough_%28arere%29.jpg/1200px-Reconstructed_Bronze_Age_Plough_%28arere%29.jpg',
            name: 'מחרשת עץ (אררה)',
            period: 'תקופת הברונזה/הברזל',
            function: ['חרישה'],
            options: {
                name: ['מגל מתכת', 'מחרשת עץ (אררה)', 'מעדר ברזל', 'קלשון'],
                period: ['תקופת האבן', 'העת העתיקה', 'תקופת הברונזה/הברזל', 'העידן המודרני'],
                function: ['חרישה', 'קציר', 'דיש', 'השקיה']
            },
            explanation: 'מחרשת העץ הפשוטה, המכונה "אררה" או מחרשת שרטוט, הופיעה בתקופת הברונזה או הברזל. היא שרטטה את פני הקרקע ויצרה תלם רדוד לזריעה, מבלי להפוך את האדמה. נגררה תחילה על ידי אדם ואחר כך על ידי בהמות משא כמו שוורים, והייתה צעד חשוב באפשרות עיבוד שטחים גדולים יותר ושיפור פוריות הקרקע בהשוואה לעיבוד ידני.'
        },
         {
            image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Roman_hoe_with_iron_blade_and_wooden_handle.jpg/800px-Roman_hoe_with_iron_blade_and_wooden_handle.jpg',
            name: 'מעדר',
            period: 'העת העתיקה/ימי הביניים',
            function: ['עידור', 'ניכוש עשבים', 'כיסוי זרעים'],
            options: {
                name: ['מגל', 'מחרשה', 'מעדר', 'מגרפה'],
                period: ['תקופת האבן', 'העת העתיקה/ימי הביניים', 'העידן המודרני המוקדם', 'העת החדשה'],
                function: ['חרישה', 'קציר', 'דיש', 'עידור', 'ניכוש עשבים', 'הובלת מים']
            },
            explanation: 'המעדר הוא כלי ותיק שהשתמשו בו למגוון משימות שאינן חריש עמוק: ניכוש עשבים בין הצמחים, ריכוך אדמה עליונה, כיסוי זרעים לאחר זריעה, ואף ככלי חפירה פשוט לעיבוד חלקות קטנות. להביו השתנו מחומרים כמו אבן ועצם לברזל, מה שהפך אותו ליעיל ועמיד יותר.'
        },
         {
            image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Sickle_and_sheaf.jpg/1200px-Sickle_and_sheaf.jpg',
            name: 'מגל מתכת',
            period: 'תקופת הברונזה/הברזל ואילך',
            function: ['קציר'],
            options: {
                name: ['מגל מתכת', 'קלשון', 'חרמש', 'מגרפת מתכת'],
                period: ['תקופת האבן', 'תקופת הברונזה/הברזל ואילך', 'העת העתיקה בלבד', 'העידן המודרני בלבד'],
                function: ['חרישה', 'קציר', 'עידור', 'איסוף קש']
            },
            explanation: 'מגל המתכת, העשוי מברונזה או ברזל, החליף את מגלי האבן וסיפק כלי קציר יעיל בהרבה. הלהב החד והעמיד אפשר קציר מהיר יותר של דגנים, שהיוו בסיס למזון עבור אוכלוסיות גדלות. הוא נשאר כלי נפוץ לחקלאים קטנים גם אל תוך העידן המודרני.'
        },
        {
            image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Scythe.JPG/1200px-Scythe.JPG',
            name: 'חרמש',
            period: 'ימי הביניים/העידן המודרני המוקדם',
            function: ['קציר'],
            options: {
                name: ['מגל', 'חרמש', 'מגרפה', 'מעדר'],
                period: ['העת העתיקה', 'ימי הביניים/העידן המודרני המוקדם', 'תקופת האבן', 'העת החדשה'],
                function: ['חרישה', 'זריעה', 'קציר', 'דיש']
            },
            explanation: 'החרמש הוא כלי קציר גדול יותר מהמגל, עם ידית ארוכה שמאפשרת לקוצר לעמוד זקוף יחסית. הוא הפך נפוץ בימי הביניים והעידן המודרני המוקדם לקציר יעיל יותר של דגנים ועשבים בשטחים גדולים. השימוש בו דרש מיומנות גבוהה והיה מסוכן, אך מהיר בהרבה ממגל בשדות נרחבים.'
        },
         {
            image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Pitchfork_-_geograph.org.uk_-_1284623.jpg/1200px-Pitchfork_-_geograph.org.uk_-_1284623.jpg',
            name: 'קלשון',
            period: 'ימי הביניים/העידן המודרני המוקדם',
            function: ['הובלת חומרים אורגניים', 'איסוף קש/חציר', 'פיזור זבל'],
            options: {
                name: ['מגל', 'קלשון', 'מחרשה', 'מעדר'],
                period: ['תקופת האבן', 'תקופת הברונזה', 'ימי הביניים/העידן המודרני המוקדם', 'העת העתיקה'],
                function: ['חרישה', 'קציר', 'דיש', 'הובלת חומרים אורגניים', 'זריעה']
            },
            explanation: 'הקלשון, עם שיניו הארוכות, היה כלי חיוני להעברה ופיזור של חומרים בתפזורת כמו חציר, קש וזבל - עבודות שכיחות וחשובות במשק החקלאי. גרסאות מוקדמות היו עשויות עץ, אך קלשוני מתכת שהופיעו מימי הביניים הפכו נפוצים וקלים יותר לשימוש.'
        }
        // Add more tools here following the same structure if needed
    ];

    let currentToolIndex = 0;
    let score = 0;
    let shuffledTools = [];

    // Get DOM elements
    const toolImage = document.getElementById('tool-image');
    const toolCounter = document.getElementById('tool-counter'); // Get the new counter element
    const scoreDisplay = document.getElementById('score');
    const nameOptionsDiv = document.getElementById('name-options');
    const periodOptionsDiv = document.getElementById('period-options');
    const functionOptionsDiv = document.getElementById('function-options');
    const submitButton = document.getElementById('submit-answer');
    const feedbackDiv = document.getElementById('feedback');
    const toolExplanationDiv = document.getElementById('tool-explanation');
    const nextToolButton = document.getElementById('next-tool');
    const gameOverDiv = document.getElementById('game-over');
    const finalScoreSpan = document.getElementById('final-score');
    const restartButton = document.getElementById('restart-game');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const fullExplanationDiv = document.getElementById('full-explanation');
    const questionAreaDiv = document.getElementById('question-area'); // Get question area


    function shuffleArray(array) {
        const shuffled = [...array]; // Create a copy to avoid modifying original array
        for (let i = shuffled.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]]; // Swap elements
        }
        return shuffled;
    }

    function loadTool(index) {
        if (index >= shuffledTools.length) {
            endGame();
            return;
        }

        const tool = shuffledTools[index];

        // Reset elements state
        toolImage.classList.remove('fade-in'); // Remove fade-in class for next animation
        feedbackDiv.classList.remove('visible', 'feedback-correct', 'feedback-incorrect');
        feedbackDiv.textContent = '';
        toolExplanationDiv.classList.remove('visible');
        toolExplanationDiv.style.display = 'none'; // Ensure display none for transition
        submitButton.style.display = 'block';
        nextToolButton.style.display = 'none';
        gameOverDiv.style.display = 'none';
        questionAreaDiv.style.display = 'block';
        submitButton.disabled = false;

        // Set image source and animate fade-in
        toolImage.src = ''; // Clear source temporarily
        toolImage.alt = tool.name;
        setTimeout(() => { // Small delay to allow opacity transition
             toolImage.src = tool.image;
             toolImage.onload = () => { // Wait for image to load before fading in
                 toolImage.classList.add('fade-in');
             }
        }, 50);


        // Update tool counter
        toolCounter.textContent = `כלי ${index + 1} מתוך ${shuffledTools.length}`;


        // Render options
        renderOptions(nameOptionsDiv, tool.options.name, 'name');
        renderOptions(periodOptionsDiv, tool.options.period, 'period');
        renderOptions(functionOptionsDiv, tool.options.function, 'function');


         // Re-enable radio buttons and uncheck previous selections for the new question
        document.querySelectorAll('#question-area input[type="radio"]').forEach(radio => {
             radio.disabled = false;
             radio.checked = false;
             // Also remove correct/incorrect classes from labels
             const label = document.querySelector(`label[for="${radio.id}"]`);
             if(label) {
                 label.classList.remove('correct', 'incorrect');
             }
        });
    }

    function renderOptions(container, options, groupName) {
        container.innerHTML = ''; // Clear previous options
        // Shuffle options within each category for more variety
         const shuffledOptions = shuffleArray(options);

        shuffledOptions.forEach(option => {
            const input = document.createElement('input');
            input.type = 'radio';
            // Create a safer ID, ensuring uniqueness
            const safeId = `${groupName}-${option.replace(/[^a-zA-Z0-9\u0590-\u05FF]/g, '').replace(/\s/g, '-')}-${Math.random().toString(36).substr(2, 5)}`;
            input.id = safeId;
            input.name = `${groupName}-option`;
            input.value = option;

            const label = document.createElement('label');
            label.htmlFor = input.id;
            label.textContent = option;

            container.appendChild(input);
            container.appendChild(label);
        });
    }

    function checkAnswer() {
        const currentTool = shuffledTools[currentToolIndex];

        const nameRadio = document.querySelector('input[name="name-option"]:checked');
        const periodRadio = document.querySelector('input[name="period-option"]:checked');
        const functionRadio = document.querySelector('input[name="function-option"]:checked');

        const selectedName = nameRadio?.value;
        const selectedPeriod = periodRadio?.value;
        const selectedFunction = functionRadio?.value;

        // Check if all selections were made
        if (!selectedName || !selectedPeriod || !selectedFunction) {
            feedbackDiv.textContent = 'אנא בחר תשובה בכל הקטגוריות לפני הבדיקה.';
            feedbackDiv.className = 'feedback-area feedback-incorrect visible';
            return; // Stop check if not all selected
        }

        // Check correctness
        const isNameCorrect = selectedName === currentTool.name;
        const isPeriodCorrect = selectedPeriod === currentTool.period;
        const isFunctionCorrect = currentTool.function.includes(selectedFunction);

        let totalCorrect = 0;
        if (isNameCorrect) totalCorrect++;
        if (isPeriodCorrect) totalCorrect++;
        if (isFunctionCorrect) totalCorrect++;

        let isCorrect = (totalCorrect === 3); // Full correct answer

        // Apply visual feedback to the selected options and reveal correct ones
        applyOptionFeedback(nameOptionsDiv, currentTool.name, selectedName, 'name-option');
        applyOptionFeedback(periodOptionsDiv, currentTool.period, selectedPeriod, 'period-option');
        applyOptionFeedback(functionOptionsDiv, currentTool.function, selectedFunction, 'function-option', true); // isMultiCorrect = true for function

        if (isCorrect) {
            score += 3; // Give 3 points for a fully correct answer
            feedbackDiv.textContent = 'כל הכבוד! התשובות נכונות!';
            feedbackDiv.className = 'feedback-area feedback-correct visible';
             // Optional: Animate score change
             scoreDisplay.style.color = '#2ecc71';
             setTimeout(() => { scoreDisplay.style.color = '#27ae60'; }, 1000);
        } else {
             // Give partial points for partially correct answers
             score += totalCorrect;
            let feedbackText = `יש לשפר. קיבלת ${totalCorrect} נקודות. `;
             if (!isNameCorrect) feedbackText += `שם הכלי הנכון: ${currentTool.name}. `;
             if (!isPeriodCorrect) feedbackText += `התקופה הנכונה: ${currentTool.period}. `;
             // For function, only mention the correct ones if the selected one was wrong
             if (!isFunctionCorrect) {
                  feedbackText += `אחת מהפונקציות הנכונות: ${currentTool.function.join(', ')}.`;
             }
            feedbackDiv.textContent = feedbackText.trim();
            feedbackDiv.className = 'feedback-area feedback-incorrect visible';
             // Optional: Animate score change (e.g., pulse or color change)
             scoreDisplay.style.color = '#e74c3c';
             setTimeout(() => { scoreDisplay.style.color = '#27ae60'; }, 1000);

        }

        scoreDisplay.textContent = `ניקוד: ${score}`;
        displayToolExplanation(currentTool.explanation);

        submitButton.style.display = 'none';
        submitButton.disabled = true; // Disable after submission
        nextToolButton.style.display = 'block';

        // Disable all radio buttons within the question area after checking
        document.querySelectorAll('#question-area input[type="radio"]').forEach(radio => {
             radio.disabled = true;
        });
    }

    function applyOptionFeedback(container, correctAnswer, selectedAnswer, groupName, isMultiCorrect = false) {
        const options = container.querySelectorAll('input[name="' + groupName + '"]');
        options.forEach(radio => {
            const label = document.querySelector(`label[for="${radio.id}"]`);
            if (!label) return; // Should not happen

            const optionValue = radio.value;

            // Check if this option is correct
            const isThisOptionCorrect = isMultiCorrect ? correctAnswer.includes(optionValue) : optionValue === correctAnswer;

            // Check if this option was selected by the user
            const isThisOptionSelected = optionValue === selectedAnswer;


            if (isThisOptionSelected) {
                // Style the selected option based on correctness
                if (isMultiCorrect ? correctAnswer.includes(selectedAnswer) : selectedAnswer === correctAnswer) {
                    label.classList.add('correct');
                } else {
                    label.classList.add('incorrect');
                }
            } else {
                // Reveal the correct answer(s) if not selected by the user
                if (isThisOptionCorrect) {
                    label.classList.add('correct'); // Mark correct answer even if not selected
                }
            }
            // Disable radio button after submission
             radio.disabled = true;
        });
    }


     function displayToolExplanation(explanation) {
        toolExplanationDiv.innerHTML = `<h3>על הכלי:</h3><p>${explanation}</p>`;
        toolExplanationDiv.style.display = 'block'; // Set display to block before adding visible class
        // Use a timeout to allow display change to register before transition
        setTimeout(() => {
             toolExplanationDiv.classList.add('visible');
        }, 50);
    }

    function nextTool() {
        currentToolIndex++;
        loadTool(currentToolIndex);
    }

    function endGame() {
        questionAreaDiv.style.display = 'none';
        toolImage.style.display = 'none'; // Hide image on game over
        submitButton.style.display = 'none';
        nextToolButton.style.display = 'none';
        feedbackDiv.classList.remove('visible'); // Fade out feedback
        feedbackDiv.textContent = ''; // Clear feedback text
        toolExplanationDiv.classList.remove('visible'); // Fade out explanation
        toolExplanationDiv.style.display = 'none';
        scoreDisplay.style.display = 'none'; // Hide score display
        toolCounter.style.display = 'none'; // Hide counter

        finalScoreSpan.textContent = score;
        gameOverDiv.style.display = 'block'; // Show game over screen
    }

    function startGame() {
        currentToolIndex = 0;
        score = 0;
        shuffledTools = shuffleArray(tools); // Shuffle the original tools array

        scoreDisplay.textContent = `ניקוד: ${score}`;
        scoreDisplay.style.display = 'block'; // Show score display
        toolCounter.style.display = 'block'; // Show counter
        toolImage.style.display = 'block'; // Show image
        feedbackDiv.style.display = 'block'; // Show feedback div
        gameOverDiv.style.display = 'none'; // Hide game over screen

        loadTool(currentToolIndex);
    }

    // Event Listeners
    submitButton.addEventListener('click', checkAnswer);
    nextToolButton.addEventListener('click', nextTool);
    restartButton.addEventListener('click', startGame);
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = fullExplanationDiv.classList.contains('visible');
        if (isHidden) {
             fullExplanationDiv.classList.remove('visible');
             fullExplanationDiv.style.display = 'none'; // Hide after transition
             toggleExplanationButton.textContent = 'הצג הסבר מורחב על התפתחות החקלאות';
        } else {
            fullExplanationDiv.style.display = 'block'; // Show before adding visible class
            setTimeout(() => { // Allow display change to register
                fullExplanationDiv.classList.add('visible');
            }, 50);
             toggleExplanationButton.textContent = 'הסתר הסבר מורחב על התפתחות החקלאות';
        }
    });

    // Initial setup
    // Make sure the full explanation starts hidden and ready for animation
    fullExplanationDiv.style.display = 'none';

    // Start the game on page load
    startGame();

</script>