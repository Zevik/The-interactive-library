---
title: "גלו את הקשר: סיגמא או פאי במולקולות בתלת-ממד"
english_slug: identify-the-bond-sigma-or-pi-in-3d-molecules
category: "כימיה"
tags:
  - כימיה אורגנית
  - קשר קוולנטי
  - קשר סיגמא
  - קשר פאי
  - מבנה מולקולרי
---
# גלו את הקשר: סיגמא או פאי במולקולות בתלת-ממד

האם כל קשר כימי זהה? איך קשרים יחידים, כפולים ומשולשים שונים במרחב, ואיך נראה ההבדל הזה בתוך מולקולה תלת-ממדית? בואו לחקור את מבנה המולקולות בעצמכם ולחשוף את הסודות מאחורי קשרי הסיגמא והפאי!

<div id="app-container" class="interactive-area">
    <h2 class="section-title">חקירת מולקולה אינטראקטיבית</h2>
    <p class="intro-text">בחרו מולקולה מהרשימה, ולאחר מכן "לחצו" על סוג קשר במודל התלת-ממדי (באמצעות הכפתורים המדומים למטה) כדי ללמוד עליו.</p>

    <div class="controls-area">
        <div class="control-group">
            <label for="molecule-select" class="control-label">בחרו מולקולה:</label>
            <select id="molecule-select" class="control-select">
                <option value="ethane">אתאן (Ethane)</option>
                <option value="ethene">אתן (Ethene)</option>
                <option value="ethyne">אצטילן (Ethyne)</option>
                <!-- Add more molecules here -->
            </select>
        </div>
    </div>

    <div id="molecule-viewer" class="viewer-container">
        <!-- Placeholder for 3D molecule viewer -->
        <div class="viewer-placeholder">
            <p>מודל תלת-ממדי של המולקולה יופיע כאן.</p>
            <p>כדי להמשיך בחקירה (סימולציה), לחצו על כפתור המייצג את סוג הקשר במולקולה:</p>
            <div class="simulated-bond-buttons">
                <button class="simulated-bond" data-bond-id="sim-single" data-bond-type="single">קשר C-C יחיד</button>
                <button class="simulated-bond" data-bond-id="sim-double" data-bond-type="double">קשר C=C כפול</button>
                <button class="simulated-bond" data-bond-id="sim-triple" data-bond-type="triple">קשר C≡C משולש</button>
                 <button class="simulated-bond" data-bond-id="sim-ch" data-bond-type="single">קשר C-H יחיד</button>
            </div>
        </div>
    </div>

    <div id="bond-info-area" class="info-panel hidden">
        <h3 class="info-title">מידע על הקשר הנבחר:</h3>
        <p id="bond-description" class="info-text"></p>
        <p id="bond-type" class="info-text"></p>
        <p id="bond-composition" class="info-text"></p>
        <div class="info-composition">
             <span id="sigma-count"></span>
             <span id="pi-count"></span>
        </div>
    </div>
</div>

<button id="toggle-explanation" class="toggle-button">הצגת הסבר מפורט</button>

<div id="explanation" class="explanation-area hidden">
    <h2 class="section-title">הסבר מקיף: קשרי סיגמא (σ) ופאי (π)</h2>

    <p>כדי להבין את המבנה המרחבי והתכונות של מולקולות, חיוני להכיר את שני הסוגים העיקריים של קשרים קוולנטיים: סיגמא (σ) ופאי (π).</p>

    <h3 class="explanation-subtitle">קשר סיגמא (σ) - עמוד השדרה של הקשר</h3>
    <ul>
        <li>**היווצרות:** נוצר מחפיפה ישירה, "ראש בראש", בין אורביטלים אטומיים (s, p) או אורביטלים היברידיים (sp, sp², sp³). צפיפות האלקטרונים מרוכזת בדיוק על הציר המחבר את גרעיני האטומים.</li>
        <li>**תפקיד:** מהווה את הקשר היסודי והחזק ביותר בין שני אטומים. הוא תמיד קיים בכל סוג של קשר קוולנטי – יחיד, כפול או משולש.</li>
        <li>**גמישות:** קשרי סיגמא מאפשרים סיבוב חופשי יחסית של קבוצות אטומים סביב ציר הקשר, מה שמשפיע על התכונות הפיזיות וצורות הקיפול של מולקולות (קונפורמציות).</li>
         <li>**ייצוג ויזואלי (קונספטואלי):** <span class="bond-icon sigma-icon">σ</span></li>
    </ul>

    <h3 class="explanation-subtitle">קשר פאי (π) - התוספת שמונעת סיבוב</h3>
    <ul>
        <li>**היווצרות:** נוצר מחפיפה צידית, "צד לצד", של אורביטלי p לא מהונדסים, הניצבים לציר קשר הסיגמא. נוצרות שתי אזורים של צפיפות אלקטרונים – אחד מעל מישור הסיגמא ואחד מתחתיו.</li>
        <li>**תפקיד:** תמיד מופיע *בנוסף* לקשר סיגמא קיים. הוא "מדביק" את האטומים במקום ומונע סיבוב חופשי סביב הקשר.</li>
        <li>**מקום במולקולה:** קיים בקשרים כפולים (קשר פאי אחד) ובקשרים משולשים (שני קשרי פאי, הניצבים זה לזה).</li>
         <li>**ייצוג ויזואלי (קונספטואלי):** <span class="bond-icon pi-icon">π</span></li>
    </ul>

    <h3 class="explanation-subtitle">מבנה הקשר לפי סוג:</h3>
    <ul>
        <li>**קשר יחיד:** מורכב מ <span class="bond-icon sigma-icon">σ</span> אחד בלבד. (למשל C-C באתאן, C-H). מאפשר סיבוב.</li>
        <li>**קשר כפול:** מורכב מ <span class="bond-icon sigma-icon">σ</span> אחד + <span class="bond-icon pi-icon">π</span> אחד. (למשל C=C באתן). מקבע את המבנה למישור.</li>
        <li>**קשר משולש:** מורכב מ <span class="bond-icon sigma-icon">σ</span> אחד + <span class="bond-icon pi-icon">π</span> אחד + <span class="bond-icon pi-icon">π</span> אחד (שני קשרי פאי מאונכים). (למשל C≡C באצטילן). מקבע את המבנה לקו ישר.</li>
    </ul>

     <h3 class="explanation-subtitle">השפעה על מבנה וגיאומטריה:</h3>
     <p>קשרי פאי, בשל אופיים המקבע, מכתיבים גיאומטריה קשיחה יותר סביב האטומים המעורבים. קשרים כפולים גורמים למבנה מישורי, וקשרים משולשים למבנה לינארי (קווי) סביבם. קשר סיגמא לבדו מאפשר גיאומטריה טטרהדרלית או אחרת עם גמישות סיבוב משמעותית יותר.</p>
</div>

<style>
    /* General Body & Typography */
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f4f7f6;
        margin: 0;
        padding: 20px;
    }

    h1, h2, h3 {
        color: #0056b3;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    h1 {
        text-align: center;
        color: #003366;
        margin-bottom: 30px;
    }

    h2.section-title {
         border-bottom: 2px solid #007bff;
         padding-bottom: 5px;
         margin-bottom: 20px;
         color: #007bff;
    }

    h3.explanation-subtitle {
         color: #0056b3;
         margin-top: 20px;
         margin-bottom: 10px;
    }

    p {
        margin-bottom: 15px;
    }

    ul {
        margin-left: 25px;
        margin-bottom: 15px;
        padding-left: 0;
    }

    li {
        margin-bottom: 10px;
        line-height: 1.5;
    }

    /* App Container & Layout */
    #app-container {
        border: 1px solid #d1d9e6;
        padding: 30px;
        border-radius: 12px;
        margin: 20px auto;
        background-color: #ffffff;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        max-width: 800px;
    }

     .intro-text {
         margin-bottom: 25px;
         font-size: 1.1em;
         color: #555;
     }

    .controls-area {
        margin-bottom: 30px;
        padding: 15px;
        background-color: #eef2f7;
        border-radius: 8px;
    }

    .control-group {
        display: flex;
        align-items: center;
        gap: 15px;
    }

    .control-label {
        font-weight: bold;
        color: #003366;
    }

    .control-select {
        padding: 10px 15px;
        border: 1px solid #a0b0c9;
        border-radius: 5px;
        font-size: 1em;
        cursor: pointer;
        background-color: #fff;
        min-width: 180px;
    }

    .control-select:focus {
        outline: none;
        border-color: #007bff;
        box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
    }


    /* Molecule Viewer Placeholder */
    #molecule-viewer {
        width: 100%;
        height: 400px; /* Consistent height */
        border: 2px dashed #a0b0c9;
        border-radius: 8px;
        margin: 20px 0;
        background-color: #eef2f7; /* Light background for placeholder */
        display: flex;
        flex-direction: column; /* Arrange content vertically */
        justify-content: center;
        align-items: center;
        text-align: center;
        color: #666;
        font-style: italic;
        position: relative;
        overflow: hidden; /* Hide potential overflow */
    }

    .viewer-placeholder {
        padding: 20px;
        /* No dashed border here, it's on the parent */
    }

    .simulated-bond-buttons {
         margin-top: 20px;
    }

    .simulated-bond {
         margin: 5px;
         padding: 12px 20px;
         cursor: pointer;
         border: 1px solid #007bff;
         border-radius: 25px; /* Pill shape */
         background-color: #e9f5ff;
         color: #007bff;
         font-size: 1rem;
         transition: background-color 0.2s ease, transform 0.1s ease, box-shadow 0.2s ease;
         min-width: 150px; /* Ensure minimum width for consistency */
    }

     .simulated-bond:hover {
         background-color: #007bff;
         color: white;
         box-shadow: 0 2px 8px rgba(0, 123, 255, 0.3);
     }

     .simulated-bond:active {
         transform: scale(0.98);
     }

     .simulated-bond.selected {
         background-color: #0056b3;
         color: white;
         border-color: #0056b3;
         font-weight: bold;
         box-shadow: 0 3px 10px rgba(0, 86, 179, 0.4);
     }


    /* Bond Info Area */
    #bond-info-area {
        min-height: 120px; /* Give it more space */
        margin-top: 30px;
        padding: 20px;
        border: 1px solid #b8daff; /* Light blue border */
        border-radius: 8px;
        background-color: #e9f5ff; /* Light blue background */
        color: #004085; /* Dark blue text */
        box-shadow: 0 2px 8px rgba(0, 123, 255, 0.1);
        opacity: 0; /* Start hidden for fade-in */
        transform: translateY(10px); /* Start slightly lower for slide-up effect */
        transition: opacity 0.4s ease-out, transform 0.4s ease-out;
    }

     #bond-info-area.visible {
          opacity: 1;
          transform: translateY(0);
     }

    #bond-info-area .info-title {
        margin-top: 0;
        color: #004085;
        border-bottom: 1px dashed #a0b0c9;
        padding-bottom: 5px;
        margin-bottom: 15px;
    }

     #bond-info-area .info-text {
         margin-bottom: 8px;
     }

     .info-composition {
          margin-top: 10px;
          font-weight: bold;
     }

     /* Icons concept (using text for now) */
     .bond-icon {
         display: inline-block;
         width: 20px;
         height: 20px;
         line-height: 20px;
         text-align: center;
         border-radius: 50%;
         margin-right: 5px;
         font-size: 0.9em;
         font-weight: bold;
         color: white;
         vertical-align: middle;
     }

     .sigma-icon {
         background-color: #28a745; /* Green */
     }

     .pi-icon {
         background-color: #dc3545; /* Red */
     }


    /* Explanation Area */
    .explanation-area {
        border: 1px solid #d1d9e6;
        padding: 30px;
        border-radius: 12px;
        margin: 20px auto;
        background-color: #ffffff;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
         max-width: 800px;
    }

    .explanation-area h2 {
        margin-top: 0;
    }

    .explanation-area ul {
        list-style: disc;
    }


    /* Toggle Button */
    .toggle-button {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        cursor: pointer;
        border: none;
        border-radius: 25px;
        background-color: #007bff;
        color: white;
        font-size: 1.1em;
        transition: background-color 0.2s ease, transform 0.1s ease, box-shadow 0.2s ease;
    }

     .toggle-button:hover {
         background-color: #0056b3;
         box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
     }

     .toggle-button:active {
          transform: scale(0.98);
     }


    /* Utility */
    .hidden {
        display: none;
    }
</style>

<script>
    // --- Molecule Data ---
    const molecules = {
        ethane: {
            name: "אתאן (Ethane)",
            bonds: [
                { id: "c1-c2", type: "single", description: "קשר C-C יחיד", composition: { sigma: 1, pi: 0 } },
                { id: "c-h", type: "single", description: "קשר C-H יחיד", composition: { sigma: 1, pi: 0 } } // Representing all C-H as one type for sim
            ],
             simulatedBondMap: {
                 "sim-single": "c1-c2",
                 "sim-ch": "c-h"
             }
        },
        ethene: {
            name: "אתן (Ethene)",
            bonds: [
                { id: "c1=c2", type: "double", description: "קשר C=C כפול", composition: { sigma: 1, pi: 1 } },
                 { id: "c-h", type: "single", description: "קשר C-H יחיד", composition: { sigma: 1, pi: 0 } }
            ],
             simulatedBondMap: {
                 "sim-double": "c1=c2",
                 "sim-ch": "c-h"
             }
        },
        ethyne: {
            name: "אצטילן (Ethyne)",
            bonds: [
                { id: "c1#c2", type: "triple", description: "קשר C≡C משולש", composition: { sigma: 1, pi: 2 } },
                 { id: "c-h", type: "single", description: "קשר C-H יחיד", composition: { sigma: 1, pi: 0 } }
            ],
             simulatedBondMap: {
                 "sim-triple": "c1#c2",
                 "sim-ch": "c-h"
             }
        }
        // Add more molecules here following the same structure
    };

    // --- State Variables ---
    let currentMoleculeId = 'ethane';
    let currentBondInfo = null; // Store info of the currently selected bond

    // --- DOM Elements ---
    const moleculeSelect = document.getElementById('molecule-select');
    const moleculeViewer = document.getElementById('molecule-viewer');
    const bondInfoArea = document.getElementById('bond-info-area');
    const bondDescriptionEl = document.getElementById('bond-description');
    const bondTypeEl = document.getElementById('bond-type');
    const bondCompositionEl = document.getElementById('bond-composition');
    const sigmaCountEl = document.getElementById('sigma-count');
    const piCountEl = document.getElementById('pi-count');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const simulatedBondButtonsContainer = moleculeViewer.querySelector('.simulated-bond-buttons'); // Get container
    const simulatedBondButtons = simulatedBondButtonsContainer.querySelectorAll('.simulated-bond'); // Get all simulated buttons


    // --- Functions ---

    // Function to load a molecule (simulated)
    function loadMolecule(moleculeId) {
        currentMoleculeId = moleculeId;
        const molecule = molecules[moleculeId];
        console.log(`Loading molecule: ${molecule.name} (Simulated View)`);

        // Update visibility of simulated bonds based on the selected molecule
        simulatedBondButtons.forEach(button => {
             const simButtonId = button.dataset.bondId;
             // Check if this simulated button ID exists in the current molecule's map
             const isRelevant = molecule.simulatedBondMap.hasOwnProperty(simButtonId);
             button.style.display = isRelevant ? 'inline-block' : 'none';
             button.classList.remove('selected'); // Remove selected state on load
        });

        // Hide bond info area when loading new molecule
        hideBondInfo();
    }

    // Function to handle a simulated bond click
    function handleSimulatedBondClick(event) {
         const clickedButton = event.target;

         // Remove 'selected' class from all simulated bond buttons
         simulatedBondButtons.forEach(button => {
              button.classList.remove('selected');
         });

         // Add 'selected' class to the clicked button
         clickedButton.classList.add('selected');

         const simButtonId = clickedButton.dataset.bondId;
         const currentMol = molecules[currentMoleculeId];
         const bondIdToFind = currentMol.simulatedBondMap[simButtonId];

         if (!bondIdToFind) {
              console.error("Simulated bond ID not mapped for current molecule:", simButtonId);
              hideBondInfo();
              return;
         }

         // For C-H, all C-H bonds are represented by one simulated button,
         // so we find the generic C-H bond data. For others, find the specific bond.
         const bond = currentMol.bonds.find(b => b.id === bondIdToFind);


         if (bond) {
             displayBondInfo(bond);
         } else {
             console.error("Bond data not found for mapped ID:", bondIdToFind, "in molecule:", currentMoleculeId);
             hideBondInfo();
         }
    }

    // Function to display bond information
    function displayBondInfo(bond) {
        currentBondInfo = bond;
        bondDescriptionEl.textContent = `קשר: ${bond.description}`;
        const bondTypeMap = { single: 'יחיד', double: 'כפול', triple: 'משולש' };
        bondTypeEl.textContent = `סוג: ${bondTypeMap[bond.type] || bond.type}`;

         // Update composition text and add icons conceptually
         let compositionText = `הרכב: ${bond.composition.sigma} קשר סיגמא`;
         let sigmaIconHTML = `<span class="bond-icon sigma-icon">σ</span> × ${bond.composition.sigma}`;
         let piIconHTML = '';

         if (bond.composition.pi > 0) {
             compositionText += `, ${bond.composition.pi} קשר פאי`;
             piIconHTML = `<span class="bond-icon pi-icon">π</span> × ${bond.composition.pi}`;
         }

         bondCompositionEl.textContent = compositionText;

         // Update the separate spans for potential future visual use
         sigmaCountEl.innerHTML = sigmaIconHTML;
         piCountEl.innerHTML = piIconHTML;


        bondInfoArea.classList.remove('hidden');
        // Trigger the transition by adding a class after a small delay
        // This ensures the display: none is removed before opacity/transform transition applies
        requestAnimationFrame(() => {
             bondInfoArea.classList.add('visible');
        });
    }

     // Function to hide the bond info area
     function hideBondInfo() {
          bondInfoArea.classList.remove('visible');
           // Add 'hidden' class after the transition finishes
          bondInfoArea.addEventListener('transitionend', function handler() {
               bondInfoArea.classList.add('hidden');
               bondInfoArea.removeEventListener('transitionend', handler);
          });
          currentBondInfo = null;
          // Remove selected state from all buttons
          simulatedBondButtons.forEach(button => {
               button.classList.remove('selected');
          });
     }


    // --- Event Listeners ---

    // Molecule select change
    moleculeSelect.addEventListener('change', (event) => {
        loadMolecule(event.target.value);
    });

    // Simulated bond button clicks (using event delegation on the container)
    simulatedBondButtonsContainer.addEventListener('click', (event) => {
        if (event.target.classList.contains('simulated-bond')) {
             handleSimulatedBondClick(event);
        }
    });

    // Toggle explanation button click
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.classList.contains('hidden');
        if (isHidden) {
             explanationDiv.classList.remove('hidden');
             // Optional: Add a class for animation if desired, then remove
             toggleExplanationButton.textContent = 'הסתר הסבר מפורט';
        } else {
             explanationDiv.classList.add('hidden');
             toggleExplanationButton.textContent = 'הצגת הסבר מפורט';
        }
    });

    // --- Initialization ---
    loadMolecule(currentMoleculeId); // Load the initial molecule

</script>
---