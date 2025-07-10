// .eleventy.js
const { DateTime } = require("luxon");

module.exports = function(eleventyConfig) {
  // Passthrough copy for the css folder
  eleventyConfig.addPassthroughCopy("css");
  
  // Filter for formatting dates
  eleventyConfig.addFilter("date", (dateObj, format = "yyyy") => {
      if(dateObj === 'now') {
          return DateTime.now().toFormat(format);
      }
      return DateTime.fromJSDate(dateObj, {zone: 'utc'}).toFormat(format);
  });

  // ----> START OF NEW CODE <----
  // Custom filter to group items by a property
  eleventyConfig.addFilter("groupby", (arr, key) => {
    if (!arr) return [];
    const map = new Map();
    arr.forEach(item => {
      const k = item.data[key];
      const collection = map.get(k);
      if (!collection) {
        map.set(k, [item]);
      } else {
        collection.push(item);
      }
    });
    // Convert map to a more usable array of objects
    return Array.from(map, ([key, items]) => ({ key, items }));
  });
  // ----> END OF NEW CODE <----

  return {
    dir: {
      input: ".",
      includes: "_includes",
      output: "_site"
    }
  };
};