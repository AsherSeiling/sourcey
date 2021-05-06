import XCTest

import sourceyTests

var tests = [XCTestCaseEntry]()
tests += sourceyTests.allTests()
XCTMain(tests)
