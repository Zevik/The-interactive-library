---
title: "סימולטור נוירופלסטי: מסע המוח אל שפה חדשה"
english_slug: neuroplastic-simulator-the-brains-journey-to-a-new-language
category: "מדעי המוח"
tags:
  - למידת שפות
  - מדעי המוח
  - נוירופלסטיות
  - קוגניציה
  - פסיכולוגיה קוגניטיבית
---
<h1>סימולטור נוירופלסטי: מסע המוח אל שפה חדשה</h1>
<p>מוכנים למסע אל תוך הרשתות העצביות שלכם? בואו נגלה יחד מה באמת קורה במוח בזמן שהוא לומד שפה חדשה. אילו קשרים נבנים, אילו מתחזקים, ואיך תא עצב בודד מרגיש את תהליך הלמידה? נסו לחבר את המילה הזרה לתמונה המתאימה, ותראו איך הסינפסות במוח הוירטואלי שלכם מתחזקות!</p>

<!-- Interactive Application HTML -->
<div id="simulator-container">
    <div id="stimulus-area">
        <h2>קלט חדש:</h2>
        <div id="stimulus-display">
             <img id="stimulus-image" src="" alt="Stimulus Image">
             <div id="foreign-word" class="word interactive"></div>
        </div>
        <div id="selection-info"></div>
    </div>
    <div id="network-area">
        <div id="brain-input-point" class="input-indicator">קלט חושי</div>
        <svg id="network-svg"></svg>
        <!-- Concept nodes will be added here by JS -->
    </div>
     <div id="feedback"></div>
</div>

<button id="toggle-explanation">אני סקרן/ית! הצג לי את הסבר המדעי</button>

<!-- Hidden Explanation HTML -->
<div id="explanation-content" style="display: none;">
    <h2>הסבר: מסע המוח אל שפה חדשה</h2>
    <p>למידת שפה חדשה היא אחת המשימות המורכבות ביותר שהמוח האנושי יכול לבצע. היא דורשת קואורדינציה של מספר רב של אזורים מוחיים ויכולות קוגניטיביות שונות.</p>

    <h3>אזורי מפתח במוח המעורבים בעיבוד שפה</h3>
    <p>עיבוד שפה אינו מתבצע באזור בודד, אלא ברשת מורכבת של אזורים. שני אזורים מרכזיים הם:</p>
    <ul>
        <li><strong>אזור ברוקה:</strong> נמצא בקליפת המוח הקדמית (בדרך כלל בצד שמאל), ואחראי בעיקר על הפקת דיבור ותחביר. פגיעה באזור זה עלולה לגרום לקושי בהפקת שפה (אפזיית ברוקה).</li>
        <li><strong>אזור ורניקה:</strong> נמצא בקליפת המוח הרקתית (בדרך כלל בצד שמאל), ואחראי על הבנת שפה. פגיעה באזור זה עלולה לגרום לקושי בהבנת שפה (אפזיית ורניקה).</li>
    </ul>
    <p>אזורים נוספים חשובים כוללים את קליפת המוח השמיעתית (עיבוד צלילי שפה), קליפת המוח הראייתית (קריאה), הקורטקס הקדם-מצחי (זיכרון עבודה, קשב) ואזורים תת-קורטיקליים.</p>

    <h3>הבסיס הנוירוביולוגי של למידה: נוירונים, סינפסות ונוירופלסטיות</h3>
    <p>המוח בנוי ממיליארדי תאי עצב הנקראים נוירונים. נוירונים מתקשרים זה עם זה באמצעות קשרים הנקראים סינפסות. למידה וזיכרון מתרחשים ברמה הסינפטית. כאשר נוירון אחד מפעיל נוירון אחר באופן חוזר ונשנה, הקשר הסינפטי ביניהם מתחזק. תהליך זה, יחד עם יצירה וגיזום של סינפסות חדשות, הוא הביטוי התאי של <strong>נוירופלסטיות</strong> – היכולת של המוח לשנות את המבנה והתפקוד שלו בתגובה לניסיון ולמידה.</p>

    <h3>איך המוח לומד שפה חדשה בפועל?</h3>
    <p>כשאתם נחשפים למילה חדשה בשפה זרה (למשל, "gat" ברומנית) ולקשר שלה למושג שאתם כבר מכירים (תמונה של חתול), המוח שלכם מתחיל לבנות קשרים עצביים חדשים או לחזק קשרים קיימים. הסינפסות בין הנוירונים המייצגים את צליל/צורת המילה "gat", הנוירונים המייצגים את התמונה של החתול, והנוירונים המייצגים את המושג "חתול" בזיכרון שלכם, הופכים חזקים יותר. ככל שאתם נחשפים יותר לקשר הזה, הקשר הסינפטי מתחזק, ההפעלה בין הנוירונים הופכת מהירה ויעילה יותר, והזיהוי וההבנה של המילה הופכים אוטומטיים יותר. הדמיה זו מדגימה באופן פשטני את התחזקות הקשר בין "קלט" (המילה והתמונה) לבין "מושג" במוח (תא העצב המייצג את 'חתול').</p>

    <h3>תפקיד החשיפה, החזרתיות, ההקשר והשינה בגיבוש הזיכרון הלשוני</h3>
    <ul>
        <li><strong>חשיפה:</strong> היכרות ראשונית עם המילה והקשר שלה.</li>
        <li><strong>חזרתיות:</strong> הפעלה חוזרת ונשנית של אותם קשרים סינפטיים, חיונית לחיזוקם.</li>
        <li><strong>הקשר:</strong> למידה בתוך הקשר משמעותי (תמונה, משפט, שיחה) עוזרת לקשר את המילה לרשת קיימת של ידע ומקלה על הגיבוש.</li>
        <li><strong>שינה:</strong> תהליכי גיבוש זיכרון (קונסולידציה) מתרחשים באופן אינטנסיבי במהלך שינה, ומסייעים להפוך את המידע החדש לידע יציב וזמין.</li>
    </ul>

    <h3>הבדלים וקשיים אפשריים בלמידת שפה שנייה לעומת שפת אם</h3>
    <p>למידת שפת אם בילדות המוקדמת מתרחשת בתקופה קריטית (חלון קריטי) שבה המוח פלסטי במיוחד לשפה. למידת שפה שנייה בגיל מאוחר יותר עדיין אפשרית לחלוטין בזכות נוירופלסטיות, אך עשויה להיות שונה. לדוגמה, לעתים קרובות קשה יותר להגיע למבטא של דובר שפת אם, ואולי נדרש מאמץ מודע גדול יותר.</p>

    <h3>גורמים נוספים המשפיעים על יעילות הלמידה</h3>
    <p>גיל (אם כי הגיל המאוחר אינו חסם), מוטיבציה, סביבת הלמידה, איכות החשיפה (כמות ואיכות הקלט), אינטראקציה חברתית, ושיטות הלמידה בהן משתמשים - כולם משפיעים על יעילות למידת שפה חדשה.</p>

    <h3>סיכום: תובנות יישומיות לומדי שפות</h3>
    <p>הבנה שוב שלמידת שפה היא בנייה פיזית של קשרים במוח מדגישה את החשיבות של: <strong>חזרתיות מרווחת</strong> (spaced repetition), <strong>חשיפה מגוונת ועשירה</strong> (במיוחד הקשבה ודיבור), <strong>למידה פעילה</strong> (להשתמש בשפה ולא רק לצרוך אותה), ו<strong>סבלנות והתמדה</strong>. כל אינטראקציה עם השפה החדשה היא הזדמנות לחזק את הרשת העצבית שלכם!</p>
</div>

<!-- JavaScript Code -->
<script>
    const simulatorContainer = document.getElementById('simulator-container');
    const stimulusImage = document.getElementById('stimulus-image');
    const foreignWordDiv = document.getElementById('foreign-word');
    const networkArea = document.getElementById('network-area');
    const networkSVG = document.getElementById('network-svg');
    const feedbackDiv = document.getElementById('feedback');
    const selectionInfoDiv = document.getElementById('selection-info');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationContent = document.getElementById('explanation-content');
    const brainInputPoint = document.getElementById('brain-input-point');

    const conceptNodesData = [
        { concept: 'cat', label: 'מושג: חתול', x: 150, y: 150 },
        { concept: 'dog', label: 'מושג: כלב', x: 350, y: 150 },
        { concept: 'house', label: 'מושג: בית', x: 150, y: 300 },
        { concept: 'tree', label: 'מושג: עץ', x: 350, y: 300 },
        { concept: 'book', label: 'מושג: ספר', x: 250, y: 225 }
    ];

    const foreignWordsData = [
        { foreign: 'pisica', concept: 'cat', imageText: 'Cat', label: 'פיסיקה (רומנית)' },
        { foreign: 'caine', concept: 'dog', imageText: 'Dog', label: 'קאיינה (רומנית)' },
        { foreign: 'casa', concept: 'house', imageText: 'House', label: 'קאסה (רומנית)' },
        { foreign: 'copac', concept: 'tree', imageText: 'Tree', label: 'קופאק (רומנית)' },
        { foreign: 'carte', concept: 'book', imageText: 'Book', label: 'קארטה (רומנית)' }
        // Add more words for practice if desired
    ];

    const connectionStrengths = {};
    conceptNodesData.forEach(node => {
        // Initialize strength randomly for visual interest, or to 0 for pure learning demo
        connectionStrengths[node.concept] = Math.floor(Math.random() * 3); // Start with some random initial strength (0-2)
    });

    const maxStrength = 8; // Increase max strength for more visual levels
    const strengthIncrement = 1; // How much strength increases on correct answer

    let currentStimulus = null;
    let selectedForeignWordConcept = null; // Store only the concept of the selected word
    let selectedConceptNode = null; // Store the concept of the selected node

    const conceptNodeElements = {}; // Map concept name to DOM element
    const connectionLineElements = {}; // Map concept name to SVG line element

    // Helper to get position relative to #network-area
    function getRelativePosition(element) {
        const rect = element.getBoundingClientRect();
        const containerRect = networkArea.getBoundingClientRect();
        return {
            x: rect.left + rect.width / 2 - containerRect.left,
            y: rect.top + rect.height / 2 - containerRect.top
        };
    }

    function renderNetwork() {
        // Clear previous nodes and lines on initial render or full redraw (not ideal for animation)
        // Better: update existing elements if possible.

        // Initial render: create nodes
        if (Object.keys(conceptNodeElements).length === 0) {
             networkArea.querySelectorAll('.node').forEach(node => node.remove());
             conceptNodesData.forEach(nodeData => {
                const nodeElement = document.createElement('div');
                nodeElement.classList.add('node');
                nodeElement.id = `node-${nodeData.concept}`;
                nodeElement.dataset.concept = nodeData.concept;
                nodeElement.textContent = nodeData.label.replace('מושג: ', ''); // Shorter label in node
                nodeElement.style.left = `${nodeData.x}px`;
                nodeElement.style.top = `${nodeData.y}px`;
                networkArea.appendChild(nodeElement);
                conceptNodeElements[nodeData.concept] = nodeElement; // Store reference

                // Add click listener to concept nodes
                nodeElement.addEventListener('click', handleConceptClick);
            });
        }

        // Always re-draw/update lines based on current strength
        networkSVG.innerHTML = ''; // Clear all lines and redraw
        const inputPointPos = getRelativePosition(brainInputPoint);


        conceptNodesData.forEach(nodeData => {
            const nodeElement = conceptNodeElements[nodeData.concept];
            const nodeCenter = getRelativePosition(nodeElement);

            const strength = connectionStrengths[nodeData.concept] || 0;
            // Scale strength for visual properties
            const scaledStrength = Math.min(strength, maxStrength);
            const strokeWidth = 1 + scaledStrength * (5 / maxStrength); // Max thickness 6
            // Use HSL for color transition: e.g., light grey -> blue -> vibrant blue/purple
            // Hue: e.g., 200 (blue) or transition from grey (0, 0% sat) to blue (200, 100% sat)
            // Lightness: e.g., 80% (light) down to 40% (dark)
            // Saturation: e.g., 10% (greyish) up to 90% (vibrant)
            const hue = 220; // Blueish tone
            const saturation = 10 + scaledStrength * (80 / maxStrength); // From 10% to 90%
            const lightness = 85 - scaledStrength * (40 / maxStrength); // From 85% to 45%
            const strokeColor = `hsl(${hue}, ${saturation}%, ${lightness}%)`;

            const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
            line.setAttribute('x1', inputPointPos.x);
            line.setAttribute('y1', inputPointPos.y);
            line.setAttribute('x2', nodeCenter.x);
            line.setAttribute('y2', nodeCenter.y);
            line.setAttribute('stroke', strokeColor);
            line.setAttribute('stroke-width', strokeWidth);
             line.classList.add('connection-line'); // Add class for CSS transition
             line.dataset.concept = nodeData.concept; // Associate line with concept
            networkSVG.appendChild(line);
            connectionLineElements[nodeData.concept] = line; // Store reference
        });
    }

    function presentStimulus() {
        // Clear previous state
        selectedForeignWordConcept = null;
        selectedConceptNode = null;
        foreignWordDiv.classList.remove('selected', 'correct', 'incorrect');
        foreignWordDiv.style.cursor = 'pointer';
        foreignWordDiv.onclick = handleForeignWordClick; // Re-enable click
        feedbackDiv.textContent = 'לחץ על המילה הזרה, ואז על המושג המתאים ברשת:';
        selectionInfoDiv.textContent = '';

        // Remove highlight from all nodes
        networkArea.querySelectorAll('.node').forEach(node => {
            node.classList.remove('selected', 'correct', 'incorrect');
        });
         // Remove highlight from all lines
         networkSVG.querySelectorAll('.connection-line').forEach(line => {
             line.classList.remove('active-path', 'correct-path', 'incorrect-path');
         });


        // Get a stimulus that isn't too strong yet, or just random
        const availableStimuli = foreignWordsData.filter(item => connectionStrengths[item.concept] < maxStrength);

        if (availableStimuli.length === 0) {
             feedbackDiv.textContent = 'כל הקשרים חזקים מאוד! סיימת בהצלחה!';
             // Optional: Reset or add more words/concepts
             return;
        }

        currentStimulus = availableStimuli[Math.floor(Math.random() * availableStimuli.length)];

        // Update stimulus display
        stimulusImage.src = `https://via.placeholder.com/150x100?text=${currentStimulus.imageText}`;
        foreignWordDiv.textContent = currentStimulus.foreign;
        foreignWordDiv.dataset.concept = currentStimulus.concept; // Store correct concept on the word element
         foreignWordDiv.classList.add('interactive'); // Make it look clickable
    }

    function handleForeignWordClick() {
         if (selectedForeignWordConcept !== null) return; // Prevent double click

        selectedForeignWordConcept = this.dataset.concept;
        selectionInfoDiv.textContent = `נבחרה מילה זרה: "${this.textContent}"`;
        feedbackDiv.textContent = 'כעת בחר את המושג ברשת המוחית התואם:';
        this.classList.add('selected'); // Visual cue
        foreignWordDiv.style.cursor = 'default'; // Disable further clicks
        foreignWordDiv.onclick = null; // Remove handler

         // Highlight possible concept nodes (optional but nice touch)
         networkArea.querySelectorAll('.node').forEach(node => node.classList.add('awaiting-selection'));
    }

    function handleConceptClick() {
        if (selectedForeignWordConcept === null) {
            feedbackDiv.textContent = 'תחילה לחץ על המילה הזרה שמוצגת למעלה!';
            return;
        }
         // Prevent clicking the same node again immediately or clicking multiple nodes
        if (selectedConceptNode !== null) return;

        selectedConceptNode = this.dataset.concept;
        const clickedNodeElement = this; // Reference to the clicked node DOM element

        selectionInfoDiv.textContent += ` | נבחר מושג: "${this.textContent}"`;

        // Animate activation flow from input to selected node
        const selectedLine = connectionLineElements[selectedConceptNode];
         if (selectedLine) {
             selectedLine.classList.add('active-path');
         }
         clickedNodeElement.classList.add('active');


        if (selectedForeignWordConcept === selectedConceptNode) {
            // Correct match!
            feedbackDiv.textContent = 'נכון! קשר עצבי חדש התחזק!';
             foreignWordDiv.classList.add('correct');
             clickedNodeElement.classList.add('correct');
             if (selectedLine) {
                selectedLine.classList.add('correct-path');
                selectedLine.classList.remove('active-path');
             }


            // Increase strength
            connectionStrengths[selectedConceptNode] = Math.min(connectionStrengths[selectedConceptNode] + strengthIncrement, maxStrength);

            // Animate strength increase (CSS transition handles the visual part)
            // Re-render lines to update properties based on new strength
            setTimeout(() => {
                 renderNetwork(); // Redraw lines with updated strength
                 // Keep correct visual state briefly before resetting
                 foreignWordDiv.classList.remove('selected', 'correct');
                 clickedNodeElement.classList.remove('selected', 'correct', 'active', 'awaiting-selection');
                 if (selectedLine) selectedLine.classList.remove('correct-path', 'active-path');
                 presentStimulus(); // Present next stimulus
            }, 1500); // Short delay to see the change

        } else {
            // Incorrect match
            feedbackDiv.textContent = 'לא נכון. היתה הפעלה שגויה ברשת. נסה שוב לחבר את המילה למושג הנכון.';
             foreignWordDiv.classList.add('incorrect');
             clickedNodeElement.classList.add('incorrect');
              if (selectedLine) {
                selectedLine.classList.add('incorrect-path');
                 selectedLine.classList.remove('active-path');
             }


            // Reset state after a delay to allow user to read feedback
            setTimeout(() => {
                selectedForeignWordConcept = null;
                selectedConceptNode = null;
                selectionInfoDiv.textContent = ''; // Clear selection info on mistake
                foreignWordDiv.classList.remove('selected', 'incorrect'); // Reset visual state
                 foreignWordDiv.classList.add('interactive');
                foreignWordDiv.style.cursor = 'pointer'; // Re-enable click on word
                foreignWordDiv.onclick = handleForeignWordClick; // Re-attach handler

                 clickedNodeElement.classList.remove('selected', 'incorrect', 'active');
                 networkArea.querySelectorAll('.node').forEach(node => node.classList.remove('awaiting-selection')); // Remove highlight
                 if (selectedLine) selectedLine.classList.remove('incorrect-path', 'active-path');

                 // Optionally weaken incorrect connection slightly, or do nothing. Let's do nothing for simplicity here.
                 // connectionStrengths[selectedConceptNode] = Math.max(0, connectionStrengths[selectedConceptNode] - 0.5);
                 // renderNetwork(); // Re-render lines if weakening is implemented
            }, 2000); // Longer delay for incorrect feedback
        }
    }

    function toggleExplanation() {
        const isHidden = explanationContent.style.display === 'none';
        explanationContent.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'סגור את ההסבר המדעי' : 'אני סקרן/ית! הצג לי את הסבר המדעי';
    }

    // Initial setup
    renderNetwork(); // Draw initial network structure
    presentStimulus(); // Load the first word/image

    // Add event listener for the toggle button
    toggleExplanationButton.addEventListener('click', toggleExplanation);

    // Ensure SVG and input point dimensions are set before getting positions
     networkArea.style.position = 'relative'; // Ensure correct positioning context
    networkSVG.style.position = 'absolute';
    networkSVG.style.top = '0';
    networkSVG.style.left = '0';
    networkSVG.style.width = '100%';
    networkSVG.style.height = '100%';

     // Adjust brain input point position relative to network area
     brainInputPoint.style.position = 'absolute';
     brainInputPoint.style.top = '20px'; // Adjust as needed
     brainInputPoint.style.left = '50%';
     brainInputPoint.style.transform = 'translateX(-50%)';
     brainInputPoint.style.zIndex = 10; // Above SVG

     // Re-render network initially once elements are positioned
     setTimeout(renderNetwork, 50); // Small delay to ensure DOM is ready/measured

</script>

<!-- CSS Styling -->
<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap'); /* Optional: Use a better font */

    body {
        font-family: 'Heebo', Arial, sans-serif; /* Use Heebo first */
        line-height: 1.7; /* Slightly more relaxed line height */
        margin: 0; /* Remove default body margin */
        padding: 20px;
        direction: rtl; /* Hebrew support */
        text-align: right; /* Hebrew support */
        background-color: #eef2f7; /* Lighter, softer background */
        color: #333;
        overflow-x: hidden; /* Prevent horizontal scroll */
    }

    h1, h2, h3 {
        color: #1a4a8a; /* Deeper blue */
        text-align: center;
        margin-bottom: 15px;
    }

    h1 {
        margin-top: 0;
        font-size: 2.5em;
        font-weight: 700;
    }

    h2 {
         font-size: 1.8em;
         font-weight: 700;
    }

     h3 {
         font-size: 1.4em;
         font-weight: 700;
         margin-top: 20px;
         border-bottom: 2px solid #1a4a8a;
         padding-bottom: 5px;
         display: inline-block; /* Border only under text */
         margin-right: auto; /* Align border to the right in RTL */
         margin-left: 0;
    }


    p {
        margin-bottom: 15px;
    }

    #simulator-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 25px; /* Increased gap */
        border: none; /* Remove outer border */
        padding: 30px; /* More padding */
        background: linear-gradient(145deg, #ffffff, #f0f0f0); /* Subtle gradient */
        border-radius: 15px; /* More rounded corners */
        margin: 30px auto;
        max-width: 750px; /* Slightly wider */
        box-shadow: 0 10px 20px rgba(0,0,0,0.1); /* Stronger, softer shadow */
        overflow: hidden; /* Hide potential overflows from animations */
    }

    #stimulus-area {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 15px;
        border-bottom: 1px solid #d0d0d0; /* Softer separator */
        padding-bottom: 25px;
        width: 100%;
         box-sizing: border-box; /* Include padding in width */
    }

    #stimulus-display {
        display: flex;
        align-items: center;
        gap: 20px;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
        justify-content: center;
    }


    #stimulus-image {
        width: 180px; /* Larger image */
        height: 120px; /* Larger image */
        border: 2px solid #ddd; /* Softer border */
        border-radius: 8px;
        object-fit: cover;
        box-shadow: 0 4px 8px rgba(0,0,0,0.08); /* Shadow on image */
    }

    #foreign-word {
        font-size: 2em; /* Larger font */
        font-weight: 700; /* Bolder */
        color: #007bff;
        padding: 8px 15px; /* More padding */
        border: 2px solid #007bff; /* Match border to text color */
        border-radius: 30px; /* Pill shape */
        transition: background-color 0.3s ease, color 0.3s ease, transform 0.1s ease;
        background-color: rgba(0, 123, 255, 0.1); /* Light background tint */
    }

     #foreign-word.interactive {
         cursor: pointer;
     }

    #foreign-word.interactive:hover {
        background-color: #007bff;
        color: white;
        transform: translateY(-2px); /* Subtle lift effect */
         box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3);
    }

    #foreign-word.selected {
        background-color: #0056b3;
        color: white;
        border-color: #0056b3;
        cursor: default;
        transform: scale(1.05); /* Pop out slightly */
         box-shadow: 0 4px 8px rgba(0, 86, 179, 0.4);
    }

     #foreign-word.correct {
         background-color: #28a745; /* Green */
         color: white;
         border-color: #28a745;
         animation: pulse-correct 0.8s ease forwards; /* Animation */
     }

      #foreign-word.incorrect {
         background-color: #dc3545; /* Red */
         color: white;
         border-color: #dc3545;
          animation: shake 0.5s ease forwards; /* Animation */
     }


    #network-area {
        position: relative;
        width: 100%; /* Make width responsive */
        max-width: 650px; /* Max width for large screens */
        height: 450px; /* Increased height */
        border: 1px solid #e0e0e0;
        background: linear-gradient(160deg, #f8f9fa, #e9ecef); /* Soft background gradient */
        border-radius: 8px;
        margin-top: 20px;
        overflow: hidden; /* Hide SVG lines outside */
    }

     #brain-input-point {
         background-color: #007bff;
         color: white;
         padding: 5px 10px;
         border-radius: 5px;
         font-size: 0.9em;
         font-weight: bold;
         text-align: center;
         min-width: 80px;
         box-shadow: 0 2px 5px rgba(0,0,0,0.2);
         opacity: 0.9;
     }


    #network-svg {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none; /* Allow clicks to pass through to nodes */
        z-index: 1; /* Ensure SVG is behind nodes */
    }

    .connection-line {
        stroke: #ced4da; /* Initial light grey */
        stroke-width: 1.5; /* Slightly thicker initial line */
        transition: stroke-width 0.6s ease-out, stroke 0.6s ease-out; /* Smooth transition for strength */
        filter: drop-shadow(0 0 1px rgba(0,0,0,0.1)); /* Subtle shadow */
    }

     /* Animation for path highlighting */
     .connection-line.active-path {
        stroke: #ffc107; /* Yellow/Orange for active path */
        stroke-dasharray: 5, 5;
        animation: dash 1s linear infinite;
     }

     .connection-line.correct-path {
         stroke: #28a745; /* Green for correct path */
         stroke-width: 4; /* Thicker */
         animation: fade-out-correct-path 1s ease forwards;
     }

      .connection-line.incorrect-path {
         stroke: #dc3545; /* Red for incorrect path */
         stroke-width: 4; /* Thicker */
          animation: fade-out-incorrect-path 1s ease forwards;
     }


    .node {
        position: absolute;
        width: 120px; /* Wider nodes */
        height: 60px; /* Taller nodes */
        background-color: #e9ecef; /* Light background */
        border: 1px solid #adb5bd; /* Soft border */
        border-radius: 12px; /* More rounded */
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
        cursor: pointer;
        z-index: 10; /* Ensure nodes are above SVG lines */
        padding: 5px;
        box-sizing: border-box;
        transition: background-color 0.2s, border-color 0.2s, transform 0.1s, box-shadow 0.2s;
        font-size: 1em; /* Slightly larger font */
        color: #495057; /* Darker text */
         box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .node:hover {
         background-color: #d0d9e0; /* Lighter hover state */
         border-color: #868e96;
         transform: translateY(-3px); /* Lift effect on hover */
          box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }

     .node.awaiting-selection {
         border-color: #007bff;
         box-shadow: 0 0 8px rgba(0, 123, 255, 0.5);
         animation: pulse-border 1.5s infinite ease-in-out; /* Gentle pulse */
     }

     .node.active {
         transform: scale(1.1); /* Pop on click */
         box-shadow: 0 0 12px rgba(0, 123, 255, 0.8);
         background-color: #007bff;
         color: white;
         border-color: #007bff;
     }

      .node.correct {
          background-color: #28a745; /* Green */
          color: white;
          border-color: #28a745;
          animation: pop-correct 0.5s ease forwards; /* Quick pop/glow */
      }

       .node.incorrect {
           background-color: #dc3545; /* Red */
           color: white;
           border-color: #dc3545;
            animation: shake 0.5s ease forwards; /* Shake animation */
       }


    #feedback {
        margin-top: 15px;
        font-size: 1.2em; /* Larger feedback font */
        font-weight: bold;
        min-height: 1.5em; /* Ensure space */
        text-align: center;
        color: #1a4a8a; /* Match header color */
         transition: color 0.3s ease; /* Smooth color change */
    }

     #feedback.correct {
         color: #28a745; /* Green for correct */
     }

     #feedback.incorrect {
         color: #dc3545; /* Red for incorrect */
     }


    #selection-info {
        margin-top: 8px; /* More space */
        font-size: 1em; /* Slightly larger */
        color: #6c757d; /* Greyish color */
        min-height: 1.2em; /* Ensure space */
        text-align: center;
        font-style: italic;
    }


    #toggle-explanation {
        display: block;
        margin: 30px auto; /* More space */
        padding: 12px 20px; /* More padding */
        font-size: 1.1em; /* Larger font */
        cursor: pointer;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 25px; /* More rounded */
        transition: background-color 0.3s ease, transform 0.1s ease;
         box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3);
    }

    #toggle-explanation:hover {
        background-color: #0056b3;
        transform: translateY(-2px); /* Lift effect */
    }

     #toggle-explanation:active {
         transform: translateY(0); /* Press effect */
         box-shadow: 0 2px 4px rgba(0, 123, 255, 0.4);
     }


    #explanation-content {
        margin-top: 20px;
        padding: 20px; /* More padding */
        border: 1px solid #e0e0e0;
        background-color: #f8f9fa; /* Light background */
        border-radius: 10px; /* More rounded */
        max-width: 750px; /* Match simulator width */
        margin-left: auto;
        margin-right: auto;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08); /* Softer shadow */
    }

    #explanation-content ul {
        list-style-type: disc;
        margin-right: 20px; /* Indent list */
        margin-bottom: 15px;
         padding-right: 0; /* Ensure proper RTL list indent */
    }

    #explanation-content li {
        margin-bottom: 10px; /* More space between list items */
    }

    /* --- Animations --- */

    @keyframes pulse-border {
        0% { box-shadow: 0 0 8px rgba(0, 123, 255, 0.5); }
        50% { box-shadow: 0 0 12px rgba(0, 123, 255, 0.8); }
        100% { box-shadow: 0 0 8px rgba(0, 123, 255, 0.5); }
    }

    @keyframes shake {
        0% { transform: translateX(0); }
        25% { transform: translateX(-5px); }
        50% { transform: translateX(5px); }
        75% { transform: translateX(-5px); }
        100% { transform: translateX(0); }
    }

     @keyframes pulse-correct {
         0% { transform: scale(1); opacity: 1; }
         50% { transform: scale(1.05); opacity: 0.9; }
         100% { transform: scale(1); opacity: 1; }
     }

     @keyframes pop-correct {
          0% { transform: scale(1); box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
          50% { transform: scale(1.15); box-shadow: 0 0 15px rgba(40, 167, 69, 0.8); }
          100% { transform: scale(1); box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
     }


    @keyframes dash {
      to {
        stroke-dashoffset: -10;
      }
    }

    @keyframes fade-out-correct-path {
        0% { opacity: 1; stroke-width: 4; }
        100% { opacity: 0; stroke-width: 0; } /* Fade out and shrink */
    }

    @keyframes fade-out-incorrect-path {
        0% { opacity: 1; stroke-width: 4; }
        100% { opacity: 0; stroke-width: 0; } /* Fade out and shrink */
    }


     /* Media queries for basic responsiveness */
     @media (max-width: 768px) {
         #simulator-container {
             padding: 20px;
             gap: 20px;
         }
         #network-area {
             height: 350px;
         }
         .node {
             width: 90px;
             height: 50px;
             font-size: 0.9em;
             border-radius: 10px;
         }
         #stimulus-display {
             flex-direction: column;
             gap: 15px;
         }
         #foreign-word {
             font-size: 1.5em;
             padding: 6px 12px;
         }
         #stimulus-image {
             width: 150px;
             height: 100px;
         }
         h1 { font-size: 2em; }
         h2 { font-size: 1.5em; }
         h3 { font-size: 1.2em; }
          #feedback { font-size: 1em; }
          #selection-info { font-size: 0.9em; }
     }

     @media (max-width: 480px) {
          #network-area {
              height: 300px;
          }
          .node {
              width: 70px;
              height: 40px;
              font-size: 0.8em;
              border-radius: 8px;
          }
           #brain-input-point {
             padding: 3px 6px;
             font-size: 0.8em;
             min-width: 60px;
           }
     }


</style>
---
```