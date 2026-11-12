# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 restore_tracker.py sample_drills.csv
archive
test_flags_rto_miss (test_restore_tracker.RestoreTrackerTest) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
````
