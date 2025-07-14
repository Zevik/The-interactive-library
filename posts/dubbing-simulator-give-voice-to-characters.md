---
title: "סימולטור דיבוב: תנו קול לדמויות!"
english_slug: dubbing-simulator-give-voice-to-characters
category: "אמנות ועיצוב / קולנוע"
tags: [דיבוב, אנימציה, סאונד, עשיית סרטים, סטודיו, סנכרון שפתיים]
---
# סימולטור דיבוב: תנו קול לדמויות!
דמיינו את עצמכם בסטודיו הקלטות מקצועי... סרט האנימציה האהוב עליכם רץ על המסך, והתפקיד שלכם הוא להפיח חיים בדמויות בשפה חדשה! זה נשמע קל, אבל האם תצליחו להתאים את הקול שלכם בדיוק לתנועות השפתיים ולרגש? היכנסו עכשיו לנעלי מדבבים מקצועיים וגלו את האתגר המרתק מאחורי הקלעים.

<div id="dubbing-app">
    <div class="video-container">
        <video id="dubbing-video" controls muted playsinline preload="metadata">
            <!-- Replace with an actual short animation clip URL -->
            <!-- Example placeholder src: https://interactive-tutorials.s3.eu-central-1.amazonaws.com/videos/placeholder_animation_clip.mp4 -->
            <source src="https://interactive-tutorials.s3.eu-central-1.amazonaws.com/videos/placeholder_animation_clip.mp4" type="video/mp4">
            המחשב שלך אינו תומך בהצגת וידאו.
        </video>
         <div class="recording-indicator">מקליט...</div>
    </div>

    <div class="controls">
        <button id="play-pause-btn" class="control-btn play">נגן / השהה</button>
        <button id="record-btn" class="control-btn record">הקלט</button>
        <button id="stop-record-btn" class="control-btn stop" disabled>עצור הקלטה</button>
        <button id="playback-btn" class="control-btn playback" disabled>האזן לדיבוב שלי</button>
    </div>

    <div class="timeline-container">
        <div id="timeline">
            <div id="progress"></div>
             <!-- Dynamic dialogue cues added here -->
        </div>
    </div>

    <div id="dialogue-display">
        <!-- Dialogue lines will appear here based on video time -->
        <p class="dialogue-line" data-time="1.5" data-duration="1.5">היי שם!</p>
        <p class="dialogue-line" data-time="3.0" data-duration="2.0">או! חשבתי שלא תגיע!</p>
        <p class="dialogue-line" data-time="5.5" data-duration="2.5">ברור שאגיע! יש הפתעה.</p>
        <p class="dialogue-line" data-time="8.0" data-duration="2.0">הפתעה? בשבילי?</p>
        <p class="dialogue-line" data-time="10.0" data-duration="2.0">במיוחד.</p>
    </div>

    <div id="message-area" class="message-area"></div>
</div>

<button id="toggle-explanation">רוצים לדעת עוד על דיבוב מקצועי?</button>

<div id="explanation" style="display: none;">
    <h2>הסבר: מאחורי קול הדמויות</h2>

    <h3>מהו דיבוב ומה מטרתו?</h3>
    <p>דיבוב הוא תהליך החלפת פס הקול המקורי של יצירה קולנועית (סרט, סדרת טלוויזיה, אנימציה וכו') בשפה אחרת. מטרתו העיקרית היא להנגיש את התוכן לקהל יעד שאינו דובר את שפת המקור, ולאפשר חוויית צפייה טבעית וסוחפת יותר בשפה המקומית, במיוחד עבור ילדים או קהלים שלא מעדיפים כתוביות.</p>

    <h3>השלבים המרכזיים בתהליך הדיבוב</h3>
    <ul>
        <li>**תרגום והתאמה (תרגום אדפטיבי):** לא מדובר רק בתרגום מילולי. התסריט מתורגם תוך התחשבות באורך המשפטים המקוריים ובתנועות השפתיים של הדמויות, כדי שהדיאלוג המתורגם יתאים בצורה הטובה ביותר ויזואלית וקצבית לנעשה על המסך. מתבצעות גם התאמות תרבותיות והומוריסטיות.</li>
        <li>**ליהוק שחקני קול:** נבחרים שחקנים שקולם וסגנון המשחק שלהם מתאימים לדמויות המקוריות ולדרישות התסריט המתורגם.</li>
        <li>**הקלטה בסטודיו:** שחקני הקול מקליטים את הדיאלוגים בסטודיו הקלטות. זהו השלב שדימתם בסימולטור. השחקנים צופים בקטע הווידאו ומתאימים את קולם ועיתוי ההקלטה שלהם לוויזואליה.</li>
        <li>**עריכה ומיקס סאונד:** פס הקול המוקלט עובר עריכה כדי לתקן שגיאות עיתוי, להוסיף אפקטים קוליים (SFX) שאינם קשורים לדיבור, ולהתאים את עוצמת הקול ואת האינטונציה. לבסוף, פס הקול החדש ממוקסס עם המוזיקה המקורית ועם אפקטי הסאונד המקוריים (או המחודשים) של הסרט ליצירת פס קול שלם.</li>
    </ul>

    <h3>האתגרים העיקריים בדיבוב</h3>
    <ul>
        <li>**סנכרון שפתיים (Lip Sync):** זהו אולי האתגר הגדול ביותר. יש להתאים את הדיאלוג החדש כמה שיותר לתנועות השפתיים המקוריות של הדמות. לעיתים קרובות דורש פשרות בתרגום או בניסוח כדי שהמשפטים יתאימו ויזואלית.</li>
        <li>**התאמת רגש ואינטונציה:** שחקן הדיבוב חייב לשמור על הביצוע הרגשי של הדמות המקורית, גם כשהוא מוגבל עיתית על ידי תנועות השפתיים והקצב המקורי.</li>
        <li>**שמירה על קצב ומקצב הדיאלוג המקורי:** הדיבוב צריך לזרום באופן טבעי ולהתאים לקצב הדיבור המקורי של הדמויות ולקצב העריכה של הסרט.</li>
        <li>**התאמה לתרבות היעד:** לעיתים נדרשות התאמות לא רק לשפה אלא גם להקשרים תרבותיים, הומור או מחוות ספציפיות.</li>
    </ul>

    <h3>כלים וטכניקות בהם משתמשים מקצועני דיבוב</h3>
    <p>מקצועני דיבוב משתמשים בתוכנות סטודיו מתקדמות המציגות את הווידאו, פס הקול המקורי (לרפרנס), ואת הדיאלוגים המתורגמים. טכניקות כמו 'קופסה' (Box Method) או 'לופ' (Looping) עוזרות לשחקנים לתרגל ולהתאים את הביצוע שלהם לקטעים קצרים שחוזרים על עצמם. תוכנות רבות מציגות גם Waveform (גל קול) של הדיבוב המקורי או המתורגם כדי לעזור בדיוק העיתוי.</p>

    <h3>חשיבות הדיבוב בחוויית הצפייה בסרטי אנימציה</h3>
    <p>דיבוב איכותי חיוני לחוויית צפייה מהנה ומובנת, במיוחד עבור קהל צעיר. הוא מאפשר חיבור רגשי לדמויות ומסיר את מחסום השפה, הופך את הסרט לנגיש יותר ומאפשר לצופים ליהנות מהוויזואליה המלאה ללא צורך בקריאת כתוביות. דיבוב טוב הוא אומנות בפני עצמה הדורשת כישרון, דיוק והבנה מעמיקה של הדמות והיצירה.</p>
</div>

<style>
    /* Color Palette & Typography */
    :root {
        --primary-color: #007bff; /* A vibrant blue */
        --secondary-color: #28a745; /* Success green */
        --danger-color: #dc3545; /* Danger red */
        --warning-color: #ffc107; /* Warning yellow */
        --info-color: #17a2b8; /* Info cyan */
        --light-bg: #f8f9fa; /* Very light grey */
        --dark-text: #343a40; /* Dark grey text */
        --muted-text: #6c757d; /* Muted grey text */
        --border-color: #dee2e6; /* Light grey border */
        --timeline-bg: #e9ecef; /* Slightly darker grey for timeline track */
        --timeline-progress: var(--primary-color);
        --dialogue-bg-active: #e0f7fa; /* Light cyan for active dialogue */
        --dialogue-border: var(--info-color);
        --box-shadow: rgba(0, 0, 0, 0.1);

        --font-family: 'Heebo', sans-serif; /* Using a common Israeli web font or similar */
    }

    /* Basic Reset and Typography */
    body {
        font-family: var(--font-family);
        line-height: 1.6;
        color: var(--dark-text);
        margin: 0;
        padding: 20px;
        background-color: var(--light-bg);
        direction: rtl;
        text-align: right;
    }

    h1, h2, h3 {
        color: var(--dark-text);
        margin-bottom: 15px;
    }

    p {
        margin-bottom: 10px;
    }

    /* App Container */
    #dubbing-app {
        max-width: 800px; /* Increased max-width for a better layout */
        margin: 20px auto;
        background-color: #ffffff; /* White background */
        border-radius: 12px; /* More rounded corners */
        padding: 25px; /* Increased padding */
        box-shadow: 0 8px 16px var(--box-shadow); /* Softer, larger shadow */
        display: flex;
        flex-direction: column;
        gap: 20px; /* Space between sections */
    }

    /* Video Container with Indicator */
    .video-container {
        position: relative;
        width: 100%;
        padding-bottom: 56.25%; /* 16:9 Aspect Ratio */
        height: 0;
        overflow: hidden;
        background-color: #000;
        border-radius: 8px; /* Rounded corners for video */
        box-shadow: inset 0 0 10px rgba(0,0,0,0.5); /* Inner shadow */
    }

    #dubbing-video {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }

    .recording-indicator {
        position: absolute;
        top: 10px;
        right: 10px; /* Position at top-right in RTL */
        background-color: var(--danger-color);
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
        font-size: 0.9em;
        font-weight: bold;
        z-index: 10; /* Above video */
        display: none; /* Hidden by default */
        animation: pulse 1.5s infinite;
    }

    @keyframes pulse {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.05); opacity: 0.8; }
        100% { transform: scale(1); opacity: 1; }
    }

    /* Controls */
    .controls {
        display: flex; /* Use flexbox for alignment */
        justify-content: center; /* Center buttons */
        gap: 10px; /* Space between buttons */
        margin-top: 10px; /* Space above controls */
    }

    .control-btn {
        padding: 12px 20px; /* More padding */
        font-size: 1em;
        cursor: pointer;
        border: none;
        border-radius: 25px; /* Pill shape */
        color: white;
        transition: background-color 0.2s ease, transform 0.1s ease;
        min-width: 100px; /* Minimum width for buttons */
        text-align: center;
    }

    .control-btn:hover:not(:disabled) {
        transform: translateY(-2px); /* Slight lift on hover */
    }

    .control-btn:active:not(:disabled) {
        transform: translateY(0); /* Push down on click */
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.2); /* Inner shadow on click */
    }

    .control-btn:disabled {
        background-color: var(--muted-text);
        cursor: not-allowed;
        opacity: 0.6;
        transform: none; /* No lift or push when disabled */
    }

    /* Specific Button Styles */
    .control-btn.play { background-color: var(--primary-color); }
    .control-btn.play:hover:not(:disabled) { background-color: #0056b3; }

    .control-btn.record { background-color: var(--danger-color); }
    .control-btn.record:hover:not(:disabled) { background-color: #c82333; }

    .control-btn.stop { background-color: var(--warning-color); color: var(--dark-text);}
    .control-btn.stop:hover:not(:disabled) { background-color: #e0a800; }

    .control-btn.playback { background-color: var(--secondary-color); }
    .control-btn.playback:hover:not(:disabled) { background-color: #218838; }

    /* Timeline */
    .timeline-container {
        width: 100%;
        margin-top: 10px; /* Space above timeline */
    }

    #timeline {
        width: 100%;
        height: 10px; /* Thicker timeline */
        background-color: var(--timeline-bg);
        border-radius: 5px;
        position: relative;
        cursor: pointer;
        overflow: hidden; /* Hide cues outside bounds */
    }

    #progress {
        height: 100%;
        width: 0%;
        background-color: var(--timeline-progress);
        border-radius: 5px;
        transition: width 0.1s linear; /* Smooth movement */
    }

    .dialogue-cue {
        position: absolute;
        top: 0; /* Align with top of timeline */
        width: 4px; /* Thicker cue */
        height: 100%; /* Full height of timeline */
        background-color: var(--info-color); /* Info color for cues */
        opacity: 0.7;
        transition: background-color 0.2s ease, opacity 0.2s ease;
        pointer-events: none;
        z-index: 2; /* Above progress bar */
    }

    .dialogue-cue.active {
         background-color: var(--warning-color); /* Highlight active cue */
         opacity: 1;
         width: 6px; /* Slightly wider when active */
    }


    /* Dialogue Display */
    #dialogue-display {
        min-height: 60px; /* Increased height */
        border: 2px dashed var(--dialogue-border); /* More prominent border */
        padding: 15px; /* Increased padding */
        border-radius: 8px;
        text-align: center;
        font-size: 1.3em; /* Larger font */
        color: var(--dark-text);
        background-color: var(--dialogue-bg-active); /* Light background */
        display: flex; /* Use flexbox */
        flex-direction: column; /* Stack lines vertically */
        justify-content: center; /* Center lines vertically */
        align-items: center; /* Center lines horizontally (RTL) */
        overflow: hidden; /* Prevent overflow */
        transition: background-color 0.3s ease;
    }

     /* Style for individual dialogue lines */
    .dialogue-line {
        margin: 3px 0; /* Adjust margin */
        padding: 2px 8px; /* Add padding */
        border-radius: 4px;
        transition: color 0.3s ease, font-weight 0.3s ease, background-color 0.3s ease, transform 0.3s ease;
        background-color: transparent;
        width: 100%; /* Take full width for centering */
        text-align: center;
    }

    .dialogue-line.active {
        font-weight: bold;
        color: var(--dark-text); /* Dark text for active */
        background-color: var(--warning-color); /* Warning color background for active */
        transform: scale(1.05); /* Subtle scale animation */
    }

     .dialogue-line.next {
        color: var(--muted-text); /* Muted color for upcoming */
        font-size: 0.9em; /* Slightly smaller for upcoming */
    }


    /* Message Area */
    .message-area {
        min-height: 25px; /* Slightly more space */
        text-align: center;
        font-weight: bold;
        margin-top: 10px; /* Space above message */
        opacity: 1;
        transition: opacity 0.3s ease, color 0.3s ease;
    }

    .message-area.info { color: var(--primary-color); }
    .message-area.success { color: var(--secondary-color); }
    .message-area.error { color: var(--danger-color); }
    .message-area.warning { color: var(--warning-color); }


    /* Explanation Toggle Button */
    #toggle-explanation {
         display: block;
         width: fit-content;
         margin: 30px auto 10px auto; /* More space above and below */
         padding: 12px 25px;
         font-size: 1.1em;
         cursor: pointer;
         border: none;
         border-radius: 25px; /* Pill shape */
         background-color: var(--muted-text);
         color: white;
         transition: background-color 0.2s ease, transform 0.1s ease;
    }

    #toggle-explanation:hover {
        background-color: #5a6268;
         transform: translateY(-2px);
    }

    #toggle-explanation:active {
         transform: translateY(0);
         box-shadow: inset 0 2px 4px rgba(0,0,0,0.2);
    }

    /* Explanation Section */
    #explanation {
        margin-top: 20px;
        border-top: 1px solid var(--border-color);
        padding-top: 20px;
        direction: rtl;
        text-align: right;
        color: var(--dark-text);
    }

    #explanation h2, #explanation h3 {
        color: var(--dark-text);
    }

    #explanation ul {
        list-style-type: disc;
        padding-right: 25px; /* More space for bullets */
    }

    #explanation li {
        margin-bottom: 10px;
    }

    /* Accessibility: Focus styles */
    button:focus, #timeline:focus, #toggle-explanation:focus {
        outline: 2px solid var(--primary-color);
        outline-offset: 3px;
    }
</style>

<script>
    const video = document.getElementById('dubbing-video');
    const playPauseBtn = document.getElementById('play-pause-btn');
    const recordBtn = document.getElementById('record-btn');
    const stopRecordBtn = document.getElementById('stop-record-btn');
    const playbackBtn = document.getElementById('playback-btn');
    const timeline = document.getElementById('timeline');
    const progress = document.getElementById('progress');
    const dialogueDisplay = document.getElementById('dialogue-display');
    const messageArea = document.getElementById('message-area');
    const toggleExplanationBtn = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const dialogueLines = dialogueDisplay.querySelectorAll('.dialogue-line');
    const recordingIndicator = document.querySelector('.recording-indicator');

    let mediaRecorder;
    let audioChunks = [];
    let recordedAudioBlob = null;
    let recordedAudioElement = null; // To hold the audio element for playback
    let isRecording = false;
    let isPlayingRecordedAudio = false; // Flag to track if user audio is playing

    // --- Helper to update message area with styling ---
    function showMessage(text, type = 'info') {
        messageArea.textContent = text;
        messageArea.className = 'message-area ' + type; // Reset and add class
        // Optional: Fade out message after a few seconds if not an error
        if (type !== 'error' && type !== 'warning') {
            // No auto-fade for critical messages
        }
    }

    function clearMessage() {
         messageArea.textContent = '';
         messageArea.className = 'message-area';
    }


    // --- Button State Management ---
    function updateButtonStates(state) {
        // State can be 'idle', 'playing_video', 'recording', 'playing_recorded'
        recordBtn.disabled = true;
        stopRecordBtn.disabled = true;
        playbackBtn.disabled = true;
        playPauseBtn.disabled = true; // Disable play/pause by default unless video is source

        recordingIndicator.style.display = 'none'; // Hide indicator by default

        switch (state) {
            case 'idle':
                 playPauseBtn.disabled = false;
                 recordBtn.disabled = false; // Can record when idle
                 playPauseBtn.textContent = video.paused ? 'נגן' : 'השהה'; // Update text based on video state
                 break;
            case 'playing_video':
                playPauseBtn.disabled = false;
                // recordBtn remains enabled if user wants to try recording over video? No, disable to avoid complexity.
                recordBtn.disabled = true;
                playPauseBtn.textContent = 'השהה';
                 break;
            case 'recording':
                stopRecordBtn.disabled = false;
                playPauseBtn.disabled = true; // Cannot control video with play/pause during recording
                 recordBtn.disabled = true; // Recording is active
                 recordingIndicator.style.display = 'block'; // Show indicator
                 break;
            case 'playing_recorded':
                 playPauseBtn.disabled = true; // Cannot control video during audio playback (synced)
                 // playbackBtn could be disabled while playing recorded audio
                 playbackBtn.disabled = true;
                 break;
            case 'loading':
                 showMessage('טוען וידאו...', 'info');
                 // Keep all buttons disabled
                 break;
             case 'ready':
                 // Initial state after loading
                 showMessage('לחצו "הקלט" כדי להתחיל!', 'info');
                 recordBtn.disabled = false;
                 playPauseBtn.disabled = false;
                 updateButtonStates('idle'); // Transition to idle
                 break;
            case 'error':
                 showMessage('אירעה שגיאה. נא רעננו את העמוד.', 'error');
                 // Keep all buttons disabled, or disable key ones
                 playPauseBtn.disabled = true;
                 recordBtn.disabled = true;
                 stopRecordBtn.disabled = true;
                 playbackBtn.disabled = true;
                 break;

        }
        // Post-recording, playback is available if audio exists
        if (recordedAudioBlob && state !== 'recording' && state !== 'playing_recorded') {
            playbackBtn.disabled = false;
        }
    }

    // --- Video Controls ---
    playPauseBtn.addEventListener('click', () => {
        if (video.paused || video.ended) {
            video.play();
            updateButtonStates('playing_video');
             clearMessage(); // Clear message on play
        } else {
            video.pause();
            updateButtonStates('idle');
        }
    });

    video.addEventListener('play', () => {
        playPauseBtn.textContent = 'השהה';
        if (!isPlayingRecordedAudio) { // Don't change state if playing recorded audio
            updateButtonStates('playing_video');
        }
    });

    video.addEventListener('pause', () => {
        playPauseBtn.textContent = 'נגן';
         if (!isPlayingRecordedAudio && !isRecording) { // Don't change state if recording or playing recorded audio
            updateButtonStates('idle');
         }
    });

    video.addEventListener('ended', () => {
        video.currentTime = 0; // Reset video
        progress.style.width = '0%'; // Reset progress
        // Stop any ongoing playback of user audio if video ends
        if (recordedAudioElement && !recordedAudioElement.paused) {
             recordedAudioElement.pause();
             recordedAudioElement.currentTime = 0;
        }
         updateDialogueDisplay(0); // Reset dialogue display
         isPlayingRecordedAudio = false; // Ensure flag is reset
         clearMessage();
         updateButtonStates('idle'); // Back to idle after video ends
    });

    video.addEventListener('timeupdate', () => {
        if (!isNaN(video.duration)) { // Check if duration is valid
            const progressPercent = (video.currentTime / video.duration) * 100;
            progress.style.width = progressPercent + '%';
            updateDialogueDisplay(video.currentTime);
        }
    });

    // Timeline click to seek - Corrected for RTL visual flow
    timeline.addEventListener('click', (e) => {
        if (video.duration && !isRecording && !isPlayingRecordedAudio) { // Disable seeking during recording/playback
            const rect = timeline.getBoundingClientRect();
            // Calculate distance from the right edge of the timeline
            const distanceFromRight = rect.right - e.clientX;
            // Calculate percentage from the right edge (0% at right, 100% at left)
            const percentFromRight = Math.max(0, Math.min(1, distanceFromRight / rect.width)); // Clamp between 0 and 1
            // Seek time is proportional to percentage from the right for RTL visual flow
            const seekTime = percentFromRight * video.duration;
            video.currentTime = seekTime;
             // No need to manually updateDialogueDisplay, timeupdate event handles it
        } else if (isRecording) {
             showMessage('לא ניתן לדלג קדימה או אחורה בזמן הקלטה.', 'warning');
        } else if (isPlayingRecordedAudio) {
             showMessage('לא ניתן לדלג קדימה או אחורה בזמן האזנה.', 'warning');
        }
    });


    // Add dialogue cues to timeline + handle initial button states
    video.addEventListener('loadedmetadata', () => {
        updateButtonStates('ready'); // Video is loaded and ready
        if (video.duration) {
            // Remove existing cues before adding (handles potential reload)
            timeline.querySelectorAll('.dialogue-cue').forEach(cue => cue.remove());

            dialogueLines.forEach(line => {
                const startTime = parseFloat(line.dataset.time);
                 // Calculate position from the right edge for RTL layout
                // Time 0 is at the right edge (0%), time = duration is at the left edge (100%)
                const rightPercent = (startTime / video.duration) * 100;
                const cue = document.createElement('div');
                cue.classList.add('dialogue-cue');
                cue.style.right = rightPercent + '%'; // Position from the right
                cue.title = `דיאלוג ב-${startTime.toFixed(1)} שנ'`; // Add tooltip
                timeline.appendChild(cue);
            });
        } else {
            showMessage('שגיאה בטעינת הוידאו (חסרה duration).', 'error');
            updateButtonStates('error');
        }
         // Initialize dialogue display on video load
         updateDialogueDisplay(0);
    });

     video.addEventListener('error', (e) => {
        console.error('Video error:', video.error);
        showMessage(`שגיאת וידאו: ${video.error.message || video.error.code}`, 'error');
         updateButtonStates('error');
    });


    // Update dialogue display and timeline cues based on video time
    function updateDialogueDisplay(currentTime) {
        const timelineCues = timeline.querySelectorAll('.dialogue-cue');
        dialogueLines.forEach((line, index) => {
            const startTime = parseFloat(line.dataset.time);
            const duration = parseFloat(line.dataset.duration);
            const endTime = startTime + duration;
            const cue = timelineCues[index]; // Get corresponding cue

            line.classList.remove('active', 'next');
            if (cue) cue.classList.remove('active');


            // Check if the line is currently active
            if (currentTime >= startTime && currentTime < endTime) {
                 line.classList.add('active');
                 if (cue) cue.classList.add('active'); // Highlight cue
            }
             // Check if the line is upcoming (within the next ~2 seconds)
            else if (currentTime < startTime && startTime < currentTime + 2) {
                 line.classList.add('next');
            }
        });
    }
    // Initialize dialogue display on video load/seek to 0
     video.addEventListener('seeked', () => updateDialogueDisplay(video.currentTime));
     // Initial call if video metadata is already loaded before script runs
     if (video.readyState >= 1) { // Check if metadata is loaded (HAVE_METADATA)
          updateButtonStates('ready');
          if (video.duration) {
              // Need to manually add cues if metadata was ready before event listener was added
               timeline.querySelectorAll('.dialogue-cue').forEach(cue => cue.remove()); // Clear any potential old cues
               dialogueLines.forEach(line => {
                   const startTime = parseFloat(line.dataset.time);
                   const rightPercent = (startTime / video.duration) * 100;
                   const cue = document.createElement('div');
                   cue.classList.add('dialogue-cue');
                   cue.style.right = rightPercent + '%';
                    cue.title = `דיאלוג ב-${startTime.toFixed(1)} שנ'`;
                   timeline.appendChild(cue);
               });
          } else {
               showMessage('שגיאה בטעינת הוידאו (חסרה duration).', 'error');
               updateButtonStates('error');
          }
          updateDialogueDisplay(0); // Initial display
     }


    // --- Recording Logic ---
    recordBtn.addEventListener('click', async () => {
        // Request microphone permission
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });

            mediaRecorder = new MediaRecorder(stream);
            audioChunks = [];
            recordedAudioBlob = null;
            recordedAudioElement = null; // Clear previous recording

            mediaRecorder.ondataavailable = event => {
                audioChunks.push(event.data);
            };

            mediaRecorder.onstop = () => {
                // Create blob and audio element
                recordedAudioBlob = new Blob(audioChunks, { type: 'audio/webm' }); // Use webm for broader compatibility
                const audioUrl = URL.createObjectURL(recordedAudioBlob);
                if (recordedAudioElement && recordedAudioElement.src) {
                    URL.revokeObjectURL(recordedAudioElement.src); // Clean up previous URL
                }
                recordedAudioElement = new Audio(audioUrl);

                 // Add event listener for playback end
                 recordedAudioElement.onended = () => {
                    console.log('Recorded audio ended');
                    isPlayingRecordedAudio = false;
                    video.pause(); // Ensure video stops if audio ends
                    video.currentTime = 0;
                    updateDialogueDisplay(0);
                    clearMessage();
                    updateButtonStates('idle'); // Back to idle state
                };


                showMessage('הקלטה הסתיימה בהצלחה! עכשיו אפשר להאזין לדיבוב שלך.', 'success');
                isRecording = false;
                 // Stop the microphone stream
                stream.getTracks().forEach(track => track.stop());
                 updateButtonStates('idle'); // Return to idle state, which will enable playback button
            };

            mediaRecorder.onerror = (event) => {
                console.error('MediaRecorder error:', event.error);
                showMessage(`שגיאת הקלטה: ${event.error.message}`, 'error');
                 isRecording = false;
                 // Attempt to stop stream if it's still active
                 stream.getTracks().forEach(track => track.stop());
                 updateButtonStates('idle'); // Return to idle state
            };


            // --- Start Recording Process ---
            video.pause(); // Pause video first
            video.currentTime = 0; // Go to the beginning for recording sync
            updateDialogueDisplay(0); // Reset dialogue display for sync

            showMessage('הקלטה החלה! תנו קול לדמויות... (עצור בכל רגע)', 'warning'); // Warning color for active recording state
             updateButtonStates('recording');

            // Use a small timeout to allow video seeking/UI update before starting recording and video playback
            setTimeout(() => {
                 try {
                    mediaRecorder.start();
                    video.play(); // Start video playback for sync
                    isRecording = true;
                 } catch (err) {
                     console.error('Error starting media recorder:', err);
                     showMessage('שגיאה בהתחלת ההקלטה.', 'error');
                     isRecording = false;
                      // Stop the microphone stream on error
                      stream.getTracks().forEach(track => track.stop());
                      updateButtonStates('idle'); // Return to idle state
                 }
            }, 200); // 200ms delay


        } catch (err) {
            console.error('Error accessing microphone:', err);
            if (err.name === 'NotAllowedError' || err.name === 'PermissionDeniedError') {
                showMessage('אין גישה למיקרופון. אנא אשרו גישה בהגדרות הדפדפן.', 'error');
            } else {
                 showMessage(`שגיאה בגישה למיקרופון: ${err.message}`, 'error');
            }
             updateButtonStates('idle'); // Ensure buttons are re-enabled appropriately
        }
    });

    stopRecordBtn.addEventListener('click', () => {
        if (mediaRecorder && mediaRecorder.state !== 'inactive') {
             showMessage('עוצר הקלטה...', 'info');
            mediaRecorder.stop(); // This triggers mediaRecorder.onstop
            video.pause(); // Stop video when recording stops
            isRecording = false;
             updateButtonStates('idle'); // UI updates will happen in onstop
        }
    });

    // --- Playback Logic ---
    playbackBtn.addEventListener('click', () => {
        if (recordedAudioElement && recordedAudioBlob) {
            // If video is playing, pause it first.
            if (!video.paused) {
                video.pause();
            }

            // Reset both video and audio to start
            video.currentTime = 0;
            if (recordedAudioElement.readyState > 0) { // Check if audio is loaded
                recordedAudioElement.currentTime = 0;
            } else {
                 // If audio element wasn't ready, wait for it
                 recordedAudioElement.onloadedmetadata = () => {
                      recordedAudioElement.currentTime = 0;
                      // Continue playback process here
                      startPlaybackSync();
                 };
                 // Trigger load if necessary (though setting src usually does it)
                 if (!recordedAudioElement.src) {
                      recordedAudioElement.src = URL.createObjectURL(recordedAudioBlob); // Should not be necessary if set in onstop
                 }
                 return; // Exit to wait for metadata
            }

             // Start playback synced
             startPlaybackSync();

        } else {
             showMessage('אין הקלטה להשמיע. אנא הקליטו קודם.', 'warning');
        }
    });

    function startPlaybackSync() {
        isPlayingRecordedAudio = true;
        showMessage('משמיע את הדיבוב שלך...', 'info');
        updateButtonStates('playing_recorded');

        // Attempt to start video and audio close together
        video.play().catch(err => {
            console.error('Error playing video during playback:', err);
             showMessage('שגיאה בניגון הוידאו.', 'error');
             isPlayingRecordedAudio = false;
             recordedAudioElement.pause(); // Stop audio too
             video.pause(); video.currentTime = 0;
             updateButtonStates('idle');
        });

        recordedAudioElement.play().catch(err => {
             console.error('Error playing recorded audio:', err);
             showMessage('שגיאה בהשמעת הדיבוב.', 'error');
             isPlayingRecordedAudio = false;
             video.pause(); // Stop video too
             video.currentTime = 0;
             updateButtonStates('idle');
        });

         // The onended event listener for recordedAudioElement handles cleanup and state change
         // Video ended listener also helps if video is shorter
    }


    // --- Explanation Toggle ---
    toggleExplanationBtn.addEventListener('click', () => {
        if (explanationDiv.style.display === 'none') {
            explanationDiv.style.display = 'block';
            toggleExplanationBtn.textContent = 'הסתר הסבר על דיבוב';
        } else {
            explanationDiv.style.display = 'none';
            toggleExplanationBtn.textContent = 'רוצים לדעת עוד על דיבוב מקצועי?';
        }
    });

    // --- Initial State ---
    updateButtonStates('loading'); // Set initial state to loading until video metadata is loaded

</script>
```