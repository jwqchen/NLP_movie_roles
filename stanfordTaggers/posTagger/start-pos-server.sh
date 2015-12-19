

cp lib/stanford-postagger-2014-08-27/stanford-postagger.jar \
   lib/stanford-postagger-2014-08-27/stanford-postagger-withModel.jar

mkdir -p edu/stanford/nlp/models/pos-tagger/english-bidirectional/
cp lib/stanford-postagger-2014-08-27/models/english-bidirectional-distsim.tagger \
   edu/stanford/nlp/models/pos-tagger/english-bidirectional/

jar -uf \
   lib/stanford-postagger-2014-08-27/stanford-postagger-withModel.jar \
   edu/stanford/nlp/models/pos-tagger/english-bidirectional/english-bidirectional-distsim.tagger

/usr/bin/java -mx1000m \
    -cp lib/stanford-postagger-2014-08-27/stanford-postagger-withModel.jar \
    edu.stanford.nlp.tagger.maxent.MaxentTaggerServer \
    -model edu/stanford/nlp/models/pos-tagger/english-bidirectional/english-bidirectional-distsim.tagger \
    -outputFormat        slashTags \
    -tokenizerOptions    "tokenizeNLs=false" \
    -outputFormatOptions keepEmptySentences \
    -encoding utf-8 -port 9001
    # -tokenizerFactory    edu.stanford.nlp.process.WhitespaceTokenizer \
    # -tokenize            false \
