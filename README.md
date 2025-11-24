# IPA transcribed Mayan language corpora (forked from [MayanV](https://github.com/transducens/mayanv))

Using the `epitran` module's transliterate function (see forked [epitran-mayan](https://github.com/cmykliz/epitran-mayan)) to re-transcribe the orthographical representations of mayan language words into the international phonetic alphabet (IPA), the entire MayanV corpora is presented here for phonological interest.

See the `transcriber.py` file for epitran-mayan transcription function.

```
# Example usage
langs = os.listdir('../mayanv-ipa/MayanV') # Get dirs
for lang in langs:
    dev_dir = os.path.join('../mayanv-ipa/MayanV', lang, 'dev')
    test_dir = os.path.join('../mayanv-ipa/MayanV', lang, 'test')
    filename = "data." + lang
    transcribe_file(os.path.join(dev_dir, filename))
    transcribe_file(os.path.join(test_dir, filename))
```
