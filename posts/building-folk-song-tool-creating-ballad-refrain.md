---
title: "האורג המילים: צרו בלדה עממית קסומה עם פזמון"
english_slug: building-folk-song-tool-creating-ballad-refrain
category: "ספרות"
tags: ["שירה", "כתיבה יוצרת", "בלדה עממית", "פזמון חוזר", "מבנה שיר", "כלי יצירה"]
---
<h1>האורג המילים: צרו בלדה עממית קסומה עם פזמון</h1>
<p>מוכנים לצאת למסע אל עולם הבלדות העממיות? בואו נגלה יחד איך הפזמון הופך שיר לסיפור שנדבק ללב! הכלי הזה יאפשר לכם לארוג את המילים שלכם למבנה הקסום הזה, בדיוק כמו האורגים והמספרים של פעם.</p>

<div class="app-container">
    <div class="song-parts-input">
        <div class="song-part">
            <label for="beit1">התחלת הסיפור (בית א'):</label>
            <textarea id="beit1" rows="4" placeholder="איך הסיפור מתחיל? תנו לקו העלילה הראשון להופיע..."></textarea>
        </div>
        <div class="song-part">
            <label for="pizmonInput">הקצב החוזר (הפזמון):</label>
            <textarea id="pizmonInput" rows="2" placeholder="איזו שורה או מחשבה חוזרת כמו הד בסיפור? היא הלב הפועם של הבלדה..."></textarea>
        </div>
        <div class="song-part">
            <label for="beit2">המשך העלילה (בית ב'):</label>
            <textarea id="beit2" rows="4" placeholder="מה קורה אחר כך? ספרו על התפנית הבאה או על התפתחות הדמויות..."></textarea>
        </div>
        <div class="song-part pizmon-section">
            <label>...והנה שוב הפזמון:</label>
            <div id="pizmon2Display" class="pizmon-display" dir="rtl"></div>
        </div>
        <div class="song-part">
            <label for="beit3">רגע שיא או שינוי (בית ג'):</label>
            <textarea id="beit3" rows="4" placeholder="הסיפור מתעמק? רגש מתחזק? זה המקום להוסיף עוצמה..."></textarea>
        </div>
        <div class="song-part pizmon-section">
            <label>...וכמובן, הקצב חוזר:</label>
            <div id="pizmon3Display" class="pizmon-display" dir="rtl"></div>
        </div>
        <div class="song-part">
            <label for="beitFinal">סיום הבלדה (בית אחרון / אופציונלי):</label>
            <textarea id="beitFinal" rows="4" placeholder="איך הסיפור נגמר? איזו תחושה או מסקנה נשארת?"></textarea>
        </div>
    </div>
    <button id="buildSongBtn" class="interactive-button">אִרגו את הבלדה</button>
    <div id="songOutput" class="song-output" dir="rtl">
        <!-- The generated song will appear here -->
    </div>
</div>

<button id="toggleExplanationBtn" class="interactive-button toggle-button">סקרנים לדעת עוד? הצגת הסבר על בלדות</button>

<div id="explanationSection" class="explanation-section">
    <h2>מגלים את קסם הבלדות העממיות והפזמון</h2>
    <p><strong>מהי בלדה עממית?</strong> דמיינו שיר שהוא גם סיפור, כזה שעובר מפה לאוזן, מדור לדור, בארובות ובכיכרות העיר. זו בלדה! לרוב הן מספרות על אירועים דרמטיים, גורליים, לפעמים אפלים או טרגיים, עם גיבורים ועם מסע.</p>
    <p><strong>מה הופך בלדה לעממית?</strong></p>
    <ul>
        <li><strong>הסיפור במרכז:</strong> יש בה עלילה ברורה, התחלה, אמצע וסוף (לפעמים מפתיע!).</li>
        <li><strong>רגשות עזים:</strong> היא נוגעת באהבה, אובדן, גבורה, נקמה - נושאים שמדברים ללב.</li>
        <li><strong>מבנה ברור:</strong> מחולקת לבתים קצרים, קלים לזכירה, עם מקצב ולעתים חריזה שסייעו בהעברתה בעל פה.</li>
    </ul>
    <p><strong>ולמה הפזמון כה חשוב?</strong> הפזמון הוא החלק שחוזר על עצמו – מילים, שורות או בית שלם – אחרי כל בית (או כמה בתים). הוא לא סתם חזרה, יש לו כוח:</p>
    <ul>
        <li><strong>עוגן וחיבור:</strong> הוא מחבר את כל חלקי הסיפור יחד, מזכיר את הרעיון המרכזי או את הנימה החוזרת.</li>
        <li><strong>קצב ומנגינה:</strong> החזרה יוצרת מקצב שמושך את המאזין והופך את השיר לקליט וקל לשירה משותפת.</li>
        <li><strong>הדגשה ורגש:</strong> הפזמון מדגיש מסר חשוב, רגש עמוק או דימוי ויזואלי מרכזי בסיפור.</li>
        <li><strong>ציפייה והנאה:</strong> המאזין מחכה לשמוע שוב את המילים המוכרות, וזה יוצר חוויה נעימה ומרתקת.</li>
    </ul>
    <p><strong>המבנה הקלאסי:</strong> לרוב תראו את זה כך: בית + פזמון + בית + פזמון + בית + פזמון... ולפעמים בית אחרון שמסיים את הסיפור באופן ייחודי.</p>
    <p><strong>דוגמאות:</strong> ביאליק, לדוגמה, השתמש במבנה דומה בבלדות שלו ("הכניסיני תחת כנפך"). וגם במוזיקה עממית מודרנית, הפזמון הוא כלי מרכזי ליצירת קליטות ועומק.</p>
    <p>עכשיו כשאתם מבינים את המבנה והכוח, חזרו למעלה ושחררו את האורג שבכם! אִרגו מילים וצרו בלדה משלכם.</p>
</div>

<style>
    /* General Styles - Enhancing the Folk/Ballad theme */
    body {
        font-family: 'Arial', sans-serif; /* Keeping Arial for readability */
        line-height: 1.6;
        color: #333;
        background-color: #f4e8d9; /* Soft, papery background */
        padding: 20px;
        direction: rtl;
    }

    .app-container {
        max-width: 750px;
        margin: 20px auto;
        padding: 30px;
        border: 1px solid #d4c4b4; /* Soft border */
        border-radius: 12px; /* More rounded */
        background-color: #fffaf0; /* Lighter papery feel inside */
        box-shadow: 0 5px 15px rgba(0,0,0,0.1); /* Subtle shadow */
        direction: rtl;
    }

    h1 {
        text-align: center;
        color: #6a0505; /* Deep red for headings */
        margin-bottom: 30px;
        font-size: 2em;
        border-bottom: 2px solid #d4c4b4; /* Separator line */
        padding-bottom: 15px;
    }

    p {
        margin-bottom: 20px;
    }

    /* Input Section Styling */
    .song-parts-input {
        margin-bottom: 30px;
    }

    .song-part {
        margin-bottom: 25px;
        background-color: #fff; /* White background for input fields */
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #e0d0c0; /* Light border for parts */
        box-shadow: inset 0 1px 5px rgba(0,0,0,0.05); /* Inner shadow */
        transition: box-shadow 0.3s ease;
    }

    .song-part:focus-within { /* Highlight part when an input inside is focused */
         box-shadow: 0 0 8px rgba(106, 5, 5, 0.2);
         border-color: #6a0505;
    }

    .song-part label {
        display: block;
        margin-bottom: 8px;
        font-weight: bold;
        color: #8b5a2b; /* Earthy brown for labels */
        font-size: 1.1em;
    }

    .song-part textarea {
        width: calc(100% - 22px);
        padding: 12px;
        border: 1px solid #c4a484;
        border-radius: 6px;
        font-size: 1rem;
        line-height: 1.6;
        box-sizing: border-box;
        resize: vertical;
        min-height: 70px; /* Increased min height */
        background-color: #f9f9f9; /* Slightly off-white input background */
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }

    .song-part textarea:focus {
        border-color: #6a0505;
        box-shadow: 0 0 5px rgba(106, 5, 5, 0.3);
        outline: none;
    }

    .pizmon-section label {
        font-style: italic;
        color: #555;
        font-weight: normal;
        font-size: 1em;
        margin-bottom: 5px;
    }

    .pizmon-display {
        background-color: #f0e6da; /* Different background for auto-filled parts */
        border: 1px dashed #a08a70; /* Dashed earthy border */
        color: #5a4a3a; /* Muted text color */
        padding: 12px;
        border-radius: 6px;
        min-height: 50px;
        white-space: pre-wrap;
        word-wrap: break-word;
        cursor: default;
        font-style: italic; /* Auto-filled text is slightly different */
        transition: background-color 0.3s ease, color 0.3s ease; /* Smooth update transition */
    }

    .pizmon-display.empty {
        color: #aaa;
        font-style: italic;
        background-color: #f8f0e8; /* Lighter background for empty */
    }

    /* Button Styling */
    .interactive-button {
        display: block;
        width: auto;
        padding: 12px 25px;
        margin: 20px auto;
        background-color: #6a0505; /* Deep red button */
        color: white;
        border: none;
        border-radius: 25px; /* Pill shape */
        font-size: 1.2rem;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        font-weight: bold;
    }

    .interactive-button:hover {
        background-color: #8b0a0a; /* Darker red on hover */
        transform: translateY(-2px); /* Subtle lift */
        box-shadow: 0 6px 12px rgba(0,0,0,0.25);
    }

    .interactive-button:active {
        background-color: #4d0000; /* Even darker on active */
        transform: translateY(1px); /* Push down */
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

    .toggle-button {
         background-color: #c4a484; /* Different color for toggle */
         color: #333;
         box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

     .toggle-button:hover {
        background-color: #d4b494;
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
     }

     .toggle-button:active {
         background-color: #a08a70;
         transform: translateY(0px);
         box-shadow: 0 1px 3px rgba(0,0,0,0.1);
     }


    /* Song Output Styling */
    .song-output {
        margin-top: 30px;
        padding: 30px;
        border: 1px solid #d4c4b4;
        border-radius: 10px;
        background-color: #fffaf0; /* Papery background */
        white-space: pre-wrap;
        word-wrap: break-word;
        min-height: 100px; /* Increased min height */
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        font-family: Georgia, serif; /* Serif font for the song output */
        font-size: 1.1rem;
        color: #3a2a1a; /* Slightly darker text for readability */
        opacity: 0; /* Initially hidden */
        transform: translateY(20px); /* Start slightly lower */
        transition: opacity 0.6s ease-out, transform 0.6s ease-out; /* Animation */
        display: none; /* Use JS to control visibility */
    }

     .song-output.visible {
         opacity: 1;
         transform: translateY(0);
         display: block; /* Make visible */
     }


    /* Explanation Section Styling */
    .explanation-section {
        margin-top: 30px;
        padding: 25px;
        border: 1px solid #d3d3d3;
        border-radius: 8px;
        background-color: #eef2f7; /* Light blue-ish background */
        direction: rtl;
        overflow: hidden; /* Hide overflow during transition */
        max-height: 0; /* Start collapsed */
        opacity: 0;
        transition: max-height 0.5s ease-in-out, opacity 0.5s ease-in-out; /* Animation */
    }

    .explanation-section.visible {
        max-height: 1000px; /* Needs to be larger than content */
        opacity: 1;
    }

    .explanation-section h2 {
        color: #1a4d7c; /* Dark blue heading */
        margin-top: 0;
        border-bottom: 1px solid #a0c0d0;
        padding-bottom: 10px;
        margin-bottom: 15px;
        font-size: 1.5em;
    }

    .explanation-section ul {
        list-style-type: disc;
        margin-right: 25px;
        padding-right: 0;
    }

     .explanation-section li {
         margin-bottom: 10px;
         line-height: 1.6;
     }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const beit1Input = document.getElementById('beit1');
        const pizmonInput = document.getElementById('pizmonInput');
        const beit2Input = document.getElementById('beit2');
        const pizmon2Display = document.getElementById('pizmon2Display');
        const beit3Input = document.getElementById('beit3');
        const pizmon3Display = document.getElementById('pizmon3Display');
        const beitFinalInput = document.getElementById('beitFinal');
        const buildSongBtn = document.getElementById('buildSongBtn');
        const songOutput = document.getElementById('songOutput');
        const toggleExplanationBtn = document.getElementById('toggleExplanationBtn');
        const explanationSection = document.getElementById('explanationSection');

        // Function to update the repeated refrain displays with animation
        const updatePizmonDisplays = () => {
            const pizmonText = pizmonInput.value.trim();

            // Check if text content is changing
            if (pizmon2Display.textContent.trim() !== pizmonText) {
                // Add a temporary class to trigger animation
                pizmon2Display.classList.add('updating');
                pizmon3Display.classList.add('updating');

                 // Update content after a short delay to allow animation to start
                 setTimeout(() => {
                    pizmon2Display.textContent = pizmonText || 'הפזמון יופיע כאן אוטומטית';
                    pizmon3Display.textContent = pizmonText || 'הפזמון יופיע כאן אוטומטית';
                     // Remove the animation class after content update
                     pizmon2Display.classList.remove('updating');
                     pizmon3Display.classList.remove('updating');
                 }, 50); // Short delay

            }

            // Manage empty state class for styling placeholder
            if (!pizmonText) {
                 pizmon2Display.classList.add('empty');
                 pizmon3Display.classList.add('empty');
            } else {
                 pizmon2Display.classList.remove('empty');
                 pizmon3Display.classList.remove('empty');
            }
        };

         // Initial update and update on input change
        updatePizmonDisplays();
        pizmonInput.addEventListener('input', updatePizmonDisplays);


        // Event listener for the build song button
        buildSongBtn.addEventListener('click', () => {
            const beit1 = beit1Input.value.trim();
            const pizmon = pizmonInput.value.trim();
            const beit2 = beit2Input.value.trim();
            const beit3 = beit3Input.value.trim();
            const beitFinal = beitFinalInput.value.trim();

            let outputParts = [];

            // Function to add a part if it has content
            const addContentPart = (content) => {
                if (content) {
                    outputParts.push(content);
                    return true;
                }
                return false;
            };

            // Function to add the refrain if it has content
            const addRefrainPart = () => {
                if (pizmon) {
                    outputParts.push(pizmon);
                    return true;
                }
                return false;
            };

            // Build the song structure: Beit1, Pizmon, Beit2, Pizmon, Beit3, Pizmon, BeitFinal
            const beit1Added = addContentPart(beit1);
            if (beit1Added) {
               addRefrainPart();
            }

            const beit2Added = addContentPart(beit2);
             if (beit2Added) {
               addRefrainPart();
            }

            const beit3Added = addContentPart(beit3);
             if (beit3Added) {
               addRefrainPart();
            }

            // Add BeitFinal
            addContentPart(beitFinal);


            // Join the parts with double newlines
            const songText = outputParts.join('\n\n');

            // Update and display the output area with animation
            if (songText.trim()) {
                // Clear previous content and hide initially for animation
                songOutput.textContent = '';
                songOutput.classList.remove('visible');
                 songOutput.style.display = 'none'; // Ensure display is none before setting text

                // Set content and trigger animation after a small delay
                setTimeout(() => {
                     songOutput.textContent = songText;
                     songOutput.style.display = 'block'; // Make display block immediately before animation
                     // Force reflow to restart animation
                     void songOutput.offsetWidth;
                     songOutput.classList.add('visible');
                }, 50); // Short delay to ensure display:none applies

            } else {
                // If no content, show placeholder without animation
                songOutput.textContent = 'אנא מלאו לפחות חלק מהשיר כדי להציג אותו.';
                 songOutput.classList.remove('visible');
                 songOutput.style.display = 'block'; // Ensure it's visible
                 // No transition for this case
            }
        });

        // Event listener for the toggle explanation button
        toggleExplanationBtn.addEventListener('click', () => {
            const isHidden = !explanationSection.classList.contains('visible'); // Check visible class
            if (isHidden) {
                explanationSection.classList.add('visible');
                toggleExplanationBtn.textContent = 'הסתר הסבר על בלדות';
            } else {
                explanationSection.classList.remove('visible');
                toggleExplanationBtn.textContent = 'סקרנים לדעת עוד? הצגת הסבר על בלדות';
            }
        });

         // Add CSS rules for the refrain update animation directly via style tag
         const style = document.createElement('style');
         style.textContent = `
             .pizmon-display.empty {
                 color: #aaa;
                 font-style: italic;
             }
              /* Simple pulse animation for updates */
             .pizmon-display.updating {
                 animation: pulse-refrain 0.5s ease-out 1;
             }
             @keyframes pulse-refrain {
                 0% { transform: scale(1); opacity: 1; }
                 50% { transform: scale(1.02); opacity: 0.8; }
                 100% { transform: scale(1); opacity: 1; }
             }
         `;
         document.head.appendChild(style);

    });
</script>
```