# CEFR-J

The file `cefrj.csv` is a modified version of the [CEFR-J Vocabulary Profile (ver 1.5)](https://github.com/openlanguageprofiles/olp-en-cefrj/blob/master/cefrj-vocabulary-profile-1.5.csv).

The RegEx replacement pattern `^([^\s\/]*)\/([^\s,]*)(.*)$` `$1$3\n$2$3` has been applied in order to have similar words on separate lines, instead of separated with slashes, for easier text matching.