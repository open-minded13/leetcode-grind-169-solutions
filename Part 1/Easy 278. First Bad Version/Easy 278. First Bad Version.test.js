const solution = require('./Easy 278. First Bad Version.js');

describe("solution", () => {

    test("single commit, broken", () => {
        const mockIsBrokenCommit = jest.fn(commit => commit >= 1);
        const findFirstBrokenCommit = solution(mockIsBrokenCommit);
        expect(findFirstBrokenCommit(1)).toBe(1);
    });

    test("single commit, not broken", () => {
        const mockIsBrokenCommit = jest.fn(false);
        const findFirstBrokenCommit = solution(mockIsBrokenCommit);
        expect(findFirstBrokenCommit(1)).toBe(2); // Return n+1 if there are no broken commits
    });

    test("two commits, first broken", () => {
        const mockIsBrokenCommit = jest.fn(commit => commit >= 1);
        const findFirstBrokenCommit = solution(mockIsBrokenCommit);
        expect(findFirstBrokenCommit(2)).toBe(1);
    });

    test("two commits, second broken", () => {
        const mockIsBrokenCommit = jest.fn(commit => commit >= 2);
        const findFirstBrokenCommit = solution(mockIsBrokenCommit);
        expect(findFirstBrokenCommit(2)).toBe(2);
    });

    test("multiple commits, first broken", () => {
        const mockIsBrokenCommit = jest.fn(commit => commit >= 1);
        const findFirstBrokenCommit = solution(mockIsBrokenCommit);
        expect(findFirstBrokenCommit(10)).toBe(1);
    });

    test("multiple commits, middle broken", () => {
        const mockIsBrokenCommit = jest.fn(commit => commit >= 5);
        const findFirstBrokenCommit = solution(mockIsBrokenCommit);
        expect(findFirstBrokenCommit(10)).toBe(5);
    });

    test("multiple commits, last broken", () => {
        const mockIsBrokenCommit = jest.fn(commit => commit >= 10);
        const findFirstBrokenCommit = solution(mockIsBrokenCommit);
        expect(findFirstBrokenCommit(10)).toBe(10);
    });

    test("multiple commits, none broken", () => {
        const mockIsBrokenCommit = jest.fn(false);
        const findFirstBrokenCommit = solution(mockIsBrokenCommit);
        expect(findFirstBrokenCommit(10)).toBe(11); // Return n+1 if there are no broken commits
    });

    test("large number of commits, early broken", () => {
        const mockIsBrokenCommit = jest.fn(commit => commit >= 1); // Break on 1st call
        const findFirstBrokenCommit = solution(mockIsBrokenCommit);
        expect(findFirstBrokenCommit(1000)).toBe(1);
    });

    test("large number of commits, late broken", () => {
        const mockIsBrokenCommit = jest.fn(commit => commit >= 1000);
        const findFirstBrokenCommit = solution(mockIsBrokenCommit);
        expect(findFirstBrokenCommit(1000)).toBe(1000);
    });
});


