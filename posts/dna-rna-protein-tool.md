---
title: "מסע המידע הגנטי: מה-DNA לחלבון"
english_slug: dna-rna-protein-tool
category: "ביולוגיה"
tags: ["ביולוגיה", "DNA", "RNA", "חלבון", "גנטיקה", "שיעתוק", "תרגום", "סימולציה אינטראקטיבית", "קוד גנטי"]
---
# מסע המידע הגנטי: מה-DNA לחלבון

איך רצף של אותיות ב-DNA הופך למכונות הפלאיות שמרכיבות את החיים? הצטרפו למסע המרתק של המידע הגנטי! כאן תראו כיצד ההוראות האצפונות ב-DNA מועתקות (עוברות שיעתוק) למולקולת שליח (RNA), ואיך מולקולת השליח הזו מתורגמת לרצף ספציפי של אבני בניין (חומצות אמינו) היוצרות את החלבון - מבצע המשימות העיקרי בתא. הכלי האינטראקטיבי שלנו יאפשר לכם להזין "הוראת DNA" ולעקוב אחר כל שלב בתהליך, כאילו הייתם בתוך התא!

<div class="interactive-app-container">
    <div class="input-section">
        <h2>שלב 1: הזנת הוראת DNA</h2>
        <p>הזינו רצף DNA דו-גדילי (נתייחס אליו כגדיל המקודד). השתמשו באותיות A, T, C, G בלבד. נסו להתחיל עם רצף קצר, למשל: <code style="direction: ltr;">ATGATAGATGA</code></p>
        <textarea id="dna-input" placeholder="הזינו כאן את רצף ה-DNA (A, T, C, G)..." spellcheck="false" autocomplete="off" autocorrect="off" autocapitalize="off"></textarea>
        <button id="synthesize-button">הפעל את התהליך!</button>
        <div class="error-message" id="error-message"></div>
    </div>

    <div class="processing-indicator" id="processing-indicator" style="display: none;">
        <div class="spinner"></div>
        <span>מפענחים את המידע הגנטי...</span>
    </div>

    <div class="output-section" id="rna-output-section" style="opacity: 0;">
        <h2>שלב 2: שיעתוק (DNA ← RNA)</h2>
        <p>המכונה התאית מעתיקה את הוראת ה-DNA למולקולת שליח חדשה - ה-RNA.</p>
        <div id="rna-sequence" class="sequence-display" style="direction: ltr; text-align: left;"></div>
    </div>

    <div class="output-section" id="protein-output-section" style="opacity: 0;">
        <h2>שלב 3: תרגום (RNA ← חלבון)</h2>
        <p>הריבוזום קורא את השליח (RNA) בקודונים (שלשות אותיות) ומתרגם אותו לשרשרת של חומצות אמינו - החלבון!</p>
         <div id="protein-sequence" class="sequence-display" style="direction: ltr; text-align: left;"></div>
         <div class="codon-translation">
            <span class="label">פירוט התרגום (קודון ← חומצת אמינו):</span>
            <div id="codon-list" style="direction: ltr; text-align: left;"></div>
        </div>
    </div>
</div>

<button id="toggle-explanation" class="toggle-button">מעוניינים להבין לעומק? הצגת ההסבר</button>

<div id="explanation" style="display: none;">
    <h2>הסבר מעמיק: שיעתוק (Transcription) ותרגום (Translation)</h2>

    <h3>המסע מתחיל: שיעתוק (DNA ל-RNA)</h3>
    <p>דמיינו את ה-DNA כספרייה ענקית של הוראות. כדי ליצור משהו, התא לא מוציא את הספר כולו מהספרייה (הגרעין), אלא מעתיק דף ספציפי (גֵן) לשליח (RNA). התהליך הזה, הנקרא שיעתוק, מתבצע על ידי אנזים מיוחד בשם RNA פולימראז.</p>
    <p>ה-RNA פולימראז "רץ" על אחד מגדילי ה-DNA (גדיל התבנית) ובונה גדיל RNA משלים. הגדיל הדומה לגדיל ה-RNA שנוצר (למעט החלפת נוקלאוטיד T בנוקלאוטיד U) נקרא הגדיל המקודד. הכלי האינטראקטיבי שלנו עובד עם הגדיל המקודד, כך שכללי ההשלמה הם למעשה החלפת T ב-U.</p>
    <p>הכללים הפשוטים:</p>
    <ul>
        <li>A ב-DNA ← U ב-RNA</li>
        <li>T ב-DNA ← A ב-RNA</li>
        <li>C ב-DNA ← G ב-RNA</li>
        <li>G ב-DNA ← C ב-RNA</li>
    </ul>
    <p>ה-RNA שנוצר (נקרא mRNA - messenger RNA) יוצא מהגרעין (באאוקריוטים) מוכן לשלב הבא.</p>

    <h3>התרגום: RNA לחלבון</h3>
    <p>מולקולת ה-mRNA מגיעה ל"מפעל ייצור החלבונים" של התא - הריבוזום. הריבוזום קורא את רצף ה-RNA בשלשות של בסיסים, שכל שלשה כזו נקראת קודון. כל קודון ברובו מתאים לחומצת אמינו ספציפית, על פי "הקוד הגנטי" האוניברסלי (כמעט) לכל היצורים החיים!</p>
    <p>תהליך התרגום מתחיל בדרך כלל בקודון "התחלה" (AUG), המקודד לחומצת האמינו מתיונין (M). הריבוזום ממשיך לקרוא קודון אחר קודון, ומולקולות מיוחדות (tRNA) מביאות את חומצת האמינו המתאימה לכל קודון. חומצות האמינו נקשרות זו לזו כמו חרוזים על חוט, ויוצרות שרשרת ארוכה הנקראת פוליפפטיד. התרגום מסתיים כאשר הריבוזום מגיע לאחד מקודוני "הסיום" (UAA, UAG, UGA), שאינם מקודדים לחומצת אמינו אלא מסמנים שהשרשרת הסתיימה.</p>
    <p>הפוליפפטיד שנוצר מתקפל למבנה תלת-ממדי מוגדר, והופך לחלבון פעיל שמבצע מגוון אדיר של תפקידים בתא ובגוף - החל מבניית מבנים, דרך זרזים (אנזימים) ועד נשאים וקולטנים.</p>

    <h4>הקוד הגנטי (טבלה חלקית/דוגמאות - הקוד המלא כלול בסימולציה):</h4>
    <p>הסימולציה משתמשת בקוד הגנטי המלא. הנה כמה דוגמאות:</p>
    <p>AUG → Methionine (M) - קודון התחלה</p>
    <p>UUU, UUC → Phenylalanine (F)</p>
    <p>UUA, UUG, CUU, CUC, CUA, CUG → Leucine (L)</p>
    <p>... (עוד 16 חומצות אמינו)</p>
    <p>UAA, UAG, UGA → STOP - קודוני סיום</p>
</div>

<style>
    /* כללי עיצוב בסיסיים - שיפור מראה כללי */
    body {
        font-family: 'Heebo', sans-serif; /* שימוש בפונט עברי נעים יותר */
        line-height: 1.7; /* מרווח שורות משופר */
        color: #343a40; /* צבע טקסט כהה יותר */
        background-color: #e9ecef; /* רקע אפור בהיר */
        padding: 20px;
        direction: rtl;
        text-align: right;
        margin: 0; /* Reset default margin */
    }

    h1, h2, h3 {
        color: #004085; /* כחול כהה יותר לכותרות */
        text-align: center;
        margin-bottom: 20px;
        font-weight: 700; /* Bold headers */
    }

    h1 {
        font-size: 2.5em;
        margin-top: 20px;
    }

    h2 {
        font-size: 1.8em;
        margin-top: 25px;
        border-bottom: 2px solid #007bff; /* קו תחתון כחול */
        padding-bottom: 5px;
        display: inline-block; /* Contain border to text width */
        margin-right: auto; /* Center-ish in RTL */
        margin-left: auto;
        display: block; /* Back to block for centering */
        text-align: right; /* Align section titles right */
    }
     .output-section h2 {
         text-align: right;
         display: block;
         margin-right: 0;
         margin-left: 0;
         border-bottom: none;
         padding-bottom: 0;
         color: #007bff;
         font-size: 1.3em;
         margin-bottom: 10px;
     }

    h3 {
        font-size: 1.4em;
        color: #0056b3; /* כחול ביניים */
        margin-top: 20px;
        margin-bottom: 15px;
    }

    /* קונטיינר האפליקציה האינטראקטיבית */
    .interactive-app-container {
        background-color: #ffffff; /* רקע לבן */
        padding: 30px; /* הגדלת ריפוד */
        border-radius: 12px; /* פינות מעוגלות יותר */
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15); /* צל עמוק יותר */
        margin: 30px auto; /* מרווח עליון ותחתון גדול יותר */
        max-width: 800px; /* הגדלת רוחב מקסימלי */
        border-top: 6px solid #007bff; /* פס עליון כחול חי */
        text-align: right;
        position: relative; /* עבור מיקום הספינר */
        overflow: hidden; /* Hide potential overflow from animations */
    }

    .input-section {
        margin-bottom: 30px;
    }

    textarea {
        width: 100%;
        padding: 15px; /* הגדלת ריפוד */
        margin-bottom: 15px;
        border: 1px solid #ced4da; /* מסגרת עדינה יותר */
        border-radius: 8px; /* פינות מעוגלות */
        font-size: 1.1em; /* גופן גדול יותר */
        box-sizing: border-box;
        min-height: 120px; /* הגדלת גובה מינימלי */
        resize: vertical;
        direction: ltr; /* Force LTR for sequences */
        text-align: left;
        font-family: 'Courier New', Courier, monospace; /* גופן מונספייס לרצפים */
        transition: border-color 0.3s ease; /* אנימציה למסגרת */
    }

    textarea:focus {
        border-color: #007bff; /* הדגשת מסגרת בפוקוס */
        outline: none; /* הסרת אאוטליין ברירת מחדל */
        box-shadow: 0 0 8px rgba(0, 123, 255, 0.25); /* צל בפוקוס */
    }

    button {
        display: block;
        width: 100%;
        padding: 14px 20px; /* הגדלת ריפוד */
        background-color: #007bff; /* כחול חי */
        color: white;
        border: none;
        border-radius: 8px; /* פינות מעוגלות */
        font-size: 1.2em; /* גופן גדול יותר */
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease, opacity 0.3s ease; /* אנימציות */
        margin-bottom: 20px;
        font-weight: 700;
    }

    button:hover:not(:disabled) {
        background-color: #0056b3; /* כחול כהה יותר בלחיצה */
    }

    button:active:not(:disabled) {
        transform: scale(0.98);
    }

     button:disabled {
         background-color: #cccccc;
         cursor: not-allowed;
         opacity: 0.7;
     }


    /* אזורי פלט - RNA וחלבון */
    .output-section {
        margin-top: 30px; /* מרווח עליון גדול יותר */
        padding-top: 20px;
        border-top: 1px solid #e9ecef; /* קו הפרדה עדין */
        opacity: 0; /* התחלה שקופה לאנימציה */
        transform: translateY(20px); /* התחלה מעט למטה לאנימציה */
        transition: opacity 0.6s ease-out, transform 0.6s ease-out; /* אנימציית הופעה */
    }

     .output-section.visible {
         opacity: 1;
         transform: translateY(0);
     }

    .sequence-display {
        background-color: #f8f9fa; /* רקע אפור בהיר מאוד */
        padding: 15px;
        border-radius: 8px;
        word-break: break-word; /* Break long words */
        font-family: 'Courier New', Courier, monospace;
        direction: ltr;
        text-align: left;
        min-height: 1.8em; /* Ensure minimum height */
        overflow-x: auto; /* Add scroll for very long sequences */
        white-space: pre-wrap; /* Wrap text but preserve spacing */
        border: 1px dashed #a0aec0; /* קו מקווקו */
        margin-bottom: 15px;
    }

    /* עיצוב אזור פירוט הקודונים */
    .codon-translation {
        margin-top: 20px;
        font-size: 0.95em;
        color: #495057; /* צבע טקסט כהה יותר */
    }

    .codon-translation .label {
        font-weight: bold;
        display: block; /* Put label on its own line */
        margin-bottom: 8px;
    }

    #codon-list {
        display: flex;
        flex-wrap: wrap;
        gap: 8px; /* הגדלת רווח בין פריטים */
        margin-top: 10px;
        direction: ltr;
        text-align: left;
         min-height: 1.5em; /* Ensure min height */
    }

    .codon-item {
        background-color: #e2f0ff; /* רקע כחלחל בהיר */
        border: 1px solid #b3d7ff; /* מסגרת כחולה עדינה */
        padding: 5px 10px; /* הגדלת ריפוד */
        border-radius: 5px; /* פינות מעוגלות */
        font-family: 'Courier New', Courier, monospace;
        white-space: nowrap;
        font-size: 0.9em;
        transition: background-color 0.3s ease, transform 0.1s ease; /* אנימציה להדגשה */
    }

     .codon-item.highlight {
         background-color: #ffda6a; /* רקע צהוב להדגשה */
         border-color: #ffc107;
         transform: scale(1.05); /* הגדלה קלה בהדגשה */
     }

    /* הודעות שגיאה */
    .error-message {
        color: #dc3545; /* אדום חזק */
        margin-top: 15px;
        font-weight: bold;
        min-height: 1.5em;
        text-align: right; /* Ensure RTL alignment */
    }

    /* כפתור הצגת הסבר */
    .toggle-button {
        display: block;
        width: auto;
        margin: 30px auto; /* מרכוז וכיוון מרווח */
        background-color: #6c757d; /* אפור */
        padding: 10px 25px;
        font-size: 1em;
        border-radius: 5px;
        font-weight: normal;
    }

    .toggle-button:hover:not(:disabled) {
        background-color: #5a6268;
    }

    /* אזור ההסבר */
    #explanation {
        background-color: #f8f9fa; /* רקע אפור בהיר מאוד */
        padding: 30px;
        border-radius: 12px;
        margin: 30px auto;
        max-width: 800px;
        border-right: 6px solid #6c757d; /* פס צד אפור */
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        text-align: right;
    }

    #explanation h2, #explanation h3 {
        color: #495057; /* צבע כהה יותר לכותרות הסבר */
        text-align: right;
        border-bottom: none;
    }

    #explanation h2 {
         border-bottom: 2px solid #6c757d;
         padding-bottom: 5px;
    }

    #explanation p, #explanation ul {
        margin-bottom: 18px; /* מרווח גדול יותר בין פסקאות */
        text-align: right;
    }

    #explanation ul {
        padding-right: 30px; /* מרווח לרשימה */
        list-style: disc outside; /* עיגולים */
    }

    #explanation li {
         margin-bottom: 8px;
    }

    code {
        background-color: #e9ecef;
        padding: 2px 5px;
        border-radius: 4px;
        font-family: 'Courier New', Courier, monospace;
        font-size: 0.9em;
    }

    /* Processing Indicator */
    .processing-indicator {
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 20px 0;
        color: #007bff;
        font-size: 1.2em;
        font-weight: bold;
    }

    .spinner {
      border: 4px solid #f3f3f3; /* Light grey */
      border-top: 4px solid #007bff; /* Blue */
      border-radius: 50%;
      width: 20px;
      height: 20px;
      animation: spin 1s linear infinite;
      margin-left: 10px; /* Space between text and spinner */
    }

    @keyframes spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }

    /* Specific styling for highlighting bases/codons */
    .rna-codon-highlight, .protein-amino-highlight {
        background-color: #ffda6a; /* Yellow highlight */
        padding: 2px 0px; /* Minimal padding for inline */
        border-radius: 3px;
        transition: background-color 0.2s ease;
    }


</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const dnaInput = document.getElementById('dna-input');
        const synthesizeButton = document.getElementById('synthesize-button');
        const rnaSequenceDiv = document.getElementById('rna-sequence');
        const proteinSequenceDiv = document.getElementById('protein-sequence');
        const codonListDiv = document.getElementById('codon-list');
        const errorMessageDiv = document.getElementById('error-message');
        const rnaOutputSection = document.getElementById('rna-output-section');
        const proteinOutputSection = document.getElementById('protein-output-section');
        const explanationDiv = document.getElementById('explanation');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const processingIndicator = document.getElementById('processing-indicator');

        // Comprehensive Genetic Code Map
        const geneticCode = {
            'AUG': 'M', // Start codon (Methionine)
            'UUU': 'F', 'UUC': 'F', // Phenylalanine
            'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', // Leucine
            'AUU': 'I', 'AUC': 'I', 'AUA': 'I', // Isoleucine
            'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', // Valine
            'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'AGU': 'S', 'AGC': 'S', // Serine
            'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', // Proline
            'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', // Threonine
            'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', // Alanine
            'UAU': 'Y', 'UAC': 'Y', // Tyrosine
            'CAU': 'H', 'CAC': 'H', // Histidine
            'CAA': 'Q', 'CAG': 'Q', // Glutamine
            'AAU': 'N', 'AAC': 'N', // Asparagine
            'AAA': 'K', 'AAG': 'K', // Lysine
            'GAU': 'D', 'GAC': 'D', // Aspartic Acid
            'GAA': 'E', 'GAG': 'E', // Glutamic Acid
            'UGU': 'C', 'UGC': 'C', // Cysteine
            'UGG': 'W', // Tryptophan
            'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R', // Arginine
            'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G', // Glycine
            'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP' // Stop codons
        };

        // Function to transcribe DNA (Coding Strand) to RNA
        function transcribe(dna) {
            // Assume input is the Coding Strand, replace T with U
            return dna.replace(/T/gi, 'U').toUpperCase();
        }

        // Function to translate RNA to Protein step-by-step with animation
        async function translateStepByStep(rna) {
             proteinSequenceDiv.innerHTML = ''; // Clear previous protein sequence
             codonListDiv.innerHTML = ''; // Clear previous codon list

            let protein = '';
            const startIndex = rna.indexOf('AUG');

            if (startIndex === -1) {
                 proteinSequenceDiv.textContent = 'אין קודון התחלה (AUG) ברצף ה-RNA.';
                 return { protein: '', codons: [] }; // Return empty results
            }

             // Display RNA for highlighting
            let rnaHtml = '';
            for(let i = 0; i < rna.length; i++) {
                // Use spans to allow individual base highlighting if needed later, or codon grouping
                if (i >= startIndex && (i - startIndex) % 3 === 0) {
                     // Mark start of a potential codon for highlighting
                     rnaHtml += `<span class="rna-base codon-start-${(i - startIndex) / 3}">`;
                }
                 rnaHtml += rna[i];
                 if (i >= startIndex && (i - startIndex) % 3 === 2) {
                     // Mark end of a potential codon
                     rnaHtml += `</span>`;
                 }
            }
            rnaSequenceDiv.innerHTML = rnaHtml;


            let currentProteinSequence = '';
            let codonsData = [];
            const codonElements = rnaSequenceDiv.querySelectorAll('span.codon-start-' + '[class^="codon-start-"]'); // Select all potential codon spans

            for (let i = 0; i < codonElements.length; i++) {
                const codonSpan = codonElements[i];
                const codon = codonSpan.textContent;

                if (codon.length < 3) {
                     // Handle incomplete codon at the very end
                     codonSpan.classList.add('rna-codon-highlight'); // Highlight the partial codon
                     // Optional: Add to codon list as partial
                     // const partialCodonItem = document.createElement('span');
                     // partialCodonItem.classList.add('codon-item');
                     // partialCodonItem.textContent = `${codon} → ?`;
                     // codonListDiv.appendChild(partialCodonItem);
                     break; // Stop processing
                }

                const aminoAcid = geneticCode[codon];

                // Highlight the current codon in RNA
                codonSpan.classList.add('rna-codon-highlight');

                // Add codon item to the list
                const codonItem = document.createElement('span');
                codonItem.classList.add('codon-item');
                codonItem.textContent = `${codon} → ${aminoAcid || 'X'}`; // Use X for unknown/invalid codon
                codonListDiv.appendChild(codonItem);
                codonsData.push({ codon: codon, amino: aminoAcid || 'X' });

                if (aminoAcid === 'STOP') {
                    currentProteinSequence += ' (STOP)';
                    proteinSequenceDiv.textContent = currentProteinSequence; // Update protein display
                    codonItem.classList.add('highlight'); // Highlight the stop codon item
                    await new Promise(resolve => setTimeout(resolve, 600)); // Pause slightly longer for STOP
                    codonSpan.classList.remove('rna-codon-highlight');
                    break; // Stop translation
                } else if (aminoAcid) {
                    currentProteinSequence += aminoAcid;
                    proteinSequenceDiv.textContent = currentProteinSequence; // Update protein display
                    codonItem.classList.add('highlight'); // Highlight the current codon item

                    await new Promise(resolve => setTimeout(resolve, 400)); // Pause for animation effect

                    // Remove highlight after delay
                     codonSpan.classList.remove('rna-codon-highlight');
                     codonItem.classList.remove('highlight');

                } else {
                    // Handle invalid/unknown codon within the reading frame
                    currentProteinSequence += 'X'; // Add 'X' for unknown
                    proteinSequenceDiv.textContent = currentProteinSequence; // Update protein display
                     codonItem.classList.add('highlight'); // Highlight the invalid codon item
                     await new Promise(resolve => setTimeout(resolve, 400)); // Pause
                     codonSpan.classList.remove('rna-codon-highlight');
                     codonItem.classList.remove('highlight');
                }
            }

             // Ensure final protein sequence is set after loop finishes naturally
             if (!currentProteinSequence.endsWith(' (STOP)')) {
                 proteinSequenceDiv.textContent = currentProteinSequence;
             }


            return { protein: currentProteinSequence, codons: codonsData };
        }


        synthesizeButton.addEventListener('click', async () => { // Make the function async
            const rawDnaInput = dnaInput.value.toUpperCase();
            const cleanedDna = rawDnaInput.replace(/[^ATCG]/g, ''); // Clean input

            // Clear previous results and errors
            rnaSequenceDiv.textContent = '';
            proteinSequenceDiv.textContent = '';
            codonListDiv.innerHTML = '';
            errorMessageDiv.textContent = '';
            rnaOutputSection.classList.remove('visible');
            proteinOutputSection.classList.remove('visible');
            rnaOutputSection.style.opacity = 0; // Ensure opacity is 0 before animation
            proteinOutputSection.style.opacity = 0; // Ensure opacity is 0 before animation


            if (rawDnaInput.length === 0) {
                errorMessageDiv.textContent = 'אנא הזן רצף DNA כדי להתחיל את המסע.';
                return;
            }

             // Basic validation: check if cleaning removed characters
            if (cleanedDna.length !== rawDnaInput.length) {
                 errorMessageDiv.textContent = 'הקלט הכיל תווים לא חוקיים. עובדו רק האותיות A, T, C, G.';
            }

            if (cleanedDna.length === 0 && rawDnaInput.length > 0) {
                 errorMessageDiv.textContent = 'הקלט שהוזן לא הכיל אותיות A, T, C, G חוקיות כלל.';
                 return;
            }

            // Disable button and show processing indicator
            synthesizeButton.disabled = true;
            processingIndicator.style.display = 'flex';


            // --- Step 1: Transcription ---
            await new Promise(resolve => setTimeout(resolve, 300)); // Small delay before showing RNA section
            const rna = transcribe(cleanedDna);
            rnaSequenceDiv.textContent = rna;
            rnaOutputSection.style.opacity = 1;
            rnaOutputSection.classList.add('visible');


            // --- Step 2: Translation with Animation ---
            await new Promise(resolve => setTimeout(resolve, 1000)); // Delay before starting translation animation
            proteinOutputSection.style.opacity = 1; // Make protein section visible before animation starts
            proteinOutputSection.classList.add('visible');
            const { protein, codons } = await translateStepByStep(rna); // Call async translation


            // Hide processing indicator and enable button after all steps
            processingIndicator.style.display = 'none';
            synthesizeButton.disabled = false;
        });

        // Toggle explanation visibility
        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            // Use CSS classes for transition if needed, but simple display toggle is fine per constraints
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מעמיק' : 'מעוניינים להבין לעומק? הצגת ההסבר';
        });

        // Initial state setup
        rnaOutputSection.style.opacity = 0;
        proteinOutputSection.style.opacity = 0;
         explanationDiv.style.display = 'none'; // Ensure explanation is hidden on load
    });
</script>