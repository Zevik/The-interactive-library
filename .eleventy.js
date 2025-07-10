// .eleventy.js
const { DateTime } = require("luxon");

module.exports = function(eleventyConfig) {
  // Passthrough copy for the css folder
  eleventyConfig.addPassthroughCopy("css");
  
  eleventyConfig.addFilter("date", (dateObj, format = "yyyy") => {
      // 'now' will be a string, so we create a new Date object from it
      if(dateObj === 'now') {
          return DateTime.now().toFormat(format);
      }
      return DateTime.fromJSDate(dateObj, {zone: 'utc'}).toFormat(format);
  });

  return {
    dir: {
      input: ".",
      includes: "_includes",
      output: "_site"
    }
  };
};