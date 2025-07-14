---
title: "להחליט כמו מישלן: אמנות השיפוט הקולינרי"
english_slug: decide-like-michelin
category: "פסיכולוגיה"
tags: [קבלת החלטות, שיפוט מומחה, דירוג מישלן, הערכת מסעדות, הטיות קוגניטיביות, קולינריה]
---
<main dir="rtl" lang="he">
    <h1>להחליט כמו מישלן<br> <small>אמנות השיפוט הקולינרי</small></h1>
    <p class="intro-text">הצטרפו אלינו למסע מרתק אל מאחורי הקלעים של מדריך המסעדות היוקרתי בעולם. האם תצליחו לזהות את הניואנסים החמקמקים ולהגיע להחלטה הנכונה, ממש כמו מבקר מישלן מנוסה? היכנסו לנעליים שלהם וגלו את המורכבות שמעבר לצלחת.</p>

    <div id="app">
        <h2><span class="icon">🕵️</span> המשימה שלך: מבקר מישלן מתלמד</h2>
        <p>בחן את התרחישים הבאים ודרג את המסעדה כאילו אתה מבקר מישלן אנונימי. זכור את הקריטריונים המרכזיים!</p>

        <div id="scenario-container">
            <div id="scenario">
                <h3 id="scenario-title"></h3>
                <p id="scenario-description"></p>

                <div id="rating-section">
                    <h4><span class="icon">⚖️</span> דרג לפי קריטריונים (1-5):</h4>
                    <div class="rating-item">
                        <label for="quality">איכות המוצרים</label>
                        <input type="range" id="quality" min="1" max="5" value="3">
                        <span id="quality-value" class="rating-value">3</span>
                    </div>
                    <div class="rating-item">
                        <label for="mastery">שליטה בטעמים ובטכניקות</label>
                        <input type="range" id="mastery" min="1" max="5" value="3">
                        <span id="mastery-value" class="rating-value">3</span>
                    </div>
                     <div class="rating-item">
                        <label for="personality">אישיות המטבח / מקוריות</label>
                        <input type="range" id="personality" min="1" max="5" value="3">
                        <span id="personality-value" class="rating-value">3</span>
                    </div>
                     <div class="rating-item">
                        <label for="value">יחס מחיר-איכות</label>
                        <input type="range" id="value" min="1" max="5" value="3">
                        <span id="value-value" class="rating-value">3</span>
                    </div>
                     <div class="rating-item">
                        <label for="consistency">עקביות (במספר ביקורים מדומיינים)</label>
                        <input type="range" id="consistency" min="1" max="5" value="3">
                        <span id="consistency-value" class="rating-value">3</span>
                    </div>

                    <h4><span class="icon">⭐</span> המלצת כוכבים כוללת (0-3):</h4>
                     <div class="rating-item">
                        <label for="stars">כוכבים</label>
                        <input type="range" id="stars" min="0" max="3" value="0">
                         <span id="stars-value" class="rating-value stars">0</span>
                    </div>

                    <button id="submit-rating"><span class="icon">✅</span> שלח את הערכה</button>
                </div>
            </div>
            <button id="next-scenario" class="hidden"><span class="icon">➡️</span> תרחיש הבא</button>
        </div>

        <div id="feedback-container" class="feedback hidden">
            <h4><span class="icon">👨‍🏫</span> משוב מהמדריך הבכיר שלך:</h4>
            <div id="feedback-content"></div>
             <button id="continue-after-feedback" class="hidden"><span class="icon">▶️</span> המשך</button>
        </div>

         <div id="completion-message" class="hidden completion">
            <h2><span class="icon">🎉</span> כל הכבוד! סיימת את התרחישים.</h2>
            <p>צברת ניסיון ראשוני בעולם השיפוט של מישלן. כעת תוכל להעמיק את ההבנה שלך עם ההסבר המלא.</p>
        </div>
    </div>

    <button id="show-explanation-btn" class="pulsing"><span class="icon">📚</span> הצג הסבר מורחב: עולם השיפוט של מישלן</button>

    <div id="explanation" class="hidden">
        <h2><span class="icon">📖</span> עולם השיפוט של מישלן: מעבר לצלחת</h2>
        <p>מדריך מישלן האדום הוא אחד ממדריכי המסעדות הוותיקים והמשפיעים בעולם. דירוג הכוכבים שלו נחשב לפסגת ההכרה הקולינרית ויכול לשנות באופן דרמטי את גורלה של מסעדה. אבל כיצד מתקבלות ההחלטות הללו? זהו תהליך מורכב ומובנה שמטרתו לשמר את יוקרת המדריך ואת אמינותו.</p>

        <h3><span class="icon">✨</span> מהם כוכבי מישלן וכיצד הם מוענקים?</h3>
        <p>כוכבי מישלן ניתנים למסעדות המציעות אוכל יוצא דופן. הדירוג הוא כדלקמן:</p>
        <ul>
            <li>⭐: מסעדה טובה מאוד בקטגוריה שלה.</li>
            <li>⭐⭐: מטבח יוצא דופן הראוי לעצור בדרך במיוחד עבורו.</li>
            <li>⭐⭐⭐: מטבח מצוין הראוי למסע מיוחד.</li>
        </ul>
        <p>ההחלטות מתקבלות על ידי צוות בינלאומי של מבקרים אנונימיים, הפועלים בסודיות ונוסעים ברחבי העולם. כל מסעדה פוטנציאלית נבדקת מספר פעמים, לעיתים קרובות על ידי מבקרים שונים, לפני שמתקבלת החלטה קולקטיבית על ידי ראשי המדריך בכל אזור.</p>

        <h3><span class="icon">📏</span> הקריטריונים הרשמיים של מישלן לדירוג מסעדות</h3>
        <p>חשוב לזכור שהדירוג מתייחס <strong>אך ורק לאיכות האוכל על הצלחת</strong>. חמשת הקריטריונים העיקריים הם:</p>
        <ol>
            <li><strong>איכות המוצרים:</strong> עד כמה חומרי הגלם טריים, עונתיים ואיכותיים. שימוש במוצרים יוצאי דופן מהווה יתרון משמעותי.</li>
            <li><strong>שליטה בטעמים ובטכניקות בישול:</strong> הדיוק בבישול, האיזון בין הטעמים, והיישום הנכון של טכניקות קלאסיות או מודרניות.</li>
            <li><strong>אישיות המטבח:</strong> האם האוכל משקף את אישיותו של השף? האם יש לו סגנון ייחודי ומזוהה? האם הוא יוצר חוויה קולינרית מקורית?</li>
            <li><strong>יחס מחיר-איכות:</strong> האם המחיר תואם את איכות האוכל ואת החוויה הקולינרית המוצעת? (חשוב לציין שזה לא הופך מסעדה זולה לכזו שמקבלת כוכב רק כי היא זולה, אלא שהמחיר צריך להיות מוצדק ביחס לאיכות).</li>
            <li><strong>עקביות בין ביקורים שונים:</strong> זהו קריטריון קריטי, במיוחד עבור דירוגים גבוהים. האם המסעדה מצליחה לספק חוויה קולינרית באותה רמה גבוהה בכל פעם שמבקרים בה? עקביות נדרשת לא רק בין ביקורים שונים, אלא גם בין מנות שונות באותה ארוחה, ובין שירותים שונים (צהריים/ערב).</li>
        </ol>
        <p>קריטריונים אלו הם הבסיס לכל הערכה, והמבקרים מאומנים לנתח את האוכל אך ורק דרכם.</p>

        <h3><span class="icon">🚶</span> תהליך קבלת ההחלטות של מבקר מישלן</h3>
        <p>התהליך מתחיל בביקור אנונימי במסעדה, בדיוק כמו כל סועד אחר. המבקר מזמין, אוכל, משלם את החשבון במלואו (זה חיוני לאנונימיות וליחס האמיתי מצד הצוות), ומתרשם מהארוחה כולה. לאחר מכן, הוא כותב דו"ח מפורט ביותר, המפרט כל מנה, את חומרי הגלם, את הטעמים, את הטכניקות, ואת התרשמותו ביחס לקריטריונים. דוחות אלו נאספים ונדונים בישיבות שבהן משתתפים מספר מבקרים וראשי המדריך. ההחלטה הסופית מתקבלת בדיון קולקטיבי, לעיתים קרובות לאחר מספר ביקורים שונים באותה מסעדה.</p>

        <h3><span class="icon">🧠</span> האתגר: אובייקטיביות מול סובייקטיביות</h3>
        <p>אמנם טעם הוא עניין סובייקטיבי, אך מישלן שואפת להגיע לשיפוט מומחה שהוא אובייקטיבי ככל הניתן. זאת עושים על ידי שימוש בקריטריונים מוגדרים היטב, הכשרה ממושכת של המבקרים, והחלטות קולקטיביות הממתנות הטיות אישיות. המטרה היא להעריך את איכות האוכל על פי סטנדרט בינלאומי גבוה, ולא רק על פי ההעדפה האישית של מבקר בודד.</p>

        <h3><span class="icon">🍽️</span> גורמים נוספים המשפיעים על הדירוג הכולל (מעבר לכוכבים)</h3>
        <p>בעוד שהכוכבים מתייחסים רק לאוכל, המדריך עצמו מספק גם דירוגים לגורמים אחרים (באמצעות סמלים שונים ולא כוכבים). גורמים אלו כוללים:</p>
        <ul>
            <li><strong>נוחות המסעדה ואווירה:</strong> עד כמה המקום נעים ומזמין.</li>
            <li><strong>איכות השירות:</strong> האם הוא מקצועי, קשוב וידידותי.</li>
            <li><strong>איכות היינות והמשקאות:</strong> מבחר והתאמה לאוכל.</li>
        </ul>
        <p>למרות שהם אינם גורמים ישירים בכוכבים, בפועל, במסעדות ברמות הגבוהות ביותר (2-3 כוכבים), לרוב גם השירות והאווירה יהיו ברמה מקבילה. עקביות, כפי שצוין, היא קריטריון קריטי הקשור גם לצד התפעולי ולא רק לטעם.</p>

        <h3><span class="icon">🚫</span> הטיות קוגניטיביות וכיצד מישלן מתמודדת איתן</h3>
        <p>כמו כל שופט אנושי, גם מבקרי מישלן עלולים להיות מושפעים מהטיות. הכשרה קפדנית ותהליך ההחלטה הקולקטיבי נועדו למזער הטיות אלו:</p>
        <ul>
            <li><strong>הטיית ההילה (Halo Effect):</strong> הנטייה לתת ציון גורף על בסיס התרשמות כללית. מישלן דורשת דירוג נפרד לכל קריטריון.</li>
            <li><strong>הטיית אישור (Confirmation Bias):</strong> חיפוש מידע שמאשר אמונה קיימת. ביקורים מרובים ודיון קבוצתי מסייעים.</li>
            <li><strong>הטיית העוגן (Anchoring Bias):</strong> הישענות יתר על המידה על פיסת המידע הראשונה. ההתמקדות בכל מנה וקריטריון בנפרד ממתנת זאת.</li>
            <li><strong>הטיית הזמינות (Availability Heuristic):</strong> הערכת תופעה על בסיס הקלות בה היא עולה לזיכרון. דוחות מפורטים ומנומקים עוזרים להתבסס על עובדות.</li>
        </ul>
        <p>תהליך מישלן מחנך את המבקרים להיות מודעים להטיות אלו ולבסס את שיפוטם על ניתוח קר ומקצועי של האוכל על פי הקריטריונים בלבד.</p>

        <h3><span class="icon">🏆</span> מדוע הדירוג כה יוקרתי ומשפיע?</h3>
        <p>היוקרה נובעת מההיסטוריה הארוכה, הסודיות, העקביות לכאורה של תהליך הבדיקה, והסטנדרטים הגבוהים. זכייה בכוכב יכולה לשנות דרמטית את גורל המסעדה והשף. זהו שיפוט מומחה במיטבו, המנסה להביא עקביות ואובייקטיביות לתחום סובייקטיבי.</p>

        <p>לסיכום, להחליט כמו מישלן זה לא רק עניין של טעם אישי, אלא יישום קפדני של קריטריונים, ניתוח אנליטי של החוויה הקולינרית, ומאמץ מודע להתגבר על הטיות קוגניטיביות.</p>
    </div>

    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background: linear-gradient(to bottom right, #f8f8f8, #e0e0e0); /* Softer background */
            color: #333;
            direction: rtl;
            text-align: right;
        }
        main {
            max-width: 800px;
            margin: 0 auto;
            background-color: #fff;
            padding: 30px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            border-radius: 12px;
            overflow: hidden; /* Clear floats/margins */
        }
         .intro-text {
            text-align: center;
            margin-bottom: 30px;
            font-size: 1.1em;
            color: #555;
         }
        h1, h2, h3, h4 {
            color: #8B0000; /* Deep Red */
            text-align: center;
            margin-bottom: 15px;
            font-weight: bold;
        }
        h1 small {
            display: block;
            font-size: 0.6em;
            color: #DAA520; /* Goldenrod */
            margin-top: 5px;
        }
         h1 {
            border-bottom: 2px solid #DAA520;
            padding-bottom: 15px;
         }
         h2 .icon, h3 .icon, h4 .icon {
             margin-left: 10px; /* Space between icon and text */
         }

        #app {
            margin-top: 30px;
            padding: 25px;
            background-color: #fffaf0; /* Floral White - light warm background */
            border-radius: 10px;
            border: 1px solid #f0e68c; /* Khaki - soft border */
            box-shadow: inset 0 0 8px rgba(218, 165, 32, 0.2); /* Subtle inner shadow */
             transition: all 0.5s ease-in-out; /* Smooth transitions for app section */
        }
        #scenario {
            margin-bottom: 20px;
            padding-bottom: 20px;
            border-bottom: 1px dashed #DAA520;
             transition: opacity 0.5s ease-in-out;
        }
        #scenario h3 {
            margin-top: 0;
            color: #b22222; /* Firebrick - slightly lighter red */
            font-size: 1.5em;
             text-align: right;
             margin-bottom: 10px;
        }
         #scenario p {
             text-align: right;
             font-size: 1.05em;
             color: #444;
         }

        #rating-section h4 {
            text-align: right;
            margin-top: 20px;
            margin-bottom: 15px;
            color: #8B0000;
            border-bottom: 1px solid #f0e68c;
            padding-bottom: 5px;
        }

        .rating-item {
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            flex-wrap: wrap;
            gap: 10px; /* Space between items */
        }
        .rating-item label {
            flex: 1;
            min-width: 180px; /* Adjusted minimum width */
            font-weight: bold;
            color: #555;
        }
        .rating-item input[type="range"] {
            flex: 2;
            -webkit-appearance: none;
            appearance: none;
            width: 100%;
            height: 10px; /* Thicker slider */
            background: #ddd;
            outline: none;
            opacity: 0.9;
            transition: opacity .2s;
            border-radius: 5px;
            cursor: pointer;
        }
         .rating-item input[type="range"]:hover {
            opacity: 1;
        }
         .rating-item input[type="range"]::-webkit-slider-thumb {
            -webkit-appearance: none;
            appearance: none;
            width: 24px; /* Larger thumb */
            height: 24px; /* Larger thumb */
            background: #8B0000;
            cursor: pointer;
            border-radius: 50%;
            border: 2px solid #fff; /* White border */
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
            transition: background-color 0.2s ease;
        }
         .rating-item input[type="range"]::-webkit-slider-thumb:hover {
             background-color: #b22222; /* Darker on hover */
         }
        .rating-item input[type="range"]::-moz-range-thumb {
            width: 24px;
            height: 24px;
            background: #8B0000;
            cursor: pointer;
            border-radius: 50%;
             border: 2px solid #fff;
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
             transition: background-color 0.2s ease;
        }
         .rating-item input[type="range"]::-moz-range-thumb:hover {
             background-color: #b22222;
         }

        .rating-value {
            margin-right: 15px; /* More space */
            min-width: 30px; /* Wider space for number */
            text-align: center;
            font-weight: bold;
            color: #DAA520; /* Goldenrod */
            font-size: 1.2em; /* Larger number */
             transition: color 0.2s ease;
        }
         .rating-value.stars {
             color: #FFD700; /* Gold for stars */
         }

        button {
            display: block;
            width: auto;
            padding: 12px 25px; /* More padding */
            margin: 25px auto;
            background-color: #8B0000; /* Deep Red */
            color: white;
            border: none;
            border-radius: 25px; /* Pill shape */
            cursor: pointer;
            font-size: 1.1rem;
            transition: background-color 0.3s ease, transform 0.1s ease;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            font-weight: bold;
        }
        button:hover {
            background-color: #b22222; /* Firebrick */
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.25);
        }
         button:active {
             transform: scale(0.98); /* Press effect */
         }
         button .icon {
             margin-left: 8px;
         }

        #next-scenario, #continue-after-feedback {
             background-color: #DAA520; /* Goldenrod */
             color: #333;
        }
         #next-scenario:hover, #continue-after-feedback:hover {
            background-color: #b8860b; /* DarkGoldenrod */
        }
         #next-scenario.hidden, #continue-after-feedback.hidden {
             visibility: hidden;
             opacity: 0;
             height: 0;
             margin: 0;
             padding: 0;
         }


        .feedback {
            margin-top: 20px;
            padding: 20px;
            background-color: #fffacd; /* LemonChiffon - light yellow */
            border: 1px solid #daa520; /* Goldenrod border */
            border-radius: 10px;
            color: #8B0000;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
             transition: opacity 0.5s ease-in-out, visibility 0.5s ease-in-out;
        }
         .feedback h4 {
            margin-top: 0;
            color: #8B0000;
             text-align: right;
             border-bottom: 1px dashed #DAA520;
             padding-bottom: 5px;
             margin-bottom: 15px;
         }
         .feedback p {
             text-align: right;
             color: #555;
             margin-bottom: 10px;
         }
          .feedback strong {
              color: #DAA520; /* Highlight key terms */
          }
         .feedback.hidden {
             visibility: hidden;
             opacity: 0;
             height: 0; /* Collapse element when hidden */
             padding: 0;
             margin-top: 0;
             border: none;
         }

         #completion-message {
             text-align: center;
             margin-top: 30px;
             padding: 20px;
             background-color: #d4edda; /* Light green */
             border: 1px solid #c3e6cb;
             border-radius: 10px;
             color: #155724; /* Dark green */
             font-size: 1.2em;
              transition: opacity 0.5s ease-in-out, visibility 0.5s ease-in-out;
         }
         #completion-message h2 {
             color: #155724;
         }
          #completion-message.hidden {
             visibility: hidden;
             opacity: 0;
             height: 0;
             padding: 0;
             margin-top: 0;
             border: none;
         }


        #show-explanation-btn {
            margin-top: 30px;
            background-color: #343a40; /* Dark Grey */
            color: #fff;
             font-size: 1.1em;
             transition: background-color 0.3s ease;
        }
         #show-explanation-btn:hover {
             background-color: #495057;
         }
         #show-explanation-btn.pulsing {
             animation: pulse 2s infinite;
         }

         @keyframes pulse {
             0% { box-shadow: 0 0 0 0 rgba(52, 58, 64, 0.4); }
             70% { box-shadow: 0 0 0 10px rgba(52, 58, 64, 0); }
             100% { box-shadow: 0 0 0 0 rgba(52, 58, 64, 0); }
         }


        #explanation {
            margin-top: 30px;
            padding: 25px;
            background-color: #fcf8e3; /* Lighter yellow */
            border: 1px solid #faebcc;
            border-radius: 10px;
            color: #856404;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
             transition: opacity 0.5s ease-in-out, visibility 0.5s ease-in-out;
        }
         #explanation h2 {
             color: #856404;
             border-bottom: 2px solid #faebcc;
             padding-bottom: 10px;
         }
         #explanation h3, #explanation h4 {
             color: #a17f1a; /* Slightly darker yellow/brown */
             text-align: right;
             margin-top: 20px;
             margin-bottom: 10px;
         }
         #explanation ul, #explanation ol {
             margin-bottom: 15px;
             padding-right: 20px; /* Indent lists */
         }
         #explanation li {
             margin-bottom: 8px;
             color: #555;
         }
          #explanation.hidden {
             visibility: hidden;
             opacity: 0;
             height: 0;
             padding: 0;
             margin-top: 0;
             border: none;
         }

         .hidden {
             display: none; /* Used initially for elements that should be hidden */
         }
         .visible {
             display: block;
         }
         /* Ensure elements transition smoothly from hidden state (using visibility/opacity) */
          .transitioning {
              /* A class to apply during the transition */
              /* No specific styles needed here, just a marker */
          }

    </style>

    <script>
        const scenarios = [
            {
                title: "תרחיש 1: המסעדה הקלאסית המצטיינת",
                description: "אתה מבקר במסעדה ותיקה בעיר אירופאית קלאסית, שידועה בבישול צרפתי מסורתי. המנות מוגשות באלגנטיות, כל פרט מושלם. חומרי הגלם הם פשוט הטובים ביותר שיש (לובסטר חי מהאקווריום, פטריות כמהין שחורות בעונתן). הטעמים עשירים, עמוקים ומדויקים לחלוטין. ניכרת שליטה טכנית אבסולוטית בכל מנה, אך אין הפתעות גדולות או חדשנות פורצת דרך. אישיות השף באה לידי ביטוי דרך שלמות הביצוע ולא דרך יצירתיות פרועה. השירות מקצועי, קשוב אך מעט רשמי. האווירה יוקרתית ושקטה. ביקרת כאן 3 פעמים בחצי השנה האחרונה, ובכל פעם החוויה הייתה זהה ברמתה הגבוהה. המחירים גבוהים, כצפוי ממקום ברמה זו, אך מוצדקים על ידי איכות הביצוע והחומרים.",
                expected: {
                    quality: 5, mastery: 5, personality: 3, value: 4, consistency: 5, stars: [2, 3] // Solid 2, potential for 3 if the "perfection" is truly transcendant
                },
                feedback: "תרחיש זה מציג מסעדה שמצטיינת באופן יוצא דופן בבסיס הקולינרי: איכות מוצרים ושליטה טכנית. אלו עמודי התווך לדירוג גבוה. אישיות המטבח אולי פחות 'צעקנית' ממקומות חדשניים, אך העקביות המוחלטת והדיוק המופתי מפצים על כך. יחס מחיר-איכות טוב יחסית לרמה. מסעדה כזו היא מועמדת חזקה מאוד לשני כוכבים (מטבח יוצא דופן ששווה לעצור בדרך עבורו), ולגבול שלושה כוכבים אם שלמות הביצוע מגיעה לרמה שמצדיקה מסע מיוחד במיוחד.",
            },
            {
                title: "תרחיש 2: הכוכב העולה והמרדני",
                description: "נשלחת לבדוק מסעדה חדשה שהפכה לשיחת העיר. השף הצעיר מגיע מרקע מרדני, והמטבח שלו משלב טכניקות מולקולריות עם טעמים מקומיים מפתיעים. המנות נראות כמו יצירות אמנות מודרנית. חלק מהטעמים הם התגלות של ממש - שילובים שלא דמיינת שיתאימו, בביצוע טכני מרשים. עם זאת, מנות אחרות מרגישות מאולצות, 'גימיקיות', או פשוט לא מאוזנות מספיק. חומרי הגלם טובים מאוד, אך לא תמיד הפרימיום העולמי. אישיות השף נוכחת בכל מנה, גם אם לא תמיד לטובה. השירות ידידותי ונלהב אך לעיתים מפוזר. ביקרת פעמיים, ובביקור השני כמה מהמנות שהיו מצוינות בביקור הראשון היו הפעם פחות טובות. המחירים יחסית גבוהים לפוטנציאל, והחוסר אחידות מקשה להצדיק אותם לחלוטין.",
                 expected: {
                    quality: 4, mastery: 4, personality: 5, value: 3, consistency: 3, stars: [0, 1] // High personality/potential, but inconsistency and occasional misses hurt Michelin chances
                },
                feedback: "כאן אנו רואים הדגשה חזקה של 'אישיות המטבח' ויצירתיות. מישלן בהחלט מעריכה חדשנות, אבל היא חייבת לעמוד בסטנדרטים גבוהים בכל שאר הקריטריונים, במיוחד 'שליטה בטעמים וטכניקות' ו'איכות מוצרים', והכי חשוב - 'עקביות'. החולשה העיקרית כאן היא חוסר האחידות בין מנות ובין ביקורים. מסעדה ברמת כוכב מישלן נדרשת לספק חוויה מצוינת *באופן עקבי*. רגעים מבריקים אינם מספיקים אם יש גם פספוסים. מסעדה כזו יכולה לקבל כוכב אם הרגעים המבריקים רבים ומרשימים במיוחד, או לא לקבל כלל אם חוסר העקביות בולט מדי.",
            },
            {
                title: "תרחיש 3: פסגת החוויה הקולינרית",
                description: "זה הביקור שחיכית לו. מסעדת יעד הממוקמת בקצה העולם, שמצריכה טיסה ותכנון מוקדם של חודשים. מהרגע שנכנסת, החוויה קולחת ללא רבב. חומרי הגלם הם נדירים, מגיעים מכל קצוות תבל ונבחרו בקפידה אובססיבית. כל מנה היא מסע קולינרי בפני עצמו - יצירת אומנות שמפעילה את כל החושים. שילוב הטעמים מפעים, הטכניקות מורכבות אך בלתי מורגשות במוצר הסופי, והביצוע מושלם לחלוטין, פעם אחר פעם. סגנון השף אישי, מובהק ומספר סיפור לאורך כל הארוחה. השירות צופה כל צורך עוד לפני שחשבת עליו, בלתי מורגש אך תמיד נוכח. האווירה אלגנטית, מרגיעה ומעצימה את החוויה. ביקרת שלוש פעמים בעבר, וכל ביקור היה ברמה עילאית. המחיר גבוה מאוד, אך הוא תואם את האיכות והחוויה יוצאת הדופן באמת.",
                expected: {
                    quality: 5, mastery: 5, personality: 5, value: 4, consistency: 5, stars: [3] // The epitome of 3 stars
                },
                feedback: "זהו תיאור קלאסי של מסעדה ברמת 3 כוכבי מישלן - 'מטבח מצוין הראוי למסע מיוחד'. מצוינות מוחלטת בכל הקריטריונים: חומרי גלם נדירים ועילאיים, שליטה טכנית וטעמים ללא רבב, אישיות מטבח חזקה וייחודית שהופכת את הארוחה לחוויה בלתי נשכחת, ועקביות ברזולוציה הגבוהה ביותר. 'יחס מחיר-איכות' נבחן ברמה הזו ביחס לאיכות יוצאת הדופן, לא האם המחיר נמוך. מסעדה כזו מייצגת את פסגת היצירה הקולינרית ובהחלט מצדיקה את הדירוג הגבוה ביותר.",
            },
             {
                title: "תרחיש 4: ההבטחה שלא מומשה",
                description: "ביקרת במסעדה חדשה שנפתחה על ידי שף עם פוטנציאל, אך ההוצאה לפועל היתה מאכזבת. חומרי הגלם היו בינוניים, הירקות נראו עייפים, והבשר לא היה בנתח הטוב ביותר. יש ניסיונות לטכניקות מורכבות כמו סו-ויד או ג'לים, אבל הדיוק חסר, מה שפוגע במרקם ובטעם. הטעמים עצמם עמוסים מדי, חסרי הרמוניה, כאילו השף מנסה יותר מדי בבת אחת. אין סגנון אחיד או קו מחשבה ברור במנות. השירות היה ידידותי אך איטי ומפוזר. האווירה רועשת ולא נעימה. המחירים גבוהים יחסית לאיכות שהתקבלה, והתחושה היתה של פספוס גדול.",
                expected: {
                    quality: 2, mastery: 2, personality: 2, value: 2, consistency: 2, stars: [0] // Clear miss by Michelin standards
                },
                feedback: "תרחיש זה מדגים מצב שבו אף אחד מהקריטריונים המרכזיים של מישלן אינו עומד בסטנדרט הנדרש. איכות מוצרים ירודה, חוסר שליטה בטכניקות וטעמים, היעדר אישיות קולינרית ברורה, חוסר עקביות (גם אם זה ביקור ראשון, הפערים בולטים), ויחס מחיר-איכות נמוך - כל אלו מצביעים על כך שהמסעדה רחוקה מרמת כוכב מישלן. מסעדה כזו לא תקבל כוכב, ובמרבית המקרים גם לא תופיע במדריך כלל, אלא אם כן היא מצטיינת בתחום אחר (כמו מחיר נוח מאוד לאיכותה), מה שלא קרה כאן. שיפוט נכון במקרה זה הוא 0 כוכבים.",
            }
        ];

        let currentScenarioIndex = 0;

        // Element references
        const scenarioContainer = document.getElementById('scenario');
        const scenarioTitle = document.getElementById('scenario-title');
        const scenarioDescription = document.getElementById('scenario-description');
        const ratingSection = document.getElementById('rating-section');
        const feedbackContainer = document.getElementById('feedback-container');
        const feedbackContent = document.getElementById('feedback-content');
        const submitButton = document.getElementById('submit-rating');
        const nextButton = document.getElementById('next-scenario');
         const continueAfterFeedbackButton = document.getElementById('continue-after-feedback');
        const explanationButton = document.getElementById('show-explanation-btn');
        const explanationSection = document.getElementById('explanation');
        const completionMessage = document.getElementById('completion-message');


        const qualityInput = document.getElementById('quality');
        const masteryInput = document.getElementById('mastery');
        const personalityInput = document.getElementById('personality');
        const valueInput = document.getElementById('value');
        const consistencyInput = document.getElementById('consistency');
        const starsInput = document.getElementById('stars');

        const qualityValueSpan = document.getElementById('quality-value');
        const masteryValueSpan = document.getElementById('mastery-value');
        const personalityValueSpan = document.getElementById('personality-value');
        const valueValueSpan = document.getElementById('value-value');
        const consistencyValueSpan = document.getElementById('consistency-value');
        const starsValueSpan = document.getElementById('stars-value');

        // Helper for smooth transitions
        function transitionElement(element, show) {
            if (show) {
                element.classList.remove('hidden');
                 // Use requestAnimationFrame to ensure display block is applied before transition
                 requestAnimationFrame(() => {
                     requestAnimationFrame(() => {
                         element.style.opacity = 1;
                         element.style.height = 'auto'; // Animate height
                         element.style.padding = show ? '20px' : '0'; // Restore padding if needed
                         element.style.marginTop = show ? '20px' : '0'; // Restore margin if needed
                         element.style.border = show ? '' : 'none'; // Restore border
                          // Remove visibility: hidden after transition ends
                          element.addEventListener('transitionend', function handler() {
                              element.style.visibility = 'visible';
                              element.removeEventListener('transitionend', handler);
                          });
                     });
                 });
            } else {
                 element.style.opacity = 0;
                 element.style.height = '0';
                 element.style.padding = '0';
                 element.style.marginTop = '0';
                 element.style.border = 'none';
                 element.style.visibility = 'hidden';
                element.classList.add('hidden'); // Add hidden class after transition
            }
        }


        // Function to update span values next to sliders
        function updateSpanValue(inputElement, spanElement) {
             const value = inputElement.value;
             spanElement.textContent = value;
             // Simple visual feedback on slider value change
             spanElement.style.transform = 'scale(1.1)';
             spanElement.style.transition = 'transform 0.1s ease';
             setTimeout(() => {
                 spanElement.style.transform = 'scale(1)';
                 spanElement.style.transition = 'transform 0.1s ease';
             }, 100);
        }

        // Add event listeners to sliders to update span values
        qualityInput.addEventListener('input', () => updateSpanValue(qualityInput, qualityValueSpan));
        masteryInput.addEventListener('input', () => updateSpanValue(masteryInput, masteryValueSpan));
        personalityInput.addEventListener('input', () => updateSpanValue(personalityInput, personalityValueSpan));
        valueInput.addEventListener('input', () => updateSpanValue(valueInput, valueValueSpan));
        consistencyInput.addEventListener('input', () => updateSpanValue(consistencyInput, consistencyValueSpan));
        starsInput.addEventListener('input', () => updateSpanValue(starsInput, starsValueSpan));


        function loadScenario(index) {
             if (index < scenarios.length) {
                const scenario = scenarios[index];
                scenarioTitle.textContent = scenario.title;
                scenarioDescription.textContent = scenario.description;

                transitionElement(scenarioContainer, true); // Show scenario
                transitionElement(ratingSection, true); // Show rating section
                transitionElement(feedbackContainer, false); // Hide feedback
                transitionElement(completionMessage, false); // Hide completion
                transitionElement(submitButton, true); // Show submit button
                transitionElement(nextButton, false); // Hide next button
                transitionElement(continueAfterFeedbackButton, false); // Hide continue button
                explanationButton.classList.remove('pulsing'); // Remove pulsing from explanation button

                // Reset slider values to default (3 for criteria, 0 for stars) and update spans
                 qualityInput.value = 3; updateSpanValue(qualityInput, qualityValueSpan);
                 masteryInput.value = 3; updateSpanValue(masteryInput, masteryValueSpan);
                 personalityInput.value = 3; updateSpanValue(personalityInput, personalityValueSpan);
                 valueInput.value = 3; updateSpanValue(valueInput, valueValueSpan);
                 consistencyInput.value = 3; updateSpanValue(consistencyInput, consistencyValueSpan);
                 starsInput.value = 0; updateSpanValue(starsInput, starsValueSpan);

            } else {
                // All scenarios completed
                transitionElement(scenarioContainer, false); // Hide scenario
                transitionElement(ratingSection, false); // Hide rating section
                transitionElement(feedbackContainer, false); // Hide feedback
                transitionElement(submitButton, false); // Hide submit button
                transitionElement(nextButton, false); // Hide next button
                transitionElement(continueAfterFeedbackButton, false); // Hide continue button

                transitionElement(completionMessage, true); // Show completion message
                 explanationButton.classList.add('pulsing'); // Pulse explanation button
            }
        }

        function submitRating() {
            const userRatings = {
                quality: parseInt(qualityInput.value),
                mastery: parseInt(masteryInput.value),
                personality: parseInt(personalityInput.value),
                value: parseInt(valueInput.value),
                consistency: parseInt(consistencyInput.value),
                stars: parseInt(starsInput.value)
            };

            const currentScenario = scenarios[currentScenarioIndex];
            const expected = currentScenario.expected;

            let feedbackHtml = `<p>${currentScenario.feedback}</p>`; // Start with general feedback from scenario data

            // Add dynamic feedback based on user's ratings vs expected
            feedbackHtml += `<p><strong>הערכה שלך:</strong><br>`;
            const criteria = ['quality', 'mastery', 'personality', 'value', 'consistency'];
            criteria.forEach(crit => {
                 let emoji = '✅';
                 let diff = userRatings[crit] - expected[crit];
                 if (Array.isArray(expected[crit])) { // If expected is a range
                     if (userRatings[crit] < expected[crit][0]) { emoji = '👇'; diff = userRatings[crit] - expected[crit][0]; }
                     else if (userRatings[crit] > expected[crit][expected[crit].length - 1]) { emoji = '☝️'; diff = userRatings[crit] - expected[crit][expected[crit].length - 1]; }
                     else { emoji = '👍'; diff = 0;} // Within range
                 } else { // If expected is a single value
                     if (Math.abs(diff) > 1) emoji = diff > 0 ? '☝️' : '👇'; // Significant difference
                     else if (diff !== 0) emoji = '🤏'; // Small difference
                 }


                 feedbackHtml += `- ${crit === 'quality' ? 'איכות מוצרים' : crit === 'mastery' ? 'שליטה' : crit === 'personality' ? 'אישיות' : crit === 'value' ? 'מחיר-איכות' : 'עקביות'}: ${userRatings[crit]}/5 ${emoji}<br>`;
            });

             // Feedback on star rating
             let starEmoji = '✅';
             let starDiffMsg = '';
             if (Array.isArray(expected.stars)) {
                 if (userRatings.stars < expected.stars[0]) { starEmoji = '👇'; starDiffMsg = ` (ציפינו למינימום ${expected.stars[0]} כוכבים)`; }
                 else if (userRatings.stars > expected.stars[expected.stars.length - 1]) { starEmoji = '☝️'; starDiffMsg = ` (ציפינו למקסימום ${expected.stars[expected.stars.length - 1]} כוכבים)`; }
                  else { starEmoji = '👍'; starDiffMsg = ` (הערכת הכוכבים שלך בטווח הצפוי של ${expected.stars.join('-')} כוכבים)`}
             } else {
                  if (userRatings.stars !== expected.stars) { starEmoji = userRatings.stars > expected.stars ? '☝️' : '👇'; starDiffMsg = ` (הערכת כוכבים שונה מהצפוי: ${expected.stars} כוכבים)`; }
                  else { starEmoji = '👍'; starDiffMsg = ` (הערכת הכוכבים שלך תואמת את הצפוי: ${expected.stars} כוכבים)`; }
             }

            feedbackHtml += `- המלצת כוכבים: ${userRatings.stars}⭐ ${starEmoji}${starDiffMsg}</p>`;

            feedbackContent.innerHTML = feedbackHtml;

            transitionElement(ratingSection, false); // Hide rating section
            transitionElement(submitButton, false); // Hide submit button
            transitionElement(feedbackContainer, true); // Show feedback

             if (currentScenarioIndex < scenarios.length - 1) {
                 transitionElement(continueAfterFeedbackButton, true); // Show continue if not last scenario
             } else {
                 transitionElement(explanationButton, true); // Ensure explanation button is visible at the end
                 explanationButton.classList.add('pulsing'); // Pulse explanation button
             }
        }

        // Event Listeners
        submitButton.addEventListener('click', submitRating);

         continueAfterFeedbackButton.addEventListener('click', () => {
             currentScenarioIndex++;
             loadScenario(currentScenarioIndex);
         });


        explanationButton.addEventListener('click', () => {
             const isHidden = explanationSection.classList.contains('hidden');
             transitionElement(explanationSection, isHidden);
             explanationButton.classList.remove('pulsing'); // Stop pulsing after clicking
             // Scroll to the explanation section if it's shown
            if (isHidden) {
                explanationSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });


        // Initial load
        loadScenario(currentScenarioIndex);

    </script>
</main>