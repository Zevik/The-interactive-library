---
title: "בלשים מוזיקליים: נגלה את כלי הנגינה העתיקים"
english_slug: musical-detectives-identify-ancient-instruments
category: "מוזיקה"
tags:
  - כלי נגינה
  - מוזיקה קלאסית
  - רנסנס
  - בארוק
  - היסטוריה של המוזיקה
---
# בלשים מוזיקליים: נגלה את כלי הנגינה העתיקים

צאו למסע בלשי מרתק אל צלילי העבר! האם תוכלו לזהות את קולם הייחודי של כלי הנגינה מתקופות הרנסנס והבארוק? האוזן שלכם היא הכלי החשוב ביותר במשימה הזו. האזינו היטב, בחרו את הכלי הנכון מתוך התמונות, וגלו כמה אתם בלשים מוזיקליים מעולים!

<div id="app">
    <div id="quiz-area">
        <div id="audio-player">
            <p><strong>שלב {{ currentQuestionNumber }} מתוך {{ totalQuestions }}:</strong></p>
            <audio id="instrument-sound">
                <source src="" type="audio/mpeg">
                הדפדפן שלך אינו תומך באלמנט האודיו.
            </audio>
            <button id="play-sound-button" aria-label="נגן צליל כלי הנגינה">האזינו לצליל 🔊</button>
        </div>

        <div id="instrument-options" class="options-grid">
            <!-- Image options will be loaded here by JavaScript -->
        </div>

        <div id="feedback">
            <!-- Feedback message will appear here -->
        </div>

        <div id="correct-instrument-info" class="info-panel">
            <h3>הכלי ששמעתם היה: <span id="correct-instrument-name"></span></h3>
            <img id="correct-instrument-image" src="" alt="Correct Instrument Image">
            <button id="next-question-button" class="button primary">לשאלה הבאה</button>
        </div>

        <div id="quiz-complete" class="info-panel">
            <h2>משימת הבלשות הושלמה!</h2>
            <p>כל הכבוד על זיהוי הכלים ההיסטוריים! מקווים שנהניתם מהמסע אל צלילי הרנסנס והבארוק.</p>
            <button id="restart-quiz-button" class="button secondary">התחילו מחדש</button>
        </div>
    </div>

     <button id="toggle-explanation-button" class="button secondary">רוצים ללמוד עוד? צללו לעומק הסיפור שמאחורי הצלילים</button>

    <div id="explanation" class="info-panel">
        <h2>הסבר נוסף: מסע אל צלילי העבר</h2>

        <section>
            <h3>מבוא לתקופות הרנסנס והבארוק במוזיקה</h3>
            <p>מוזיקת הרנסנס (בערך 1400-1600) התאפיינה בריבוי קולות (פוליפוניה), הרמוניות רגועות יחסית וצליל טהור. מוזיקת הבארוק (בערך 1600-1750) לעומתה, הכניסה דרמה, ניגודים חריפים (כמו בין סולן לתזמורת קטנה - קונצ'רטו גרוסו), והתפתחה בה תחושת טונאליות מודרנית יותר. שתי התקופות הללו ראו התפתחות משמעותית בכלי הנגינה ושימוש הולך וגובר בהם, לצד המוזיקה הקולית.</p>
        </section>

        <section>
            <h3>למה הכלים הישנים נשמעים אחרת?</h3>
            <p>כלי נגינה "עתיקים" או "תקופתיים" נשמעים שונה ממקביליהם המודרניים ממספר סיבות מרתקות:</p>
            <ul>
                <li><strong>מבנה:</strong> הגיאומטריה של הכלים הייתה שונה – קשתות קצרות יותר בכלי קשת, מבנה פנימי שונה בכלי נשיפה.</li>
                <li><strong>חומרים:</strong> השתמשו במעי גולמי למיתרים במקום מתכת, עץ שונה, ועורות אחרים לתופים.</li>
                <li><strong>שיטות נגינה:</strong> טכניקות כמו שימוש בוויברטו, פוזיציות יד, וטכניקות קשת היו שונות מהיום.</li>
                <li><strong>כיוון (פיץ' וטמפרמנט):</strong> גובה הצליל הכללי היה בדרך כלל נמוך יותר, ו"מזג הכיוון" היה שונה, מה שיצר הרמוניות וצלילים ייחודיים.</li>
            </ul>
            <p>כל אלה יוצרים צליל בעל אופי שונה – לעיתים עדין יותר, 'אדמתי', או בעל צבעים ייחודיים שפחות נפוצים בכלים המודרניים.</p>
        </section>

         <section>
            <h3>פגשו את הכלים: סקירה קצרה</h3>
            <ul>
                <li><strong>לאוטה:</strong> כלי מיתר שפרטים בצורת אגס, פופולרי במיוחד ברנסנס. צליל מתוק ועדין.</li>
                <li><strong>צ'מבלו:</strong> כלי מקלדת מיוחד שבו המיתרים נצבטים (ולא מוכים). צליל מבריק אך ללא יכולת לשלוט בווליום.</li>
                <li><strong>ויולה דה גמבה:</strong> כלי קשת אלגנטי שמוחזק בין הרגליים, עם מספר מיתרים וסריגים. צליל רך ועשיר.</li>
                <li><strong>חלילית:</strong> כלי נשיפה מעץ, אהוב בכל התקופות, עם צליל פשוט וישיר.</li>
                <li><strong>קרומהורן:</strong> כלי נשיפה עם קנה כפול מכוסה שיוצר צליל "זמזם" אופייני וקצת קומי.</li>
                <li><strong>תאורבו:</strong> לאוטה ענקית עם צוואר ארוך במיוחד למיתרי בס נמוכים, שימש לליווי (בס קונטינואו) בבארוק.</li>
                <li><strong>כינור בארוק:</strong> האב הקדמון לכינור המודרני, עם קשת קלה יותר, צוואר קצר יותר ומיתרי מעי. הצליל עדין ופחות דרמטי מהכינור המודרני.</li>
            </ul>
        </section>

        <section>
            <h3>האזנה אקטיבית: מנעד הצלילים והצבעים</h3>
            <p>האפליקציה הזו מזמינה אתכם לפתח את האוזן לניואנסים הללו. נסו לשים לב להבדלים בצבע הצליל, לאופן שבו הצליל דועך, ול"אופי" הכללי של כל כלי. הצלילים האלה הם חלק בלתי נפרד מהשפה והאסתטיקה המוזיקלית של תקופות הרנסנס והבארוק.</p>
        </section>

        <section>
            <h3>"ביצוע אותנטי": להחיות את העבר</h3>
            <p>מוזיקאים רבים היום מקדישים את הקריירה שלהם ל"ביצוע אותנטי" או "ביצוע תקופתי". הם משתמשים בכלי נגינה היסטוריים (או העתקים מדויקים שלהם) וטכניקות נגינה עתיקות כדי לשחזר ככל הניתן את הצליל והחוויה שהיו נהוגים כשהמוזיקה נכתבה לראשונה. זה מאפשר לנו להבין ולהעריך את המוזיקה הזו בצורה עמוקה ומקורית יותר.</p>
        </section>

        <section>
            <h3>סיכום</h3>
            <p>אנו מקווים שנהניתם ממשימת הבלשות המוזיקלית! היכרות עם כלי הנגינה ההיסטוריים היא מפתח להבנה עמוקה יותר של עולם המוזיקה הקלאסית בכלל, ושל תקופות הרנסנס והבארוק בפרט. המשיכו לחקור ולהקשיב!</p>
        </section>
    </div>
</div>

<style>
    :root {
        --primary-color: #4A90E2; /* A pleasant blue */
        --secondary-color: #50E3C2; /* A vibrant green */
        --text-color: #333;
        --background-color: #F8F8F8;
        --card-background: #FFFFFF;
        --correct-color: #7ED321; /* Green */
        --incorrect-color: #D0021B; /* Red */
        --border-color: #E0E0E0;
        --shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        --border-radius: 8px;
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: var(--text-color);
        background-color: var(--background-color);
        margin: 0;
        padding: 20px;
        direction: rtl; /* Hebrew support */
        text-align: right; /* Hebrew support */
    }

    h1, h2, h3 {
        color: var(--primary-color);
        text-align: center;
        margin-bottom: 20px;
    }

    #app {
        max-width: 800px;
        margin: 20px auto;
        background-color: var(--card-background);
        padding: 30px;
        border-radius: var(--border-radius);
        box-shadow: var(--shadow);
    }

    #quiz-area {
        min-height: 400px; /* Ensure area has some minimum height */
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 20px;
    }

    #audio-player {
        text-align: center;
        margin-bottom: 20px;
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 20px;
        width: 100%;
    }

    #play-sound-button {
        background-color: var(--secondary-color);
        color: white;
        border: none;
        padding: 12px 25px;
        border-radius: var(--border-radius);
        font-size: 1.1em;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

    #play-sound-button:hover {
        background-color: #42c8ac; /* Darker green */
    }
     #play-sound-button:active {
        transform: scale(0.98);
    }

    audio {
         display: none; /* Hide default audio controls */
    }


    .options-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); /* Responsive grid */
        gap: 20px;
        width: 100%;
        justify-items: center; /* Center items in grid cells */
    }

    .option {
        cursor: pointer;
        border: 3px solid transparent;
        border-radius: var(--border-radius);
        overflow: hidden; /* Ensure border-radius works with image */
        text-align: center;
        transition: border-color 0.3s ease, transform 0.2s ease, box-shadow 0.3s ease;
        padding: 0; /* Remove default padding */
        position: relative; /* For icon overlay */
        width: 100%; /* Make option take full grid cell width */
        max-width: 180px; /* Limit max width of each option card */
        background-color: var(--card-background);
        box-shadow: var(--shadow);
         display: flex;
        flex-direction: column;
        align-items: center;
    }

    .option:hover {
        border-color: var(--primary-color);
        transform: translateY(-5px); /* Lift effect on hover */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }

    .option img {
        width: 100%; /* Make image fill the option width */
        height: 180px; /* Fixed height for images */
        object-fit: cover; /* Cover the area without stretching */
        display: block;
        border-bottom: 1px solid var(--border-color);
         transition: transform 0.3s ease;
    }
     .option:hover img {
        transform: scale(1.03);
     }


    .option span.instrument-name {
        display: block;
        padding: 10px;
        font-weight: bold;
        font-size: 1em;
         color: var(--text-color);
    }

     .option .icon-overlay {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 3em;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        opacity: 0;
        transition: opacity 0.3s ease;
     }
     .option.selected .icon-overlay {
         opacity: 1;
     }
     .option.selected.correct .icon-overlay {
         content: '✔'; /* Checkmark */
         color: var(--correct-color);
     }
      .option.selected.incorrect .icon-overlay {
         content: '✖'; /* X */
         color: var(--incorrect-color);
      }


    #feedback {
        margin-top: 20px;
        padding: 15px;
        border-radius: var(--border-radius);
        font-size: 1.3em;
        font-weight: bold;
        text-align: center;
        min-height: 1.5em; /* Reserve space */
        opacity: 0; /* Start hidden */
        transform: translateY(20px); /* Start lower */
        transition: opacity 0.5s ease-out, transform 0.5s ease-out;
        width: 100%;
    }

    #feedback.show {
        opacity: 1;
        transform: translateY(0);
    }

    #feedback.correct {
        color: white;
        background-color: var(--correct-color);
    }

    #feedback.incorrect {
         color: white;
        background-color: var(--incorrect-color);
    }

    .info-panel {
        margin-top: 20px;
        padding: 20px;
        border-radius: var(--border-radius);
        background-color: var(--background-color);
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.05);
        text-align: center;
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.5s ease-out, transform 0.5s ease-out;
         width: 100%;
        max-width: 500px;
    }
     .info-panel.show {
        opacity: 1;
        transform: translateY(0);
    }

    #correct-instrument-info img {
        max-width: 200px;
        height: auto;
        margin-top: 15px;
        border-radius: var(--border-radius);
        box-shadow: var(--shadow);
    }

    .button {
        padding: 10px 20px;
        font-size: 1em;
        cursor: pointer;
        border: none;
        border-radius: var(--border-radius);
        transition: background-color 0.3s ease, transform 0.1s ease;
        margin-top: 15px;
    }
    .button.primary {
        background-color: var(--primary-color);
        color: white;
    }
     .button.primary:hover {
        background-color: #357abd; /* Darker blue */
     }
    .button.secondary {
        background-color: transparent;
        color: var(--primary-color);
        border: 2px solid var(--primary-color);
    }
    .button.secondary:hover {
        background-color: rgba(74, 144, 226, 0.1);
    }
     .button:active {
        transform: scale(0.98);
    }


    #toggle-explanation-button {
        display: block; /* Make it a block element */
        margin: 30px auto 0; /* Center it below the quiz */
        width: fit-content; /* Fit width to content */
    }


    #explanation {
        text-align: right;
        padding: 20px;
         margin-top: 30px; /* Space below the button */
         display: none; /* Start hidden */
          background-color: var(--card-background);
         box-shadow: var(--shadow);
    }

    #explanation.show {
        display: block;
    }


    #explanation section {
        margin-bottom: 25px;
        padding-bottom: 15px;
        border-bottom: 1px dashed var(--border-color);
    }
     #explanation section:last-child {
         border-bottom: none;
     }

    #explanation h3 {
        color: var(--secondary-color);
        text-align: right;
        margin-bottom: 10px;
         border-bottom: 2px solid var(--secondary-color);
         padding-bottom: 5px;
         width: fit-content;
     }

    #explanation ul {
        list-style: none;
        padding: 0;
         margin-top: 10px;
    }

    #explanation li {
        margin-bottom: 10px;
        padding-right: 20px;
        position: relative;
    }
     #explanation li::before {
         content: '🎵'; /* Music note bullet */
         position: absolute;
         right: 0;
         color: var(--primary-color);
     }

     /* Animations */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }

    .animate-fade-in-up {
        animation: fadeInUp 0.5s ease-out forwards;
    }
     .animate-pulse {
         animation: pulse 0.5s ease-in-out;
     }


     /* Responsive Adjustments */
     @media (max-width: 600px) {
         body {
             padding: 10px;
         }
         #app {
             padding: 15px;
         }
         .options-grid {
              grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
              gap: 10px;
         }
         .option img {
             height: 150px;
         }
         .button {
             padding: 8px 15px;
             font-size: 0.9em;
         }
         #feedback {
              font-size: 1.1em;
              padding: 10px;
         }
         .info-panel {
             padding: 15px;
         }
          #correct-instrument-info img {
             max-width: 150px;
         }
          h1 {
              font-size: 1.8em;
         }
          h2 {
             font-size: 1.5em;
          }
          h3 {
             font-size: 1.2em;
          }
     }


</style>

<script>
    const instruments = {
        lute: { name: "לאוטה", image: "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Renaissance_lute_by_Sixtus_Rauwolf%2C_Augsburg%2C_1590.jpg/800px-Renaissance_lute_by_Sixtus_Rauwolf%2C_Augsburg%2C_1590.jpg" },
        harpsichord: { name: "צ'מבלו", image: "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Harpsichord.jpg/800px-Harpsichord.jpg" },
        viola_da_gamba: { name: "ויולה דה גמבה", image: "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Bass_viola_da_gamba_MET_DP145546.jpg/800px-Bass_viola_da_gamba_MET_DP145546.jpg" },
        recorder: { name: "חלילית", image: "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Alto_recorder_Mollenhauer.jpg/800px-Alto_recorder_Mollenhauer.jpg" },
        crumhorn: { name: "קרומהורן", image: "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Tenor_krummhorn.jpg/800px-Tenor_krummhorn.jpg" },
        theorbo: { name: "תאורבו", image: "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Theorbo.jpg/800px-Theorbo.jpg" },
        baroque_violin: { name: "כינור בארוק", image: "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Baroque_violin_by_Jacob_Stainer_1679.jpg/800px-Baroque_violin_by_Jacob_Stainer_1679.jpg" },
        // Add more instruments as needed
    };

     // Adding more questions for better quiz flow
    const allQuestions = [
        { audio: "https://www.music.vt.edu/musicdictionary/L/Lute/lute.mp3", correctInstrument: "lute", options: ["lute", "theorbo", "harpsichord", "baroque_violin"] },
        { audio: "https://www.music.vt.edu/musicdictionary/H/Harpsichord/HarpsichordSound.mp3", correctInstrument: "harpsichord", options: ["harpsichord", "viola_da_gamba", "recorder", "lute"] },
        { audio: "https://www.music.vt.edu/musicdictionary/V/Violadagamba/violadagambasound.mp3", correctInstrument: "viola_da_gamba", options: ["baroque_violin", "viola_da_gamba", "crumhorn", "theorbo"] },
        { audio: "https://www.music.vt.edu/musicdictionary/R/Recorder/RecorderSound.mp3", correctInstrument: "recorder", options: ["recorder", "crumhorn", "harpsichord", "viola_da_gamba"] },
        { audio: "https://www.music.vt.edu/musicdictionary/C/Crummhorn/crumhorn.mp3", correctInstrument: "crumhorn", options: ["crumhorn", "recorder", "lute", "harpsichord"] },
        { audio: "https://www.music.vt.edu/musicdictionary/T/Theorbo/theorbo.mp3", correctInstrument: "theorbo", options: ["lute", "theorbo", "baroque_violin", "viola_da_gamba"] },
         { audio: "https://www.music.vt.edu/musicdictionary/B/Baroque%20Violin/BaroqueViolin.mp3", correctInstrument: "baroque_violin", options: ["baroque_violin", "viola_da_gamba", "lute", "theorbo"] },
         // Adding variety in options, ensuring correct one is always present
         { audio: "https://www.music.vt.edu/musicdictionary/L/Lute/lute.mp3", correctInstrument: "lute", options: ["crumhorn", "harpsichord", "lute", "baroque_violin"] },
        { audio: "https://www.music.vt.edu/musicdictionary/H/Harpsichord/HarpsichordSound.mp3", correctInstrument: "harpsichord", options: ["theorbo", "recorder", "harpsichord", "viola_da_gamba"] },
    ];

    let currentQuestionIndex = 0;
    let questionsForThisGame = []; // Array to hold shuffled questions for the current game session

    const instrumentSound = document.getElementById('instrument-sound');
    const playSoundButton = document.getElementById('play-sound-button');
    const instrumentOptionsDiv = document.getElementById('instrument-options');
    const feedbackDiv = document.getElementById('feedback');
    const correctInfoDiv = document.getElementById('correct-instrument-info');
    const correctInstrumentNameSpan = document.getElementById('correct-instrument-name');
    const correctInstrumentImage = document.getElementById('correct-instrument-image');
    const nextButton = document.getElementById('next-question-button');
    const quizCompleteDiv = document.getElementById('quiz-complete');
    const restartButton = document.getElementById('restart-quiz-button');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation-button');

    // Update question counter display
    const questionCounterSpan = document.querySelector('#audio-player p strong');


    // Helper to shuffle array
    function shuffleArray(array) {
        const shuffled = array.slice(); // Create a copy
        for (let i = shuffled.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]]; // Swap elements
        }
        return shuffled;
    }

     // Helper to select a random subset of options including the correct one
    function selectRandomOptions(correctInstrumentSlug, allSlugs, numOptions = 4) {
        let options = new Set([correctInstrumentSlug]); // Start with the correct one
        const availableSlugs = allSlugs.filter(slug => slug !== correctInstrumentSlug);
        const shuffledAvailable = shuffleArray(availableSlugs);

        for(let i = 0; options.size < numOptions && i < shuffledAvailable.length; i++) {
            options.add(shuffledAvailable[i]);
        }
         // Ensure we have enough options, even if we need to repeat from originals
         while (options.size < numOptions) {
             options.add(allSlugs[Math.floor(Math.random() * allSlugs.length)]);
         }

        return shuffleArray(Array.from(options));
    }


    function startGame() {
        currentQuestionIndex = 0;
        // Shuffle all questions and maybe pick a subset
        questionsForThisGame = shuffleArray(allQuestions); // Use all questions shuffled
        quizCompleteDiv.classList.remove('show');
        quizCompleteDiv.style.display = 'none'; // Hide quiz complete message
         document.getElementById('quiz-area').style.display = 'flex'; // Show quiz area

        loadQuestion(currentQuestionIndex);
    }


    function loadQuestion(index) {
        if (index >= questionsForThisGame.length) {
            endGame();
            return;
        }

        const question = questionsForThisGame[index];
        const allInstrumentSlugs = Object.keys(instruments);
        const optionsForThisQuestion = selectRandomOptions(question.correctInstrument, allInstrumentSlugs, 4); // Select 4 options

        // Reset UI elements
        feedbackDiv.classList.remove('show', 'correct', 'incorrect');
        feedbackDiv.innerText = '';
        correctInfoDiv.classList.remove('show');
        correctInfoDiv.style.display = 'none';
        nextButton.style.display = 'none';
        instrumentSound.style.display = 'block'; // Show player (or just the button)
        playSoundButton.style.display = 'block'; // Show play button
        instrumentOptionsDiv.innerHTML = ''; // Clear previous options

        // Update question counter
        questionCounterSpan.innerText = `שלב ${currentQuestionIndex + 1} מתוך ${questionsForThisGame.length}`;


        // Load audio
        instrumentSound.src = question.audio;
        instrumentSound.load(); // Load the new audio source


        // Create and append option elements
        optionsForThisQuestion.forEach(instrumentSlug => {
            const instrumentData = instruments[instrumentSlug];
            const optionDiv = document.createElement('div');
            optionDiv.classList.add('option');
            optionDiv.dataset.instrument = instrumentSlug;

            const img = document.createElement('img');
            img.src = instrumentData.image;
            img.alt = instrumentData.name;

             const nameSpan = document.createElement('span');
             nameSpan.classList.add('instrument-name');
             nameSpan.innerText = instrumentData.name; // Add name below image

             const iconOverlay = document.createElement('div');
             iconOverlay.classList.add('icon-overlay');
             iconOverlay.innerHTML = ''; // Will be populated by checkAnswer

             optionDiv.appendChild(img);
             optionDiv.appendChild(nameSpan);
             optionDiv.appendChild(iconOverlay);

            // Add click listener *after* options are loaded
            optionDiv.addEventListener('click', () => checkAnswer(instrumentSlug, optionDiv));

            instrumentOptionsDiv.appendChild(optionDiv);
             // Add animation class
             setTimeout(() => optionDiv.classList.add('animate-fade-in-up'), 50 + optionsForThisQuestion.indexOf(instrumentSlug) * 100); // Staggered animation
        });


        // Pause audio and reset time when question loads
        instrumentSound.pause();
        instrumentSound.currentTime = 0;

         // Enable clicking on options
        document.querySelectorAll('.option').forEach(option => {
            option.style.pointerEvents = 'auto';
            option.style.border = '3px solid transparent'; // Reset border
            option.classList.remove('selected', 'correct', 'incorrect');
            option.querySelector('.icon-overlay').innerHTML = ''; // Clear icon
        });
    }

     function playSound() {
         instrumentSound.currentTime = 0; // Rewind to start
         instrumentSound.play().catch(error => console.error("Audio playback failed:", error)); // Handle potential autoplay errors
     }

    function checkAnswer(selectedInstrumentSlug, selectedOptionElement) {
        const question = questionsForThisGame[currentQuestionIndex];
        const correctInstrumentSlug = question.correctInstrument;
        const correctInstrumentData = instruments[correctInstrumentSlug];

        // Disable clicking after an answer
        document.querySelectorAll('.option').forEach(option => {
            option.style.pointerEvents = 'none';
        });

        // Add visual feedback to the selected option
        selectedOptionElement.classList.add('selected');

        if (selectedInstrumentSlug === correctInstrumentSlug) {
            feedbackDiv.innerText = 'מעולה, זיהוי מדויק!';
            feedbackDiv.classList.add('correct');
             selectedOptionElement.classList.add('correct');
             selectedOptionElement.querySelector('.icon-overlay').innerHTML = '✔';
             selectedOptionElement.classList.add('animate-pulse'); // Add pulse on correct answer
        } else {
            feedbackDiv.innerText = `המממ... לא הפעם. הקול הזה שייך ל${correctInstrumentData.name}.`;
            feedbackDiv.classList.add('incorrect');
             selectedOptionElement.classList.add('incorrect');
             selectedOptionElement.querySelector('.icon-overlay').innerHTML = '✖';

            // Highlight the correct one as well
             const correctOptionElement = document.querySelector(`.option[data-instrument="${correctInstrumentSlug}"]`);
             if(correctOptionElement) {
                  correctOptionElement.classList.add('correct');
                   correctOptionElement.style.border = `3px solid ${getComputedStyle(document.documentElement).getPropertyValue('--correct-color').trim()}`;
             }
        }

        // Show feedback with animation
        feedbackDiv.style.display = 'block';
        setTimeout(() => feedbackDiv.classList.add('show'), 50); // Animate in

        // Show correct instrument info
        correctInstrumentNameSpan.innerText = correctInstrumentData.name;
        correctInstrumentImage.src = correctInstrumentData.image;
        correctInfoDiv.style.display = 'block';
         setTimeout(() => correctInfoDiv.classList.add('show'), 600); // Animate in after feedback

        // Show next button
         nextButton.style.display = 'block';


        currentQuestionIndex++; // Prepare for the next question
    }

    function endGame() {
        document.getElementById('quiz-area').style.display = 'none'; // Hide quiz area
        quizCompleteDiv.style.display = 'block';
        quizCompleteDiv.classList.add('show', 'animate-fade-in-up'); // Show quiz complete message
    }


    // Event Listeners
     playSoundButton.addEventListener('click', playSound);

    nextButton.addEventListener('click', () => {
        loadQuestion(currentQuestionIndex);
    });

    restartButton.addEventListener('click', () => {
        startGame(); // Restart the game
    });

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.classList.contains('hide');
        if (isHidden) {
            explanationDiv.style.display = 'block';
            setTimeout(() => explanationDiv.classList.add('show'), 10); // Small delay for display:block to apply before animation
            explanationDiv.classList.remove('hide');
            toggleExplanationButton.innerText = 'סגרו את הסיפור';
            toggleExplanationButton.classList.remove('secondary');
            toggleExplanationButton.classList.add('primary');
        } else {
            explanationDiv.classList.remove('show');
             explanationDiv.classList.add('hide');
            setTimeout(() => explanationDiv.style.display = 'none', 500); // Delay hide until animation ends
            toggleExplanationButton.innerText = 'רוצים ללמוד עוד? צללו לעומק הסיפור שמאחורי הצלילים';
             toggleExplanationButton.classList.remove('primary');
            toggleExplanationButton.classList.add('secondary');
        }
    });


    // Initial setup
    document.addEventListener('DOMContentLoaded', () => {
        startGame(); // Start the first game when the page loads
        // Set total questions count dynamically (for initial display)
         document.querySelector('#audio-player p strong').innerText = `שלב 1 מתוך ${allQuestions.length}`;
    });

</script>