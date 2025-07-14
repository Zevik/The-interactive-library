---
title: "המסע המופלא של הסלעים - סימולציה אינטראקטיבית"
english_slug: interactive-rock-cycle-model
category: "גיאולוגיה"
tags:
  - מדע
  - כדור הארץ
  - הדמיה
  - אינטראקטיבי
  - גיאולוגיה
---
<h1>המסע המופלא של הסלעים: סימולציה אינטראקטיבית</h1>

ברוכים הבאים למסע המופלא אל לב כדור הארץ והקרום שלו! הדמיה זו מזמינה אתכם לחקור את מחזור הסלעים הדינמי והמתמשך. גלו כיצד סלע אחד יכול להפוך לסלע מסוג אחר לגמרי, בהשפעת תהליכים עוצמתיים כמו חום, לחץ, בליה והתכה.

**איך משחקים?**
פשוט גררו פיסת סלע מאזור אחד (סוג סלע) לאזור אחר (סוג סלע אחר). צפו באנימציה ובפידבק שיציגו לכם את התהליך הגיאולוגי המתרחש! נסו את כל המעברים האפשריים.

<div id="rock-cycle-container">
    <div class="rock-zone" id="igneous-zone">
        <h2>🔥 סלע יסוד (Igneous)</h2>
        <p class="zone-desc">נוצר מקירור והתגבשות של מאגמה או לבה</p>
        <div class="rock-pieces">
            <div class="rock-piece" draggable="true" data-type="igneous">🌋</div>
            <div class="rock-piece" draggable="true" data-type="igneous">🪨</div>
        </div>
    </div>

    <div class="process-feedback">גררו פיסת סלע בין אזורים כדי לראות את המסע שלה!</div>

    <div class="rock-zone" id="sedimentary-zone">
        <h2>💧 סלע משקע (Sedimentary)</h2>
        <p class="zone-desc">נוצר משקיעה והתקשות של חלקיקי סלע קיימים</p>
         <div class="rock-pieces">
            <div class="rock-piece" draggable="true" data-type="sedimentary">🏖️</div>
            <div class="rock-piece" draggable="true" data-type="sedimentary">🧱</div>
        </div>
    </div>

    <div class="rock-zone" id="metamorphic-zone">
        <h2>⛰️ סלע מטאמורפי (Metamorphic)</h2>
        <p class="zone-desc">סלע שהשתנה עקב חום ולחץ עזים</p>
         <div class="rock-pieces">
            <div class="rock-piece" draggable="true" data-type="metamorphic">💎</div>
            <div class="rock-piece" draggable="true" data-type="metamorphic">🗿</div>
        </div>
    </div>

     <!-- Add visual connectors? Hard to implement with static HTML/CSS -->
     <!-- Let's rely on the drag interaction and feedback -->

</div>

<button id="show-explanation-button">🔍 הצג/הסתר הסבר מדעי מורחב</button>

<div id="explanation" style="display: none;">
    <h2>מחזור הסלעים - ההסבר המדעי המורחב</h2>
    <p>מחזור הסלעים הוא אחד מתהליכי המפתח המעצבים את פני כדור הארץ. זהו תהליך מעגלי ומתמשך, ללא נקודת התחלה או סוף אמיתית, שבו סלעים עוברים שינויים פיזיקליים וכימיים והופכים מסוג אחד למשנהו.</p>
    <ul>
        <li><b>סלע יסוד (Igneous Rocks):</b> סלעים אלו "נולדים" עמוק בתוך כדור הארץ, או על פני השטח בעת התפרצות געשית. הם נוצרים כאשר סלע מותך (מאגמה או לבה) מתקרר ומתגבש. מהירות הקירור משפיעה על גודל הגבישים בסלע. דוגמאות: גרניט, בזלת.</li>
        <li><b>סלע משקע (Sedimentary Rocks):</b> סלעים אלו נוצרים על פני השטח. תהליך הבליה (התפוררות סלעים קיימים עקב רוח, מים, קרח ושינויי טמפרטורה) והסחיפה (הובלת החלקיקים המפוררים ע"י מים, רוח או קרח) יוצרים משקעים (כמו חול, חצץ, בוץ). המשקעים נשקעים בשכבות (לרוב במקווי מים), ולאורך מיליוני שנים עוברים דחיסה והתאחדות (ליתיפיקציה) כתוצאה ממשקל השכבות העליונות והצטברות מינרלים ביניהם. דוגמאות: אבן חול, אבן גיר, קונגלומרט.</li>
        <li><b>סלע מטאמורפי (Metamorphic Rocks):</b> סלעים אלו נוצרים בתנאים של חום ולחץ קיצוניים, לרוב עמוק בתוך קרום כדור הארץ או באזורי התנגשות לוחות טקטוניים. סלע קיים (יסוד, משקע, או אפילו מטאמורפי קודם) אינו נמס, אך המינרלים שבו משתנים או מתארגנים מחדש במבנה חדש. דוגמאות: שיש (מאבן גיר), צפחה (מחרסית או בזלת), גנייס (מגרניט או סלעי משקע).</li>
    </ul>
    <p><b>התהליכים המניעים את המחזור:</b></p>
    <ul>
        <li><b>התכה והתגבשות:</b> סלע (מטאמורפי או משקע) שנקבר עמוק מספיק ונחשף לחום קיצוני יותך למאגמה. המאגמה יכולה להתקרר ולהתגבש לסלע יסוד.</li>
        <li><b>בליה, סחיפה, שקיעה והתאחדות:</b> כל סוג סלע שנחשף על פני השטח יעבור בליה וסחיפה. המשקעים שנוצרו ישקעו ויתאחדו לסלע משקע.</li>
        <li><b>חום ולחץ:</b> כל סוג סלע שנקבר עמוק ונחשף לחום ולחץ גבוהים יעבור התמרה (מטאמורפוזה) ויהפוך לסלע מטאמורפי.</li>
    </ul>
    <p>סימולציה זו מציגה את המעברים העיקריים במחזור. כל גרירה של סלע מאזור אחד לאחר מדמה את אחד התהליכים הגיאולוגיים העוצמתיים הללו.</p>
</div>

<style>
@import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

body {
    font-family: 'Heebo', sans-serif;
    direction: rtl;
    text-align: right;
    background: linear-gradient(to bottom, #f0f8ff, #cce7ff); /* Soft sky gradient */
    padding: 20px;
    color: #333;
    line-height: 1.7;
    margin: 0;
}

h1, h2 {
    color: #4a2c1d; /* Deeper brownish */
    text-align: center;
    margin-bottom: 15px;
    font-weight: 700;
}

h1 {
    font-size: 2.5em;
    margin-top: 0;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
}

h2 {
     font-size: 1.6em;
     color: #5d4037; /* Even deeper */
}

#rock-cycle-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center; /* Center zones */
    align-items: flex-start; /* Align to top within container */
    gap: 40px; /* Increased gap */
    padding: 30px;
    background-color: #ffffff; /* Pure white for contrast */
    border-radius: 20px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2); /* Stronger shadow */
    margin: 30px auto; /* Center block and add margin */
    max-width: 1000px; /* Max width for large screens */
    position: relative;
    min-height: 450px; /* Ensure adequate height */
    overflow: hidden; /* Hide any overflow from animations */
}

.rock-zone {
    width: 280px; /* Wider zones */
    min-height: 300px; /* Taller zones */
    border: 4px dashed #a1887f; /* Earthy dashed border */
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    background-color: #efebe9; /* Light earthy background */
    transition: border-color 0.4s ease-in-out, transform 0.3s ease;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    position: relative; /* For potential absolute positioning inside */
}

.rock-zone.drag-over {
    border-color: #4CAF50; /* Vibrant green */
    transform: scale(1.05); /* Slightly more pronounced scale */
    background-color: #e8f5e9; /* Lighter green tint */
}

.zone-desc {
    font-size: 0.9em;
    color: #5d4037;
    margin-top: -10px; /* Pull description closer to title */
    margin-bottom: 15px;
    font-weight: 300;
}

.rock-pieces {
    display: flex;
    flex-wrap: wrap;
    gap: 15px; /* Increased gap between pieces */
    justify-content: center;
    margin-top: 15px;
    flex-grow: 1; /* Allow pieces container to grow */
    align-content: flex-start; /* Pack pieces to the top */
}


.rock-piece {
    width: 60px; /* Larger pieces */
    height: 60px;
    background: linear-gradient(to bottom right, #795548, #5d4037); /* Earthy gradient */
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 10px; /* Slightly larger radius */
    cursor: grab;
    font-size: 2em; /* Larger emojis */
    box-shadow: 3px 3px 8px rgba(0, 0, 0, 0.4); /* Stronger shadow */
    transition: transform 0.3s ease, opacity 0.3s ease, box-shadow 0.3s ease;
    user-select: none; /* Prevent text selection */
}

.rock-piece:active {
    cursor: grabbing;
    transform: scale(1.15); /* More pronounced scale on active */
    box-shadow: 5px 5px 12px rgba(0, 0, 0, 0.5);
}

/* Animations for dropped pieces */
@keyframes popIn {
    0% { transform: scale(0.5); opacity: 0; }
    80% { transform: scale(1.05); opacity: 1; }
    100% { transform: scale(1); }
}

@keyframes shake {
    0%, 100% { transform: translateX(0); }
    20%, 60% { transform: translateX(-5px); }
    40%, 80% { transform: translateX(5px); }
}

@keyframes melt {
    0% { transform: scale(1); opacity: 1; }
    100% { transform: scale(0.8) translateY(10px); opacity: 0.5; } /* Simulate melting/sinking */
}

@keyframes breakApart {
     0% { transform: scale(1); opacity: 1; }
     50% { transform: scale(1.1); opacity: 0.8; }
     100% { transform: scale(0.9); opacity: 0; } /* Simple fade out */
}


.rock-piece.animate-pop { animation: popIn 0.5s ease-out; }
.rock-piece.animate-shake { animation: shake 0.6s ease-in-out; }
.rock-piece.animate-melt { animation: melt 0.8s ease-out forwards; } /* forwards to keep end state */
.rock-piece.animate-break { animation: breakApart 0.8s ease-out forwards; }


.process-feedback {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: rgba(0, 0, 0, 0.85); /* Darker, more prominent */
    color: white;
    padding: 20px 30px; /* More padding */
    border-radius: 10px; /* Rounded corners */
    font-size: 1.3em; /* Larger font */
    font-weight: 700;
    text-align: center;
    min-width: 250px;
    z-index: 100; /* Ensure on top */
    opacity: 0; /* Start hidden */
    pointer-events: none;
    transition: opacity 0.6s ease-in-out; /* Slower fade */
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
}

#show-explanation-button {
    display: block;
    margin: 30px auto; /* More vertical margin */
    padding: 14px 30px; /* More padding */
    font-size: 1.1em;
    cursor: pointer;
    background-color: #1a73e8; /* Google Blue for a modern feel */
    color: white;
    border: none;
    border-radius: 8px; /* More rounded */
    transition: background-color 0.3s ease, transform 0.1s ease;
    font-weight: 700;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

#show-explanation-button:hover {
    background-color: #1558b8; /* Darker blue */
    transform: translateY(-2px); /* Slight lift effect */
}

#show-explanation-button:active {
     transform: translateY(0); /* Press effect */
     box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
}

#explanation {
    background-color: #e3f2fd; /* Light blue tint */
    padding: 25px; /* More padding */
    border-radius: 15px; /* More rounded */
    margin-top: 25px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    border-right: 5px solid #1a73e8; /* Accent border */
}

#explanation h2 {
    color: #0d47a1; /* Darker blue */
    margin-top: 0;
    border-bottom: 2px solid #1a73e8; /* Underline heading */
    padding-bottom: 10px;
}

#explanation p, #explanation li {
    font-size: 1em;
    color: #333;
    margin-bottom: 15px;
    line-height: 1.8;
}

#explanation ul {
    list-style: none; /* Remove default bullets */
    padding: 0;
    margin-right: 0; /* Reset margin */
}

#explanation li {
    margin-bottom: 15px;
    position: relative;
    padding-right: 25px; /* Space for custom bullet */
}

#explanation li::before {
    content: '•'; /* Custom bullet point */
    color: #1a73e8; /* Blue color */
    font-weight: bold;
    display: inline-block;
    position: absolute;
    right: 0;
    top: 0;
}

#explanation b {
    color: #0d47a1; /* Dark blue for bold text */
}

/* Basic responsiveness */
@media (max-width: 900px) {
    #rock-cycle-container {
        flex-direction: column;
        align-items: center;
        min-height: auto;
        gap: 25px; /* Smaller gap on mobile */
        padding: 20px;
    }
    .rock-zone {
        width: 90%; /* Wider zones on smaller screens */
        min-height: 250px; /* Adjust height */
        padding: 15px;
    }
    .process-feedback {
        position: static; /* Static position on small screens */
        transform: none;
        margin-top: 20px;
        margin-bottom: 10px;
        opacity: 1; /* Always visible or handle visibility differently */
        background-color: #fff; /* Lighter background */
        color: #333;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        font-size: 1.1em;
        padding: 15px;
        min-width: auto;
        width: 90%;
    }
     h1 { font-size: 2em; }
     h2 { font-size: 1.4em; }
     .rock-piece { width: 55px; height: 55px; font-size: 1.8em; }
     #show-explanation-button { font-size: 1em; padding: 10px 20px; }
     #explanation { padding: 20px; }
     #explanation p, #explanation li { font-size: 0.95em; }

}

</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const rockZones = document.querySelectorAll('.rock-zone');
    const rockPieces = document.querySelectorAll('.rock-piece');
    const feedbackDisplay = document.querySelector('.process-feedback');
    const explanationButton = document.getElementById('show-explanation-button');
    const explanationDiv = document.getElementById('explanation');

    // Mapping of transitions to process descriptions and new emojis
    const processMap = {
        'igneous-to-sedimentary': { text: 'בליה, סחיפה והתאחדות - הופך לסלע משקע!', emoji: '🧱', animation: 'animate-break' },
        'sedimentary-to-metamorphic': { text: 'חום ולחץ עזים - הופך לסלע מטאמורפי!', emoji: '💎', animation: 'animate-shake' },
        'metamorphic-to-igneous': { text: 'התכה והתגבשות - הופך לסלע יסוד!', emoji: '🌋', animation: 'animate-melt' },

        // Other possible transitions
        'igneous-to-metamorphic': { text: 'חום ולחץ משנים אותו - הופך לסלע מטאמורפי!', emoji: '🗿', animation: 'animate-shake' },
        'sedimentary-to-igneous': { text: 'התכה והתגבשות מחדש - הופך לסלע יסוד!', emoji: '🪨', animation: 'animate-melt' },
        'metamorphic-to-sedimentary': { text: 'בליה, סחיפה ושקיעה - הופך לסלע משקע!', emoji: '🏖️', animation: 'animate-break' },

        // Transitions within the same type (optional but adds realism)
        'igneous-to-igneous': { text: 'מחזור פנימי: נמס ומתגבש מחדש כסלע יסוד אחר!', emoji: '🌋', animation: 'animate-melt' }, // Or '🪨'
        'sedimentary-to-sedimentary': { text: 'נשחק, נסחף ונשקע שוב כסלע משקע!', emoji: '🧱', animation: 'animate-break' }, // Or '🏖️'
        'metamorphic-to-metamorphic': { text: 'חשיפה נוספת לחום ולחץ משנה אותו שוב!', emoji: '💎', animation: 'animate-shake' } // Or '🗿'
    };

    let draggedItem = null;
    let originZoneId = null;
    let currentAnimationClass = null; // To track and remove animation classes

    rockPieces.forEach(piece => {
        piece.addEventListener('dragstart', (e) => {
            draggedItem = e.target;
            originZoneId = draggedItem.closest('.rock-zone').id;
            e.dataTransfer.effectAllowed = 'move';
            e.dataTransfer.setData('text/plain', null);

            // Add dragging style
            draggedItem.style.opacity = '0.7';
            draggedItem.style.transform = 'scale(1.1)';
             // Remove any previous animation class before dragging
            if (currentAnimationClass) {
                 draggedItem.classList.remove(currentAnimationClass);
                 currentAnimationClass = null; // Reset
             }
        });

        piece.addEventListener('dragend', (e) => {
             if (draggedItem) {
                draggedItem.style.opacity = '1';
                draggedItem.style.transform = 'scale(1)';
                // Keep the animation class after dragend so it plays on drop
                // if (currentAnimationClass) {
                //     draggedItem.classList.remove(currentAnimationClass);
                // }
             }
            // draggedItem is nullified in the drop handler
            // originZoneId = null; // Also nullified in drop handler
        });
    });

    rockZones.forEach(zone => {
        zone.addEventListener('dragover', (e) => {
            e.preventDefault();
            e.dataTransfer.dropEffect = 'move';
            zone.classList.add('drag-over');
        });

        zone.addEventListener('dragleave', (e) => {
            zone.classList.remove('drag-over');
        });

        zone.addEventListener('drop', (e) => {
            e.preventDefault();
            zone.classList.remove('drag-over');

            if (draggedItem) {
                const targetZoneId = zone.id;
                const originType = originZoneId.replace('-zone', '');
                const targetType = targetZoneId.replace('-zone', '');

                const processKey = `${originType}-to-${targetType}`;
                const processInfo = processMap[processKey] || { text: 'תהליך גיאולוגי מעניין...', emoji: draggedItem.textContent, animation: '' }; // Default fallback

                // Display the feedback
                feedbackDisplay.textContent = processInfo.text;
                feedbackDisplay.style.opacity = '1';

                // Hide feedback after a delay
                setTimeout(() => {
                    feedbackDisplay.style.opacity = '0';
                }, 4000); // Show for 4 seconds

                // --- Animation and Update ---
                // Add the animation class BEFORE appending, if any
                 if (processInfo.animation) {
                     currentAnimationClass = processInfo.animation; // Store for removal
                     draggedItem.classList.add(currentAnimationClass);

                     // Listen for animation end to update emoji and remove class
                     const animationEndHandler = () => {
                         draggedItem.textContent = processInfo.emoji; // Change emoji after animation
                         draggedItem.classList.remove(currentAnimationClass);
                         currentAnimationClass = null; // Reset
                         draggedItem.removeEventListener('animationend', animationEndHandler); // Clean up listener
                         draggedItem.style.opacity = '1'; // Ensure opacity is reset after animation
                         draggedItem.style.transform = 'scale(1)'; // Ensure scale is reset
                     };
                      draggedItem.addEventListener('animationend', animationEndHandler);

                     // If the animation makes it disappear (like melt/break), append immediately,
                     // but if it's just shake/pop, wait for a moment before appending
                     if (processInfo.animation === 'animate-melt' || processInfo.animation === 'animate-break') {
                           // Append immediately so the animation happens in the new container
                            const targetRockPiecesContainer = zone.querySelector('.rock-pieces');
                             if (targetRockPiecesContainer) {
                                 targetRockPiecesContainer.appendChild(draggedItem);
                            }
                     } else {
                          // For non-disappearing animations, maybe a slight delay? Or just append immediately too for simplicity.
                           const targetRockPiecesContainer = zone.querySelector('.rock-pieces');
                             if (targetRockPiecesContainer) {
                                 targetRockPiecesContainer.appendChild(draggedItem);
                            }
                     }


                 } else {
                    // No specific animation, just update emoji and append
                     draggedItem.textContent = processInfo.emoji;
                     const targetRockPiecesContainer = zone.querySelector('.rock-pieces');
                     if (targetRockPiecesContainer) {
                         targetRockPiecesContainer.appendChild(draggedItem);
                     }
                      draggedItem.style.opacity = '1'; // Ensure opacity is reset
                      draggedItem.style.transform = 'scale(1)'; // Ensure scale is reset
                 }


                draggedItem = null; // Reset dragged item AFTER handling animation and appending
                originZoneId = null;
            }
        });
    });

    // Explanation button functionality
    explanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        // Optional: scroll into view when shown
        if (isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });

    // Initial feedback message fade-in
    setTimeout(() => {
        feedbackDisplay.style.opacity = '1';
        setTimeout(() => {
            feedbackDisplay.style.opacity = '0';
        }, 3000);
    }, 1000);

});
</script>