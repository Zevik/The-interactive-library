---
title: "קסם הצלילים: מסע בעקבות הכוונון המוזיקלי"
english_slug: why-does-music-sound-good-from-pythagorean-to-equal-temperament
category: "אמנות ועיצוב / מוזיקה"
tags: מוזיקה, תיאוריה, כוונון, טמפרמנט מושווה, פיתגורס, אקוסטיקה, סאונד
---
# קסם הצלילים: מסע בעקבות הכוונון המוזיקלי

האם עצרתם פעם לתהות מה גורם לשילובים מסוימים של צלילים להישמע... פשוט נכון? בעוד שאחרים צורמים ולא נעימים? מסתבר שהסוד טמון לא רק באמנות, אלא גם במתמטיקה ובפיזיקה של הגלים. במשך מאות שנים, מוזיקאים, מתמטיקאים ופילוסופים חיפשו את הדרך ה'מושלמת' לכוון כלי נגינה, מסע שהוביל לפשרות מרתקות ויצירת עולמות הרמוניים חדשים.

<div id="app">
    <h2>האזינו וגלו: איך נשמעים כוונונים היסטוריים?</h2>
    <p>צללו עמוק אל תוך עולם הכוונון המוזיקלי. בחרו שיטה, האזינו לסולם ואקורד, והרגישו את ההבדלים העדינים שמעצבים את המוזיקה שאנו מכירים.</p>

    <div class="controls">
        <div>
            <label for="tuning-system">בחרו עולם צלילים (שיטת כוונון):</label>
            <select id="tuning-system">
                <option value="pythagorean">פיתגוראי</option>
                <option value="just">טהור (Just Intonation)</option>
                <option value="equal">מושווה (Equal Temperament)</option>
            </select>
        </div>
        <div class="playback-buttons">
            <button id="play-scale">נגנו את סולם דו מז'ור</button>
            <button id="play-chord">נגנו את אקורד דו מז'ור</button>
        </div>
    </div>

    <div class="display">
        <h3>יחסי התדירויות בסולם דו מז'ור בשיטה: <span id="current-tuning-name"></span></h3>
        <table id="note-ratios-table">
            <thead>
                <tr>
                    <th>תו</th>
                    <th>יחס תדירות יחסית (לדו)</th>
                    <th>תדירות (בערך, ב-Hz)</th>
                </tr>
            </thead>
            <tbody id="note-ratios">
                <!-- Ratios will be populated and animated here by JS -->
            </tbody>
        </table>
        <p class="chord-info">אקורד דו מז'ור מורכב מהתווים: דו, מי, סול.</p>
    </div>
</div>

<style>
    /* Root variables for easier theme management */
    :root {
        --primary-color: #4a90e2; /* A pleasant blue */
        --secondary-color: #50e3c2; /* A turquoise/green */
        --background-color: #f4f7f6; /* Light background */
        --card-background: #ffffff; /* White card */
        --text-color: #333;
        --border-color: #ddd;
        --hover-color: #e9e9e9;
        --active-color: #d9d9d9;
        --playing-color: #ffeb3b; /* Yellow */
        --playing-border: #fbc02d; /* Darker yellow */
    }

    body {
        font-family: 'Arial', sans-serif; /* Using a standard font */
        line-height: 1.6;
        color: var(--text-color);
        background-color: var(--background-color);
        margin: 0;
        padding: 20px;
    }

    #app {
        margin: 20px auto;
        padding: 30px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--card-background);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
        max-width: 800px; /* Limit width for better readability */
    }

    #app h2 {
        color: var(--primary-color);
        margin-top: 0;
        margin-bottom: 15px;
        font-size: 1.8rem;
    }

    #app p {
        margin-bottom: 20px;
    }

    .controls {
        margin-bottom: 30px;
        display: flex;
        flex-direction: column; /* Stack controls on small screens */
        gap: 20px;
        align-items: flex-start;
    }

    @media (min-width: 600px) {
      .controls {
        flex-direction: row; /* Side-by-side on larger screens */
        align-items: center;
        justify-content: space-between;
      }
      .controls > div {
          flex-grow: 1; /* Allow flex items to grow */
      }
      .playback-buttons {
          display: flex;
          gap: 10px;
      }
    }


    .controls label {
        margin-right: 10px;
        font-weight: bold;
        white-space: nowrap; /* Prevent label wrapping */
    }

    .controls button, .controls select {
        padding: 10px 20px;
        border: 1px solid var(--primary-color);
        border-radius: 25px; /* Pill shape */
        cursor: pointer;
        font-size: 1rem;
        transition: background-color 0.3s ease, border-color 0.3s ease, transform 0.1s ease;
        background-color: transparent;
        color: var(--primary-color);
        outline: none; /* Remove outline on focus */
    }

     .controls select {
         appearance: none; /* Remove default arrow */
         background-image: url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%234a90e2%22%20d%3D%22M287%2C197.9l-138.1-138.1c-3.7-3.7-9.6-3.7-13.3%2C0L5.4%2C197.9c-3.7%2C3.7-3.7%2C9.6%2C0%2C13.3l21.2%2C21.2c3.7%2C3.7%2C9.6%2C3.7%2C13.3%2C0l116.7-116.7l116.7%2C116.7c3.7%2C3.7%2C9.6%2C3.7%2C13.3%2C0l21.2-21.2C290.7%2C207.6%2C290.7%2C201.6%2C287%2C197.9z%22%2F%3E%3C%2Fsvg%3E'); /* Custom arrow */
         background-repeat: no-repeat;
         background-position: right 15px top 50%;
         background-size: 12px auto;
         padding-right: 40px; /* Make space for the arrow */
     }

    .controls button:hover {
        background-color: var(--primary-color);
        color: var(--card-background);
    }

    .controls button:active {
         transform: scale(0.98);
    }

    .display {
        margin-top: 30px;
        background-color: #fafafa; /* Light grey background for display area */
        padding: 20px;
        border-radius: 8px;
        border: 1px solid var(--border-color);
    }

    .display h3 {
        margin-top: 0;
        color: var(--text-color);
        font-size: 1.4rem;
        margin-bottom: 15px;
    }

    #current-tuning-name {
        color: var(--primary-color);
    }

    .display table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 10px;
    }

    .display th, .display td {
        border: 1px solid #eee; /* Lighter border */
        padding: 12px 10px;
        text-align: center;
    }

    .display th {
        background-color: #eef; /* Very light blue */
        font-weight: bold;
    }

    .display tr:nth-child(even) {
        background-color: #f9f9f9; /* Alternating row color */
    }

    /* Animation for playing notes */
    #note-ratios tr.is-playing {
        background-color: var(--playing-color) !important; /* Override zebra striping */
        color: var(--text-color);
        font-weight: bold;
        animation: pulse 0.8s ease-out infinite alternate; /* Subtle pulsing */
    }

    @keyframes pulse {
        from {
            box-shadow: 0 0 0 0px rgba(255, 235, 59, 0.7);
        }
        to {
            box-shadow: 0 0 0 10px rgba(255, 235, 59, 0);
        }
    }

    .chord-info {
        margin-top: 15px;
        font-size: 0.9rem;
        color: #555;
        text-align: center;
    }


    #toggle-explanation {
        display: block;
        margin: 30px auto 0; /* Space above, center horizontally */
        padding: 12px 25px;
        font-size: 1rem;
        cursor: pointer;
        border: 1px solid var(--secondary-color);
        border-radius: 25px;
        background-color: transparent;
        color: var(--secondary-color);
        transition: background-color 0.3s ease, color 0.3s ease, transform 0.1s ease;
        outline: none;
    }

    #toggle-explanation:hover {
        background-color: var(--secondary-color);
        color: var(--card-background);
    }
     #toggle-explanation:active {
         transform: scale(0.98);
     }

    #explanation-container {
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px solid var(--border-color);
        transition: all 0.5s ease-in-out; /* Smooth toggle animation */
        overflow: hidden; /* Hide overflow during collapse */
        max-height: 2000px; /* Set a max-height for transition */
    }

    #explanation-container.hidden {
        max-height: 0; /* Collapse height */
        padding-top: 0;
        margin-top: 0;
        border-top: none;
    }

    #explanation-container h2 {
         color: var(--secondary-color);
         margin-top: 20px;
         font-size: 1.6rem;
    }

    #explanation-container h3 {
        color: var(--primary-color);
        margin-top: 20px;
        margin-bottom: 10px;
        font-size: 1.2rem;
    }
     #explanation-container p {
         margin-bottom: 15px;
     }
</style>

<button id="toggle-explanation">הצגת הסיפור המלא מאחורי הכוונון</button>

<div id="explanation-container" class="hidden">
    <h2>הסיפור המרתק: המסע אל הכוונון המושלם (והפשרה שהצילה את המוזיקה המודרנית)</h2>

    <h3>הקדמה: מדוע יחסים מתמטיים קובעים איך המוזיקה נשמעת?</h3>
    <p>כוונון מוזיקלי אינו עניין טכני גרידא; הוא הבסיס הפיזיקלי לחוויה ההרמונית שלנו. האוזן האנושית מגיבה בצורה מיוחדת ליחסים פשוטים בין תדירויות: יחס 2:1 נשמע כאותו צליל רק גבוה יותר (אוקטבה), ויחס 3:2 יוצר מרווח "זך" ויציב במיוחד (קווינטה). יחסים אלו נשמעים הרמוניים (קונסוננטים), בעוד יחסים מורכבים יותר נשמעים פחות יציבים או צורמים (דיסוננטים). ההיסטוריה של הכוונון היא סיפור של ניסיון למצוא מערכת צלילים שתאפשר ליצור מרווחים ואקורדים קונסוננטיים רבים ככל האפשר, בתוך מגבלות כלי הנגינה והמתמטיקה.</p>

    <h3>פיתגורס והכוונון הפיתגוראי: לבנות סולם מקווינטות זכות</h3>
    <p>פיתגורס, הפילוסוף והמתמטיקאי שכולנו מכירים מהתיכון, היה גם הראשון שחקר באופן שיטתי את הקשר בין מתמטיקה ומוזיקה. הוא גילה שהצלילים הנעימים ביותר מתקבלים ממיתרים שיחס אורכם הוא מספרים שלמים ופשוטים. שיטת הכוונון הפיתגוראי, המיוחסת לו, בונה את כל הסולם המוזיקלי אך ורק על בסיס יחס הקווינטה הזכה (3:2). מתחילים מצליל בסיס (נניח, דו), ו"עורמים" קווינטות עולות ויורדות (דו -> סול -> רה -> לה -> מי -> סי... וגם דו -> פה). כל תו חדש מקבל את תדירותו על ידי כפל או חלוקה ב-3/2 (תוך התאמה לאוקטבה הנכונה על ידי כפל/חלוקה ב-2). התוצאה: כל המרווחים המבוססים על יחסים המורכבים מ-2 ו-3 בלבד (כמו קווינטות, קווארטות, ואוקטבות) נשמעים "זכים" בצורה מושלמת. האזינו בסימולציה לשיטה זו ושימו לב במיוחד לקווינטה (דו-סול).</p>

    <h3>הקאץ' הפיתגוראי: ה"פסיק" המתמטי וה"קווינטה של הזאב"</h3>
    <p>השיטה הפיתגוראית נתקלת בבעיה כשאנחנו מנסים לסגור מעגל. אם עולים 12 קווינטות פיתגוראיות בזו אחר זו (דו -> סול -> רה -> ... -> סי#), הייתם מצפים להגיע בחזרה לצליל דו, רק שבע אוקטבות מעל הצליל ההתחלתי. מבחינה מתמטית, (3/2) בחזקת 12 אמור להיות שווה בדיוק ל-2 בחזקת 7 (שבע אוקטבות). אבל... זה לא קורה! (3/2)^12 גדול במעט מ-2^7. ההפרש הקטן הזה נקרא ה"פסיק הפיתגוראי" (כ-23.5 סנט), והוא מרווח קטן מדי מכדי לשים לב אליו בדרך כלל, אך גדול מספיק כדי למנוע ממעגל הקווינטות להיסגר באופן מושלם. בפועל, כשמנסים לכוון 12 צלילים בשיטה זו, אחת הקווינטות חייבת להישאר "פתוחה" או "שבורה" – היא תהיה צרה או רחבה מדי, ותישמע צורמת במיוחד. זוהי ה"קווינטה של הזאב", כי היא "מייללת" כמו זאב. הדבר הגביל את היכולת לנגן בחופשיות בסולמות שונים או להשתמש בכל האקורדים.</p>

    <h3>טמפרמנט טהור (Just Intonation): הטוהר של היחסים הפשוטים</h3>
    <p>שיטת הכוונון הטהור, שהתפתחה מאוחר יותר, התמקדה ביצירת אקורדים קונסוננטיים בצורה מושלמת, באמצעות יחסים פשוטים לא רק של 2 ו-3, אלא גם של 5 (לדוגמה, טרצה גדולה ביחס של 5:4, וטרצה קטנה ביחס 6:5). בשיטה זו, אקורד דו מז'ור, למשל, נשמע צלול והרמוני בצורה יוצאת דופן, כי היחסים בין דו:מי:סול הם בדיוק 4:5:6. האזינו בסימולציה לשיטה זו ושימו לב לצלילות של אקורד דו מז'ור.</p>

    <h3>הבעיה של הטהור: מה קורה כשיוצאים מהמסלול?</h3>
    <p>החיסרון המשמעותי של הכוונון הטהור מתגלה במהירות כשמנסים לעבור לסולמות אחרים (מודולציה). טרצות, לדוגמה, מחושבות ביחסים שונים בהתאם להקשר ההרמוני. טרצת רה-פה בסולם דו מז'ור הטהור (שמתבסס על יחסים מדו) לא תהיה טרצה קטנה טהורה (6:5), ותישמע צורמת. כדי לנגן בצורה טהורה בכל סולם, היה צורך להוסיף צלילים רבים (דו#, רה ב2-גרסאות, מי ב2-גרסאות וכו') או לכוון את הכלי תוך כדי נגינה – דבר שהוא בלתי אפשרי בפסנתר או בגיטרה רגילים. הגמישות ההרמונית הייתה מוגבלת מאוד, מה שהקשה על התפתחות סגנונות מוזיקליים חדשים שהתבססו על מעברים תכופים בין סולמות.</p>

    <h3>חיפוש אחר פשרה: טמפרמנטים מיצועיים ואחרים</h3>
    <p>כדי להתגבר על בעיות אלו, התפתחו לאורך השנים "טמפרמנטים" שונים – שיטות פשרניות ש"מיצעו" (temper) מעט את המרווחים ה"זכים" כדי לפזר את חוסר הדיוק על פני מספר מרווחים, במקום לרכז אותו ב"קווינטת זאב" אחת. שיטות כמו הטמפרמנט המיצועי (Meantone Temperament) הקטינו במעט את הקווינטות הפיתגוראיות כדי שהטרצות הגדולות יישמעו קרובות יותר לטרצה הטהורה (5:4). שיטות אלו אפשרו נגינה נוחה יותר בכמה סולמות קרובים, אך עדיין סבלו מדיסוננסים בסולמות מרוחקים.</p>

    <h3>הטמפרמנט המושווה (Equal Temperament): הפשרה שהשתלטה על העולם</h3>
    <p>הפתרון המודרני, שהפך לסטנדרט בכלי מקלדת ופריטה במערב, הוא הטמפרמנט המושווה. שיטה זו זנחה את ה"טוהר" המתמטי המוחלט של מרבית המרווחים לטובת שוויון מוחלט: האוקטבה מחולקת ל-12 חצאי טונים *שווים לחלוטין* מבחינה לוגריתמית. כל חצי טון הוא יחס של השורש ה-12 של 2 (בערך 1.05946). המשמעות היא שכל מרווח בעל אותו שם (לדוגמה, כל הקווינטות) נשמע *בדיוק* אותו הדבר, בכל מקום על הכלי. מעגל הקווינטות "נסגר" בצורה מושלמת: 12 קווינטות שוות (כל אחת בגודל 7 חצאי טונים מושווים) מסתכמות בדיוק ב-7 אוקטבות. אף מרווח, למעט האוקטבה, אינו "טהור" לחלוטין כמו ביחסים הפשוטים, אך כולם "קרובים מספיק".</p>

    <h3>מדוע הטמפרמנט המושווה הוא הפשרה המנצחת?</h3>
    <p>הסימולציה מאפשרת לכם לשמוע את הפשרות הללו בפעולה. האזינו לאקורד דו מז'ור בשיטה הטהורה – הוא צלול ומבריק. האזינו לו בשיטה הפיתגוראית – הטרצה עלולה להישמע מעט "קשה". האזינו לו בטמפרמנט המושווה – הוא נשמע "מקובל", הרמוני, אך אולי פחות "צלול" מהטהור. היתרון העצום של המושווה הוא הגמישות האינסופית: ניתן לנגן בחופשיות בכל 12 הסולמות מז'ור ומינור, לעבור ביניהם בצורה חלקה (מודולציה), ולבנות הרמוניות מורכבות, מבלי להיתקל ב"קווינטות זאב" או בטרצות צורמות ששוברות את האוזן. ויתור קל על ה"טוהר" המושלם של מרווחים בודדים פתח את הדלת לעושר ההרמוני והמלחין שאנו מכירים ואוהבים במוזיקה המערבית מבאך ועד היום. זו הפשרה המתמטית שאפשרה את המהפכה המוזיקלית.</p>
</div>

<script>
    // Ensure AudioContext is created upon user gesture to comply with browser policies
    let audioContext = null;
    let currentOscillators = [];

    const BASE_FREQ = 261.63; // Hz (C4 - Middle C)

    // Define notes and their ratios for C Major scale/chord relative to C
    // Added keys matching Hebrew note names for easier lookup
    const scaleNotesHebrew = ['דו', 'רה', 'מי', 'פה', 'סול', 'לה', 'סי', 'דו'];
    const chordNotesHebrew = ['דו', 'מי', 'סול'];

    const tunings = {
        pythagorean: {
            name: 'פיתגוראי',
            ratios: { // Relative to C=1, built from 3/2
                'דו': { ratio: '1/1', value: 1 },
                'רה': { ratio: '9/8', value: 9/8 }, // C -> G (3/2), G -> D (3/2 * 3/2 = 9/4 -> 9/8)
                'מי': { ratio: '81/64', value: 81/64 }, // D -> A -> E
                'פה': { ratio: '4/3', value: 4/3 }, // F -> C (4/3 inverted from 3/4)
                'סול': { ratio: '3/2', value: 3/2 },
                'לה': { ratio: '27/16', value: 27/16 }, // E -> B -> F# -> C# -> G# -> D# -> A# -> F -> C -> G -> D -> A
                'סי': { ratio: '243/128', value: 243/128 }, // F# -> C# -> ... -> B
                'דו(אוקטבה)': { ratio: '2/1', value: 2 }
            }
        },
        just: {
            name: 'טהור (Just Intonation)',
            ratios: { // Standard Just Intonation for C Major Scale/Chord
                'דו': { ratio: '1/1', value: 1 },
                'רה': { ratio: '9/8', value: 9/8 },
                'מי': { ratio: '5/4', value: 5/4 },
                'פה': { ratio: '4/3', value: 4/3 },
                'סול': { ratio: '3/2', value: 3/2 },
                'לה': { ratio: '5/3', value: 5/3 },
                'סי': { ratio: '15/8', value: 15/8 },
                'דו(אוקטבה)': { ratio: '2/1', value: 2 }
            }
        },
        equal: {
            name: 'מושווה (Equal Temperament)',
            ratios: { // Relative to C=1, 2^(semitones/12)
                'דו': { ratio: '1', value: 1 }, // C (0 semitones from C)
                'רה': { ratio: '2^(2/12)', value: Math.pow(2, 2/12) }, // D (2 semitones)
                'מי': { ratio: '2^(4/12)', value: Math.pow(2, 4/12) }, // E (4 semitones)
                'פה': { ratio: '2^(5/12)', value: Math.pow(2, 5/12) }, // F (5 semitones)
                'סול': { ratio: '2^(7/12)', value: Math.pow(2, 7/12) }, // G (7 semitones)
                'לה': { ratio: '2^(9/12)', value: Math.pow(2, 9/12) }, // A (9 semitones)
                'סי': { ratio: '2^(11/12)', value: Math.pow(2, 11/12) }, // B (11 semitones)
                'דו(אוקטבה)': { ratio: '2', value: 2 } // C (12 semitones)
            }
        }
    };

    // DOM elements
    const tuningSelect = document.getElementById('tuning-system');
    const playScaleButton = document.getElementById('play-scale');
    const playChordButton = document.getElementById('play-chord');
    const noteRatiosTableBody = document.getElementById('note-ratios');
    const currentTuningNameSpan = document.getElementById('current-tuning-name');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationContainer = document.getElementById('explanation-container');
    const appContainer = document.getElementById('app'); // Get app container for initial interaction handling


    // Function to initialize AudioContext on first user interaction
    function initAudioContext() {
        if (!audioContext) {
            audioContext = new (window.AudioContext || window.webkitAudioContext)();
             // Check if context is suspended and resume if necessary (for some browsers)
            if (audioContext.state === 'suspended') {
                audioContext.resume();
            }
        }
    }

    // Function to stop any currently playing sound and clear highlights
    function stopSound() {
         if (!audioContext) return; // Don't try to stop if not initialized
        currentOscillators.forEach(osc => {
            try {
                osc.stop(); // Stop the sound immediately
                osc.disconnect();
            } catch (e) {
                // Oscillator might have already stopped
                console.warn("Error stopping oscillator:", e);
            }
        });
        currentOscillators = [];
        // Clear all playing highlights
        document.querySelectorAll('#note-ratios tr').forEach(row => {
            row.classList.remove('is-playing');
        });
    }

    // Function to play a single note with a simple envelope
    function playNote(frequency, duration = 1.5, noteHebrew = '') {
        initAudioContext(); // Ensure context is active

        const oscillator = audioContext.createOscillator();
        const gainNode = audioContext.createGain();

        oscillator.type = 'sine'; // sine wave for clarity, can be changed later
        oscillator.frequency.setValueAtTime(frequency, audioContext.currentTime);

        // Simple ADSR envelope (Attack, Decay, Sustain, Release)
        const attackTime = 0.02;
        const decayTime = 0.1;
        const sustainLevel = 0.5; // Lower sustain
        const releaseTime = 0.3;
        const maxGain = 0.3; // Max volume

        gainNode.gain.setValueAtTime(0, audioContext.currentTime); // Start at 0 volume
        gainNode.gain.linearRampToValueAtTime(maxGain, audioContext.currentTime + attackTime); // Attack
        gainNode.gain.linearRampToValueAtTime(maxGain * sustainLevel, audioContext.currentTime + attackTime + decayTime); // Decay
        // Sustain level is held until release

        oscillator.connect(gainNode).connect(audioContext.destination);
        oscillator.start(audioContext.currentTime);
        // Schedule stop and release
        gainNode.gain.linearRampToValueAtTime(0.0001, audioContext.currentTime + duration - releaseTime); // Start release
        oscillator.stop(audioContext.currentTime + duration); // Stop oscillator completely after duration

        // Add to tracking list
        currentOscillators.push(oscillator);
         // Clean up list after note ends
        oscillator.onended = () => {
            currentOscillators = currentOscillators.filter(osc => osc !== oscillator);
             // Remove highlight when note fully ends (including release)
             if(noteHebrew) {
                 const noteRow = document.querySelector(`#note-ratios tr[data-note-heb="${noteHebrew}"]`);
                 if (noteRow) {
                     noteRow.classList.remove('is-playing');
                 }
             }
        };

         // Add highlight immediately when note starts
         if(noteHebrew) {
             const noteRow = document.querySelector(`#note-ratios tr[data-note-heb="${noteHebrew}"]`);
             if (noteRow) {
                 noteRow.classList.add('is-playing');
                 // Note: The highlight is removed in the onended callback
             }
         }
    }

    // Function to play a sequence of notes (scale)
    async function playScale(notes) {
        stopSound(); // Stop any previous sound
        const selectedTuning = tuningSelect.value;
        const tuningRatios = tunings[selectedTuning].ratios;
        let delay = 0;
        const delayBetweenNotes = 500; // ms

        for (let i = 0; i < notes.length; i++) {
            const noteHebrew = notes[i];
            // Handle octave C explicitly
            const noteKey = (noteHebrew === 'דו' && i > 0) ? 'דו(אוקטבה)' : noteHebrew;

            const ratioData = tuningRatios[noteKey];

            if (ratioData) {
                const frequency = BASE_FREQ * ratioData.value;
                 // Use a promise-based delay to wait between notes
                await new Promise(resolve => setTimeout(resolve, delayBetweenNotes));
                playNote(frequency, 1.0, noteKey); // Play note for 1 second
            }
        }
    }

    // Function to play multiple notes simultaneously (chord)
    function playChord(notes) {
        stopSound(); // Stop any previous sound
        const selectedTuning = tuningSelect.value;
        const tuningRatios = tunings[selectedTuning].ratios;
        const chordDuration = 3.0; // Duration for the chord

        notes.forEach(noteHebrew => {
             const ratioData = tuningRatios[noteHebrew];
             if (ratioData) {
                const frequency = BASE_FREQ * ratioData.value;
                playNote(frequency, chordDuration, noteHebrew); // Play chord notes for 3 seconds
            }
        });
    }

    // Function to update the table with current tuning ratios
    function updateRatiosDisplay() {
        const selectedTuning = tuningSelect.value;
        const tuningData = tunings[selectedTuning];
        currentTuningNameSpan.textContent = tuningData.name;
        noteRatiosTableBody.innerHTML = ''; // Clear current table

        // Display ratios for all scale notes (including octave C)
        const notesToDisplayKeys = ['דו', 'רה', 'מי', 'פה', 'סול', 'לה', 'סי', 'דו(אוקטבה)'];
        const notesToDisplayHebrew = ['דו', 'רה', 'מי', 'פה', 'סול', 'לה', 'סי', 'דו (אוקטבה)']; // Display names


        notesToDisplayKeys.forEach((noteKey, index) => {
             const ratioData = tuningData.ratios[noteKey];
             const row = noteRatiosTableBody.insertRow();
             row.setAttribute('data-note-heb', noteKey); // Add data attribute for JS targeting

             const cellNote = row.insertCell(0);
             const cellRatio = row.insertCell(1);
             const cellFrequency = row.insertCell(2);

             cellNote.textContent = notesToDisplayHebrew[index]; // Use friendly display name
             if (ratioData) {
                 cellRatio.textContent = ratioData.ratio;
                 cellFrequency.textContent = (BASE_FREQ * ratioData.value).toFixed(3) + ' Hz'; // Show frequency with more precision
             } else {
                 cellRatio.textContent = '-';
                 cellFrequency.textContent = '-';
             }
        });
    }

    // Event listeners
    tuningSelect.addEventListener('change', () => {
        stopSound(); // Stop sound when changing tuning
        updateRatiosDisplay();
    });

    // Use mousedown/touchstart to initialize audio context immediately on first interaction
    appContainer.addEventListener('mousedown', initAudioContext, { once: true });
    appContainer.addEventListener('touchstart', initAudioContext, { once: true });


    playScaleButton.addEventListener('click', () => {
         initAudioContext(); // Ensure context is active on click too
         playScale(scaleNotesHebrew);
    });

    playChordButton.addEventListener('click', () => {
        initAudioContext(); // Ensure context is active on click too
        playChord(chordNotesHebrew);
    });

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationContainer.classList.contains('hidden');
        explanationContainer.classList.toggle('hidden', !isHidden); // Set hidden state
        explanationContainer.style.maxHeight = isHidden ? explanationContainer.scrollHeight + "px" : '0'; // Animate height

        toggleExplanationButton.textContent = isHidden ? 'הסתר את הסיפור המלא' : 'הצגת הסיפור המלא מאחורי הכוונון';

         // Remove max-height after transition to allow dynamic content
         explanationContainer.addEventListener('transitionend', function handler() {
            if (!explanationContainer.classList.contains('hidden')) {
                explanationContainer.style.maxHeight = 'none';
            }
             explanationContainer.removeEventListener('transitionend', handler);
         });

         if (!isHidden) {
              explanationContainer.style.maxHeight = explanationContainer.scrollHeight + "px"; // Set current height before transition
              requestAnimationFrame(() => {
                  explanationContainer.style.maxHeight = '0'; // Animate to 0
              });
         }
    });


    // Initial display update
    updateRatiosDisplay();

</script>
---
```