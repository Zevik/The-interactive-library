---
title: "לראות שמיעה: אפקט מקגורק"
english_slug: see-hearing-mcgurk-effect
category: "פסיכולוגיה"
tags:
  - פסיכולוגיה קוגניטיבית
  - תפיסה חושית
  - שמיעה
  - ראייה
  - אשליה חושית
  - עיבוד מידע
---
# לראות שמיעה: אפקט מקגורק - האשליה שמשנה את מה שאתם שומעים

האם דמיינתם פעם שהעיניים שלכם יכולות לשנות את מה שהאוזניים שלכם שומעות? לא רק "לשפר" או "להבהיר", אלא ממש לגרום לכם לשמוע מילה *אחרת* ממה שנאמר בפועל? התכוננו לפגוש את המוח שלכם בפעולה, בחוויה שתטלטל את האופן שבו אתם מבינים את תפיסת המציאות.

<div id="mcgurk-app">
    <h2>חוו בעצמכם את אפקט מקגורק</h2>
    <p class="subtitle">בחרו את תנועת השפתיים (וידאו) ואת הצליל האקוסטי (שמע), ואז לחצו על "צפו והקשיבו". המוח שלכם יעשה את השאר...</p>

    <div class="controls">
        <div class="control-section">
            <h3>צפו (וידאו):</h3>
            <button data-media-type="video" data-value="gah">גה</button>
            <button data-media-type="video" data-value="bah">בה</button>
        </div>
        <div class="control-section">
            <h3>הקשיבו (שמע):</h3>
            <button data-media-type="audio" data-value="gah">גה</button>
            <button data-media-type="audio" data-value="bah">בה</button>
        </div>
    </div>

    <div class="player-area">
        <div class="video-container">
             <video id="mcgurk-video" width="320" height="240" preload="auto" playsinline></video>
             <div class="video-placeholder">בחרו וידאו כדי לצפות כאן בתנועת השפתיים</div>
        </div>
        <audio id="mcgurk-audio" preload="auto"></audio>
        <button id="play-button" disabled>צפו והקשיבו</button>
    </div>

    <div class="perception-report">
        <h3>וואו! מה שמעתם בפועל?</h3>
        <p>הקשיבו לתחושת הבטן הראשונה שלכם - איזו הברה הכי קרובה למה שתפסתם?</p>
        <div class="options">
            <button data-perception="bah">בה</button>
            <button data-perception="gah">גה</button>
            <button data-perception="dah">דה</button>
            <button data-perception="other">אחר/בלבול</button>
        </div>
        <p id="reported-perception"></p>
    </div>
</div>

<style>
    /* Overall App Container */
    #mcgurk-app {
        font-family: 'Heebo', sans-serif; /* A common, pleasant Hebrew-friendly font */
        direction: rtl;
        text-align: center;
        max-width: 600px;
        margin: 30px auto; /* More vertical margin */
        padding: 30px; /* More padding */
        border: none; /* Remove default border */
        border-radius: 12px; /* More rounded corners */
        background-color: #ffffff; /* Clean white background */
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1); /* Soft shadow */
        color: #333;
        overflow: hidden; /* Ensure rounded corners apply */
    }

    #mcgurk-app h2 {
        color: #1a237e; /* Deep blue for main title */
        margin-top: 0;
        margin-bottom: 10px;
        font-size: 2em; /* Larger title */
        font-weight: 700;
    }

    #mcgurk-app .subtitle {
        color: #555;
        margin-bottom: 30px; /* More space after subtitle */
        font-size: 1.1em;
    }

    #mcgurk-app h3 {
        color: #3949ab; /* Slightly lighter blue for section titles */
        margin-top: 20px;
        margin-bottom: 15px;
        font-size: 1.4em;
        font-weight: 600;
    }

    /* Controls Section */
    .controls {
        display: flex;
        justify-content: center;
        gap: 40px; /* Increased gap */
        margin-bottom: 30px; /* More space below controls */
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
    }

    .control-section {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .control-section h3 {
         margin-top: 0; /* Adjust margin */
         margin-bottom: 10px;
         font-size: 1.2em;
         font-weight: 600;
         color: #5c6bc0; /* Medium blue */
    }

    .control-section button {
        padding: 12px 20px; /* Increased padding */
        margin: 5px;
        border: 2px solid #e0e0e0; /* Lighter, more subtle border */
        border-radius: 6px; /* More rounded */
        background-color: #f5f5f5; /* Light gray background */
        cursor: pointer;
        font-size: 1.1em; /* Slightly larger font */
        transition: all 0.2s ease-in-out; /* Smooth transition for hover/selected states */
        min-width: 80px; /* Ensure consistent button size */
        font-weight: 500;
        color: #444;
    }

    .control-section button:hover:not(:disabled) {
        background-color: #e0e0e0; /* Darker gray on hover */
        border-color: #bdbdbd;
    }

    .control-section button.selected {
        background-color: #42a5f5; /* Brighter blue when selected */
        color: white;
        border-color: #2196f3;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* Add shadow to selected */
        transform: translateY(-2px); /* Slight lift */
    }

    .control-section button:disabled {
        opacity: 0.6;
        cursor: not-allowed;
    }

    /* Player Area */
    .player-area {
        margin-bottom: 30px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .video-container {
        width: 320px; /* Match video width */
        height: 240px; /* Match video height */
        border: 1px solid #ddd;
        border-radius: 8px;
        overflow: hidden; /* Hide parts of video if it exceeds bounds */
        margin-bottom: 20px;
        background-color: #eee; /* Background when placeholder is visible */
        position: relative; /* Needed for absolute positioning of placeholder */
    }

    #mcgurk-video {
        display: block; /* Remove extra space below video */
        width: 100%;
        height: 100%;
        object-fit: cover; /* Ensure video covers the container */
        transition: opacity 0.5s ease-in-out;
        opacity: 0; /* Hide initially via opacity for smooth transition */
    }

     .video-placeholder {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #666;
        font-size: 1.1em;
        padding: 20px;
        text-align: center;
        background-color: #f0f0f0;
        transition: opacity 0.5s ease-in-out;
        opacity: 1; /* Show initially */
     }

     #mcgurk-video.visible {
         opacity: 1;
     }

      .video-placeholder.hidden {
          opacity: 0;
          pointer-events: none; /* Make it non-interactive when hidden */
      }


    #play-button {
        padding: 12px 25px;
        font-size: 1.2em;
        background-color: #4caf50; /* Green play button */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        transition: background-color 0.2s ease-in-out, transform 0.1s ease-in-out;
        font-weight: 600;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    #play-button:hover:not(:disabled) {
        background-color: #388e3c; /* Darker green on hover */
         box-shadow: 0 5px 10px rgba(0, 0, 0, 0.3);
    }

    #play-button:active:not(:disabled) {
         transform: scale(0.98); /* Slight press effect */
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }


    #play-button:disabled {
        background-color: #b0bec5; /* Gray disabled */
        cursor: not-allowed;
        box-shadow: none;
    }

    /* Perception Report Section */
    .perception-report {
        margin-top: 30px;
        padding: 25px;
        border-top: 1px solid #eee;
        background-color: #e3f2fd; /* Light blue background */
        border-radius: 8px;
        opacity: 0; /* Hide initially with opacity */
        transform: translateY(20px); /* Start slightly lower */
        transition: opacity 0.5s ease-out, transform 0.5s ease-out; /* Animation */
    }

    .perception-report.visible {
        opacity: 1;
        transform: translateY(0);
    }

     .perception-report h3 {
         color: #1a237e; /* Deep blue */
         margin-top: 0;
     }

     .perception-report p {
         color: #555;
         margin-bottom: 20px;
     }

    .perception-report .options {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 10px; /* Space between options buttons */
    }

    .perception-report .options button {
         padding: 12px 18px;
         margin: 5px; /* Adjust margin if gap is used */
         border: 2px solid #e0e0e0;
         border-radius: 6px;
         background-color: #f5f5f5;
         cursor: pointer;
         font-size: 1.1em;
         transition: all 0.2s ease-in-out;
         font-weight: 500;
         min-width: 70px;
         color: #444;
    }

     .perception-report .options button:hover:not(:disabled) {
        background-color: #e0e0e0;
        border-color: #bdbdbd;
    }

    .perception-report .options button.selected {
        background-color: #42a5f5;
        color: white;
        border-color: #2196f3;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        transform: translateY(-2px);
    }


    #reported-perception {
        margin-top: 20px;
        font-weight: bold;
        color: #00796b; /* Teal color for result */
        font-size: 1.2em;
        min-height: 1.5em; /* Reserve space even when empty */
    }

    /* Explanation Toggle Button */
    #toggle-explanation {
        display: block;
        width: fit-content;
        margin: 30px auto; /* More margin */
        padding: 12px 25px;
        font-size: 1.1em;
        background-color: #1e88e5; /* Medium blue */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        transition: background-color 0.2s ease-in-out, transform 0.1s ease-in-out;
        font-weight: 600;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    #toggle-explanation:hover {
         background-color: #1565c0; /* Darker blue on hover */
          box-shadow: 0 5px 10px rgba(0, 0, 0, 0.3);
    }
     #toggle-explanation:active {
         transform: scale(0.98);
          box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
     }


    /* Explanation Section */
    #explanation {
        margin-top: 20px;
        padding: 30px; /* More padding */
        border: none;
        border-radius: 12px; /* Match app container radius */
        background-color: #fce4ec; /* Very light pink background */
        text-align: right;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); /* Soft shadow */
        opacity: 0; /* Hide initially with opacity */
        transform: translateY(20px); /* Start slightly lower */
        transition: opacity 0.5s ease-out, transform 0.5s ease-out; /* Animation */
    }

    #explanation.visible {
        opacity: 1;
        transform: translateY(0);
    }


    #explanation h3 {
        color: #ad1457; /* Deep pink for explanation titles */
        margin-top: 0;
        margin-bottom: 15px;
        font-size: 1.5em;
        font-weight: 700;
    }

    #explanation p {
        line-height: 1.7; /* Increased line height for readability */
        margin-bottom: 15px;
        color: #444;
        font-size: 1.1em;
    }

     #explanation p:last-child {
         margin-bottom: 0;
     }

     /* Responsive adjustments */
     @media (max-width: 480px) {
         #mcgurk-app, #explanation {
             padding: 20px;
             margin: 20px auto;
         }

         .controls {
             flex-direction: column;
             gap: 20px;
         }

         .control-section {
             width: 100%;
             align-items: stretch;
         }

         .control-section h3 {
             text-align: center;
         }

         .control-section button {
             width: calc(100% - 10px); /* Adjust for margin */
             min-width: auto;
         }

         .video-container {
             width: 100%; /* Make video container full width */
             height: auto; /* Adjust height proportionally */
             max-height: 250px; /* Prevent excessive height on very wide screens */
         }

          #mcgurk-video {
             height: auto; /* Allow video to scale height */
          }

         .perception-report .options button {
              width: calc(50% - 20px); /* Two buttons per row */
              margin: 5px;
         }
     }

</style>

<button id="toggle-explanation">רוצים להבין איך זה קורה? לחצו כאן להסבר המדעי</button>

<div id="explanation" style="display: none;">
    <h3>הקסם במוח: מהו אפקט מקגורק?</h3>
    <p>אפקט מקגורק הוא אחת הדוגמאות המדהימות ביותר לאופן שבו החושים שלנו לא עובדים "בדד". זוהי אשליית תפיסה שמגלה לנו סוד כמוס: המוח שלנו כל הזמן משלב ומעבד מידע מכל החושים בו זמנית כדי לבנות את ה"מציאות" שאנחנו חווים. במקרה של דיבור, המוח לוקח גם את מה ששומעים (הצלילים האקוסטיים) וגם את מה שרואים (תנועות הפה והשפתיים), ומחבר אותם לתפיסה אחת קוהרנטית.</p>

    <h3>איך האשליה נולדת?</h3>
    <p>ההדגמה הקלאסית, שאתם אולי חוויתם זה עתה (בעיקר בשילוב של וידאו 'גה' ושמע 'בה'), מערבת קונפליקט. כשהעיניים רואות תנועת שפתיים של "גה" (שפתיים פתוחות, לשון אחורה) והאוזניים שומעות צליל של "בה" (שפתיים סגורות בתחילת ההברה), המוח מקבל מסרים סותרים. במקום להגיד "אני מבולבל", הוא מנסה ליישב את הסתירה ו"ממציא" את הפתרון הסביר ביותר בהקשר של הפקת דיבור. לעיתים קרובות, הפתרון הזה הוא ההברה "דה" (המערבת מגע של הלשון עם החך, פשרה תפיסתית בין 'גה' ל-'בה').</p>

    <h3>אינטגרציה רב-חושית: שיתוף פעולה מנצח (כמעט תמיד)</h3>
    <p>היכולת הזו של המוח לשלב מידע מחושים שונים נקראת אינטגרציה רב-חושית. היא חיונית לנו בחיי היומיום. לדוגמה, כשאנחנו חוצים כביש, אנחנו משלבים ראייה ושמיעה (רואים את המכונית, שומעים את הרעש שלה). כשמישהו מדבר בסביבה רועשת, העיניים שעוקבות אחרי תנועות השפתיים עוזרות למוח "לנקות" את הרעש ולפענח את הדיבור. אפקט מקגורק פשוט חושף את המנגנון הזה בזמן שהוא טועה - כשהקלט החושי סותר באופן קיצוני.</p>

    <h3>למה 'דה'?</h3>
    <p>בחזרה לדוגמה הקלאסית: הברה 'גה' היא וילונית (נוצרת בחלק האחורי של הפה), והברה 'בה' היא שפתית (נוצרת בשפתיים). ההברה 'דה' היא מכתשית (נוצרת כשהלשון נוגעת בחלק הקדמי של החך, מאחורי השיניים). מבחינה ארטיקולטורית ותפיסתית, 'דה' נחשבת לעיתים קרובות כנקודת פשרה סבירה כשהמוח מנסה לפענח קונפליקט בין מידע ויזואלי של 'גה' למידע שמיעתי של 'בה'. זה לא תמיד קורה לכולם, והתפיסה יכולה להיות מושפעת מגורמים אישיים ואיכות המדיה, אבל זהו האפקט הנפוץ ביותר.</p>

    <h3>מעבר לאשליה</h3>
    <p>אפקט מקגורק הוא יותר מסתם טריק מגניב של המוח. הוא כלי חשוב למדענים החוקרים תפיסה וקוגניציה. הוא מראה לנו כמה התפיסה שלנו היא יצירה פעילה של המוח, לא רק קליטה פסיבית של מידע. הוא מדגים את החשיבות העצומה של אינטגרציה רב-חושית בתפיסת דיבור, עם השלכות על הבנת קשיי שמיעה, פיתוח טכנולוגיות לזיהוי דיבור, ואפילו איך אנחנו לומדים שפה.</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const video = document.getElementById('mcgurk-video');
        const audio = document.getElementById('mcgurk-audio');
        const playButton = document.getElementById('play-button');
        const mediaButtons = document.querySelectorAll('.control-section button[data-media-type]');
        const videoPlaceholder = document.querySelector('.video-placeholder');
        const perceptionButtons = document.querySelectorAll('.perception-report button[data-perception]');
        const perceptionReportDiv = document.querySelector('.perception-report');
        const reportedPerceptionP = document.getElementById('reported-perception');
        const explanationDiv = document.getElementById('explanation');
        const toggleExplanationButton = document.getElementById('toggle-explanation');

        let selectedVideoValue = null;
        let selectedAudioValue = null;

        // Use relative paths assuming they are in an 'assets' directory at the root
        const sources = {
            video: {
                gah: './assets/video/mcgurk-gah.mp4',
                bah: './assets/video/mcgurk-bah.mp4'
            },
            audio: {
                gah: './assets/audio/mcgurk-gah.mp3',
                bah: './assets/audio/mcgurk-bah.mp3'
            }
        };

        function updatePlayButtonState() {
            if (selectedVideoValue && selectedAudioValue) {
                playButton.disabled = false;
                playButton.textContent = 'צפו והקשיבו';
            } else {
                playButton.disabled = true;
                playButton.textContent = 'בחרו וידאו ושמע';
            }
        }

        function resetPerceptionReport() {
            reportedPerceptionP.textContent = '';
            perceptionReportDiv.classList.remove('visible');
            perceptionReportDiv.style.display = 'none'; // Ensure it's hidden physically
            perceptionButtons.forEach(btn => btn.classList.remove('selected'));
        }

        function showPerceptionReport() {
             perceptionReportDiv.style.display = 'block'; // Show physically first
             // Use a slight delay before adding the visible class to ensure transition works
             setTimeout(() => {
                 perceptionReportDiv.classList.add('visible');
             }, 50);
        }


        // Handle media selection buttons
        mediaButtons.forEach(button => {
            button.addEventListener('click', () => {
                const type = button.dataset.mediaType;
                const value = button.dataset.value;

                // Deselect other buttons of the same type
                document.querySelectorAll(`.control-section button[data-media-type="${type}"]`).forEach(btn => btn.classList.remove('selected'));

                // Select this button
                button.classList.add('selected');

                // Store selection and load media
                if (type === 'video') {
                    selectedVideoValue = value;
                    video.src = sources.video[selectedVideoValue];
                     // Load video to make it ready
                    video.load();
                     // Show video element and hide placeholder
                    video.classList.add('visible');
                    videoPlaceholder.classList.add('hidden');

                } else { // type === 'audio'
                    selectedAudioValue = value;
                    audio.src = sources.audio[selectedAudioValue];
                    audio.load(); // Load audio to make it ready
                }

                // Reset report section when selection changes
                resetPerceptionReport();
                updatePlayButtonState();
            });
        });

        // Handle Play Button
        playButton.addEventListener('click', () => {
            if (selectedVideoValue && selectedAudioValue) {
                playButton.disabled = true;
                playButton.textContent = 'מנגן...';
                resetPerceptionReport(); // Ensure report is hidden before playing

                // Play sequence: Play audio first, then video immediately after audio starts
                // This often results in better perceived sync than video then audio.
                audio.play().then(() => {
                    // Audio started playing, now play video
                    video.play().catch(error => {
                         console.error("Error playing video:", error);
                         // Handle video playback errors (e.g., user gesture required)
                         alert("שגיאה בהפעלת הוידאו. ייתכן שהדפדפן דורש אינטראקציה לפני הפעלה.");
                         playButton.disabled = false; // Re-enable button on error
                         updatePlayButtonState(); // Update button text
                    });
                }).catch(error => {
                    console.error("Error playing audio:", error);
                    // Handle audio playback errors
                    alert("שגיאה בהפעלת השמע. ייתכן שהקבצים אינם זמינים או שהדפדפן דורש אינטראקציה לפני הפעלה.");
                    playButton.disabled = false; // Re-enable button on error
                    updatePlayButtonState(); // Update button text
                });

                // Use the 'ended' event from both to ensure report shows regardless
                let mediaEndedCount = 0;
                const mediaEndedHandler = () => {
                    mediaEndedCount++;
                    // Wait for both to signal end, or just one if the other fails/is short
                    // A simple approach is to show report after either ends, or after a timeout
                    // Let's stick to one ending event for simplicity as the original code did.
                    // Use video.onended as video is visual anchor. Add audio fallback.
                    if (mediaEndedCount === 1) { // Show report after the first one ends
                        // A small delay can make it feel smoother
                         setTimeout(showPerceptionReport, 300);
                         playButton.disabled = false; // Re-enable play button
                         updatePlayButtonState(); // Update button text
                    }
                };

                video.onended = mediaEndedHandler;
                audio.onended = mediaEndedHandler; // Fallback/additional trigger

            }
        });

        // Handle Perception Report Buttons
        perceptionButtons.forEach(button => {
            button.addEventListener('click', () => {
                perceptionButtons.forEach(btn => btn.classList.remove('selected'));
                button.classList.add('selected');
                const perception = button.dataset.perception;
                let perceptionText = '';
                switch(perception) {
                    case 'bah': perceptionText = 'בה'; break;
                    case 'gah': perceptionText = 'גה'; break;
                    case 'dah': perceptionText = 'דה'; break;
                    case 'other': perceptionText = 'אחר'; break;
                    default: perceptionText = perception; // Should not happen
                }
                reportedPerceptionP.textContent = `דיווחת ששמעת: ${perceptionText}`;
                 // Optional: Add a subtle confirmation animation/style to the reported text
                 reportedPerceptionP.style.transform = 'scale(1.05)';
                 reportedPerceptionP.style.color = '#004d40'; /* Darker teal */
                 setTimeout(() => {
                      reportedPerceptionP.style.transform = 'scale(1)';
                       reportedPerceptionP.style.color = '#00796b'; /* Original teal */
                 }, 300);
            });
        });

        // Handle Explanation Toggle Button
        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            if (isHidden) {
                explanationDiv.style.display = 'block'; // Show physically first
                // Use a slight delay before adding the visible class to ensure transition works
                setTimeout(() => {
                    explanationDiv.classList.add('visible');
                }, 50);

                toggleExplanationButton.textContent = 'הסתר הסבר על אפקט מקגורק';
            } else {
                 explanationDiv.classList.remove('visible');
                 // Use a delay matching the transition duration before hiding physically
                 setTimeout(() => {
                     explanationDiv.style.display = 'none';
                 }, 500); // Match CSS transition duration

                toggleExplanationButton.textContent = 'רוצים להבין איך זה קורה? לחצו כאן להסבר המדעי';
            }
        });

        // Initial setup
        updatePlayButtonState(); // Disable play button until selections are made
        video.style.display = 'block'; // Keep video element block, manage visibility via opacity/placeholder
        // Hide report and explanation using the class for transition
        perceptionReportDiv.style.display = 'none';
        explanationDiv.style.display = 'none';
         video.classList.remove('visible'); // Start video hidden via opacity
         videoPlaceholder.classList.remove('hidden'); // Start placeholder visible

    });
</script>
---
```