---
title: "מסע בזמן: זיהוי סגנונות אדריכליים"
english_slug: architecture-style-identification-game
category: "אדריכלות"
tags: ["אדריכלות", "סגנונות אדריכליים", "היסטוריה של האדריכלות", "אמנות", "תרבות", "משחק", "אינטראקטיבי"]
---
# מסע בזמן אדריכלי: האתגר הגדול

הסתכלו סביבכם - בכל פינה בעולם, מבנים עומדים כעדי ראייה מהעבר, כל אחד מספר סיפור על התקופה בה קם, על הידיים שיצרו אותו, ועל הרעיונות שעיצבו עולמות. האם יש לכם את העין החדה לזהות את טביעת האצבע הייחודית של כל סגנון אדריכלי? בואו נצא למסע מרתק בזמן ובמרחב ונראה אם תצליחו לפענח את שפת האבן והבטון!

<div class="architecture-game">
    <div class="game-area">
        <div class="stats-container">
            <div id="progress" class="game-stat">שאלה: 1 / 6</div>
            <div id="score" class="game-stat">ניקוד: 0</div>
        </div>
        <div class="image-container">
            <img id="game-image" src="" alt="מבנה אדריכלי לזיהוי">
            <div class="image-overlay"></div> <!-- For transition effect -->
        </div>
        <div id="style-buttons" class="buttons-container">
            <button class="style-button" data-style="גותי">גותי</button>
            <button class="style-button" data-style="בארוק">בארוק</button>
            <button class="style-button" data-style="מודרניסטי">מודרניסטי</button>
        </div>
        <div id="feedback" class="feedback-area">
            הסתכלו היטב על התמונה ובחרו את הסגנון האדריכלי המתאים מבין האפשרויות. בהצלחה!
        </div>
    </div>
    <div id="end-game-message" class="end-game-message" style="display: none;">
        <h2>המסע הסתיים!</h2>
        <p id="final-score">הניקוד הסופי שלך: 0</p>
        <p>מקווים שנהניתם מהמסע אל עולם סגנונות האדריכלות. המשיכו לחקור ולגלות עוד!</p>
        <button id="restart-game" class="style-button">שחק שוב?</button>
    </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    :root {
        --primary-color: #4A90E2; /* A nice blue */
        --secondary-color: #50E3C2; /* A teal accent */
        --background-color: #F8F9FA; /* Light grey background */
        --card-background: #FFFFFF; /* White card background */
        --text-color: #333; /* Dark grey text */
        --border-color: #E0E0E0; /* Light grey border */
        --correct-color: #7ED321; /* Green */
        --incorrect-color: #D0021B; /* Red */
        --shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        --transition-duration: 0.4s;
    }

    body {
        font-family: 'Heebo', sans-serif;
        line-height: 1.6;
        color: var(--text-color);
        background-color: var(--background-color);
        padding: 20px;
        direction: rtl;
        text-align: right;
    }

    h1, h2, h3 {
        color: var(--primary-color);
        text-align: center;
        margin-bottom: 20px;
    }

    .architecture-game {
        max-width: 700px;
        margin: 20px auto;
        padding: 20px;
        background-color: var(--card-background);
        border-radius: 12px;
        box-shadow: var(--shadow);
        text-align: center;
        overflow: hidden; /* Needed for image transitions */
    }

    .game-area {
        /* Flex or grid can be used here for layout if needed */
    }

    .stats-container {
        display: flex;
        justify-content: space-between;
        margin-bottom: 20px;
        font-size: 1.1rem;
        font-weight: bold;
        color: #555;
    }

    .game-stat {
        padding: 5px 10px;
        background-color: #eee;
        border-radius: 6px;
    }


    .image-container {
        margin-bottom: 20px;
        border-radius: 8px;
        overflow: hidden; /* Prevents shadow/border issues with rounded corners */
        position: relative; /* For overlay positioning */
        box-shadow: 0 2px 6px rgba(0,0,0,0.15);
        background-color: #ccc; /* Placeholder color during load/transition */
    }

    #game-image {
        display: block; /* Removes extra space below image */
        max-width: 100%;
        height: auto;
        transition: opacity var(--transition-duration) ease-in-out;
        opacity: 1; /* Start fully visible */
    }

     .image-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(255, 255, 255, 0); /* Initially transparent */
        transition: background-color var(--transition-duration) ease-in-out;
        pointer-events: none; /* Allow clicks on elements below */
    }


    .buttons-container {
        display: flex;
        justify-content: center;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
        gap: 10px; /* Space between buttons */
        margin-bottom: 20px;
    }

    .style-button {
        padding: 12px 24px;
        font-size: 1.1rem;
        cursor: pointer;
        border: none; /* Remove default border */
        border-radius: 25px; /* Pill shape */
        background-color: var(--primary-color);
        color: white;
        transition: background-color var(--transition-duration) ease, transform 0.1s ease;
        font-weight: bold;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }

    .style-button:hover:not(:disabled) {
        background-color: #3A7ACC; /* Darker shade of primary */
        box-shadow: 0 3px 6px rgba(0,0,0,0.3);
    }

    .style-button:active:not(:disabled) {
        transform: scale(0.98); /* Slightly shrink on press */
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }

    .style-button:disabled {
        opacity: 0.6;
        cursor: not-allowed;
        box-shadow: none;
    }

    .feedback-area {
        margin-top: 10px; /* Reduced margin */
        padding: 15px;
        min-height: 2.5em; /* Ensure enough space for text */
        border-radius: 8px;
        font-size: 1.2rem;
        font-weight: bold;
        text-align: center;
        opacity: 0; /* Start hidden */
        transform: translateY(10px); /* Start slightly lower */
        transition: opacity var(--transition-duration) ease, transform var(--transition-duration) ease, background-color var(--transition-duration) ease, color var(--transition-duration) ease;
    }

    .feedback-visible {
        opacity: 1;
        transform: translateY(0);
    }

    .feedback-correct {
        background-color: var(--correct-color);
        color: white;
        box-shadow: 0 2px 5px rgba(0, 128, 0, 0.3);
    }

    .feedback-incorrect {
        background-color: var(--incorrect-color);
        color: white;
         box-shadow: 0 2px 5px rgba(128, 0, 0, 0.3);
    }

    #toggle-explanation {
        display: block;
        width: fit-content;
        margin: 30px auto 20px auto; /* More space around */
        padding: 12px 24px;
        font-size: 1.1rem;
        cursor: pointer;
        border: none;
        border-radius: 25px;
        background-color: #6c757d; /* Grey */
        color: white;
        transition: background-color var(--transition-duration) ease, transform 0.1s ease;
        font-weight: bold;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    #toggle-explanation:hover {
        background-color: #5a6268;
        box-shadow: 0 3px 6px rgba(0,0,0,0.15);
    }
     #toggle-explanation:active {
        transform: scale(0.98);
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }


    #explanation-section {
        margin-top: 30px;
        padding: 20px;
        border-radius: 12px;
        background-color: var(--card-background);
        box-shadow: var(--shadow);
        direction: rtl;
        text-align: right;
        display: none; /* Initially hidden */
    }

    #explanation-section h2 {
         color: var(--primary-color);
         text-align: center;
         margin-bottom: 20px;
         font-size: 1.8rem;
    }

    #explanation-section h3 {
        color: #555; /* Slightly softer color for subheadings */
        margin-top: 20px;
        margin-bottom: 10px;
        font-size: 1.4rem;
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 5px;
    }

    #explanation-section h4 {
        color: #666;
        margin-top: 15px;
        margin-bottom: 8px;
        font-size: 1.2rem;
    }

    #explanation-section p, #explanation-section ul {
        line-height: 1.7;
        margin-bottom: 15px;
    }

    #explanation-section ul {
        padding-right: 25px; /* Indent list items for RTL */
        list-style-type: disc; /* Use discs for list items */
    }

    #explanation-section li {
        margin-bottom: 8px;
    }

    .end-game-message {
        padding: 30px 20px;
        text-align: center;
        font-size: 1.3rem;
    }

    .end-game-message h2 {
        margin-bottom: 15px;
        font-size: 2rem;
        color: var(--secondary-color); /* Use accent color for end message */
    }

    .end-game-message p {
        margin-bottom: 20px;
    }

    #restart-game {
       margin-top: 15px;
       background-color: var(--secondary-color);
       color: var(--text-color); /* Dark text on light teal */
    }
     #restart-game:hover {
       background-color: #40C0A7;
    }


</style>

<button id="toggle-explanation">הצג/הסתר מדריך סגנונות</button>

<div id="explanation-section">
    <h2>מדריך סגנונות אדריכליים: הכירו את השחקנים הראשיים</h2>

    <h3>פענוח שפת הבניינים: מבוא לסגנונות</h3>
    <p>כל סגנון אדריכלי הוא כמו פרק בספר ההיסטוריה האנושית. הוא משקף לא רק טכניקות בנייה, אלא גם אמונות, ערכים, טכנולוגיות ותפיסות עולם של תקופתו. זיהוי סגנונות מאפשר לנו לחבר את הנקודות בין העבר להווה, להבין למה מבנים נראים כפי שהם, ולהעריך את היופי והתחכום שבהם בהקשרם התרבותי וההיסטורי.</p>

    <h3>הסגנון הגותי: שאיפה לשמיים (מאות 12-16)</h3>
    <p>נולד בצרפת של ימי הביניים, הסגנון הגותי התמקד בהגעה לגבהים חסרי תקדים, כסמל לשאיפה רוחנית וקרבה לאלוהים. דמיינו יער של אבן המטפס מעלה.</p>
    <h4>מאפיינים בולטים:</h4>
    <ul>
        <li>**אנכיות קיצונית:** קווים ישרים וגבוהים שמושכים את העין למעלה.</li>
        <li>**קשתות מחודדות (קשתות צלעות):** יעילות מבנית שאפשרה בנייה גבוהה יותר ושימוש בפחות חומר. יוצרות תחושת קלילות ואנכיות.</li>
        <li>**תמיכות דואות (Flying Buttresses):** "זרועות" אבן חיצוניות שתומכות בקירות הגבוהים ומאפשרות חלונות עצומים.</li>
        <li>**חלונות ויטראז' ענקיים:** מכניסים אור צבעוני ומיסטי, לעיתים קרובות עם סיפורים מצוירים. חלונות רוזטה עגולים ומורכבים.</li>
        <li>**גרגוילים:** פסלי מפלצות משונות ששימשו גם כמרזבים, ומוסיפים נופך דרמטי ומסתורי.</li>
    </ul>

    <h3>סגנון הבארוק: דרמה, תנועה ופאר (מאות 17-18)</h3>
    <p>התפתח באיטליה והתפשט באירופה, הבארוק הוא ההפך המוחלט מהריסון. הוא נועד להרשים, לרגש ולעורר יראת כבוד באמצעות עושר ויזואלי ותחושת תנועה בלתי פוסקת.</p>
    <h4>מאפיינים בולטים:</h4>
    <ul>
        <li>**עקומות ופיתולים:** קירות, עמודים ורכיבים אדריכליים אינם ישרים, אלא גליים ומעוקלים.</li>
        <li>**קישוטיות מוגזמת:** שפע של פסלים, תבליטים, זהב, ציורים ופרטים דקורטיביים מורכבים.</li>
        <li>**משחק אור וצל (קייארוסקורו):** שימוש דרמטי בניגודים בין אזורים מוארים למוצללים ליצירת עומק ותחושת תנועה.</li>
        <li>**אשליות אופטיות:** ציורי תקרה שיוצרים אשליה של שמיים פתוחים או המשכיות של החלל האדריכלי.</li>
        <li>**קנה מידה גרנדיוזי:** מבנים ענקיים ומרשימים (ארמונות, כיכרות, כנסיות).</li>
    </ul>

    <h3>הסגנון המודרניסטי: פונקציה לפני הכל (מאה 20 ואילך)</h3>
    <p>צמח מתוך המהפכה התעשייתית ורוח המאה ה-20, המודרניזם ביקש להתנתק מהעבר ולחפש אמת חדשה באדריכלות - אמת פונקציונלית, יעילה, ונקייה מקישוטים מיותרים.</p>
    <h4>מאפיינים בולטים:</h4>
    <ul>
        <li>**פונקציונליזם:** העיצוב נובע ישירות מהשימוש והצורך. "הצורה בעקבות הפונקציה".</li>
        <li>**מינימליזם:** היעדר כמעט מוחלט של קישוטים. קווים נקיים, ישרים וצורות גאומטריות פשוטות.</li>
        <li>**חומרים חדשים:** שימוש נרחב וגלוי בבטון מזוין, פלדה וזכוכית.</li>
        <li>**חללים פתוחים (Open Plan):** תכנון פנימי גמיש ופתוח הודות לשימוש בעמודים במקום קירות נושאים.</li>
        <li>**חזית חופשית וחלונות סרט:** קירות חיצוניים שאינם נושאים משקל מאפשרים גמישות בעיצוב החזית ושימוש בחלונות אופקיים ארוכים.</li>
    </ul>

    <h3>לסיכום: למה ללמוד סגנונות?</h3>
    <p>הבנת הסגנונות הללו היא מפתח לפתיחת הסיפורים שמבנים מספרים. אמנם בעולם האמיתי ישנם שילובים וגרסאות מקומיות רבות, אך הכרת העקרונות הבסיסיים תאפשר לכם להביט אחרת על כל בניין שתפגשו במסעותיכם, ולזהות את ה"שפה" האדריכלית שלו.</p>
</div>

<script>
    const images = [
        {
            src: "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/NotreDame_Paris_-_exterior.jpg/800px-NotreDame_Paris_-_exterior.jpg",
            alt: "קתדרלת נוטרדאם פריז",
            style: "גותי",
            feedbackCorrect: "בדיוק! הקשתות המחודדות, התמיכות הדואות ושאיפה לגובה הם הסימנים הברורים לסגנון הגותי. מרשים!",
            feedbackIncorrect: "כמעט! הסתכלו היטב על הקשתות המחודדות והתמיכות המרשימות מבחוץ – אלו סימנים מובהקים של הסגנון הגותי. נסו את התמונה הבאה."
        },
        {
            src: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/St._Peter%27s_Square%2C_Vatican_City.jpg/800px-St._Peter%27s_Square%2C_Vatican_City.jpg",
            alt: "כיכר פטרוס הקדוש, רומא",
            style: "בארוק",
            feedbackCorrect: "מצוין! העקומות הדרמטיות של הקולונדה הענקית והתחושה הגרנדיוזית זועקות בארוק. זוהי אמנות שנועדה להדהים.",
            feedbackIncorrect: "לא לגמרי נכון. הסגנון הבארוקי אוהב דרמה, תנועה וקנה מידה עצום כדי להרשים, בדיוק כמו הכיכר המפורסמת הזו. המשיכו לשאלה הבאה."
        },
        {
            src: "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Villa_Savoye_Poissy.jpg/800px-Villa_Savoye_Poissy.jpg",
            alt: "וילה סבואה, לה קורבוזיה",
            style: "מודרניסטי",
            feedbackCorrect: "בינגו! עמודי הפיילוטיס המרימים את הבית, החלונות הסרטים הארוכים והקווים הנקיים - זהו לב ליבו של המודרניזם האדריכלי. עבודה נהדרת!",
            feedbackIncorrect: "לא הפעם. המודרניזם מתאפיין בקווים נקיים, שימוש בחומרים כמו בטון וזכוכית, והתמקדות בפונקציה, כפי שרואים בוילה אייקונית זו. בואו נראה את השאלה הבאה."
        },
         {
            src: "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Amiens_Cathedral_Nave.jpg/800px-Amiens_Cathedral_Nave.jpg",
            alt: "ספינת קתדרלת אמיין",
            style: "גותי",
            feedbackCorrect: "בדיוק! מבט פנימה מגלה את שיא השאיפה הגותית לגובה ואור, עם קשתות הצלעים המסובכות והקירות המרקיעים שחקים.",
            feedbackIncorrect: "נסו שוב. האנכיות הקיצונית והשימוש בקשתות צלעים בפנים המבנה הם מאפיינים מובהקים של הסגנון הגותי. שימו לב לגבהים המטורפים!"
        },
        {
            src: "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Palace_of_Versailles_Hall_of_Mirrors.jpg/800px-Palace_of_Versailles_Hall_of_Mirrors.jpg",
            alt: "היכל המראות, ורסאי",
            style: "בארוק",
            feedbackCorrect: "יופי! היכל המראות הוא דוגמה מושלמת לבארוק - פאר מוגזם, קישוטיות עשירה ומשחק עם אור ומראות ליצירת אינסוף ותנועה.",
            feedbackIncorrect: "לא הפעם. הסגנון הבארוק אוהב להשתמש בקישוטיות רבה, זהב, מראות ומשחקי אור כדי ליצור תחושת פאר ודרמה. חשבו על ארמונות מלכותיים מהמאה ה-17."
        },
        {
            src: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Mies_van_der_Rohe_Farnsworth_House.jpg/800px-Mies_van_der_Rohe_Farnsworth_House.jpg",
            alt: "בית פרנסוורת', מיס ואן דר רוהה",
            style: "מודרניסטי",
            feedbackCorrect: "כל הכבוד! השקיפות המוחלטת, השימוש המינימליסטי בפלדה וזכוכית, והקווים הישרים לחלוטין - זהו מודרניזם טהור במיטבו. אתם שולטים בזיהוי!",
            feedbackIncorrect: "עוד ניסיון. האדריכלות המודרניסטית מדגישה פונקציונליות, שימוש בחומרים תעשייתיים (כמו זכוכית ופלדה) וקווים נקיים ללא קישוטים. בית זכוכית כזה הוא דוגמה קלאסית."
        }
    ];

    let currentImageIndex = 0;
    let score = 0;
    const totalImages = images.length;

    const gameArea = document.querySelector('.game-area');
    const endGameMessage = document.getElementById('end-game-message');
    const finalScoreDisplay = document.getElementById('final-score');
    const restartButton = document.getElementById('restart-game');


    const gameImage = document.getElementById('game-image');
    const imageContainer = document.querySelector('.image-container');
    const imageOverlay = document.querySelector('.image-overlay');
    const styleButtons = document.getElementById('style-buttons');
    const feedbackArea = document.getElementById('feedback');
    const progressDisplay = document.getElementById('progress');
    const scoreDisplay = document.getElementById('score');

    const explanationSection = document.getElementById('explanation-section');
    const toggleExplanationButton = document.getElementById('toggle-explanation');

    function updateStats() {
        progressDisplay.textContent = `שאלה: ${currentImageIndex + 1} / ${totalImages}`;
        scoreDisplay.textContent = `ניקוד: ${score}`;
    }

    function loadCurrentImage() {
        if (currentImageIndex < totalImages) {
            const currentImage = images[currentImageIndex];

            // Hide current image and feedback with fade
            imageContainer.style.opacity = 0;
            feedbackArea.classList.remove('feedback-visible', 'feedback-correct', 'feedback-incorrect');
            feedbackArea.style.opacity = 0;


            // Use a small delay to allow fade out before changing source
            setTimeout(() => {
                 // Preload next image
                const nextImage = new Image();
                nextImage.onload = () => {
                    // Once loaded, update the game image source
                    gameImage.src = currentImage.src;
                    gameImage.alt = currentImage.alt;

                    // Fade in the new image
                    imageContainer.style.opacity = 1;

                    feedbackArea.textContent = 'הסתכלו היטב על התמונה ובחרו את הסגנון האדריכלי המתאים מבין האפשרויות.';
                    feedbackArea.className = 'feedback-area feedback-visible'; // Show default feedback
                    feedbackArea.style.opacity = 1; // Ensure opacity is reset

                    enableButtons();
                    updateStats();
                };
                nextImage.src = currentImage.src; // Start loading

            }, 400); // Match CSS transition duration


        } else {
            // Game finished
            showEndGameMessage();
        }
    }

     function showEndGameMessage() {
        gameArea.style.display = 'none';
        endGameMessage.style.display = 'block';
        finalScoreDisplay.textContent = `הניקוד הסופי שלך: ${score} מתוך ${totalImages}.`;
     }

     function restartGame() {
        currentImageIndex = 0;
        score = 0;
        gameArea.style.display = 'block';
        endGameMessage.style.display = 'none';
        loadCurrentImage();
     }


    function handleButtonClick(event) {
        const selectedStyle = event.target.dataset.style;
        const currentImage = images[currentImageIndex];
        const correctStyle = currentImage.style;
        const feedbackCorrect = currentImage.feedbackCorrect;
        const feedbackIncorrect = currentImage.feedbackIncorrect;

        disableButtons();

        feedbackArea.classList.remove('feedback-correct', 'feedback-incorrect'); // Reset classes
        feedbackArea.classList.add('feedback-visible'); // Ensure visible

        if (selectedStyle === correctStyle) {
            feedbackArea.textContent = feedbackCorrect;
            feedbackArea.classList.add('feedback-correct');
            score++; // Increment score only on correct answer
        } else {
            feedbackArea.textContent = feedbackIncorrect;
            feedbackArea.classList.add('feedback-incorrect');
        }

        updateStats(); // Update score display immediately after answer


        // Move to the next image after a delay
        setTimeout(() => {
            currentImageIndex++;
            loadCurrentImage(); // This will handle the transition and re-enabling buttons
        }, 3000); // 3 second delay to read feedback
    }

    function enableButtons() {
        styleButtons.querySelectorAll('.style-button').forEach(button => {
            button.disabled = false;
        });
    }

    function disableButtons() {
        styleButtons.querySelectorAll('.style-button').forEach(button => {
            button.disabled = true;
        });
    }

    function toggleExplanation() {
        const isHidden = explanationSection.style.display === 'none' || explanationSection.style.display === '';
        explanationSection.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר מדריך סגנונות' : 'הצג מדריך סגנונות';
    }

    // Add event listeners
    styleButtons.querySelectorAll('.style-button').forEach(button => {
        button.addEventListener('click', handleButtonClick);
    });

    toggleExplanationButton.addEventListener('click', toggleExplanation);
    restartButton.addEventListener('click', restartGame);

    // Initialize the game
    updateStats(); // Set initial stats
    loadCurrentImage(); // Load the first image

</script>
---