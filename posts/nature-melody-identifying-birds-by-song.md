---
title: "מנגינת הטבע: צלילי הציפורים המסתוריים"
english_slug: nature-melody-identifying-birds-by-song
category: "ביולוגיה"
tags: [ציפורים, שירה, זיהוי, אקולוגיה, טבע]
---
# מנגינת הטבע: צלילי הציפורים המסתוריים

האם אי פעם יצאתם לטבע או אפילו רק הקשבתם לרחשים מעבר לחלון, ושמעתם שירת ציפורים קסומה שתהיתם למי היא שייכת? עולם הצלילים של הציפורים הוא מרתק ועשיר, והיכולת לזהות את המינים השונים רק לפי שירתן פותחת בפנינו שער לחוויה עמוקה יותר של הטבע סביבנו. האם האוזן שלכם חדה מספיק לאתגר? בואו נגלה!

<div id="bird-song-app" class="game-container">
    <div id="challenge-area" class="game-section">
        <div class="header-flex">
             <h2><i class="icon-headset"></i> מה הציפור שרה?</h2>
             <div id="score-display" class="score-board"><span id="current-score">0</span> / <span id="total-challenges">0</span></div>
        </div>

        <div class="audio-player-area">
             <p id="challenge-info" class="info-text">לחצו על כפתור ההשמעה והקשיבו היטב:</p>
             <button id="play-sound-btn" class="game-button play-button" title="השמע שירה"><i class="icon-play"></i> השמע</button>
             <audio id="bird-audio" src="" preload="auto"></audio>
             <div class="audio-indicator"></div> <!-- Visual indicator -->
        </div>
    </div>

    <div id="options-area" class="game-section">
        <h3><i class="icon-question"></i> מי הזמר המסתורי?</h3>
        <div id="options-list" class="options-grid">
            <!-- Options will be loaded here by JS -->
        </div>
    </div>

    <div id="feedback-area" class="game-section feedback-section">
        <!-- Feedback and facts will appear here -->
    </div>

    <div id="end-of-game" class="game-section end-screen" style="display: none;">
        <h2><i class="icon-trophy"></i> סיימנו את האתגר!</h2>
        <p id="final-score" class="final-score-text"></p>
        <button onclick="restartGame()" class="game-button restart-button"><i class="icon-reload"></i> אתגר חדש</button>
    </div>
</div>

<style>
    /* Basic Reset & Global Styles */
    #bird-song-app * {
        box-sizing: border-box;
    }

    #bird-song-app {
        font-family: 'Arial', sans-serif; /* Using common sans-serif */
        direction: rtl;
        text-align: right;
        max-width: 750px; /* Slightly wider for better layout */
        margin: 25px auto;
        padding: 30px;
        border: 1px solid #e0e0e0;
        border-radius: 12px; /* More rounded corners */
        background-color: #fefefe; /* Lighter background */
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08); /* Softer shadow */
        color: #333;
    }

    /* Headers */
    #bird-song-app h2, #bird-song-app h3 {
        color: #00796b; /* Teal color for headings */
        border-bottom: 2px solid #009688; /* Matching border */
        padding-bottom: 8px;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

     #bird-song-app h2 i, #bird-song-app h3 i { /* Basic icon styling (assuming placeholder classes) */
        font-size: 1.2em;
        color: #009688;
     }


    /* Header Flex for Score */
    .header-flex {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 15px;
    }

    /* Score Display */
    .score-board {
        font-size: 1.2em;
        font-weight: bold;
        color: #00796b;
        background-color: #e0f2f1; /* Light teal background */
        padding: 8px 15px;
        border-radius: 20px;
        min-width: 100px; /* Give it a fixed size */
        text-align: center;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
    }

    .score-board span {
        color: #004d40; /* Darker teal */
    }

    /* Info Text */
    .info-text {
        font-size: 1.1em;
        color: #555;
        margin-bottom: 15px;
        text-align: center;
    }

    /* Buttons - General Style */
    .game-button {
        display: inline-flex; /* Use flex for icon and text */
        align-items: center;
        gap: 8px;
        padding: 12px 25px;
        font-size: 1.1em;
        color: #fff;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }

    .game-button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    .game-button:active {
        transform: translateY(0);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }

    .game-button:disabled {
        opacity: 0.6;
        cursor: not-allowed;
        transform: none;
        box-shadow: none;
    }

    /* Specific Button Styles */
    .play-button {
        background-color: #4caf50; /* Green */
        display: block; /* Center it */
        margin: 15px auto;
    }

    .play-button:hover:not(:disabled) {
        background-color: #388e3c; /* Darker green */
    }

     .play-button.playing {
        background-color: #ff9800; /* Orange while playing */
     }

    .restart-button {
         background-color: #03a9f4; /* Light blue */
         margin-top: 20px;
    }

    .restart-button:hover:not(:disabled) {
         background-color: #0288d1; /* Darker blue */
    }

    #explanation-toggle {
        display: block;
        width: fit-content;
        margin: 30px auto; /* Add space */
        padding: 10px 20px;
        font-size: 1em;
        color: #fff;
        background-color: #795548; /* Brown */
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease;
         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }

    #explanation-toggle:hover {
        background-color: #5d4037; /* Darker brown */
        transform: translateY(-1px);
         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
     #explanation-toggle:active {
        transform: translateY(0);
         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
     }


    /* Audio Player Area */
    .audio-player-area {
         text-align: center;
         margin-bottom: 25px;
         position: relative; /* Needed for indicator positioning */
    }

     /* Simple visual indicator while playing */
    .audio-indicator {
        height: 4px;
        background-color: #ffeb3b; /* Yellow */
        width: 0%;
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0; /* Span full width */
        margin: 0 auto;
        transition: width linear; /* Smooth progress */
        display: none; /* Hide initially */
    }
     .audio-player-area.playing .audio-indicator {
         display: block;
     }


    /* Options Grid */
    .options-grid {
        display: grid; /* Use CSS Grid */
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); /* Responsive grid */
        gap: 20px; /* Space between options */
        margin-top: 25px;
        justify-items: center; /* Center items in grid cells */
    }

    /* Individual Option */
    .option {
        background-color: #e0f7fa; /* Light cyan */
        border: 1px solid #b2ebf2; /* Matching border */
        border-radius: 8px;
        padding: 15px;
        width: 100%; /* Take full width of grid cell */
        max-width: 200px; /* Max width for large screens */
        text-align: center;
        cursor: pointer;
        transition: transform 0.2s ease, box-shadow 0.2s ease, background-color 0.3s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        display: flex;
        flex-direction: column;
        justify-content: space-between; /* Push name to bottom */
    }

    .option:hover:not(.disabled):not(.correct):not(.incorrect) {
        transform: translateY(-3px); /* Lift effect on hover */
        box-shadow: 0 5px 10px rgba(0, 0, 0, 0.15);
        background-color: #b2ebf2; /* Slightly darker on hover */
    }

    .option img {
        max-width: 100%;
        height: 130px; /* Fixed height */
        object-fit: cover;
        border-radius: 6px;
        margin-bottom: 12px;
        display: block;
        margin-left: auto;
        margin-right: auto;
         border: 1px solid #ccc; /* Subtle image border */
    }

    .option .bird-name {
        font-weight: bold;
        color: #004d40; /* Dark teal */
        font-size: 1.1em;
    }

    /* Option States */
    .option.correct {
        background-color: #d4edda; /* Light green */
        border-color: #28a745; /* Green */
        box-shadow: 0 0 10px rgba(40, 167, 69, 0.5); /* Green glow */
         pointer-events: none; /* Disable clicks */
         opacity: 1; /* Full opacity */
    }

    .option.incorrect {
        background-color: #f8d7da; /* Light red */
        border-color: #dc3545; /* Red */
        box-shadow: 0 0 10px rgba(220, 53, 69, 0.5); /* Red glow */
         pointer-events: none; /* Disable clicks */
         opacity: 0.7; /* Slightly dim incorrect */
    }

    .option.disabled {
        cursor: not-allowed;
        opacity: 0.5; /* Dim disabled options */
        pointer-events: none; /* Crucial to prevent clicks */
         transform: none; /* Remove hover effect */
         box-shadow: none;
    }

     .options-grid.disabled-options .option:not(.correct):not(.incorrect) {
          opacity: 0.5; /* Dim non-selected options while waiting */
     }


    /* Feedback Area */
    .feedback-section {
        margin-top: 30px;
        padding: 20px;
        border-top: 2px dashed #e0e0e0; /* Visual separator */
        min-height: 80px; /* Reserve more space */
        font-size: 1.1em;
        line-height: 1.6;
        position: relative; /* For potential animations */
         opacity: 0; /* Hide initially */
         transition: opacity 0.5s ease; /* Fade in effect */
    }

    .feedback-section.visible {
        opacity: 1;
    }


    .feedback-correct {
        color: #155724; /* Dark green */
        font-weight: bold;
        margin-bottom: 10px;
    }
     .feedback-correct::before { /* Optional icon */
         content: '\2705 '; /* Checkmark emoji */
         color: #28a745;
     }


    .feedback-incorrect {
        color: #721c24; /* Dark red */
        font-weight: bold;
        margin-bottom: 10px;
    }
     .feedback-incorrect::before { /* Optional icon */
         content: '\274c '; /* Cross emoji */
         color: #dc3545;
     }


    .feedback-fact {
        color: #444;
        font-style: italic;
         margin-top: 10px;
         padding-top: 10px;
         border-top: 1px solid #eee;
    }


    /* End of Game Screen */
    .end-screen {
        text-align: center;
        margin-top: 30px;
        padding: 25px;
        background-color: #e8f5e9; /* Light green background */
        border: 2px solid #4caf50;
        border-radius: 10px;
    }

    .end-screen h2 {
         color: #2e7d32; /* Dark green */
         border-bottom: none;
         margin-bottom: 15px;
         justify-content: center;
    }
     .end-screen h2 i {
        color: #4caf50;
     }


    .final-score-text {
        font-size: 1.3em;
        font-weight: bold;
        color: #1b5e20; /* Very dark green */
        margin-bottom: 20px;
    }

    /* Explanation Section */
    #explanation-section {
        margin-top: 40px; /* More space above */
        padding: 30px;
        border: 1px solid #cfd8dc; /* Light grey blue */
        border-radius: 10px;
        background-color: #eceff1; /* Very light grey blue */
        direction: rtl;
        text-align: right;
        line-height: 1.7;
        color: #455a64; /* Darker grey blue */
        box-shadow: 0 3px 8px rgba(0, 0, 0, 0.08);
    }

    #explanation-section h2 {
        color: #455a64; /* Matching header color */
        border-bottom: 2px solid #78909c;
        padding-bottom: 8px;
        margin-bottom: 20px;
    }

    #explanation-section p {
        margin-bottom: 15px;
    }

    #explanation-section ul {
        list-style: disc inside;
        padding-right: 20px;
        margin-bottom: 15px;
    }

     #explanation-section li {
        margin-bottom: 12px;
     }

    #explanation-section ul ul { /* Nested list */
        list-style: circle inside;
        margin-top: 8px;
        margin-bottom: 8px;
        padding-right: 20px;
    }
     #explanation-section ul ul li {
         margin-bottom: 5px;
         font-size: 0.95em;
         line-height: 1.5;
     }


    /* Placeholder icon styles (replace with actual icon font or SVG) */
    /* You would typically include an icon font library (like Font Awesome) */
    /* For this exercise, these are just visual placeholders */
    .icon-headset::before { content: '🎧'; margin-left: 5px; }
    .icon-play::before { content: '▶️'; margin-left: 5px; }
    .icon-question::before { content: '❓'; margin-left: 5px; }
    .icon-trophy::before { content: '🏆'; margin-left: 5px; }
    .icon-reload::before { content: '🔄'; margin-left: 5px; }


</style>

<button id="explanation-toggle">רוצים לדעת יותר? לחצו להסבר מעמיק</button>

<div id="explanation-section" style="display: none;">
    <h2>מדוע ציפורים שרות, ואיך נזהה את המנגינות שלהן?</h2>
    <p>שירת הציפורים היא הרבה יותר מסתם רקע נעים לצלילי הבוקר. זוהי שפה מורכבת וחיונית בעולם הציפורים, ומקור מידע יקר מפז לכל מי שמתעניין בטבע.</p>
    <ul>
        <li>
            **התזמורת האווירית: למה הן שרות?**
            <p>שירת ציפורים משרתת מגוון מטרות קריטיות להישרדותן ולהצלחתן:
                <ul>
                    <li>**למצוא אהבה:** זכרים רבים שרים כדי למשוך נקבות. שירה מרשימה ומורכבת יכולה להיות הצהרת בריאות וכוח, המאותתת על זכר איכותי.</li>
                    <li>**לשמור על הבית:** השירה משמשת להכרזה על בעלות על טריטוריה ולהרחקת יריבים מאותו מין. היא דרך יעילה למנוע סכסוכים מיותרים.</li>
                    <li>**שיחות יומיומיות:** בנוסף לשירה (המנגינה המורכבת יותר), ציפורים משתמשות גם ב'קריאות' קצרות לתקשורת מהירה - איתור מזון, אזהרה מפני טורפים, שמירה על קשר בתוך הלהקה ועוד.</li>
                </ul>
            </p>
        </li>
        <li>
            **עולם של צלילים:**
            <p>ישנם אלפי מינים של ציפורים בעולם, ולכל אחד מהם "שפת שירה" ייחודית משלו. המגוון עצום: יש שירות פשוטות וקצרות, ויש כאלו שהן סימפוניות של ממש! גם בישראל הקטנה, בהיותה על נתיב נדידה מרכזי, ניתן לשמוע מגוון אדיר של זמרים - מקומיים וחולפים.</p>
        </li>
        <li>
            **להיות בלש צלילים: איך מזהים לפי שירה?**
            <p>זיהוי לפי שירה דורש אימון והקשבה פעילה, אך ישנם מאפיינים מרכזיים שכדאי לשים לב אליהם:
                <ul>
                    <li>**גובה הצליל (Pitch):** האם הצלילים גבוהים ודקים, או נמוכים ועמוקים?</li>
                    <li>**מקצב וקצב (Rhythm & Tempo):** האם השירה מהירה או איטית? אחידה או משתנה? האם יש הפסקות קצרות או ארוכות?</li>
                    <li>**מבנה השירה (Structure):** האם יש חזרות על מוטיב מסוים? האם השירה מחולקת ל"בתים" ברורים? האם היא כוללת שריקות, צקצוקים, גרגורים, או חיקויים?</li>
                    <li>**מורכבות (Complexity):** האם השירה פשוטה ומונוטונית, או עשירה במגוון צלילים ומנגינות?</li>
                    <li>**משך השירה:** כמה זמן נמשכת כל פעם שהציפור שרה?</li>
                </ul>
                ככל שתקשיבו יותר ותנסו לשים לב למאפיינים אלו, כך תשתפר יכולתכם לקשר אותם למינים ספציפיים.
            </p>
        </li>
        <li>
            **אמנים מקומיים: דוגמאות משלנו**
            <p>הירגזי המצוי, למשל, מוכר בשירתו הקצבית והחוזרת, שנשמעת כמו "ציק-ציק-ציק". השחרור מציע מנגינה זורמת ומלודית דמוית חליל. והזמיר המנוקד? הוא אמן חיקויים ושירה מורכבת להפליא.</p>
        </li>
        <li>
            **למה זה חשוב לנו?**
            <p>עבור צפרים, זיהוי לפי שירה הוא כלי חיוני לאיתור ציפורים סמויות או רחוקות. עבור חוקרים ואקולוגים, ניטור שירת ציפורים מסייע במעקב אחר בריאות אוכלוסיות, גילוי מינים חדשים באזור או כאלה שנעלמו, ולהבנת ההשפעה של שינויי סביבה על עולם הציפורים. זוהי גם פשוט דרך נפלאה להתחבר לטבע ברמה עמוקה יותר.</p>
        </li>
    </ul>
    <p>האתגר האינטראקטיבי שלמעלה הוא הזדמנות מצוינת להתחיל לפתח את "האוזן הצפרית" שלכם. בהצלחה!</p>
</div>


<script>
    document.addEventListener('DOMContentLoaded', () => {
        const challenges = [
            {
                id: 1,
                audio: '/assets/audio/nature-melody-identifying-birds-by-song/great-tit.mp3', // Placeholder path
                correctBirdId: 'great-tit',
                options: [
                    { id: 'house-sparrow', name: 'דרור הבית', image: '/assets/images/nature-melody-identifying-birds-by-song/house-sparrow.jpg' }, // Placeholder path
                    { id: 'great-tit', name: 'ירגזי מצוי', image: '/assets/images/nature-melody-identifying-birds-by-song/great-tit.jpg' }, // Placeholder path
                    { id: 'blackbird', name: 'שחרור', image: '/assets/images/nature-melody-identifying-birds-by-song/blackbird.jpg' } // Placeholder path
                ],
                fact: "שירתו הקצבית של הירגזי המצוי היא אחת המוכרות ביותר באזורים מיושבים, נשמעת לרוב כחזרה על צלילים כמו 'ציק-ציק' או 'טווי-טווי', והיא משמשת בעיקר לסימון טריטוריה."
            },
            {
                id: 2,
                audio: '/assets/audio/nature-melody-identifying-birds-by-song/blackbird.mp3', // Placeholder path
                correctBirdId: 'blackbird',
                options: [
                    { id: 'blackbird', name: 'שחרור', image: '/assets/images/nature-melody-identifying-birds-by-song/blackbird.jpg' }, // Placeholder path
                    { id: 'common-kingfisher', name: 'שלדג גמדי', image: '/assets/images/nature-melody-identifying-birds-by-song/common-kingfisher.jpg' }, // Placeholder path
                    { id: 'hoopoe', name: 'דוכיפת', image: '/assets/images/nature-melody-identifying-birds-by-song/hoopoe.jpg' } // Placeholder path
                ],
                fact: "שירת השחרור היא מלודית, עשירה ודמוית חליל, עם מגוון רחב של צלילים וטונים משתנים. לרוב שומעים אותה מעמדות תצפית בולטות, כמו קצה עץ או גג."
            },
             {
                id: 3,
                audio: '/assets/audio/nature-melody-identifying-birds-by-song/house-sparrow.mp3', // Placeholder path
                correctBirdId: 'house-sparrow',
                options: [
                    { id: 'european-starling', name: 'זרזיר מצוי', image: '/assets/images/nature-melody-identifying-birds-by-song/european-starling.jpg' }, // Placeholder path
                    { id: 'house-sparrow', name: 'דרור הבית', image: '/assets/images/nature-melody-identifying-birds-by-song/house-sparrow.jpg' }, // Placeholder path
                    { id: 'palestinian-sunbird', name: 'צופית בוהקת', image: '/assets/images/nature-melody-identifying-birds-by-song/palestinian-sunbird.jpg' } // Placeholder path
                ],
                fact: "הדרור הוא סמל לחיים עירוניים וחקלאיים. קולותיו אינם שירה מורכבת, אלא בעיקר ציוצים פשוטים, קצרים וחוזרים ('צירפ') המשמשים לתקשורת בתוך הלהקה ולשמירה על קשר."
            },
             {
                id: 4,
                audio: '/assets/audio/nature-melody-identifying-birds-by-song/palestinian-sunbird.mp3', // Placeholder path
                correctBirdId: 'palestinian-sunbird',
                options: [
                    { id: 'great-tit', name: 'ירגזי מצוי', image: '/assets/images/nature-melody-identifying-birds-by-song/great-tit.jpg' }, // Placeholder path
                    { id: 'house-sparrow', name: 'דרור הבית', image: '/assets/images/nature-melody-identifying-birds-by-song/house-sparrow.jpg' }, // Placeholder path
                    { id: 'palestinian-sunbird', name: 'צופית בוהקת', image: '/assets/images/nature-melody-identifying-birds-by-song/palestinian-sunbird.jpg' } // Placeholder path
                ],
                fact: "הצופית הבוהקת, עם צבעיה המרהיבים, משמיעה שירה מהירה, גבוהה וצייצנית, המורכבת ממגוון רחב של צלילים ולעיתים גם חיקויים של ציפורים אחרות."
            }
        ];

        let currentChallengeIndex = 0;
        let score = 0;
        const audioPlayer = document.getElementById('bird-audio');
        const playSoundBtn = document.getElementById('play-sound-btn');
        const optionsListDiv = document.getElementById('options-list');
        const feedbackArea = document.getElementById('feedback-area');
        const scoreDisplay = document.getElementById('current-score');
        const totalChallengesDisplay = document.getElementById('total-challenges');
        const endOfGameDiv = document.getElementById('end-of-game');
        const finalScoreP = document.getElementById('final-score');
        const challengeInfoP = document.getElementById('challenge-info');
        const audioPlayerArea = document.querySelector('.audio-player-area');
        const audioIndicator = document.querySelector('.audio-indicator');


        const explanationToggleBtn = document.getElementById('explanation-toggle');
        const explanationSection = document.getElementById('explanation-section');

        // Explanation toggle functionality
        explanationToggleBtn.addEventListener('click', () => {
            const isHidden = explanationSection.style.display === 'none';
            explanationSection.style.display = isHidden ? 'block' : 'none';
            explanationToggleBtn.textContent = isHidden ? 'הסתר הסבר' : 'רוצים לדעת יותר? לחצו להסבר מעמיק';
        });


        function loadChallenge(index) {
            // Hide feedback and end screen initially for the new challenge
            feedbackArea.classList.remove('visible');
            feedbackArea.innerHTML = '';
            endOfGameDiv.style.display = 'none';

            if (index >= challenges.length) {
                endGame();
                return;
            }

            const challenge = challenges[index];
            audioPlayer.src = challenge.audio;

            optionsListDiv.innerHTML = ''; // Clear previous options
            optionsListDiv.classList.remove('disabled-options'); // Ensure options are enabled for the new challenge

            challengeInfoP.textContent = 'לחצו על כפתור ההשמעה והקשיבו היטב:';
            playSoundBtn.style.display = 'block';
            playSoundBtn.disabled = false; // Enable play button for the new challenge
             playSoundBtn.classList.remove('playing'); // Remove playing state class
             audioPlayerArea.classList.remove('playing'); // Remove container playing state

            scoreDisplay.textContent = score;
            totalChallengesDisplay.textContent = challenges.length;

            // Use a slight delay before showing options to imply flow
             // This part might need adjustment based on desired flow (show options immediately vs after first play)
             // Let's show options immediately but guide user to play sound first
             challenge.options.forEach(option => {
                 const optionDiv = document.createElement('div');
                 optionDiv.classList.add('option');
                 optionDiv.innerHTML = `
                     <img src="${option.image}" alt="${option.name}">
                     <div class="bird-name">${option.name}</div>
                 `;
                 optionDiv.dataset.birdId = option.id;
                 // Attach click listener ONLY when the challenge is ready
                 optionDiv.addEventListener('click', handleOptionClick);
                 optionsListDiv.appendChild(optionDiv);
             });
        }

        function handleOptionClick(event) {
            // Prevent multiple clicks on options within the same challenge
            if (optionsListDiv.classList.contains('disabled-options')) {
                return;
            }
            optionsListDiv.classList.add('disabled-options'); // Disable further clicks on all options container


            const selectedOption = event.currentTarget;
            const selectedBirdId = selectedOption.dataset.birdId;
            const currentChallenge = challenges[currentChallengeIndex];

            // Immediately disable clicks on all options to prevent changing answer
             optionsListDiv.querySelectorAll('.option').forEach(opt => {
                 opt.removeEventListener('click', handleOptionClick); // Remove listener
                 opt.classList.add('disabled'); // Add disabled visual state
             });

            // Stop the audio if it's playing
            audioPlayer.pause();
            audioPlayer.currentTime = 0; // Reset audio
            playSoundBtn.classList.remove('playing'); // Remove playing state
            audioPlayerArea.classList.remove('playing');


            // Process the selection
            if (selectedBirdId === currentChallenge.correctBirdId) {
                score++;
                selectedOption.classList.remove('disabled'); // Remove disabled state for the selected one
                selectedOption.classList.add('correct');
                feedbackArea.innerHTML = `<p class="feedback-correct">כל הכבוד! זיהיתם נכון!</p><p class="feedback-fact">${currentChallenge.fact}</p>`;
            } else {
                selectedOption.classList.remove('disabled'); // Remove disabled state for the selected one
                selectedOption.classList.add('incorrect');
                // Highlight the correct answer as well
                const correctOption = optionsListDiv.querySelector(`[data-bird-id="${currentChallenge.correctBirdId}"]`);
                if(correctOption) {
                     correctOption.classList.remove('disabled'); // Remove disabled state for the correct one
                     correctOption.classList.add('correct');
                }
                 feedbackArea.innerHTML = `<p class="feedback-incorrect">אופס! זוהי שירת ${findBirdNameById(currentChallenge.correctBirdId, currentChallenge.options)}.</p><p class="feedback-fact">${currentChallenge.fact}</p>`;
            }

            scoreDisplay.textContent = score;
            feedbackArea.classList.add('visible'); // Make feedback visible with transition

            // Move to next challenge after a short delay
            setTimeout(() => {
                 currentChallengeIndex++;
                 loadChallenge(currentChallengeIndex);
            }, 4000); // Wait 4 seconds to allow feedback reading
        }

        function findBirdNameById(id, options) {
            const option = options.find(opt => opt.id === id);
            return option ? option.name : 'ציפור לא ידועה';
        }

        function endGame() {
            document.getElementById('challenge-area').style.display = 'none';
            document.getElementById('options-area').style.display = 'none';
             feedbackArea.classList.remove('visible'); // Hide feedback
            feedbackArea.style.display = 'none'; // Ensure it's hidden structurally
            endOfGameDiv.style.display = 'block'; // Show end screen
            finalScoreP.textContent = `הניקוד הסופי שלכם: ${score} מתוך ${challenges.length}.`;
        }

        window.restartGame = function() {
             currentChallengeIndex = 0;
             score = 0;
             document.getElementById('challenge-area').style.display = 'block';
             document.getElementById('options-area').style.display = 'block';
             feedbackArea.style.display = 'block'; // Make feedback area available again
             endOfGameDiv.style.display = 'none';
             loadChallenge(currentChallengeIndex);
        }


        // Initial load
        totalChallengesDisplay.textContent = challenges.length;
        loadChallenge(currentChallengeIndex);

        // Event listener for play button
        playSoundBtn.addEventListener('click', () => {
             if (audioPlayer.paused) {
                audioPlayer.play();
                playSoundBtn.classList.add('playing'); // Add playing state class
                audioPlayerArea.classList.add('playing'); // Add container playing state
                challengeInfoP.textContent = 'מקשיבים לשירה...';

                 // Update indicator width during playback
                audioPlayer.addEventListener('timeupdate', updateAudioIndicator);

                audioPlayer.onended = () => {
                   playSoundBtn.classList.remove('playing'); // Remove playing state
                   audioPlayerArea.classList.remove('playing');
                   challengeInfoP.textContent = 'הקשב לשירה ובחר את הציפור המתאימה:';
                   audioPlayer.removeEventListener('timeupdate', updateAudioIndicator);
                   audioIndicator.style.width = '0%'; // Reset indicator
               };

             } else {
                 audioPlayer.pause();
                 playSoundBtn.classList.remove('playing'); // Remove playing state
                 audioPlayerArea.classList.remove('playing');
                 challengeInfoP.textContent = 'השמע הופסק. לחצו שוב להמשך או להשמעה מחודשת.';
                 audioPlayer.removeEventListener('timeupdate', updateAudioIndicator);
             }
        });

        // Function to update the audio indicator width
        function updateAudioIndicator() {
            const percentage = (audioPlayer.currentTime / audioPlayer.duration) * 100;
            audioIndicator.style.width = percentage + '%';
        }


         // Handle cases where audio fails to load
        audioPlayer.onerror = () => {
            console.error("Error loading audio file for challenge", currentChallengeIndex);
            feedbackArea.innerHTML = '<p class="feedback-incorrect">שגיאה בטעינת קובץ השירה. לא ניתן להמשיך.</p>';
             feedbackArea.classList.add('visible');
            playSoundBtn.disabled = true;
            optionsListDiv.classList.add('disabled-options'); // Disable options if audio fails
            optionsListDiv.querySelectorAll('.option').forEach(opt => opt.classList.add('disabled'));
        };

         // Handle audio readiness - enable play button only when audio is playable
         audioPlayer.oncanplaythrough = () => {
             playSoundBtn.disabled = false;
         };

         // Initially disable play button until audio is ready
         playSoundBtn.disabled = true;
    });
</script>
```