---
title: "העיר החיה: צור אותה, שנה אותה - מסע בזמן מהחומה לגורד שחקים"
english_slug: the-living-city-build-it-change-it-a-time-journey-from-the-wall-to-the-skyscraper
category: "ארכאולוגיה"
tags: [היסטוריה עירונית, התפתחות ערים, ימי הביניים, עת חדשה, תכנון עירוני, סימולציה, גאוגרפיה היסטורית]
---
<h1>העיר החיה: צור אותה, שנה אותה - מסע בזמן מהחומה לגורד שחקים</h1>
<p>האם דמיינתם פעם איך נראו הרחובות שאתם מכירים לפני מאות שנים? איך כפר קטן הפך למטרופולין שוקק? הצטרפו למסע אינטראקטיבי בזמן ובנו בעצמכם את סיפור הצמיחה העירונית!</p>

<div id="app">
    <div id="controls">
        <div id="period-select">
            <h2>בחרו תקופה:</h2>
            <button class="period-btn active" data-period="medieval">ימי הביניים</button>
            <button class="period-btn" data-period="renaissance">רנסנס / עת חדשה מוקדמת</button>
            <button class="period-btn" data-period="industrial">המהפכה התעשייתית</button>
            <button class="period-btn" data-period="modern">עת מודרנית / עכשווית</button>
        </div>
        <div id="building-options">
            <h2>אלמנטים לבנייה:</h2>
            <!-- Building options will load here based on period -->
        </div>
        <div id="info-panel">
            <h2>לוח בקרה:</h2>
            <p>לחצו על אלמנט לבנייה, ואז לחצו על המפה כדי להוסיף אותו לעיר.</p>
        </div>
    </div>
    <div id="map-container">
        <div id="map">
            <!-- Base map elements -->
             <div class="base-element base-river"></div>
             <div class="base-element base-castle" style="left: 50%; top: 40%;"></div>
             <!-- More initial medieval houses for a village feel -->
             <div class="base-element base-houses medieval initial" style="left: 50%; top: 45%;"></div>
             <div class="base-element base-houses medieval initial" style="left: 55%; top: 50%;"></div>
             <div class="base-element base-houses medieval initial" style="left: 45%; top: 50%;"></div>
              <div class="base-element base-houses medieval initial" style="left: 52%; top: 53%;"></div>
             <div class="base-element base-houses medieval initial" style="left: 48%; top: 53%;"></div>
             <!-- Initial wall segment example -->
             <div class="base-element base-wall medieval initial" style="width: 120px; height: 5px; left: 40%; top: 60%;"></div>
              <div class="base-element base-wall medieval initial" style="width: 5px; height: 80px; left: 40%; top: 60%;"></div>
              <div class="base-element base-wall medieval initial" style="width: 5px; height: 80px; left: 55%; top: 60%;"></div>
               <div class="base-element base-wall medieval initial" style="width: 120px; height: 5px; left: 40%; top: 68%;"></div>

            <!-- Placed buildings will appear here -->
             <div id="placement-preview" class="placed-element" style="display: none; opacity: 0.7; pointer-events: none;"></div>
        </div>
    </div>
</div>

<button id="toggleExplanation">הצגת הסיפור המלא של העיר</button>

<div id="explanation" style="display: none;">
    <h2>מבוא: העיר כפלימפססט של היסטוריה חיה</h2>
    <p>ערים אינן רק אוסף של מבנים ורחובות – הן אורגניזמים חיים, נושמים ומשתנים ללא הרף. כל אבן, כל שביל, כל גורד שחקים הוא עדות לתהליכים היסטוריים עמוקים: החלטות אמיצות, המצאות פורצות דרך, שינויים חברתיים וכלכליים מטלטלים. דמיינו את העיר כ"פלימפססט" (Palimpsest) – מגילה עתיקה שעליה נכתבו סיפורים שוב ושוב, כששכבות העבר מציצות מתחת למילים החדשות. מסע בזמן אל לב העיר מגלה לנו כיצד עברה טרנספורמציות מדהימות לאורך הדורות, ומסייע לנו לפענח את המבנה והאופי הייחודי של המרחב העירוני שאנו חיים בו היום.</p>

    <h2>העיר בימי הביניים: חיים בצל החומות</h2>
    <p>בעולם של אי-ודאות ואיומים, העיר בימי הביניים צמחה לרוב בחיק מבצר (טירה) או מרכז רוחני (קתדרלה). החומות האדירות לא רק הגנו עליה פיזית, אלא גם עיצבו את צורתה הצפופה והמפותלת. בתוך החומות הדחוסות שקק חיים של מסחר מקומי תוסס בשווקים, מלאכה מיומנת שאורגנה בגילדות קפדניות, ומרכז שירותים חיוני לאזור החקלאי שמסביב. הרחובות הצרים, לעיתים קרובות נטולי תכנון, והתנאים הסניטריים המאתגרים, יצרו מרחב אנושי אינטנסיבי ורב-חושי, בו כל פינה סיפרה סיפור של קהילה והישרדות.</p>

    <h2>הרנסנס והעת החדשה המוקדמת: מבט חדש על המרחב</h2>
    <p>עם דעיכת ימי הביניים ועליית כוחם של מדינות לאום וסחר בינלאומי, הערים החלו להתאושש ולגדול. הרנסנס הביא עמו לא רק מהפכה באמנות ובמדע, אלא גם גישה חדשה לתכנון המרחב העירוני. באיטליה ובמקומות נוספים, החלו מתכננים לראות בעיר יצירת אמנות בפני עצמה, עם דגש על סימטריה, פרופורציה, כיכרות רחבות ידיים, ארמונות מפוארים ורחובות ישרים שנועדו להפגין כוח וסדר. הגידול באוכלוסייה והתרחבות הפעילות הכלכלית החלו ללחוץ על גבולות החומות הישנות, ובנייה החלה לזלוג החוצה, אך רוב האוכלוסייה נותרה מרוכזת בתוך הגרעין ההיסטורי.</p>

    <h2>המהפכה התעשייתית: עשן, ברזל וצמיחה אקספלואיסיבית</h2>
    <p>המאה ה-19 שינתה את פני העיר ללא היכר. המעבר המטאורי מחברה חקלאית לחברה תעשייתית גרם למסע נדודים עצום של מיליוני אנשים מהכפרים אל המרכזים העירוניים, בחיפוש אחר פרנסה במפעלים החדשים. ערים התנפחו במהירות מסחררת, לרוב ללא תכנון או פיקוח. נוף עירוני חדש נולד: ארובות מתמרות, מסילות רכבת החוצות שכונות, ובתי חרושת שפלטו עשן ורעש. הגידול המואץ יצר אתגרים חברתיים קשים מנשוא: שכונות פועלים דחוסות ועניות, תנאי תברואה מחרידים, זיהום אוויר ומים חמור, ומחלות שהתפשטו במהירות. זו הייתה תקופה של קדמה טכנולוגית לצד סבל אנושי עצום, שהובילה בסופו של דבר לקריאות לרפורמה ולתחילתו של התכנון העירוני המודרני.</p>

    <h2>המאה ה-20 והעת העכשווית: מהירות, מרחב ואתגרי העתיד</h2>
    <p>המאה ה-20 היתה עידן התחבורה והטכנולוגיה, שהשפיעו עמוקות על צורת העיר. המצאת הרכב הפרטי הפכה את האוטוסטרדה לסמל עירוני והובילה לתופעת ה"פרבור" (Suburbanization) – התפשטות האוכלוסייה לפרוורים ירוקים יותר, מחוץ לגרעין העירוני ההיסטורי. התכנון העירוני הפך מקצוע מדעי, עם דגש על הפרדת אזורי שימוש (מגורים, תעשייה, מסחר), בניית גורדי שחקים ששינו את קו הרקיע, פיתוח פארקים רחבי ידיים ומערכות תחבורה מסיביות. כיום, הערים עומדות בפני אתגרים גלובליים מורכבים: שינויי אקלים, צורך בתחבורה בת קיימא, התחדשות עירונית שמכבדת את העבר אך מסתכלת לעתיד, והפיכתן למרחבים מכילים, חכמים וירוקים יותר עבור כל תושביהן.</p>

    <h2>המנועים הגדולים של השינוי העירוני</h2>
    <p>מה גורם לעיר להשתנות? תמיד מדובר בשילוב כוחות:
        <ul>
            <li><strong>טכנולוגיה:</strong> מגלגל המים, דרך מנוע הקיטור והמעלית, ועד האינטרנט והמכונית האוטונומית – טכנולוגיה תמיד שינתה את האופן שבו אנו חיים, בונים ומתניידים בעיר.</li>
            <li><strong>כלכלה:</strong> ממסחר ימי, דרך תעשייה כבדה, ועד כלכלת ידע ושירותים – המודל הכלכלי מכתיב היכן יתמקדו העסקים, היכן יעבדו אנשים, ואילו מבנים יהיו נחוצים.</li>
            <li><strong>חברה ותרבות:</strong> גידול אוכלוסין, תנועות הגירה, שינויים בהרכב החברתי, מודעות סביבתית, מדיניות ממשלתית ותפיסות תרבותיות משפיעים על אופי החיים העירוניים ועל הכיוון אליו העיר צומחת.</li>
        </ul>
    </p>
</div>

<style>
    body {
        font-family: 'Arial Hebrew', 'David', sans-serif; /* Use Hebrew fonts */
        line-height: 1.6;
        margin: 0;
        padding: 0; /* Remove default body padding */
        background: linear-gradient(to bottom, #e0f2f7, #b3e5fc); /* Subtle gradient background */
        color: #333;
        direction: rtl; /* Hebrew direction */
        text-align: right;
        min-height: 100vh; /* Ensure body covers full viewport height */
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    h1, h2 {
        color: #0056b3;
        text-align: center;
        margin-bottom: 15px;
    }
     h1 {
         margin-top: 20px;
         font-size: 2.2em;
     }
     p {
         margin-bottom: 1em;
         max-width: 900px;
         margin-left: auto;
         margin-right: auto;
         padding: 0 15px;
     }

    #app {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 25px; /* Increased gap */
        margin-top: 20px;
        background-color: rgba(255, 255, 255, 0.95); /* Slightly transparent white */
        padding: 30px; /* Increased padding */
        border-radius: 12px; /* More rounded corners */
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15); /* More pronounced shadow */
        width: 95%; /* Make it wider */
        max-width: 1000px; /* Max width for large screens */
        margin-bottom: 30px;
    }
    #controls {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 20px;
        width: 100%;
    }
     #period-select, #building-options, #info-panel {
        flex: 1;
        min-width: 280px; /* Slightly larger min-width */
        background-color: #eef; /* Light blue background */
        padding: 20px; /* Increased padding */
        border-radius: 8px; /* Rounded corners */
        border: 1px solid #cce; /* Lighter border */
        box-shadow: inset 0 1px 5px rgba(0, 0, 0, 0.05); /* Subtle inner shadow */
    }
     #period-select h2, #building-options h2, #info-panel h2 {
        margin-top: 0;
        margin-bottom: 15px;
        text-align: center;
         color: #0056b3;
         font-size: 1.3em;
         border-bottom: 1px solid #cce; /* Separator */
         padding-bottom: 10px;
    }
    #period-select button, .building-option {
        display: inline-block;
        padding: 10px 15px;
        margin: 5px 3px; /* Reduced horizontal margin */
        cursor: pointer;
        border: none; /* No default border */
        border-radius: 20px; /* Pill-shaped buttons */
        background-color: #e1f5fe; /* Very light blue */
        color: #01579b; /* Darker blue text */
        font-size: 1em;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Subtle button shadow */
    }
    #period-select button:hover, .building-option:hover {
        background-color: #b3e5fc; /* Lighter blue on hover */
        transform: translateY(-2px); /* Lift effect */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }
     #period-select button:active, .building-option:active {
         transform: translateY(0); /* Press effect */
         box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
     }
    #period-select button.active {
        background-color: #0277bd; /* Darker blue for active */
        color: #fff;
        box-shadow: 0 3px 6px rgba(0, 0, 0, 0.2);
    }
     .building-option {
        background-color: #e8f5e9; /* Very light green */
        color: #1b5e20; /* Darker green */
     }
      .building-option:hover {
        background-color: #c8e6c9; /* Lighter green on hover */
     }
     .building-option.selected {
        background-color: #388e3c; /* Darker green for selected */
        color: #fff;
        box-shadow: 0 3px 6px rgba(0, 0, 0, 0.2);
     }
     #info-panel p {
         text-align: center;
         margin-bottom: 0;
         padding: 0;
         font-size: 1.1em;
         color: #01579b;
     }
      #info-panel strong {
          color: #c2185b; /* Accent color */
      }


    #map-container {
        width: 100%;
        max-width: 900px; /* Slightly wider map */
        aspect-ratio: 4 / 3;
        border: 2px solid #000;
        position: relative;
        overflow: hidden;
        background: radial-gradient(circle at 50% 80%, #a5d6a7, #66bb6a); /* More engaging ground color */
        box-shadow: inset 0 0 15px rgba(0,0,0,0.3); /* Stronger inner shadow */
        border-radius: 8px;
        cursor: crosshair; /* Cursor indicates placing */
    }
     #map {
         position: relative;
         width: 100%;
         height: 100%;
     }

     .base-element {
         position: absolute;
         transform: translate(-50%, -50%); /* Center element on coordinates */
         transition: opacity 0.5s ease; /* Fade effect for base elements */
         z-index: 1; /* Ensure base elements are below placed */
     }
     .base-river {
         width: 110%; /* Make it slightly wider than map */
         height: 50px; /* Thicker river */
         background: linear-gradient(to right, #0277bd, #039be5); /* Blue gradient */
         bottom: 5%; /* Slightly higher */
         left: -5%; /* Start slightly off-left */
         transform: none; /* Don't center river */
         border-top: 2px solid #01579b;
         border-bottom: 2px solid #01579b;
         box-shadow: 0 0 10px rgba(0, 100, 200, 0.5); /* Subtle glow */
         z-index: 0; /* River at the back */
     }
     .base-castle {
         width: 90px; /* Slightly larger */
         height: 90px;
         background-color: #795548; /* Brown */
         border: 3px solid #5d4037; /* Darker brown border */
         border-radius: 5px;
         box-shadow: 3px 3px 8px rgba(0,0,0,0.4);
         z-index: 2; /* Castle on top of initial village */
         background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect x="10" y="20" width="80" height="70" fill="%238d6e63"/><rect x="0" y="10" width="100" height="10" fill="%235d4037"/><rect x="15" y="0" width="10" height="20" fill="%235d4037"/><rect x="45" y="0" width="10" height="20" fill="%235d4037"/><rect x="75" y="0" width="10" height="20" fill="%235d4037"/><circle cx="50" cy="50" r="40" fill-opacity="0"/></svg>'); /* Simple SVG castle graphic */
          background-size: 80% auto;
          background-repeat: no-repeat;
          background-position: center 10%;
          color: #fff; /* For text label */
          font-size: 0.8em;
          display: flex;
          align-items: flex-end;
          justify-content: center;
          padding-bottom: 5px;
          text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
     }
     /* Base houses and walls fade out in later periods */
     .base-houses.initial, .base-wall.initial {
         transition: opacity 0.7s ease;
     }
     .base-houses {
          width: 35px; /* Slightly larger */
          height: 35px;
          background-color: #ff8a65; /* Light orange-red */
          border: 2px solid #f4511e; /* Darker border */
          border-radius: 4px;
          box-shadow: 1px 1px 3px rgba(0,0,0,0.2);
          z-index: 1;
          background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect x="10" y="40" width="80" height="50" fill="%23f4511e"/><path d="M10 40 L50 10 L90 40 Z" fill="%23bf360c"/></svg>'); /* Simple house SVG */
          background-size: 90% auto;
          background-repeat: no-repeat;
          background-position: center bottom;
     }
     .base-wall {
         background-color: #8d6e63; /* Brown */
         border: 2px solid #5d4037; /* Darker border */
         box-shadow: 1px 1px 3px rgba(0,0,0,0.2);
         z-index: 1;
     }
     .base-wall[style*="width: 5px"] { /* Style for vertical segments */
          width: 8px !important; /* Make vertical walls slightly wider */
     }
      .base-wall[style*="height: 5px"] { /* Style for horizontal segments */
          height: 8px !important; /* Make horizontal walls slightly wider */
     }


    .placed-element {
        position: absolute;
        /* Default size - specific types override */
        width: 50px;
        height: 50px;
        background-color: #ccc; /* Default */
        border: 2px solid #666;
        transform: translate(-50%, -50%) scale(0.5); /* Start smaller for animation */
        opacity: 0; /* Start invisible */
        animation: placeElement 0.5s ease-out forwards; /* Animation on placement */
        z-index: 2; /* Above base elements, below preview */
        box-sizing: border-box;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 0.7em; /* Smaller text */
        text-align: center;
        color: white;
        padding: 3px; /* Increased padding */
        overflow: hidden;
        cursor: grab; /* Indicates it can be interacted with (though dragging isn't implemented, this feels gamey) */
        box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
        transition: box-shadow 0.2s ease; /* Hover effect */
    }

    .placed-element:hover {
        box-shadow: 3px 3px 8px rgba(0,0,0,0.4); /* Lift on hover */
    }

     #placement-preview {
         z-index: 3; /* Above placed elements */
         box-shadow: 0 0 10px rgba(0, 150, 255, 0.6); /* Glow effect */
         border-style: dashed; /* Dashed border */
     }


    /* Specific building styles - using brighter/clearer colors */
     .building-market { background-color: #ffeb3b; color: #333; width: 60px; height: 40px; border-color: #fbc02d;} /* Yellow */
     .building-guildhall { background-color: #bdbdbd; color: #333; border-color: #757575;} /* Grey */
     .building-cathedral { background-color: #7e57c2; color: #fff; width: 70px; height: 80px; border-color: #5e35b1;} /* Deep Purple */
     .building-factory { background-color: #455a64; color: #fff; width: 80px; height: 60px; border-color: #263238;} /* Blue Grey */
     .building-railway { background-color: #bf360c; color: #fff; width: 100%; height: 10px; border: none; transform: translate(-50%, -50%) scaleX(0.5); opacity: 0; animation: placeRailway 0.8s ease-out forwards; background-image: linear-gradient(to right, #bf360c 50%, #a1310b 50%); background-size: 20px 10px;} /* Deep Orange - Represents a line */
     .building-planned-street { background-color: #e0e0e0; color: #333; width: 100px; height: 10px; border-color: #9e9e9e; transform: translate(-50%, -50%) scaleX(0.5); opacity: 0; animation: placeStreet 0.6s ease-out forwards;} /* Grey - Represents a street segment */
     .building-skyscraper { background-color: #4dd0e1; color: #fff; width: 40px; height: 120px; border-color: #00bcd4; background-image: linear-gradient(rgba(255,255,255,0.2) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.2) 1px, transparent 1px); background-size: 10px 10px;} /* Cyan - Window pattern */
     .building-park { background-color: #8bc34a; color: #333; width: 80px; height: 80px; border: 2px dashed #33691e; border-radius: 50%; background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="30" cy="70" r="15" fill="%2333691e"/><circle cx="70" cy="70" r="15" fill="%2333691e"/><circle cx="50" cy="40" r="20" fill="%2333691e"/></svg>'); background-size: 80% auto; background-repeat: no-repeat; background-position: center;} /* Light Green - Trees icon */
     .building-highway { background-color: #78909c; color: #fff; width: 180px; height: 30px; border-color: #455a64; background-image: linear-gradient(to right, transparent 45%, #e0e0e0 45%, #e0e0e0 55%, transparent 55%); background-size: 20px 30px;} /* Blue Grey - Road lines */

    /* Animation Keyframes */
    @keyframes placeElement {
        to {
            transform: translate(-50%, -50%) scale(1);
            opacity: 1;
        }
    }
     @keyframes placeRailway {
         to {
            transform: translate(-50%, -50%) scaleX(1);
            opacity: 1;
         }
     }
     @keyframes placeStreet {
         to {
            transform: translate(-50%, -50%) scaleX(1);
            opacity: 1;
         }
     }


    #toggleExplanation {
        display: block;
        margin: 30px auto;
        padding: 12px 25px; /* Slightly larger */
        font-size: 1.2em; /* Larger font */
        cursor: pointer;
        border: none;
        border-radius: 25px; /* Rounded pill shape */
        background-color: #007bff; /* Primary blue */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
         box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3);
    }
    #toggleExplanation:hover {
        background-color: #0056b3; /* Darker blue */
        transform: translateY(-2px); /* Lift effect */
        box-shadow: 0 6px 12px rgba(0, 123, 255, 0.4);
    }
     #toggleExplanation:active {
        transform: translateY(0); /* Press effect */
        box-shadow: 0 2px 4px rgba(0, 123, 255, 0.2);
     }


    #explanation {
        margin-top: 20px;
        padding: 30px; /* Increased padding */
        background-color: #e3f2fd; /* Very light blue */
        border-radius: 12px; /* Rounded corners */
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        border-right: 6px solid #2196f3; /* Stronger visual marker */
        max-width: 900px; /* Match app width */
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 30px;
    }
    #explanation h2 {
        color: #0d47a1; /* Dark blue */
        margin-top: 20px;
        margin-bottom: 15px;
        border-bottom: 2px solid #bbdefb; /* Lighter separator */
        padding-bottom: 8px;
         text-align: right;
         font-size: 1.6em;
    }
     #explanation h2:first-of-type {
         margin-top: 0;
     }
     #explanation p {
         text-align: right;
         margin-bottom: 15px;
         font-size: 1.1em;
         line-height: 1.7;
         padding: 0; /* Remove padding added earlier */
         max-width: 100%; /* Allow explanation paragraphs full width within container */
     }
     #explanation ul {
         margin-bottom: 15px;
         padding-right: 20px; /* Indent list */
     }
      #explanation li {
          margin-bottom: 8px;
          line-height: 1.6;
      }
      #explanation strong {
          color: #d84315; /* Accent color for key terms */
      }

</style>

<script>
    const periodData = {
        medieval: {
            name: "ימי הביניים",
            buildings: [
                { id: 'medieval-market', type: 'building-market', name: 'שוק קטן', text: 'שוק' },
                { id: 'medieval-guildhall', type: 'building-guildhall', name: 'בית גילדות', text: 'גילדות' },
                { id: 'medieval-wall', type: 'base-wall', name: 'חומה נוספת (סמל)', text: 'חומה' }, // Re-using base style for a new placable element
                { id: 'medieval-houses', type: 'base-houses', name: 'קבוצת בתים', text: 'בתים' }
            ]
        },
        renaissance: {
            name: "רנסנס / עת חדשה מוקדמת",
            buildings: [
                { id: 'renaissance-market', type: 'building-market', name: 'שוק גדול יותר', text: 'שוק' },
                { id: 'renaissance-cathedral', type: 'building-cathedral', name: 'קתדרלה / כנסייה גדולה', text: 'כנסייה' },
                { id: 'renaissance-palace', type: 'base-castle', name: 'ארמון / מבנה ציבורי (סמל)', text: 'ארמון' },
                { id: 'renaissance-houses', type: 'base-houses', name: 'קבוצת בתים (צפופה)', text: 'בתים' },
                 { id: 'renaissance-planned-street', type: 'building-planned-street', name: 'רחוב מתוכנן (לסימון)', text: 'רחוב' }
            ]
        },
        industrial: {
            name: "המהפכה התעשייתית",
            buildings: [
                { id: 'industrial-factory', type: 'building-factory', name: 'מפעל', text: 'מפעל' },
                { id: 'industrial-railway', type: 'building-railway', name: 'מסילת רכבת (לסימון)', text: 'רכבת' },
                { id: 'industrial-tenements', type: 'base-houses', name: 'בתי פועלים (צפוף)', text: 'פועלים' }
            ]
        },
        modern: {
            name: "עת מודרנית / עכשווית",
            buildings: [
                { id: 'modern-skyscraper', type: 'building-skyscraper', name: 'גורד שחקים', text: 'מגדל' },
                { id: 'modern-park', type: 'building-park', name: 'פארק ציבורי', text: 'פארק' },
                { id: 'modern-highway', type: 'building-highway', name: 'כביש מהיר (לסימון)', text: 'כביש' },
                { id: 'modern-apartments', type: 'base-houses', name: 'בנייני מגורים (גבוה)', text: 'דירות' }
            ]
        }
    };

    let currentPeriod = 'medieval';
    let selectedBuilding = null; // Stores the { type, id, name, text } of building currently selected
    let placementPreview = document.getElementById('placement-preview');


    const mapContainer = document.getElementById('map-container'); // Use container for mouse tracking
    const mapElement = document.getElementById('map');
    const periodButtons = document.querySelectorAll('.period-btn');
    const buildingOptionsDiv = document.getElementById('building-options');
    const infoPanel = document.getElementById('info-panel');
    const toggleExplanationButton = document.getElementById('toggleExplanation');
    const explanationDiv = document.getElementById('explanation');

    // Function to render building options for the current period
    function renderBuildingOptions() {
        buildingOptionsDiv.innerHTML = '<h2>אלמנטים לבנייה:</h2>'; // Reset options
        const buildings = periodData[currentPeriod].buildings;
        if (buildings && buildings.length > 0) {
            buildings.forEach(b => {
                const btn = document.createElement('button');
                btn.classList.add('building-option');
                btn.textContent = b.name;
                btn.dataset.type = b.type;
                btn.dataset.id = b.id;
                 btn.dataset.text = b.text; // Store short text for map label
                btn.addEventListener('click', () => {
                    // Deselect any previously selected building
                    document.querySelectorAll('.building-option').forEach(opt => opt.classList.remove('selected'));
                    // Select the current building
                    btn.classList.add('selected');
                    selectedBuilding = { type: b.type, id: b.id, name: b.name, text: b.text };
                    infoPanel.innerHTML = `<h2>בנייה פעילה:</h2><p>לחצו על המפה כדי להוסיף: <br><strong>${b.name}</strong></p>`;
                     updatePlacementPreview(); // Show/update preview on selection
                });
                buildingOptionsDiv.appendChild(btn);
            });
        } else {
             buildingOptionsDiv.innerHTML += '<p>אין אפשרויות בנייה מיוחדות בתקופה זו.</p>';
        }
         // If the previously selected building is not available in the new period, clear selection
         if (selectedBuilding && !buildings.some(b => b.id === selectedBuilding.id)) {
             selectedBuilding = null;
             infoPanel.innerHTML = '<h2>לוח בקרה:</h2><p>בחרו אלמנט לבנייה, ואז לחצו על המפה כדי להוסיף אותו לעיר.</p>';
              hidePlacementPreview();
         } else if (selectedBuilding) {
              // If selected building is still valid, ensure info panel is updated
              infoPanel.innerHTML = `<h2>בנייה פעילה:</h2><p>לחצו על המפה כדי להוסיף: <br><strong>${selectedBuilding.name}</strong></p>`;
              updatePlacementPreview();
         } else {
             // If no building was selected initially or after period change
             infoPanel.innerHTML = '<h2>לוח בקרה:</h2><p>בחרו אלמנט לבנייה, ואז לחצו על המפה כדי להוסיף אותו לעיר.</p>';
              hidePlacementPreview();
         }
    }

    // Function to update the placement preview element
    function updatePlacementPreview() {
        if (!selectedBuilding) {
            hidePlacementPreview();
            return;
        }
         placementPreview.className = 'placed-element'; // Reset classes
         placementPreview.classList.add(selectedBuilding.type); // Add building specific class
         placementPreview.textContent = selectedBuilding.text; // Set text label
         placementPreview.style.display = 'flex'; // Show it
         placementPreview.style.opacity = '0.7'; // Set preview opacity
         placementPreview.style.animation = 'none'; // Disable placement animation for preview
          // Reset transform from animation to allow proper positioning
         placementPreview.style.transform = 'translate(-50%, -50%) scale(1)';
         placementPreview.style.borderStyle = 'dashed'; // Add dashed border
         placementPreview.style.boxShadow = '0 0 10px rgba(0, 150, 255, 0.6)'; // Add glow

         // Copy size styles from potential CSS rules (basic approximation)
         // This is a bit hacky, a better way would be to store sizes in periodData
         const tempDiv = document.createElement('div');
         tempDiv.className = selectedBuilding.type;
         tempDiv.style.cssText = 'position: absolute; visibility: hidden;';
         document.body.appendChild(tempDiv);
         const style = getComputedStyle(tempDiv);
         placementPreview.style.width = style.width;
         placementPreview.style.height = style.height;
         document.body.removeChild(tempDiv);


    }

     // Function to hide the placement preview element
     function hidePlacementPreview() {
         placementPreview.style.display = 'none';
     }


    // Function to change the active period
    function changePeriod(periodId) {
        if (periodId === currentPeriod) return;
        currentPeriod = periodId;

        // Update active button class
        periodButtons.forEach(btn => {
            btn.classList.remove('active');
            if (btn.dataset.period === periodId) {
                btn.classList.add('active');
            }
        });

        // Render building options for the new period
        renderBuildingOptions();

        // Update info panel
        infoPanel.innerHTML = `<h2>תקופה נוכחית:</h2><p><strong>${periodData[currentPeriod].name}</strong></p>`;

         // Fade out initial base elements that are "ancient" relative to the new period
        document.querySelectorAll('.base-element.initial').forEach(el => {
             // Simple logic: Medieval elements fade out slightly in non-medieval periods
             if (el.classList.contains('medieval')) {
                el.style.opacity = periodId === 'medieval' ? '1' : '0.4'; // Dim older elements
                // el.style.pointerEvents = periodId === 'medieval' ? 'auto' : 'none'; // Make older elements less interactive - maybe too complex
             }
             // Add similar logic for other base elements if introduced
        });

        // Optionally, fade out placed elements from FUTURE periods
         document.querySelectorAll('.placed-element').forEach(el => {
             // Elements placed in a later period than the current one are not visible
             const placedPeriod = el.dataset.period;
             const periods = Object.keys(periodData); // ['medieval', 'renaissance', ...]
             const placedIndex = periods.indexOf(placedPeriod);
             const currentIndex = periods.indexOf(currentPeriod);

             if (placedIndex > currentIndex) {
                 el.style.display = 'none'; // Hide future elements
             } else {
                  el.style.display = 'flex'; // Show current/past elements
                  el.style.opacity = placedIndex < currentIndex ? '0.6' : '1'; // Dim past elements slightly
             }
         });

         hidePlacementPreview(); // Hide preview on period change
    }

    // Event listener for period buttons
    periodButtons.forEach(button => {
        button.addEventListener('click', () => {
            changePeriod(button.dataset.period);
        });
    });

    // Event listener for map container mouse movement to update preview position
    mapContainer.addEventListener('mousemove', (event) => {
        if (!selectedBuilding) return; // No building selected

        const mapRect = mapElement.getBoundingClientRect();
        // Position relative to the map element, not container
        const mouseX = event.clientX - mapRect.left;
        const mouseY = event.clientY - mapRect.top;

        // Ensure mouse is within map bounds before showing/positioning
        if (mouseX >= 0 && mouseX <= mapRect.width && mouseY >= 0 && mouseY <= mapRect.height) {
             placementPreview.style.left = `${(mouseX / mapRect.width) * 100}%`;
             placementPreview.style.top = `${(mouseY / mapRect.height) * 100}%`;
             if (placementPreview.style.display === 'none') {
                 updatePlacementPreview(); // Show and style it if it was hidden
             }
        } else {
            hidePlacementPreview(); // Hide if mouse leaves map area
        }
    });

     // Hide preview if mouse leaves the map container entirely
     mapContainer.addEventListener('mouseleave', () => {
         hidePlacementPreview();
     });


    // Event listener for map clicks to place buildings
    mapElement.addEventListener('click', (event) => {
        if (!selectedBuilding) return; // Nothing selected to place

         // Check if the click was on the map background, not on an existing element
         // This is a basic check; more robust collision detection would be complex
         if (event.target !== mapElement && !event.target.classList.contains('base-element') && !event.target.classList.contains('placed-element')) {
             // The click was likely on the map background itself
         } else if (event.target !== mapElement) {
             // Clicked on an existing element, potentially do nothing or add future interaction
             console.log('Clicked on an existing element:', event.target);
             return; // Prevent placing if clicked directly on an element
         }


        // Calculate click position relative to the map div
        const mapRect = mapElement.getBoundingClientRect();
        const clickX = event.clientX - mapRect.left;
        const clickY = event.clientY - mapRect.top;

         // Create the new element
        const newElement = document.createElement('div');
        newElement.classList.add('placed-element', selectedBuilding.type);
        newElement.dataset.type = selectedBuilding.type;
        newElement.dataset.period = currentPeriod; // Mark which period it was placed in
        newElement.textContent = selectedBuilding.text; // Add short text label

        // Position the element (using percentage for responsiveness relative to map size)
        newElement.style.left = `${(clickX / mapRect.width) * 100}%`;
        newElement.style.top = `${(clickY / mapRect.height) * 100}%`;

        // Add to the map
        mapElement.appendChild(newElement);

         // Reset animation state to re-trigger on new element
         newElement.style.animation = 'none';
         newElement.offsetHeight; /* trigger reflow */
         // Check specific animation name based on type, default to placeElement
         const animationName = newElement.classList.contains('building-railway') ? 'placeRailway' :
                               newElement.classList.contains('building-planned-street') ? 'placeStreet' : 'placeElement';
         newElement.style.animation = `${animationName} 0.5s ease-out forwards`;


        // Update info panel with placing confirmation (optional but game-like)
         infoPanel.innerHTML = `<h2>הוספת אלמנט:</h2><p>העיר גדלה! נוסף <strong>${selectedBuilding.name}</strong>.</p>`;

         // Keep the building selected for easier repeated placement
         // Optionally, you could deselect here:
         // document.querySelectorAll('.building-option').forEach(opt => opt.classList.remove('selected'));
         // selectedBuilding = null;
         // hidePlacementPreview();
         // infoPanel.innerHTML = '<h2>לוח בקרה:</h2><p>לחצו על אלמנט לבנייה, ואז לחצו על המפה כדי להוסיף אותו לעיר.</p>';
         updatePlacementPreview(); // Ensure preview updates correctly if item remains selected

    });


     // Toggle explanation visibility
     toggleExplanationButton.addEventListener('click', () => {
         const isHidden = explanationDiv.style.display === 'none';
         explanationDiv.style.display = isHidden ? 'block' : 'none';
         toggleExplanationButton.textContent = isHidden ? 'הסתרת הסיפור המלא' : 'הצגת הסיפור המלא של העיר';
          // Scroll to explanation if showing
         if (isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth' });
         }
     });


    // Initial render
    changePeriod('medieval'); // Set initial period state and update controls/info

</script>