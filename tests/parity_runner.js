#!/usr/bin/env node
"use strict";

// Reads a JSON array of {name, plan, bars} and prints the JS verdict for each,
// so test_parity.py can diff it against the Python state machine.
const fs = require("fs");
const path = require("path");
const LiveMath = require(path.join(__dirname, "..", "web", "live.js"));

const cases = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
const out = cases.map(function (testCase) {
  const result = LiveMath.evaluateSetup(testCase.plan, testCase.bars);
  return { status: result.status, event: Boolean(result.event) };
});
process.stdout.write(JSON.stringify(out));
