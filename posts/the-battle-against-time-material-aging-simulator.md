---
title: "הקרב נגד הזמן: סימולטור התבלות חומרים"
english_slug: the-battle-against-time-material-aging-simulator
category: "הנדסת חומרים"
tags: ["הזדקנות חומרים", "קורוזיה", "עייפות החומר", "הנדסת חומרים", "תחזוקה", "סימולציה", "אינטראקטיבי"]
---
# הקרב נגד הזמן: סימולטור התבלות חומרים

האם עצרתם פעם לחשוב מדוע מבנים עתיקים עומדים במשך מאות שנים, בעוד גשרים מודרניים דורשים תחזוקה בלתי פוסקת? מהם הכוחות הנסתרים שפושטים במעלה עמודי בטון או אוכלים בשקט את מתכת הגשרים? צללו לתוך העולם המרתק של התבלות חומרים וגלו כיצד הזמן וגורמי סביבה בלתי נראים משפיעים על עמידות החומרים שסביבנו, וכיצד מהנדסים נאבקים ב"קרב נגד הזמן".

<div class="aging-simulator">
    <h2>סימולטור התבלות חומרים אינטראקטיבי</h2>

    <div class="controls-grid">
        <div class="control-group">
            <label for="material-select">בחר את החומר במבחן:</label>
            <select id="material-select">
                <option value="steel">פלדה</option>
                <option value="concrete">בטון מזוין</option>
                <option value="aluminum">אלומיניום (סגסוגת מבנית)</option>
            </select>
        </div>

        <div class="control-group">
            <label>בחר את התנאים הסביבתיים הקשים:</label>
            <div class="env-checkboxes">
                <div><input type="checkbox" id="env-humidity" value="humidity"> <label for="env-humidity"><i class="fas fa-water"></i> לחות גבוהה / גשם</label></div>
                <div><input type="checkbox" id="env-salt" value="salt"> <label for="env-salt"><i class="fas fa- кораблик"></i> מים מלוחים / אוויר ים</label></div>
                <div><input type="checkbox" id="env-cyclic-load" value="cyclic-load"> <label for="env-cyclic-load"><i class="fas fa-sync-alt"></i> עומס מחזורי / ויברציות</label></div>
                <div><input type="checkbox" id="env-temperature" value="temperature"> <label for="env-temperature"><i class="fas fa-temperature-high"></i> טמפרטורה קיצונית / מחזורי קור-חום</label></div>
            </div>
        </div>

        <div class="control-group slider-group">
            <label for="time-slider">הרץ את סימולציית הזמן (שנים): <span id="current-year">0</span></label>
            <input type="range" id="time-slider" min="0" max="100" value="0">
        </div>
    </div>

    <div class="simulation-area">
        <div class="material-sample" id="material-sample">
            <!-- Visual representation of the material sample will be here -->
            <div class="sample-overlay rust-overlay"></div>
            <div class="sample-overlay cracks-overlay"></div>
             <div class="sample-overlay spalling-overlay"></div> <!-- Added spalling overlay for concrete -->
        </div>
        <div class="integrity-display">
            <span>שלמות מבנית:</span> <span id="integrity-value">100%</span>
            <div class="integrity-bar-container">
                <div class="integrity-bar" id="integrity-bar" style="width: 100%;"></div>
            </div>
        </div>
    </div>
     <div class="feedback-message" id="feedback-message"></div> <!-- Added feedback area -->
</div>

<button id="toggle-explanation">? למה זה קורה? גלה את המנגנונים מאחורי התבלות החומרים</button>

<div id="aging-explanation" style="display: none;">
    <h2>התבלות חומרים: מנגנונים ודרכי התמודדות</h2>

    <h3>מבוא: מהי התבלות חומרים ומדוע היא קריטית?</h3>
    <p>התבלות חומרים (Degradation or Aging) היא תהליך טבעי ובלתי נמנע שבו חומרים, כמו מתכות ובטון, מאבדים בהדרגה את חוזקם, עמידותם ותכונותיהם המקוריות. תהליך זה נגרם מחשיפה לגורמי סביבה כמו לחות, טמפרטורה, מלחים, קרינה ועומסים מכניים חוזרים. הבנת מנגנוני ההתבלות אינה רק תיאורטית - היא קריטית להבטחת בטיחות מבנים ותשתיות, תכנון מוצרים עם אורך חיים סביר, ופיתוח אסטרטגיות תחזוקה יעילות.</p>

    <h3>שני מנגנוני התבלות הרסניים:</h3>

    <h4>קורוזיה (שיתוך): התקפה כימית ואלקטרוכימית</h4>
    <p><strong>מהי קורוזיה?</strong> קורוזיה היא תהליך הידרדרות כימי או אלקטרוכימי של חומר, לרוב מתכת, כתוצאה מתגובה עם סביבתו. התהליך המוכר ביותר הוא חלודה – חמצון ברזל בפלדה בנוכחות מים וחמצן. תהליך זה הופך את המתכת לתרכובות פחות יציבות וחלשות יותר.</p>
    <p><strong>סוגים נפוצים של קורוזיה:</strong></p>
    <ul>
        <li><strong>חלודה:</strong> ספציפית לברזל ופלדה. התוצר הנקבובי (חלודה) אינו מגן על המתכת שמתחתיו ומאפשר לתהליך להתקדם לעומק.</li>
        <li><strong>קורוזיה גלוונית:</strong> נגרמת ממגע בין שתי מתכות שונות בסביבה לחה. המתכת הפחות אצילה (יותר אקטיבית) מתנהגת כאנודה ונאכלת מהר יותר, בעוד המתכת היותר אצילה מוגנת.</li>
        <li><strong>קורוזיית חריצים ובורות:</strong> מתרחשת באזורים מוגבלים (חריצים, סדקים, מתחת לברגים) שבהם יש קושי בזרימת חמצן, מה שיוצר הפרשי ריכוזים ומאיץ קורוזיה מקומית.</li>
        <li><strong>קורוזיה בבטון:</strong> למרות שבטון אינו מתכת, סביבה קורוזיבית (למשל, חדירת כלורידים ממי ים) יכולה לגרום לקורוזיה של מוטות הפלדה (זיון) בתוכו. התוצר של קורוזיית הזיון (חלודה) תופח בנפחו, יוצר לחצים פנימיים בבטון וגורם לסדיקה והתפוררות (Spalling) של הבטון עצמו.</li>
    </ul>
    <p><strong>גורמים מאיצי קורוזיה:</strong> לחות, מלחים (במיוחד כלורידים), חומציות, טמפרטורה גבוהה, מזהמים באוויר/מים.</p>

    <h4>עייפות החומר (Fatigue): כשל שקט מעומס מחזורי</h4>
    <p><strong>מהי עייפות החומר?</strong> זוהי תופעה שבה חומר נכשל פתאומית לאחר שנחשף למספר רב של מחזורי העמסה (מאמצים) שהם נמוכים משמעותית מחוזק הקריעה שלו במשיכה סטטית. כשל עייפות הוא הסיבה הנפוצה ביותר לכשל ברכיבים מכניים ומבניים הנמצאים תחת עומסים משתנים (כמו כנפי מטוסים, גשרים, חלקי מכונות).</p>
    <p><strong>התפתחות כשל עייפות:</strong></p>
    <ul>
        <li><strong>התחלה:</strong> סדקי עייפות מתחילים לרוב בנקודות ריכוז מאמץ קטנות (פגמים על פני השטח או בתוך החומר).</li>
        <li><strong>התקדמות:</strong> כל מחזור העמסה פותח ומזיז את קצות הסדק מעט, מה שגורם לו לגדול בהדרגה. התקדמות זו יוצרת סימנים אופייניים הנראים כמו "פסים" על משטח השבר.</li>
        <li><strong>כשל סופי:</strong> כאשר הסדק מגיע לגודל קריטי, השטח הנותר של הרכיב אינו מסוגל לשאת את העומס, ומתרחש כשל סופי מהיר ושביר, לרוב ללא אזהרה מוקדמת.</li>
    </ul>
    <p><strong>גורמים המשפיעים על עייפות:</strong> גודל טווח המאמץ במחזור, מספר מחזורי ההעמסה, סוג החומר, מצב פני השטח (חספוס, שריטות), טמפרטורה וסביבה קורוזיבית (השילוב נקרא Corrosion Fatigue והוא הרסני במיוחד).</p>

    <h3>מנגנוני התבלות חשובים נוספים:</h3>
    <ul>
        <li><strong>בלאי ושחיקה (Wear & Abrasion):</strong> הסרת חומר ממשטחים במגע עקב תנועה יחסית.</li>
        <li><strong>סחיפה (Erosion):</strong> הסרת חומר עקב פגיעת חלקיקים הנישאים בנוזל או גז.</li>
        <li><strong>זחילה (Creep):</strong> דפורמציה איטית תחת עומס קבוע בטמפרטורות גבוהות.</li>
        <li><strong>התפרקות מפגעי טמפרטורה/קרינה:</strong> שינויים מבניים או כימיים הנגרמים מחום קיצוני, קור קיצוני או קרינה (UV, גרעינית).</li>
    </ul>

    <h3>אסטרטגיות הנדסיות למאבק בהתבלות:</h3>
    <p>מהנדסים משתמשים במגוון שיטות להאטת או מניעת התבלות, ולהארכת חיי השירות של רכיבים ומבנים:</p>
    <ul>
        <li><strong>בחירת חומרים:</strong> שימוש בסגסוגות עמידות לקורוזיה (נירוסטה, אלומיניום מיוחד), חומרים בעלי גבול עייפות גבוה, או פולימרים עמידים לקרינה/כימיקלים.</li>
        <li><strong>הגנות פני שטח:</strong> צבעים וציפויים (מחסום לסביבה), טיפולי שטח לשיפור עמידות לעייפות (כמו Shot Peening), ציפויי מתכת או קרמיקה.</li>
        <li><strong>הגנה קתודית ואנודות הקרבה:</strong> שיטות אלקטרוכימיות להגנה על מתכות, נפוצות בצנרת תת-קרקעית, ספינות ומבני חוף.</li>
        <li><strong>תכנון קפדני:</strong> הימנעות מפינות חדות וריכוזי מאמץ, תכנון ניקוז יעיל, הפרדה בין מתכות שונות בסביבה קורוזיבית.</li>
        <li><strong>תחזוקה וניטור:</strong> בדיקות לא הרסניות (NDT), זיהוי מוקדם של סדקים וקורוזיה, תיקונים יזומים.</li>
    </ul>

    <p>הקרב נגד הזמן הוא מאבק מתמשך בהנדסה. על ידי הבנה ויישום עקרונות התבלות, אנו יכולים לבנות עולם בטוח ועמיד יותר.</p>
</div>

<script>
    const materialSelect = document.getElementById('material-select');
    const envCheckboxes = document.querySelectorAll('.controls-grid input[type="checkbox"]');
    const timeSlider = document.getElementById('time-slider');
    const currentYearSpan = document.getElementById('current-year');
    const materialSampleDiv = document.getElementById('material-sample');
    const integrityValueSpan = document.getElementById('integrity-value');
    const integrityBar = document.getElementById('integrity-bar');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const agingExplanationDiv = document.getElementById('aging-explanation');
    const rustOverlay = materialSampleDiv.querySelector('.rust-overlay');
    const cracksOverlay = materialSampleDiv.querySelector('.cracks-overlay');
    const spallingOverlay = materialSampleDiv.querySelector('.spalling-overlay');
    const feedbackMessageDiv = document.getElementById('feedback-message');


    // Base integrity loss rate per year (minimal aging without factors)
    const BASE_AGING_RATE = 0.05; // Reduced base rate

    // Aging factors weights (how much each environment factor contributes for each material per year)
    const AGING_WEIGHTS = {
        steel: {
            humidity: 0.7, // Increases corrosion
            salt: 1.8, // Significantly increases corrosion (rust)
            cyclic_load: 1.5, // Causes fatigue cracking
            temperature: 0.2 // Minor effect, maybe accelerates other processes
        },
        concrete: {
            humidity: 0.1, // Can contribute indirectly via rebar corrosion or freeze-thaw
            salt: 2.5, // Major cause of rebar corrosion & spalling (chloride attack)
            cyclic_load: 0.8, // Causes micro-cracking and reduces integrity
            temperature: 1.2 // Thermal cycling causes cracking, freeze-thaw damage
        },
        aluminum: {
            humidity: 0.2, // Can cause minor surface corrosion
            salt: 1.5, // Causes pitting or galvanic corrosion depending on alloy
            cyclic_load: 1.9, // Highly susceptible to fatigue cracking
            temperature: 0.3 // Minor effect
        }
    };

    // Mapping of damage types to visual overlays and factors
    const DAMAGE_TYPES = {
        rust: {
            materials: ['steel'],
            factors: ['humidity', 'salt'],
            overlay: rustOverlay
        },
        cracks: {
            materials: ['steel', 'aluminum', 'concrete'],
            factors: ['cyclic-load', 'temperature'], // Temp can cause thermal cracks
            overlay: cracksOverlay
        },
         spalling: { // Concrete specific damage
            materials: ['concrete'],
            factors: ['salt', 'temperature', 'humidity'], // Salt/Freeze-thaw major causes
            overlay: spallingOverlay
         }
    };

    // Visual feedback thresholds
    const DAMAGE_LEVELS = {
        low: { threshold: 20, message: "סימני התבלות ראשונים נראים." }, // 20% damage = 80% integrity
        medium: { threshold: 50, message: "החומר מתחיל להיחלש באופן משמעותי." }, // 50% damage = 50% integrity
        high: { threshold: 80, message: "החומר קרוב לכשל קטסטרופלי!" } // 80% damage = 20% integrity
    };

    // Keep track of displayed message to avoid repetition
    let lastMessage = "";

    function updateSimulation() {
        const material = materialSelect.value;
        const years = parseInt(timeSlider.value);
        currentYearSpan.textContent = years;

        // Hide all overlays initially
        rustOverlay.style.opacity = 0;
        cracksOverlay.style.opacity = 0;
        spallingOverlay.style.opacity = 0;

        // Reset filter
        materialSampleDiv.style.filter = 'none';

        let totalAgingRate = BASE_AGING_RATE;
        const activeFactors = {};
        const activeFactorTypes = []; // Track the types of damage likely occurring

        envCheckboxes.forEach(checkbox => {
            if (checkbox.checked) {
                activeFactors[checkbox.value] = true;
                 const weightKey = checkbox.value.replace('-', '_'); // e.g., 'cyclic-load' -> 'cyclic_load'
                 if (AGING_WEIGHTS[material] && AGING_WEIGHTS[material][weightKey] !== undefined) {
                    totalAgingRate += AGING_WEIGHTS[material][weightKey];
                 }

                 // Add factor types to active types list
                 for (const type in DAMAGE_TYPES) {
                     if (DAMAGE_TYPES[type].materials.includes(material) && DAMAGE_TYPES[type].factors.includes(checkbox.value)) {
                         if (!activeFactorTypes.includes(type)) {
                            activeFactorTypes.push(type);
                         }
                     }
                 }
            }
        });

        // Calculate integrity loss. Using a slightly less linear model, maybe power of time?
        // Let's stick closer to the original structure but scale the rate and effect.
        // integrity = 100 - totalAgingRate * years * scaleFactor;
        // A simple model where integrity decreases faster over time with higher rates:
        const damagePercentage = Math.min(100, totalAgingRate * years * 0.7); // Scale factor adjusted for visual pace
        let integrity = 100 - damagePercentage;


        integrityValueSpan.textContent = `${Math.round(integrity)}%`;
        integrityBar.style.width = `${integrity}%`;

        // Update integrity bar color
        if (integrity > 70) {
            integrityBar.style.backgroundColor = '#28a745'; // Green
        } else if (integrity > 30) {
            integrityBar.style.backgroundColor = '#ffc107'; // Orange/Yellow
        } else {
            integrityBar.style.backgroundColor = '#dc3545'; // Red
        }

        // --- Apply Visual Damage Effects ---
        const damageLevelNormalized = damagePercentage / 100; // Value between 0 and 1

        // General degradation filter (makes sample look older/worn)
        materialSampleDiv.style.filter = `grayscale(${damageLevelNormalized * 0.5}) brightness(${1 - damageLevelNormalized * 0.2})`; // Adjust based on damage

        // Apply specific overlays based on material and active factor types
        activeFactorTypes.forEach(type => {
            const config = DAMAGE_TYPES[type];
            if (config && config.overlay) {
                let intensity = damageLevelNormalized; // Base intensity from total damage

                // Adjust intensity based on how relevant the *active* factors are to this specific damage type
                // This is a heuristic: If salt is active for steel rust, increase rust intensity
                let factorSpecificBoost = 0;
                if (type === 'rust' && (activeFactors.humidity || activeFactors.salt)) {
                     factorSpecificBoost = (activeFactors.humidity ? 0.3 : 0) + (activeFactors.salt ? 0.7 : 0); // Salt boosts more
                } else if (type === 'cracks' && (activeFactors['cyclic-load'] || activeFactors.temperature)) {
                     factorSpecificBoost = (activeFactors['cyclic-load'] ? 0.6 : 0) + (activeFactors.temperature ? 0.4 : 0);
                } else if (type === 'spalling' && (activeFactors.salt || activeFactors.temperature)) {
                     factorSpecificBoost = (activeFactors.salt ? 0.8 : 0) + (activeFactors.temperature ? 0.5 : 0); // Salt and Temp major for spalling
                }
                 intensity = Math.min(1, intensity + factorSpecificBoost * damageLevelNormalized); // Add boost, max 1

                config.overlay.style.opacity = intensity;

                // Optional: Adjust overlay appearance based on intensity (e.g., size of cracks pattern)
                if (type === 'cracks' || type === 'spalling') {
                     // Example: Make crack pattern appear denser or larger
                     // This requires modifying background-size or other properties dynamically.
                     // For simplicity, let's primarily rely on opacity and potential pattern differences via CSS classes.
                }
            }
        });


        // --- Display Feedback Messages ---
        let currentMessage = "";
        if (damagePercentage >= DAMAGE_LEVELS.high.threshold) {
            currentMessage = DAMAGE_LEVELS.high.message;
        } else if (damagePercentage >= DAMAGE_LEVELS.medium.threshold) {
            currentMessage = DAMAGE_LEVELS.medium.message;
        } else if (damagePercentage >= DAMAGE_LEVELS.low.threshold) {
            currentMessage = DAMAGE_LEVELS.low.message;
        } else {
             currentMessage = "החומר שומר על שלמותו במצב זה.";
        }

        if (currentMessage !== lastMessage || years === 0) {
            feedbackMessageDiv.textContent = currentMessage;
            feedbackMessageDiv.style.opacity = 1;
            // Optional: Add a subtle pulse or animation on message change
        }
         lastMessage = currentMessage;

         if (years === 0) {
             feedbackMessageDiv.textContent = "התחל את הסימולציה על ידי הזזת סרגל הזמן.";
             lastMessage = feedbackMessageDiv.textContent; // Reset last message for year 0
         }


    }

    // Event listeners
    materialSelect.addEventListener('change', updateSimulation);
    envCheckboxes.forEach(checkbox => checkbox.addEventListener('change', updateSimulation));
    timeSlider.addEventListener('input', updateSimulation); // Use 'input' for live update

    // Initial simulation update
    updateSimulation();

    // Toggle explanation visibility
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = agingExplanationDiv.style.display === 'none';
        agingExplanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר' : '? למה זה קורה? גלה את המנגנונים מאחורי התבלות החומרים';
        toggleExplanationButton.classList.toggle('active', isHidden);
    });

</script>

<style>
    /* Add a basic font-awesome include for icons if available in environment */
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css');

    .aging-simulator {
        font-family: 'Arial', sans-serif;
        direction: rtl;
        max-width: 850px; /* Slightly wider */
        margin: 30px auto;
        padding: 30px;
        border: none;
        border-radius: 12px; /* More rounded corners */
        background: linear-gradient(145deg, #e0e0e0, #ffffff); /* Subtle gradient */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2); /* Stronger, softer shadow */
        color: #333;
    }

    .aging-simulator h2 {
        text-align: center;
        color: #1a237e; /* Deep blue */
        margin-top: 0;
        margin-bottom: 25px;
        font-size: 1.8em;
    }

    .controls-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); /* Responsive grid */
        gap: 20px; /* Space between groups */
        margin-bottom: 30px;
        padding-bottom: 20px;
        border-bottom: 1px dashed #b0bec5; /* More visually interesting separator */
    }

    .control-group {
        padding: 15px;
        background-color: #eceff1; /* Light background for groups */
        border-radius: 8px;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
    }

     .control-group label {
        font-weight: bold;
        margin-bottom: 10px;
        display: block;
        color: #37474f; /* Darker gray */
        font-size: 1.1em;
     }

     .env-checkboxes {
        display: flex;
        flex-direction: column;
        gap: 8px;
     }

     .env-checkboxes div {
        display: flex;
        align-items: center;
     }

     .env-checkboxes input[type="checkbox"] {
        margin-left: 8px; /* Space between checkbox and label */
        accent-color: #1a237e; /* Style checkbox color */
     }

      .env-checkboxes label {
        font-weight: normal; /* Not bold */
        margin-bottom: 0; /* Remove label margin */
        display: inline-block; /* Align with checkbox */
        font-size: 1em;
        color: #546e7a;
        cursor: pointer; /* Indicate clickable */
     }

     .env-checkboxes label i {
         margin-left: 5px; /* Space between icon and text */
         color: #00838f; /* Teal color for icons */
     }


    select, input[type="range"] {
        padding: 10px;
        border: 1px solid #b0bec5;
        border-radius: 5px;
        font-size: 1em;
        width: 100%; /* Make controls full width */
        box-sizing: border-box; /* Include padding/border in width */
    }

    select {
         background-color: #ffffff;
         cursor: pointer;
    }

     input[type="range"] {
         -webkit-appearance: none; /* Override default slider styles */
         appearance: none;
         height: 8px;
         background: #b0bec5;
         outline: none;
         opacity: 0.8;
         transition: opacity .2s;
         margin-top: 10px;
     }

     input[type="range"]:hover {
         opacity: 1;
     }

     input[type="range"]::-webkit-slider-thumb {
         -webkit-appearance: none;
         appearance: none;
         width: 20px;
         height: 20px;
         background: #1a237e;
         cursor: pointer;
         border-radius: 50%;
         border: 2px solid #fff;
         box-shadow: 0 1px 3px rgba(0,0,0,0.2);
     }

     input[type="range"]::-moz-range-thumb {
         width: 20px;
         height: 20px;
         background: #1a237e;
         cursor: pointer;
         border-radius: 50%;
         border: 2px solid #fff;
         box-shadow: 0 1px 3px rgba(0,0,0,0.2);
     }

     .slider-group label {
         display: flex;
         justify-content: space-between;
         align-items: center;
     }

     .slider-group label span {
         background-color: #1a237e;
         color: white;
         padding: 3px 8px;
         border-radius: 4px;
         font-size: 0.9em;
     }


    .simulation-area {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 20px;
    }

    .material-sample {
        width: 250px; /* Larger sample */
        height: 180px; /* Larger sample */
        border: 4px solid #546e7a; /* Darker, thicker border */
        margin-bottom: 25px;
        position: relative;
        overflow: hidden;
        box-shadow: inset 0 0 15px rgba(0,0,0,0.3); /* Stronger inner shadow */
        background-color: #e0e0e0; /* Default subtle background */
        /* Material specific backgrounds will be set by JS */
        transition: background-color 0.5s ease, filter 0.5s ease;
         border-radius: 8px;
    }

     /* Specific material styles */
     #material-sample[style*="steel"] { background-color: #a9a9a9; } /* Darker gray steel */
     #material-sample[style*="concrete"] {
         background-color: #c0c0c0; /* Concrete base */
         background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12'%3E%3Cg fill='%23d4d4d4'%3E%3Ccircle cx='6' cy='6' r='5'%3E%3C/circle%3E%3C/g%3E%3C/svg%3E"), url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='10'%3E%3Cg fill='%23b0b0b0'%3E%3Ccircle cx='5' cy='5' r='4'%3E%3C/circle%3E%3C/g%3E%3C/svg%3E");
         background-size: 12px 12px, 10px 10px;
         background-position: 0 0, 5px 5px;
     } /* More realistic concrete pattern */
     #material-sample[style*="aluminum"] { background-color: #bdbdbd; } /* Lighter gray aluminum */


     .sample-overlay {
         pointer-events: none;
         position: absolute;
         top: 0;
         left: 0;
         width: 100%;
         height: 100%;
         mix-blend-mode: multiply; /* Blends with background better */
         opacity: 0; /* Default hidden */
         transition: opacity 0.5s ease-out; /* Smooth transition */
         background-size: cover; /* Ensure patterns cover the area */
     }

    .rust-overlay {
         background-image: url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXR0ZXJuIGlkPSJyZXBlYXQtcnVzdCIgcGF0dGVyblVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgd2lkdGg9IjE1IiBoZWlnaHQ9IjE1Ij48Y2lyY2xlIGN4PSI3LjUiIGN5PSI3LjUiIHI9IjQiIGZpbGw9IiM4YjQ1MTkiIGZpbGwtb3BhY2l0eT0iMC43Ii8+PHBhdGggZD0iTTIuNSw1IEwxMi41LDEwIE01LDIuNSAxMCwxMi41IiBzdHJva2U9IiM4YjQ1MTkiIHN0cm9rZS1vcGFjaXR5PSIwLjUiIHN0cm9rZS13aWR0aD0iMSIvPjwvcGF0dGVybj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSJ1cmwoI3JlcGVhdC1ydXN0KSIvPjwvc3ZnPg=='); /* More complex rust pattern */
        background-color: rgba(139, 69, 19, 0.4); /* Brownish semi-transparent */
        background-size: 20px 20px;
        mix-blend-mode: multiply;
    }

    .cracks-overlay {
        /* More detailed crack pattern */
        background-image: url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXR0ZXJuIGlkPSJyZXBlYXQtY3JhY2tzIiBwYXR0ZXJuVW5pdHM9InVzZXJTcGFjZU9uVXNlIiB3aWR0aD0iMjAiIGhlaWdodD0iMjAiPjxsaW5lIHgxPSIwIiB5MT0iMTAiIHgyPSIyMCIgeTI9IjEwIiBzdHJva2U9IiMxMDM4NGQiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIi8+PGxpbmUgeDE9IjEwIiB5MT0iMCIgeDI9IjEwIiB5Mj0iMjAiIHN0cm9rZT0iIzEwMzg0ZCIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtbGluZWNhcD0icm91bmQiLz48Y2lyY2xlIGN4PSI1IiBjeT0iNSIgcj0iMC41IiBmaWxsPSIjMTAzODRmIi8+PGNpcmNsZSBjeD0iMTUiIGN5PSI1IiByPSIwLjUiIGZpbGw9IiMxMDM4NGYiLz48Y2lyY2xlIGN4PSI1IiBjeT0iMTUiIHI9IjAuNSIgZmlsbD0iIzEwMzg0ZiIvPjxjaXJjbGUgY3g9IjE1IiBjeT0iMTUiIHI9IjAuNSIgZmlsbD0iIzEwMzg0ZiIvPjwvcGF0dGVybj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSJ1cmwoI3JlcGVhdC1jcmFja3MpIi8+PC9zdmc+');
        background-size: 30px 30px;
        mix-blend-mode: multiply;
        filter: brightness(0.5); /* Make cracks stand out */
    }

    .spalling-overlay {
         /* Concrete spalling/crumbling effect */
        background-image: url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXR0ZXJuIGlkPSJyZXBlYXQtc3BhbGxpbmciIHBhdHRlcm5Vbml0cz0idXNlclNwYWNlT25Vc2UiIHdpZHRoPSIyNSIgaGVpZ2h0PSIyNSI+PHJlY3Qgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSIgZmlsbD0iI2UwZTBkMCIvPjxjaXJjcnJvbSByPSIyIiBjeD0iOCIgY3k9IjgiIGZpbGw9IiNhMGEwYTAiLz48Y2lyY3JvbSByPSIxLjUiIGN4PSIxOCIgY3k9IjEyIiBmaWxsPSIjYjBiMGIwIi8+PGNpcmNyb20gcj0iMi41IiBjeD0iMTIiIGN5PSIxOCIgZmlsbD0iI2MwYzBjMCIvPjwvcGF0dGVybj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSJ1cmwoI3JlcGVhdC1zcGFsbGluZykiLz48L3N2Z3M+');
        background-size: 40px 40px;
        background-color: rgba(192, 192, 192, 0.5); /* Light greyish background */
        mix-blend-mode: multiply;
    }


    .integrity-display {
        width: 100%;
        text-align: center;
        margin-top: 15px;
        font-size: 1.1em;
        color: #37474f;
    }

    .integrity-bar-container {
        width: 90%; /* Wider bar */
        max-width: 450px;
        height: 25px; /* Taller bar */
        background-color: #cfd8dc; /* Lighter background */
        border-radius: 12px;
        overflow: hidden;
        margin: 12px auto;
        border: 1px solid #90a4ae;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
    }

    .integrity-bar {
        height: 100%;
        background-color: #28a745; /* Initial Green */
        transition: width 0.5s ease-out, background-color 0.5s ease; /* Smooth transitions */
    }

    .feedback-message {
         text-align: center;
         margin-top: 20px;
         min-height: 1.5em; /* Reserve space */
         color: #1a237e;
         font-weight: bold;
         font-size: 1em;
         opacity: 0;
         transition: opacity 0.5s ease-in-out;
    }

     #toggle-explanation {
        display: block;
        width: fit-content;
        margin: 30px auto; /* More space */
        padding: 12px 20px;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        direction: rtl;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
         box-shadow: 0 2px 4px rgba(0,0,0,0.2);
     }

     #toggle-explanation:hover {
        background-color: #0056b3;
        box-shadow: 0 3px 6px rgba(0,0,0,0.3);
     }

     #toggle-explanation.active {
         background-color: #dc3545; /* Red when active/showing */
     }
      #toggle-explanation.active:hover {
         background-color: #c82333;
      }


     #aging-explanation {
        font-family: 'Arial', sans-serif;
        direction: rtl;
        max-width: 850px;
        margin: 30px auto;
        padding: 30px;
        border: none;
        border-radius: 12px;
        background: #ffffff;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        line-height: 1.7;
        color: #333;
     }

     #aging-explanation h2, #aging-explanation h3, #aging-explanation h4 {
        color: #1a237e;
        margin-top: 25px;
        margin-bottom: 12px;
     }

      #aging-explanation h2 {
         text-align: center;
         font-size: 1.6em;
      }
       #aging-explanation h3 {
         font-size: 1.4em;
         border-bottom: 1px solid #eceff1;
         padding-bottom: 5px;
       }
        #aging-explanation h4 {
         font-size: 1.2em;
         color: #37474f;
        }

     #aging-explanation p {
        margin-bottom: 18px;
        text-align: justify;
     }

     #aging-explanation ul {
        margin-bottom: 18px;
        padding-right: 25px; /* Adjust for RTL */
        list-style: disc outside; /* Use disc style */
        color: #546e7a; /* Softer bullet color */
     }

     #aging-explanation li {
        margin-bottom: 10px;
     }

     /* Responsive adjustments */
     @media (max-width: 600px) {
         .controls-grid {
             grid-template-columns: 1fr; /* Stack controls on small screens */
         }
         .aging-simulator, #aging-explanation {
             padding: 20px;
             margin: 20px auto;
         }
          .material-sample {
             width: 100%; /* Full width on small screens */
             max-width: 250px; /* But don't get too big */
             height: 180px;
          }
          #toggle-explanation {
             width: 90%;
             box-sizing: border-box;
          }
     }
</style>
```