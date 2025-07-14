---
title: "מפענחים את סודות האקלים: הדמיית קלימוגרפים"
english_slug: deciphering-climate-secrets-climatograph-game
category: "מדעי הסביבה / גאוגרפיה"
tags: [אקלים, קלימוגרף, גאוגרפיה פיזית, טמפרטורה, משקעים]
---
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>מפענחים את סודות האקלים: הדמיית קלימוגרפים</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <!-- Optionally add Chartjs annotations plugin for highlighting - requires adding script tag here -->
    <!-- <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-annotation@1.0.2"></script> -->
</head>
<body>

    <header>
        <h1>מסע פענוח קלימוגרפים: להיות בלשי אקלים!</h1>
        <p>הצטרפ/י למסע מרתק שבו תפענח/י את סודות האקלים של מקומות שונים בעולם! קלימוגרף הוא כמו "תעודת הזהות" האקלימית של כל מקום – הוא מגלה לנו בגרף אחד את הטמפרטורות והמשקעים לאורך כל השנה. האם תצליח/י לקרוא את המפה הזו ולגלות מה מסתתר מאחורי הקווים והעמודות?</p>
    </header>

    <div id="app-container">
        <div id="climatograph-area">
            <h2>קלימוגרף: <span id="location-name"></span></h2>
            <div class="chart-canvas-container">
                 <canvas id="climatograph-chart"></canvas>
            </div>

        </div>

        <div id="questions-area">
            <h3>משימת פענוח:</h3>
            <div id="progress"></div>
            <div id="question-box">
                <div id="question-text"></div>
                <input type="text" id="user-answer" placeholder="הכנס/י תשובתך כאן...">
                <button id="submit-answer">בדיקה</button>
                <div id="feedback"></div>
                <button id="next-question" class="nav-button" style="display: none;">שאלה הבאה &rarr;</button>
                <button id="next-location" class="nav-button" style="display: none;">עיר/אזור הבא &rarr;</button>
            </div>
        </div>
    </div>

    <button id="toggle-explanation" class="toggle-button">הסבר: איך לקרוא קלימוגרף?</button>

    <div id="explanation" style="display: none;">
        <h2>הסבר: מפענחים קלימוגרפים</h2>
        <p>ברוכים הבאים לעולם המרתק של הקלימוגרפים! הכלי החזותי הזה הוא מפתח להבנת דפוסי האקלים על פני כדור הארץ.</p>

        <h3>אז מה זה בעצם קלימוגרף?</h3>
        <p>קלימוגרף הוא גרף ייחודי המציג בו זמנית שני נתוני אקלים מרכזיים לאורך חודשי השנה: הטמפרטורה הממוצעת וכמות המשקעים הממוצעת (גשם, שלג וכו'). הוא מאפשר לנו לזהות במהירות את "טביעת האצבע" האקלימית של כל מקום, לראות מתי חם או קר, ומתי יבש או גשום.</p>

        <h3>מבנה הקלימוגרף: פשוט ויעיל!</h3>
        <p>הקלימוגרף מורכב משלושה חלקים עיקריים:</p>
        <ul>
            <li>**ציר ה-X (האופקי למטה):** מייצג תמיד את חודשי השנה, מינואר ועד דצמבר (או כפי שהם מוצגים בהדמיה). הוא מאפשר לנו לראות את השינויים העונתיים.</li>
            <li>**ציר ה-Y השמאלי (האנכי משמאל):** שייך לנתוני ה**טמפרטורה**. הטמפרטורה מוצגת בדרך כלל כ**קו** (לרוב בצבע חם כמו אדום). כל נקודה על הקו מראה את הטמפרטורה הממוצעת לאותו חודש. שימו לב לקנה המידה בציר זה (מעלות צלזיוס).</li>
            <li>**ציר ה-Y הימני (האנכי מימין):** שייך לנתוני ה**משקעים**. כמות המשקעים מוצגת בדרך כלל כ**עמודות** (לרוב בצבע קר כמו כחול). גובה כל עמודה מראה את כמות המשקעים הממוצעת לאותו חודש. שימו לב לקנה המידה בציר זה (מילימטרים).</li>
        </ul>
        <p>הפער בין קנה המידה של הטמפרטורה והמשקעים משמעותי! הוא מאפשר להציג את שני סוגי הנתונים בגרף אחד, גם אם ערכיהם המספריים שונים מאוד (לדוגמה, 20°C לעומת 100 מ"מ).</p>

        <h3>איך "קוראים" את הסיפור שמספר הקלימוגרף?</h3>
        <p>התבוננות בקלימוגרף מגלה לנו מידע רב:</p>
        <ul>
            <li>**עונתיות הטמפרטורה:** האם קו הטמפרטורה עולה ויורד באופן משמעותי? מתי הוא בשיא (החודש החם ביותר) ומתי בשפל (החודש הקר ביותר)? מהו הטווח (ההפרש) בין החודש החם לקר? טווח גדול מצביע לרוב על אקלים יבשתי, טווח קטן על אקלים ימי או טרופי.</li>
            <li>**עונתיות המשקעים:** האם עמודות המשקעים גבוהות באחידות או שונות מאוד זו מזו? מתי הן בשיא (החודש הגשום ביותר) ומתי בשפל (החודש היבש ביותר)? האם יש עונה יבשה או גשומה מובהקת?</li>
            <li>**הקשר בין טמפרטורה למשקעים:** האם העונה החמה היא גם הגשומה (כמו באקלים טרופי עם גשמי קיץ)? או שאולי העונה החמה יבשה והקרה גשומה (כמו באקלים ים-תיכוני)? הקשר הזה קריטי לזיהוי סוג האקלים!</li>
        </ul>

        <h3>זיהוי סוגי אקלים נפוצים:</h3>
        <p>כל סוג אקלים "מצייר" קלימוגרף בעל דפוס אופייני:</p>
        <ul>
            <li>**אקלים ים-תיכוני:** קו טמפרטורה בצורת קשת (קיץ חם, חורף קריר), ועמודות משקעים נמוכות מאוד בקיץ וגבוהות בחורף. כמו בישראל!</li>
            <li>**אקלים מדברי:** מעט מאוד עמודות משקעים (לרוב כמעט אפס) לאורך כל השנה. קו טמפרטורה עם טווח שנתי גדול (קיץ חם מאוד, חורף קריר).</li>
            <li>**אקלים טרופי:** קו טמפרטורה יציב וגבוה יחסית לאורך כל השנה. עמודות משקעים גבוהות, לעיתים עם עונה גשומה מובחנת או גשם כמעט יומיומי.</li>
            <li>**אקלים ממוזג:** קו טמפרטורה עם עונתיות ברורה וטווח שנתי בינוני. עמודות משקעים המתפרסות יחסית באחידות על פני כל השנה, או עם שיא בעונה מסוימת (אך לרוב אין עונה יבשה מובהקת).</li>
        </ul>
        <p>ככל שתתנסה/י בפענוח קלימוגרפים נוספים, כך תשתפר יכולתך לזהות סוגי אקלים שונים ולהבין את הסיפור האקלימי של כל מקום בעולם!</p>
    </div>


    <style>
        /* Reset and Basic Styles */
        * {
            box-sizing: border-box;
        }

        body {
            font-family: 'Arial', sans-serif; /* Using a common, readable font */
            line-height: 1.7; /* Improved readability */
            margin: 0;
            padding: 20px;
            direction: rtl;
            text-align: right;
            background: linear-gradient(to bottom, #e0f7fa, #b2ebf2); /* Subtle background gradient */
            color: #333;
        }

        header {
            text-align: center;
            margin-bottom: 40px;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }

        h1 {
            color: #00796b; /* Teal color */
            margin-top: 0;
            font-size: 2em;
        }

        h2, h3 {
            color: #004d40; /* Darker teal */
            margin-top: 20px;
        }

        p {
            margin-bottom: 15px;
            color: #555;
        }

        #app-container {
            display: flex;
            flex-direction: column;
            gap: 30px; /* Increased gap */
            margin-top: 30px;
            padding: 30px; /* Increased padding */
            background-color: #ffffff;
            border-radius: 12px; /* More rounded corners */
            box-shadow: 0 6px 12px rgba(0,0,0,0.15); /* Stronger shadow */
        }

        #climatograph-area {
             flex: 2;
             min-width: 300px;
        }

        #climatograph-area h2 {
             text-align: center; /* Center climatograph title */
             margin-bottom: 15px;
             font-size: 1.5em;
             color: #00796b;
        }

        .chart-canvas-container {
            position: relative;
            height: 400px; /* Fixed height for chart */
            width: 100%;
        }

        #questions-area {
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 20px; /* Increased gap */
            background-color: #e0f2f7; /* Light blue background */
            padding: 25px; /* Increased padding */
            border-radius: 10px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            min-width: 280px; /* Ensure minimum width */
        }

        #questions-area h3 {
            margin-top: 0;
            font-size: 1.4em;
            color: #004d40;
            text-align: center;
        }

        #progress {
            text-align: center;
            font-size: 1em;
            color: #004d40;
            margin-bottom: 15px;
        }

        #question-box {
             display: flex;
             flex-direction: column;
             gap: 15px;
        }

        #question-text {
            font-size: 1.2em; /* Larger font size */
            margin-bottom: 10px;
            font-weight: bold;
            color: #333;
            text-align: center;
        }

        #user-answer {
            padding: 12px; /* Increased padding */
            border: 1px solid #b2ebf2; /* Light blue border */
            border-radius: 6px; /* More rounded */
            font-size: 1.1em; /* Larger font size */
            width: 100%; /* Full width */
            transition: border-color 0.3s ease, box-shadow 0.3s ease;
        }

        #user-answer:focus {
            outline: none;
            border-color: #00796b; /* Teal focus border */
            box-shadow: 0 0 5px rgba(0, 121, 107, 0.3);
        }

        button {
            padding: 12px 20px; /* Increased padding */
            background: linear-gradient(to right, #00796b, #004d40); /* Gradient button */
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 1.1em;
            transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
            width: 100%; /* Full width for buttons */
            text-align: center;
        }

        button:hover {
            background: linear-gradient(to right, #004d40, #00362c); /* Darker gradient on hover */
            box-shadow: 0 4px 8px rgba(0,0,0,0.25);
        }

        button:active {
            transform: scale(0.98); /* Press effect */
        }

         button:disabled {
            background: #cccccc;
            cursor: not-allowed;
            box-shadow: none;
         }

        .nav-button {
            background: linear-gradient(to right, #4dd0e1, #00bcd4); /* Lighter gradient for nav */
            margin-top: 10px;
        }

        .nav-button:hover {
            background: linear-gradient(to right, #00bcd4, #00acc1);
        }


        #feedback {
            margin-top: 10px;
            padding: 15px; /* Increased padding */
            border-radius: 6px;
            min-height: 1.5em;
            text-align: center;
            font-weight: bold;
            transition: background-color 0.3s ease, color 0.3s ease;
            opacity: 0; /* Start hidden for animation */
            transform: translateY(10px); /* Start slightly offset */
            animation: feedback-fade-in 0.5s forwards; /* Apply animation */
        }

        @keyframes feedback-fade-in {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }


        .feedback-correct {
            background-color: #c8e6c9; /* Light green */
            color: #1b5e20; /* Dark green */
            border: 1px solid #a5d6a7;
        }

        .feedback-incorrect {
            background-color: #ffcdd2; /* Light red */
            color: #c62828; /* Dark red */
            border: 1px solid #ef9a9a;
        }

        .toggle-button {
             display: block;
             margin: 40px auto; /* Center and increase margin */
             padding: 14px 25px; /* More padding */
             background-color: #78909c; /* Blue-grey */
             color: white;
             border: none;
             border-radius: 8px; /* More rounded */
             cursor: pointer;
             font-size: 1.1em;
             transition: background-color 0.3s ease, box-shadow 0.3s ease;
             box-shadow: 0 2px 4px rgba(0,0,0,0.15);
             width: auto; /* Allow button to size based on content */
             min-width: 200px;
        }

        .toggle-button:hover {
             background-color: #546e7a; /* Darker blue-grey */
             box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }


        #explanation {
            margin-top: 20px;
            padding: 30px; /* Increased padding */
            border: 1px solid #b2ebf2;
            border-radius: 10px;
            background-color: #e0f2f7; /* Light blue background */
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            /* Animation for toggle */
            opacity: 0;
            max-height: 0;
            overflow: hidden;
            transition: opacity 0.5s ease-in-out, max-height 0.5s ease-in-out;
        }

        #explanation.visible {
            opacity: 1;
            max-height: 2000px; /* Sufficiently large value */
        }

        #explanation h2, #explanation h3 {
            color: #004d40;
            text-align: right; /* Align explanation headers right */
        }

        #explanation ul {
            list-style-type: disc;
            margin-right: 30px; /* Adjust for RTL */
            padding-right: 0;
            margin-bottom: 20px;
        }

        #explanation li {
            margin-bottom: 10px;
        }

         #explanation strong {
             color: #00796b; /* Highlight keywords */
         }


        /* Responsive design */
        @media (min-width: 768px) {
            #app-container {
                flex-direction: row;
            }
             #climatograph-area {
                 flex: 2;
             }
             #questions-area {
                 flex: 1;
             }
             button, #user-answer {
                width: auto; /* Allow buttons/input to size based on content/flex */
             }
             #question-box {
                align-items: center; /* Center items in the column */
             }
        }

        @media (min-width: 1024px) {
             #app-container {
                gap: 50px;
             }
             #climatograph-area {
                 flex: 3; /* Give chart more space on large screens */
             }
             #questions-area {
                 flex: 1;
                 min-width: 350px; /* Slightly wider questions area */
             }
        }

        /* Chart.js Specific Styling Overrides */
        /* This is handled directly in the JS config for chart appearance */

    </style>

    <script>
        // Data for different locations
        const locations = [
            {
                name: "תל אביב, ישראל",
                months: ["ינו", "פבר", "מרץ", "אפר", "מאי", "יונ", "יול", "אוג", "ספט", "אוק", "נוב", "דצמ"],
                temperature: [13.5, 13.9, 15.8, 18.2, 21.3, 24.6, 27.0, 27.5, 26.5, 23.7, 19.1, 15.2], // Avg monthly temp in C
                precipitation: [147, 112, 62, 16, 2, 0, 0, 0, 0.7, 34, 81, 127], // Avg monthly precip in mm
                questions: [
                    {
                        text: "מהי כמות המשקעים הממוצעת בחודש ינואר (במ״מ)?",
                        answer: 147,
                        type: 'number',
                         hint: 'התבונן/י בעמודה הכחולה מעל ינואר וקרא/י את הערך בציר הימני (משקעים).'
                    },
                    {
                        text: "מהי הטמפרטורה הממוצעת בחודש יולי (במעלות צלזיוס)?",
                        answer: 27.0,
                        type: 'number',
                        tolerance: 0.5, // Slightly increased tolerance for temperature readings
                         hint: 'התבונן/י בנקודה האדומה מעל יולי וקרא/י את הערך בציר השמאלי (טמפרטורה).'
                    },
                     {
                        text: "באיזה חודש כמות המשקעים היא הנמוכה ביותר?",
                        answer: "יונ",
                        type: 'month_name',
                         hint: 'חפש/י את העמודה הכחולה הנמוכה ביותר. באיזה חודש היא נמצאת?'
                    },
                     {
                        text: "באיזה חודש הטמפרטורה הממוצעת היא הגבוהה ביותר?",
                        answer: "אוג",
                        type: 'month_name',
                         hint: 'חפש/י את הנקודה האדומה הגבוהה ביותר על הקו. באיזה חודש היא נמצאת?'
                    },
                     {
                        text: "מהו טווח הטמפרטורות השנתי הממוצע (הפרש בין החודש החם ביותר לקר ביותר, במעלות צלזיוס)?",
                        answer: 27.5 - 13.5, // Calculation
                        type: 'calculation',
                        tolerance: 1.0, // Increased tolerance for calculation
                        hint: 'מצא/י את החודש עם הטמפרטורה הכי גבוהה ואת החודש עם הטמפרטורה הכי נמוכה. חשב/י את ההפרש ביניהן.'
                    },
                     {
                        text: "בהתבסס על הקלימוגרף, באיזו עונה (קיץ/חורף) יורדים עיקר המשקעים בתל אביב?",
                        answer: "חורף",
                        type: 'season',
                         hint: 'האם העמודות הכחולות גבוהות יותר בחודשי הקיץ (יוני-אוגוסט) או בחודשי החורף (דצמבר-פברואר)?'
                    }
                ]
            },
             {
                name: "אסואן, מצרים", // Desert Climate Example
                months: ["ינו", "פבר", "מרץ", "אפר", "מאי", "יונ", "יול", "אוג", "ספט", "אוק", "נוב", "דצמ"],
                temperature: [16.6, 18.7, 23.0, 27.9, 32.9, 35.1, 35.4, 35.5, 32.7, 28.0, 22.7, 18.1], // Avg monthly temp in C
                precipitation: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], // Avg monthly precip in mm
                 questions: [
                    {
                        text: "מהי כמות המשקעים הממוצעת בחודש אפריל (במ״מ)?",
                        answer: 0,
                        type: 'number',
                         hint: 'התבונן/י בעמודה הכחולה מעל אפריל.'
                    },
                     {
                        text: "מהי הטמפרטורה הממוצעת בחודש יוני (במעלות צלזיוס)?",
                        answer: 35.1,
                        type: 'number',
                         tolerance: 0.5,
                         hint: 'התבונן/י בנקודה האדומה מעל יוני.'
                    },
                     {
                        text: "באיזה חודש כמות המשקעים היא הגבוהה ביותר באסואן?",
                        answer: "אין משקעים", // Specific phrasing
                        type: 'text_strict',
                         hint: 'התבונן/י בעמודות המשקעים. מה קורה בחודש עם העמודה הגבוהה ביותר?'
                    },
                     {
                        text: "מהו טווח הטמפרטורות השנתי הממוצע (הפרש בין החודש החם ביותר לקר ביותר, במעלות צלזיוס)?",
                         answer: 35.5 - 16.6, // Calculation
                        type: 'calculation',
                         tolerance: 1.5, // Increased tolerance for larger range calculation
                         hint: 'מצא/י את הטמפרטורה הכי גבוהה והכי נמוכה, וחשב/י את ההפרש.'
                    },
                     {
                        text: "בהתבסס על הקלימוגרף, איזה סוג אקלים אופייני לאסואן? (מדברי/ים תיכוני/ממוזג)",
                        answer: "מדברי",
                        type: 'climate_type',
                         hint: 'האם יש עמודות גשם משמעותיות? מה בנוגע לטווח הטמפרטורות?'
                    }
                 ]
            },
            {
                name: "לונדון, בריטניה", // Temperate Climate Example
                months: ["ינו", "פבר", "מרץ", "אפר", "מאי", "יונ", "יול", "אוג", "ספט", "אוק", "נוב", "דצמ"],
                temperature: [5.4, 5.7, 7.9, 10.5, 13.5, 16.4, 18.7, 18.4, 15.6, 12.2, 8.4, 5.9], // Avg monthly temp in C
                precipitation: [56, 41, 40, 45, 45, 48, 43, 50, 49, 60, 57, 55], // Avg monthly precip in mm
                 questions: [
                    {
                        text: "מהי הטמפרטורה הממוצעת בחודש ינואר (במעלות צלזיוס)?",
                        answer: 5.4,
                        type: 'number',
                         tolerance: 0.5,
                         hint: 'התבונן/י בנקודה האדומה מעל ינואר.'
                    },
                     {
                        text: "מהי כמות המשקעים הממוצעת בחודש אוקטובר (במ״מ)?",
                        answer: 60,
                        type: 'number',
                        hint: 'התבונן/י בעמודה הכחולה מעל אוקטובר.'
                    },
                     {
                        text: "באיזה חודש הטמפרטורה הממוצעת היא הנמוכה ביותר בלונדון?",
                        answer: "ינו",
                        type: 'month_name',
                         hint: 'חפש/י את הנקודה האדומה הנמוכה ביותר.'
                    },
                     {
                        text: "האם יש בלונדון עונה יבשה מובהקת (לדוגמה, חודשים רבים עם פחות מ-10 מ״מ גשם)? (כן/לא)",
                        answer: "לא",
                        type: 'yes_no',
                         hint: 'האם ישנם חודשים עם עמודות כחולות נמוכות מאוד, כמו באסואן או בתל אביב בקיץ?'
                    },
                      {
                        text: "האם עיקר המשקעים יורד בעונה מסוימת או מתפרס על פני השנה?",
                        answer: "מתפרס על פני השנה",
                        type: 'text_strict',
                         hint: 'האם העמודות הכחולות גבוהות משמעותית בעונה אחת לעומת אחרת, או שהן די דומות בגובהן רוב השנה?'
                    }
                 ]
            }
             // Add more locations here following the same structure
        ];

        let currentlocationIndex = 0;
        let currentQuestionIndex = 0;
        let chart; // To hold the Chart.js instance

        const locationNameElement = document.getElementById('location-name');
        const questionTextElement = document.getElementById('question-text');
        const userAnswerInput = document.getElementById('user-answer');
        const submitAnswerButton = document.getElementById('submit-answer');
        const feedbackElement = document.getElementById('feedback');
        const nextQuestionButton = document.getElementById('next-question');
        const nextlocationButton = document.getElementById('next-location');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationElement = document.getElementById('explanation');
        const progressElement = document.getElementById('progress');
        const questionBoxElement = document.getElementById('question-box'); // Needed for animations

        // Helper to normalize text answers (case, spaces, punctuation)
        const normalizeText = (text) => {
            if (typeof text !== 'string') return text;
            return text.toLowerCase().trim().replace(/[.,!?'"״]/g, '').replace(/\s+/g, ' ');
        };

         // Function to update progress display
         function updateProgress() {
             const location = locations[currentlocationIndex];
             const totalQuestions = location.questions.length;
             progressElement.textContent = `שאלה ${currentQuestionIndex + 1} מתוך ${totalQuestions}`;
             if (currentQuestionIndex >= totalQuestions) {
                  progressElement.textContent = `כל השאלות עבור ${location.name} הושלמו!`;
             }
         }

        // Function to load and display the climatograph for the current location
        function loadClimatograph() {
            const location = locations[currentlocationIndex];
            locationNameElement.textContent = location.name;

            if (chart) {
                chart.destroy(); // Destroy previous chart instance
            }

            const ctx = document.getElementById('climatograph-chart').getContext('2d');
            chart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: location.months,
                    datasets: [
                        {
                            label: 'משקעים (מ״מ)',
                            data: location.precipitation,
                            backgroundColor: 'rgba(0, 188, 212, 0.8)', // Cyan - more vibrant blue
                            borderColor: 'rgba(0, 151, 167, 1)', // Darker Cyan
                            borderWidth: 1,
                            yAxisID: 'precipitation',
                            order: 2,
                             barPercentage: 0.8, // Make bars slightly thinner
                             categoryPercentage: 0.8
                        },
                        {
                            label: 'טמפרטורה (מ״צ)',
                            data: location.temperature,
                            backgroundColor: 'rgba(255, 82, 82, 0.8)', // Reddish-Orange
                            borderColor: 'rgba(211, 47, 47, 1)', // Darker Red
                            borderWidth: 3, // Thicker line
                            type: 'line',
                            fill: false,
                            yAxisID: 'temperature',
                             order: 1,
                             tension: 0.2, // Add slight curve to line
                             pointBackgroundColor: 'rgba(255, 82, 82, 1)',
                             pointBorderColor: '#fff',
                             pointBorderWidth: 2,
                             pointRadius: 5,
                             pointHoverRadius: 7
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'top',
                            rtl: true,
                            labels: {
                                usePointStyle: true,
                                padding: 20,
                                font: {
                                     size: 15,
                                     weight: 'bold'
                                },
                                color: '#333'
                            }
                        },
                         tooltip: {
                             rtl: true,
                             backgroundColor: 'rgba(0,0,0,0.7)',
                             bodyColor: '#fff',
                             titleColor: '#fff',
                             borderColor: '#fff',
                             borderWidth: 1,
                             callbacks: {
                                  label: function(context) {
                                      let label = context.dataset.label || '';
                                      if (label) {
                                          label += ': ';
                                      }
                                      if (context.parsed.y !== null) {
                                          // Format numbers nicely for Hebrew locale
                                          label += new Intl.NumberFormat('he-IL', { maximumFractionDigits: 1 }).format(context.parsed.y);
                                          if (context.dataset.label.includes('טמפרטורה')) {
                                              label += ' °C';
                                          } else if (context.dataset.label.includes('משקעים')) {
                                              label += ' מ״מ';
                                          }
                                      }
                                      return label;
                                  }
                             },
                             titleFont: { size: 14, weight: 'bold' },
                             bodyFont: { size: 13 }
                         }
                    },
                    scales: {
                         x: {
                            title: {
                                display: true,
                                text: 'חודש',
                                font: { size: 15, weight: 'bold' },
                                color: '#555'
                            },
                            grid: {
                                drawOnChartArea: false
                            },
                             ticks: {
                                 font: { size: 12 },
                                 color: '#666'
                             }
                         },
                        temperature: {
                            type: 'linear',
                            position: 'left',
                            title: {
                                display: true,
                                text: 'טמפרטורה (°C)',
                                font: { size: 15, weight: 'bold' },
                                color: 'rgba(211, 47, 47, 1)' // Match line color
                            },
                             grid: {
                                borderDash: [3, 3],
                                color: '#e0e0e0'
                             },
                             ticks: {
                                beginAtZero: false,
                                callback: function(value) { return value + '°C'; },
                                font: { size: 12 },
                                color: '#666'
                             }
                        },
                        precipitation: {
                            type: 'linear',
                            position: 'right',
                            title: {
                                display: true,
                                text: 'משקעים (מ״מ)',
                                font: { size: 15, weight: 'bold' },
                                color: 'rgba(0, 151, 167, 1)' // Match bar color
                            },
                            grid: {
                                drawOnChartArea: false,
                                color: '#e0e0e0'
                            },
                            ticks: {
                                beginAtZero: true,
                                callback: function(value) { return value + ' מ״מ'; },
                                font: { size: 12 },
                                color: '#666'
                            }
                        }
                    },
                     rtl: true // Enable RTL for the whole chart
                }
            });

            displayQuestion();
        }

        // Function to display the current question
        function displayQuestion() {
            const location = locations[currentlocationIndex];
            updateProgress();
            if (currentQuestionIndex < location.questions.length) {
                const question = location.questions[currentQuestionIndex];
                questionTextElement.textContent = question.text;
                userAnswerInput.value = ''; // Clear previous answer
                feedbackElement.textContent = ''; // Clear feedback
                feedbackElement.className = ''; // Remove feedback classes
                 // Reset feedback opacity and position for animation
                 feedbackElement.style.opacity = 0;
                 feedbackElement.style.transform = 'translateY(10px)';

                submitAnswerButton.style.display = 'block'; // Show submit button
                nextQuestionButton.style.display = 'none'; // Hide next button
                nextlocationButton.style.display = 'none'; // Hide next location button
                userAnswerInput.style.display = 'block'; // Show input field
                userAnswerInput.disabled = false; // Enable input
                 userAnswerInput.focus(); // Focus input for easy typing

                 // Reset chart highlighting (if any) - requires annotations plugin or direct dataset manipulation
                 // For now, we rely on Chart.js redraw on load. Future improvement: highlight specific elements.

            } else {
                // No more questions for this location
                questionTextElement.textContent = `משימת הפענוח עבור ${location.name} הושלמה בהצלחה!`;
                progressElement.textContent = `כל הכבוד! ענית על כל השאלות עבור ${location.name}.`;
                userAnswerInput.style.display = 'none'; // Hide input
                submitAnswerButton.style.display = 'none'; // Hide submit button
                feedbackElement.textContent = '';
                feedbackElement.className = '';
                nextQuestionButton.style.display = 'none';

                 // Show next location button if there are more locations
                if (currentlocationIndex < locations.length - 1) {
                     nextlocationButton.style.display = 'block';
                } else {
                     // All locations completed
                     questionTextElement.textContent = "סיימת את כל משימות הפענוח! כל הכבוד על העבודה הבלשית!";
                     progressElement.textContent = ""; // Clear progress text
                     nextlocationButton.style.display = 'none';
                     // Optionally add a restart button here
                }
            }
        }

        // Function to check the user's answer
        function checkAnswer() {
            const location = locations[currentlocationIndex];
            const question = location.questions[currentQuestionIndex];
            const userAnswer = userAnswerInput.value.trim();
            let isCorrect = false;
            let feedbackText = "";

            // Check if input is empty
            if (userAnswer === "") {
                 feedbackElement.textContent = "אנא הכנס/י תשובה.";
                 feedbackElement.className = 'feedback-incorrect';
                 feedbackElement.style.opacity = 1; // Show feedback immediately
                 feedbackElement.style.transform = 'translateY(0)';
                 return; // Stop check function if empty
            }


            switch (question.type) {
                 case 'number':
                 case 'calculation':
                     const numericAnswer = parseFloat(userAnswer);
                     const correctAnswer = parseFloat(question.answer);
                     const tolerance = question.tolerance || 0;
                     if (!isNaN(numericAnswer)) {
                         isCorrect = Math.abs(numericAnswer - correctAnswer) <= tolerance;
                     }
                    const correctAnswerFormatted = new Intl.NumberFormat('he-IL', { maximumFractionDigits: question.tolerance !== undefined ? 1 : 0 }).format(correctAnswer);
                     feedbackText = isCorrect ? "מעולה! תשובה נכונה." : `המממ... נסה/י שוב. התשובה הנכונה היא בערך ${correctAnswerFormatted}.`;
                     break;
                 case 'month_name':
                    // Compare normalized input with normalized month name or index (1-12)
                     const monthNames = location.months;
                     const normalizedInput = normalizeText(userAnswer);
                     // Ensure correctMonthName is derived from the intended answer, regardless of its type
                     const correctMonthName = typeof question.answer === 'number' ? monthNames[question.answer - 1] : question.answer; // Adjust for 0-based index
                     const normalizedCorrect = normalizeText(correctMonthName);

                     // Allow checking against the index number (1-12) as text
                     const monthIndexInput = parseInt(userAnswer, 10);
                     // Correct 0-based index from answer which might be a month name string or 1-based number
                     const correctMonthIndex = typeof question.answer === 'number' ? question.answer - 1 : monthNames.indexOf(question.answer);


                     if (!isNaN(monthIndexInput) && monthIndexInput >= 1 && monthIndexInput <= 12) {
                         isCorrect = monthIndexInput - 1 === correctMonthIndex;
                     } else {
                         isCorrect = normalizedInput === normalizedCorrect;
                     }

                    feedbackText = isCorrect ? "נכון!" : `קרוב/ה, אבל לא מדויק. שם החודש הנכון הוא "${correctMonthName}".`;
                    break;
                 case 'season':
                 case 'climate_type':
                 case 'yes_no':
                    const normalizedAnswer = normalizeText(userAnswer);
                    const normalizedExpected = normalizeText(question.answer);
                    isCorrect = normalizedAnswer === normalizedExpected;
                    // Extract options from question text for feedback
                    const optionsMatch = question.text.match(/\((.*?)\)/);
                    const options = optionsMatch ? optionsMatch[1].split('/').map(opt => opt.trim()).join(' או ') : '';
                    feedbackText = isCorrect ? "נכון מאוד!" : `המממ... נסה/י שוב.${options ? ` האפשרויות הן: ${options}.` : ''}`;
                     break;
                 case 'text_strict': // For specific phrasing answers
                     isCorrect = normalizeText(userAnswer) === normalizeText(question.answer); // Use normalization even for strict text
                     feedbackText = isCorrect ? "מדויק!" : `כמעט, אבל עליך לנסח את התשובה באופן מדויק יותר. התשובה הנכונה היא: "${question.answer.trim()}"`;
                     break;
                 default: // Default to simple text comparison
                     isCorrect = normalizeText(userAnswer) === normalizeText(question.answer);
                      feedbackText = isCorrect ? "נכון." : `נסה/י שוב. התשובה הנכונה היא: "${question.answer.trim()}"`;
            }


            if (isCorrect) {
                feedbackElement.textContent = feedbackText;
                feedbackElement.className = 'feedback-correct';
                submitAnswerButton.style.display = 'none'; // Hide submit button
                nextQuestionButton.style.display = 'block'; // Show next button
                userAnswerInput.disabled = true; // Disable input after correct answer
                // Trigger feedback animation
                feedbackElement.style.opacity = 0; // Reset for animation
                feedbackElement.style.transform = 'translateY(10px)'; // Reset for animation
                void feedbackElement.offsetWidth; // Trigger reflow
                feedbackElement.style.opacity = 1;
                feedbackElement.style.transform = 'translateY(0)';

            } else {
                feedbackElement.textContent = feedbackText;
                feedbackElement.className = 'feedback-incorrect';
                userAnswerInput.disabled = false; // Ensure input is enabled
                 // Trigger feedback animation
                 feedbackElement.style.opacity = 0; // Reset for animation
                 feedbackElement.style.transform = 'translateY(10px)'; // Reset for animation
                 void feedbackElement.offsetWidth; // Trigger reflow
                 feedbackElement.style.opacity = 1;
                 feedbackElement.style.transform = 'translateY(0)';

                 // Optionally provide a hint after a few incorrect attempts
                 // This would require tracking attempts, adding complexity. Keep it simple for now.
            }
        }

        // Function to move to the next question
        function nextQuestion() {
            currentQuestionIndex++;
            displayQuestion();
        }

        // Function to move to the next location
        function nextLocation() {
             currentlocationIndex++;
             currentQuestionIndex = 0; // Reset questions for the new location
             userAnswerInput.style.display = 'block'; // Show input again
             nextlocationButton.style.display = 'none'; // Hide next location button immediately
             loadClimatograph();
        }

        // Function to toggle explanation visibility
        function toggleExplanation() {
            const isHidden = explanationElement.style.display === 'none';
             if (isHidden) {
                 explanationElement.style.display = 'block';
                 // Use requestAnimationFrame to ensure display change is processed before animation
                 requestAnimationFrame(() => {
                    explanationElement.classList.add('visible');
                 });
                 toggleExplanationButton.textContent = 'הסתר הסבר על קלימוגרפים';
             } else {
                 explanationElement.classList.remove('visible');
                  // Wait for animation to finish before hiding completely
                 explanationElement.addEventListener('transitionend', function handler() {
                     explanationElement.style.display = 'none';
                      explanationElement.removeEventListener('transitionend', handler);
                 });
                 toggleExplanationButton.textContent = 'הצג הסבר על קלימוגרפים';
             }
        }


        // Event listeners
        submitAnswerButton.addEventListener('click', checkAnswer);
        nextQuestionButton.addEventListener('click', nextQuestion);
        nextlocationButton.addEventListener('click', nextLocation);
        toggleExplanationButton.addEventListener('click', toggleExplanation);

        // Allow pressing Enter to submit answer
        userAnswerInput.addEventListener('keypress', function(event) {
            if (event.key === 'Enter') {
                event.preventDefault(); // Prevent form submission
                if (submitAnswerButton.style.display !== 'none' && !userAnswerInput.disabled) {
                    checkAnswer();
                }
            }
        });


        // Initialize the application
        loadClimatograph();

    </script>
</body>
</html>
---
```