// 1. Matching Digits (\d):
//    - \d matches any single digit (0-9).
let pattern = /\d/;

// 2. Matching Word Characters (\w = [a-zA-Z0-9_]):
//    - \w matches any word character, which includes letters, digits, and underscore.
pattern = /\w/;

// 3. Matching White Space (\s):
//    - \s matches any whitespace character, including spaces, tabs, and newlines.
pattern = /\s/;

// 4. Matching Email Addresses (Basic):
//    - [a-zA-Z0-9._%+-]+ matches the username part of the email address.
//    - @[a-zA-Z0-9.-]+ matches the @ symbol and the domain name.
//    - \.[a-zA-Z]{2,} matches the top-level domain (TLD) with at least two characters.
pattern = /[a-zA-Z0-9_.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/;

// 5. Matching URLs (Basic):
//    - (https?|ftp):// matches either "http", "https", or "ftp".
pattern = /(https?|ftp):\/\/[^\s/$.?#].[^\s]*/;

// 6. Matching Dates (MM/DD/YYYY format):
//    - ^ matches the start of the string.
//    - (0[1-9]|1[0-2]) matches the month in MM format (01-12).
//    - / matches the separator between month and day.
//    - (0[1-9]|[12][0-9]|3[01]) matches the day in DD format (01-31).
//    - / matches the separator between day and year.
//    - \d{4} matches the year in YYYY format (e.g., 2023).
//    - $ matches the end of the string.
pattern = /^(0[1-9]|1[0-2])\/(0[1-9]|[12][0-9]|3[01])\/\d{4}$/;

// 7. Matching Phone Numbers (U.S.):
//    - \d{3}-\d{3}-\d{4} matches the format XXX-XXX-XXXX for U.S. phone numbers.
pattern = /\d{3}-\d{3}-\d{4}/;

// 8. Matching HTML Tags (Basic):
//    - <[^>]+> matches any HTML tag, including its attributes.
pattern = /<[^>]+>/;

// 9. Matching IPv4 Addresses:
//    - (\d{1,3}\.){3} matches the first three parts of the IPv4 address (e.g., 192.168.1.).
//    - \d{1,3} matches the last part of the IPv4 address (e.g., 1).
pattern = /(\d{1,3}\.){3}\d{1,3}/;

// 10. Matching Zip Codes (U.S.):
//     - \d{5} matches the five-digit ZIP code.
//     - (-\d{4})? makes the last four digits optional (ZIP+4 format).
pattern = /\d{5}(-\d{4})?/;

// Note: These comments provide an explanation of what each regular expression does.
// You can modify and use them based on your specific text processing needs.

const demoReFunctions = () => {
    let testString = "Example string 123 with different 456 patterns 789.";

    // Key functions:

    // String.prototype.matchAll
    // Purpose: Finds all non-overlapping occurrences of the pattern in the string.
    // Input: Pattern (regex), string to search in.
    // Returns: Iterator over match objects.
    console.log("String.prototype.matchAll results:");
    for (const match of testString.matchAll(/\d+/g)) {
        console.log(" -", match[0]);
    }

    // String.prototype.replace
    // Purpose: Replaces occurrences of the pattern in the string with 'repl'.
    // Input: Pattern (regex), replacement string, string to perform replacement in.
    // Returns: Modified string.
    let subResult = testString.replace(/\d+/g, "#");
    console.log("String.prototype.replace result:", subResult);

    // String.prototype.replace (with function)
    // Purpose: Like replace, but returns a tuple of the modified string and the number of substitutions made.
    // Input: Pattern (regex), replacement function, string to perform replacement in.
    // Returns: Tuple (modified string, number of substitutions made).
    let subnResult = (() => {
        let count = 0;
        let result = testString.replace(/\d+/g, () => {
            count++;
            return "#";
        });
        return [result, count];
    })();
    console.log("String.prototype.replace with function result:", subnResult);

    // String.prototype.split
    // Purpose: Splits the string by occurrences of the pattern.
    // Input: Pattern (regex), string to split.
    // Returns: List of strings resulting from the split.
    let splitResult = testString.split(/\s+/);
    console.log("String.prototype.split result:", splitResult);

    // Other functions:

    // String.prototype.search
    // Purpose: Searches for the FIRST occurrence of the pattern in the string.
    // Input: Pattern (regex), string to search in.
    // Returns: Index of the first match if found; -1 otherwise.
    let searchResult = testString.search(/\d/);
    console.log("String.prototype.search result:", searchResult !== -1 ? testString[searchResult] : "No match");

    searchResult = testString.search(/\d+/);
    console.log("String.prototype.search result:", searchResult !== -1 ? testString.substring(searchResult, searchResult + testString.match(/\d+/)[0].length) : "No match");

    // String.prototype.match
    // Purpose: Matches the pattern at the BEGINNING of the string.
    // Input: Pattern (regex), string to match against.
    // Returns: Match object if the beginning of the string matches the pattern; null otherwise.
    let matchResult = testString.match(/^Example/);
    console.log("String.prototype.match result:", matchResult ? matchResult[0] : "No match");

    // String.prototype.match
    // Purpose: Checks if the entire string matches the pattern.
    // Input: Pattern (regex), string to match against.
    // Returns: Match object if the entire string matches; null otherwise.
    let fullMatchResult = testString.match(/^.*789\.$/);
    console.log("String.prototype.match (full) result:", fullMatchResult ? fullMatchResult[0] : "No match");

    // Creating a RegExp object for efficiency when used multiple times
    // Purpose: Compiles a regex pattern for repeated use.
    // Input: Pattern (regex).
    // Returns: Compiled regex object.
    let compiledPattern = /\d+/g;
    let compiledFindAllResult = Array.from(testString.matchAll(compiledPattern)).map(match => match[0]);
    console.log("Compiled pattern matchAll result:", compiledFindAllResult);

    // String.prototype.test
    // Purpose: Tests for a match in the string.
    // Input: Pattern (regex).
    // Returns: True if match is found, false otherwise.
    let testPattern = /\d+/;
    console.log("RegExp.prototype.test result:", testPattern.test(testString));

    // Other useful RegExp flags:
    // i - Ignore case
    // g - Global match
    // m - Multiline
    let caseInsensitivePattern = /example/i;
    let globalPattern = /\d+/g;
    let multilinePattern = /^pattern/m;

    console.log("Case-insensitive match:", caseInsensitivePattern.test("EXAMPLE string"));
    console.log("Global match:", testString.match(globalPattern));
    console.log("Multiline match:", "first line\npattern".match(multilinePattern));
};

demoReFunctions();
