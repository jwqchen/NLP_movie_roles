# start-nert-server.sh starts the nert server, run with "bash start-nert-server.sh"
# nertclient.py is client to the nert server, "import nertclient" in your main code

/usr/bin/java -mx1000m -cp \
    lib/stanford-ner-2014-08-27/stanford-ner-with-classifier.jar \
    edu.stanford.nlp.ie.NERServer \
    -loadClassifier lib/stanford-ner-2014-08-27/classifiers/english.all.3class.distsim.crf.ser.gz \
    -outputFormat slashTags \
    -tokenizerFactory edu.stanford.nlp.process.WhitespaceTokenizer \
    -tokenizerOptions "tokenizeNLs=false" \
    -encoding utf-8 -port 9000
