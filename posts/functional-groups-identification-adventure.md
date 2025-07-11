---
title: "הרפתקת זיהוי קבוצות פונקציונליות"
english_slug: functional-groups-identification-adventure
category: "כימיה"
tags: [כימיה אורגנית, קבוצות פונקציונליות, לימוד אינטראקטיבי, מולקולות, משחק חינוכי]
---

# הרפתקת זיהוי קבוצות פונקציונליות

צאו למסע מרתק אל עולם הכימיה האורגנית! ממש כמו אבני בניין מיוחדות, קבוצות אטומים מסוימות - הקבוצות הפונקציונליות - הן המפתח להבנת התנהגותן ותכונותיהן של מולקולות. האם תצליחו לזהות אותן? בחנו את עצמכם במגוון מולקולות ותגלו את הסודות החבויים במבנים!

<div id="app-container">
    <div class="molecule-display">
        <img id="molecule-image" src="" alt="מבנה מולקולה" class="molecule-img">
        <div id="highlight-area" class="highlight-area">
             <span id="highlight-text"></span>
        </div>
    </div>
    <div class="controls">
        <p class="question-text">איזו קבוצה פונקציונלית "מסתתרת" במולקולה זו?</p>
        <div class="buttons-grid">
            <button class="group-button" data-group="כהל">כהל (-OH)</button>
            <button class="group-button" data-group="חומצה קרבוקסילית">חומצה קרבוקסילית (-COOH)</button>
            <button class="group-button" data-group="אלדהיד">אלדהיד (-CHO)</button>
            <button class="group-button" data-group="קטון">קטון (>C=O)</button>
            <button class="group-button" data-group="אמין">אמין (-NH₂ / -NH- / -N-)</button>
             <button class="group-button" data-group="אתר">אתר (R-O-R')</button>
             <button class="group-button" data-group="אסטר">אסטר (-COO-)</button>
             <button class="group-button" data-group="אמיד">אמיד (-CONH₂)</button>
        </div>
        <div id="feedback" class="feedback"></div>
        <button id="next-molecule" class="next-button" style="display: none;">המולקולה הבאה ></button>
    </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@400;700&display=swap');

    #app-container {
        font-family: 'Heebo', sans-serif;
        direction: rtl;
        text-align: center;
        padding: 25px;
        background: linear-gradient(145deg, #eef2f7, #dbe5f4); /* Soft gradient background */
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
        max-width: 800px;
        margin: 40px auto;
        display: flex;
        flex-direction: column;
        align-items: center;
        color: #333;
        overflow: hidden; /* Hide potential overflow from animations */
    }

    .molecule-display {
        margin-bottom: 25px;
        min-height: 180px; /* Reserve more space */
        position: relative; /* For highlighting */
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .molecule-img {
        max-width: 95%;
        height: auto;
        border: 2px solid #c0d9ee; /* Softer border */
        border-radius: 10px;
        background-color: #ffffff;
        padding: 15px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
        transition: opacity 0.6s ease-in-out; /* Fade in new images */
        opacity: 1; /* Default state */
    }

     .molecule-img.fade-out {
         opacity: 0;
     }


    .highlight-area {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        pointer-events: none; /* Allow clicks on image below */
        opacity: 0;
        transition: opacity 0.8s ease-in-out;
        z-index: 10; /* Above image */
    }

     .highlight-area.visible {
         opacity: 1;
     }

    #highlight-text {
        font-size: 1.6em; /* Larger highlight text */
        font-weight: bold;
        color: #0d6efd; /* Primary blue */
        background-color: rgba(255, 255, 255, 0.9); /* Semi-transparent background */
        padding: 8px 15px;
        border-radius: 8px;
        border: 2px solid #0d6efd;
        box-shadow: 0 0 15px rgba(13, 109, 253, 0.5); /* Glow effect */
        animation: pulse-glow 1.5s infinite alternate; /* Subtle animation */
    }

     @keyframes pulse-glow {
         0% { box-shadow: 0 0 15px rgba(13, 109, 253, 0.5), 0 0 5px rgba(13, 109, 253, 0.3); }
         100% { box-shadow: 0 0 20px rgba(13, 109, 253, 0.8), 0 0 8px rgba(13, 109, 253, 0.5); }
     }


    .controls {
        width: 100%;
        text-align: center;
    }

    .question-text {
        margin-bottom: 20px;
        font-size: 1.2em;
        color: #1a1a1a; /* Darker text */
        font-weight: bold;
    }

    .buttons-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); /* Adjust min width */
        gap: 12px; /* Slightly larger gap */
        margin-bottom: 25px;
    }

    .group-button {
        padding: 14px 18px; /* More padding */
        border: none;
        border-radius: 8px; /* More rounded */
        cursor: pointer;
        font-size: 1.05em; /* Slightly larger font */
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        background-color: #0d6efd; /* Primary blue */
        color: white;
        box-shadow: 0 4px 10px rgba(13, 109, 253, 0.2);
        will-change: transform, background-color, box-shadow; /* Performance hint */
    }

    .group-button:hover:not(:disabled) {
        background-color: #0b5ed7; /* Darker blue */
        transform: translateY(-3px); /* More pronounced lift */
        box-shadow: 0 6px 15px rgba(13, 109, 253, 0.3);
    }

    .group-button:active:not(:disabled) {
        background-color: #0a58ca; /* Even darker */
        transform: translateY(0);
        box-shadow: 0 2px 5px rgba(13, 109, 253, 0.2);
    }

    .group-button:disabled {
        opacity: 0.6;
        cursor: not-allowed;
        box-shadow: none;
    }

    .group-button.correct {
        background-color: #28a745; /* Green */
        box-shadow: 0 4px 10px rgba(40, 167, 69, 0.3);
        animation: pulse-green 0.6s ease;
    }

    .group-button.wrong {
        background-color: #dc3545; /* Red */
        box-shadow: 0 4px 10px rgba(220, 53, 69, 0.3);
        animation: shake 0.4s ease;
    }

    @keyframes pulse-green {
        0% { transform: scale(1); box-shadow: 0 4px 10px rgba(40, 167, 69, 0.3); }
        50% { transform: scale(1.03); box-shadow: 0 6px 15px rgba(40, 167, 69, 0.4); }
        100% { transform: scale(1); box-shadow: 0 4px 10px rgba(40, 167, 69, 0.3); }
    }

     @keyframes shake {
        0%, 100% { transform: translateX(0); }
        20%, 60% { transform: translateX(-6px); }
        40%, 80% { transform: translateX(6px); }
     }


    .feedback {
        margin-top: 20px;
        min-height: 1.8em; /* Reserve more space */
        font-size: 1.2em; /* Larger font */
        font-weight: bold;
        color: #333;
        opacity: 0; /* Start hidden for animation */
        transition: opacity 0.5s ease-in-out;
    }

    .feedback.visible {
        opacity: 1;
    }

    .feedback.correct {
        color: #28a745; /* Green */
    }

    .feedback.wrong {
        color: #dc3545; /* Red */
    }

    .next-button {
        margin-top: 25px; /* More space */
        padding: 12px 30px; /* Larger padding */
        font-size: 1.1em;
        font-weight: bold;
        background-color: #6c757d; /* Grey */
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        box-shadow: 0 4px 10px rgba(108, 117, 125, 0.2);
        will-change: transform, background-color, box-shadow;
    }

    .next-button:hover {
        background-color: #5a6268;
         transform: translateY(-2px);
         box-shadow: 0 6px 15px rgba(108, 117, 125, 0.3);
    }

    .next-button:active {
        background-color: #545b62;
         transform: translateY(0);
         box-shadow: 0 2px 5px rgba(108, 117, 125, 0.2);
    }


     #show-explanation {
        display: block;
        margin: 40px auto 20px auto; /* Adjust margin */
        padding: 12px 25px;
        font-size: 1.1em;
        font-weight: bold;
        background-color: #17a2b8; /* Teal */
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        box-shadow: 0 4px 10px rgba(23, 162, 184, 0.2);
         will-change: transform, background-color, box-shadow;
    }

    #show-explanation:hover {
        background-color: #138496;
         transform: translateY(-2px);
         box-shadow: 0 6px 15px rgba(23, 162, 184, 0.3);
    }
     #show-explanation:active {
        background-color: #117a8b;
         transform: translateY(0);
         box-shadow: 0 2px 5px rgba(23, 162, 184, 0.2);
    }

    #explanation {
        display: none;
        margin-top: 20px;
        padding: 25px; /* More padding */
        background-color: #e9ecef; /* Light grey */
        border-radius: 10px;
        text-align: right;
        line-height: 1.7; /* Improve readability */
        box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.05); /* Subtle inner shadow */
    }

    #explanation h2 {
        color: #1a1a1a;
        margin-bottom: 20px;
        text-align: center;
        font-size: 1.8em;
        border-bottom: 2px solid #adb5bd; /* Separator line */
        padding-bottom: 10px;
    }

    #explanation p {
        margin-bottom: 18px;
        font-size: 1.05em;
    }

    #explanation strong {
        color: #0056b3;
         font-weight: bold;
    }

     #explanation ul {
         list-style-type: none; /* Remove default list style */
         padding: 0;
         margin-top: 15px;
     }

     #explanation li {
         margin-bottom: 12px;
         padding-right: 15px;
         position: relative; /* For custom bullet */
         text-indent: -15px; /* Align text */
     }

     #explanation li::before {
         content: '•'; /* Custom bullet point */
         color: #007bff; /* Blue bullet */
         font-weight: bold;
         display: inline-block;
         width: 15px;
         margin-right: 5px;
         text-indent: 0;
     }

</style>

<button id="show-explanation">הצג/הסתר מדריך מהיר ></button>

<div id="explanation">
    <h2>פיענוח קבוצות פונקציונליות: המדריך</h2>
    <p>ברוכים הבאים למסע אל לב המולקולות! כל מולקולה אורגנית מורכבת משלד פחמני, אך הקבוצות הפונקציונליות הן אלו שמקנות לה את אופייה הייחודי ואת יכולותיה להגיב.</p>
    <p>הבנתן חיונית לכל מי שמגלה עניין בכימיה אורגנית. הנה מבט מהיר על כמה מהקבוצות שתפגשו:</p>
    <ul>
        <li><strong>כהל (-OH):</strong> קבוצת הידרוקסיל. מולקולות כמו אתנול (הכהל במשקאות) מכילות אותה. מקנה למולקולה תכונות קוטביות ויכולת ליצור קשרי מימן.</li>
        <li><strong>חומצה קרבוקסילית (-COOH):</strong> קבוצת קרבוקסיל, שהיא שילוב של קבוצת קרבוניל (C=O) והידרוקסיל (OH). אלו חומצות חלשות יחסית, כמו חומצה אצטית (חומץ).</li>
        <li><strong>אלדהיד (-CHO):</strong> מכיל קבוצת קרבוניל (C=O) שקשורה לפחמן אחד ולמימן. תמיד נמצא בקצה שרשרת הפחמנים. לדוגמה: פורמאלדהיד.</li>
        <li><strong>קטון (>C=O):</strong> מכיל קבוצת קרבוניל (C=O) שקשורה לשני אטומי פחמן. נמצא בתוך שרשרת הפחמנים, כמו אצטון (מסיר לק).</li>
        <li><strong>אמין (-NH₂, -NH-, או -N-):</strong> מכיל אטום חנקן הקשור לפחמנים ו/או מימנים. אלו בסיסים אורגניים, כמו בסיסים הנמצאים בדנ"א.</li>
        <li><strong>אתר (R-O-R'):</strong> אטום חמצן המקשר בין שתי שרשרות פחמניות (או טבעות). לדוגמה: אתר דיאתילי.</li>
         <li><strong>אסטר (-COO-):</strong> נוצר מתגובה של חומצה קרבוקסילית וכהל. מכיל קבוצת קרבוניל הקשורה לאטום חמצן שמחובר לשרשרת פחמנית נוספת. רבים מהאסטרים בעלי ריחות פירותיים.</li>
         <li><strong>אמיד (-CONH₂):</strong> מכיל קבוצת קרבוניל הקשורה לאטום חנקן. המקשרים החשובים בחלבונים (קשר פפטידי) הם למעשה קשרי אמיד.</li>
    </ul>
    <p>התנסו במשחק, חפשו את הקבוצות הללו ותהפכו למומחים בזיהוי מבנים!</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const moleculeImage = document.getElementById('molecule-image');
        const highlightArea = document.getElementById('highlight-area');
        const highlightTextSpan = document.getElementById('highlight-text');
        const groupButtons = document.querySelectorAll('.group-button');
        const feedbackDiv = document.getElementById('feedback');
        const nextButton = document.getElementById('next-molecule');
        const showExplanationButton = document.getElementById('show-explanation');
        const explanationDiv = document.getElementById('explanation');

        // Array of molecule data with better placeholder descriptions and highlight text
        // In a real app, images would show actual structures, and highlightData might contain coordinates
        const molecules = [
            { img: 'https://via.placeholder.com/350x180?text=Ethanol%20(Alcohol)', correctGroup: 'כהל', highlightText: '-OH' },
            { img: 'https://via.placeholder.com/350x180?text=Ethanoic+Acid%20(Carboxylic%20Acid)', correctGroup: 'חומצה קרבוקסילית', highlightText: '-COOH' },
            { img: 'https://via.placeholder.com/350x180?text=Propanal%20(Aldehyde)', correctGroup: 'אלדהיד', highlightText: '-CHO' },
            { img: 'https://via.placeholder.com/350x180?text=Propanone%20(Ketone)', correctGroup: 'קטון', highlightText: '>C=O' },
            { img: 'https://via.placeholder.com/350x180?text=Ethylamine%20(Amine)', correctGroup: 'אמין', highlightText: '-NH₂' },
            { img: 'https://via.placeholder.com/350x180?text=Diethyl+Ether%20(Ether)', correctGroup: 'אתר', highlightText: 'R-O-R\'' },
            { img: 'https://via.placeholder.com/350x180?text=Methyl+Acetate%20(Ester)', correctGroup: 'אסטר', highlightText: '-COO-' },
            { img: 'https://via.placeholder.com/350x180?text=Acetamide%20(Amide)', correctGroup: 'אמיד', highlightText: '-CONH₂' },
             { img: 'https://via.placeholder.com/350x180?text=Butan-1-ol%20(Alcohol)', correctGroup: 'כהל', highlightText: '-OH' },
             { img: 'https://via.placeholder.com/350x180?text=Butanoic+Acid%20(Carboxylic%20Acid)', correctGroup: 'חומצה קרבוקסילית', highlightText: '-COOH' },
             { img: 'https://via.placeholder.com/350x180?text=Butanone%20(Ketone)', correctGroup: 'קטון', highlightText: '>C=O' },
              { img: 'https://via.placeholder.com/350x180?text=Hexanal%20(Aldehyde)', correctGroup: 'אלדהיד', highlightText: '-CHO' },

        ];

        let currentMoleculeIndex = 0;
        let shuffledMolecules = [];

        function shuffleArray(array) {
            for (let i = array.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [array[i], array[j]] = [array[j], array[i]]; // Swap elements
            }
            return array;
        }

        function startGame() {
             shuffledMolecules = shuffleArray([...molecules]); // Shuffle a copy
             currentMoleculeIndex = 0;
             loadMolecule(currentMoleculeIndex);
        }


        function loadMolecule(index) {
            // Add fade-out class for animation
            moleculeImage.classList.add('fade-out');

            // Wait for fade-out, then change source and fade in
            setTimeout(() => {
                if (index >= shuffledMolecules.length) {
                    // End of game
                    feedbackDiv.textContent = '!🎉 כל הכבוד! סיימת את כל המולקולות 🎉';
                    feedbackDiv.className = 'feedback correct visible'; // Keep feedback visible
                    moleculeImage.style.display = 'none'; // Hide image
                    highlightArea.classList.remove('visible');
                    highlightTextSpan.textContent = '';
                    groupButtons.forEach(button => {
                        button.classList.remove('correct', 'wrong');
                        button.disabled = true;
                    });
                    nextButton.style.display = 'none';
                    // Optionally, add a "Start Over" button
                    return;
                }

                currentMoleculeIndex = index;
                const molecule = shuffledMolecules[currentMoleculeIndex];

                moleculeImage.src = molecule.img;
                moleculeImage.alt = `מבנה מולקולה: ${molecule.correctGroup}`;
                moleculeImage.style.display = 'block'; // Ensure image is visible

                // Remove fade-out and trigger fade-in
                moleculeImage.classList.remove('fade-out');


                feedbackDiv.textContent = '';
                feedbackDiv.className = 'feedback'; // Reset classes
                feedbackDiv.classList.remove('visible'); // Hide feedback

                nextButton.style.display = 'none';
                highlightArea.classList.remove('visible');
                highlightTextSpan.textContent = '';


                groupButtons.forEach(button => {
                    button.disabled = false; // Re-enable buttons
                    button.classList.remove('correct', 'wrong'); // Remove previous feedback classes
                });
            }, 500); // Match CSS transition duration
        }

        function checkAnswer(selectedGroup, clickedButton) {
            // Disable all buttons immediately
            groupButtons.forEach(button => button.disabled = true);

            const correctMolecule = shuffledMolecules[currentMoleculeIndex];
            const correctGroup = correctMolecule.correctGroup;
            const highlightText = correctMolecule.highlightText;

            // Apply feedback class to the specific button clicked
            if (selectedGroup === correctGroup) {
                 clickedButton.classList.add('correct');
                 feedbackDiv.textContent = `מעולה! זיהית נכון! זוהי אכן קבוצת ${correctGroup}.`;
                 feedbackDiv.className = 'feedback correct visible';
                 highlightTextSpan.textContent = highlightText;
                 highlightArea.classList.add('visible'); // Show highlight
            } else {
                 clickedButton.classList.add('wrong');
                 feedbackDiv.textContent = `אופס... זוהי לא קבוצת ${selectedGroup}. נסה שוב או לחץ על 'המולקולה הבאה' לגלות את התשובה.`;
                 feedbackDiv.className = 'feedback wrong visible';
                 // Optionally show correct highlight after wrong answer, but simpler to just show it on correct. Sticking to showing only on correct guess.
            }

             // Always show the next button after the first attempt
            nextButton.style.display = 'block';
        }

        groupButtons.forEach(button => {
            button.addEventListener('click', () => {
                 if (!button.disabled) { // Ensure button is not already disabled
                    checkAnswer(button.getAttribute('data-group'), button);
                 }
            });
        });

        nextButton.addEventListener('click', () => {
             // If the user clicked 'Next' after a wrong answer, show the correct highlight briefly before loading next molecule
             const correctMolecule = shuffledMolecules[currentMoleculeIndex];
             const correctGroup = correctMolecule.correctGroup;

             // Check if the *correct* button was NOT selected
             const correctButtonWasClicked = document.querySelector('.group-button.correct');

             if (!correctButtonWasClicked) {
                 // User answered incorrectly, show the correct answer visually before moving on
                 feedbackDiv.textContent = `הקבוצה הנכונה הייתה: ${correctGroup}.`;
                 feedbackDiv.className = 'feedback visible'; // Neutral feedback state
                  highlightTextSpan.textContent = correctMolecule.highlightText;
                  highlightArea.classList.add('visible'); // Show correct highlight

                 // Wait a moment before loading the next molecule
                 setTimeout(() => {
                     loadMolecule(currentMoleculeIndex + 1);
                 }, 1500); // Show highlight for 1.5 seconds
             } else {
                  // User answered correctly, just load the next molecule
                  loadMolecule(currentMoleculeIndex + 1);
             }
        });

        showExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
            if (isHidden) {
                 explanationDiv.style.display = 'block';
                 showExplanationButton.textContent = 'הסתר מדריך מהיר <';
            } else {
                 explanationDiv.style.display = 'none';
                 showExplanationButton.textContent = 'הצג/הסתר מדריך מהיר >';
            }
        });


        // Initial game start
        startGame();
    });
</script>